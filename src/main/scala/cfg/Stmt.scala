package cfg

import cfg.ExprUtil.{ translate}
import org.json4s.{CustomSerializer, DefaultFormats, Extraction, JArray, JBool, JField, JInt, JObject, JString, TypeInfo}
import org.opalj.br.{BooleanType, ByteType, CharType, DoubleType, FieldType, FloatType, IntegerType, LongType, ObjectType, ReferenceType, ShortType}
import org.opalj.tac
import org.opalj.tac.DUVar
import org.opalj.value.ValueInformation

sealed trait Stmt {
}

class FieldTypeSerializer extends CustomSerializer[FieldType](format =>
  ({
    case JObject(JField("type", JString("Bool")) :: Nil) => BooleanType
    case JObject(JField("type", JString("Float")) :: Nil) => ByteType
    case JObject(JField("type", JString("Char")) :: Nil) => CharType
    case JObject(JField("type", JString("Short")) :: Nil) => ShortType
    case JObject(JField("type", JString("Integer")) :: Nil) => IntegerType
    case JObject(JField("type", JString("Long")) :: Nil) => LongType
    case JObject(JField("type", JString("Float")) :: Nil) => FloatType
    case JObject(JField("type", JString("Double")) :: Nil) => DoubleType
    case o => o.extract(DefaultFormats, Manifest.classType(classOf[ObjectType])) },
    {
    case b: BooleanType => JObject(JField("type", JString("Bool")))
    case b: ByteType =>JObject(JField("type", JString("Float")))
    case b: CharType => JObject(JField("type", JString("Char")))
    case b: ShortType => JObject(JField("type", JString("Short")))
    case b: IntegerType => JObject(JField("type", JString("Integer")))
    case b: LongType => JObject(JField("type", JString("Long")))
    case b: FloatType => JObject(JField("type", JString("Float")))
    case b: DoubleType => JObject(JField("type", JString("Double")))
    case o: ObjectType => Extraction.decompose(o)(DefaultFormats)
  })
)


class StmtSerializer extends CustomSerializer[Stmt](format =>
  (
  {
    case JObject(JField("targetVar", e1) :: JField("expr", e2)::Nil) =>
      Assignment(e1.extract(format, Manifest.classType(classOf[Var])), e2.extract(format, Manifest.classType(classOf[Expr])))
    case JObject(JField("left", left) ::JField("op", JInt(id)) :: JField("right", right) :: Nil) =>
      If(left.extract(format, Manifest.classType(classOf[Expr])), RelationalOps(id.intValue), right.extract(format, Manifest.classType(classOf[Expr])))
    case JObject(JField("ret", ret) ::Nil) =>
      ReturnValue(ret.extract(format, Manifest.classType(classOf[Expr])))
    case JObject(JField("declaringClass", declaringClass) :: JField("isInterface", JBool(isInterface)) :: JField("name", JString(name)) :: JField("params", JArray(p)) :: Nil) =>
      StaticMethodCall(
        declaringClass.extract(format, Manifest.classType(classOf[ObjectType])),
        isInterface,
        name,
        p.map(a => a.extract[Expr](format, Manifest.classType(classOf[Expr])))
      )
    case JObject(JField("expr", expr) ::Nil) =>
      ExprStmt(expr.extract(format, Manifest.classType(classOf[Expr])))
    case JObject(JField("className", JString("return")) :: Nil) =>
      Return()
    case JObject(JField("className", JString("nop")) :: Nil) =>
      Nop()
    case JObject(JField("className", JString("goto")) :: Nil) =>
      Goto()
    case JObject(JField("virtual", JBool(true))::
      JField("declaringClass", declaringClass) ::
      JField("isInterface", JBool(isInterface)) ::
      JField("name", JString(name)) ::
      JField("receiver", receiver) ::
      JField("params", JArray(p)) ::
      Nil) =>
      VirtualMethodCall(
        declaringClass.extract(format, Manifest.classType(classOf[ObjectType])), //This might be wrong
        isInterface,
        name,
        receiver.extract(format, Manifest.classType(classOf[Expr])),
        p.map(a => a.extract[Expr](format, Manifest.classType(classOf[Expr])))
      )
    case JObject(JField("virtual", JBool(false)) ::
      JField("declaringClass", declaringClass) ::
      JField("isInterface", JBool(isInterface)) ::
      JField("name", JString(name)) ::
      JField("receiver", receiver) ::
      JField("params", JArray(p)) ::
      Nil) =>
      NonVirtualMethodCall(
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
      JField("value", value) ::
      Nil) =>
      PutField(
        declaringClass.extract(format, Manifest.classType(classOf[ObjectType])), //This might be wrong
        name,
        fieldType.extract(format, Manifest.classType(classOf[FieldType])),
        objRef.extract(format, Manifest.classType(classOf[Expr])),
        value.extract(format, Manifest.classType(classOf[Expr]))
      )
      },
    {
    case a: Assignment =>
      JObject(
        JField("targetVar", Extraction.decompose(a.targetVar)(format)) ::
          JField("expr", Extraction.decompose(a.expr)(format)) :: Nil)
    case i: If =>
      JObject(
        JField("left", Extraction.decompose(i.left)(format)) ::
          JField("op", JInt(i.relationalOps.id)) ::
          JField("right", Extraction.decompose(i.right)(format)) ::
          Nil
      )
    case r: ReturnValue =>
      JObject(
        JField("ret", Extraction.decompose(r.ret)(format)) ::
        Nil
      )
    case s: StaticMethodCall =>
      JObject(
        JField("declaringClass", Extraction.decompose(s.declaringClass)(format)) ::
          JField("isInterface", JBool(s.isInterface)) ::
          JField("name", JString(s.name)) ::
          JField("params", JArray(s.params.map(p => Extraction.decompose(p)(format)).toList)) ::
          Nil
      )
    case v: VirtualMethodCall =>
      JObject(
        JField("virtual", JBool(true)) ::
        JField("declaringClass", Extraction.decompose(v.declaringClass)(format)) ::
          JField("isInterface", JBool(v.isInterface)) ::
          JField("name", JString(v.name)) ::
          JField("receiver", Extraction.decompose(v.receiver)(format)) ::
          JField("params", JArray(v.params.map(p => Extraction.decompose(p)(format)).toList)) ::
          Nil
      )
    case v: NonVirtualMethodCall =>
      JObject(
        JField("virtual", JBool(false)) ::
        JField("declaringClass", Extraction.decompose(v.declaringClass)(format)) ::
          JField("isInterface", JBool(v.isInterface)) ::
          JField("name", JString(v.name)) ::
          JField("receiver", Extraction.decompose(v.receiver)(format)) ::
          JField("params", JArray(v.params.map(p => Extraction.decompose(p)(format)).toList)) ::
          Nil
      )
    case p: PutField =>
      JObject(
        JField("declaringClass", Extraction.decompose(p.declaringClass)(format)) ::
          JField("name", JString(p.name)) ::
          JField("fieldType", Extraction.decompose(p.declaredFieldType)(format)) ::
          JField("objRef", Extraction.decompose(p.objRef)(format))::
          JField("value", Extraction.decompose(p.value)(format))::
          Nil)
    case r: Return =>
      JObject(JField("className", JString("return")) :: Nil)
    case _:Nop =>
      JObject(JField("className", JString("nop")) :: Nil)
    case _: Goto =>
      JObject(JField("className", JString("goto")) :: Nil)
    case e: ExprStmt =>
      JObject(JField("expr", Extraction.decompose(e.expr)(format)))
  }
  )
)
object StmtUtil {
  def translateStmt(stmt: tac.Stmt[DUVar[ValueInformation]]): Stmt = stmt match {
    case i: tac.If[DUVar[ValueInformation]] => If(translate(i.leftExpr), RelationalOps(i.condition.id), translate(i.rightExpr))
    case goto: tac.Goto => Goto()
    case ret: tac.Return => Return()
    case a: tac.Assignment[DUVar[ValueInformation]] => Assignment(translate(a.targetVar).asInstanceOf[Var], translate(a.expr))
    case ret: tac.ReturnValue[DUVar[ValueInformation]] => ReturnValue(translate(ret.expr))
    case nop: tac.Nop => Nop()
    case pf: tac.PutField[DUVar[ValueInformation]] => PutField(pf.declaringClass, pf.name, pf.declaredFieldType, translate(pf.objRef), translate(pf.value))
    case nvm: tac.NonVirtualMethodCall[DUVar[ValueInformation]] =>
      NonVirtualMethodCall(nvm.declaringClass, nvm.isInterface, nvm.name, translate(nvm.receiver), nvm.params.map(translate(_)))
    case vm: tac.VirtualMethodCall[DUVar[ValueInformation]] =>
      VirtualMethodCall(vm.declaringClass, vm.isInterface, vm.name, translate(vm.receiver), vm.params.map(translate(_)))
    case sm: tac.StaticMethodCall[DUVar[ValueInformation]] =>
      StaticMethodCall(sm.declaringClass, sm.isInterface, sm.name, sm.params.map(translate(_)))
    case e: tac.ExprStmt[DUVar[ValueInformation]] => ExprStmt(translate(e.expr))
  }

  def getVars(stmt: Stmt): Set[Int] = stmt match {
    case If(left, relationalOps, right) => ExprUtil.getVars(left) ++ ExprUtil.getVars(right )
    case Assignment(targetVar, expr) => ExprUtil.getVars(targetVar) ++ ExprUtil.getVars(expr)
    case ReturnValue(ret) => ExprUtil.getVars(ret)
    case PutField(declaringClass, name, declaredFieldType, objRef, value) => ExprUtil.getVars(objRef) ++ ExprUtil.getVars(value)
    case NonVirtualMethodCall(declaringClass, isInterface, name, receiver, params) => ExprUtil.getVars(receiver) ++ params.flatMap(p => ExprUtil.getVars(p)).toSet
    case VirtualMethodCall(declaringClass, isInterface, name, receiver, params) => ExprUtil.getVars(receiver) ++ params.flatMap(p => ExprUtil.getVars(p)).toSet
    case StaticMethodCall(declaringClass, isInterface, name, params) => params.flatMap(p => ExprUtil.getVars(p)).toSet
    case ExprStmt(expr) => ExprUtil.getVars(expr)
    case _ => Set()
  }
}
object RelationalOps extends Enumeration {
  final val LT = Value("<")
  final val < = LT
  final val GT = Value(">")
  final val > = GT
  final val LE = Value("<=")
  final val <= = LE
  final val GE = Value(">=")
  final val >= = GE

  final val EQ = Value("==")
  final val == = EQ
  final val NE = Value("!=")
  final val != = NE

  final val CMPG = Value("cmpg")
  final val CMPL = Value("cmpl")
  final val CMP = Value("cmp")

}

case class If(left: Expr, relationalOps: RelationalOps.Value, right: Expr) extends Stmt
case class Goto() extends Stmt
case class Return() extends Stmt
case class Assignment(targetVar: Var, expr: Expr) extends Stmt
case class ReturnValue(ret: Expr) extends Stmt
case class Nop() extends Stmt
case class PutField(
                    declaringClass: ObjectType,
                    name: String,
                    declaredFieldType: FieldType,
                    objRef: Expr,
                    value: Expr) extends Stmt
case class NonVirtualMethodCall(
                                 declaringClass: ObjectType,
                                 isInterface: Boolean,
                                 name: String,
                                 receiver: Expr,
                                 params: Seq[Expr]
                               ) extends Stmt
case class VirtualMethodCall(
                                 declaringClass: ReferenceType,
                                 isInterface: Boolean,
                                 name: String,
                                 receiver: Expr,
                                 params: Seq[Expr]
                               ) extends Stmt
case class StaticMethodCall(
                              declaringClass: ReferenceType,
                              isInterface: Boolean,
                              name: String,
                              params: Seq[Expr]
                            ) extends Stmt
case class ExprStmt(expr: Expr) extends Stmt


