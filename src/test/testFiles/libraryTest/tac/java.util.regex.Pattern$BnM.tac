boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={1,7} (origin=-1),
	1: useSites={0,8,4,6} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={3},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={2},value={int[], null}[↦6;refId=105],origin=1),GetField(pc=6,java.util.regex.Pattern$BnM,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=9,UVar(defSites={1},value={int[], null}[↦6;refId=105]))),
	3: Assignment(pc=10,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=10,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={2},value=int ∈ [0,2147483647]))),
	4: PutField(pc=11,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=15,DVar(useSites={6},value=int = 0,origin=5),IntConst(pc=15,0)),
	6: PutField(pc=16,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={5},value=int = 0)),
	7: Assignment(pc=20,DVar(useSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦20;refId=107],origin=7),GetField(pc=20,java.util.regex.Pattern$BnM,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]))),
	8: Assignment(pc=24,DVar(useSites={9},value=int ∈ [0,1],origin=8),VirtualFunctionCall(pc=24,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦20;refId=107]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	9: ReturnValue(pc=27,UVar(defSites={8},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_5,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_5,BB_3}
	BB_2: BasicBlock(start=9,end=9) -> {BB_4}
	BB_3: BasicBlock(start=3,end=8) -> {BB_5,BB_2}
	BB_4: ExitNode(normalReturn=true)
	BB_5: ExitNode(normalReturn=false)
))

void <init>(int[],int[],int[],java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,4,2,1,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3),
	3: useSites={3} (origin=-4),
	4: useSites={4} (origin=-5)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$BnM,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]),UVar(defSites={-2},value={int[], null}[↦-2;refId=103])),
	2: PutField(pc=11,java.util.regex.Pattern$BnM,lastOcc,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]),UVar(defSites={-3},value={int[], null}[↦-3;refId=104])),
	3: PutField(pc=16,java.util.regex.Pattern$BnM,optoSft,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]),UVar(defSites={-4},value={int[], null}[↦-4;refId=105])),
	4: PutField(pc=22,java.util.regex.Pattern$BnM,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]),UVar(defSites={-5},value={_ <: java.util.regex.Pattern$Node, null}[↦-5;refId=106])),
	5: Return(pc=25)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=5) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$Node optimize(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	1: useSites={0,8,4,2,46,49,53,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),InstanceOf(pc=1,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-1;refId=102]),java.util.regex.Pattern$Slice)),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=3),
	2: ReturnValue(pc=8,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-1;refId=102])),
	3: Checkcast(pc=10,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-1;refId=102]),java.util.regex.Pattern$Slice),
	4: Assignment(pc=13,DVar(useSites={50,54,14,5,29,27},value={int[], null}[↦13;refId=105],origin=4),GetField(pc=13,java.util.regex.Pattern$Slice,buffer,int[],UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Slice, null}[↦-1;refId=103]))),
	5: Assignment(pc=18,DVar(useSites={40,28,26,38,33,25,13,11,43,7,23},value=int ∈ [0,2147483647],origin=5),ArrayLength(pc=18,UVar(defSites={4},value={int[], null}[↦13;refId=105]))),
	6: Assignment(pc=21,DVar(useSites={7},value=int = 4,origin=6),IntConst(pc=21,4)),
	7: If(pc=22,UVar(defSites={5},value=int ∈ [0,2147483647]),>=,UVar(defSites={6},value=int = 4),target=9),
	8: ReturnValue(pc=26,UVar(defSites={-2},value=_ <: java.util.regex.Pattern$Slice[↦-1;refId=103])),
	9: Assignment(pc=27,DVar(useSites={10},value=int = 128,origin=9),IntConst(pc=27,128)),
	10: Assignment(pc=30,DVar(useSites={50,54,19},value=int[][↦30;refId=108;length=128],origin=10),NewArray(pc=30,[UVar(defSites={9},value=int = 128)],int[])),
	11: Assignment(pc=35,DVar(useSites={50,38,54,33,45},value=int[][↦35;refId=109],origin=11),NewArray(pc=35,[UVar(defSites={5},value=int ∈ [4,2147483647])],int[])),
	12: Assignment(pc=39,DVar(useSites={20,18,14,13},value=int = 0,origin=12),IntConst(pc=39,0)),
	13: If(pc=43,UVar(defSites={20,12},value=int ∈ [0,2147483647]),>=,UVar(defSites={5},value=int ∈ [4,2147483647]),target=22),
	14: Assignment(pc=50,DVar(useSites={16},value=an int,origin=14),ArrayLoad(pc=50,UVar(defSites={20,12},value=int ∈ [0,2147483646]),UVar(defSites={4},value=int[][↦13;refId=105]))),
	15: Assignment(pc=51,DVar(useSites={16},value=int = 127,origin=15),IntConst(pc=51,127)),
	16: Assignment(pc=53,DVar(useSites={19},value=int ∈ [0,127],origin=16),BinaryExpr(pc=53,ComputationalTypeInt,UVar(defSites={14},value=an int),&,UVar(defSites={15},value=int = 127))),
	17: Assignment(pc=55,DVar(useSites={18},value=int = 1,origin=17),IntConst(pc=55,1)),
	18: Assignment(pc=56,DVar(useSites={19},value=int ∈ [1,2147483647],origin=18),BinaryExpr(pc=56,ComputationalTypeInt,UVar(defSites={20,12},value=int ∈ [0,2147483646]),+,UVar(defSites={17},value=int = 1))),
	19: ArrayStore(pc=57,UVar(defSites={10},value=int[][↦30;refId=108;length=128]),UVar(defSites={16},value=int ∈ [0,127]),UVar(defSites={18},value=int ∈ [1,2147483647])),
	20: Assignment(pc=58,DVar(useSites={18,14,21,13},value=int ∈ [1,2147483647],origin=20),BinaryExpr(pc=58,ComputationalTypeInt,UVar(defSites={20,12},value=int ∈ [0,2147483646]),+,IntConst(pc=58,1))),
	21: Goto(pc=61,target=13),
	22: Nop(pc=64),
	23: If(pc=67,UVar(defSites={40,5},value=int ∈ [-128,2147483647]),<=,IntConst(pc=-333,0),target=42),
	24: Assignment(pc=71,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=71,1)),
	25: Assignment(pc=72,DVar(useSites={32,36,28,34,26,37,27},value=int ∈ [-1,2147483646],origin=25),BinaryExpr(pc=72,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,2147483647]),-,UVar(defSites={24},value=int = 1))),
	26: If(pc=78,UVar(defSites={34,25},value=int ∈ [-128,2147483647]),<,UVar(defSites={40,5},value=int ∈ [0,2147483647]),target=36),
	27: Assignment(pc=84,DVar(useSites={30},value=an int,origin=27),ArrayLoad(pc=84,UVar(defSites={34,25},value=int ∈ [0,2147483647]),UVar(defSites={4},value=int[][↦13;refId=105]))),
	28: Assignment(pc=89,DVar(useSites={29},value=int ∈ [-2147483647,2147483647],origin=28),BinaryExpr(pc=89,ComputationalTypeInt,UVar(defSites={34,25},value=int ∈ [0,2147483647]),-,UVar(defSites={40,5},value=int ∈ [0,2147483647]))),
	29: Assignment(pc=90,DVar(useSites={30},value=an int,origin=29),ArrayLoad(pc=90,UVar(defSites={28},value=int ∈ [-2147483647,2147483647]),UVar(defSites={4},value=int[][↦13;refId=105]))),
	30: If(pc=91,UVar(defSites={27},value=an int),!=,UVar(defSites={29},value=an int),target=40),
	31: Assignment(pc=98,DVar(useSites={32},value=int = 1,origin=31),IntConst(pc=98,1)),
	32: Assignment(pc=99,DVar(useSites={33},value=int ∈ [-1,2147483646],origin=32),BinaryExpr(pc=99,ComputationalTypeInt,UVar(defSites={34,25},value=int ∈ [0,2147483647]),-,UVar(defSites={31},value=int = 1))),
	33: ArrayStore(pc=101,UVar(defSites={11},value=int[][↦35;refId=109]),UVar(defSites={32},value=int ∈ [-1,2147483646]),UVar(defSites={40,5},value=int ∈ [0,2147483647])),
	34: Assignment(pc=102,DVar(useSites={32,36,28,26,37,35,27},value=int ∈ [-1,2147483646],origin=34),BinaryExpr(pc=102,ComputationalTypeInt,UVar(defSites={34,25},value=int ∈ [0,2147483647]),+,IntConst(pc=102,-1))),
	35: Goto(pc=105,target=26),
	36: If(pc=110,UVar(defSites={34,25,37},value=int ∈ [-128,2147483647]),<=,IntConst(pc=-333,0),target=40),
	37: Assignment(pc=115,DVar(useSites={36,38},value=int ∈ [0,2147483646],origin=37),BinaryExpr(pc=115,ComputationalTypeInt,UVar(defSites={34,25,37},value=int ∈ [1,2147483647]),+,IntConst(pc=115,-1))),
	38: ArrayStore(pc=121,UVar(defSites={11},value=int[][↦35;refId=109]),UVar(defSites={37},value=int ∈ [0,2147483646]),UVar(defSites={40,5},value=int ∈ [0,2147483647])),
	39: Goto(pc=122,target=36),
	40: Assignment(pc=125,DVar(useSites={28,26,38,33,41,23},value=int ∈ [-1,2147483646],origin=40),BinaryExpr(pc=125,ComputationalTypeInt,UVar(defSites={40,5},value=int ∈ [0,2147483647]),+,IntConst(pc=125,-1))),
	41: Goto(pc=128,target=23),
	42: Assignment(pc=134,DVar(useSites={43},value=int = 1,origin=42),IntConst(pc=134,1)),
	43: Assignment(pc=135,DVar(useSites={45},value=int ∈ [-1,2147483646],origin=43),BinaryExpr(pc=135,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,2147483647]),-,UVar(defSites={42},value=int = 1))),
	44: Assignment(pc=136,DVar(useSites={45},value=int = 1,origin=44),IntConst(pc=136,1)),
	45: ArrayStore(pc=137,UVar(defSites={11},value=int[][↦35;refId=109]),UVar(defSites={43},value=int ∈ [-1,2147483646]),UVar(defSites={44},value=int = 1)),
	46: Assignment(pc=139,DVar(useSites={47},value=int ∈ [0,1],origin=46),InstanceOf(pc=139,UVar(defSites={-2},value=_ <: java.util.regex.Pattern$Slice[↦-1;refId=103]),java.util.regex.Pattern$SliceS)),
	47: If(pc=142,UVar(defSites={46},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=52),
	48: Assignment(pc=145,DVar(useSites={50,51},value=java.util.regex.Pattern$BnMS[↦145;refId=241],origin=48),New(pc=145,java.util.regex.Pattern$BnMS)),
	49: Assignment(pc=155,DVar(useSites={50},value={_ <: java.util.regex.Pattern$Node, null}[↦155;refId=242],origin=49),GetField(pc=155,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={-2},value=_ <: java.util.regex.Pattern$Slice[↦-1;refId=103]))),
	50: NonVirtualMethodCall(pc=158,java.util.regex.Pattern$BnMS,isInterface=false,void <init>(int[],int[],int[],java.util.regex.Pattern$Node),UVar(defSites={48},value=java.util.regex.Pattern$BnMS[↦145;refId=241]),(UVar(defSites={4},value=int[][↦13;refId=105]),UVar(defSites={10},value=int[][↦30;refId=108;length=128]),UVar(defSites={11},value=int[][↦35;refId=109]),UVar(defSites={49},value={_ <: java.util.regex.Pattern$Node, null}[↦155;refId=242]))),
	51: ReturnValue(pc=161,UVar(defSites={48},value=java.util.regex.Pattern$BnMS[↦145;refId=241])),
	52: Assignment(pc=162,DVar(useSites={54,55},value=java.util.regex.Pattern$BnM[↦162;refId=244],origin=52),New(pc=162,java.util.regex.Pattern$BnM)),
	53: Assignment(pc=172,DVar(useSites={54},value={_ <: java.util.regex.Pattern$Node, null}[↦172;refId=245],origin=53),GetField(pc=172,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={-2},value=_ <: java.util.regex.Pattern$Slice[↦-1;refId=103]))),
	54: NonVirtualMethodCall(pc=175,java.util.regex.Pattern$BnM,isInterface=false,void <init>(int[],int[],int[],java.util.regex.Pattern$Node),UVar(defSites={52},value=java.util.regex.Pattern$BnM[↦162;refId=244]),(UVar(defSites={4},value=int[][↦13;refId=105]),UVar(defSites={10},value=int[][↦30;refId=108;length=128]),UVar(defSites={11},value=int[][↦35;refId=109]),UVar(defSites={53},value={_ <: java.util.regex.Pattern$Node, null}[↦172;refId=245]))),
	55: ReturnValue(pc=178,UVar(defSites={52},value=java.util.regex.Pattern$BnM[↦162;refId=244]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_a,BB_7}
	BB_10: BasicBlock(start=37,end=38) -> {BB_1f,BB_9}
	BB_11: BasicBlock(start=52,end=54) -> {BB_1f,BB_19}
	BB_12: BasicBlock(start=14,end=14) -> {BB_1f,BB_d}
	BB_13: BasicBlock(start=22,end=22) -> {BB_1a}
	BB_14: BasicBlock(start=27,end=27) -> {BB_1f,BB_4}
	BB_15: BasicBlock(start=48,end=50) -> {BB_1f,BB_1d}
	BB_16: ExitNode(normalReturn=true)
	BB_17: BasicBlock(start=40,end=41) -> {BB_1a}
	BB_18: BasicBlock(start=26,end=26) -> {BB_1b,BB_14}
	BB_19: BasicBlock(start=55,end=55) -> {BB_16}
	BB_1: BasicBlock(start=5,end=5) -> {BB_1f,BB_3}
	BB_1a: BasicBlock(start=23,end=23) -> {BB_f,BB_e}
	BB_1b: BasicBlock(start=36,end=36) -> {BB_10,BB_17}
	BB_1c: BasicBlock(start=30,end=30) -> {BB_b,BB_17}
	BB_1d: BasicBlock(start=51,end=51) -> {BB_16}
	BB_1e: BasicBlock(start=4,end=4) -> {BB_1f,BB_1}
	BB_1f: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=46,end=47) -> {BB_11,BB_15}
	BB_3: BasicBlock(start=6,end=7) -> {BB_c,BB_5}
	BB_4: BasicBlock(start=28,end=29) -> {BB_1f,BB_1c}
	BB_5: BasicBlock(start=9,end=12) -> {BB_6}
	BB_6: BasicBlock(start=13,end=13) -> {BB_13,BB_12}
	BB_7: BasicBlock(start=2,end=2) -> {BB_16}
	BB_8: BasicBlock(start=34,end=35) -> {BB_18}
	BB_9: BasicBlock(start=39,end=39) -> {BB_1b}
	BB_a: BasicBlock(start=3,end=3) -> {BB_1f,BB_1e}
	BB_b: BasicBlock(start=31,end=33) -> {BB_1f,BB_8}
	BB_c: BasicBlock(start=8,end=8) -> {BB_16}
	BB_d: BasicBlock(start=15,end=21) -> {BB_6}
	BB_e: BasicBlock(start=42,end=45) -> {BB_1f,BB_2}
	BB_f: BasicBlock(start=24,end=25) -> {BB_18}
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,14,19,27} (origin=-1),
	1: useSites={32,36,2,34,26,38,45,29,31} (origin=-2),
	2: useSites={8,4,28,42,26,22,31} (origin=-3),
	3: useSites={9,29} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={10,1},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$BnM,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]))),
	1: Assignment(pc=8,DVar(useSites={28,6,3},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=8,UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	2: Assignment(pc=12,DVar(useSites={3},value=an int,origin=2),GetField(pc=12,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	3: Assignment(pc=17,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=17,ComputationalTypeInt,UVar(defSites={2},value=an int),-,UVar(defSites={1},value=int ∈ [0,2147483647]))),
	4: If(pc=23,UVar(defSites={42,22,-3},value=an int),>,UVar(defSites={3},value=an int),target=44),
	5: Assignment(pc=28,DVar(useSites={6},value=int = 1,origin=5),IntConst(pc=28,1)),
	6: Assignment(pc=29,DVar(useSites={8,24,20,10,13,7},value=int ∈ [-1,2147483646],origin=6),BinaryExpr(pc=29,ComputationalTypeInt,UVar(defSites={1},value=int ∈ [0,2147483647]),-,UVar(defSites={5},value=int = 1))),
	7: If(pc=34,UVar(defSites={24,6},value=int ∈ [-1,2147483646]),<,IntConst(pc=-333,0),target=26),
	8: Assignment(pc=41,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=41,ComputationalTypeInt,UVar(defSites={42,22,-3},value=an int),+,UVar(defSites={24,6},value=int ∈ [0,2147483646]))),
	9: Assignment(pc=42,DVar(useSites={16,11},value=int ∈ [0,65535],origin=9),VirtualFunctionCall(pc=42,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={8},value=an int)))),
	10: Assignment(pc=55,DVar(useSites={11},value=an int,origin=10),ArrayLoad(pc=55,UVar(defSites={24,6},value=int ∈ [0,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	11: If(pc=56,UVar(defSites={9},value=int ∈ [0,65535]),==,UVar(defSites={10},value=an int),target=24),
	12: Assignment(pc=62,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=62,1)),
	13: Assignment(pc=63,DVar(useSites={18},value=int ∈ [1,2147483647],origin=13),BinaryExpr(pc=63,ComputationalTypeInt,UVar(defSites={24,6},value=int ∈ [0,2147483646]),+,UVar(defSites={12},value=int = 1))),
	14: Assignment(pc=65,DVar(useSites={17},value={int[], null}[↦65;refId=111],origin=14),GetField(pc=65,java.util.regex.Pattern$BnM,lastOcc,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]))),
	15: Assignment(pc=70,DVar(useSites={16},value=int = 127,origin=15),IntConst(pc=70,127)),
	16: Assignment(pc=72,DVar(useSites={17},value=int ∈ [0,65535],origin=16),BinaryExpr(pc=72,ComputationalTypeInt,UVar(defSites={9},value=int ∈ [0,65535]),&,UVar(defSites={15},value=int = 127))),
	17: Assignment(pc=73,DVar(useSites={18},value=an int,origin=17),ArrayLoad(pc=73,UVar(defSites={16},value=int ∈ [0,65535]),UVar(defSites={14},value={int[], null}[↦65;refId=111]))),
	18: Assignment(pc=74,DVar(useSites={21},value=an int,origin=18),BinaryExpr(pc=74,ComputationalTypeInt,UVar(defSites={13},value=int ∈ [1,2147483647]),-,UVar(defSites={17},value=an int))),
	19: Assignment(pc=76,DVar(useSites={20},value={int[], null}[↦76;refId=114],origin=19),GetField(pc=76,java.util.regex.Pattern$BnM,optoSft,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]))),
	20: Assignment(pc=81,DVar(useSites={21},value=an int,origin=20),ArrayLoad(pc=81,UVar(defSites={24,6},value=int ∈ [0,2147483646]),UVar(defSites={19},value={int[], null}[↦76;refId=114]))),
	21: Assignment(pc=82,DVar(useSites={22},value=an int,origin=21),StaticFunctionCall(pc=82,java.lang.Math,isInterface=false,int max(int,int),(UVar(defSites={18},value=an int),UVar(defSites={20},value=an int)))),
	22: Assignment(pc=85,DVar(useSites={8,4,28,42,26,23,31},value=an int,origin=22),BinaryExpr(pc=85,ComputationalTypeInt,UVar(defSites={42,22,-3},value=an int),+,UVar(defSites={21},value=an int))),
	23: Goto(pc=87,target=4),
	24: Assignment(pc=90,DVar(useSites={8,20,10,25,13,7},value=int ∈ [-1,2147483645],origin=24),BinaryExpr(pc=90,ComputationalTypeInt,UVar(defSites={24,6},value=int ∈ [0,2147483646]),+,IntConst(pc=90,-1))),
	25: Goto(pc=93,target=7),
	26: PutField(pc=98,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={42,22,-3},value=an int)),
	27: Assignment(pc=102,DVar(useSites={29},value={_ <: java.util.regex.Pattern$Node, null}[↦102;refId=118],origin=27),GetField(pc=102,java.util.regex.Pattern$BnM,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BnM[↦-1;refId=102]))),
	28: Assignment(pc=109,DVar(useSites={29},value=an int,origin=28),BinaryExpr(pc=109,ComputationalTypeInt,UVar(defSites={42,22,-3},value=an int),+,UVar(defSites={1},value=int ∈ [0,2147483647]))),
	29: Assignment(pc=111,DVar(useSites={30},value=int ∈ [0,1],origin=29),VirtualFunctionCall(pc=111,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦102;refId=118]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={28},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	30: If(pc=118,UVar(defSites={29},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=42),
	31: PutField(pc=123,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={42,22,-3},value=an int)),
	32: Assignment(pc=127,DVar(useSites={35},value={int[], null}[↦127;refId=121],origin=32),GetField(pc=127,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	33: Assignment(pc=130,DVar(useSites={35},value=int = 0,origin=33),IntConst(pc=130,0)),
	34: Assignment(pc=132,DVar(useSites={35},value=an int,origin=34),GetField(pc=132,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	35: ArrayStore(pc=135,UVar(defSites={32},value={int[], null}[↦127;refId=121]),UVar(defSites={33},value=int = 0),UVar(defSites={34},value=an int)),
	36: Assignment(pc=137,DVar(useSites={39},value={int[], null}[↦137;refId=124],origin=36),GetField(pc=137,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	37: Assignment(pc=140,DVar(useSites={39},value=int = 1,origin=37),IntConst(pc=140,1)),
	38: Assignment(pc=142,DVar(useSites={39},value=an int,origin=38),GetField(pc=142,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	39: ArrayStore(pc=145,UVar(defSites={36},value={int[], null}[↦137;refId=124]),UVar(defSites={37},value=int = 1),UVar(defSites={38},value=an int)),
	40: Assignment(pc=146,DVar(useSites={41},value=int = 1,origin=40),IntConst(pc=146,1)),
	41: ReturnValue(pc=147,UVar(defSites={40},value=int = 1)),
	42: Assignment(pc=148,DVar(useSites={8,4,28,26,22,43,31},value=an int,origin=42),BinaryExpr(pc=148,ComputationalTypeInt,UVar(defSites={42,22,-3},value=an int),+,IntConst(pc=148,1))),
	43: Goto(pc=151,target=4),
	44: Assignment(pc=155,DVar(useSites={45},value=int = 1,origin=44),IntConst(pc=155,1)),
	45: PutField(pc=156,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={44},value=int = 1)),
	46: Assignment(pc=159,DVar(useSites={47},value=int = 0,origin=46),IntConst(pc=159,0)),
	47: ReturnValue(pc=160,UVar(defSites={46},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_16,BB_4}
	BB_10: ExitNode(normalReturn=true)
	BB_11: BasicBlock(start=40,end=41) -> {BB_10}
	BB_12: BasicBlock(start=26,end=29) -> {BB_16,BB_14}
	BB_13: BasicBlock(start=36,end=39) -> {BB_16,BB_11}
	BB_14: BasicBlock(start=30,end=30) -> {BB_b,BB_8}
	BB_15: BasicBlock(start=4,end=4) -> {BB_1,BB_e}
	BB_16: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=6) -> {BB_6}
	BB_2: BasicBlock(start=10,end=10) -> {BB_16,BB_9}
	BB_3: BasicBlock(start=21,end=21) -> {BB_16,BB_d}
	BB_4: BasicBlock(start=2,end=2) -> {BB_16,BB_7}
	BB_5: BasicBlock(start=12,end=17) -> {BB_16,BB_f}
	BB_6: BasicBlock(start=7,end=7) -> {BB_12,BB_a}
	BB_7: BasicBlock(start=3,end=3) -> {BB_15}
	BB_8: BasicBlock(start=31,end=35) -> {BB_16,BB_13}
	BB_9: BasicBlock(start=11,end=11) -> {BB_c,BB_5}
	BB_a: BasicBlock(start=8,end=9) -> {BB_16,BB_2}
	BB_b: BasicBlock(start=42,end=43) -> {BB_15}
	BB_c: BasicBlock(start=24,end=25) -> {BB_6}
	BB_d: BasicBlock(start=22,end=23) -> {BB_15}
	BB_e: BasicBlock(start=44,end=47) -> {BB_10}
	BB_f: BasicBlock(start=18,end=20) -> {BB_16,BB_3}
))

