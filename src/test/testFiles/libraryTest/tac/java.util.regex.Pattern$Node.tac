boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={0,2} (origin=-1),
	1: useSites={5,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Node[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104]),==,NullExpr(pc=-333),target=5),
	2: Assignment(pc=8,DVar(useSites={3},value={_ <: java.util.regex.Pattern$Node, null}[↦8;refId=105],origin=2),GetField(pc=8,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Node[↦-1;refId=102]))),
	3: Assignment(pc=12,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=12,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={2},value={_ <: java.util.regex.Pattern$Node, null}[↦8;refId=105]),(UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103])))),
	4: ReturnValue(pc=15,UVar(defSites={3},value=int ∈ [0,1])),
	5: Assignment(pc=17,DVar(useSites={6},value=int ∈ [0,1],origin=5),GetField(pc=17,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	6: ReturnValue(pc=20,UVar(defSites={5},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_6,BB_2}
	BB_2: BasicBlock(start=6,end=6) -> {BB_4}
	BB_3: BasicBlock(start=2,end=3) -> {BB_6,BB_5}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=4,end=4) -> {BB_4}
	BB_6: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0,2} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Node[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value={_ <: java.util.regex.Pattern$Node, null}[↦5;refId=104],origin=1),GetStatic(pc=5,java.util.regex.Pattern,accept,java.util.regex.Pattern$Node)),
	2: PutField(pc=8,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Node[↦-1;refId=102]),UVar(defSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦5;refId=104])),
	3: Return(pc=11)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

