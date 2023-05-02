package cfg

import org.opalj.br.DeclaredMethod
import org.opalj.br.analyses.Project
import org.opalj.br.cfg.{BasicBlock, CFGNode}
import org.opalj.tac.{DUVar, Stmt}
import org.opalj.value.ValueInformation

import java.math.BigInteger

case class CRNode(method: MethodDescription, instructions: List[StmtNode], id: Int) extends CfgNode {
  override def isCallRet: Boolean = true
}


