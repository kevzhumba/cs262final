boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={1,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=1,0)),
	1: PutField(pc=2,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]),UVar(defSites={0},value=int = 0)),
	2: Assignment(pc=6,DVar(useSites={3},value=int = 0,origin=2),IntConst(pc=6,0)),
	3: PutField(pc=7,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={2},value=int = 0)),
	4: Assignment(pc=10,DVar(useSites={5},value=int = 0,origin=4),IntConst(pc=10,0)),
	5: ReturnValue(pc=11,UVar(defSites={4},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=5) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={18,10,54,14,1,5,21,45,35,51,27,7,39,23,47,31} (origin=-1),
	1: useSites={0,32,40,4,44,34,50,26,17,9,55,15} (origin=-2),
	2: useSites={32,40,53,29,3,55,15} (origin=-3),
	3: useSites={32,40,55,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value={int[], null}[↦2;refId=105],origin=0),GetField(pc=2,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$Loop,beginIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=an int,origin=2),ArrayLoad(pc=9,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦2;refId=105]))),
	3: If(pc=10,UVar(defSites={-3},value=an int),<=,UVar(defSites={2},value=an int),target=54),
	4: Assignment(pc=14,DVar(useSites={6},value={int[], null}[↦14;refId=109],origin=4),GetField(pc=14,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	5: Assignment(pc=18,DVar(useSites={6},value=an int,origin=5),GetField(pc=18,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	6: Assignment(pc=21,DVar(useSites={8,12,22,46,37,19},value=an int,origin=6),ArrayLoad(pc=21,UVar(defSites={5},value=an int),UVar(defSites={4},value={int[], null}[↦14;refId=109]))),
	7: Assignment(pc=27,DVar(useSites={8},value=an int,origin=7),GetField(pc=27,java.util.regex.Pattern$Loop,cmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	8: If(pc=30,UVar(defSites={6},value=an int),>=,UVar(defSites={7},value=an int),target=21),
	9: Assignment(pc=34,DVar(useSites={13},value={int[], null}[↦34;refId=121],origin=9),GetField(pc=34,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	10: Assignment(pc=38,DVar(useSites={13},value=an int,origin=10),GetField(pc=38,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	11: Assignment(pc=43,DVar(useSites={12},value=int = 1,origin=11),IntConst(pc=43,1)),
	12: Assignment(pc=44,DVar(useSites={13},value=int ∈ [-2147483647,2147483647],origin=12),BinaryExpr(pc=44,ComputationalTypeInt,UVar(defSites={6},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={11},value=int = 1))),
	13: ArrayStore(pc=45,UVar(defSites={9},value={int[], null}[↦34;refId=121]),UVar(defSites={10},value=an int),UVar(defSites={12},value=int ∈ [-2147483647,2147483647])),
	14: Assignment(pc=47,DVar(useSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦47;refId=124],origin=14),GetField(pc=47,java.util.regex.Pattern$Loop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	15: Assignment(pc=53,DVar(useSites={16,20},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=53,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦47;refId=124]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	16: If(pc=60,UVar(defSites={15},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=20),
	17: Assignment(pc=64,DVar(useSites={19},value={int[], null}[↦64;refId=127],origin=17),GetField(pc=64,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	18: Assignment(pc=68,DVar(useSites={19},value=an int,origin=18),GetField(pc=68,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	19: ArrayStore(pc=73,UVar(defSites={17},value={int[], null}[↦64;refId=127]),UVar(defSites={18},value=an int),UVar(defSites={6},value=int ∈ [-2147483648,2147483646])),
	20: ReturnValue(pc=76,UVar(defSites={15},value=int ∈ [0,1])),
	21: Assignment(pc=80,DVar(useSites={22},value=an int,origin=21),GetField(pc=80,java.util.regex.Pattern$Loop,cmax,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	22: If(pc=83,UVar(defSites={6},value=an int),>=,UVar(defSites={21},value=an int),target=54),
	23: Assignment(pc=87,DVar(useSites={25},value=an int,origin=23),GetField(pc=87,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	24: Assignment(pc=90,DVar(useSites={25},value=int = -1,origin=24),IntConst(pc=90,-1)),
	25: If(pc=91,UVar(defSites={23},value=an int),==,UVar(defSites={24},value=int = -1),target=34),
	26: Assignment(pc=95,DVar(useSites={28},value={_ <: java.util.regex.IntHashSet[], null}[↦95;refId=112],origin=26),GetField(pc=95,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	27: Assignment(pc=99,DVar(useSites={28},value=an int,origin=27),GetField(pc=99,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	28: Assignment(pc=102,DVar(useSites={29},value={_ <: java.util.regex.IntHashSet, null}[↦102;refId=115],origin=28),ArrayLoad(pc=102,UVar(defSites={27},value=an int),UVar(defSites={26},value={_ <: java.util.regex.IntHashSet[], null}[↦95;refId=112]))),
	29: Assignment(pc=104,DVar(useSites={30},value=int ∈ [0,1],origin=29),VirtualFunctionCall(pc=104,java.util.regex.IntHashSet,isInterface=false,boolean contains(int),UVar(defSites={28},value={_ <: java.util.regex.IntHashSet, null}[↦102;refId=115]),(UVar(defSites={-3},value=int ∈ [-2147483647,2147483647])))),
	30: If(pc=107,UVar(defSites={29},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=34),
	31: Assignment(pc=111,DVar(useSites={32},value={_ <: java.util.regex.Pattern$Node, null}[↦111;refId=118],origin=31),GetField(pc=111,java.util.regex.Pattern$Loop,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	32: Assignment(pc=117,DVar(useSites={33},value=int ∈ [0,1],origin=32),VirtualFunctionCall(pc=117,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={31},value={_ <: java.util.regex.Pattern$Node, null}[↦111;refId=118]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	33: ReturnValue(pc=120,UVar(defSites={32},value=int ∈ [0,1])),
	34: Assignment(pc=122,DVar(useSites={38},value={int[], null}[↦122;refId=133],origin=34),GetField(pc=122,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	35: Assignment(pc=126,DVar(useSites={38},value=an int,origin=35),GetField(pc=126,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	36: Assignment(pc=131,DVar(useSites={37},value=int = 1,origin=36),IntConst(pc=131,1)),
	37: Assignment(pc=132,DVar(useSites={38},value=int ∈ [-2147483647,2147483647],origin=37),BinaryExpr(pc=132,ComputationalTypeInt,UVar(defSites={6},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={36},value=int = 1))),
	38: ArrayStore(pc=133,UVar(defSites={34},value={int[], null}[↦122;refId=133]),UVar(defSites={35},value=an int),UVar(defSites={37},value=int ∈ [-2147483647,2147483647])),
	39: Assignment(pc=135,DVar(useSites={40},value={_ <: java.util.regex.Pattern$Node, null}[↦135;refId=136],origin=39),GetField(pc=135,java.util.regex.Pattern$Loop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	40: Assignment(pc=141,DVar(useSites={41},value=int ∈ [0,1],origin=40),VirtualFunctionCall(pc=141,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={39},value={_ <: java.util.regex.Pattern$Node, null}[↦135;refId=136]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	41: If(pc=148,UVar(defSites={40},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=44),
	42: Assignment(pc=151,DVar(useSites={43},value=int = 1,origin=42),IntConst(pc=151,1)),
	43: ReturnValue(pc=152,UVar(defSites={42},value=int = 1)),
	44: Assignment(pc=154,DVar(useSites={46},value={int[], null}[↦154;refId=139],origin=44),GetField(pc=154,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	45: Assignment(pc=158,DVar(useSites={46},value=an int,origin=45),GetField(pc=158,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	46: ArrayStore(pc=163,UVar(defSites={44},value={int[], null}[↦154;refId=139]),UVar(defSites={45},value=an int),UVar(defSites={6},value=int ∈ [-2147483648,2147483646])),
	47: Assignment(pc=165,DVar(useSites={49},value=an int,origin=47),GetField(pc=165,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	48: Assignment(pc=168,DVar(useSites={49},value=int = -1,origin=48),IntConst(pc=168,-1)),
	49: If(pc=169,UVar(defSites={47},value=an int),==,UVar(defSites={48},value=int = -1),target=54),
	50: Assignment(pc=173,DVar(useSites={52},value={_ <: java.util.regex.IntHashSet[], null}[↦173;refId=142],origin=50),GetField(pc=173,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	51: Assignment(pc=177,DVar(useSites={52},value=an int,origin=51),GetField(pc=177,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	52: Assignment(pc=180,DVar(useSites={53},value={_ <: java.util.regex.IntHashSet, null}[↦180;refId=145],origin=52),ArrayLoad(pc=180,UVar(defSites={51},value=an int),UVar(defSites={50},value={_ <: java.util.regex.IntHashSet[], null}[↦173;refId=142]))),
	53: VirtualMethodCall(pc=182,java.util.regex.IntHashSet,isInterface=false,void add(int),UVar(defSites={52},value={_ <: java.util.regex.IntHashSet, null}[↦180;refId=145]),(UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]))),
	54: Assignment(pc=186,DVar(useSites={55},value={_ <: java.util.regex.Pattern$Node, null}[↦186;refId=130],origin=54),GetField(pc=186,java.util.regex.Pattern$Loop,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	55: Assignment(pc=192,DVar(useSites={56},value=int ∈ [0,1],origin=55),VirtualFunctionCall(pc=192,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={54},value={_ <: java.util.regex.Pattern$Node, null}[↦186;refId=130]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	56: ReturnValue(pc=195,UVar(defSites={55},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1c,BB_4}
	BB_10: BasicBlock(start=9,end=13) -> {BB_1c,BB_3}
	BB_11: BasicBlock(start=53,end=53) -> {BB_1c,BB_7}
	BB_12: BasicBlock(start=34,end=38) -> {BB_1c,BB_15}
	BB_13: BasicBlock(start=17,end=19) -> {BB_1c,BB_c}
	BB_14: BasicBlock(start=7,end=8) -> {BB_10,BB_e}
	BB_15: BasicBlock(start=39,end=40) -> {BB_1c,BB_5}
	BB_16: BasicBlock(start=50,end=52) -> {BB_1c,BB_11}
	BB_17: BasicBlock(start=16,end=16) -> {BB_c,BB_13}
	BB_18: BasicBlock(start=31,end=32) -> {BB_1c,BB_f}
	BB_19: BasicBlock(start=26,end=28) -> {BB_1c,BB_d}
	BB_1: BasicBlock(start=56,end=56) -> {BB_9}
	BB_1a: BasicBlock(start=23,end=25) -> {BB_19,BB_12}
	BB_1b: BasicBlock(start=4,end=6) -> {BB_1c,BB_14}
	BB_1c: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=42,end=43) -> {BB_9}
	BB_3: BasicBlock(start=14,end=15) -> {BB_1c,BB_17}
	BB_4: BasicBlock(start=1,end=2) -> {BB_1c,BB_8}
	BB_5: BasicBlock(start=41,end=41) -> {BB_6,BB_2}
	BB_6: BasicBlock(start=44,end=46) -> {BB_1c,BB_b}
	BB_7: BasicBlock(start=54,end=55) -> {BB_1c,BB_1}
	BB_8: BasicBlock(start=3,end=3) -> {BB_7,BB_1b}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=30,end=30) -> {BB_18,BB_12}
	BB_b: BasicBlock(start=47,end=49) -> {BB_16,BB_7}
	BB_c: BasicBlock(start=20,end=20) -> {BB_9}
	BB_d: BasicBlock(start=29,end=29) -> {BB_1c,BB_a}
	BB_e: BasicBlock(start=21,end=22) -> {BB_1a,BB_7}
	BB_f: BasicBlock(start=33,end=33) -> {BB_9}
))

boolean matchInit(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={32,16,42,26,38,22,1,29,3,35,19,11,7} (origin=-1),
	1: useSites={0,36,28,18,10,6,33,41,39,23} (origin=-2),
	2: useSites={36,33,39,23} (origin=-3),
	3: useSites={36,33,39,23} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={43},value=an int,origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: Assignment(pc=15,DVar(useSites={5},value=an int,origin=3),GetField(pc=15,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	4: Assignment(pc=18,DVar(useSites={5},value=int = -1,origin=4),IntConst(pc=18,-1)),
	5: If(pc=19,UVar(defSites={3},value=an int),==,UVar(defSites={4},value=int = -1),target=15),
	6: Assignment(pc=23,DVar(useSites={8},value={_ <: java.util.regex.IntHashSet[], null}[↦23;refId=109],origin=6),GetField(pc=23,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	7: Assignment(pc=27,DVar(useSites={8},value=an int,origin=7),GetField(pc=27,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	8: Assignment(pc=30,DVar(useSites={9},value={_ <: java.util.regex.IntHashSet, null}[↦30;refId=112],origin=8),ArrayLoad(pc=30,UVar(defSites={7},value=an int),UVar(defSites={6},value={_ <: java.util.regex.IntHashSet[], null}[↦23;refId=109]))),
	9: If(pc=31,UVar(defSites={8},value={_ <: java.util.regex.IntHashSet, null}[↦30;refId=112]),!=,NullExpr(pc=-333),target=15),
	10: Assignment(pc=35,DVar(useSites={14},value={_ <: java.util.regex.IntHashSet[], null}[↦35;refId=113],origin=10),GetField(pc=35,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	11: Assignment(pc=39,DVar(useSites={14},value=an int,origin=11),GetField(pc=39,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	12: Assignment(pc=42,DVar(useSites={14,13},value=java.util.regex.IntHashSet[↦42;refId=114],origin=12),New(pc=42,java.util.regex.IntHashSet)),
	13: NonVirtualMethodCall(pc=46,java.util.regex.IntHashSet,isInterface=false,void <init>(),UVar(defSites={12},value=java.util.regex.IntHashSet[↦42;refId=114]),()),
	14: ArrayStore(pc=49,UVar(defSites={10},value={_ <: java.util.regex.IntHashSet[], null}[↦35;refId=113]),UVar(defSites={11},value=an int),UVar(defSites={12},value=java.util.regex.IntHashSet[↦42;refId=114])),
	15: Assignment(pc=50,DVar(useSites={17},value=int = 0,origin=15),IntConst(pc=50,0)),
	16: Assignment(pc=52,DVar(useSites={17},value=an int,origin=16),GetField(pc=52,java.util.regex.Pattern$Loop,cmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	17: If(pc=55,UVar(defSites={15},value=int = 0),>=,UVar(defSites={16},value=an int),target=25),
	18: Assignment(pc=59,DVar(useSites={21},value={int[], null}[↦59;refId=131],origin=18),GetField(pc=59,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	19: Assignment(pc=63,DVar(useSites={21},value=an int,origin=19),GetField(pc=63,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	20: Assignment(pc=66,DVar(useSites={21},value=int = 1,origin=20),IntConst(pc=66,1)),
	21: ArrayStore(pc=67,UVar(defSites={18},value={int[], null}[↦59;refId=131]),UVar(defSites={19},value=an int),UVar(defSites={20},value=int = 1)),
	22: Assignment(pc=69,DVar(useSites={23},value={_ <: java.util.regex.Pattern$Node, null}[↦69;refId=134],origin=22),GetField(pc=69,java.util.regex.Pattern$Loop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	23: Assignment(pc=75,DVar(useSites={44},value=int ∈ [0,1],origin=23),VirtualFunctionCall(pc=75,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={22},value={_ <: java.util.regex.Pattern$Node, null}[↦69;refId=134]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	24: Goto(pc=80,target=41),
	25: Assignment(pc=83,DVar(useSites={27},value=int = 0,origin=25),IntConst(pc=83,0)),
	26: Assignment(pc=85,DVar(useSites={27},value=an int,origin=26),GetField(pc=85,java.util.regex.Pattern$Loop,cmax,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	27: If(pc=88,UVar(defSites={25},value=int = 0),>=,UVar(defSites={26},value=an int),target=38),
	28: Assignment(pc=92,DVar(useSites={31},value={int[], null}[↦92;refId=122],origin=28),GetField(pc=92,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	29: Assignment(pc=96,DVar(useSites={31},value=an int,origin=29),GetField(pc=96,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	30: Assignment(pc=99,DVar(useSites={31},value=int = 1,origin=30),IntConst(pc=99,1)),
	31: ArrayStore(pc=100,UVar(defSites={28},value={int[], null}[↦92;refId=122]),UVar(defSites={29},value=an int),UVar(defSites={30},value=int = 1)),
	32: Assignment(pc=102,DVar(useSites={33},value={_ <: java.util.regex.Pattern$Node, null}[↦102;refId=125],origin=32),GetField(pc=102,java.util.regex.Pattern$Loop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	33: Assignment(pc=108,DVar(useSites={44,34},value=int ∈ [0,1],origin=33),VirtualFunctionCall(pc=108,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={32},value={_ <: java.util.regex.Pattern$Node, null}[↦102;refId=125]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	34: If(pc=115,UVar(defSites={33},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=41),
	35: Assignment(pc=119,DVar(useSites={36},value={_ <: java.util.regex.Pattern$Node, null}[↦119;refId=128],origin=35),GetField(pc=119,java.util.regex.Pattern$Loop,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	36: Assignment(pc=125,DVar(useSites={44},value=int ∈ [0,1],origin=36),VirtualFunctionCall(pc=125,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={35},value={_ <: java.util.regex.Pattern$Node, null}[↦119;refId=128]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	37: Goto(pc=130,target=41),
	38: Assignment(pc=134,DVar(useSites={39},value={_ <: java.util.regex.Pattern$Node, null}[↦134;refId=119],origin=38),GetField(pc=134,java.util.regex.Pattern$Loop,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	39: Assignment(pc=140,DVar(useSites={44},value=int ∈ [0,1],origin=39),VirtualFunctionCall(pc=140,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={38},value={_ <: java.util.regex.Pattern$Node, null}[↦134;refId=119]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	40: Nop(pc=143),
	41: Assignment(pc=146,DVar(useSites={43},value={int[], null}[↦146;refId=137],origin=41),GetField(pc=146,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	42: Assignment(pc=150,DVar(useSites={43},value=an int,origin=42),GetField(pc=150,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]))),
	43: ArrayStore(pc=155,UVar(defSites={41},value={int[], null}[↦146;refId=137]),UVar(defSites={42},value=an int),UVar(defSites={2},value=an int)),
	44: ReturnValue(pc=158,UVar(defSites={36,33,39,23},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_8,BB_3}
	BB_10: BasicBlock(start=34,end=34) -> {BB_14,BB_6}
	BB_11: BasicBlock(start=22,end=23) -> {BB_8,BB_a}
	BB_12: BasicBlock(start=44,end=44) -> {BB_16}
	BB_13: BasicBlock(start=3,end=5) -> {BB_9,BB_4}
	BB_14: BasicBlock(start=35,end=36) -> {BB_8,BB_b}
	BB_15: BasicBlock(start=18,end=21) -> {BB_8,BB_11}
	BB_16: ExitNode(normalReturn=true)
	BB_1: BasicBlock(start=10,end=13) -> {BB_8,BB_2}
	BB_2: BasicBlock(start=14,end=14) -> {BB_8,BB_9}
	BB_3: BasicBlock(start=1,end=2) -> {BB_8,BB_13}
	BB_4: BasicBlock(start=6,end=8) -> {BB_8,BB_5}
	BB_5: BasicBlock(start=9,end=9) -> {BB_1,BB_9}
	BB_6: BasicBlock(start=41,end=43) -> {BB_8,BB_12}
	BB_7: BasicBlock(start=40,end=40) -> {BB_6}
	BB_8: ExitNode(normalReturn=false)
	BB_9: BasicBlock(start=15,end=17) -> {BB_15,BB_c}
	BB_a: BasicBlock(start=24,end=24) -> {BB_6}
	BB_b: BasicBlock(start=37,end=37) -> {BB_6}
	BB_c: BasicBlock(start=25,end=27) -> {BB_e,BB_d}
	BB_d: BasicBlock(start=28,end=31) -> {BB_8,BB_f}
	BB_e: BasicBlock(start=38,end=39) -> {BB_8,BB_7}
	BB_f: BasicBlock(start=32,end=33) -> {BB_8,BB_10}
))

void <init>(int,int)
AITACode(params=(Parameters(
	0: useSites={0,4,2,1} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Loop,countIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]),UVar(defSites={-2},value=an int)),
	2: PutField(pc=11,java.util.regex.Pattern$Loop,beginIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]),UVar(defSites={-3},value=an int)),
	3: Assignment(pc=15,DVar(useSites={4},value=int = -1,origin=3),IntConst(pc=15,-1)),
	4: PutField(pc=16,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Loop[↦-1;refId=102]),UVar(defSites={3},value=int = -1)),
	5: Return(pc=19)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=5) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

