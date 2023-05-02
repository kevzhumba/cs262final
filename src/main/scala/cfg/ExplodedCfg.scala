package cfg

import org.opalj.br.DeclaredMethod
import org.opalj.br.analyses.Project
import org.opalj.br.cfg.CFGNode
import org.opalj.tac.cg.CallGraph


case class ExplodedCfg(_entry: CfgNode,
                       _nodes: Set[CfgNode],
                       _predecessors: Map[Int, Set[CfgNode]],
                       _successors: Map[Int, Set[CfgNode]],
                       _callers: List[(Int, MethodDescription)],
                       _callees: List[(Int, List[MethodDescription])]) {

  def getEntry(method: MethodDescription): CfgNode =
    _nodes.find(n => n.method.equals(method) && n.isEntry).get

  def getPredecessors(node: CfgNode): Set[CfgNode] = _predecessors.get(node.id) match {
    case Some(value) => value
    case None => throw new RuntimeException("Node doesn't exist")
  }

  def getSuccessors(node: CfgNode): Set[CfgNode] = _successors.get(node.id) match {
    case Some(value) => value
    case None => throw new RuntimeException("Node doesn't exist")
  }

  def successors: Map[Int, Set[CfgNode]] = _successors

  def predecessors: Map[Int, Set[CfgNode]] = _predecessors

  def entry: CfgNode = _entry

  def nodes: Set[CfgNode] = _nodes

}
//What are things we probably need?
//Unique method identifier + stmt identifier

case class StmtNode(stmt: Stmt, method: MethodDescription, isCallRet: Boolean, parentNode: Int, idx: Int)

object CfgProcessor {
  def toMethodDescription(method: DeclaredMethod, isStatic: Boolean): MethodDescription =
    MethodDescription(method.toJava, method.descriptor.parametersCount, method.declaringClassType, isStatic)
  implicit def wrapNode(cfgNode: CFGNode): Option[CFGNode] = Option(cfgNode)

  def buildIntraproceduralCFG[T](callGraph: CallGraph, tac: TACGenerator)(implicit p: Project[T]) = {
    //First add all nodes intraprocedural predecessors and successors
    val methods = callGraph.reachableMethods().map(_.method)
    var result: Map[MethodDescription, ExplodedCfg] = Map()
    for (method <- methods if !callGraph.hasVMLevelCaller(method)) {
      var predecessors: Map[Int, Set[CfgNode]] = Map()
      var successors: Map[Int, Set[CfgNode]] = Map()
      var nodeSet: Set[CfgNode] = Set()
      tac.get(method) match {
        case Some(code) =>
          val cfg = code.cfg
          val callers: List[(Int, MethodDescription)] =
            callGraph
              .callersOf(method)
              .iterator
              .toList
              .map(a => {
                val code1 = tac.get(a._1).get; (code1.pcToIndex(a._2), toMethodDescription(a._1, code1.params.parameters(0) eq null))
              })

          val callees: List[(Int, List[MethodDescription])] =
            callGraph
              .calleesOf(method)
              .map(a => (
                code.pcToIndex(a._1),
                a._2.map(
                  c => toMethodDescription(
                    c.method,
                    tac.get(c.method).map(m => m.params.parameters(0) eq null).getOrElse(true)
                  )
                ).toList)
              )
              .toList
          //register all items in hashcons
          val methodDescription = toMethodDescription(method, code.params.parameters(0) eq null)
          for (bb <- cfg.allBBs.toList ++ List(cfg.abnormalReturnNode, cfg.normalReturnNode) ++ cfg.catchNodes) {
            val ret = if (bb.isBasicBlock) tac.get(method.definedMethod)
              .instructions
              .slice(bb.asBasicBlock.startPC, bb.asBasicBlock.endPC + 1)
              .toList else List()
            CfgNodeFactory.createNode(Some(bb), methodDescription, unrwrapinstructions = ret)
            if (ret.exists(stmt => stmt.isMethodCall || !stmt.forallSubExpressions(expr => !expr.isFunctionCall))) { //there is acall return
              CfgNodeFactory.createNode(Some(bb), methodDescription, true, unrwrapinstructions = List(ret.last))
            }
          }
          // Add local preds
          for (bb <- cfg.allBBs.toList ++ List(cfg.abnormalReturnNode, cfg.normalReturnNode) ++ cfg.catchNodes) {
            val ret = if (bb.isBasicBlock) tac.get(method.definedMethod)
              .instructions
              .slice(bb.asBasicBlock.startPC, bb.asBasicBlock.endPC + 1)
              .toList else List()
            val node = CfgNodeFactory.createNode(Some(bb), methodDescription, unrwrapinstructions = ret)
            nodeSet += node
            predecessors += (node.id -> (predecessors.getOrElse(node.id, Set()) ++ bb.predecessors.map(p => CfgNodeFactory.createNode(Some(p), methodDescription))))
            successors += (node.id -> (successors.getOrElse(node.id, Set()) ++ bb.successors.map(s => CfgNodeFactory.createNode(Some(s), methodDescription))))
          }
          //Add call returns
          for (bb <- cfg.allBBs.toList ++ List(cfg.abnormalReturnNode, cfg.normalReturnNode) ++ cfg.catchNodes) { //TODO add catch nodes
            val ret = if (bb.isBasicBlock) tac.get(method.definedMethod)
              .instructions
              .slice(bb.asBasicBlock.startPC, bb.asBasicBlock.endPC + 1)
              .toList else List()
            val node = CfgNodeFactory.createNode(Some(bb), methodDescription, unrwrapinstructions = ret)
            if (ret.exists(stmt => stmt.isMethodCall || !stmt.forallSubExpressions(expr => !expr.isFunctionCall))) { //there is acall return
              val callRet = CfgNodeFactory.createNode(Some(bb), methodDescription, true, unrwrapinstructions = List(ret.last))
              nodeSet += node
              nodeSet += callRet
              //replace the call nodes successors with call ret
              //replace
              successors += (callRet.id -> successors(node.id))
              successors(node.id).foreach(s => predecessors += (s.id -> (predecessors(s.id) - node + callRet)))
              predecessors += (callRet.id -> Set(node))
              successors += (node.id -> Set(callRet))
            }
          }
          result += (methodDescription -> ExplodedCfg(nodeSet.find(p => p.isEntry).get, nodeSet, predecessors, successors, callers, callees))
        case None => println(method)
      }
    }
    result
  }
}


