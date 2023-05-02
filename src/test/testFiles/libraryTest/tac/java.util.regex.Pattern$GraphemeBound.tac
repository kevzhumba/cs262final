void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$GraphemeBound[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={8,28} (origin=-1),
	1: useSites={0,2,1,9,25,5,29,27} (origin=-2),
	2: useSites={18,9,13,29,19,11,7,15} (origin=-3),
	3: useSites={18,14,9,29,19,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={7},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,from,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=7,DVar(useSites={11},value=an int,origin=1),GetField(pc=7,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	2: Assignment(pc=13,DVar(useSites={3},value=int ∈ [0,1],origin=2),GetField(pc=13,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: If(pc=16,UVar(defSites={2},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=7),
	4: Assignment(pc=19,DVar(useSites={7},value=int = 0,origin=4),IntConst(pc=19,0)),
	5: Assignment(pc=23,DVar(useSites={11},value=an int,origin=5),VirtualFunctionCall(pc=23,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	6: Nop(pc=26),
	7: If(pc=31,UVar(defSites={-3},value=an int),!=,UVar(defSites={0,4},value=an int),target=11),
	8: Assignment(pc=35,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦35;refId=114],origin=8),GetField(pc=35,java.util.regex.Pattern$GraphemeBound,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$GraphemeBound[↦-1;refId=102]))),
	9: Assignment(pc=41,DVar(useSites={10},value=int ∈ [0,1],origin=9),VirtualFunctionCall(pc=41,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦35;refId=114]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	10: ReturnValue(pc=44,UVar(defSites={9},value=int ∈ [0,1])),
	11: If(pc=48,UVar(defSites={-3},value=an int),>=,UVar(defSites={1,5},value=an int),target=24),
	12: Assignment(pc=53,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=53,1)),
	13: Assignment(pc=54,DVar(useSites={14},value=an int,origin=13),BinaryExpr(pc=54,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),-,UVar(defSites={12},value=int = 1))),
	14: Assignment(pc=55,DVar(useSites={16},value=int ∈ [0,65535],origin=14),VirtualFunctionCall(pc=55,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={13},value=an int)))),
	15: Assignment(pc=62,DVar(useSites={16},value=int ∈ [0,65535],origin=15),VirtualFunctionCall(pc=62,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),(UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	16: Assignment(pc=67,DVar(useSites={17},value=int ∈ [0,1],origin=16),StaticFunctionCall(pc=67,java.lang.Character,isInterface=false,boolean isSurrogatePair(char,char),(UVar(defSites={14},value=int ∈ [0,65535]),UVar(defSites={15},value=int ∈ [0,65535])))),
	17: If(pc=70,UVar(defSites={16},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=22),
	18: Assignment(pc=75,DVar(useSites={20},value=an int,origin=18),StaticFunctionCall(pc=75,java.lang.Character,isInterface=false,int codePointBefore(java.lang.CharSequence,int),(UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	19: Assignment(pc=80,DVar(useSites={20},value=an int,origin=19),StaticFunctionCall(pc=80,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	20: Assignment(pc=83,DVar(useSites={21},value=int ∈ [0,1],origin=20),StaticFunctionCall(pc=83,java.util.regex.Grapheme,isInterface=false,boolean isBoundary(int,int),(UVar(defSites={18},value=an int),UVar(defSites={19},value=an int)))),
	21: If(pc=86,UVar(defSites={20},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=28),
	22: Assignment(pc=89,DVar(useSites={23},value=int = 0,origin=22),IntConst(pc=89,0)),
	23: ReturnValue(pc=90,UVar(defSites={22},value=int = 0)),
	24: Assignment(pc=92,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=92,1)),
	25: PutField(pc=93,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={24},value=int = 1)),
	26: Assignment(pc=97,DVar(useSites={27},value=int = 1,origin=26),IntConst(pc=97,1)),
	27: PutField(pc=98,java.util.regex.Matcher,requireEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={26},value=int = 1)),
	28: Assignment(pc=102,DVar(useSites={29},value={_ <: java.util.regex.Pattern$Node, null}[↦102;refId=117],origin=28),GetField(pc=102,java.util.regex.Pattern$GraphemeBound,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$GraphemeBound[↦-1;refId=102]))),
	29: Assignment(pc=108,DVar(useSites={30},value=int ∈ [0,1],origin=29),VirtualFunctionCall(pc=108,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦102;refId=117]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	30: ReturnValue(pc=111,UVar(defSites={29},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_15,BB_4}
	BB_10: BasicBlock(start=18,end=18) -> {BB_15,BB_13}
	BB_11: ExitNode(normalReturn=true)
	BB_12: BasicBlock(start=30,end=30) -> {BB_11}
	BB_13: BasicBlock(start=19,end=19) -> {BB_15,BB_3}
	BB_14: BasicBlock(start=4,end=5) -> {BB_15,BB_5}
	BB_15: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=10,end=10) -> {BB_11}
	BB_2: BasicBlock(start=24,end=27) -> {BB_e}
	BB_3: BasicBlock(start=20,end=20) -> {BB_15,BB_f}
	BB_4: BasicBlock(start=1,end=3) -> {BB_9,BB_14}
	BB_5: BasicBlock(start=6,end=6) -> {BB_9}
	BB_6: BasicBlock(start=17,end=17) -> {BB_10,BB_7}
	BB_7: BasicBlock(start=22,end=23) -> {BB_11}
	BB_8: BasicBlock(start=12,end=14) -> {BB_15,BB_d}
	BB_9: BasicBlock(start=7,end=7) -> {BB_c,BB_b}
	BB_a: BasicBlock(start=16,end=16) -> {BB_15,BB_6}
	BB_b: BasicBlock(start=11,end=11) -> {BB_8,BB_2}
	BB_c: BasicBlock(start=8,end=9) -> {BB_15,BB_1}
	BB_d: BasicBlock(start=15,end=15) -> {BB_15,BB_a}
	BB_e: BasicBlock(start=28,end=29) -> {BB_15,BB_12}
	BB_f: BasicBlock(start=21,end=21) -> {BB_7,BB_e}
))

