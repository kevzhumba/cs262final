void <init>(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=2,java.util.regex.Pattern$Start,isInterface=false,void <init>(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern$StartS[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]))),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={12,1,9} (origin=-1),
	1: useSites={0,16,8,20,18,22,5,13,39,15} (origin=-2),
	2: useSites={28,26,13,3,11,27,15} (origin=-3),
	3: useSites={28,33,13,31} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$StartS,minLength,int,UVar(defSites={-1},value=java.util.regex.Pattern$StartS[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=9,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={1},value=an int))),
	3: If(pc=10,UVar(defSites={-3},value=an int),<=,UVar(defSites={2},value=an int),target=8),
	4: Assignment(pc=14,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=14,1)),
	5: PutField(pc=15,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={4},value=int = 1)),
	6: Assignment(pc=18,DVar(useSites={7},value=int = 0,origin=6),IntConst(pc=18,0)),
	7: ReturnValue(pc=19,UVar(defSites={6},value=int = 0)),
	8: Assignment(pc=21,DVar(useSites={10},value=an int,origin=8),GetField(pc=21,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	9: Assignment(pc=25,DVar(useSites={10},value=an int,origin=9),GetField(pc=25,java.util.regex.Pattern$StartS,minLength,int,UVar(defSites={-1},value=java.util.regex.Pattern$StartS[↦-1;refId=102]))),
	10: Assignment(pc=28,DVar(useSites={26,11},value=an int,origin=10),BinaryExpr(pc=28,ComputationalTypeInt,UVar(defSites={8},value=an int),-,UVar(defSites={9},value=an int))),
	11: If(pc=34,UVar(defSites={36,-3,27},value=an int),>,UVar(defSites={10},value=an int),target=38),
	12: Assignment(pc=38,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦38;refId=106],origin=12),GetField(pc=38,java.util.regex.Pattern$StartS,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$StartS[↦-1;refId=102]))),
	13: Assignment(pc=44,DVar(useSites={14},value=int ∈ [0,1],origin=13),VirtualFunctionCall(pc=44,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node, null}[↦38;refId=106]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={36,-3,27},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	14: If(pc=47,UVar(defSites={13},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=26),
	15: PutField(pc=52,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={36,-3,27},value=an int)),
	16: Assignment(pc=56,DVar(useSites={19},value={int[], null}[↦56;refId=109],origin=16),GetField(pc=56,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	17: Assignment(pc=59,DVar(useSites={19},value=int = 0,origin=17),IntConst(pc=59,0)),
	18: Assignment(pc=61,DVar(useSites={19},value=an int,origin=18),GetField(pc=61,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	19: ArrayStore(pc=64,UVar(defSites={16},value={int[], null}[↦56;refId=109]),UVar(defSites={17},value=int = 0),UVar(defSites={18},value=an int)),
	20: Assignment(pc=66,DVar(useSites={23},value={int[], null}[↦66;refId=112],origin=20),GetField(pc=66,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	21: Assignment(pc=69,DVar(useSites={23},value=int = 1,origin=21),IntConst(pc=69,1)),
	22: Assignment(pc=71,DVar(useSites={23},value=an int,origin=22),GetField(pc=71,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	23: ArrayStore(pc=74,UVar(defSites={20},value={int[], null}[↦66;refId=112]),UVar(defSites={21},value=int = 1),UVar(defSites={22},value=an int)),
	24: Assignment(pc=75,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=75,1)),
	25: ReturnValue(pc=76,UVar(defSites={24},value=int = 1)),
	26: If(pc=80,UVar(defSites={36,-3,27},value=an int),==,UVar(defSites={10},value=an int),target=38),
	27: Assignment(pc=88,DVar(useSites={32,36,28,26,33,13,11,15},value=an int,origin=27),BinaryExpr(pc=88,ComputationalTypeInt,UVar(defSites={36,-3,27},value=an int),+,IntConst(pc=88,1))),
	28: Assignment(pc=91,DVar(useSites={29},value=int ∈ [0,65535],origin=28),VirtualFunctionCall(pc=91,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={36,-3,27},value=an int)))),
	29: Assignment(pc=96,DVar(useSites={30},value=int ∈ [0,1],origin=29),StaticFunctionCall(pc=96,java.lang.Character,isInterface=false,boolean isHighSurrogate(char),(UVar(defSites={28},value=int ∈ [0,65535])))),
	30: If(pc=99,UVar(defSites={29},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	31: Assignment(pc=104,DVar(useSites={32},value=an int,origin=31),VirtualFunctionCall(pc=104,java.lang.CharSequence,isInterface=true,int length(),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),())),
	32: If(pc=109,UVar(defSites={27},value=an int),>=,UVar(defSites={31},value=an int),target=11),
	33: Assignment(pc=114,DVar(useSites={34},value=int ∈ [0,65535],origin=33),VirtualFunctionCall(pc=114,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),(UVar(defSites={27},value=int ∈ [-2147483648,2147483646])))),
	34: Assignment(pc=119,DVar(useSites={35},value=int ∈ [0,1],origin=34),StaticFunctionCall(pc=119,java.lang.Character,isInterface=false,boolean isLowSurrogate(char),(UVar(defSites={33},value=int ∈ [0,65535])))),
	35: If(pc=122,UVar(defSites={34},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	36: Assignment(pc=125,DVar(useSites={28,26,13,11,27,15},value=int ∈ [-2147483647,2147483647],origin=36),BinaryExpr(pc=125,ComputationalTypeInt,UVar(defSites={27},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=125,1))),
	37: Goto(pc=128,target=11),
	38: Assignment(pc=132,DVar(useSites={39},value=int = 1,origin=38),IntConst(pc=132,1)),
	39: PutField(pc=133,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={38},value=int = 1)),
	40: Assignment(pc=136,DVar(useSites={41},value=int = 0,origin=40),IntConst(pc=136,0)),
	41: ReturnValue(pc=137,UVar(defSites={40},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_16,BB_3}
	BB_10: BasicBlock(start=33,end=33) -> {BB_16,BB_12}
	BB_11: BasicBlock(start=32,end=32) -> {BB_10,BB_9}
	BB_12: BasicBlock(start=34,end=34) -> {BB_16,BB_6}
	BB_13: BasicBlock(start=36,end=37) -> {BB_9}
	BB_14: BasicBlock(start=30,end=30) -> {BB_8,BB_9}
	BB_15: BasicBlock(start=4,end=7) -> {BB_7}
	BB_16: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=24,end=25) -> {BB_7}
	BB_2: BasicBlock(start=14,end=14) -> {BB_c,BB_a}
	BB_3: BasicBlock(start=1,end=3) -> {BB_b,BB_15}
	BB_4: BasicBlock(start=27,end=28) -> {BB_16,BB_e}
	BB_5: BasicBlock(start=12,end=13) -> {BB_16,BB_2}
	BB_6: BasicBlock(start=35,end=35) -> {BB_13,BB_9}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=31,end=31) -> {BB_16,BB_11}
	BB_9: BasicBlock(start=11,end=11) -> {BB_5,BB_f}
	BB_a: BasicBlock(start=26,end=26) -> {BB_f,BB_4}
	BB_b: BasicBlock(start=8,end=10) -> {BB_9}
	BB_c: BasicBlock(start=15,end=19) -> {BB_16,BB_d}
	BB_d: BasicBlock(start=20,end=23) -> {BB_16,BB_1}
	BB_e: BasicBlock(start=29,end=29) -> {BB_16,BB_14}
	BB_f: BasicBlock(start=38,end=41) -> {BB_7}
))

