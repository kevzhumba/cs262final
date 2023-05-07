package lattice

import org.scalatest._
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class ConstantOperatorSpec extends AnyFlatSpec with Matchers {
  val constant1 = Constant(
    Map(
      "arg_1" -> (Integer(false, Some(1)), AbstractObject(Set())),
      "arg_2" -> (Integer(false, Some(2)), AbstractObject(Set()))
    )
  )

  val constant2 = Constant(
    Map(
      "arg_2" -> (Integer(false, Some(2)), AbstractObject(Set())),
      "arg_3" -> (Integer(false, Some(3)), AbstractObject(Set()))
    )
  )

  "join" should "join two constants" in {
    val joined = ConstantOperator.join(constant1, constant2)
    joined.asInstanceOf[Constant].vals should contain allOf (
      "arg_1" -> (Integer(false, Some(1)), AbstractObject(Set())),
      "arg_2" -> (Integer(false, Some(2)), AbstractObject(Set())),
      "arg_3" -> (Integer(false, Some(3)), AbstractObject(Set()))
    )
  }

  "getArgs" should "return a constant containing only arguments" in {
    val args = ConstantOperator.getArgs(constant1)
    args.asInstanceOf[Constant].vals should contain allOf (
      "arg_1" -> (Integer(false, Some(1)), AbstractObject(Set())),
      "arg_2" -> (Integer(false, Some(2)), AbstractObject(Set()))
    )
  }

  "restoreLocal" should "return a constant containing only local variables" in {
    val local = ConstantOperator.restoreLocal(constant1)
    local.asInstanceOf[Constant].vals shouldBe empty
  }

  "addRetInformation" should "add return value to the constant" in {
    val ret = Constant(
      Map(
        "returnForCaller" -> (Integer(false, Some(1)), AbstractObject(Set()))
      )
    )

    val withRet = ConstantOperator.addRetInformation(ret, constant1)
    withRet.asInstanceOf[Constant].vals should contain allOf (
      "arg_1" -> (Integer(false, Some(1)), AbstractObject(Set())),
      "arg_2" -> (Integer(false, Some(2)), AbstractObject(Set())),
      "returnFromCallee" -> (Integer(false, Some(1)), AbstractObject(Set()))
    )
  }

  "getRet" should "return a constant containing only the return value" in {
    val ret = Constant(
      Map(
        "returnForCaller" -> (Integer(false, Some(1)), AbstractObject(Set())),
        "arg_1" -> (Integer(false, Some(1)), AbstractObject(Set()))
      )
    )

    val retValue = ConstantOperator.getRet(ret)
    retValue
      .asInstanceOf[Constant]
      .vals should contain only ("returnForCaller" -> (Integer(
      false,
      Some(1)
    ), AbstractObject(Set())))
  }

  "bindParams" should "bind arguments to the given value" in {
    val bound = ConstantOperator.bindParams(constant1, constant2, false)
    bound.asInstanceOf[Constant].vals should contain allOf (
      "-2" -> (Integer(false, Some(1)), AbstractObject(Set())),
      "-3" -> (Integer(false, Some(2)), AbstractObject(Set())),
      "arg_2" -> (Integer(false, Some(2)), AbstractObject(Set())),
      "arg_3" -> (Integer(false, Some(3)), AbstractObject(Set()))
    )
  }

  "joinIntegers" should "join two integers" in {
    ConstantOperator.joinIntegers(
      Integer(false, Some(1)),
      Integer(false, Some(1))
    ) shouldEqual Integer(false, Some(1))
    ConstantOperator.joinIntegers(
      Integer(false, Some(1)),
      Integer(false, Some(2))
    ) shouldEqual Integer(false, None)
    ConstantOperator.joinIntegers(
      Integer(false, Some(1)),
      Integer(true, Some(2))
    ) shouldEqual Integer(false, Some(1))
    ConstantOperator.joinIntegers(
      Integer(true, Some(1)),
      Integer(true, Some(2))
    ) shouldEqual Integer(true, Some(2))
  }
}
