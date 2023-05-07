package lattice

/** Specifies how values are combined and compared in the lattice.
  */
trait ValueOperator {
  def join(l1: Value, l2: Value): Value

  def geq(l1: Value, l2: Value): Boolean

  def leq(l1: Value, l2: Value): Boolean

  def isBottom(l1: Value): Boolean

  def getRet(l1: Value): Value

  // Should rebind ret mappings to one that makse sense, i.e caller for return -> returnfromcallee
  def addRetInformation(ret: Value, l2: Value): Value

  def restoreLocal(l1: Value): Value

  def getArgs(l1: Value): Value

  def bindParams(args: Value, l2: Value, isStatic: Boolean): Value

}

trait Value extends Serializable {}
