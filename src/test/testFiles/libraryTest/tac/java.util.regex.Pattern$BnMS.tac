boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,32,16,33,21,3} (origin=-1),
	1: useSites={40,44,2,42,38,37,53,35,31} (origin=-2),
	2: useSites={24,34,50,10,6,49,25,5,37,31} (origin=-3),
	3: useSites={24,6,49,35,11} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={12,1},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$BnMS,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	1: Assignment(pc=8,DVar(useSites={8,6},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=8,UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	2: Assignment(pc=12,DVar(useSites={4},value=an int,origin=2),GetField(pc=12,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	3: Assignment(pc=16,DVar(useSites={4},value=an int,origin=3),GetField(pc=16,java.util.regex.Pattern$BnMS,lengthInChars,int,UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	4: Assignment(pc=19,DVar(useSites={5},value=an int,origin=4),BinaryExpr(pc=19,ComputationalTypeInt,UVar(defSites={2},value=an int),-,UVar(defSites={3},value=an int))),
	5: If(pc=25,UVar(defSites={50,25,-3},value=an int),>,UVar(defSites={4},value=an int),target=52),
	6: Assignment(pc=32,DVar(useSites={28,10,9},value=an int,origin=6),StaticFunctionCall(pc=32,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={50,25,-3},value=an int),UVar(defSites={1},value=int ∈ [0,2147483647])))),
	7: Assignment(pc=39,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=39,1)),
	8: Assignment(pc=40,DVar(useSites={12,22,29,15},value=int ∈ [-1,2147483646],origin=8),BinaryExpr(pc=40,ComputationalTypeInt,UVar(defSites={1},value=int ∈ [0,2147483647]),-,UVar(defSites={7},value=int = 1))),
	9: If(pc=45,UVar(defSites={28,6},value=an int),<=,IntConst(pc=-333,0),target=31),
	10: Assignment(pc=52,DVar(useSites={11},value=an int,origin=10),BinaryExpr(pc=52,ComputationalTypeInt,UVar(defSites={50,25,-3},value=an int),+,UVar(defSites={28,6},value=int ∈ [1,2147483647]))),
	11: Assignment(pc=53,DVar(useSites={18,13,27},value=an int,origin=11),StaticFunctionCall(pc=53,java.lang.Character,isInterface=false,int codePointBefore(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={10},value=an int)))),
	12: Assignment(pc=64,DVar(useSites={13},value=an int,origin=12),ArrayLoad(pc=64,UVar(defSites={8,29},value=an int),UVar(defSites={0},value=int[][↦1;refId=105]))),
	13: If(pc=65,UVar(defSites={11},value=an int),==,UVar(defSites={12},value=an int),target=27),
	14: Assignment(pc=70,DVar(useSites={15},value=int = 1,origin=14),IntConst(pc=70,1)),
	15: Assignment(pc=71,DVar(useSites={20},value=an int,origin=15),BinaryExpr(pc=71,ComputationalTypeInt,UVar(defSites={8,29},value=an int),+,UVar(defSites={14},value=int = 1))),
	16: Assignment(pc=73,DVar(useSites={19},value={int[], null}[↦73;refId=175],origin=16),GetField(pc=73,java.util.regex.Pattern$BnMS,lastOcc,int[],UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	17: Assignment(pc=78,DVar(useSites={18},value=int = 127,origin=17),IntConst(pc=78,127)),
	18: Assignment(pc=80,DVar(useSites={19},value=int ∈ [0,127],origin=18),BinaryExpr(pc=80,ComputationalTypeInt,UVar(defSites={11},value=an int),&,UVar(defSites={17},value=int = 127))),
	19: Assignment(pc=81,DVar(useSites={20},value=an int,origin=19),ArrayLoad(pc=81,UVar(defSites={18},value=int ∈ [0,127]),UVar(defSites={16},value={int[], null}[↦73;refId=175]))),
	20: Assignment(pc=82,DVar(useSites={23},value=an int,origin=20),BinaryExpr(pc=82,ComputationalTypeInt,UVar(defSites={15},value=an int),-,UVar(defSites={19},value=an int))),
	21: Assignment(pc=84,DVar(useSites={22},value={int[], null}[↦84;refId=178],origin=21),GetField(pc=84,java.util.regex.Pattern$BnMS,optoSft,int[],UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	22: Assignment(pc=89,DVar(useSites={23},value=an int,origin=22),ArrayLoad(pc=89,UVar(defSites={8,29},value=an int),UVar(defSites={21},value={int[], null}[↦84;refId=178]))),
	23: Assignment(pc=90,DVar(useSites={24},value=an int,origin=23),StaticFunctionCall(pc=90,java.lang.Math,isInterface=false,int max(int,int),(UVar(defSites={20},value=an int),UVar(defSites={22},value=an int)))),
	24: Assignment(pc=100,DVar(useSites={25},value=an int,origin=24),StaticFunctionCall(pc=100,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={50,25,-3},value=an int),UVar(defSites={23},value=an int)))),
	25: Assignment(pc=103,DVar(useSites={24,34,50,10,26,6,49,5,37,31},value=an int,origin=25),BinaryExpr(pc=103,ComputationalTypeInt,UVar(defSites={50,25,-3},value=an int),+,UVar(defSites={24},value=an int))),
	26: Goto(pc=105,target=5),
	27: Assignment(pc=112,DVar(useSites={28},value=an int,origin=27),StaticFunctionCall(pc=112,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={11},value=an int)))),
	28: Assignment(pc=115,DVar(useSites={10,9,29},value=an int,origin=28),BinaryExpr(pc=115,ComputationalTypeInt,UVar(defSites={28,6},value=int ∈ [1,2147483647]),-,UVar(defSites={27},value=an int))),
	29: Assignment(pc=118,DVar(useSites={12,22,30,15},value=an int,origin=29),BinaryExpr(pc=118,ComputationalTypeInt,UVar(defSites={8,29},value=an int),+,IntConst(pc=118,-1))),
	30: Goto(pc=121,target=9),
	31: PutField(pc=126,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={50,25,-3},value=an int)),
	32: Assignment(pc=130,DVar(useSites={35},value={_ <: java.util.regex.Pattern$Node, null}[↦130;refId=183],origin=32),GetField(pc=130,java.util.regex.Pattern$BnMS,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	33: Assignment(pc=136,DVar(useSites={34},value=an int,origin=33),GetField(pc=136,java.util.regex.Pattern$BnMS,lengthInChars,int,UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	34: Assignment(pc=139,DVar(useSites={35},value=an int,origin=34),BinaryExpr(pc=139,ComputationalTypeInt,UVar(defSites={50,25,-3},value=an int),+,UVar(defSites={33},value=an int))),
	35: Assignment(pc=141,DVar(useSites={36},value=int ∈ [0,1],origin=35),VirtualFunctionCall(pc=141,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={32},value={_ <: java.util.regex.Pattern$Node, null}[↦130;refId=183]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={34},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	36: If(pc=148,UVar(defSites={35},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=48),
	37: PutField(pc=153,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={50,25,-3},value=an int)),
	38: Assignment(pc=157,DVar(useSites={41},value={int[], null}[↦157;refId=186],origin=38),GetField(pc=157,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	39: Assignment(pc=160,DVar(useSites={41},value=int = 0,origin=39),IntConst(pc=160,0)),
	40: Assignment(pc=162,DVar(useSites={41},value=an int,origin=40),GetField(pc=162,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	41: ArrayStore(pc=165,UVar(defSites={38},value={int[], null}[↦157;refId=186]),UVar(defSites={39},value=int = 0),UVar(defSites={40},value=an int)),
	42: Assignment(pc=167,DVar(useSites={45},value={int[], null}[↦167;refId=189],origin=42),GetField(pc=167,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	43: Assignment(pc=170,DVar(useSites={45},value=int = 1,origin=43),IntConst(pc=170,1)),
	44: Assignment(pc=172,DVar(useSites={45},value=an int,origin=44),GetField(pc=172,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	45: ArrayStore(pc=175,UVar(defSites={42},value={int[], null}[↦167;refId=189]),UVar(defSites={43},value=int = 1),UVar(defSites={44},value=an int)),
	46: Assignment(pc=176,DVar(useSites={47},value=int = 1,origin=46),IntConst(pc=176,1)),
	47: ReturnValue(pc=177,UVar(defSites={46},value=int = 1)),
	48: Assignment(pc=181,DVar(useSites={49},value=int = 1,origin=48),IntConst(pc=181,1)),
	49: Assignment(pc=182,DVar(useSites={50},value=an int,origin=49),StaticFunctionCall(pc=182,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={50,25,-3},value=an int),UVar(defSites={48},value=int = 1)))),
	50: Assignment(pc=185,DVar(useSites={24,34,10,6,49,25,5,37,51,31},value=an int,origin=50),BinaryExpr(pc=185,ComputationalTypeInt,UVar(defSites={50,25,-3},value=an int),+,UVar(defSites={49},value=an int))),
	51: Goto(pc=187,target=5),
	52: Assignment(pc=191,DVar(useSites={53},value=int = 1,origin=52),IntConst(pc=191,1)),
	53: PutField(pc=192,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={52},value=int = 1)),
	54: Assignment(pc=195,DVar(useSites={55},value=int = 0,origin=54),IntConst(pc=195,0)),
	55: ReturnValue(pc=196,UVar(defSites={54},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_e,BB_7}
	BB_10: BasicBlock(start=24,end=24) -> {BB_e,BB_12}
	BB_11: BasicBlock(start=37,end=41) -> {BB_e,BB_f}
	BB_12: BasicBlock(start=25,end=26) -> {BB_1}
	BB_13: BasicBlock(start=52,end=55) -> {BB_18}
	BB_14: BasicBlock(start=14,end=19) -> {BB_e,BB_15}
	BB_15: BasicBlock(start=20,end=22) -> {BB_e,BB_c}
	BB_16: BasicBlock(start=46,end=47) -> {BB_18}
	BB_17: BasicBlock(start=48,end=49) -> {BB_e,BB_19}
	BB_18: ExitNode(normalReturn=true)
	BB_19: BasicBlock(start=50,end=51) -> {BB_1}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3,BB_13}
	BB_1a: BasicBlock(start=31,end=35) -> {BB_e,BB_d}
	BB_2: BasicBlock(start=10,end=11) -> {BB_e,BB_9}
	BB_3: BasicBlock(start=6,end=6) -> {BB_e,BB_a}
	BB_4: BasicBlock(start=28,end=30) -> {BB_5}
	BB_5: BasicBlock(start=9,end=9) -> {BB_2,BB_1a}
	BB_6: BasicBlock(start=13,end=13) -> {BB_14,BB_8}
	BB_7: BasicBlock(start=2,end=2) -> {BB_e,BB_b}
	BB_8: BasicBlock(start=27,end=27) -> {BB_e,BB_4}
	BB_9: BasicBlock(start=12,end=12) -> {BB_e,BB_6}
	BB_a: BasicBlock(start=7,end=8) -> {BB_5}
	BB_b: BasicBlock(start=3,end=4) -> {BB_1}
	BB_c: BasicBlock(start=23,end=23) -> {BB_e,BB_10}
	BB_d: BasicBlock(start=36,end=36) -> {BB_17,BB_11}
	BB_e: ExitNode(normalReturn=false)
	BB_f: BasicBlock(start=42,end=45) -> {BB_e,BB_16}
))

void <init>(int[],int[],int[],java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,6,1,9} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4),
	4: useSites={0} (origin=-5)
)),stmts=(
	0: NonVirtualMethodCall(pc=6,java.util.regex.Pattern$BnM,isInterface=false,void <init>(int[],int[],int[],java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]),(UVar(defSites={-2},value={int[], null}[↦-2;refId=103]),UVar(defSites={-3},value={int[], null}[↦-3;refId=104]),UVar(defSites={-4},value={int[], null}[↦-4;refId=105]),UVar(defSites={-5},value={_ <: java.util.regex.Pattern$Node, null}[↦-5;refId=106]))),
	1: Assignment(pc=10,DVar(useSites={2,5},value={int[], null}[↦10;refId=108],origin=1),GetField(pc=10,java.util.regex.Pattern$BnMS,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	2: Assignment(pc=17,DVar(useSites={4},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=17,UVar(defSites={1},value={int[], null}[↦10;refId=108]))),
	3: Assignment(pc=20,DVar(useSites={4,10,5},value=int = 0,origin=3),IntConst(pc=20,0)),
	4: If(pc=27,UVar(defSites={10,3},value=int ∈ [0,2147483647]),>=,UVar(defSites={2},value=int ∈ [0,2147483647]),target=12),
	5: Assignment(pc=34,DVar(useSites={7},value=an int,origin=5),ArrayLoad(pc=34,UVar(defSites={10,3},value=int ∈ [0,2147483646]),UVar(defSites={1},value=int[][↦10;refId=108]))),
	6: Assignment(pc=39,DVar(useSites={8},value=an int,origin=6),GetField(pc=39,java.util.regex.Pattern$BnMS,lengthInChars,int,UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]))),
	7: Assignment(pc=44,DVar(useSites={8},value=an int,origin=7),StaticFunctionCall(pc=44,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={5},value=an int)))),
	8: Assignment(pc=47,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=47,ComputationalTypeInt,UVar(defSites={6},value=an int),+,UVar(defSites={7},value=an int))),
	9: PutField(pc=48,java.util.regex.Pattern$BnMS,lengthInChars,int,UVar(defSites={-1},value=java.util.regex.Pattern$BnMS[↦-1;refId=102]),UVar(defSites={8},value=an int)),
	10: Assignment(pc=51,DVar(useSites={4,5,11},value=int ∈ [1,2147483647],origin=10),BinaryExpr(pc=51,ComputationalTypeInt,UVar(defSites={10,3},value=int ∈ [0,2147483646]),+,IntConst(pc=51,1))),
	11: Goto(pc=54,target=4),
	12: Return(pc=57)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_9,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_9,BB_3}
	BB_2: BasicBlock(start=1,end=2) -> {BB_9,BB_5}
	BB_3: BasicBlock(start=6,end=7) -> {BB_9,BB_7}
	BB_4: BasicBlock(start=12,end=12) -> {BB_6}
	BB_5: BasicBlock(start=3,end=3) -> {BB_8}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=8,end=11) -> {BB_8}
	BB_8: BasicBlock(start=4,end=4) -> {BB_1,BB_4}
	BB_9: ExitNode(normalReturn=false)
))

