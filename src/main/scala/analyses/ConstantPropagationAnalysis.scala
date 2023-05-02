package analyses

import cfg._
import lattice.{Constant, ConstantOperator, Integer, Value}

object ConstantPropagationAnalysis extends Analysis {
    override def botValue: Value = ???

    override def topValue: Value = ???

    override def initialValue(cfg: ExplodedCfg): Value = {
      val ints = cfg.nodes.flatMap(c => c.instructions.flatMap(i => StmtUtil.getVars(i.stmt))).toList
      println(ints)
      Constant(ints.map(i => (i.toString, Integer(true, None))).toMap)
    }

  override def transfer(stmtNode: StmtNode, in: Value): Value = {
      val input: Constant = in.asInstanceOf[Constant]
      val stmt: Stmt = stmtNode.stmt
      val isCallRet = stmtNode.isCallRet
      stmt match {
        case r: ReturnValue => Constant(input.vals + ("returnForCaller" -> evalExpr(r.ret, isCallRet, input)._1))
        case a: Assignment =>
          if (isCallRet) {
            val res = evalExpr(a.expr, isCallRet, input)._1
            Constant(input.vals ++ a.targetVar.vars.map(v => (v.toString, res)).toMap)
          } else {
            val res = evalExpr(a.expr, isCallRet, input)
            if (!(res._1 eq null)) {
              Constant(input.vals ++ a.targetVar.vars.map(v => (v.toString, res._1)).toMap)
            } else {
              val params = res._2
              Constant(input.vals ++ params.zipWithIndex.map(i => ("arg_" + i._2.toString, i._1)).toMap)
            }
          }
        case _ => println("Unhandled stmt"); in
      }
    }


  implicit def convert(arg: Integer): (Integer, List[Integer]) = {
    (arg, null)
  }
  def evalExpr(expr: Expr, isCallRet: Boolean, in: Constant): (Integer, List[Integer])= {
    expr match {
      case i: IntConstant => Integer(false, Some(i.value))
      case b: BinExpr =>
        val left = evalExpr(b.left, isCallRet, in)._1
        val right = evalExpr(b.right, isCallRet, in)._1
        if (left.isBot || right.isBot)
          Integer(true, None)
        else if (left.int.isEmpty || right.int.isEmpty) {
          Integer(false, None)
        } else {
          Integer(false, Some(b.op match {
            case cfg.BinOps.Add => left.int.get + right.int.get
            case cfg.BinOps.Subtract => left.int.get - right.int.get
            case cfg.BinOps.Multiply => left.int.get * right.int.get
            case cfg.BinOps.Divide => left.int.get / right.int.get
            case cfg.BinOps.Modulo => left.int.get % right.int.get
            case cfg.BinOps.And => left.int.get & right.int.get
            case cfg.BinOps.Or => left.int.get | right.int.get
            case cfg.BinOps.XOr => left.int.get ^ right.int.get
          }) )
        }
      case unExpr: UnExpr =>
        val op = evalExpr(unExpr.operand, isCallRet, in)._1
        if (op.isBot)
          Integer(true, None)
        else if (op.int.isEmpty) {
          Integer(false, None)
        } else {
          unExpr.op match {
            case cfg.UnOps.Negate => Integer(false, Some(-1 * op.int.get))
          }
        }
      case v: Var =>
        val vals = v.vars.map(i => in.vals(i.toString))
        var runningInt: Option[Integer] = None
        for (int <- vals) {
          runningInt match {
            case Some(value) => runningInt = Some(ConstantOperator.joinIntegers(value, int))
            case None => runningInt = Some(int)
          }
        }
        runningInt.get
      case s: StaticFunctionCall =>
        if (isCallRet) {
          in.vals.get("returnFromCallee") match {
            case Some(value) => value
            case None => Integer(true, None)
          }
        } else {
          (null, s.params.map(evalExpr(_, isCallRet, in)._1).toList)
        }
      case _ => println("Unhandled expr"); Integer(false, None)
    }
  }

}


