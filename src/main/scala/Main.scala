import cfg.{Assignment, BBEntryNode, BBNode, BinExpr, BinOps, CRNode, CfgNode, CfgProcessor, ExNode, ExplodedCfg, Expr, ExprSerializer, ExprStmt, FieldTypeSerializer, Goto, If, IntConstant, MethodDescription, NonVirtualFunctionCall, Nop, PutField, Return, StaticFunctionCall, StaticMethodCall, Stmt, StmtSerializer, TACGenerator, Var, VirtualFunctionCall}
import cli.CliParser
import dataflow.{ComputationUnit, Machine}
import io.grpc.netty.NettyChannelBuilder
import org.json4s.{DefaultFormats, FieldSerializer, ShortTypeHints}
import org.json4s.native.Serialization
import org.json4s.native.Serialization.{read, write}
import org.opalj.br.ObjectType
import org.opalj.tac.cg.CFA_1_1_CallGraphKey
import protos.dataflow.{DataflowServerGrpc, GetHeartbeatRequest, ReceiveComputationUnitRequest}
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
      for ((method, idx) <- methods.zipWithIndex) {
        val port = 6000 + idx
        val prog = cfg(method)
        val calleePorts = prog._callees.flatMap(_._2).distinct.map[(MethodDescription, String, Int)](m => (m, "127.0.0.1", methods.indexOf(m) + 6000))
        val callerPorts = prog._callers.map(_._2).map(m => (m, "127.0.0.1", methods.indexOf(m) + 6000))
        val unit = ComputationUnit(prog, "constant", calleePorts, callerPorts)
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
      while(true) {

      }
      // println(PrettyPrinter.prettyPrint(cfg.successors))
    case None =>
  }

}