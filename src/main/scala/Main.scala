import cfg._
import cli.CliParser
import dataflow.{ComputationUnit, Machine}
import io.grpc.netty.NettyChannelBuilder
import lattice.Constant
import org.json4s.ShortTypeHints
import org.json4s.native.Serialization
import org.json4s.native.Serialization.{read, write}
import org.opalj.tac.cg.CFA_1_1_CallGraphKey
import protos.dataflow.DataflowServerGrpc.DataflowServerBlockingStub
import protos.dataflow.{
  DataflowServerGrpc,
  GetHeartbeatRequest,
  ReceiveComputationUnitRequest,
  ShutDownRequest
}

object Main extends App {
  // Set up JSON serialization formats
  implicit val formats = Serialization.formats(
    ShortTypeHints(
      List(
        classOf[BBNode],
        classOf[BBEntryNode],
        classOf[ExNode],
        classOf[CRNode]
      )
    )
  ) +
    new StmtSerializer() + new ExprSerializer() + new FieldTypeSerializer()

  // Parse command line arguments
  val argConfig = CliParser.parseArgs(args)
  argConfig match {
    case Some(value) =>
      if (value.worker) {
        runWorkerMachine(value.host, value.port)
      } else {
        // Load Java project and construct control flow graph
        implicit val p = JavaLoader.loadJavaProject(value.project)
        val callGraph = p.get(CFA_1_1_CallGraphKey)
        // Generate three address code for all reachable methods
        val tac = TACGenerator(callGraph.reachableMethods().map(_.method).toSet)
        if (value.generate_tac) {
          tac.printToFile(value.out)
        }
        println("Constructing CFG")
        val cfg = CfgProcessor.buildIntraproceduralCFG(callGraph, tac)
        runMainMachine(cfg, value.machines)
      }
    case None =>
  }

  def runWorkerMachine(host: String, port: Int): Unit = {
    val machine = new Machine(host, port)
    machine.run()
  }

  /** Starts worker machines on localhost with ports 6000, 6001, ... Assigns
    * each worker machine a computation unit corresponding to a method in the
    * control flow graph.
    *
    * @param cfg
    *   Map of method descriptions to exploded control flow graphs
    * @return
    *   List of tuples of worker machines and their computation units
    */
  def startWorkerMachines(
      cfg: Map[MethodDescription, ExplodedCfg],
      workerMachines: List[(String, Int)]
  ): List[(Machine, ComputationUnit)] = {
    val methods = cfg.keys.toList.sortBy(f => cfg(f).nodes.size).reverse
    var machines: List[(Machine, ComputationUnit)] = List()
    var nonLocalMachines: List[(Machine, ComputationUnit)] = List()
    val methodPorts = methods.zipWithIndex.map(m => {
      if (m._2 < workerMachines.size) {
        (m._1, workerMachines(m._2)._1, workerMachines(m._2)._2)
      } else {
        (m._1, "127.0.0.1", methods.indexOf(m._1) + 6000)
      }
    } )

    for ((method, idx) <- methods.zipWithIndex) {
      val port = 6000 + idx
      val prog = cfg(method)
      val unit = ComputationUnit(prog, "constant", methodPorts)
      if (idx < workerMachines.size) {
        val (host1, port1) = workerMachines(idx)
        val machine = new Machine(host1, port1)
        nonLocalMachines = nonLocalMachines ++ List((machine, unit))
      } else {
        val machine = new Machine("127.0.0.1", port)
        machines = machines ++ List((machine, unit))
      }
    }

    for ((machine, unit) <- machines) {
      val machineThread = new Thread {
        override def run(): Unit = machine.run()
      }
      machineThread.start()
    }
    nonLocalMachines ++ machines
  }

  /** Sends heartbeat requests to all worker machines until they have all
    * converged
    *
    * @param stubs
    *   List of grpc stubs for worker machines
    */
  def getHeartbeatRequests(stubs: List[DataflowServerBlockingStub]): Unit = {
    var i = 0
    while (i < 5) {
      if (
        stubs.forall(stub => stub.getHeartbeat(GetHeartbeatRequest()).converged)
      ) {
        i = i + 1
      } else {
        i = 0
      }
      Thread.sleep(1000)
    }
  }

  /** Starts worker machines and sends them computation units corresponding to
    * methods in the control flow graph. Sends heartbeat requests to all worker
    * machines until they have all converged. Shuts down all worker machines and
    * prints the results.
    *
    * @param cfg
    *   Map of method descriptions to exploded control flow graphs
    * @param otherMachines
    *   List of tuples of hostnames and ports of other worker machines
    */
  def runMainMachine(
      cfg: Map[MethodDescription, ExplodedCfg],
      otherMachines: List[(String, Int)]
  ): Unit = {
    val methods = cfg.keys.toList
    println(otherMachines)
    val machines = startWorkerMachines(cfg, otherMachines)
    var stubs: List[DataflowServerBlockingStub] = List()
    for ((machine, unit) <- machines) {
      val channel = NettyChannelBuilder
        .forAddress(machine.host, machine.port)
        .usePlaintext()
        .build
      val blockingStub = DataflowServerGrpc.blockingStub(channel)
      val json = write(unit)
      stubs = stubs ++ List(blockingStub)
      blockingStub.receiveComputationUnit(ReceiveComputationUnitRequest(json))
    }
    getHeartbeatRequests(stubs)
    val results = stubs.map(stub => stub.shutDown(ShutDownRequest()).payload)
    val map = results.map(json => read[Map[Int, Constant]](json))
  }

}
