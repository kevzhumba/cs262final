boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={1} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$BranchConn,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$BranchConn[↦-1;refId=102]))),
	1: Assignment(pc=7,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=7,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={0},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=105]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	2: ReturnValue(pc=10,UVar(defSites={1},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$BranchConn[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: ReturnValue(pc=4,UVar(defSites={0},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

