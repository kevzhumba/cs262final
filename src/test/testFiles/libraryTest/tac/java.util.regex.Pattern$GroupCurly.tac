boolean match2(java.util.regex.Matcher,int,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,8,2,5,21,11} (origin=-1),
	1: useSites={16,18,10,22,14,3,7} (origin=-2),
	2: useSites={22,17,9,3} (origin=-3),
	3: useSites={1,19} (origin=-4),
	4: useSites={22,3} (origin=-5)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$GroupCurly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	1: If(pc=5,UVar(defSites={-4,19},value=an int),>=,UVar(defSites={0},value=an int),target=21),
	2: Assignment(pc=9,DVar(useSites={3},value={_ <: java.util.regex.Pattern$Node, null}[↦9;refId=105],origin=2),GetField(pc=9,java.util.regex.Pattern$GroupCurly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	3: Assignment(pc=16,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=16,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={2},value={_ <: java.util.regex.Pattern$Node, null}[↦9;refId=105]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={18,-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	4: If(pc=19,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=21),
	5: Assignment(pc=26,DVar(useSites={6},value=int ∈ [0,1],origin=5),GetField(pc=26,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	6: If(pc=29,UVar(defSites={5},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=16),
	7: Assignment(pc=33,DVar(useSites={9},value={int[], null}[↦33;refId=108],origin=7),GetField(pc=33,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	8: Assignment(pc=37,DVar(useSites={9},value=an int,origin=8),GetField(pc=37,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	9: ArrayStore(pc=41,UVar(defSites={7},value={int[], null}[↦33;refId=108]),UVar(defSites={8},value=an int),UVar(defSites={18,-3},value=an int)),
	10: Assignment(pc=43,DVar(useSites={15},value={int[], null}[↦43;refId=112],origin=10),GetField(pc=43,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	11: Assignment(pc=47,DVar(useSites={13},value=an int,origin=11),GetField(pc=47,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	12: Assignment(pc=50,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=50,1)),
	13: Assignment(pc=51,DVar(useSites={15},value=an int,origin=13),BinaryExpr(pc=51,ComputationalTypeInt,UVar(defSites={11},value=an int),+,UVar(defSites={12},value=int = 1))),
	14: Assignment(pc=53,DVar(useSites={15},value=an int,origin=14),GetField(pc=53,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	15: ArrayStore(pc=56,UVar(defSites={10},value={int[], null}[↦43;refId=112]),UVar(defSites={13},value=an int),UVar(defSites={14},value=an int)),
	16: Assignment(pc=59,DVar(useSites={17},value=an int,origin=16),GetField(pc=59,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	17: If(pc=62,UVar(defSites={18,-3},value=an int),==,UVar(defSites={16},value=an int),target=21),
	18: Assignment(pc=69,DVar(useSites={22,17,9,3},value=an int,origin=18),GetField(pc=69,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	19: Assignment(pc=73,DVar(useSites={20,1},value=int ∈ [-2147483647,2147483647],origin=19),BinaryExpr(pc=73,ComputationalTypeInt,UVar(defSites={-4,19},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=73,1))),
	20: Goto(pc=76,target=0),
	21: Assignment(pc=80,DVar(useSites={22},value={_ <: java.util.regex.Pattern$Node, null}[↦80;refId=115],origin=21),GetField(pc=80,java.util.regex.Pattern$GroupCurly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	22: Assignment(pc=87,DVar(useSites={23},value=int ∈ [0,1],origin=22),VirtualFunctionCall(pc=87,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦80;refId=115]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={18,-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	23: ReturnValue(pc=90,UVar(defSites={22},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_3}
	BB_1: BasicBlock(start=5,end=6) -> {BB_6,BB_7}
	BB_2: BasicBlock(start=10,end=15) -> {BB_d,BB_7}
	BB_3: BasicBlock(start=21,end=22) -> {BB_d,BB_8}
	BB_4: BasicBlock(start=2,end=3) -> {BB_d,BB_c}
	BB_5: BasicBlock(start=17,end=17) -> {BB_a,BB_3}
	BB_6: BasicBlock(start=7,end=7) -> {BB_d,BB_9}
	BB_7: BasicBlock(start=16,end=16) -> {BB_d,BB_5}
	BB_8: BasicBlock(start=23,end=23) -> {BB_b}
	BB_9: BasicBlock(start=8,end=9) -> {BB_d,BB_2}
	BB_a: BasicBlock(start=18,end=20) -> {BB_0}
	BB_b: ExitNode(normalReturn=true)
	BB_c: BasicBlock(start=4,end=4) -> {BB_1,BB_3}
	BB_d: ExitNode(normalReturn=false)
))

void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype,int,int,boolean)
AITACode(params=(Parameters(
	0: useSites={0,4,2,6,1,5,3,7} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={3} (origin=-3),
	3: useSites={4} (origin=-4),
	4: useSites={2} (origin=-5),
	5: useSites={5} (origin=-6),
	6: useSites={6} (origin=-7),
	7: useSites={7} (origin=-8)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$GroupCurly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: PutField(pc=12,java.util.regex.Pattern$GroupCurly,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),UVar(defSites={-5},value={java.util.regex.Pattern$Qtype, null}[↦-5;refId=104])),
	3: PutField(pc=17,java.util.regex.Pattern$GroupCurly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),UVar(defSites={-3},value=an int)),
	4: PutField(pc=22,java.util.regex.Pattern$GroupCurly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),UVar(defSites={-4},value=an int)),
	5: PutField(pc=28,java.util.regex.Pattern$GroupCurly,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),UVar(defSites={-6},value=an int)),
	6: PutField(pc=34,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),UVar(defSites={-7},value=an int)),
	7: PutField(pc=40,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),UVar(defSites={-8},value=int ∈ [0,1])),
	8: Return(pc=43)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=8) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={8,20,44,2,50,10,6,22,54,41,25,57,53,45,29,61,51,27,59,15,47,63} (origin=-1),
	1: useSites={0,32,34,54,1,45,51,23} (origin=-2),
	2: useSites={28,54,45,51,23} (origin=-3),
	3: useSites={54,45,51,23} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={28,66,62,33,9,13},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=7,DVar(useSites={58,17,3},value={int[], null}[↦7;refId=107],origin=1),GetField(pc=7,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	2: Assignment(pc=15,DVar(useSites={3},value=an int,origin=2),GetField(pc=15,java.util.regex.Pattern$GroupCurly,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	3: Assignment(pc=18,DVar(useSites={58},value=an int,origin=3),ArrayLoad(pc=18,UVar(defSites={2},value=an int),UVar(defSites={1},value={int[], null}[↦7;refId=107]))),
	4: Assignment(pc=21,DVar(useSites={62},value=int = 0,origin=4),IntConst(pc=21,0)),
	5: Assignment(pc=24,DVar(useSites={66},value=int = 0,origin=5),IntConst(pc=24,0)),
	6: Assignment(pc=28,DVar(useSites={7},value=int ∈ [0,1],origin=6),GetField(pc=28,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	7: If(pc=31,UVar(defSites={6},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=15),
	8: Assignment(pc=37,DVar(useSites={9},value=an int,origin=8),GetField(pc=37,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	9: Assignment(pc=40,DVar(useSites={62},value=an int,origin=9),ArrayLoad(pc=40,UVar(defSites={8},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	10: Assignment(pc=46,DVar(useSites={12},value=an int,origin=10),GetField(pc=46,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	11: Assignment(pc=49,DVar(useSites={12},value=int = 1,origin=11),IntConst(pc=49,1)),
	12: Assignment(pc=50,DVar(useSites={13},value=an int,origin=12),BinaryExpr(pc=50,ComputationalTypeInt,UVar(defSites={10},value=an int),+,UVar(defSites={11},value=int = 1))),
	13: Assignment(pc=51,DVar(useSites={66},value=an int,origin=13),ArrayLoad(pc=51,UVar(defSites={12},value=an int),UVar(defSites={0},value=int[][↦1;refId=105]))),
	14: Nop(pc=52),
	15: Assignment(pc=57,DVar(useSites={17},value=an int,origin=15),GetField(pc=57,java.util.regex.Pattern$GroupCurly,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	16: Assignment(pc=60,DVar(useSites={17},value=int = -1,origin=16),IntConst(pc=60,-1)),
	17: ArrayStore(pc=61,UVar(defSites={1},value=int[][↦7;refId=107]),UVar(defSites={15},value=an int),UVar(defSites={16},value=int = -1)),
	18: Assignment(pc=62,DVar(useSites={40,56,67},value=int = 1,origin=18),IntConst(pc=62,1)),
	19: Assignment(pc=65,DVar(useSites={38,21},value=int = 0,origin=19),IntConst(pc=65,0)),
	20: Assignment(pc=71,DVar(useSites={21},value=an int,origin=20),GetField(pc=71,java.util.regex.Pattern$GroupCurly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	21: If(pc=74,UVar(defSites={38,19},value=an int),>=,UVar(defSites={20},value=an int),target=40),
	22: Assignment(pc=78,DVar(useSites={23},value={_ <: java.util.regex.Pattern$Node, null}[↦78;refId=251],origin=22),GetField(pc=78,java.util.regex.Pattern$GroupCurly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	23: Assignment(pc=84,DVar(useSites={24},value=int ∈ [0,1],origin=23),VirtualFunctionCall(pc=84,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={22},value={_ <: java.util.regex.Pattern$Node, null}[↦78;refId=251]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={34,-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	24: If(pc=87,UVar(defSites={23},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=36),
	25: Assignment(pc=91,DVar(useSites={26},value=int ∈ [0,1],origin=25),GetField(pc=91,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	26: If(pc=94,UVar(defSites={25},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=34),
	27: Assignment(pc=100,DVar(useSites={28},value=an int,origin=27),GetField(pc=100,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	28: ArrayStore(pc=104,UVar(defSites={0},value={int[], null}[↦1;refId=105]),UVar(defSites={27},value=an int),UVar(defSites={34,-3},value=an int)),
	29: Assignment(pc=108,DVar(useSites={31},value=an int,origin=29),GetField(pc=108,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	30: Assignment(pc=111,DVar(useSites={31},value=int = 1,origin=30),IntConst(pc=111,1)),
	31: Assignment(pc=112,DVar(useSites={33},value=an int,origin=31),BinaryExpr(pc=112,ComputationalTypeInt,UVar(defSites={29},value=an int),+,UVar(defSites={30},value=int = 1))),
	32: Assignment(pc=114,DVar(useSites={33},value=an int,origin=32),GetField(pc=114,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	33: ArrayStore(pc=117,UVar(defSites={0},value=int[][↦1;refId=105]),UVar(defSites={31},value=an int),UVar(defSites={32},value=an int)),
	34: Assignment(pc=119,DVar(useSites={28,54,45,51,23},value=an int,origin=34),GetField(pc=119,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	35: Goto(pc=123,target=38),
	36: Assignment(pc=126,DVar(useSites={40,56,67},value=int = 0,origin=36),IntConst(pc=126,0)),
	37: Goto(pc=129,target=40),
	38: Assignment(pc=132,DVar(useSites={21,39},value=an int,origin=38),BinaryExpr(pc=132,ComputationalTypeInt,UVar(defSites={38,19},value=an int),+,IntConst(pc=132,1))),
	39: Goto(pc=135,target=20),
	40: If(pc=140,UVar(defSites={36,18},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=56),
	41: Assignment(pc=144,DVar(useSites={43},value={java.util.regex.Pattern$Qtype, null}[↦144;refId=120],origin=41),GetField(pc=144,java.util.regex.Pattern$GroupCurly,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	42: Assignment(pc=147,DVar(useSites={43},value={java.util.regex.Pattern$Qtype, null}[↦147;refId=121],origin=42),GetStatic(pc=147,java.util.regex.Pattern$Qtype,GREEDY,java.util.regex.Pattern$Qtype)),
	43: If(pc=150,UVar(defSites={41},value={java.util.regex.Pattern$Qtype, null}[↦144;refId=120]),!=,UVar(defSites={42},value={java.util.regex.Pattern$Qtype, null}[↦147;refId=121]),target=47),
	44: Assignment(pc=157,DVar(useSites={45},value=an int,origin=44),GetField(pc=157,java.util.regex.Pattern$GroupCurly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	45: Assignment(pc=161,DVar(useSites={56,67},value=int ∈ [0,1],origin=45),VirtualFunctionCall(pc=161,java.util.regex.Pattern$GroupCurly,isInterface=false,boolean match0(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={34,-3},value=an int),UVar(defSites={44},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	46: Goto(pc=166,target=56),
	47: Assignment(pc=170,DVar(useSites={49},value={java.util.regex.Pattern$Qtype, null}[↦170;refId=122],origin=47),GetField(pc=170,java.util.regex.Pattern$GroupCurly,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	48: Assignment(pc=173,DVar(useSites={49},value={java.util.regex.Pattern$Qtype, null}[↦173;refId=123],origin=48),GetStatic(pc=173,java.util.regex.Pattern$Qtype,LAZY,java.util.regex.Pattern$Qtype)),
	49: If(pc=176,UVar(defSites={47},value={java.util.regex.Pattern$Qtype, null}[↦170;refId=122]),!=,UVar(defSites={48},value={java.util.regex.Pattern$Qtype, null}[↦173;refId=123]),target=53),
	50: Assignment(pc=183,DVar(useSites={51},value=an int,origin=50),GetField(pc=183,java.util.regex.Pattern$GroupCurly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	51: Assignment(pc=187,DVar(useSites={56,67},value=int ∈ [0,1],origin=51),VirtualFunctionCall(pc=187,java.util.regex.Pattern$GroupCurly,isInterface=false,boolean match1(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={34,-3},value=an int),UVar(defSites={50},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	52: Goto(pc=192,target=56),
	53: Assignment(pc=199,DVar(useSites={54},value=an int,origin=53),GetField(pc=199,java.util.regex.Pattern$GroupCurly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	54: Assignment(pc=203,DVar(useSites={56,67},value=int ∈ [0,1],origin=54),VirtualFunctionCall(pc=203,java.util.regex.Pattern$GroupCurly,isInterface=false,boolean match2(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={34,-3},value=an int),UVar(defSites={53},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	55: Nop(pc=206),
	56: If(pc=210,UVar(defSites={36,18,54,45,51},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=67),
	57: Assignment(pc=216,DVar(useSites={58},value=an int,origin=57),GetField(pc=216,java.util.regex.Pattern$GroupCurly,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	58: ArrayStore(pc=221,UVar(defSites={1},value=int[][↦7;refId=107]),UVar(defSites={57},value=an int),UVar(defSites={3},value=an int)),
	59: Assignment(pc=223,DVar(useSites={60},value=int ∈ [0,1],origin=59),GetField(pc=223,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	60: If(pc=226,UVar(defSites={59},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=67),
	61: Assignment(pc=232,DVar(useSites={62},value=an int,origin=61),GetField(pc=232,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	62: ArrayStore(pc=237,UVar(defSites={0},value={int[], null}[↦1;refId=105]),UVar(defSites={61},value=an int),UVar(defSites={4,9},value=an int)),
	63: Assignment(pc=241,DVar(useSites={65},value=an int,origin=63),GetField(pc=241,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	64: Assignment(pc=244,DVar(useSites={65},value=int = 1,origin=64),IntConst(pc=244,1)),
	65: Assignment(pc=245,DVar(useSites={66},value=an int,origin=65),BinaryExpr(pc=245,ComputationalTypeInt,UVar(defSites={63},value=an int),+,UVar(defSites={64},value=int = 1))),
	66: ArrayStore(pc=248,UVar(defSites={0},value=int[][↦1;refId=105]),UVar(defSites={65},value=an int),UVar(defSites={5,13},value=an int)),
	67: ReturnValue(pc=251,UVar(defSites={36,18,54,45,51},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1f,BB_12}
	BB_10: BasicBlock(start=29,end=33) -> {BB_1f,BB_4}
	BB_11: BasicBlock(start=61,end=62) -> {BB_1f,BB_17}
	BB_12: BasicBlock(start=1,end=3) -> {BB_1f,BB_1e}
	BB_13: BasicBlock(start=22,end=23) -> {BB_1f,BB_9}
	BB_14: BasicBlock(start=44,end=45) -> {BB_1f,BB_e}
	BB_15: BasicBlock(start=59,end=60) -> {BB_1b,BB_11}
	BB_16: BasicBlock(start=27,end=28) -> {BB_1f,BB_10}
	BB_17: BasicBlock(start=63,end=66) -> {BB_1f,BB_1b}
	BB_18: BasicBlock(start=18,end=19) -> {BB_d}
	BB_19: ExitNode(normalReturn=true)
	BB_1: BasicBlock(start=38,end=39) -> {BB_d}
	BB_1a: BasicBlock(start=50,end=51) -> {BB_1f,BB_b}
	BB_1b: BasicBlock(start=67,end=67) -> {BB_19}
	BB_1c: BasicBlock(start=40,end=40) -> {BB_8,BB_3}
	BB_1d: BasicBlock(start=55,end=55) -> {BB_8}
	BB_1e: BasicBlock(start=4,end=7) -> {BB_5,BB_21}
	BB_1f: ExitNode(normalReturn=false)
	BB_20: BasicBlock(start=47,end=49) -> {BB_2,BB_1a}
	BB_21: BasicBlock(start=15,end=17) -> {BB_1f,BB_18}
	BB_2: BasicBlock(start=53,end=54) -> {BB_1f,BB_1d}
	BB_3: BasicBlock(start=41,end=43) -> {BB_20,BB_14}
	BB_4: BasicBlock(start=34,end=35) -> {BB_1}
	BB_5: BasicBlock(start=8,end=9) -> {BB_1f,BB_7}
	BB_6: BasicBlock(start=36,end=37) -> {BB_1c}
	BB_7: BasicBlock(start=10,end=13) -> {BB_1f,BB_c}
	BB_8: BasicBlock(start=56,end=56) -> {BB_1b,BB_f}
	BB_9: BasicBlock(start=24,end=24) -> {BB_a,BB_6}
	BB_a: BasicBlock(start=25,end=26) -> {BB_4,BB_16}
	BB_b: BasicBlock(start=52,end=52) -> {BB_8}
	BB_c: BasicBlock(start=14,end=14) -> {BB_21}
	BB_d: BasicBlock(start=20,end=21) -> {BB_1c,BB_13}
	BB_e: BasicBlock(start=46,end=46) -> {BB_8}
	BB_f: BasicBlock(start=57,end=58) -> {BB_1f,BB_15}
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={8,18,30,5,37,31} (origin=-1),
	1: useSites={0,24,4,36,28,2,6,38,14,1,33,17,21,13,3,27,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={10,11},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={20,22},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	2: Assignment(pc=11,DVar(useSites={15},value=int ∈ [0,1],origin=2),GetField(pc=11,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	3: Assignment(pc=17,DVar(useSites={33},value=int ∈ [0,1],origin=3),GetField(pc=17,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	4: VirtualMethodCall(pc=23,java.util.regex.Pattern$TreeInfo,isInterface=false,void reset(),UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),()),
	5: Assignment(pc=27,DVar(useSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=106],origin=5),GetField(pc=27,java.util.regex.Pattern$GroupCurly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	6: ExprStmt(pc=31,VirtualFunctionCall(pc=31,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=106]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	7: Assignment(pc=36,DVar(useSites={9},value=an int,origin=7),GetField(pc=36,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	8: Assignment(pc=40,DVar(useSites={9},value=an int,origin=8),GetField(pc=40,java.util.regex.Pattern$GroupCurly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	9: Assignment(pc=43,DVar(useSites={10},value=an int,origin=9),BinaryExpr(pc=43,ComputationalTypeInt,UVar(defSites={7},value=an int),*,UVar(defSites={8},value=an int))),
	10: Assignment(pc=45,DVar(useSites={13,11},value=an int,origin=10),BinaryExpr(pc=45,ComputationalTypeInt,UVar(defSites={9},value=an int),+,UVar(defSites={0},value=an int))),
	11: If(pc=51,UVar(defSites={10},value=an int),>=,UVar(defSites={0},value=an int),target=13),
	12: Assignment(pc=54,DVar(useSites={13},value=int = 268435455,origin=12),IntConst(pc=54,268435455)),
	13: PutField(pc=61,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={12,10},value=an int)),
	14: Assignment(pc=67,DVar(useSites={15},value=int ∈ [0,1],origin=14),GetField(pc=67,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	15: Assignment(pc=70,DVar(useSites={16},value=int ∈ [0,1],origin=15),BinaryExpr(pc=70,ComputationalTypeInt,UVar(defSites={2},value=int ∈ [0,1]),&,UVar(defSites={14},value=int ∈ [0,1]))),
	16: If(pc=71,UVar(defSites={15},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=26),
	17: Assignment(pc=75,DVar(useSites={19},value=an int,origin=17),GetField(pc=75,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	18: Assignment(pc=79,DVar(useSites={19},value=an int,origin=18),GetField(pc=79,java.util.regex.Pattern$GroupCurly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	19: Assignment(pc=82,DVar(useSites={20},value=an int,origin=19),BinaryExpr(pc=82,ComputationalTypeInt,UVar(defSites={17},value=an int),*,UVar(defSites={18},value=an int))),
	20: Assignment(pc=84,DVar(useSites={22,21},value=an int,origin=20),BinaryExpr(pc=84,ComputationalTypeInt,UVar(defSites={19},value=an int),+,UVar(defSites={1},value=an int))),
	21: PutField(pc=90,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={20},value=an int)),
	22: If(pc=96,UVar(defSites={20},value=an int),>=,UVar(defSites={1},value=an int),target=28),
	23: Assignment(pc=100,DVar(useSites={24},value=int = 0,origin=23),IntConst(pc=100,0)),
	24: PutField(pc=101,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={23},value=int = 0)),
	25: Goto(pc=104,target=28),
	26: Assignment(pc=108,DVar(useSites={27},value=int = 0,origin=26),IntConst(pc=108,0)),
	27: PutField(pc=109,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={26},value=int = 0)),
	28: Assignment(pc=113,DVar(useSites={29},value=int ∈ [0,1],origin=28),GetField(pc=113,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	29: If(pc=116,UVar(defSites={28},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=35),
	30: Assignment(pc=120,DVar(useSites={32},value=an int,origin=30),GetField(pc=120,java.util.regex.Pattern$GroupCurly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	31: Assignment(pc=124,DVar(useSites={32},value=an int,origin=31),GetField(pc=124,java.util.regex.Pattern$GroupCurly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	32: If(pc=127,UVar(defSites={30},value=an int),!=,UVar(defSites={31},value=an int),target=35),
	33: PutField(pc=133,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={3},value=int ∈ [0,1])),
	34: Goto(pc=136,target=37),
	35: Assignment(pc=140,DVar(useSites={36},value=int = 0,origin=35),IntConst(pc=140,0)),
	36: PutField(pc=141,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={35},value=int = 0)),
	37: Assignment(pc=145,DVar(useSites={38},value={_ <: java.util.regex.Pattern$Node, null}[↦145;refId=109],origin=37),GetField(pc=145,java.util.regex.Pattern$GroupCurly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	38: Assignment(pc=149,DVar(useSites={39},value=int ∈ [0,1],origin=38),VirtualFunctionCall(pc=149,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={37},value={_ <: java.util.regex.Pattern$Node, null}[↦145;refId=109]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	39: ReturnValue(pc=152,UVar(defSites={38},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_a,BB_3}
	BB_10: BasicBlock(start=23,end=25) -> {BB_b}
	BB_1: BasicBlock(start=5,end=6) -> {BB_a,BB_d}
	BB_2: BasicBlock(start=37,end=38) -> {BB_a,BB_e}
	BB_3: BasicBlock(start=1,end=4) -> {BB_a,BB_1}
	BB_4: BasicBlock(start=13,end=16) -> {BB_5,BB_f}
	BB_5: BasicBlock(start=17,end=22) -> {BB_b,BB_10}
	BB_6: BasicBlock(start=12,end=12) -> {BB_4}
	BB_7: BasicBlock(start=35,end=36) -> {BB_2}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=30,end=32) -> {BB_c,BB_7}
	BB_a: ExitNode(normalReturn=false)
	BB_b: BasicBlock(start=28,end=29) -> {BB_7,BB_9}
	BB_c: BasicBlock(start=33,end=34) -> {BB_2}
	BB_d: BasicBlock(start=7,end=11) -> {BB_4,BB_6}
	BB_e: BasicBlock(start=39,end=39) -> {BB_8}
	BB_f: BasicBlock(start=26,end=27) -> {BB_b}
))

boolean match1(java.util.regex.Matcher,int,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,24,18,9,5,21} (origin=-1),
	1: useSites={20,10,14,1,29,27,23} (origin=-2),
	2: useSites={10,22,1,15} (origin=-3),
	3: useSites={6,30} (origin=-4),
	4: useSites={10,1} (origin=-5)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$GroupCurly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	1: Assignment(pc=8,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=8,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={0},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=105]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={29,-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	2: If(pc=11,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=5),
	3: Assignment(pc=14,DVar(useSites={4},value=int = 1,origin=3),IntConst(pc=14,1)),
	4: ReturnValue(pc=15,UVar(defSites={3},value=int = 1)),
	5: Assignment(pc=18,DVar(useSites={6},value=an int,origin=5),GetField(pc=18,java.util.regex.Pattern$GroupCurly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	6: If(pc=21,UVar(defSites={-4,30},value=an int),<,UVar(defSites={5},value=an int),target=9),
	7: Assignment(pc=24,DVar(useSites={8},value=int = 0,origin=7),IntConst(pc=24,0)),
	8: ReturnValue(pc=25,UVar(defSites={7},value=int = 0)),
	9: Assignment(pc=27,DVar(useSites={10},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=108],origin=9),GetField(pc=27,java.util.regex.Pattern$GroupCurly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	10: Assignment(pc=34,DVar(useSites={11},value=int ∈ [0,1],origin=10),VirtualFunctionCall(pc=34,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=108]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={29,-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	11: If(pc=37,UVar(defSites={10},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=14),
	12: Assignment(pc=40,DVar(useSites={13},value=int = 0,origin=12),IntConst(pc=40,0)),
	13: ReturnValue(pc=41,UVar(defSites={12},value=int = 0)),
	14: Assignment(pc=44,DVar(useSites={15},value=an int,origin=14),GetField(pc=44,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	15: If(pc=47,UVar(defSites={29,-3},value=an int),!=,UVar(defSites={14},value=an int),target=18),
	16: Assignment(pc=50,DVar(useSites={17},value=int = 0,origin=16),IntConst(pc=50,0)),
	17: ReturnValue(pc=51,UVar(defSites={16},value=int = 0)),
	18: Assignment(pc=53,DVar(useSites={19},value=int ∈ [0,1],origin=18),GetField(pc=53,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	19: If(pc=56,UVar(defSites={18},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=29),
	20: Assignment(pc=60,DVar(useSites={22},value={int[], null}[↦60;refId=112],origin=20),GetField(pc=60,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	21: Assignment(pc=64,DVar(useSites={22},value=an int,origin=21),GetField(pc=64,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	22: ArrayStore(pc=68,UVar(defSites={20},value={int[], null}[↦60;refId=112]),UVar(defSites={21},value=an int),UVar(defSites={29,-3},value=an int)),
	23: Assignment(pc=70,DVar(useSites={28},value={int[], null}[↦70;refId=115],origin=23),GetField(pc=70,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	24: Assignment(pc=74,DVar(useSites={26},value=an int,origin=24),GetField(pc=74,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	25: Assignment(pc=77,DVar(useSites={26},value=int = 1,origin=25),IntConst(pc=77,1)),
	26: Assignment(pc=78,DVar(useSites={28},value=an int,origin=26),BinaryExpr(pc=78,ComputationalTypeInt,UVar(defSites={24},value=an int),+,UVar(defSites={25},value=int = 1))),
	27: Assignment(pc=80,DVar(useSites={28},value=an int,origin=27),GetField(pc=80,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	28: ArrayStore(pc=83,UVar(defSites={23},value={int[], null}[↦70;refId=115]),UVar(defSites={26},value=an int),UVar(defSites={27},value=an int)),
	29: Assignment(pc=85,DVar(useSites={10,22,1,15},value=an int,origin=29),GetField(pc=85,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	30: Assignment(pc=89,DVar(useSites={6,31},value=int ∈ [-2147483647,2147483647],origin=30),BinaryExpr(pc=89,ComputationalTypeInt,UVar(defSites={-4,30},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=89,1))),
	31: Goto(pc=92,target=0)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_b,BB_4}
	BB_10: ExitNode(normalReturn=true)
	BB_1: BasicBlock(start=5,end=6) -> {BB_6,BB_3}
	BB_2: BasicBlock(start=14,end=14) -> {BB_b,BB_c}
	BB_3: BasicBlock(start=9,end=10) -> {BB_b,BB_9}
	BB_4: BasicBlock(start=2,end=2) -> {BB_1,BB_7}
	BB_5: BasicBlock(start=12,end=13) -> {BB_10}
	BB_6: BasicBlock(start=7,end=8) -> {BB_10}
	BB_7: BasicBlock(start=3,end=4) -> {BB_10}
	BB_8: BasicBlock(start=16,end=17) -> {BB_10}
	BB_9: BasicBlock(start=11,end=11) -> {BB_5,BB_2}
	BB_a: BasicBlock(start=23,end=28) -> {BB_b,BB_e}
	BB_b: ExitNode(normalReturn=false)
	BB_c: BasicBlock(start=15,end=15) -> {BB_f,BB_8}
	BB_d: BasicBlock(start=20,end=22) -> {BB_b,BB_a}
	BB_e: BasicBlock(start=29,end=31) -> {BB_0}
	BB_f: BasicBlock(start=18,end=19) -> {BB_e,BB_d}
))

boolean match0(java.util.regex.Matcher,int,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={64,72,24,20,12,76,44,60,50,42,58,70,22,14,33,81,89,5,85,3,35,83,7,55,31} (origin=-1),
	1: useSites={0,48,56,50,90,17,45,15} (origin=-2),
	2: useSites={40,34,18,90,38,29,27,23,15} (origin=-3),
	3: useSites={54,41,13} (origin=-4),
	4: useSites={56,50,90,45,15} (origin=-5)
)),stmts=(
	0: Assignment(pc=4,DVar(useSites={88,84,28,66,34,10,6,78,75,39,23,63},value={int[], null}[↦4;refId=105],origin=0),GetField(pc=4,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=9,DVar(useSites={84},value=int = 0,origin=1),IntConst(pc=9,0)),
	2: Assignment(pc=12,DVar(useSites={88},value=int = 0,origin=2),IntConst(pc=12,0)),
	3: Assignment(pc=16,DVar(useSites={4},value=int ∈ [0,1],origin=3),GetField(pc=16,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	4: If(pc=19,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	5: Assignment(pc=25,DVar(useSites={6},value=an int,origin=5),GetField(pc=25,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	6: Assignment(pc=28,DVar(useSites={84},value=an int,origin=6),ArrayLoad(pc=28,UVar(defSites={5},value=an int),UVar(defSites={0},value={int[], null}[↦4;refId=105]))),
	7: Assignment(pc=34,DVar(useSites={9},value=an int,origin=7),GetField(pc=34,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	8: Assignment(pc=37,DVar(useSites={9},value=int = 1,origin=8),IntConst(pc=37,1)),
	9: Assignment(pc=38,DVar(useSites={10},value=an int,origin=9),BinaryExpr(pc=38,ComputationalTypeInt,UVar(defSites={7},value=an int),+,UVar(defSites={8},value=int = 1))),
	10: Assignment(pc=39,DVar(useSites={88},value=an int,origin=10),ArrayLoad(pc=39,UVar(defSites={9},value=an int),UVar(defSites={0},value=int[][↦4;refId=105]))),
	11: Nop(pc=40),
	12: Assignment(pc=44,DVar(useSites={13},value=an int,origin=12),GetField(pc=44,java.util.regex.Pattern$GroupCurly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	13: If(pc=47,UVar(defSites={-4},value=an int),>=,UVar(defSites={12},value=an int),target=81),
	14: Assignment(pc=54,DVar(useSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦54;refId=110],origin=14),GetField(pc=54,java.util.regex.Pattern$GroupCurly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	15: Assignment(pc=61,DVar(useSites={16},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=61,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦54;refId=110]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	16: If(pc=64,UVar(defSites={15},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=81),
	17: Assignment(pc=71,DVar(useSites={18},value=an int,origin=17),GetField(pc=71,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	18: Assignment(pc=75,DVar(useSites={40,38,65,69,77,29,19,27,47},value=an int,origin=18),BinaryExpr(pc=75,ComputationalTypeInt,UVar(defSites={17},value=an int),-,UVar(defSites={-3},value=an int))),
	19: If(pc=80,UVar(defSites={18},value=an int),>,IntConst(pc=-333,0),target=31),
	20: Assignment(pc=84,DVar(useSites={21},value=int ∈ [0,1],origin=20),GetField(pc=84,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	21: If(pc=87,UVar(defSites={20},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=29),
	22: Assignment(pc=93,DVar(useSites={23},value=an int,origin=22),GetField(pc=93,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	23: ArrayStore(pc=97,UVar(defSites={0},value={int[], null}[↦4;refId=105]),UVar(defSites={22},value=an int),UVar(defSites={-3},value=an int)),
	24: Assignment(pc=101,DVar(useSites={26},value=an int,origin=24),GetField(pc=101,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	25: Assignment(pc=104,DVar(useSites={26},value=int = 1,origin=25),IntConst(pc=104,1)),
	26: Assignment(pc=105,DVar(useSites={28},value=an int,origin=26),BinaryExpr(pc=105,ComputationalTypeInt,UVar(defSites={24},value=an int),+,UVar(defSites={25},value=int = 1))),
	27: Assignment(pc=109,DVar(useSites={28},value=an int,origin=27),BinaryExpr(pc=109,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={18},value=int ∈ [-2147483648,0]))),
	28: ArrayStore(pc=110,UVar(defSites={0},value=int[][↦4;refId=105]),UVar(defSites={26},value=an int),UVar(defSites={27},value=an int)),
	29: Assignment(pc=114,DVar(useSites={90},value=an int,origin=29),BinaryExpr(pc=114,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={18},value=int ∈ [-2147483648,0]))),
	30: Goto(pc=116,target=81),
	31: Assignment(pc=120,DVar(useSites={32},value=int ∈ [0,1],origin=31),GetField(pc=120,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	32: If(pc=123,UVar(defSites={31},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=40),
	33: Assignment(pc=129,DVar(useSites={34},value=an int,origin=33),GetField(pc=129,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	34: ArrayStore(pc=133,UVar(defSites={0},value={int[], null}[↦4;refId=105]),UVar(defSites={33},value=an int),UVar(defSites={40,-3},value=an int)),
	35: Assignment(pc=137,DVar(useSites={37},value=an int,origin=35),GetField(pc=137,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	36: Assignment(pc=140,DVar(useSites={37},value=int = 1,origin=36),IntConst(pc=140,1)),
	37: Assignment(pc=141,DVar(useSites={39},value=an int,origin=37),BinaryExpr(pc=141,ComputationalTypeInt,UVar(defSites={35},value=an int),+,UVar(defSites={36},value=int = 1))),
	38: Assignment(pc=145,DVar(useSites={39},value=an int,origin=38),BinaryExpr(pc=145,ComputationalTypeInt,UVar(defSites={40,-3},value=an int),+,UVar(defSites={18},value=int ∈ [1,2147483647]))),
	39: ArrayStore(pc=146,UVar(defSites={0},value=int[][↦4;refId=105]),UVar(defSites={37},value=an int),UVar(defSites={38},value=an int)),
	40: Assignment(pc=150,DVar(useSites={56,34,50,90,38,65,41,69,45,47,63},value=an int,origin=40),BinaryExpr(pc=150,ComputationalTypeInt,UVar(defSites={40,-3},value=an int),+,UVar(defSites={18},value=int ∈ [1,2147483647]))),
	41: Assignment(pc=152,DVar(useSites={50,42,54,43,79},value=int ∈ [-2147483647,2147483647],origin=41),BinaryExpr(pc=152,ComputationalTypeInt,UVar(defSites={-4,41},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=152,1))),
	42: Assignment(pc=157,DVar(useSites={43},value=an int,origin=42),GetField(pc=157,java.util.regex.Pattern$GroupCurly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	43: If(pc=160,UVar(defSites={41},value=int ∈ [-2147483647,2147483647]),>=,UVar(defSites={42},value=an int),target=54),
	44: Assignment(pc=167,DVar(useSites={45},value={_ <: java.util.regex.Pattern$Node, null}[↦167;refId=141],origin=44),GetField(pc=167,java.util.regex.Pattern$GroupCurly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	45: Assignment(pc=174,DVar(useSites={46},value=int ∈ [0,1],origin=45),VirtualFunctionCall(pc=174,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={44},value={_ <: java.util.regex.Pattern$Node, null}[↦167;refId=141]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={40},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	46: If(pc=177,UVar(defSites={45},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=54),
	47: Assignment(pc=186,DVar(useSites={49},value=an int,origin=47),BinaryExpr(pc=186,ComputationalTypeInt,UVar(defSites={40},value=an int),+,UVar(defSites={18},value=int ∈ [1,2147483647]))),
	48: Assignment(pc=188,DVar(useSites={49},value=an int,origin=48),GetField(pc=188,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	49: If(pc=191,UVar(defSites={47},value=an int),==,UVar(defSites={48},value=an int),target=31),
	50: Assignment(pc=200,DVar(useSites={51},value=int ∈ [0,1],origin=50),VirtualFunctionCall(pc=200,java.util.regex.Pattern$GroupCurly,isInterface=false,boolean match0(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={40},value=an int),UVar(defSites={41},value=int ∈ [-2147483647,2147483646]),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	51: If(pc=203,UVar(defSites={50},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=54),
	52: Assignment(pc=206,DVar(useSites={53},value=int = 1,origin=52),IntConst(pc=206,1)),
	53: ReturnValue(pc=207,UVar(defSites={52},value=int = 1)),
	54: If(pc=211,UVar(defSites={41,79},value=an int),<=,UVar(defSites={-4},value=int ∈ [-2147483648,2147483646]),target=81),
	55: Assignment(pc=215,DVar(useSites={56},value={_ <: java.util.regex.Pattern$Node, null}[↦215;refId=145],origin=55),GetField(pc=215,java.util.regex.Pattern$GroupCurly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	56: Assignment(pc=222,DVar(useSites={57},value=int ∈ [0,1],origin=56),VirtualFunctionCall(pc=222,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={55},value={_ <: java.util.regex.Pattern$Node, null}[↦215;refId=145]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={40,69},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	57: If(pc=225,UVar(defSites={56},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=69),
	58: Assignment(pc=229,DVar(useSites={59},value=int ∈ [0,1],origin=58),GetField(pc=229,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	59: If(pc=232,UVar(defSites={58},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=67),
	60: Assignment(pc=238,DVar(useSites={62},value=an int,origin=60),GetField(pc=238,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	61: Assignment(pc=241,DVar(useSites={62},value=int = 1,origin=61),IntConst(pc=241,1)),
	62: Assignment(pc=242,DVar(useSites={63},value=an int,origin=62),BinaryExpr(pc=242,ComputationalTypeInt,UVar(defSites={60},value=an int),+,UVar(defSites={61},value=int = 1))),
	63: ArrayStore(pc=244,UVar(defSites={0},value={int[], null}[↦4;refId=105]),UVar(defSites={62},value=an int),UVar(defSites={40,69},value=an int)),
	64: Assignment(pc=248,DVar(useSites={66},value=an int,origin=64),GetField(pc=248,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	65: Assignment(pc=254,DVar(useSites={66},value=an int,origin=65),BinaryExpr(pc=254,ComputationalTypeInt,UVar(defSites={40,69},value=an int),-,UVar(defSites={18},value=int ∈ [1,2147483647]))),
	66: ArrayStore(pc=255,UVar(defSites={0},value=int[][↦4;refId=105]),UVar(defSites={64},value=an int),UVar(defSites={65},value=an int)),
	67: Assignment(pc=256,DVar(useSites={68},value=int = 1,origin=67),IntConst(pc=256,1)),
	68: ReturnValue(pc=257,UVar(defSites={67},value=int = 1)),
	69: Assignment(pc=261,DVar(useSites={56,90,70,65,77,75,63},value=an int,origin=69),BinaryExpr(pc=261,ComputationalTypeInt,UVar(defSites={40,69},value=an int),-,UVar(defSites={18},value=int ∈ [1,2147483647]))),
	70: Assignment(pc=264,DVar(useSites={71},value=int ∈ [0,1],origin=70),GetField(pc=264,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	71: If(pc=267,UVar(defSites={70},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=79),
	72: Assignment(pc=273,DVar(useSites={74},value=an int,origin=72),GetField(pc=273,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	73: Assignment(pc=276,DVar(useSites={74},value=int = 1,origin=73),IntConst(pc=276,1)),
	74: Assignment(pc=277,DVar(useSites={75},value=an int,origin=74),BinaryExpr(pc=277,ComputationalTypeInt,UVar(defSites={72},value=an int),+,UVar(defSites={73},value=int = 1))),
	75: ArrayStore(pc=279,UVar(defSites={0},value={int[], null}[↦4;refId=105]),UVar(defSites={74},value=an int),UVar(defSites={69},value=an int)),
	76: Assignment(pc=283,DVar(useSites={78},value=an int,origin=76),GetField(pc=283,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	77: Assignment(pc=289,DVar(useSites={78},value=an int,origin=77),BinaryExpr(pc=289,ComputationalTypeInt,UVar(defSites={69},value=an int),-,UVar(defSites={18},value=int ∈ [1,2147483647]))),
	78: ArrayStore(pc=290,UVar(defSites={0},value=int[][↦4;refId=105]),UVar(defSites={76},value=an int),UVar(defSites={77},value=an int)),
	79: Assignment(pc=291,DVar(useSites={80,54},value=int ∈ [-2147483648,2147483646],origin=79),BinaryExpr(pc=291,ComputationalTypeInt,UVar(defSites={41,79},value=int ∈ [-2147483647,2147483647]),+,IntConst(pc=291,-1))),
	80: Goto(pc=294,target=54),
	81: Assignment(pc=298,DVar(useSites={82},value=int ∈ [0,1],origin=81),GetField(pc=298,java.util.regex.Pattern$GroupCurly,capture,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	82: If(pc=301,UVar(defSites={81},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=89),
	83: Assignment(pc=307,DVar(useSites={84},value=an int,origin=83),GetField(pc=307,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	84: ArrayStore(pc=312,UVar(defSites={0},value={int[], null}[↦4;refId=105]),UVar(defSites={83},value=an int),UVar(defSites={6,1},value=an int)),
	85: Assignment(pc=316,DVar(useSites={87},value=an int,origin=85),GetField(pc=316,java.util.regex.Pattern$GroupCurly,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	86: Assignment(pc=319,DVar(useSites={87},value=int = 1,origin=86),IntConst(pc=319,1)),
	87: Assignment(pc=320,DVar(useSites={88},value=an int,origin=87),BinaryExpr(pc=320,ComputationalTypeInt,UVar(defSites={85},value=an int),+,UVar(defSites={86},value=int = 1))),
	88: ArrayStore(pc=323,UVar(defSites={0},value=int[][↦4;refId=105]),UVar(defSites={87},value=an int),UVar(defSites={2,10},value=an int)),
	89: Assignment(pc=325,DVar(useSites={90},value={_ <: java.util.regex.Pattern$Node, null}[↦325;refId=122],origin=89),GetField(pc=325,java.util.regex.Pattern$GroupCurly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupCurly[↦-1;refId=102]))),
	90: Assignment(pc=332,DVar(useSites={91},value=int ∈ [0,1],origin=90),VirtualFunctionCall(pc=332,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={89},value={_ <: java.util.regex.Pattern$Node, null}[↦325;refId=122]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={40,69,29,-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	91: ReturnValue(pc=335,UVar(defSites={90},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=6) -> {BB_28,BB_1e}
	BB_10: BasicBlock(start=57,end=57) -> {BB_6,BB_a}
	BB_11: BasicBlock(start=29,end=30) -> {BB_1c}
	BB_12: BasicBlock(start=89,end=90) -> {BB_28,BB_3}
	BB_13: BasicBlock(start=1,end=4) -> {BB_1a,BB_0}
	BB_14: BasicBlock(start=60,end=63) -> {BB_28,BB_16}
	BB_15: BasicBlock(start=85,end=88) -> {BB_28,BB_12}
	BB_16: BasicBlock(start=64,end=66) -> {BB_28,BB_20}
	BB_17: BasicBlock(start=17,end=19) -> {BB_e,BB_22}
	BB_18: BasicBlock(start=22,end=23) -> {BB_28,BB_1}
	BB_19: BasicBlock(start=44,end=45) -> {BB_28,BB_f}
	BB_1: BasicBlock(start=24,end=28) -> {BB_28,BB_11}
	BB_1a: BasicBlock(start=12,end=13) -> {BB_d,BB_1c}
	BB_1b: BasicBlock(start=54,end=54) -> {BB_26,BB_1c}
	BB_1c: BasicBlock(start=81,end=82) -> {BB_9,BB_12}
	BB_1d: BasicBlock(start=76,end=78) -> {BB_28,BB_27}
	BB_1e: BasicBlock(start=7,end=10) -> {BB_28,BB_23}
	BB_1f: BasicBlock(start=50,end=50) -> {BB_28,BB_7}
	BB_20: BasicBlock(start=67,end=68) -> {BB_5}
	BB_21: BasicBlock(start=16,end=16) -> {BB_1c,BB_17}
	BB_22: BasicBlock(start=31,end=32) -> {BB_2,BB_25}
	BB_23: BasicBlock(start=11,end=11) -> {BB_1a}
	BB_24: BasicBlock(start=72,end=75) -> {BB_28,BB_1d}
	BB_25: BasicBlock(start=40,end=43) -> {BB_1b,BB_19}
	BB_26: BasicBlock(start=55,end=56) -> {BB_28,BB_10}
	BB_27: BasicBlock(start=79,end=80) -> {BB_1b}
	BB_28: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=33,end=34) -> {BB_28,BB_4}
	BB_3: BasicBlock(start=91,end=91) -> {BB_5}
	BB_4: BasicBlock(start=35,end=39) -> {BB_28,BB_25}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=58,end=59) -> {BB_20,BB_14}
	BB_7: BasicBlock(start=51,end=51) -> {BB_1b,BB_c}
	BB_8: BasicBlock(start=47,end=49) -> {BB_1f,BB_22}
	BB_9: BasicBlock(start=83,end=84) -> {BB_28,BB_15}
	BB_a: BasicBlock(start=69,end=71) -> {BB_24,BB_27}
	BB_b: BasicBlock(start=0,end=0) -> {BB_28,BB_13}
	BB_c: BasicBlock(start=52,end=53) -> {BB_5}
	BB_d: BasicBlock(start=14,end=15) -> {BB_28,BB_21}
	BB_e: BasicBlock(start=20,end=21) -> {BB_18,BB_11}
	BB_f: BasicBlock(start=46,end=46) -> {BB_1b,BB_8}
))

