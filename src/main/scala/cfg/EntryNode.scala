package cfg


case class BBEntryNode(method: MethodDescription, instructions: List[StmtNode], id: Int) extends CfgNode {
  override def isEntry: Boolean = true
}


