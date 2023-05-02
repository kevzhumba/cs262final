package cfg

import org.opalj.br.ObjectType

case class MethodDescription(
                              fqn: String, 
                              numParams: Int, 
                              declaringClass: ObjectType, isStatic: Boolean)
