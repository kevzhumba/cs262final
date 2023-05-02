package cfg

import cfg.StmtUtil.translateStmt
import org.opalj.br.DeclaredMethod
import org.opalj.br.cfg.{BasicBlock, CFGNode, CatchNode, ExitNode}
import org.opalj.tac.DUVar
import org.opalj.tac.Stmt
import org.opalj.value.ValueInformation

import scala.collection.mutable

object CfgNodeFactory {
  val hashCons: mutable.HashMap[Key, CfgNode] = mutable.HashMap()

  var counter = 0

  type Key = (Option[CFGNode], MethodDescription, Boolean, Boolean)

  def createNode(
                  node: Option[CFGNode], 
                  method: MethodDescription, 
                  isCallRet: Boolean = false, 
                  isExit: Boolean = false,
                  unrwrapinstructions: List[Stmt[DUVar[ValueInformation]]] = List()): CfgNode = {
    val key = (node, method, isCallRet, isExit)
    if (hashCons.contains(key)) {
//      println("Existing node")
      hashCons(key)
    } else {
      val ret = node match {
        case Some(value) => value match {
          case block: BasicBlock =>
            if (isCallRet) {
              val instructions = unrwrapinstructions.zipWithIndex
                .map(s =>
                  StmtNode(
                    translateStmt(s._1),
                    method,
                    isCallRet,
                    counter,
                    s._2 + value.asBasicBlock.endPC)
                )
              CRNode(method, instructions, counter)
            }
            else if (block.startPC == 0) {
              val instructions = unrwrapinstructions.zipWithIndex
                .map(s =>
                  StmtNode(
                    translateStmt(s._1),
                    method,
                    isCallRet,
                    counter,
                    s._2 + value.asBasicBlock.startPC)
                )
              BBEntryNode(method, instructions, counter)
            }
            else {
              val instructions = unrwrapinstructions.zipWithIndex
                .map(s =>
                  StmtNode(
                    translateStmt(s._1),
                    method,
                    isCallRet,
                    counter,
                    s._2 + value.asBasicBlock.startPC)
                )
              if (instructions.isEmpty) {
                throw new RuntimeException()
              }
              BBNode(method, instructions, counter)
            }
          case node: ExitNode => ExNode(node.isNormalReturnExitNode, method, List(), counter)
        }
      }
      counter = counter + 1
//      println("New node")
//      println(hashCons)
//      println(node)
//      println(method)
//      println(isCallRet)
//      println(isExit)
      hashCons.put(key, ret)
      ret
    }
  }
}
