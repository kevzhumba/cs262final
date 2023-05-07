package cfg

import org.opalj.br.DeclaredMethod
import org.opalj.br.analyses.Project
import org.opalj.br.cfg.{BasicBlock, CFGNode, CatchNode, ExitNode}
import org.opalj.tac.{DUVar, Stmt, Var}
import org.opalj.value.ValueInformation

import scala.collection.immutable.List

/** Class representing a node of a CFG
  */
trait CfgNode {
  def method: MethodDescription

  def isCallRet: Boolean = false

  def isEntry: Boolean = false

  def isExit: Boolean = false

  def instructions: List[StmtNode]

  def id: Int
}

case class BBNode(
    method: MethodDescription,
    instructions: List[StmtNode],
    id: Int
) extends CfgNode
