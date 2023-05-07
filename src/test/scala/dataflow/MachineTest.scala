package dataflow

import org.scalatest.matchers.should.Matchers
import org.scalatest.flatspec.AnyFlatSpec
import org.mockito.Mockito._
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
import cfg.ExNode
import cfg.ReturnValue
import cfg.BBEntryNode
import cfg.ExplodedCfg
import protos.dataflow.DataflowServerGrpc
import protos.dataflow.GetCallerInfoResponse
import analyses.{Analysis, ConstantPropagationAnalysis}

class MachineSpec extends AnyFlatSpec with Matchers {
  val machine = new Machine("localhost", 1234)
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
  val cfg = ExplodedCfg(
    exampleBBEntryNode,
    Set(
      BBEntryNode(
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
      ),
      ExNode(
        false,
        MethodDescription(
          "espTest.Foo",
          2,
          ObjectType("espTest / Foo"),
          false
        ),
        List(),
        16
      ),
      ExNode(
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
    ),
    Map(
      15 -> Set(),
      16 -> Set(),
      17 -> Set(
        BBEntryNode(
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
      )
    ),
    Map(
      15 -> Set(
        ExNode(
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
    List()
  )
  machine.cfg = cfg
  val mockStub = mock(classOf[DataflowServerGrpc.DataflowServerBlockingStub])
  val latticeElem =
    machine.valueOperator.getArgs(machine.out.get(exampleBBEntryNode))
  val json = write(latticeElem)
  when(mockStub.getCallerInfo).thenReturn(
    GetCallerInfoResponse(json)
  )
  machine.methodStubs = Map(
    MethodDescription(
      "espTest.Main",
      1,
      ObjectType("espTest / Main"),
      true
    ) -> mockStub
  )

  "computeInForBBEntryNode" should "return the correct input for a BBNode" in {

    val node = exampleBBEntryNode
    val result = machine.computeInForBBEntryNode(node)
    result shouldEqual 1
  }

//   "computeInForCrNode" should "return the correct input for a CRNode" in {
//     val callNode =
//       BBNode(1, List(Instruction("const", "a", "1")), List(), List())
//     val crNode =
//       CRNode(2, List(Instruction("call", "foo", "3")), callNode, List())
//     machine.in.put(callNode, Value.makeInteger(1))
//     machine.cfg =
//       new ExplodedCfg(List(callNode, crNode), List(), List(), Map(), Map())
//     machine.cfg._callees = Map(3 -> List(MethodDescription("foo", List())))
//     val result = machine.computeInForCrNode(crNode)
//     result shouldEqual Value.makeInteger(0)
//   }

//   "computeInForExitNode" should "return the correct input for an ExNode" in {
//     val node1 = BBNode(1, List(Instruction("const", "a", "1")), List(), List())
//     val node2 = BBNode(2, List(Instruction("const", "b", "2")), List(), List())
//     val exitNode = ExNode(3, List(), List(node1, node2))
//     machine.out.put(node1, Value.makeInteger(1))
//     machine.out.put(node2, Value.makeInteger(2))
//     val result = machine.computeInForExitNode(exitNode)
//     result shouldEqual Value.makeInteger(2)
//   }
}
