package cfg

/** Class representing an entry node of a CFG
  */
case class BBEntryNode(
    method: MethodDescription,
    instructions: List[StmtNode],
    id: Int
) extends CfgNode {
  override def isEntry: Boolean = true
}
