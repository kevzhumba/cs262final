package cfg

import org.opalj.br.DeclaredMethod
import org.opalj.br.analyses.Project
import org.opalj.br.cfg.{BasicBlock, CFGNode}
import org.opalj.tac.{Checkcast, DUVar, Stmt}
import org.opalj.value.ValueInformation


case class BBEntryNode(method: MethodDescription, instructions: List[StmtNode], id: Int) extends CfgNode {
  override def isEntry: Boolean = true
}


