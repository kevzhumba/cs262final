package analyses

import cfg._
import lattice.{AbstractObject, AllocationSite, Constant, ConstantOperator, Integer, Value}
import org.json4s.ShortTypeHints
import protos.dataflow.{DataflowServerGrpc, GetFieldRequest, PutFieldRequest}
import org.json4s.native.Serialization
import org.json4s.native.Serialization.{read, write}

import java.io.ObjectInputStream.GetField

object ConstantPropagationAnalysis extends Analysis {
  implicit val formats = Serialization.formats(
    ShortTypeHints(
      List(
        classOf[BBNode],
        classOf[BBEntryNode],
        classOf[ExNode],
        classOf[CRNode]))) +
    new StmtSerializer() + new ExprSerializer() + new FieldTypeSerializer()

  val nullAlloc = AbstractObject(Set(AllocationSite(null, -1, null)))
  override def defaultFieldValue: (Integer, AbstractObject) = (Integer(false, Some(0)), nullAlloc)
  override def botValue: Value = ???

  override def topValue: Value = ???

  override def initialValue(cfg: ExplodedCfg): Value = {
    val ints = cfg.nodes.flatMap(c => c.instructions.flatMap(i => StmtUtil.getVars(i.stmt))).toList
    Constant(ints.map(i => (i.toString, (Integer(true, None), AbstractObject(Set())))).toMap)
  }

  override def transfer(stmtNode: StmtNode,
                        in: Value,
                        stubs: Map[MethodDescription, DataflowServerGrpc.DataflowServerBlockingStub]): Value = {
      val input: Constant = in.asInstanceOf[Constant]
      val stmt: Stmt = stmtNode.stmt
      val isCallRet = stmtNode.isCallRet
      stmt match {
        case r: ReturnValue => Constant(input.vals + ("returnForCaller" -> evalExpr(r.ret, isCallRet, input, stmtNode, stubs)._1))
        case a: Assignment =>
          if (isCallRet) {
            val res = evalExpr(a.expr, isCallRet, input, stmtNode, stubs)._1
            Constant(input.vals ++ a.targetVar.vars.map(v => (v.toString, res)).toMap)
          } else {
            val res = evalExpr(a.expr, isCallRet, input, stmtNode, stubs)
            if (!(res._1 eq null)) {
              Constant(input.vals ++ a.targetVar.vars.map(v => (v.toString, res._1)).toMap)
            } else {
              val params = res._2
              Constant(input.vals ++ params.zipWithIndex.map(i => ("arg_" + i._2.toString, i._1)).toMap)
            }
          }
        case PutField(declaringClass, name, declaredFieldType, objRef, value) =>
          val obj = evalExpr(objRef, isCallRet, input, stmtNode, stubs)._1._2
          val set = evalExpr(value, isCallRet, input, stmtNode, stubs)._1
          for (alloc <- obj.sites) {
            val allocJson = write(alloc)
            val setJson = write(set)
            stubs(alloc.method).putField(PutFieldRequest(allocJson,name,setJson))
          }
          in
        case NonVirtualMethodCall(declaringClass, isInterface, name, receiver, params) =>
          if (isCallRet) {
            in
          } else {
            val recv = evalExpr(receiver, isCallRet, input, stmtNode, stubs)._1
            val args = params.map(evalExpr(_, isCallRet, input, stmtNode, stubs)._1).toList
            Constant(input.vals ++ (recv :: args).zipWithIndex.map(i => ("arg_" + i._2.toString, i._1)).toMap)
          }
        case StaticMethodCall(declaringClass, isInterface, name, params) =>
          if (isCallRet) {
            in
          } else {
            val args = params.map(evalExpr(_, isCallRet, input, stmtNode, stubs)._1).toList
            Constant(input.vals ++ args.zipWithIndex.map(i => ("arg_" + i._2.toString, i._1)).toMap)
          }
        case VirtualMethodCall(declaringClass, isInterface, name, receiver, params) =>
          if (isCallRet) {
            in
          } else {
            val recv = evalExpr(receiver, isCallRet, input, stmtNode, stubs)._1
            val args = params.map(evalExpr(_, isCallRet, input, stmtNode, stubs)._1).toList
            Constant(input.vals ++ (recv :: args).zipWithIndex.map(i => ("arg_" + i._2.toString, i._1)).toMap)
          }
        case ExprStmt(expr) => throw new RuntimeException("EVAL")
        case _ =>  in
      }
    }

  implicit def convert(arg: (Integer, AbstractObject)): ((Integer, AbstractObject), List[(Integer, AbstractObject)]) = {
    (arg, null)
  }
  def evalExpr(
                expr: Expr,
                isCallRet: Boolean,
                in: Constant,
                stmtNode: StmtNode,
                stubs: Map[MethodDescription, DataflowServerGrpc.DataflowServerBlockingStub]): ((Integer, AbstractObject), List[(Integer, AbstractObject)])= {
    expr match {
      case Null() => ((Integer(true, None), nullAlloc), null)
      case New(typ) => ((Integer(true, None), AbstractObject(Set(AllocationSite(stmtNode.method, stmtNode.idx, typ)))), null)
      case i: IntConstant => ((Integer(false, Some(i.value)), AbstractObject(Set())), null)
      case b: BinExpr =>
        val left = evalExpr(b.left, isCallRet, in, stmtNode, stubs)._1._1
        val right = evalExpr(b.right, isCallRet, in,stmtNode, stubs)._1._1
        if (left.isBot || right.isBot)
          ((Integer(true, None), AbstractObject(Set())), null)
        else if (left.int.isEmpty || right.int.isEmpty) {
          ((Integer(false, None), AbstractObject(Set())), null)
        } else {
          ((Integer(false, Some(b.op match {
            case cfg.BinOps.Add => left.int.get + right.int.get
            case cfg.BinOps.Subtract => left.int.get - right.int.get
            case cfg.BinOps.Multiply => left.int.get * right.int.get
            case cfg.BinOps.Divide => left.int.get / right.int.get
            case cfg.BinOps.Modulo => left.int.get % right.int.get
            case cfg.BinOps.And => left.int.get & right.int.get
            case cfg.BinOps.Or => left.int.get | right.int.get
            case cfg.BinOps.XOr => left.int.get ^ right.int.get
          }) ), AbstractObject(Set())), null)
        }
      case unExpr: UnExpr =>
        val op = evalExpr(unExpr.operand, isCallRet, in,stmtNode, stubs)._1
        if (op._1.isBot)
          ((Integer(true, None), AbstractObject(Set())), null)
        else if (op._1.int.isEmpty) {
          ((Integer(false, None), AbstractObject(Set())), null)
        } else {
          unExpr.op match {
            case cfg.UnOps.Negate => ((Integer(false, Some(-1 * op._1.int.get)), AbstractObject(Set())), null)
          }
        }
      case v: Var =>
        val vals = v.vars.map(i => in.vals(i.toString))
        var runningInt: Option[(Integer, AbstractObject)] = None
        for (int <- vals) {
          runningInt match {
            case Some(value) => runningInt = Some((
              ConstantOperator.joinIntegers(value._1, int._1),
              ConstantOperator.joinAbstractObjects(value._2, int._2)))
            case None => runningInt = Some(int)
          }
        }
        runningInt.get
      case s: StaticFunctionCall =>
        if (isCallRet) {
          in.vals.get("returnFromCallee") match {
            case Some(value) => value
            case None => ((Integer(true, None), AbstractObject(Set())), null)
          }
        } else {
          (null, s.params.map(evalExpr(_, isCallRet, in,stmtNode, stubs)._1).toList)
        }
      case v: VirtualFunctionCall =>
        if (isCallRet) {
          in.vals.get("returnFromCallee") match {
            case Some(value) => value
            case None => ((Integer(true, None), AbstractObject(Set())), null)
          }
        } else {
          (null, (v.receiver :: v.params.toList).map(evalExpr(_, isCallRet, in, stmtNode, stubs)._1))
        }
      case n: NonVirtualFunctionCall =>
        if (isCallRet) {
          in.vals.get("returnFromCallee") match {
            case Some(value) => value
            case None => ((Integer(true, None), AbstractObject(Set())), null)
          }
        } else {
          (null, (n.receiver :: n.params.toList).map(evalExpr(_, isCallRet, in, stmtNode, stubs)._1))
        }
      case ReadField(declaringClass, name, declaredFieldType, objRef) =>
        val obj = evalExpr(objRef, isCallRet, in, stmtNode, stubs)._1._2
        var value = defaultFieldValue
        val method = write(stmtNode.method)
        for (alloc <- obj.sites) {
          val allocJson = write(alloc)
          val response = stubs(alloc.method).getField(GetFieldRequest(allocJson, name, method))
          value = ConstantOperator.joinTuples(value, read[(Integer, AbstractObject)](response.value))
        }
        value
      case _ => println("Unhandled expr"); ((Integer(false, None), AbstractObject(Set())), null)
    }
  }

}


