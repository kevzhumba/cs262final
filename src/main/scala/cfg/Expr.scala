package cfg

import org.json4s.{CustomSerializer, Extraction, JArray, JBool, JField, JInt, JObject, JString}
import org.opalj.br.{FieldType, MethodDescriptor, ObjectType, ReferenceType}
import org.opalj.tac
import org.opalj.tac.{BinaryExpr, DUVar, Var}
import org.opalj.value.ValueInformation

sealed trait Expr {

}

class ExprSerializer extends CustomSerializer[Expr](format => (
  {
    case JObject(JField("value", JInt(i)):: Nil) => IntConstant(i.intValue)
    case JObject(JField("vars", JArray(x)) :: Nil) => Var(x.map(_.asInstanceOf[JInt].num.intValue))
    case JObject(JField("left", left) :: JField("op", JInt(id)) :: JField("right", right) :: Nil) =>
        BinExpr(
          left.extract(
            format, Manifest.classType(classOf[Expr])),
          BinOps(id.intValue),
          right.extract(
            format,  Manifest.classType(classOf[Expr])
          )
        )
    case JObject(JField("op", JInt(id)) :: JField("operand", operand):: Nil) =>
      UnExpr(UnOps(id.intValue), operand.extract(format, Manifest.classType(classOf[Expr])))
    case JObject(JField("declaringClass", declaringClass) :: JField("isInterface", JBool(isInterface)) :: JField("name", JString(name)) :: JField("params", JArray(p)) :: Nil) =>
      StaticFunctionCall(
        declaringClass.extract(format, Manifest.classType(classOf[ObjectType])),
        isInterface,
        name,
        p.map(a => a.extract[Expr](format, Manifest.classType(classOf[Expr])))
      )
    case JObject(JField("virtual", JBool(true)) ::
      JField("declaringClass", declaringClass) ::
      JField("isInterface", JBool(isInterface)) ::
      JField("name", JString(name)) ::
      JField("receiver", receiver) ::
      JField("params", JArray(p)) ::
      Nil) => VirtualFunctionCall(
        declaringClass.extract(format, Manifest.classType(classOf[ObjectType])), //This might be wrong
        isInterface,
        name,
        receiver.extract(format, Manifest.classType(classOf[Expr])),
        p.map(a => a.extract[Expr](format, Manifest.classType(classOf[Expr])))
      )
    case JObject(JField("virtual", JBool(true)) ::
      JField("declaringClass", declaringClass) ::
      JField("isInterface", JBool(isInterface)) ::
      JField("name", JString(name)) ::
      JField("receiver", receiver) ::
      JField("params", JArray(p)) ::
      Nil) =>
      NonVirtualFunctionCall(
        declaringClass.extract(format, Manifest.classType(classOf[ObjectType])), //This might be wrong
        isInterface,
        name,
        receiver.extract(format, Manifest.classType(classOf[Expr])),
        p.map(a => a.extract[Expr](format, Manifest.classType(classOf[Expr])))
      )
    case JObject(
      JField("declaringClass", declaringClass) ::
        JField("name", JString(name)) ::
        JField("fieldType", fieldType) ::
        JField("objRef", objRef) ::
        Nil) =>
        ReadField(
          declaringClass.extract(format, Manifest.classType(classOf[ObjectType])), //This might be wrong
          name,
          fieldType.extract(format, Manifest.classType(classOf[FieldType])),
          objRef.extract(format, Manifest.classType(classOf[Expr])),
        )
    case JObject(JField("typ", typ) :: Nil) =>
      New(typ.extract(format, Manifest.classType(classOf[ObjectType])))
  }, {
    case i: IntConstant => JObject(JField("value", JInt(i.value)))
    case v: Var => JObject(JField("vars", JArray(v.vars.map(JInt(_)))) :: Nil)
    case b: BinExpr => JObject(
      JField("left", Extraction.decompose(b.left)(format)) ::
        JField("op", JInt(b.op.id)) ::
        JField("right", Extraction.decompose(b.right)(format)) ::Nil)
    case u: UnExpr => JObject(
      JField("op", JInt(u.op.id)) ::
        JField("operand", Extraction.decompose(u.operand)(format)) ::
        Nil)
    case s: StaticFunctionCall =>
      JObject(
        JField("declaringClass", Extraction.decompose(s.declaringClass)(format)) ::
          JField("isInterface", JBool(s.isInterface)) ::
          JField("name", JString(s.name)) ::
          JField("params", JArray(s.params.map(p => Extraction.decompose(p)(format)).toList)) ::
          Nil
      )
    case v: VirtualFunctionCall =>
      JObject(
        JField("virtual", JBool(true)) ::
          JField("declaringClass", Extraction.decompose(v.declaringClass)(format)) ::
          JField("isInterface", JBool(v.isInterface)) ::
          JField("name", JString(v.name)) ::
          JField("receiver", Extraction.decompose(v.receiver)(format)) ::
          JField("params", JArray(v.params.map(p => Extraction.decompose(p)(format)).toList)) ::
          Nil
      )
    case v: NonVirtualFunctionCall =>
      JObject(
        JField("virtual", JBool(false)) ::
          JField("declaringClass", Extraction.decompose(v.declaringClass)(format)) ::
          JField("isInterface", JBool(v.isInterface)) ::
          JField("name", JString(v.name)) ::
          JField("receiver", Extraction.decompose(v.receiver)(format)) ::
          JField("params", JArray(v.params.map(p => Extraction.decompose(p)(format)).toList)) ::
          Nil
      )
    case r: ReadField =>
      JObject(
        JField("declaringClass", Extraction.decompose(r.declaringClass)(format)) ::
          JField("name", JString(r.name)) ::
          JField("fieldType", Extraction.decompose(r.declaredFieldType)(format)) ::
          JField("objRef", Extraction.decompose(r.objRef)(format)) ::
          Nil)
    case n: New =>
      JObject(
        JField("typ", Extraction.decompose(n.typ)(format)) ::
          Nil)


}
))

object ExprUtil {
  def translate(expr: tac.Expr[DUVar[ValueInformation]]): Expr =
    expr match {
      case i: tac.IntConst => IntConstant(i.value)
      case n: tac.NullExpr => Null()
      case b: tac.BinaryExpr[DUVar[ValueInformation]] =>
        BinExpr(translate(b.left), BinOps(b.op.id), translate(b.right))
      case u: tac.PrefixExpr[DUVar[ValueInformation]] =>
        UnExpr(UnOps(u.op.id), translate(u.operand))
      case n: tac.New =>
        New(n.tpe)
      case rf: tac.GetField[DUVar[ValueInformation]] =>
        ReadField(rf.declaringClass, rf.name, rf.declaredFieldType, translate(rf.objRef))
      case nvf: tac.NonVirtualFunctionCall[DUVar[ValueInformation]] =>
        NonVirtualFunctionCall(nvf.declaringClass, nvf.isInterface, nvf.name, translate(nvf.receiver), nvf.params.map(translate(_)))
      case nvf: tac.VirtualFunctionCall[DUVar[ValueInformation]] =>
        VirtualFunctionCall(nvf.declaringClass, nvf.isInterface, nvf.name, translate(nvf.receiver), nvf.params.map(translate(_)))
      case s: tac.StaticFunctionCall[DUVar[ValueInformation]] =>
        StaticFunctionCall(s.declaringClass, s.isInterface, s.name, s.params.map(translate(_)))
      case v: tac.Var[DUVar[ValueInformation]] =>
        if (v.asVar.isInstanceOf[tac.DVar[ValueInformation]]) {
          Var(List(v.asVar.hashCode() - tac.Var.ASTID * 1171 + 13))
        } else {
          Var(v.asVar.definedBy.toList)
        }
    }

  def getVars(expr: Expr): Set[Int] =
    expr match {
      case IntConstant(value) => Set()
      case BinExpr(left, op, right) => getVars(left) ++ getVars(right)
      case UnExpr(op, operand) => getVars(operand)
      case ReadField(declaringClass, name, declaredFieldType, objRef) =>
        getVars(objRef)
      case NonVirtualFunctionCall(declaringClass, isInterface, name, receiver, params) =>
        getVars(receiver) ++ params.flatMap(p => getVars(p)).toSet
      case VirtualFunctionCall(declaringClass, isInterface, name, receiver, params) =>
        getVars(receiver) ++ params.flatMap(p => getVars(p)).toSet
      case StaticFunctionCall(declaringClass, isInterface, name, params) => params.flatMap(p => getVars(p)).toSet
      case Var(vars) => vars.toSet
      case _ => Set()
    }

}
object BinOps extends Enumeration {

  final val Add = Value("+")
  final val Subtract = Value("-")
  final val Multiply = Value("*")
  final val Divide = Value("/")
  final val Modulo = Value("%")

  final val And = Value("&")
  final val Or = Value("|")
  final val XOr = Value("^")

  final val ShiftLeft = Value("<<")
  final val ShiftRight = Value(">>")
  final val UnsignedShiftRight = Value(">>>")
}

object UnOps extends Enumeration {

  final val Negate = Value("-")

  final val Not = Value("!")

}
case class IntConstant(value: Int) extends Expr
case class Null() extends Expr
case class BinExpr(left: Expr, op: BinOps.Value, right: Expr) extends Expr
case class UnExpr(op: UnOps.Value, operand: Expr) extends Expr
case class New(typ: ObjectType) extends Expr
case class ReadField(declaringClass: ObjectType, name: String, declaredFieldType: FieldType, objRef: Expr) extends Expr
case class NonVirtualFunctionCall(
                                   declaringClass: ObjectType,
                                   isInterface: Boolean,
                                   name: String,
                                   receiver: Expr,
                                   params: Seq[Expr]) extends Expr

case class VirtualFunctionCall(declaringClass: ReferenceType,
                               isInterface: Boolean,
                               name: String,
                               receiver: Expr,
                               params: Seq[Expr]
                              ) extends Expr

case class StaticFunctionCall(declaringClass: ObjectType,
                              isInterface: Boolean,
                              name: String,
                              params: Seq[Expr]) extends Expr

case class Var(vars: List[Int]) extends Expr




