void <init>(java.util.concurrent.ConcurrentHashMap$Node[])
AITACode(params=(Parameters(
	0: useSites={4,3} (origin=-1),
	1: useSites={4} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={3},value=int = -1,origin=0),IntConst(pc=1,-1)),
	1: Assignment(pc=2,DVar(useSites={3},value=null[↦2],origin=1),NullExpr(pc=2)),
	2: Assignment(pc=3,DVar(useSites={3},value=null[↦3],origin=2),NullExpr(pc=3)),
	3: NonVirtualMethodCall(pc=4,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object),UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$ForwardingNode[↦-1;refId=102]),(UVar(defSites={0},value=int = -1),UVar(defSites={1},value=null[↦2]),UVar(defSites={2},value=null[↦3]))),
	4: PutField(pc=9,java.util.concurrent.ConcurrentHashMap$ForwardingNode,nextTable,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$ForwardingNode[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-2;refId=103])),
	5: Return(pc=12)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=4,end=5) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

