boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={52,54,41,5,39,63} (origin=-1),
	1: useSites={0,64,4,60,2,42,62,55} (origin=-2),
	2: useSites={64,28,42,14,33,9,21,27,55,15,31} (origin=-3),
	3: useSites={64,28,34,42,22,55,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Matcher,anchoringBounds,boolean,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=8,DVar(useSites={8,13,27},value=an int,origin=2),GetField(pc=8,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: Goto(pc=11,target=5),
	4: Assignment(pc=15,DVar(useSites={8,13,27},value=an int,origin=4),VirtualFunctionCall(pc=15,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	5: Assignment(pc=21,DVar(useSites={6},value=int ∈ [0,1],origin=5),GetField(pc=21,java.util.regex.Pattern$Dollar,multiline,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]))),
	6: If(pc=24,UVar(defSites={5},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=27),
	7: Assignment(pc=30,DVar(useSites={8},value=int = 2,origin=7),IntConst(pc=30,2)),
	8: Assignment(pc=31,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=31,ComputationalTypeInt,UVar(defSites={4,2},value=an int),-,UVar(defSites={7},value=int = 2))),
	9: If(pc=32,UVar(defSites={-3},value=an int),>=,UVar(defSites={8},value=an int),target=12),
	10: Assignment(pc=35,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=35,0)),
	11: ReturnValue(pc=36,UVar(defSites={10},value=int = 0)),
	12: Assignment(pc=40,DVar(useSites={13},value=int = 2,origin=12),IntConst(pc=40,2)),
	13: Assignment(pc=41,DVar(useSites={14},value=an int,origin=13),BinaryExpr(pc=41,ComputationalTypeInt,UVar(defSites={4,2},value=an int),-,UVar(defSites={12},value=int = 2))),
	14: If(pc=42,UVar(defSites={-3},value=an int),!=,UVar(defSites={13},value=an int),target=27),
	15: Assignment(pc=47,DVar(useSites={17},value=int ∈ [0,65535],origin=15),VirtualFunctionCall(pc=47,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={-3},value=an int)))),
	16: Assignment(pc=56,DVar(useSites={17},value=int = 13,origin=16),IntConst(pc=56,13)),
	17: If(pc=58,UVar(defSites={15},value=int ∈ [0,65535]),==,UVar(defSites={16},value=int = 13),target=20),
	18: Assignment(pc=61,DVar(useSites={19},value=int = 0,origin=18),IntConst(pc=61,0)),
	19: ReturnValue(pc=62,UVar(defSites={18},value=int = 0)),
	20: Assignment(pc=65,DVar(useSites={21},value=int = 1,origin=20),IntConst(pc=65,1)),
	21: Assignment(pc=66,DVar(useSites={22},value=an int,origin=21),BinaryExpr(pc=66,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={20},value=int = 1))),
	22: Assignment(pc=67,DVar(useSites={24},value=int ∈ [0,65535],origin=22),VirtualFunctionCall(pc=67,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),(UVar(defSites={21},value=an int)))),
	23: Assignment(pc=76,DVar(useSites={24},value=int = 10,origin=23),IntConst(pc=76,10)),
	24: If(pc=78,UVar(defSites={22},value=int ∈ [0,65535]),==,UVar(defSites={23},value=int = 10),target=27),
	25: Assignment(pc=81,DVar(useSites={26},value=int = 0,origin=25),IntConst(pc=81,0)),
	26: ReturnValue(pc=82,UVar(defSites={25},value=int = 0)),
	27: If(pc=86,UVar(defSites={-3},value=an int),>=,UVar(defSites={4,2},value=an int),target=59),
	28: Assignment(pc=91,DVar(useSites={30,49,45,47},value=int ∈ [0,65535],origin=28),VirtualFunctionCall(pc=91,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	29: Assignment(pc=100,DVar(useSites={30},value=int = 10,origin=29),IntConst(pc=100,10)),
	30: If(pc=102,UVar(defSites={28},value=int ∈ [0,65535]),!=,UVar(defSites={29},value=int = 10),target=44),
	31: If(pc=106,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),<=,IntConst(pc=-333,0),target=39),
	32: Assignment(pc=111,DVar(useSites={33},value=int = 1,origin=32),IntConst(pc=111,1)),
	33: Assignment(pc=112,DVar(useSites={34},value=int ∈ [0,2147483645],origin=33),BinaryExpr(pc=112,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [1,2147483646]),-,UVar(defSites={32},value=int = 1))),
	34: Assignment(pc=113,DVar(useSites={36},value=int ∈ [0,65535],origin=34),VirtualFunctionCall(pc=113,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),(UVar(defSites={33},value=int ∈ [0,2147483645])))),
	35: Assignment(pc=118,DVar(useSites={36},value=int = 13,origin=35),IntConst(pc=118,13)),
	36: If(pc=120,UVar(defSites={34},value=int ∈ [0,65535]),!=,UVar(defSites={35},value=int = 13),target=39),
	37: Assignment(pc=123,DVar(useSites={38},value=int = 0,origin=37),IntConst(pc=123,0)),
	38: ReturnValue(pc=124,UVar(defSites={37},value=int = 0)),
	39: Assignment(pc=126,DVar(useSites={40},value=int ∈ [0,1],origin=39),GetField(pc=126,java.util.regex.Pattern$Dollar,multiline,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]))),
	40: If(pc=129,UVar(defSites={39},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=59),
	41: Assignment(pc=133,DVar(useSites={42},value={_ <: java.util.regex.Pattern$Node, null}[↦133;refId=119],origin=41),GetField(pc=133,java.util.regex.Pattern$Dollar,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]))),
	42: Assignment(pc=139,DVar(useSites={43},value=int ∈ [0,1],origin=42),VirtualFunctionCall(pc=139,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={41},value={_ <: java.util.regex.Pattern$Node, null}[↦133;refId=119]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	43: ReturnValue(pc=142,UVar(defSites={42},value=int ∈ [0,1])),
	44: Assignment(pc=145,DVar(useSites={45},value=int = 13,origin=44),IntConst(pc=145,13)),
	45: If(pc=147,UVar(defSites={28},value=int ∈ [0,65535]),==,UVar(defSites={44},value=int = 13),target=52),
	46: Assignment(pc=152,DVar(useSites={47},value=int = 133,origin=46),IntConst(pc=152,133)),
	47: If(pc=155,UVar(defSites={28},value=int ∈ [0,65535]),==,UVar(defSites={46},value=int = 133),target=52),
	48: Assignment(pc=160,DVar(useSites={49},value=int = 1,origin=48),IntConst(pc=160,1)),
	49: Assignment(pc=161,DVar(useSites={51},value=int ∈ [0,131071],origin=49),BinaryExpr(pc=161,ComputationalTypeInt,UVar(defSites={28},value=int ∈ [0,65535]),|,UVar(defSites={48},value=int = 1))),
	50: Assignment(pc=162,DVar(useSites={51},value=int = 8233,origin=50),IntConst(pc=162,8233)),
	51: If(pc=165,UVar(defSites={49},value=int ∈ [0,131071]),!=,UVar(defSites={50},value=int = 8233),target=57),
	52: Assignment(pc=169,DVar(useSites={53},value=int ∈ [0,1],origin=52),GetField(pc=169,java.util.regex.Pattern$Dollar,multiline,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]))),
	53: If(pc=172,UVar(defSites={52},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=59),
	54: Assignment(pc=176,DVar(useSites={55},value={_ <: java.util.regex.Pattern$Node, null}[↦176;refId=116],origin=54),GetField(pc=176,java.util.regex.Pattern$Dollar,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]))),
	55: Assignment(pc=182,DVar(useSites={56},value=int ∈ [0,1],origin=55),VirtualFunctionCall(pc=182,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={54},value={_ <: java.util.regex.Pattern$Node, null}[↦176;refId=116]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	56: ReturnValue(pc=185,UVar(defSites={55},value=int ∈ [0,1])),
	57: Assignment(pc=186,DVar(useSites={58},value=int = 0,origin=57),IntConst(pc=186,0)),
	58: ReturnValue(pc=187,UVar(defSites={57},value=int = 0)),
	59: Assignment(pc=189,DVar(useSites={60},value=int = 1,origin=59),IntConst(pc=189,1)),
	60: PutField(pc=190,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={59},value=int = 1)),
	61: Assignment(pc=194,DVar(useSites={62},value=int = 1,origin=61),IntConst(pc=194,1)),
	62: PutField(pc=195,java.util.regex.Matcher,requireEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={61},value=int = 1)),
	63: Assignment(pc=199,DVar(useSites={64},value={_ <: java.util.regex.Pattern$Node, null}[↦199;refId=113],origin=63),GetField(pc=199,java.util.regex.Pattern$Dollar,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]))),
	64: Assignment(pc=205,DVar(useSites={65},value=int ∈ [0,1],origin=64),VirtualFunctionCall(pc=205,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={63},value={_ <: java.util.regex.Pattern$Node, null}[↦199;refId=113]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	65: ReturnValue(pc=208,UVar(defSites={64},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_22,BB_3}
	BB_10: BasicBlock(start=25,end=26) -> {BB_1e}
	BB_11: BasicBlock(start=20,end=22) -> {BB_22,BB_b}
	BB_12: BasicBlock(start=46,end=47) -> {BB_2,BB_1c}
	BB_13: BasicBlock(start=57,end=58) -> {BB_1e}
	BB_14: BasicBlock(start=29,end=30) -> {BB_20,BB_15}
	BB_15: BasicBlock(start=44,end=45) -> {BB_2,BB_12}
	BB_16: BasicBlock(start=59,end=64) -> {BB_22,BB_5}
	BB_17: BasicBlock(start=27,end=27) -> {BB_16,BB_4}
	BB_18: BasicBlock(start=12,end=14) -> {BB_c,BB_17}
	BB_19: BasicBlock(start=54,end=55) -> {BB_22,BB_e}
	BB_1: BasicBlock(start=5,end=6) -> {BB_17,BB_1a}
	BB_1a: BasicBlock(start=7,end=9) -> {BB_18,BB_d}
	BB_1b: BasicBlock(start=39,end=40) -> {BB_6,BB_16}
	BB_1c: BasicBlock(start=48,end=51) -> {BB_2,BB_13}
	BB_1d: BasicBlock(start=18,end=19) -> {BB_1e}
	BB_1e: ExitNode(normalReturn=true)
	BB_1f: BasicBlock(start=16,end=17) -> {BB_1d,BB_11}
	BB_20: BasicBlock(start=31,end=31) -> {BB_8,BB_1b}
	BB_21: BasicBlock(start=4,end=4) -> {BB_22,BB_1}
	BB_22: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=52,end=53) -> {BB_16,BB_19}
	BB_3: BasicBlock(start=1,end=1) -> {BB_21,BB_7}
	BB_4: BasicBlock(start=28,end=28) -> {BB_22,BB_14}
	BB_5: BasicBlock(start=65,end=65) -> {BB_1e}
	BB_6: BasicBlock(start=41,end=42) -> {BB_22,BB_a}
	BB_7: BasicBlock(start=2,end=3) -> {BB_1}
	BB_8: BasicBlock(start=32,end=34) -> {BB_22,BB_9}
	BB_9: BasicBlock(start=35,end=36) -> {BB_1b,BB_f}
	BB_a: BasicBlock(start=43,end=43) -> {BB_1e}
	BB_b: BasicBlock(start=23,end=24) -> {BB_10,BB_17}
	BB_c: BasicBlock(start=15,end=15) -> {BB_22,BB_1f}
	BB_d: BasicBlock(start=10,end=11) -> {BB_1e}
	BB_e: BasicBlock(start=56,end=56) -> {BB_1e}
	BB_f: BasicBlock(start=37,end=38) -> {BB_1e}
))

void <init>(boolean)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Dollar,multiline,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]),UVar(defSites={-2},value=int ∈ [0,1])),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={2,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.regex.Pattern$Dollar,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Dollar[↦-1;refId=102]))),
	1: ExprStmt(pc=5,VirtualFunctionCall(pc=5,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={0},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104]),(UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103])))),
	2: Assignment(pc=10,DVar(useSites={3},value=int ∈ [0,1],origin=2),GetField(pc=10,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	3: ReturnValue(pc=13,UVar(defSites={2},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

