package analyses

import cfg.{Assignment, Var}
import lattice.{AbstractObject, Constant, Integer}
import org.scalatest.funsuite.AnyFunSuite

class ConstantPropagationAnalysisTest extends AnyFunSuite {
  val in = Constant(
    Map() +
      ("1" -> (Integer(false, Some(5)), AbstractObject(Set()))) +
      ("2" -> (Integer(false, Some(4)), AbstractObject(Set())))+
      ("3" -> (Integer(false, None), AbstractObject(Set()))) +
      ("4" -> (Integer(true, None), AbstractObject(Set())))
  )

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

  test("TestUnExpr") {
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

}
