void <init>(int,java.lang.Object,java.lang.Object,java.util.concurrent.ConcurrentHashMap$Node,java.util.concurrent.ConcurrentHashMap$TreeNode)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4),
	4: useSites={0} (origin=-5),
	5: useSites={1} (origin=-6)
)),stmts=(
	0: NonVirtualMethodCall(pc=6,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.concurrent.ConcurrentHashMap$Node),UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={-5},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-5;refId=105]))),
	1: PutField(pc=12,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),UVar(defSites={-6},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-6;refId=106])),
	2: Return(pc=15)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

