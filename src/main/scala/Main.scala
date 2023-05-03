import cfg.{Assignment, BBEntryNode, BBNode, BinExpr, BinOps, CRNode, CfgNode, CfgProcessor, ExNode, ExplodedCfg, Expr, ExprSerializer, ExprStmt, FieldTypeSerializer, Goto, If, IntConstant, MethodDescription, NonVirtualFunctionCall, Nop, PutField, Return, StaticFunctionCall, StaticMethodCall, Stmt, StmtSerializer, TACGenerator, Var, VirtualFunctionCall}
import cli.CliParser
import dataflow.{ComputationUnit, Machine}
import io.grpc.netty.NettyChannelBuilder
import lattice.Constant
import org.json4s.{DefaultFormats, FieldSerializer, ShortTypeHints}
import org.json4s.native.Serialization
import org.json4s.native.Serialization.{read, write}
import org.opalj.br.ObjectType
import org.opalj.tac.cg.CFA_1_1_CallGraphKey
import protos.dataflow.{DataflowServerGrpc, GetHeartbeatRequest, ReceiveComputationUnitRequest, ShutDownRequest}
import protos.dataflow.DataflowServerGrpc.{DataflowServerBlockingStub, stub}


object Main extends App {
  implicit val formats = Serialization.formats(
    ShortTypeHints(
      List(
        classOf[BBNode],
        classOf[BBEntryNode],
        classOf[ExNode],
        classOf[CRNode]))) +
    new StmtSerializer() + new ExprSerializer() + new FieldTypeSerializer()

  val argConfig = CliParser.parseArgs(args)
  argConfig match {
    case Some(value) =>
      implicit val p = JavaLoader.loadJavaProject(value.project)
      //println(p.config.getStringList("org.opalj.tac.cg.CallGraphKey.modules"))
      val callGraph = p.get(CFA_1_1_CallGraphKey)
      val tac = TACGenerator(callGraph.reachableMethods().map(_.method).toSet)
      if (value.generate_tac) {
        tac.printToFile(value.out)
      }
      println("Constructing CFG")
      val cfg = CfgProcessor.buildIntraproceduralCFG(callGraph, tac)
      val methods = cfg.keys.toList
      var machines: List[(Machine, ComputationUnit)] = List()
      val methodPorts = methods.map(m => (m, "127.0.0.1", methods.indexOf(m) + 6000))
      for ((method, idx) <- methods.zipWithIndex) {
        val port = 6000 + idx
        val prog = cfg(method)
        val unit = ComputationUnit(prog, "constant", methodPorts)
        val machine = new Machine("127.0.0.1", port)
        machines = machines ++ List((machine, unit))
      }
      var stubs: List[DataflowServerBlockingStub] = List()
      for ((machine, unit) <- machines) {
        val machineThread = new Thread {
          override def run(): Unit = machine.run()
        }
        machineThread.start()
      }

      for ((machine, unit) <- machines) {
        val channel = NettyChannelBuilder.forAddress(machine.host, machine.port).usePlaintext().build
        val blockingStub = DataflowServerGrpc.blockingStub(channel)
        val json = write(unit)
        stubs = stubs ++ List(blockingStub)
        blockingStub.receiveComputationUnit(ReceiveComputationUnitRequest(json))
      }
      var i = 0
      while(i < 5) {
        if (stubs.forall(stub => stub.getHeartbeat(GetHeartbeatRequest()).converged)){
          i = i + 1
        } else {
          i = 0
        }
        Thread.sleep(1000)
      }
      val results = stubs.map(stub => stub.shutDown(ShutDownRequest()).payload)
      val map = results.map(json => read[Map[Int,Constant]](json))
      for (i <- map.indices) {
        println(methods(i))
        println(map(i).map(p => (cfg(methods(i)).nodes.find(n => n.id == p._1).get, p._2)))
      }
      // println(PrettyPrinter.prettyPrint(cfg.successors))
    case None =>
  }

}