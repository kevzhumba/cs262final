java.util.Iterator iterator()
AITACode(params=(Parameters(
	0: useSites={1} (origin=-1)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2,3},value=java.util.HashMap$KeyIterator[↦0;refId=103],origin=0),New(pc=0,java.util.HashMap$KeyIterator)),
	1: Assignment(pc=5,DVar(useSites={2},value={_ <: java.util.HashMap, null}[↦5;refId=104],origin=1),GetField(pc=5,java.util.HashMap$KeySet,this$0,java.util.HashMap,UVar(defSites={-1},value=java.util.HashMap$KeySet[↦-1;refId=102]))),
	2: NonVirtualMethodCall(pc=8,java.util.HashMap$KeyIterator,isInterface=false,void <init>(java.util.HashMap),UVar(defSites={0},value=java.util.HashMap$KeyIterator[↦0;refId=103]),(UVar(defSites={1},value={_ <: java.util.HashMap, null}[↦5;refId=104]))),
	3: ReturnValue(pc=11,UVar(defSites={0},value=java.util.HashMap$KeyIterator[↦0;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=3,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void <init>(java.util.HashMap)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: PutField(pc=2,java.util.HashMap$KeySet,this$0,java.util.HashMap,UVar(defSites={-1},value=java.util.HashMap$KeySet[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103])),
	1: NonVirtualMethodCall(pc=6,java.util.AbstractSet,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.HashMap$KeySet[↦-1;refId=102]),()),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

