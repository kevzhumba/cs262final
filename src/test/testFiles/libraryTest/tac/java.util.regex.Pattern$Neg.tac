void <init>(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Neg[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Neg,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Neg[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={16,29,7} (origin=-1),
	1: useSites={0,8,4,26,30,1,17,5,3,23,15} (origin=-2),
	2: useSites={8,6,30,17} (origin=-3),
	3: useSites={8,30,17} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={26,23},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=10,DVar(useSites={2},value=int ∈ [0,1],origin=1),GetField(pc=10,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	2: If(pc=13,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=5),
	3: Assignment(pc=18,DVar(useSites={4},value=an int,origin=3),VirtualFunctionCall(pc=18,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	4: PutField(pc=21,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=26,DVar(useSites={6},value=an int,origin=5),GetField(pc=26,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	6: If(pc=29,UVar(defSites={-3},value=an int),>=,UVar(defSites={5},value=an int),target=14),
	7: Assignment(pc=33,DVar(useSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦33;refId=111],origin=7),GetField(pc=33,java.util.regex.Pattern$Neg,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Neg[↦-1;refId=102]))),
	8: Assignment(pc=39,DVar(useSites={9},value=int ∈ [0,1],origin=8),VirtualFunctionCall(pc=39,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦33;refId=111]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	9: If(pc=42,UVar(defSites={8},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=12),
	10: Assignment(pc=45,DVar(useSites={28},value=int = 1,origin=10),IntConst(pc=45,1)),
	11: Goto(pc=46,target=13),
	12: Assignment(pc=49,DVar(useSites={28},value=int ∈ [0,1],origin=12),IntConst(pc=49,0)),
	13: Goto(pc=52,target=23),
	14: Assignment(pc=56,DVar(useSites={15},value=int = 1,origin=14),IntConst(pc=56,1)),
	15: PutField(pc=57,java.util.regex.Matcher,requireEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={14},value=int = 1)),
	16: Assignment(pc=61,DVar(useSites={17},value={_ <: java.util.regex.Pattern$Node, null}[↦61;refId=107],origin=16),GetField(pc=61,java.util.regex.Pattern$Neg,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Neg[↦-1;refId=102]))),
	17: Assignment(pc=67,DVar(useSites={18},value=int ∈ [0,1],origin=17),VirtualFunctionCall(pc=67,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={16},value={_ <: java.util.regex.Pattern$Node, null}[↦61;refId=107]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	18: If(pc=70,UVar(defSites={17},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=21),
	19: Assignment(pc=73,DVar(useSites={28},value=int = 1,origin=19),IntConst(pc=73,1)),
	20: Goto(pc=74,target=22),
	21: Assignment(pc=77,DVar(useSites={28},value=int ∈ [0,1],origin=21),IntConst(pc=77,0)),
	22: Nop(pc=78),
	23: PutField(pc=83,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={0},value=an int)),
	24: Goto(pc=86,target=28),
	25: CaughtException(pc=89,<ANY>,caused by={exception[VM]@8,exception@8,exception[VM]@17,exception@17}),
	26: PutField(pc=94,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={0},value=an int)),
	27: Throw(pc=99,UVar(defSites={-100008,-1000008,-100017,-1000017},value=_ <: java.lang.Throwable[refId=115; values=«java.lang.NullPointerException[↦-100067;refId=108], _ <: java.lang.Throwable[↦-1000067;refId=109], java.lang.NullPointerException[↦-100039;refId=112], _ <: java.lang.Throwable[↦-1000039;refId=113]»])),
	28: If(pc=102,UVar(defSites={12,10,21,19},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=34),
	29: Assignment(pc=106,DVar(useSites={30},value={_ <: java.util.regex.Pattern$Node, null}[↦106;refId=116],origin=29),GetField(pc=106,java.util.regex.Pattern$Neg,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Neg[↦-1;refId=102]))),
	30: Assignment(pc=112,DVar(useSites={31},value=int ∈ [0,1],origin=30),VirtualFunctionCall(pc=112,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={29},value={_ <: java.util.regex.Pattern$Node, null}[↦106;refId=116]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	31: If(pc=115,UVar(defSites={30},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=34),
	32: Assignment(pc=118,DVar(useSites={35},value=int = 1,origin=32),IntConst(pc=118,1)),
	33: Goto(pc=119,target=35),
	34: Assignment(pc=122,DVar(useSites={35},value=int ∈ [0,1],origin=34),IntConst(pc=122,0)),
	35: ReturnValue(pc=123,UVar(defSites={32,34},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_19,BB_5}
	BB_10: BasicBlock(start=28,end=28) -> {BB_13,BB_f}
	BB_11: BasicBlock(start=21,end=21) -> {BB_8}
	BB_12: BasicBlock(start=32,end=33) -> {BB_15}
	BB_13: BasicBlock(start=34,end=34) -> {BB_15}
	BB_14: BasicBlock(start=3,end=3) -> {BB_19,BB_18}
	BB_15: BasicBlock(start=35,end=35) -> {BB_17}
	BB_16: BasicBlock(start=18,end=18) -> {BB_d,BB_11}
	BB_17: ExitNode(normalReturn=true)
	BB_18: BasicBlock(start=4,end=4) -> {BB_1}
	BB_19: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=6) -> {BB_a,BB_4}
	BB_2: BasicBlock(start=10,end=11) -> {BB_7}
	BB_3: BasicBlock(start=25,end=27) -> {BB_19}
	BB_4: BasicBlock(start=14,end=17) -> {BB_16,BB_e}
	BB_5: BasicBlock(start=1,end=2) -> {BB_14,BB_1}
	BB_6: BasicBlock(start=9,end=9) -> {BB_9,BB_2}
	BB_7: BasicBlock(start=13,end=13) -> {BB_c}
	BB_8: BasicBlock(start=22,end=22) -> {BB_c}
	BB_9: BasicBlock(start=12,end=12) -> {BB_7}
	BB_a: BasicBlock(start=7,end=8) -> {BB_6,BB_e}
	BB_b: BasicBlock(start=31,end=31) -> {BB_13,BB_12}
	BB_c: BasicBlock(start=23,end=24) -> {BB_10}
	BB_d: BasicBlock(start=19,end=20) -> {BB_8}
	BB_e: CatchNode([5,23)=>25,<none>) -> {BB_3}
	BB_f: BasicBlock(start=29,end=30) -> {BB_19,BB_b}
),exceptionHandlers=(
	ExceptionHandler([5, 23) -> 25, <FINALLY>)
))

