boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={8} (origin=-1),
	1: useSites={0,4,9,3,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=5,1)),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=6,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={1},value=int = 1))),
	3: PutField(pc=7,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={2},value=an int)),
	4: Assignment(pc=12,DVar(useSites={6},value=an int,origin=4),GetField(pc=12,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	5: Assignment(pc=15,DVar(useSites={6},value=int = 2,origin=5),IntConst(pc=15,2)),
	6: Assignment(pc=16,DVar(useSites={7},value=an int,origin=6),BinaryExpr(pc=16,ComputationalTypeInt,UVar(defSites={4},value=an int),+,UVar(defSites={5},value=int = 2))),
	7: PutField(pc=17,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={6},value=an int)),
	8: Assignment(pc=21,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦21;refId=105],origin=8),GetField(pc=21,java.util.regex.Pattern$LineEnding,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LineEnding[↦-1;refId=102]))),
	9: Assignment(pc=25,DVar(useSites={10},value=int ∈ [0,1],origin=9),VirtualFunctionCall(pc=25,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦21;refId=105]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	10: ReturnValue(pc=28,UVar(defSites={9},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=10,end=10) -> {BB_3}
	BB_2: BasicBlock(start=1,end=9) -> {BB_4,BB_1}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$LineEnding[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={28,37,15} (origin=-1),
	1: useSites={0,36,18,38,41,23,31} (origin=-2),
	2: useSites={2,22,1,17} (origin=-3),
	3: useSites={2,18,38,25,31} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=5,UVar(defSites={-3},value=an int),>=,UVar(defSites={0},value=an int),target=40),
	2: Assignment(pc=10,DVar(useSites={8,4,12,10,6,14,21},value=int ∈ [0,65535],origin=2),VirtualFunctionCall(pc=10,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	3: Assignment(pc=19,DVar(useSites={4},value=int = 10,origin=3),IntConst(pc=19,10)),
	4: If(pc=21,UVar(defSites={2},value=int ∈ [0,65535]),==,UVar(defSites={3},value=int = 10),target=15),
	5: Assignment(pc=26,DVar(useSites={6},value=int = 11,origin=5),IntConst(pc=26,11)),
	6: If(pc=28,UVar(defSites={2},value=int ∈ [0,65535]),==,UVar(defSites={5},value=int = 11),target=15),
	7: Assignment(pc=33,DVar(useSites={8},value=int = 12,origin=7),IntConst(pc=33,12)),
	8: If(pc=35,UVar(defSites={2},value=int ∈ [0,65535]),==,UVar(defSites={7},value=int = 12),target=15),
	9: Assignment(pc=40,DVar(useSites={10},value=int = 133,origin=9),IntConst(pc=40,133)),
	10: If(pc=43,UVar(defSites={2},value=int ∈ [0,65535]),==,UVar(defSites={9},value=int = 133),target=15),
	11: Assignment(pc=48,DVar(useSites={12},value=int = 8232,origin=11),IntConst(pc=48,8232)),
	12: If(pc=51,UVar(defSites={2},value=int ∈ [0,65535]),==,UVar(defSites={11},value=int = 8232),target=15),
	13: Assignment(pc=56,DVar(useSites={14},value=int = 8233,origin=13),IntConst(pc=56,8233)),
	14: If(pc=59,UVar(defSites={2},value=int ∈ [0,65535]),!=,UVar(defSites={13},value=int = 8233),target=20),
	15: Assignment(pc=63,DVar(useSites={18},value={_ <: java.util.regex.Pattern$Node, null}[↦63;refId=112],origin=15),GetField(pc=63,java.util.regex.Pattern$LineEnding,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LineEnding[↦-1;refId=102]))),
	16: Assignment(pc=68,DVar(useSites={17},value=int = 1,origin=16),IntConst(pc=68,1)),
	17: Assignment(pc=69,DVar(useSites={18},value=int ∈ [-2147483647,2147483647],origin=17),BinaryExpr(pc=69,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={16},value=int = 1))),
	18: Assignment(pc=71,DVar(useSites={19},value=int ∈ [0,1],origin=18),VirtualFunctionCall(pc=71,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦63;refId=112]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={17},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	19: ReturnValue(pc=74,UVar(defSites={18},value=int ∈ [0,1])),
	20: Assignment(pc=77,DVar(useSites={21},value=int = 13,origin=20),IntConst(pc=77,13)),
	21: If(pc=79,UVar(defSites={2},value=int ∈ [0,65535]),!=,UVar(defSites={20},value=int = 13),target=42),
	22: Assignment(pc=82,DVar(useSites={24,38,30,25},value=int ∈ [-2147483647,2147483647],origin=22),BinaryExpr(pc=82,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=82,1))),
	23: Assignment(pc=87,DVar(useSites={24},value=an int,origin=23),GetField(pc=87,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	24: If(pc=90,UVar(defSites={22},value=int ∈ [-2147483647,2147483647]),>=,UVar(defSites={23},value=an int),target=35),
	25: Assignment(pc=95,DVar(useSites={27},value=int ∈ [0,65535],origin=25),VirtualFunctionCall(pc=95,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),(UVar(defSites={22},value=int ∈ [-2147483647,2147483646])))),
	26: Assignment(pc=100,DVar(useSites={27},value=int = 10,origin=26),IntConst(pc=100,10)),
	27: If(pc=102,UVar(defSites={25},value=int ∈ [0,65535]),!=,UVar(defSites={26},value=int = 10),target=37),
	28: Assignment(pc=106,DVar(useSites={31},value={_ <: java.util.regex.Pattern$Node, null}[↦106;refId=109],origin=28),GetField(pc=106,java.util.regex.Pattern$LineEnding,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LineEnding[↦-1;refId=102]))),
	29: Assignment(pc=111,DVar(useSites={30},value=int = 1,origin=29),IntConst(pc=111,1)),
	30: Assignment(pc=112,DVar(useSites={31},value=int ∈ [-2147483646,2147483647],origin=30),BinaryExpr(pc=112,ComputationalTypeInt,UVar(defSites={22},value=int ∈ [-2147483647,2147483646]),+,UVar(defSites={29},value=int = 1))),
	31: Assignment(pc=114,DVar(useSites={32},value=int ∈ [0,1],origin=31),VirtualFunctionCall(pc=114,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦106;refId=109]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={30},value=int ∈ [-2147483646,2147483647]),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	32: If(pc=117,UVar(defSites={31},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=37),
	33: Assignment(pc=120,DVar(useSites={34},value=int = 1,origin=33),IntConst(pc=120,1)),
	34: ReturnValue(pc=121,UVar(defSites={33},value=int = 1)),
	35: Assignment(pc=123,DVar(useSites={36},value=int = 1,origin=35),IntConst(pc=123,1)),
	36: PutField(pc=124,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={35},value=int = 1)),
	37: Assignment(pc=128,DVar(useSites={38},value={_ <: java.util.regex.Pattern$Node, null}[↦128;refId=115],origin=37),GetField(pc=128,java.util.regex.Pattern$LineEnding,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LineEnding[↦-1;refId=102]))),
	38: Assignment(pc=134,DVar(useSites={39},value=int ∈ [0,1],origin=38),VirtualFunctionCall(pc=134,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={37},value={_ <: java.util.regex.Pattern$Node, null}[↦128;refId=115]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={22},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	39: ReturnValue(pc=137,UVar(defSites={38},value=int ∈ [0,1])),
	40: Assignment(pc=142,DVar(useSites={41},value=int = 1,origin=40),IntConst(pc=142,1)),
	41: PutField(pc=143,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={40},value=int = 1)),
	42: Assignment(pc=146,DVar(useSites={43},value=int = 0,origin=42),IntConst(pc=146,0)),
	43: ReturnValue(pc=147,UVar(defSites={42},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_3}
	BB_10: BasicBlock(start=25,end=25) -> {BB_c,BB_18}
	BB_11: BasicBlock(start=28,end=31) -> {BB_c,BB_7}
	BB_12: BasicBlock(start=33,end=34) -> {BB_9}
	BB_13: BasicBlock(start=7,end=8) -> {BB_4,BB_d}
	BB_14: BasicBlock(start=39,end=39) -> {BB_9}
	BB_15: BasicBlock(start=3,end=4) -> {BB_1,BB_d}
	BB_16: BasicBlock(start=35,end=36) -> {BB_f}
	BB_17: BasicBlock(start=40,end=41) -> {BB_e}
	BB_18: BasicBlock(start=26,end=27) -> {BB_11,BB_f}
	BB_1: BasicBlock(start=5,end=6) -> {BB_d,BB_13}
	BB_2: BasicBlock(start=20,end=21) -> {BB_e,BB_8}
	BB_3: BasicBlock(start=1,end=1) -> {BB_6,BB_17}
	BB_4: BasicBlock(start=9,end=10) -> {BB_a,BB_d}
	BB_5: BasicBlock(start=13,end=14) -> {BB_d,BB_2}
	BB_6: BasicBlock(start=2,end=2) -> {BB_c,BB_15}
	BB_7: BasicBlock(start=32,end=32) -> {BB_12,BB_f}
	BB_8: BasicBlock(start=22,end=24) -> {BB_16,BB_10}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=11,end=12) -> {BB_5,BB_d}
	BB_b: BasicBlock(start=19,end=19) -> {BB_9}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=18) -> {BB_c,BB_b}
	BB_e: BasicBlock(start=42,end=43) -> {BB_9}
	BB_f: BasicBlock(start=37,end=38) -> {BB_c,BB_14}
))

