package cfg

import org.opalj.br.ObjectType

/** Class representing a method description
  *
  * @param fqn
  * @param numParams
  * @param declaringClass
  * @param isStatic
  */
case class MethodDescription(
    fqn: String,
    numParams: Int,
    declaringClass: ObjectType,
    isStatic: Boolean
)
