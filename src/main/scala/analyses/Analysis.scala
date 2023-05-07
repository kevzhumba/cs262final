package analyses

import cfg.{ExplodedCfg, MethodDescription, StmtNode}
import lattice.{AbstractObject, Value}
import protos.dataflow.DataflowServerGrpc

/** Base trait for all analyses
  */
trait Analysis {

  def initialValue(cfg: ExplodedCfg): Value

  def topValue: Value

  def botValue: Value

  def defaultFieldValue: (lattice.Integer, AbstractObject)

  def transfer(
      stmtNode: StmtNode,
      in: Value,
      stubs: Map[
        MethodDescription,
        DataflowServerGrpc.DataflowServerBlockingStub
      ]
  ): Value

}
