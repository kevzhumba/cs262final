package lattice

object ConstantOperator extends ValueOperator {
  override def geq(l1: Value, l2: Value): Boolean = {???}
  override def join(l1: Value, l2: Value): Value = {
    val map1 = l1.asInstanceOf[Constant].vals
    val map2 = l2.asInstanceOf[Constant].vals
    Constant(map1 ++ map2.map { case (k, v) => k -> joinIntegers(v, map1.getOrElse(k, Integer(true, None))) })
  }
  override def leq(l1: Value, l2: Value): Boolean = ???
  override def isBottom(l1: Value): Boolean = ???

  override def getArgs(l1: Value): Value = {
    val c1 = l1.asInstanceOf[Constant]
    println("GETTING ARGS")
    val args = c1.vals.filter(k => k._1.contains("arg"))
    println(args)
    Constant(args)
  }

  override def restoreLocal(l1: Value): Value = {
    val c1 = l1.asInstanceOf[Constant]
    val local = c1.vals.filter(k => !(k._1.contains("arg") || k._1.contains("returnFromCallee")))
    Constant(local)
  }


  override def addRetInformation(ret: Value, l2: Value): Value = {
    val cret = ret.asInstanceOf[Constant]
    val retVal = cret.vals.getOrElse("returnForCaller", Integer(true, None))
    Constant(l2.asInstanceOf[Constant].vals + ("returnFromCallee" -> retVal))
  }

  override def getRet(l1: Value): Value = {
    val c1 = l1.asInstanceOf[Constant]
    Constant(c1.vals.filter(k => k._1.contains("returnForCaller")))
  }
    
  override def bindParams(args: Value, l2: Value, isStatic: Boolean): Value = {
    val startIdx = if (isStatic) -2 else -1
    val constant = args.asInstanceOf[Constant]
    Constant(l2.asInstanceOf[Constant].vals ++
      constant.vals.map(k => ((startIdx - k._1.substring("arg_".length).toInt).toString, k._2)))
  }



  def joinIntegers(i1: Integer, i2: Integer): Integer = {
    if (i1.isBot) {
      i2
    } else if (i2.isBot) {
      i1
    } else if (i1.int.isEmpty || i2.int.isEmpty) {
      Integer(false, None)
    } else if (i1.int.get != i2.int.get) {
      Integer(false, None)
    } else {
      i1
    }
  }
}

case class Integer(isBot: Boolean, int: Option[Int])

case class Constant(vals: Map[String, Integer]) extends Value


