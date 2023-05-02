package analyses

import cfg.{ ExplodedCfg, MethodDescription, StmtNode}
import lattice.Value
import org.opalj.br.analyses.Project


trait Analysis {

  def initialValue(cfg: ExplodedCfg): Value

  def topValue: Value

  def botValue: Value

  def transfer(stmtNode: StmtNode, in: Value): Value

}
