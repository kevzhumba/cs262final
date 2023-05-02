java.lang.Object getKey()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.lang.Object, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={-1},value=_ <: java.util.HashMap$Node[↦-1;refId=102]))),
	1: ReturnValue(pc=4,UVar(defSites={0},value={_ <: java.lang.Object, null}[↦1;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={0,4,2,1,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3),
	3: useSites={3} (origin=-4),
	4: useSites={4} (origin=-5)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.HashMap$Node[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.HashMap$Node,hash,int,UVar(defSites={-1},value=_ <: java.util.HashMap$Node[↦-1;refId=102]),UVar(defSites={-2},value=an int)),
	2: PutField(pc=11,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={-1},value=_ <: java.util.HashMap$Node[↦-1;refId=102]),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103])),
	3: PutField(pc=16,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={-1},value=_ <: java.util.HashMap$Node[↦-1;refId=102]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104])),
	4: PutField(pc=22,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$Node[↦-1;refId=102]),UVar(defSites={-5},value={_ <: java.util.HashMap$Node, null}[↦-5;refId=105])),
	5: Return(pc=25)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=5) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

