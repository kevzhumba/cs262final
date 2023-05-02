package dataflow

import analyses.{Analysis, ConstantPropagationAnalysis}
import cfg.{BBEntryNode, BBNode, CRNode, CfgNode, ExNode, ExplodedCfg, ExprSerializer, FieldTypeSerializer, MethodDescription, StmtSerializer}
import io.grpc.ServerBuilder
import io.grpc.netty.{NettyChannelBuilder, NettyServerBuilder}
import lattice.{Constant, ConstantOperator, Value, ValueOperator}
import org.opalj.br.DeclaredMethod
import org.opalj.br.cfg.CFG
import org.opalj.tac.fpcf.properties.cg.Callers
import protos.dataflow.{DataflowServerGrpc, GetCalleeInfoRequest, GetCalleeInfoResponse, GetCallerInfoRequest, GetCallerInfoResponse, GetHeartbeatRequest, GetHeartbeatResponse, ReceiveComputationUnitRequest, ReceiveComputationUnitResponse, SetTriggerRequest, SetTriggerResponse}

import scala.collection.mutable
import scala.concurrent.{ExecutionContext, Future}
import org.json4s._
import org.json4s.DefaultFormats
import org.json4s.native.Serialization
import org.json4s.native.Serialization.{read, write}

import java.net.InetSocketAddress
import java.util.concurrent.atomic.AtomicBoolean
import java.util.concurrent.{ConcurrentHashMap, ConcurrentMap}

case class DataflowProblem[V <: Value](analysis: Analysis)

case class ComputationUnit(
                            cfg: ExplodedCfg,
                            analysis: String,
                            callees: List[(MethodDescription, String, Int)],
                            callers: List[(MethodDescription, String, Int)])

class Machine(val host: String, val port: Int) {

  implicit val formats = Serialization.formats(
    ShortTypeHints(
      List(
        classOf[BBNode],
        classOf[BBEntryNode],
        classOf[ExNode],
        classOf[CRNode]))) +
    new StmtSerializer() + new ExprSerializer() + new FieldTypeSerializer()

  val in: ConcurrentMap[CfgNode, Value] = new ConcurrentHashMap()
  val out: ConcurrentMap[CfgNode, Value] = new ConcurrentHashMap()
  var method: MethodDescription = null
  var cfg: ExplodedCfg = null
  var change: Boolean = true
  var waiting: AtomicBoolean = new AtomicBoolean(false)
  val calleeStubs: ConcurrentMap[MethodDescription,  DataflowServerGrpc.DataflowServerBlockingStub] = new ConcurrentHashMap()
  val callerStubs: ConcurrentMap[MethodDescription,  DataflowServerGrpc.DataflowServerBlockingStub] = new ConcurrentHashMap()
  var valueOperator: ValueOperator = null
  var analysis: Analysis = null

  private class MachineServer extends protos.dataflow.DataflowServerGrpc.DataflowServer {

    override def getHeartbeat(request: GetHeartbeatRequest): Future[GetHeartbeatResponse] = {
      Future.successful(GetHeartbeatResponse(waiting.get() && !change))
    }

    override def getCallerInfo(request: GetCallerInfoRequest): Future[GetCallerInfoResponse] = {
      val lattice = request.lattice
      val idx = request.caller
      if (lattice.equals("constant")) {
        val node = cfg.nodes.find(n => !n.isCallRet  && n.instructions.exists(s => s.idx == idx)).get //this is the caller node
        println("I AM GETTING ARGS " + port)
        println(out.get(node))
        val latticeElem = valueOperator.getArgs(out.get(node)) //this ensures only arguments are passed
        //Need to filter args somehow or something? add this later.
        val json = write(latticeElem)
        Future.successful(GetCallerInfoResponse(lattice, json))
      } else {
        throw new RuntimeException("Not constant")
      }
    }

    override def receiveComputationUnit(request: ReceiveComputationUnitRequest): Future[ReceiveComputationUnitResponse] = {
      if (method == null && cfg == null) {
        val unit = read[ComputationUnit](request.computationunit)
        initialize(unit)
      }
      Future.successful(ReceiveComputationUnitResponse())
   }

    override def getCalleeInfo(request: GetCalleeInfoRequest): Future[GetCalleeInfoResponse] = {
      val lattice = request.lattice
      if (lattice.equals("constant")) {
        val latticeElem = valueOperator.getRet(out.get(cfg.nodes.find(p => p.isExit && p.asInstanceOf[ExNode].isNormalReturn).get)) //this should give only return information
        val json = write(latticeElem)
        Future.successful(GetCalleeInfoResponse(lattice, json))
      } else {
        throw new RuntimeException("Not Constant")
      }
    }

    override def setTrigger(request: SetTriggerRequest): Future[SetTriggerResponse] = {
      waiting.set(false)
      Future.successful(SetTriggerResponse())
    }
  }

  def initialize(unit: ComputationUnit): Unit = {
    cfg = unit.cfg
    method = cfg.entry.method
    for (callee <- unit.callees) {
      val channel = NettyChannelBuilder.forAddress(callee._2, callee._3).usePlaintext().build
      val blockingStub = DataflowServerGrpc.blockingStub(channel)
      calleeStubs.put(callee._1, blockingStub)
    }
    for (caller <- unit.callers) {
      val channel = NettyChannelBuilder.forAddress(caller._2, caller._3).usePlaintext().build
      val blockingStub = DataflowServerGrpc.blockingStub(channel)
      callerStubs.put(caller._1, blockingStub)
    }
    if (unit.analysis.equals("constant")) {
      analysis = ConstantPropagationAnalysis
      valueOperator = ConstantOperator
    }
    println(cfg._callers)
    println(cfg._callees)
    val initial = analysis.initialValue(cfg)
    for (node <- cfg.nodes) {
      in.put(node, initial)
      out.put(node, initial)
    }
  }

  def run(): Unit = {
    val serverThread = new Thread {
      override def run(): Unit = startServer()
    }
    serverThread.start()
    while (cfg == null || method == null) {
      println("Waiting")
      Thread.sleep(1000) //wait until we have gotten the stuff from the client
    }
    Thread.sleep(5000)
    handleComputation()
  }

  def startServer(): Unit = {
    val server = NettyServerBuilder.forAddress(new InetSocketAddress(host, port))
      .addService(DataflowServerGrpc.bindService(new MachineServer, ExecutionContext.global))
      .build
    server.start
    server.awaitTermination()
  }

  def handleComputation() = {
    val rpo = reversePostOrder(cfg)
    while (true) {
      if (!waiting.getAndSet(true)) {
        change = true
        converge(rpo)
      }
      Thread.sleep(500)
    }
  }

  def getCallees(node: CfgNode): List[MethodDescription] = {
    if (node.isExit || node.isCallRet) {
      List()
    } else {
      val indices = node.instructions.map(s => s.idx)
      var result: List[MethodDescription] = List()
      for (callee <- cfg._callees) {
        if (indices.contains(callee._1)) {
          result = result ++ callee._2
        }
      }
      result
    }
  }

  def converge(rpo: List[CfgNode]) = {
    while (change) {
      change = false
      for (node <- rpo) {
        println("Machine " + port + " processing node " + node.toString)
        val inFact = node match {
          case node: BBNode => computeInForBBNode(node)
          case node: CRNode => computeInForCrNode(node)
          case node: ExNode => computeInForExitNode(node)
          case node: BBEntryNode => computeInForBBEntryNode(node)
          case _ => throw new RuntimeException()
        }
        println(inFact)
        in.put(node, inFact)
        val outFact = node.instructions.foldLeft[Value](inFact)((v, s) => analysis.transfer(s,v))
        println(outFact)
        println(out.get(node))
        if (!outFact.equals(out.get(node))) {
          println("CHANGED")
          out.put(node, outFact)
          change = true
          for (callee <- getCallees(node)) {
            calleeStubs.get(callee).setTrigger(SetTriggerRequest())
          }
          if (node.isExit) {
            callerStubs.forEach((k,v) => v.setTrigger(SetTriggerRequest()))
          }
        }
      }
    }
  }

  def computeInForCrNode(node: CRNode): Value = {
    val callNode =
      cfg.getPredecessors(node).find(p => p.isInstanceOf[BBEntryNode] || p.isInstanceOf[BBNode]).get
    val indices = node.instructions.map(_.idx)
    val callees = cfg._callees.find(c => indices.contains(c._1)).get._2
    //For each callee, get the things and join them
    var running: Option[Value] = None
    for (callee <- callees) {
      val req = GetCalleeInfoRequest("constant")
      val response = calleeStubs.get(callee).getCalleeInfo(req)

      val ret = read[Constant](response.payload)
      println("GETTING RETURN INFO")
      println(ret)
      running match {
        case Some(value) => running = Some(valueOperator.join(value, ret))
        case None => running = Some(ret)
      }
    }
    valueOperator.addRetInformation(running.get,valueOperator.restoreLocal(out.get(callNode)))
  }

  def computeInForExitNode(node: ExNode): Value = {
    var running: Option[Value] = None
    for (pred <- cfg.getPredecessors(node)) {
      val predRet = valueOperator.getRet(out.get(pred))
      running match {
        case Some(value) => running = Some(valueOperator.join(value, predRet))
        case None => running = Some(predRet)
      }
    }
    running.get
  }

  def computeInForBBNode(node: BBNode): Value = {
    var running: Option[Value] = None
    println(cfg.getPredecessors(node))
    for (pred <- cfg.getPredecessors(node)) {
      println(pred)
      println(out.get(pred))
      val predL = valueOperator.restoreLocal(out.get(pred))
      running match {
        case Some(value) => running = Some(valueOperator.join(value, predL))
        case None => running = Some(predL)
      }
    }
    running.get
  }

  def computeInForBBEntryNode(node: BBEntryNode): Value = {
    var running: Option[Value] = None
    for (caller <- cfg._callers) {
      //TODO add handling if we can't get the thing(If it goes down ig)
      //The callers should just give us argument information
      val req = GetCallerInfoRequest("constant", caller._1)
      val stub = callerStubs.get(caller._2)
      val response = stub.getCallerInfo(req)
      val constant = read[Constant](response.payload)
      running match {
        case Some(value) => running = Some(valueOperator.join(value, constant))
        case None => running = Some(constant)
      }
    }
    println("ENTRYNODE")
    println(running)
    if (running.isEmpty) {
      in.get(node)
    } else {
      valueOperator.bindParams(running.get, in.get(node), method.isStatic)
    }
  }

  def reversePostOrder(cfg: ExplodedCfg): List[CfgNode] = {
    val resultStack: mutable.Stack[CfgNode] = new mutable.Stack()
    val interStack: mutable.Stack[(CfgNode, Boolean)] = new mutable.Stack()
    var visitedSet: Set[CfgNode] = Set()
    interStack.push((cfg.entry, false))
    while (!interStack.isEmpty) {
      val popped = interStack.pop()
      val (current, status) = popped
      if (status) {
        resultStack.push(current)
      } else if (!visitedSet.contains(current)) {
        visitedSet += current
        interStack.push((current, true))
        val successors = cfg.getSuccessors(current)
          for (succ <- successors) {
            if (!visitedSet.contains(succ)) { //Since we already visited call return, should be fine here
              interStack.push((succ, false))
            }
          }
      }
    }
    resultStack.toList
  }


}
