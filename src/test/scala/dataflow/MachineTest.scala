package dataflow

import org.scalatest.matchers.should.Matchers
import org.scalatest.flatspec.AnyFlatSpec
import org.mockito.Mockito._
import org.mockito.ArgumentMatchers.any
import cfg.{
  BBNode,
  MethodDescription,
  Assignment,
  BinExpr,
  BinOps,
  StaticFunctionCall,
  StaticMethodCall,
  StmtNode,
  UnExpr,
  UnOps,
  Var,
  VirtualFunctionCall,
  VirtualMethodCall
}
import lattice.{AbstractObject, AllocationSite, Constant, Integer}
import org.opalj.br.{ObjectType, VirtualMethod}
import org.json4s._
import org.json4s.native.Serialization
import org.json4s.native.Serialization.{read, write}
import cfg.{ExNode, ReturnValue, BBEntryNode, ExplodedCfg, CRNode}
import protos.dataflow.{
  GetCallerInfoResponse,
  GetCalleeInfoResponse,
  DataflowServerGrpc
}

class MachineSpec extends AnyFlatSpec with Matchers {
  val machine = new Machine("localhost", 1234)
  implicit val formats = machine.formats

  // Create example nodes for example cfg
  val exampleBBEntryNode = BBEntryNode(
    MethodDescription(
      "espTest.Foo",
      2,
      ObjectType("espTest / Foo"),
      false
    ),
    List(
      StmtNode(
        Assignment(
          Var(List(0)),
          BinExpr(Var(List(-2)), BinOps.Add, Var(List(-3)))
        ),
        MethodDescription(
          "espTest.Foo",
          2,
          ObjectType("espTest / Foo"),
          false
        ),
        false,
        15,
        0
      ),
      StmtNode(
        ReturnValue(Var(List(0))),
        MethodDescription(
          "espTest.Foo",
          2,
          ObjectType("espTest / Foo"),
          false
        ),
        false,
        15,
        1
      )
    ),
    15
  )
  val exampleExNode = ExNode(
    false,
    MethodDescription(
      "espTest.Foo",
      2,
      ObjectType("espTest / Foo"),
      false
    ),
    List(),
    16
  )
  val exampleExNode2 = ExNode(
    true,
    MethodDescription(
      "espTest.Foo",
      2,
      ObjectType("espTest / Foo"),
      false
    ),
    List(),
    17
  )

  val exampleCfg = ExplodedCfg(
    exampleBBEntryNode,
    Set(
      exampleBBEntryNode,
      exampleExNode,
      exampleExNode2
    ),
    Map(
      15 -> Set(),
      16 -> Set(),
      17 -> Set(
        exampleBBEntryNode
      )
    ),
    Map(
      15 -> Set(
        exampleExNode2
      ),
      16 -> Set(),
      17 -> Set()
    ),
    List(
      (
        4,
        MethodDescription("espTest.Main", 1, ObjectType("espTest / Main"), true)
      )
    ),
    List(
      (
        1,
        List(
          MethodDescription(
            "espTest.Foo",
            2,
            ObjectType("espTest / Foo"),
            false
          )
        )
      )
    )
  )

  // Initialize cfg and machine data structures, mock grpc stubs
  machine.cfg = exampleCfg
  val mockStub = mock(classOf[DataflowServerGrpc.DataflowServerBlockingStub])
  val latticeElem = Map() +
    ("1" -> (Integer(false, Some(5)), AbstractObject(Set())))
  val json = write(latticeElem)
  when(mockStub.getCallerInfo(any())).thenReturn(
    GetCallerInfoResponse(json)
  )
  when(mockStub.getCalleeInfo(any())).thenReturn(
    GetCalleeInfoResponse(json)
  )
  val exampleMethodDescription = MethodDescription(
    "espTest.Main",
    1,
    ObjectType("espTest / Main"),
    true
  )
  machine.methodStubs = Map(
    exampleMethodDescription -> mockStub,
    MethodDescription(
      "espTest.Foo",
      2,
      ObjectType("espTest / Foo"),
      false
    ) -> mockStub
  )
  machine.method = exampleMethodDescription
  machine.in.put(exampleBBEntryNode, Constant(latticeElem))
  machine.out.put(exampleBBEntryNode, Constant(latticeElem))

  "computeInForBBEntryNode" should "return the correct input for a BBENode" in {
    val node = exampleBBEntryNode
    val result = machine.computeInForBBEntryNode(node)
    result shouldEqual Constant(latticeElem)
  }

  "computeInForCrNode" should "return the correct input for a CRNode" in {
    val node = CRNode(
      MethodDescription(
        "espTest.Foo",
        2,
        ObjectType("espTest / Foo"),
        false
      ),
      List(
        StmtNode(
          ReturnValue(Var(List(0))),
          MethodDescription(
            "espTest.Foo",
            2,
            ObjectType("espTest / Foo"),
            false
          ),
          false,
          15,
          1
        )
      ),
      17
    )
    val result = machine.computeInForCrNode(node)
    result shouldEqual Constant(
      Map(
        "1" -> (Integer(false, Some(5)), AbstractObject(Set())),
        "returnFromCallee" -> (Integer(true, None), AbstractObject(Set()))
      )
    )
  }

  "computeInForExitNode" should "return the correct input for an ExNode" in {
    val node = exampleExNode2
    val result = machine.computeInForExitNode(node)
    result shouldEqual Constant(Map())
  }

  "computeInForBBNode" should "return the correct input for an BBNode" in {
    val node = BBNode(
      MethodDescription(
        "espTest.Foo",
        2,
        ObjectType("espTest / Foo"),
        false
      ),
      List(),
      17
    )
    val result = machine.computeInForBBNode(node)
    result shouldEqual Constant(latticeElem)
  }
}
