package dataflow

import analyses.{Analysis, ConstantPropagationAnalysis}
import cfg._
import io.grpc.netty.{NettyChannelBuilder, NettyServerBuilder}
import lattice._
import org.json4s._
import org.json4s.native.Serialization
import org.json4s.native.Serialization.{read, write}
import protos.dataflow._

import java.net.InetSocketAddress
import java.util.concurrent.atomic.AtomicBoolean
import java.util.concurrent.{ConcurrentHashMap, ConcurrentMap}
import scala.collection.mutable
import scala.concurrent.{ExecutionContext, Future}
import scala.util.control.Breaks.{break, breakable}


case class ComputationUnit(
                            cfg: ExplodedCfg,
                            analysis: String,
                            methods: List[(MethodDescription, String, Int)])

class Machine(val host: String, val port: Int) {
  //TODO A

  implicit val formats = Serialization.formats(
    ShortTypeHints(
      List(
        classOf[BBNode],
        classOf[BBEntryNode],
        classOf[ExNode],
        classOf[CRNode]))) +
    new StmtSerializer() + new ExprSerializer() + new FieldTypeSerializer()
  // Machine state
  //Local state
  val in: ConcurrentMap[CfgNode, Value] = new ConcurrentHashMap()
  val out: ConcurrentMap[CfgNode, Value] = new ConcurrentHashMap()

  //Points to state: these should be allocation sites that were allocated in this method
  val pointsTo: ConcurrentMap[(AllocationSite, String), (lattice.Integer, AbstractObject)] = new ConcurrentHashMap()
  //Map from allocation site to reader? hmmmm that seems reasonable

  var method: MethodDescription = null
  var cfg: ExplodedCfg = null
  var change: Boolean = true
  var waiting: AtomicBoolean = new AtomicBoolean(false)
  val heartBeat: AtomicBoolean = new AtomicBoolean(false)
  var methodStubs: Map[MethodDescription,  DataflowServerGrpc.DataflowServerBlockingStub] = Map()
  var valueOperator: ValueOperator = null
  var analysis: Analysis = null
  val endFlag: AtomicBoolean = new AtomicBoolean(false)
  val readers: ConcurrentMap[(AllocationSite, String), Set[MethodDescription]] = new ConcurrentHashMap()

  private class MachineServer extends protos.dataflow.DataflowServerGrpc.DataflowServer {
    override def getField(request: GetFieldRequest): Future[GetFieldResponse] = {
      val alloc = read[AllocationSite](request.allocSite)
      val value = pointsTo.getOrDefault((alloc, request.field), analysis.defaultFieldValue)
      val method = read[MethodDescription](request.requestingMethod)
      readers.compute((alloc, request.field), (k, v) => if (v == null) Set(method) else v + method)
      val json = write(value)
      Future.successful(GetFieldResponse(json))
    }

    override def putField(request: PutFieldRequest): Future[PutFieldResponse] = {
      val value = read[(lattice.Integer, AbstractObject)](request.value)
      val allocationSite = read[AllocationSite](request.allocSite)
      val field = request.field
      pointsTo.compute(
        (allocationSite, field),
        (k, v) => if (v == null) ConstantOperator.joinTuples(value, analysis.defaultFieldValue) else ConstantOperator.joinTuples(v, value))
      readers.getOrDefault((allocationSite, field), Set()).foreach(m => methodStubs(m).setTrigger(SetTriggerRequest()))
      Future.successful(PutFieldResponse())
    }

    override def getHeartbeat(request: GetHeartbeatRequest): Future[GetHeartbeatResponse] = { //TODO make this more robust
      Future.successful(GetHeartbeatResponse(heartBeat.get()))
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

    override def shutDown(request: ShutDownRequest): Future[ShutDownResponse] = {
      var map: Map[Int, Value] = Map()
      for (node <- cfg.nodes) {
        val lattice = out.get(node)
        map += (node.id -> lattice.asInstanceOf[Constant])
      }
      val json = write(map)
      endFlag.set(true)
      println(pointsTo)
      Future.successful(ShutDownResponse("constant", json))
    }
  }

  def initialize(unit: ComputationUnit): Unit = {
    for (method <- unit.methods) {
      val channel = NettyChannelBuilder.forAddress(method._2, method._3).usePlaintext().build
      val blockingStub = DataflowServerGrpc.blockingStub(channel)
      methodStubs += (method._1 -> blockingStub)
    }
    if (unit.analysis.equals("constant")) {
      analysis = ConstantPropagationAnalysis
      valueOperator = ConstantOperator
    }
    println(unit.cfg._callers)
    println(unit.cfg._callees)
    val initial = analysis.initialValue(unit.cfg)
    for (node <- unit.cfg.nodes) {
      in.put(node, initial)
      out.put(node, initial)
    }
    cfg = unit.cfg
    method = cfg.entry.method
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
    breakable {
      while (true) {
        if (!waiting.getAndSet(true)) {
          change = true
          heartBeat.set(false)
          converge(rpo)
          heartBeat.set(true)
        }
        if (endFlag.get()) {
          break()
        }
      }
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
        val inFact = node match {
          case node: BBNode => computeInForBBNode(node)
          case node: CRNode => computeInForCrNode(node)
          case node: ExNode => computeInForExitNode(node)
          case node: BBEntryNode => computeInForBBEntryNode(node)
          case _ => throw new RuntimeException()
        }
        in.put(node, inFact)
        val outFact = node.instructions.foldLeft[Value](inFact)((v, s) => analysis.transfer(s,v, methodStubs))
        if (!outFact.equals(out.get(node))) {
          out.put(node, outFact)
          change = true
          for (callee <- getCallees(node)) {
            methodStubs(callee).setTrigger(SetTriggerRequest())
          }
          if (node.isExit) {
            for (method <- cfg._callers) {
              methodStubs(method._2).setTrigger(SetTriggerRequest())
            }
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
      val response = methodStubs(callee).getCalleeInfo(req)
      val ret = read[Constant](response.payload)
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
      val stub = methodStubs(caller._2)
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
