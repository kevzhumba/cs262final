void <init>(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Pos[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Pos,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Pos[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={5,13} (origin=-1),
	1: useSites={0,4,10,6,14,1,3,7} (origin=-2),
	2: useSites={6,14} (origin=-3),
	3: useSites={6,14} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={10,7},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=10,DVar(useSites={2},value=int ∈ [0,1],origin=1),GetField(pc=10,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	2: If(pc=13,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=5),
	3: Assignment(pc=18,DVar(useSites={4},value=an int,origin=3),VirtualFunctionCall(pc=18,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	4: PutField(pc=21,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=25,DVar(useSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦25;refId=107],origin=5),GetField(pc=25,java.util.regex.Pattern$Pos,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Pos[↦-1;refId=102]))),
	6: Assignment(pc=31,DVar(useSites={12},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=31,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦25;refId=107]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	7: PutField(pc=39,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={0},value=an int)),
	8: Goto(pc=42,target=12),
	9: CaughtException(pc=45,<ANY>,caused by={exception[VM]@6,exception@6}),
	10: PutField(pc=50,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={0},value=an int)),
	11: Throw(pc=55,UVar(defSites={-100006,-1000006},value=_ <: java.lang.Throwable[refId=110; values=«java.lang.NullPointerException[↦-100031;refId=108], _ <: java.lang.Throwable[↦-1000031;refId=109]»])),
	12: If(pc=58,UVar(defSites={6},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=18),
	13: Assignment(pc=62,DVar(useSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦62;refId=111],origin=13),GetField(pc=62,java.util.regex.Pattern$Pos,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Pos[↦-1;refId=102]))),
	14: Assignment(pc=68,DVar(useSites={15},value=int ∈ [0,1],origin=14),VirtualFunctionCall(pc=68,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦62;refId=111]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	15: If(pc=71,UVar(defSites={14},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=18),
	16: Assignment(pc=74,DVar(useSites={19},value=int = 1,origin=16),IntConst(pc=74,1)),
	17: Goto(pc=75,target=19),
	18: Assignment(pc=78,DVar(useSites={19},value=int ∈ [0,1],origin=18),IntConst(pc=78,0)),
	19: ReturnValue(pc=79,UVar(defSites={16,18},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_f,BB_3}
	BB_1: BasicBlock(start=5,end=6) -> {BB_7,BB_2}
	BB_2: CatchNode([5,-1)=>9,<none>) -> {BB_4}
	BB_3: BasicBlock(start=1,end=2) -> {BB_8,BB_1}
	BB_4: BasicBlock(start=9,end=11) -> {BB_f}
	BB_5: BasicBlock(start=13,end=14) -> {BB_f,BB_b}
	BB_6: BasicBlock(start=12,end=12) -> {BB_c,BB_5}
	BB_7: BasicBlock(start=7,end=8) -> {BB_6}
	BB_8: BasicBlock(start=3,end=3) -> {BB_f,BB_e}
	BB_9: BasicBlock(start=16,end=17) -> {BB_a}
	BB_a: BasicBlock(start=19,end=19) -> {BB_d}
	BB_b: BasicBlock(start=15,end=15) -> {BB_9,BB_c}
	BB_c: BasicBlock(start=18,end=18) -> {BB_a}
	BB_d: ExitNode(normalReturn=true)
	BB_e: BasicBlock(start=4,end=4) -> {BB_1}
	BB_f: ExitNode(normalReturn=false)
),exceptionHandlers=(
	ExceptionHandler([5, 7) -> 9, <FINALLY>)
))

