package analyses

import cfg.{Assignment, BinExpr, BinOps, StaticFunctionCall, StaticMethodCall, StmtNode, UnExpr, UnOps, Var, VirtualFunctionCall, VirtualMethodCall}
import lattice.{AbstractObject, AllocationSite, Constant, Integer}
import org.opalj.br.{ObjectType, VirtualMethod}
import org.scalatest.funsuite.AnyFunSuite

class ConstantPropagationAnalysisTest extends AnyFunSuite {
  val in = Constant(
    Map() +
      ("1" -> (Integer(false, Some(5)), AbstractObject(Set()))) +
      ("2" -> (Integer(false, Some(4)), AbstractObject(Set())))+
      ("3" -> (Integer(false, None), AbstractObject(Set()))) +
      ("4" -> (Integer(true, None), AbstractObject(Set()))) +
      ("5" -> (Integer(true, None), AbstractObject(Set(AllocationSite(null, -1, null)))))
  )
  val retIn = Constant(Map() + ("returnFromCallee" -> (Integer(false, Some(5)), AbstractObject(Set()))))

  test("testAssign") {
    val assgn = Var(List(6))
    val assignStmt = Assignment(assgn, Var(List(1)))
    val stmtNode = StmtNode(assignStmt, null, false, 0, 0)
    val out = ConstantPropagationAnalysis.transfer(stmtNode, in, Map())
    assert(out.asInstanceOf[Constant].vals.get("6").get._1.int.get == 5)
  }

  test("testMethodCalls") {
    val var1 = Var(List(1))
    val var2 = Var(List(2))
    val var3 = Var(List(3))
    val recv = Var(List(5))
    val stmt1 = StaticMethodCall(ObjectType.String, true, "test", Seq(var1, var2, var3))
    val stmtNode = StmtNode(stmt1, null, false, 0, 0)
    val ret = ConstantPropagationAnalysis.transfer(stmtNode, in, Map()).asInstanceOf[Constant]
    assert(ret.vals.get("arg_0").get._1.int.get == 5)
    assert(ret.vals.get("arg_1").get._1.int.get == 4)
    assert(ret.vals.get("arg_2").get._1.int.isEmpty)
    val stmt2 = VirtualMethodCall(ObjectType.String, true, "test", recv, Seq(var1, var2, var3))
    val stmtNode2 = StmtNode(stmt2, null, false, 0, 0)
    val ret2 = ConstantPropagationAnalysis.transfer(stmtNode2, in, Map()).asInstanceOf[Constant]
    assert(ret2.vals.get("arg_0").get._2.sites.size == 1)
    assert(ret2.vals.get("arg_1").get._1.int.get == 5)
    assert(ret2.vals.get("arg_2").get._1.int.get == 4)
    assert(ret2.vals.get("arg_3").get._1.int.isEmpty)
  }


  test("TestVar") {
    val expr = Var(List(1))
    val out = ConstantPropagationAnalysis.evalExpr(expr, false, in, null)
    assert(out._1._1.int.get == 5)
    val expr2 = Var(List(1, 2))
    val out2 = ConstantPropagationAnalysis.evalExpr(expr2, false, in, null)
    assert(out2._1._1.int.isEmpty)
    val expr3 = Var(List(1, 4))
    val out3 = ConstantPropagationAnalysis.evalExpr(expr3, false, in, null)
    assert(out3._1._1.int.get == 5)
  }

  test("TestBinExpr") {
    val var1 = Var(List(1))
    val var2 = Var(List(2))
    val var3 = Var(List(3))
    val var4 = Var(List(4))
    val expr = BinExpr(var1, BinOps.Add, var2)
    val out = ConstantPropagationAnalysis.evalExpr(expr, false, in, null)
    assert(out._1._1.int.get == 9)
    val expr2 = BinExpr(var1, BinOps.Add, var3)
    val out2 = ConstantPropagationAnalysis.evalExpr(expr2, false, in, null)
    assert(out2._1._1.int.isEmpty)
    assert(!out2._1._1.isBot)
    val expr3 = BinExpr(var1, BinOps.Add, var4)
    val out3 = ConstantPropagationAnalysis.evalExpr(expr3, false, in, null)
    assert(out3._1._1.isBot)
  }

  test("TestUnExpr") {
    val var1 = Var(List(1))
    val var2 = Var(List(2))
    val var3 = Var(List(3))
    val var4 = Var(List(4))
    val expr = UnExpr(UnOps.Negate, var1)
    val out = ConstantPropagationAnalysis.evalExpr(expr, false, in, null)
    assert(out._1._1.int.get == -5)
    val expr2 = UnExpr(UnOps.Negate, var3)
    val out2 = ConstantPropagationAnalysis.evalExpr(expr2, false, in, null)
    assert(out2._1._1.int.isEmpty)
    assert(!out2._1._1.isBot)
    val expr3 = UnExpr(UnOps.Negate, var4)
    val out3 = ConstantPropagationAnalysis.evalExpr(expr3, false, in, null)
    assert(out3._1._1.isBot)
  }

  test("FunctionCall") {
    val var1 = Var(List(1))
    val var2 = Var(List(2))
    val var3 = Var(List(3))
    val recv = Var(List(5))
    val expr = StaticFunctionCall(ObjectType.String, false, "test", Seq(var1, var2, var3))
    val out = ConstantPropagationAnalysis.evalExpr(expr, false, in, null)
    assert(out._2.size == 3)
    assert(out._2(0)._1.int.get == 5)
    assert(out._2(1)._1.int.get == 4)
    assert(out._2(2)._1.int.isEmpty)
    val expr1 = StaticFunctionCall(ObjectType.String, true, "test", Seq(var1, var2, var3))
    val out1 = ConstantPropagationAnalysis.evalExpr(expr1, true, retIn, null)
    assert(out1._1._1.int.get == 5)
    val expr2 = VirtualFunctionCall(ObjectType.String, true, "test",recv, Seq(var1, var2, var3))
    val out2 = ConstantPropagationAnalysis.evalExpr(expr2, true, retIn, null)
    assert(out2._1._1.int.get == 5)
    val expr3 = VirtualFunctionCall(ObjectType.String, false, "test", recv, Seq(var1, var2, var3))
    val out3 = ConstantPropagationAnalysis.evalExpr(expr3, false, in, null)
    assert(out3._2.size ==4)
    assert(out3._2(0)._2.sites.size == 1)
  }
}
