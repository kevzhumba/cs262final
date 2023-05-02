void <init>(int,java.lang.Object,java.lang.Object,java.util.concurrent.ConcurrentHashMap$Node)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4),
	4: useSites={1} (origin=-5)
)),stmts=(
	0: NonVirtualMethodCall(pc=4,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]))),
	1: PutField(pc=10,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦-1;refId=102]),UVar(defSites={-5},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-5;refId=105])),
	2: Return(pc=13)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void <init>(int,java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={0,2,1,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3),
	3: useSites={3} (origin=-4)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦-1;refId=102]),UVar(defSites={-2},value=an int)),
	2: PutField(pc=11,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦-1;refId=102]),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103])),
	3: PutField(pc=16,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦-1;refId=102]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104])),
	4: Return(pc=19)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=4) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

