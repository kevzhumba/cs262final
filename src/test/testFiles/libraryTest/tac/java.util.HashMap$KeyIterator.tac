void <init>(java.util.HashMap)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={0,1} (origin=-2)
)),stmts=(
	0: PutField(pc=2,java.util.HashMap$KeyIterator,this$0,java.util.HashMap,UVar(defSites={-1},value=java.util.HashMap$KeyIterator[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103])),
	1: NonVirtualMethodCall(pc=7,java.util.HashMap$HashIterator,isInterface=false,void <init>(java.util.HashMap),UVar(defSites={-1},value=java.util.HashMap$KeyIterator[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103]))),
	2: Return(pc=10)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.lang.Object next()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.HashMap$Node, null}[↦1;refId=104],origin=0),VirtualFunctionCall(pc=1,java.util.HashMap$KeyIterator,isInterface=false,java.util.HashMap$Node nextNode(),UVar(defSites={-1},value=java.util.HashMap$KeyIterator[↦-1;refId=102]),())),
	1: Assignment(pc=4,DVar(useSites={2},value={_ <: java.lang.Object, null}[↦4;refId=105],origin=1),GetField(pc=4,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={0},value={_ <: java.util.HashMap$Node, null}[↦1;refId=104]))),
	2: ReturnValue(pc=7,UVar(defSites={1},value={_ <: java.lang.Object, null}[↦4;refId=105]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=2,end=2) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

