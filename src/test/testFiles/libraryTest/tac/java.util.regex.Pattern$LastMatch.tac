boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={4} (origin=-1),
	1: useSites={0,5} (origin=-2),
	2: useSites={1,5} (origin=-3),
	3: useSites={5} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,oldLast,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=5,UVar(defSites={-3},value=an int),==,UVar(defSites={0},value=an int),target=4),
	2: Assignment(pc=8,DVar(useSites={3},value=int = 0,origin=2),IntConst(pc=8,0)),
	3: ReturnValue(pc=9,UVar(defSites={2},value=int = 0)),
	4: Assignment(pc=11,DVar(useSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦11;refId=106],origin=4),GetField(pc=11,java.util.regex.Pattern$LastMatch,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LastMatch[↦-1;refId=102]))),
	5: Assignment(pc=17,DVar(useSites={6},value=int ∈ [0,1],origin=5),VirtualFunctionCall(pc=17,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦11;refId=106]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	6: ReturnValue(pc=20,UVar(defSites={5},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_6,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_3,BB_5}
	BB_2: BasicBlock(start=6,end=6) -> {BB_4}
	BB_3: BasicBlock(start=2,end=3) -> {BB_4}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=4,end=5) -> {BB_6,BB_2}
	BB_6: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$LastMatch[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

