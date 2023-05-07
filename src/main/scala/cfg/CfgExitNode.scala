package cfg

import org.opalj.br.DeclaredMethod
import org.opalj.br.analyses.Project
import org.opalj.br.cfg.CFGNode

/** Class representing an exit node of a CFG
  */
case class ExNode(
    isNormalReturn: Boolean,
    method: MethodDescription,
    instructions: List[StmtNode],
    id: Int
) extends CfgNode {
  override def isExit: Boolean = true
}
