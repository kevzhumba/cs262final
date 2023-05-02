void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$End[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={8} (origin=-1),
	1: useSites={0,4,2,9,7} (origin=-2),
	2: useSites={9,5} (origin=-3),
	3: useSites={9} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Matcher,anchoringBounds,boolean,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=8,DVar(useSites={5},value=an int,origin=2),GetField(pc=8,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: Goto(pc=11,target=5),
	4: Assignment(pc=15,DVar(useSites={5},value=an int,origin=4),VirtualFunctionCall(pc=15,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	5: If(pc=23,UVar(defSites={-3},value=an int),!=,UVar(defSites={4,2},value=an int),target=11),
	6: Assignment(pc=27,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=27,1)),
	7: PutField(pc=28,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={6},value=int = 1)),
	8: Assignment(pc=32,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦32;refId=107],origin=8),GetField(pc=32,java.util.regex.Pattern$End,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$End[↦-1;refId=102]))),
	9: Assignment(pc=38,DVar(useSites={10},value=int ∈ [0,1],origin=9),VirtualFunctionCall(pc=38,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦32;refId=107]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	10: ReturnValue(pc=41,UVar(defSites={9},value=int ∈ [0,1])),
	11: Assignment(pc=42,DVar(useSites={12},value=int = 0,origin=11),IntConst(pc=42,0)),
	12: ReturnValue(pc=43,UVar(defSites={11},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_9,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_7,BB_4}
	BB_2: BasicBlock(start=10,end=10) -> {BB_6}
	BB_3: BasicBlock(start=1,end=1) -> {BB_8,BB_5}
	BB_4: BasicBlock(start=6,end=9) -> {BB_9,BB_2}
	BB_5: BasicBlock(start=2,end=3) -> {BB_1}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=11,end=12) -> {BB_6}
	BB_8: BasicBlock(start=4,end=4) -> {BB_9,BB_1}
	BB_9: ExitNode(normalReturn=false)
))

