package lattice

import cfg.MethodDescription
import org.opalj.br.ObjectType

case class AbstractObject(sites: Set[AllocationSite]) extends Value {
}




case class AllocationSite(method: MethodDescription, idx: Int, objectType: ObjectType)