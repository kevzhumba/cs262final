int cursor()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: ReturnValue(pc=4,UVar(defSites={0},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

int skip()
AITACode(params=(Parameters(
	0: useSites={0,1,7} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={6,3},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={4},value={int[], null}[↦6;refId=103],origin=1),GetField(pc=6,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=10,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=10,1)),
	3: Assignment(pc=11,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=11,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={2},value=int = 1))),
	4: Assignment(pc=12,DVar(useSites={8},value=an int,origin=4),ArrayLoad(pc=12,UVar(defSites={3},value=an int),UVar(defSites={1},value={int[], null}[↦6;refId=103]))),
	5: Assignment(pc=16,DVar(useSites={6},value=int = 2,origin=5),IntConst(pc=16,2)),
	6: Assignment(pc=17,DVar(useSites={7},value=an int,origin=6),BinaryExpr(pc=17,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={5},value=int = 2))),
	7: PutField(pc=18,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={6},value=an int)),
	8: ReturnValue(pc=22,UVar(defSites={4},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=4) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=5,end=8) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$Node group0()
AITACode(params=(Parameters(
	0: useSites={64,160,112,136,40,56,20,148,84,212,52,244,12,28,156,220,2,18,170,234,154,58,122,6,134,70,14,142,1,225,81,113,9,41,57,121,5,69,229,149,13,141,109,237,29,131,67,195,35,19,147,83,27,59,187,123,135,71,151,119,247,143,159} (origin=-1)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={211},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=7,DVar(useSites={148},value=an int,origin=1),GetField(pc=7,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=13,DVar(useSites={3},value={_ <: java.util.List, null}[↦13;refId=103],origin=2),GetField(pc=13,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	3: Assignment(pc=16,DVar(useSites={162,158,115,111},value=an int,origin=3),VirtualFunctionCall(pc=16,java.util.List,isInterface=true,int size(),UVar(defSites={2},value={_ <: java.util.List, null}[↦13;refId=103]),())),
	4: Assignment(pc=24,DVar(useSites={5},value=null[↦24],origin=4),NullExpr(pc=24)),
	5: PutField(pc=25,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={4},value=null[↦24])),
	6: Assignment(pc=29,DVar(useSites={8},value=an int,origin=6),VirtualFunctionCall(pc=29,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	7: Assignment(pc=36,DVar(useSites={8},value=int = 63,origin=7),IntConst(pc=36,63)),
	8: If(pc=38,UVar(defSites={6},value=an int),!=,UVar(defSites={7},value=int = 63),target=139),
	9: Assignment(pc=42,DVar(useSites={10},value=an int,origin=9),VirtualFunctionCall(pc=42,java.util.regex.Pattern,isInterface=false,int skip(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	10: Switch(pc=49,defaultTarget=121,index=UVar(defSites={9},value=an int),npairs=(IntIntPair(33,17),IntIntPair(36,118),IntIntPair(58,11),IntIntPair(60,35),IntIntPair(61,17),IntIntPair(62,26),IntIntPair(64,118)),
	11: Assignment(pc=117,DVar(useSites={12},value=int = 1,origin=11),IntConst(pc=117,1)),
	12: Assignment(pc=118,DVar(useSites={242,150,214,153,185,149,181,203,199,215,15},value={_ <: java.util.regex.Pattern$Node, null}[↦118;refId=181],origin=12),VirtualFunctionCall(pc=118,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node createGroup(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={11},value=int = 1)))),
	13: Assignment(pc=123,DVar(useSites={208,210,14,174,209,201,153,243,151,207,175},value={_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182],origin=13),GetField(pc=123,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	14: Assignment(pc=130,DVar(useSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦130;refId=184],origin=14),VirtualFunctionCall(pc=130,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182])))),
	15: PutField(pc=133,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node, null}[↦118;refId=181]),UVar(defSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦130;refId=184])),
	16: Goto(pc=136,target=145),
	17: Assignment(pc=140,DVar(useSites={18},value=int = 1,origin=17),IntConst(pc=140,1)),
	18: Assignment(pc=141,DVar(useSites={24,21},value={_ <: java.util.regex.Pattern$Node, null}[↦141;refId=193],origin=18),VirtualFunctionCall(pc=141,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node createGroup(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={17},value=int = 1)))),
	19: Assignment(pc=146,DVar(useSites={20},value={_ <: java.util.regex.Pattern$Node, null}[↦146;refId=194],origin=19),GetField(pc=146,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	20: Assignment(pc=153,DVar(useSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦153;refId=196],origin=20),VirtualFunctionCall(pc=153,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={19},value={_ <: java.util.regex.Pattern$Node, null}[↦146;refId=194])))),
	21: PutField(pc=156,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={18},value={_ <: java.util.regex.Pattern$Node, null}[↦141;refId=193]),UVar(defSites={20},value={_ <: java.util.regex.Pattern$Node, null}[↦153;refId=196])),
	22: Nop(pc=161),
	23: Assignment(pc=166,DVar(useSites={208,24,210,242,150,214,174,209,201,153,185,149,181,243,203,199,151,215,207,175},value=java.util.regex.Pattern$Pos[↦166;refId=198],origin=23),New(pc=166,java.util.regex.Pattern$Pos)),
	24: NonVirtualMethodCall(pc=171,java.util.regex.Pattern$Pos,isInterface=false,void <init>(java.util.regex.Pattern$Node),UVar(defSites={23},value=java.util.regex.Pattern$Pos[↦166;refId=198]),(UVar(defSites={18},value=_ <: java.util.regex.Pattern$Node[↦141;refId=193]))),
	25: Goto(pc=177,target=145),
	26: Assignment(pc=195,DVar(useSites={27},value=int = 1,origin=26),IntConst(pc=195,1)),
	27: Assignment(pc=196,DVar(useSites={30,33},value={_ <: java.util.regex.Pattern$Node, null}[↦196;refId=130],origin=27),VirtualFunctionCall(pc=196,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node createGroup(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={26},value=int = 1)))),
	28: Assignment(pc=201,DVar(useSites={29},value={_ <: java.util.regex.Pattern$Node, null}[↦201;refId=131],origin=28),GetField(pc=201,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	29: Assignment(pc=208,DVar(useSites={30},value={_ <: java.util.regex.Pattern$Node, null}[↦208;refId=133],origin=29),VirtualFunctionCall(pc=208,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦201;refId=131])))),
	30: PutField(pc=211,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦196;refId=130]),UVar(defSites={29},value={_ <: java.util.regex.Pattern$Node, null}[↦208;refId=133])),
	31: Assignment(pc=214,DVar(useSites={208,210,242,150,214,174,33,209,201,153,185,149,181,243,203,199,151,215,207,175},value=java.util.regex.Pattern$Ques[↦214;refId=135],origin=31),New(pc=214,java.util.regex.Pattern$Ques)),
	32: Assignment(pc=219,DVar(useSites={33},value={java.util.regex.Pattern$Qtype, null}[↦219;refId=136],origin=32),GetStatic(pc=219,java.util.regex.Pattern$Qtype,INDEPENDENT,java.util.regex.Pattern$Qtype)),
	33: NonVirtualMethodCall(pc=222,java.util.regex.Pattern$Ques,isInterface=false,void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Qtype),UVar(defSites={31},value=java.util.regex.Pattern$Ques[↦214;refId=135]),(UVar(defSites={27},value=_ <: java.util.regex.Pattern$Node[↦196;refId=130]),UVar(defSites={32},value={java.util.regex.Pattern$Qtype, null}[↦219;refId=136]))),
	34: Goto(pc=228,target=145),
	35: Assignment(pc=232,DVar(useSites={40,86,37,39},value=an int,origin=35),VirtualFunctionCall(pc=232,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	36: Assignment(pc=239,DVar(useSites={37},value=int = 61,origin=36),IntConst(pc=239,61)),
	37: If(pc=241,UVar(defSites={35},value=an int),==,UVar(defSites={36},value=int = 61),target=67),
	38: Assignment(pc=246,DVar(useSites={39},value=int = 33,origin=38),IntConst(pc=246,33)),
	39: If(pc=248,UVar(defSites={35},value=an int),==,UVar(defSites={38},value=int = 33),target=67),
	40: Assignment(pc=254,DVar(useSites={48,42,63},value={java.lang.String, null}[↦254;refId=142],origin=40),VirtualFunctionCall(pc=254,java.util.regex.Pattern,isInterface=false,java.lang.String groupname(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={35},value=an int)))),
	41: Assignment(pc=260,DVar(useSites={42},value={_ <: java.util.Map, null}[↦260;refId=144],origin=41),VirtualFunctionCall(pc=260,java.util.regex.Pattern,isInterface=false,java.util.Map namedGroups(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	42: Assignment(pc=265,DVar(useSites={43},value=int ∈ [0,1],origin=42),VirtualFunctionCall(pc=265,java.util.Map,isInterface=true,boolean containsKey(java.lang.Object),UVar(defSites={41},value={_ <: java.util.Map, null}[↦260;refId=144]),(UVar(defSites={40},value={java.lang.String, null}[↦254;refId=142])))),
	43: If(pc=270,UVar(defSites={42},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=54),
	44: Assignment(pc=274,DVar(useSites={45,47},value=java.lang.StringBuilder[↦274;refId=147],origin=44),New(pc=274,java.lang.StringBuilder)),
	45: NonVirtualMethodCall(pc=278,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={44},value=java.lang.StringBuilder[↦274;refId=147]),()),
	46: Assignment(pc=281,DVar(useSites={47},value=String("Named capturing group <")[@281;refId=149],origin=46),StringConst(pc=281,Named capturing group <)),
	47: Assignment(pc=284,DVar(useSites={48},value={java.lang.StringBuilder, null}[↦284;refId=151],origin=47),VirtualFunctionCall(pc=284,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={44},value=java.lang.StringBuilder[↦274;refId=147]),(UVar(defSites={46},value=String("Named capturing group <")[@281;refId=149])))),
	48: Assignment(pc=289,DVar(useSites={50},value={java.lang.StringBuilder, null}[↦289;refId=154],origin=48),VirtualFunctionCall(pc=289,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={47},value={java.lang.StringBuilder, null}[↦284;refId=151]),(UVar(defSites={40},value={java.lang.String, null}[↦254;refId=142])))),
	49: Assignment(pc=292,DVar(useSites={50},value=String("> is already defined")[@292;refId=155],origin=49),StringConst(pc=292,> is already defined)),
	50: Assignment(pc=295,DVar(useSites={51},value={java.lang.StringBuilder, null}[↦295;refId=158],origin=50),VirtualFunctionCall(pc=295,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={48},value={java.lang.StringBuilder, null}[↦289;refId=154]),(UVar(defSites={49},value=String("> is already defined")[@292;refId=155])))),
	51: Assignment(pc=298,DVar(useSites={52},value={java.lang.String, null}[↦298;refId=161],origin=51),VirtualFunctionCall(pc=298,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={50},value={java.lang.StringBuilder, null}[↦295;refId=158]),())),
	52: Assignment(pc=301,DVar(useSites={53},value={_ <: java.util.regex.PatternSyntaxException, null}[↦301;refId=163],origin=52),VirtualFunctionCall(pc=301,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={51},value={java.lang.String, null}[↦298;refId=161])))),
	53: Throw(pc=304,UVar(defSites={52},value={_ <: java.util.regex.PatternSyntaxException, null}[↦301;refId=163])),
	54: Assignment(pc=305,DVar(useSites={211},value=int = 1,origin=54),IntConst(pc=305,1)),
	55: Assignment(pc=308,DVar(useSites={56},value=int = 0,origin=55),IntConst(pc=308,0)),
	56: Assignment(pc=309,DVar(useSites={242,150,214,65,153,185,149,181,203,199,215},value={_ <: java.util.regex.Pattern$Node, null}[↦309;refId=166],origin=56),VirtualFunctionCall(pc=309,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node createGroup(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={55},value=int = 0)))),
	57: Assignment(pc=314,DVar(useSites={64,208,210,174,209,201,153,243,151,207,175},value={_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167],origin=57),GetField(pc=314,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	58: Assignment(pc=319,DVar(useSites={63},value={_ <: java.util.Map, null}[↦319;refId=169],origin=58),VirtualFunctionCall(pc=319,java.util.regex.Pattern,isInterface=false,java.util.Map namedGroups(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	59: Assignment(pc=325,DVar(useSites={61},value=an int,origin=59),GetField(pc=325,java.util.regex.Pattern,capturingGroupCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	60: Assignment(pc=328,DVar(useSites={61},value=int = 1,origin=60),IntConst(pc=328,1)),
	61: Assignment(pc=329,DVar(useSites={62},value=an int,origin=61),BinaryExpr(pc=329,ComputationalTypeInt,UVar(defSites={59},value=an int),-,UVar(defSites={60},value=int = 1))),
	62: Assignment(pc=330,DVar(useSites={63},value={java.lang.Integer, null}[↦330;refId=171],origin=62),StaticFunctionCall(pc=330,java.lang.Integer,isInterface=false,java.lang.Integer valueOf(int),(UVar(defSites={61},value=an int)))),
	63: ExprStmt(pc=333,VirtualFunctionCall(pc=333,java.util.Map,isInterface=true,java.lang.Object put(java.lang.Object,java.lang.Object),UVar(defSites={58},value={_ <: java.util.Map, null}[↦319;refId=169]),(UVar(defSites={40},value={java.lang.String, null}[↦254;refId=142]),UVar(defSites={62},value={java.lang.Integer, null}[↦330;refId=171])))),
	64: Assignment(pc=342,DVar(useSites={65},value={_ <: java.util.regex.Pattern$Node, null}[↦342;refId=176],origin=64),VirtualFunctionCall(pc=342,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={57},value={_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167])))),
	65: PutField(pc=345,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={56},value={_ <: java.util.regex.Pattern$Node, null}[↦309;refId=166]),UVar(defSites={64},value={_ <: java.util.regex.Pattern$Node, null}[↦342;refId=176])),
	66: Goto(pc=348,target=145),
	67: Assignment(pc=352,DVar(useSites={84},value=an int,origin=67),GetField(pc=352,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	68: Assignment(pc=358,DVar(useSites={69},value=int = 1,origin=68),IntConst(pc=358,1)),
	69: Assignment(pc=359,DVar(useSites={96,72,102,77,107,91},value={_ <: java.util.regex.Pattern$Node, null}[↦359;refId=219],origin=69),VirtualFunctionCall(pc=359,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node createGroup(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={68},value=int = 1)))),
	70: Assignment(pc=364,DVar(useSites={74,71},value={_ <: java.util.regex.Pattern$Node, null}[↦364;refId=220],origin=70),GetField(pc=364,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	71: Assignment(pc=371,DVar(useSites={72},value={_ <: java.util.regex.Pattern$Node, null}[↦371;refId=222],origin=71),VirtualFunctionCall(pc=371,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={70},value={_ <: java.util.regex.Pattern$Node, null}[↦364;refId=220])))),
	72: PutField(pc=374,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={69},value={_ <: java.util.regex.Pattern$Node, null}[↦359;refId=219]),UVar(defSites={71},value={_ <: java.util.regex.Pattern$Node, null}[↦371;refId=222])),
	73: Assignment(pc=378,DVar(useSites={74},value={_ <: java.util.regex.Pattern$Node, null}[↦378;refId=224],origin=73),GetStatic(pc=378,java.util.regex.Pattern,lookbehindEnd,java.util.regex.Pattern$Node)),
	74: PutField(pc=381,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={70},value={_ <: java.util.regex.Pattern$Node, null}[↦364;refId=220]),UVar(defSites={73},value={_ <: java.util.regex.Pattern$Node, null}[↦378;refId=224])),
	75: Assignment(pc=384,DVar(useSites={100,76,106,90,78,94,105,89,101,77,95},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226],origin=75),New(pc=384,java.util.regex.Pattern$TreeInfo)),
	76: NonVirtualMethodCall(pc=388,java.util.regex.Pattern$TreeInfo,isInterface=false,void <init>(),UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]),()),
	77: ExprStmt(pc=396,VirtualFunctionCall(pc=396,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={69},value=_ <: java.util.regex.Pattern$Node[↦359;refId=219]),(UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226])))),
	78: Assignment(pc=402,DVar(useSites={79},value=int ∈ [0,1],origin=78),GetField(pc=402,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	79: If(pc=405,UVar(defSites={78},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=83),
	80: Assignment(pc=409,DVar(useSites={81},value=String("Look-behind group does not have an obvious maximum length")[@409;refId=229],origin=80),StringConst(pc=409,Look-behind group does not have an obvious maximum length)),
	81: Assignment(pc=412,DVar(useSites={82},value={_ <: java.util.regex.PatternSyntaxException, null}[↦412;refId=231],origin=81),VirtualFunctionCall(pc=412,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={80},value=String("Look-behind group does not have an obvious maximum length")[@409;refId=229])))),
	82: Throw(pc=415,UVar(defSites={81},value={_ <: java.util.regex.PatternSyntaxException, null}[↦412;refId=231])),
	83: Assignment(pc=420,DVar(useSites={84},value=an int,origin=83),GetField(pc=420,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	84: Assignment(pc=423,DVar(useSites={98,87},value=int ∈ [0,1],origin=84),VirtualFunctionCall(pc=423,java.util.regex.Pattern,isInterface=false,boolean findSupplementary(int,int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={67},value=an int),UVar(defSites={83},value=an int)))),
	85: Assignment(pc=430,DVar(useSites={86},value=int = 61,origin=85),IntConst(pc=430,61)),
	86: If(pc=432,UVar(defSites={35},value=int ∈ [33,61]),!=,UVar(defSites={85},value=int = 61),target=98),
	87: If(pc=437,UVar(defSites={84},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=93),
	88: Assignment(pc=440,DVar(useSites={208,210,242,150,214,174,209,201,153,185,149,181,243,203,91,199,151,215,207,175},value=java.util.regex.Pattern$BehindS[↦440;refId=239],origin=88),New(pc=440,java.util.regex.Pattern$BehindS)),
	89: Assignment(pc=447,DVar(useSites={91},value=an int,origin=89),GetField(pc=447,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	90: Assignment(pc=452,DVar(useSites={91},value=an int,origin=90),GetField(pc=452,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	91: NonVirtualMethodCall(pc=455,java.util.regex.Pattern$BehindS,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int),UVar(defSites={88},value=java.util.regex.Pattern$BehindS[↦440;refId=239]),(UVar(defSites={69},value=_ <: java.util.regex.Pattern$Node[↦359;refId=219]),UVar(defSites={89},value=an int),UVar(defSites={90},value=an int))),
	92: Goto(pc=458,target=97),
	93: Assignment(pc=461,DVar(useSites={96,208,210,242,150,214,174,209,201,153,185,149,181,243,203,199,151,215,207,175},value=java.util.regex.Pattern$Behind[↦461;refId=241],origin=93),New(pc=461,java.util.regex.Pattern$Behind)),
	94: Assignment(pc=468,DVar(useSites={96},value=an int,origin=94),GetField(pc=468,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	95: Assignment(pc=473,DVar(useSites={96},value=an int,origin=95),GetField(pc=473,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	96: NonVirtualMethodCall(pc=476,java.util.regex.Pattern$Behind,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int),UVar(defSites={93},value=java.util.regex.Pattern$Behind[↦461;refId=241]),(UVar(defSites={69},value=_ <: java.util.regex.Pattern$Node[↦359;refId=219]),UVar(defSites={94},value=an int),UVar(defSites={95},value=an int))),
	97: Goto(pc=482,target=109),
	98: If(pc=487,UVar(defSites={84},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=104),
	99: Assignment(pc=490,DVar(useSites={208,210,242,102,150,214,174,209,201,153,185,149,181,243,203,199,151,215,207,175},value=java.util.regex.Pattern$NotBehindS[↦490;refId=234],origin=99),New(pc=490,java.util.regex.Pattern$NotBehindS)),
	100: Assignment(pc=497,DVar(useSites={102},value=an int,origin=100),GetField(pc=497,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	101: Assignment(pc=502,DVar(useSites={102},value=an int,origin=101),GetField(pc=502,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	102: NonVirtualMethodCall(pc=505,java.util.regex.Pattern$NotBehindS,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int),UVar(defSites={99},value=java.util.regex.Pattern$NotBehindS[↦490;refId=234]),(UVar(defSites={69},value=_ <: java.util.regex.Pattern$Node[↦359;refId=219]),UVar(defSites={100},value=an int),UVar(defSites={101},value=an int))),
	103: Goto(pc=508,target=108),
	104: Assignment(pc=511,DVar(useSites={208,210,242,150,214,174,209,201,153,185,149,181,243,203,107,199,151,215,207,175},value=java.util.regex.Pattern$NotBehind[↦511;refId=236],origin=104),New(pc=511,java.util.regex.Pattern$NotBehind)),
	105: Assignment(pc=518,DVar(useSites={107},value=an int,origin=105),GetField(pc=518,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	106: Assignment(pc=523,DVar(useSites={107},value=an int,origin=106),GetField(pc=523,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={75},value=java.util.regex.Pattern$TreeInfo[↦384;refId=226]))),
	107: NonVirtualMethodCall(pc=526,java.util.regex.Pattern$NotBehind,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int),UVar(defSites={104},value=java.util.regex.Pattern$NotBehind[↦511;refId=236]),(UVar(defSites={69},value=_ <: java.util.regex.Pattern$Node[↦359;refId=219]),UVar(defSites={105},value=an int),UVar(defSites={106},value=an int))),
	108: Nop(pc=529),
	109: Assignment(pc=535,DVar(useSites={110},value={_ <: java.util.List, null}[↦535;refId=295],origin=109),GetField(pc=535,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	110: Assignment(pc=538,DVar(useSites={111},value=an int,origin=110),VirtualFunctionCall(pc=538,java.util.List,isInterface=true,int size(),UVar(defSites={109},value={_ <: java.util.List, null}[↦535;refId=295]),())),
	111: If(pc=543,UVar(defSites={3},value=an int),>=,UVar(defSites={110},value=an int),target=145),
	112: Assignment(pc=547,DVar(useSites={115},value={_ <: java.util.List, null}[↦547;refId=300],origin=112),GetField(pc=547,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	113: Assignment(pc=553,DVar(useSites={114},value={_ <: java.util.List, null}[↦553;refId=301],origin=113),GetField(pc=553,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	114: Assignment(pc=556,DVar(useSites={115},value=an int,origin=114),VirtualFunctionCall(pc=556,java.util.List,isInterface=true,int size(),UVar(defSites={113},value={_ <: java.util.List, null}[↦553;refId=301]),())),
	115: Assignment(pc=561,DVar(useSites={116},value={_ <: java.util.List, null}[↦561;refId=306],origin=115),VirtualFunctionCall(pc=561,java.util.List,isInterface=true,java.util.List subList(int,int),UVar(defSites={112},value={_ <: java.util.List, null}[↦547;refId=300]),(UVar(defSites={3},value=int ∈ [-2147483648,2147483646]),UVar(defSites={114},value=an int)))),
	116: VirtualMethodCall(pc=566,java.util.List,isInterface=true,void clear(),UVar(defSites={115},value={_ <: java.util.List, null}[↦561;refId=306]),()),
	117: Goto(pc=571,target=145),
	118: Assignment(pc=575,DVar(useSites={119},value=String("Unknown group type")[@575;refId=188],origin=118),StringConst(pc=575,Unknown group type)),
	119: Assignment(pc=578,DVar(useSites={120},value={_ <: java.util.regex.PatternSyntaxException, null}[↦578;refId=190],origin=119),VirtualFunctionCall(pc=578,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={118},value=String("Unknown group type")[@575;refId=188])))),
	120: Throw(pc=581,UVar(defSites={119},value={_ <: java.util.regex.PatternSyntaxException, null}[↦578;refId=190])),
	121: VirtualMethodCall(pc=583,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	122: VirtualMethodCall(pc=587,java.util.regex.Pattern,isInterface=false,void addFlag(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	123: Assignment(pc=591,DVar(useSites={129,125},value=an int,origin=123),VirtualFunctionCall(pc=591,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	124: Assignment(pc=598,DVar(useSites={125},value=int = 41,origin=124),IntConst(pc=598,41)),
	125: If(pc=600,UVar(defSites={123},value=an int),!=,UVar(defSites={124},value=int = 41),target=128),
	126: Assignment(pc=603,DVar(useSites={127},value=null[↦603],origin=126),NullExpr(pc=603)),
	127: ReturnValue(pc=604,UVar(defSites={126},value=null[↦603])),
	128: Assignment(pc=607,DVar(useSites={129},value=int = 58,origin=128),IntConst(pc=607,58)),
	129: If(pc=609,UVar(defSites={123},value=an int),==,UVar(defSites={128},value=int = 58),target=133),
	130: Assignment(pc=613,DVar(useSites={131},value=String("Unknown inline modifier")[@613;refId=125],origin=130),StringConst(pc=613,Unknown inline modifier)),
	131: Assignment(pc=616,DVar(useSites={132},value={_ <: java.util.regex.PatternSyntaxException, null}[↦616;refId=127],origin=131),VirtualFunctionCall(pc=616,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={130},value=String("Unknown inline modifier")[@613;refId=125])))),
	132: Throw(pc=619,UVar(defSites={131},value={_ <: java.util.regex.PatternSyntaxException, null}[↦616;refId=127])),
	133: Assignment(pc=621,DVar(useSites={134},value=int = 1,origin=133),IntConst(pc=621,1)),
	134: Assignment(pc=622,DVar(useSites={242,150,214,137,153,185,149,181,203,199,215},value={_ <: java.util.regex.Pattern$Node, null}[↦622;refId=118],origin=134),VirtualFunctionCall(pc=622,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node createGroup(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={133},value=int = 1)))),
	135: Assignment(pc=627,DVar(useSites={208,136,210,174,209,201,153,243,151,207,175},value={_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119],origin=135),GetField(pc=627,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	136: Assignment(pc=634,DVar(useSites={137},value={_ <: java.util.regex.Pattern$Node, null}[↦634;refId=121],origin=136),VirtualFunctionCall(pc=634,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={135},value={_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119])))),
	137: PutField(pc=637,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={134},value={_ <: java.util.regex.Pattern$Node, null}[↦622;refId=118]),UVar(defSites={136},value={_ <: java.util.regex.Pattern$Node, null}[↦634;refId=121])),
	138: Goto(pc=640,target=145),
	139: Assignment(pc=643,DVar(useSites={211},value=int = 1,origin=139),IntConst(pc=643,1)),
	140: Assignment(pc=646,DVar(useSites={141},value=int = 0,origin=140),IntConst(pc=646,0)),
	141: Assignment(pc=647,DVar(useSites={144,242,150,214,153,185,149,181,203,199,215},value={_ <: java.util.regex.Pattern$Node, null}[↦647;refId=108],origin=141),VirtualFunctionCall(pc=647,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node createGroup(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={140},value=int = 0)))),
	142: Assignment(pc=652,DVar(useSites={208,210,174,209,201,153,243,151,143,207,175},value={_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109],origin=142),GetField(pc=652,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	143: Assignment(pc=659,DVar(useSites={144},value={_ <: java.util.regex.Pattern$Node, null}[↦659;refId=111],origin=143),VirtualFunctionCall(pc=659,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={142},value={_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109])))),
	144: PutField(pc=662,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={141},value={_ <: java.util.regex.Pattern$Node, null}[↦647;refId=108]),UVar(defSites={143},value={_ <: java.util.regex.Pattern$Node, null}[↦659;refId=111])),
	145: Assignment(pc=666,DVar(useSites={147},value=int = 41,origin=145),IntConst(pc=666,41)),
	146: Assignment(pc=668,DVar(useSites={147},value=String("Unclosed group")[@668;refId=311],origin=146),StringConst(pc=668,Unclosed group)),
	147: VirtualMethodCall(pc=671,java.util.regex.Pattern,isInterface=false,void accept(int,java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={145},value=int = 41),UVar(defSites={146},value=String("Unclosed group")[@668;refId=311]))),
	148: PutField(pc=677,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={1},value=an int)),
	149: Assignment(pc=682,DVar(useSites={192,176,240,152,216,196,164,204,170,154,166,150,206,238,222,205,189,195,171,155,167,191},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314],origin=149),VirtualFunctionCall(pc=682,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node closure(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=298; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»])))),
	150: If(pc=690,UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314]),!=,UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=298; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),target=153),
	151: PutField(pc=695,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={104,88,142,57,13,93,99,135,23,31},value={_ <: java.util.regex.Pattern$Node, null}[refId=299; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], java.util.regex.Pattern$Ques[↦214;refId=135], java.util.regex.Pattern$BehindS[↦440;refId=239], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], java.util.regex.Pattern$Behind[↦461;refId=241], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182], java.util.regex.Pattern$NotBehind[↦511;refId=236]»])),
	152: ReturnValue(pc=700,UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314])),
	153: If(pc=703,UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=298; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),!=,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value={_ <: java.util.regex.Pattern$Node, null}[refId=299; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], java.util.regex.Pattern$Ques[↦214;refId=135], java.util.regex.Pattern$BehindS[↦440;refId=239], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], java.util.regex.Pattern$Behind[↦461;refId=241], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),target=156),
	154: PutField(pc=709,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314])),
	155: ReturnValue(pc=714,UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314])),
	156: Assignment(pc=718,DVar(useSites={157},value={_ <: java.util.List, null}[↦718;refId=315],origin=156),GetField(pc=718,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	157: Assignment(pc=721,DVar(useSites={158},value=an int,origin=157),VirtualFunctionCall(pc=721,java.util.List,isInterface=true,int size(),UVar(defSites={156},value={_ <: java.util.List, null}[↦718;refId=315]),())),
	158: If(pc=726,UVar(defSites={3},value=an int),>=,UVar(defSites={157},value=an int),target=164),
	159: Assignment(pc=730,DVar(useSites={162},value={_ <: java.util.List, null}[↦730;refId=320],origin=159),GetField(pc=730,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	160: Assignment(pc=736,DVar(useSites={161},value={_ <: java.util.List, null}[↦736;refId=321],origin=160),GetField(pc=736,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	161: Assignment(pc=739,DVar(useSites={162},value=an int,origin=161),VirtualFunctionCall(pc=739,java.util.List,isInterface=true,int size(),UVar(defSites={160},value={_ <: java.util.List, null}[↦736;refId=321]),())),
	162: Assignment(pc=744,DVar(useSites={163},value={_ <: java.util.List, null}[↦744;refId=326],origin=162),VirtualFunctionCall(pc=744,java.util.List,isInterface=true,java.util.List subList(int,int),UVar(defSites={159},value={_ <: java.util.List, null}[↦730;refId=320]),(UVar(defSites={3},value=int ∈ [-2147483648,2147483646]),UVar(defSites={161},value=an int)))),
	163: VirtualMethodCall(pc=749,java.util.List,isInterface=true,void clear(),UVar(defSites={162},value={_ <: java.util.List, null}[↦744;refId=326]),()),
	164: Assignment(pc=756,DVar(useSites={165},value=int ∈ [0,1],origin=164),InstanceOf(pc=756,UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314]),java.util.regex.Pattern$Ques)),
	165: If(pc=759,UVar(defSites={164},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=189),
	166: Checkcast(pc=764,UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314]),java.util.regex.Pattern$Ques),
	167: Assignment(pc=771,DVar(useSites={169},value={java.util.regex.Pattern$Qtype, null}[↦771;refId=333],origin=167),GetField(pc=771,java.util.regex.Pattern$Ques,type,java.util.regex.Pattern$Qtype,UVar(defSites={149},value={java.util.regex.Pattern$Ques, null}[↦682;refId=331]))),
	168: Assignment(pc=774,DVar(useSites={169},value={java.util.regex.Pattern$Qtype, null}[↦774;refId=335],origin=168),GetStatic(pc=774,java.util.regex.Pattern$Qtype,POSSESSIVE,java.util.regex.Pattern$Qtype)),
	169: If(pc=777,UVar(defSites={167},value={java.util.regex.Pattern$Qtype, null}[↦771;refId=333]),!=,UVar(defSites={168},value={java.util.regex.Pattern$Qtype, null}[↦774;refId=335]),target=172),
	170: PutField(pc=783,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={149},value=java.util.regex.Pattern$Ques[↦682;refId=331])),
	171: ReturnValue(pc=788,UVar(defSites={149},value=java.util.regex.Pattern$Ques[↦682;refId=331])),
	172: Assignment(pc=790,DVar(useSites={174,173},value=java.util.regex.Pattern$BranchConn[↦790;refId=336],origin=172),New(pc=790,java.util.regex.Pattern$BranchConn)),
	173: NonVirtualMethodCall(pc=794,java.util.regex.Pattern$BranchConn,isInterface=false,void <init>(),UVar(defSites={172},value=java.util.regex.Pattern$BranchConn[↦790;refId=336]),()),
	174: PutField(pc=797,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value={_ <: java.util.regex.Pattern$Node, null}[refId=319; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], java.util.regex.Pattern$Ques[↦214;refId=135], java.util.regex.Pattern$BehindS[↦440;refId=239], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], java.util.regex.Pattern$Behind[↦461;refId=241], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),UVar(defSites={172},value=java.util.regex.Pattern$BranchConn[↦790;refId=336])),
	175: Assignment(pc=801,DVar(useSites={185,181,187},value={_ <: java.util.regex.Pattern$Node, null}[↦801;refId=339],origin=175),GetField(pc=801,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value=_ <: java.util.regex.Pattern$Node[refId=319; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], java.util.regex.Pattern$Ques[↦214;refId=135], java.util.regex.Pattern$BehindS[↦440;refId=239], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], java.util.regex.Pattern$Behind[↦461;refId=241], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]))),
	176: Assignment(pc=807,DVar(useSites={178},value={java.util.regex.Pattern$Qtype, null}[↦807;refId=340],origin=176),GetField(pc=807,java.util.regex.Pattern$Ques,type,java.util.regex.Pattern$Qtype,UVar(defSites={149},value=java.util.regex.Pattern$Ques[↦682;refId=331]))),
	177: Assignment(pc=810,DVar(useSites={178},value={java.util.regex.Pattern$Qtype, null}[↦810;refId=341],origin=177),GetStatic(pc=810,java.util.regex.Pattern$Qtype,GREEDY,java.util.regex.Pattern$Qtype)),
	178: If(pc=813,UVar(defSites={176},value={java.util.regex.Pattern$Qtype, null}[↦807;refId=340]),!=,UVar(defSites={177},value={java.util.regex.Pattern$Qtype, null}[↦810;refId=341]),target=183),
	179: Assignment(pc=816,DVar(useSites={188,181},value=java.util.regex.Pattern$Branch[↦816;refId=345],origin=179),New(pc=816,java.util.regex.Pattern$Branch)),
	180: Assignment(pc=821,DVar(useSites={181},value=null[↦821],origin=180),NullExpr(pc=821)),
	181: NonVirtualMethodCall(pc=823,java.util.regex.Pattern$Branch,isInterface=false,void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Node,java.util.regex.Pattern$Node),UVar(defSites={179},value=java.util.regex.Pattern$Branch[↦816;refId=345]),(UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=318; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),UVar(defSites={180},value=null[↦821]),UVar(defSites={175},value={_ <: java.util.regex.Pattern$Node, null}[↦801;refId=339]))),
	182: Goto(pc=827,target=187),
	183: Assignment(pc=830,DVar(useSites={188,185},value=java.util.regex.Pattern$Branch[↦830;refId=342],origin=183),New(pc=830,java.util.regex.Pattern$Branch)),
	184: Assignment(pc=834,DVar(useSites={185},value=null[↦834],origin=184),NullExpr(pc=834)),
	185: NonVirtualMethodCall(pc=837,java.util.regex.Pattern$Branch,isInterface=false,void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Node,java.util.regex.Pattern$Node),UVar(defSites={183},value=java.util.regex.Pattern$Branch[↦830;refId=342]),(UVar(defSites={184},value=null[↦834]),UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=318; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),UVar(defSites={175},value={_ <: java.util.regex.Pattern$Node, null}[↦801;refId=339]))),
	186: Nop(pc=840),
	187: PutField(pc=843,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={175},value={_ <: java.util.regex.Pattern$Node, null}[↦801;refId=252])),
	188: ReturnValue(pc=847,UVar(defSites={179,183},value=java.util.regex.Pattern$Branch[refId=259; values=«java.util.regex.Pattern$Branch[↦830;refId=255], java.util.regex.Pattern$Branch[↦816;refId=257]»])),
	189: Assignment(pc=850,DVar(useSites={190},value=int ∈ [0,1],origin=189),InstanceOf(pc=850,UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314]),java.util.regex.Pattern$Curly)),
	190: If(pc=853,UVar(defSites={189},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=246),
	191: Checkcast(pc=858,UVar(defSites={149},value={_ <: java.util.regex.Pattern$Node, null}[↦682;refId=314]),java.util.regex.Pattern$Curly),
	192: Assignment(pc=865,DVar(useSites={194},value={java.util.regex.Pattern$Qtype, null}[↦865;refId=350],origin=192),GetField(pc=865,java.util.regex.Pattern$Curly,type,java.util.regex.Pattern$Qtype,UVar(defSites={149},value={java.util.regex.Pattern$Curly, null}[↦682;refId=348]))),
	193: Assignment(pc=868,DVar(useSites={194},value={java.util.regex.Pattern$Qtype, null}[↦868;refId=352],origin=193),GetStatic(pc=868,java.util.regex.Pattern$Qtype,POSSESSIVE,java.util.regex.Pattern$Qtype)),
	194: If(pc=871,UVar(defSites={192},value={java.util.regex.Pattern$Qtype, null}[↦865;refId=350]),!=,UVar(defSites={193},value={java.util.regex.Pattern$Qtype, null}[↦868;refId=352]),target=197),
	195: PutField(pc=877,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348])),
	196: ReturnValue(pc=882,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348])),
	197: Assignment(pc=883,DVar(useSites={198,199},value=java.util.regex.Pattern$TreeInfo[↦883;refId=353],origin=197),New(pc=883,java.util.regex.Pattern$TreeInfo)),
	198: NonVirtualMethodCall(pc=887,java.util.regex.Pattern$TreeInfo,isInterface=false,void <init>(),UVar(defSites={197},value=java.util.regex.Pattern$TreeInfo[↦883;refId=353]),()),
	199: Assignment(pc=895,DVar(useSites={200},value=int ∈ [0,1],origin=199),VirtualFunctionCall(pc=895,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=318; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),(UVar(defSites={197},value=java.util.regex.Pattern$TreeInfo[↦883;refId=353])))),
	200: If(pc=898,UVar(defSites={199},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=214),
	201: Checkcast(pc=902,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value={_ <: java.util.regex.Pattern$Node, null}[refId=319; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], java.util.regex.Pattern$Ques[↦214;refId=135], java.util.regex.Pattern$BehindS[↦440;refId=239], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], java.util.regex.Pattern$Behind[↦461;refId=241], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),java.util.regex.Pattern$GroupTail),
	202: Assignment(pc=908,DVar(useSites={212,213,211},value=java.util.regex.Pattern$GroupCurly[↦908;refId=358],origin=202),New(pc=908,java.util.regex.Pattern$GroupCurly)),
	203: Assignment(pc=913,DVar(useSites={211},value={_ <: java.util.regex.Pattern$Node, null}[↦913;refId=359],origin=203),GetField(pc=913,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=318; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]))),
	204: Assignment(pc=918,DVar(useSites={211},value=an int,origin=204),GetField(pc=918,java.util.regex.Pattern$Curly,cmin,int,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348]))),
	205: Assignment(pc=923,DVar(useSites={211},value=an int,origin=205),GetField(pc=923,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348]))),
	206: Assignment(pc=928,DVar(useSites={211},value={java.util.regex.Pattern$Qtype, null}[↦928;refId=360],origin=206),GetField(pc=928,java.util.regex.Pattern$Curly,type,java.util.regex.Pattern$Qtype,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348]))),
	207: Checkcast(pc=932,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value={java.util.regex.Pattern$GroupTail, null}[refId=356; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182]»]),java.util.regex.Pattern$GroupTail),
	208: Assignment(pc=935,DVar(useSites={211},value=an int,origin=208),GetField(pc=935,java.util.regex.Pattern$GroupTail,localIndex,int,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value={java.util.regex.Pattern$GroupTail, null}[refId=356; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182]»]))),
	209: Checkcast(pc=939,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value=java.util.regex.Pattern$GroupTail[refId=356; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182]»]),java.util.regex.Pattern$GroupTail),
	210: Assignment(pc=942,DVar(useSites={211},value=an int,origin=210),GetField(pc=942,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value=java.util.regex.Pattern$GroupTail[refId=356; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182]»]))),
	211: NonVirtualMethodCall(pc=946,java.util.regex.Pattern$GroupCurly,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype,int,int,boolean),UVar(defSites={202},value=java.util.regex.Pattern$GroupCurly[↦908;refId=358]),(UVar(defSites={203},value={_ <: java.util.regex.Pattern$Node, null}[↦913;refId=359]),UVar(defSites={204},value=an int),UVar(defSites={205},value=an int),UVar(defSites={206},value={java.util.regex.Pattern$Qtype, null}[↦928;refId=360]),UVar(defSites={208},value=an int),UVar(defSites={210},value=an int),UVar(defSites={0,54,139},value=int ∈ [0,1]))),
	212: PutField(pc=950,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={202},value=java.util.regex.Pattern$GroupCurly[↦908;refId=358])),
	213: ReturnValue(pc=955,UVar(defSites={202},value=java.util.regex.Pattern$GroupCurly[↦908;refId=358])),
	214: Checkcast(pc=957,UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=_ <: java.util.regex.Pattern$Node[refId=318; values=«java.util.regex.Pattern$Ques[↦214;refId=135], _ <: java.util.regex.Pattern$Node[↦622;refId=118], java.util.regex.Pattern$BehindS[↦440;refId=239], _ <: java.util.regex.Pattern$Node[↦118;refId=181], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166], java.util.regex.Pattern$Behind[↦461;refId=241], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),java.util.regex.Pattern$GroupHead),
	215: Assignment(pc=960,DVar(useSites={230,221},value=an int,origin=215),GetField(pc=960,java.util.regex.Pattern$GroupHead,localIndex,int,UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=java.util.regex.Pattern$GroupHead[refId=363; values=«_ <: java.util.regex.Pattern$Node[↦622;refId=118], _ <: java.util.regex.Pattern$Node[↦118;refId=181], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166]»]))),
	216: Assignment(pc=967,DVar(useSites={218},value={java.util.regex.Pattern$Qtype, null}[↦967;refId=365],origin=216),GetField(pc=967,java.util.regex.Pattern$Curly,type,java.util.regex.Pattern$Qtype,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348]))),
	217: Assignment(pc=970,DVar(useSites={218},value={java.util.regex.Pattern$Qtype, null}[↦970;refId=366],origin=217),GetStatic(pc=970,java.util.regex.Pattern$Qtype,GREEDY,java.util.regex.Pattern$Qtype)),
	218: If(pc=973,UVar(defSites={216},value={java.util.regex.Pattern$Qtype, null}[↦967;refId=365]),!=,UVar(defSites={217},value={java.util.regex.Pattern$Qtype, null}[↦970;refId=366]),target=228),
	219: Assignment(pc=976,DVar(useSites={244,226,242,241,233,221,243,239},value=java.util.regex.Pattern$Loop[↦976;refId=372],origin=219),New(pc=976,java.util.regex.Pattern$Loop)),
	220: Assignment(pc=981,DVar(useSites={221},value=an int,origin=220),GetField(pc=981,java.util.regex.Pattern,localCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	221: NonVirtualMethodCall(pc=986,java.util.regex.Pattern$Loop,isInterface=false,void <init>(int,int),UVar(defSites={219},value=java.util.regex.Pattern$Loop[↦976;refId=372]),(UVar(defSites={220},value=an int),UVar(defSites={215},value=an int))),
	222: Assignment(pc=993,DVar(useSites={224},value=an int,origin=222),GetField(pc=993,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348]))),
	223: Assignment(pc=996,DVar(useSites={224},value=int = 2147483647,origin=223),IntConst(pc=996,2147483647)),
	224: If(pc=999,UVar(defSites={222},value=an int),!=,UVar(defSites={223},value=int = 2147483647),target=232),
	225: Assignment(pc=1003,DVar(useSites={226},value={_ <: java.util.List, null}[↦1003;refId=377],origin=225),GetField(pc=1003,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	226: ExprStmt(pc=1008,VirtualFunctionCall(pc=1008,java.util.List,isInterface=true,boolean add(java.lang.Object),UVar(defSites={225},value={_ <: java.util.List, null}[↦1003;refId=377]),(UVar(defSites={219},value=java.util.regex.Pattern$Loop[↦976;refId=372])))),
	227: Goto(pc=1014,target=232),
	228: Assignment(pc=1017,DVar(useSites={244,242,230,241,233,243,239},value=java.util.regex.Pattern$LazyLoop[↦1017;refId=367],origin=228),New(pc=1017,java.util.regex.Pattern$LazyLoop)),
	229: Assignment(pc=1022,DVar(useSites={230},value=an int,origin=229),GetField(pc=1022,java.util.regex.Pattern,localCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	230: NonVirtualMethodCall(pc=1027,java.util.regex.Pattern$LazyLoop,isInterface=false,void <init>(int,int),UVar(defSites={228},value=java.util.regex.Pattern$LazyLoop[↦1017;refId=367]),(UVar(defSites={229},value=an int),UVar(defSites={215},value=an int))),
	231: Nop(pc=1030),
	232: Assignment(pc=1032,DVar(useSites={233,245},value=java.util.regex.Pattern$Prolog[↦1032;refId=386],origin=232),New(pc=1032,java.util.regex.Pattern$Prolog)),
	233: NonVirtualMethodCall(pc=1038,java.util.regex.Pattern$Prolog,isInterface=false,void <init>(java.util.regex.Pattern$Loop),UVar(defSites={232},value=java.util.regex.Pattern$Prolog[↦1032;refId=386]),(UVar(defSites={228,219},value=_ <: java.util.regex.Pattern$Loop[refId=376; values=«java.util.regex.Pattern$LazyLoop[↦1017;refId=367], java.util.regex.Pattern$Loop[↦976;refId=372]»]))),
	234: Assignment(pc=1045,DVar(useSites={236},value=an int,origin=234),GetField(pc=1045,java.util.regex.Pattern,localCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	235: Assignment(pc=1048,DVar(useSites={236},value=int = 1,origin=235),IntConst(pc=1048,1)),
	236: Assignment(pc=1049,DVar(useSites={237},value=an int,origin=236),BinaryExpr(pc=1049,ComputationalTypeInt,UVar(defSites={234},value=an int),+,UVar(defSites={235},value=int = 1))),
	237: PutField(pc=1050,java.util.regex.Pattern,localCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={236},value=an int)),
	238: Assignment(pc=1057,DVar(useSites={239},value=an int,origin=238),GetField(pc=1057,java.util.regex.Pattern$Curly,cmin,int,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348]))),
	239: PutField(pc=1060,java.util.regex.Pattern$Loop,cmin,int,UVar(defSites={228,219},value=_ <: java.util.regex.Pattern$Loop[refId=376; values=«java.util.regex.Pattern$LazyLoop[↦1017;refId=367], java.util.regex.Pattern$Loop[↦976;refId=372]»]),UVar(defSites={238},value=an int)),
	240: Assignment(pc=1067,DVar(useSites={241},value=an int,origin=240),GetField(pc=1067,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={149},value=java.util.regex.Pattern$Curly[↦682;refId=348]))),
	241: PutField(pc=1070,java.util.regex.Pattern$Loop,cmax,int,UVar(defSites={228,219},value=_ <: java.util.regex.Pattern$Loop[refId=376; values=«java.util.regex.Pattern$LazyLoop[↦1017;refId=367], java.util.regex.Pattern$Loop[↦976;refId=372]»]),UVar(defSites={240},value=an int)),
	242: PutField(pc=1076,java.util.regex.Pattern$Loop,body,java.util.regex.Pattern$Node,UVar(defSites={228,219},value=_ <: java.util.regex.Pattern$Loop[refId=376; values=«java.util.regex.Pattern$LazyLoop[↦1017;refId=367], java.util.regex.Pattern$Loop[↦976;refId=372]»]),UVar(defSites={104,88,56,12,134,141,93,99,23,31},value=java.util.regex.Pattern$GroupHead[refId=275; values=«_ <: java.util.regex.Pattern$Node[↦622;refId=118], _ <: java.util.regex.Pattern$Node[↦118;refId=181], _ <: java.util.regex.Pattern$Node[↦647;refId=108], _ <: java.util.regex.Pattern$Node[↦309;refId=166]»])),
	243: PutField(pc=1082,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={104,88,142,57,13,93,99,135,23,31},value={_ <: java.util.regex.Pattern$Node, null}[refId=370; values=«{_ <: java.util.regex.Pattern$Node, null}[↦652;refId=109], java.util.regex.Pattern$Ques[↦214;refId=135], java.util.regex.Pattern$BehindS[↦440;refId=239], {_ <: java.util.regex.Pattern$Node, null}[↦314;refId=167], java.util.regex.Pattern$NotBehindS[↦490;refId=234], java.util.regex.Pattern$Pos[↦166;refId=198], {_ <: java.util.regex.Pattern$Node, null}[↦627;refId=119], java.util.regex.Pattern$Behind[↦461;refId=241], {_ <: java.util.regex.Pattern$Node, null}[↦123;refId=182], java.util.regex.Pattern$NotBehind[↦511;refId=236]»]),UVar(defSites={228,219},value=_ <: java.util.regex.Pattern$Loop[refId=376; values=«java.util.regex.Pattern$LazyLoop[↦1017;refId=367], java.util.regex.Pattern$Loop[↦976;refId=372]»])),
	244: PutField(pc=1088,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={228,219},value=_ <: java.util.regex.Pattern$Loop[refId=376; values=«java.util.regex.Pattern$LazyLoop[↦1017;refId=367], java.util.regex.Pattern$Loop[↦976;refId=372]»])),
	245: ReturnValue(pc=1093,UVar(defSites={232},value=java.util.regex.Pattern$Prolog[↦1032;refId=386])),
	246: Assignment(pc=1095,DVar(useSites={247},value=String("Internal logic error")[@1095;refId=382],origin=246),StringConst(pc=1095,Internal logic error)),
	247: Assignment(pc=1098,DVar(useSites={248},value={_ <: java.util.regex.PatternSyntaxException, null}[↦1098;refId=384],origin=247),VirtualFunctionCall(pc=1098,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={246},value=String("Internal logic error")[@1095;refId=382])))),
	248: Throw(pc=1101,UVar(defSites={247},value={_ <: java.util.regex.PatternSyntaxException, null}[↦1098;refId=384]))
),cfg=CFG(
	BB_0: BasicBlock(start=52,end=52) -> {BB_7c,BB_2b}
	BB_10: BasicBlock(start=46,end=47) -> {BB_7c,BB_57}
	BB_11: BasicBlock(start=93,end=96) -> {BB_7c,BB_28}
	BB_12: BasicBlock(start=228,end=230) -> {BB_7c,BB_65}
	BB_13: BasicBlock(start=57,end=58) -> {BB_7c,BB_3f}
	BB_14: BasicBlock(start=78,end=79) -> {BB_83,BB_4f}
	BB_15: BasicBlock(start=164,end=165) -> {BB_f,BB_37}
	BB_16: BasicBlock(start=179,end=181) -> {BB_7c,BB_5d}
	BB_17: BasicBlock(start=121,end=121) -> {BB_7c,BB_82}
	BB_18: BasicBlock(start=132,end=132) -> {BB_7c}
	BB_19: BasicBlock(start=133,end=134) -> {BB_7c,BB_4e}
	BB_1: BasicBlock(start=138,end=138) -> {BB_56}
	BB_1a: BasicBlock(start=116,end=116) -> {BB_7c,BB_1c}
	BB_1b: BasicBlock(start=248,end=248) -> {BB_7c}
	BB_1c: BasicBlock(start=117,end=117) -> {BB_56}
	BB_1d: BasicBlock(start=85,end=86) -> {BB_49,BB_67}
	BB_1e: BasicBlock(start=201,end=201) -> {BB_7c,BB_8}
	BB_1f: BasicBlock(start=70,end=71) -> {BB_7c,BB_62}
	BB_20: BasicBlock(start=192,end=192) -> {BB_7c,BB_2e}
	BB_21: BasicBlock(start=28,end=29) -> {BB_7c,BB_75}
	BB_22: BasicBlock(start=38,end=39) -> {BB_69,BB_5b}
	BB_23: BasicBlock(start=21,end=21) -> {BB_7c,BB_3d}
	BB_24: BasicBlock(start=137,end=137) -> {BB_7c,BB_1}
	BB_25: BasicBlock(start=92,end=92) -> {BB_28}
	BB_26: BasicBlock(start=197,end=198) -> {BB_7c,BB_5c}
	BB_27: BasicBlock(start=65,end=65) -> {BB_7c,BB_4b}
	BB_28: BasicBlock(start=97,end=97) -> {BB_2c}
	BB_29: BasicBlock(start=156,end=157) -> {BB_7c,BB_6b}
	BB_2: BasicBlock(start=234,end=243) -> {BB_7c,BB_36}
	BB_2a: BasicBlock(start=9,end=9) -> {BB_7c,BB_9}
	BB_2b: BasicBlock(start=53,end=53) -> {BB_7c}
	BB_2c: BasicBlock(start=109,end=110) -> {BB_7c,BB_80}
	BB_2d: BasicBlock(start=77,end=77) -> {BB_7c,BB_14}
	BB_2e: BasicBlock(start=193,end=194) -> {BB_7b,BB_26}
	BB_2f: BasicBlock(start=212,end=213) -> {BB_5a}
	BB_30: BasicBlock(start=124,end=125) -> {BB_35,BB_7a}
	BB_31: BasicBlock(start=225,end=226) -> {BB_7c,BB_81}
	BB_32: BasicBlock(start=13,end=14) -> {BB_7c,BB_7d}
	BB_33: BasicBlock(start=41,end=41) -> {BB_7c,BB_d}
	BB_34: BasicBlock(start=73,end=74) -> {BB_7c,BB_6e}
	BB_35: BasicBlock(start=128,end=129) -> {BB_4d,BB_19}
	BB_36: BasicBlock(start=244,end=245) -> {BB_5a}
	BB_37: BasicBlock(start=166,end=166) -> {BB_7c,BB_50}
	BB_38: BasicBlock(start=34,end=34) -> {BB_56}
	BB_39: BasicBlock(start=148,end=149) -> {BB_7c,BB_59}
	BB_3: BasicBlock(start=0,end=3) -> {BB_7c,BB_79}
	BB_3a: BasicBlock(start=64,end=64) -> {BB_7c,BB_27}
	BB_3b: BasicBlock(start=17,end=18) -> {BB_7c,BB_78}
	BB_3c: BasicBlock(start=191,end=191) -> {BB_7c,BB_20}
	BB_3d: BasicBlock(start=22,end=24) -> {BB_7c,BB_e}
	BB_3e: BasicBlock(start=44,end=45) -> {BB_7c,BB_10}
	BB_3f: BasicBlock(start=59,end=62) -> {BB_7c,BB_58}
	BB_40: BasicBlock(start=118,end=119) -> {BB_7c,BB_7}
	BB_41: BasicBlock(start=54,end=56) -> {BB_7c,BB_13}
	BB_42: BasicBlock(start=144,end=144) -> {BB_7c,BB_56}
	BB_43: BasicBlock(start=49,end=50) -> {BB_7c,BB_76}
	BB_44: BasicBlock(start=159,end=161) -> {BB_7c,BB_52}
	BB_45: BasicBlock(start=187,end=188) -> {BB_5a}
	BB_46: BasicBlock(start=172,end=173) -> {BB_7c,BB_c}
	BB_47: BasicBlock(start=219,end=221) -> {BB_7c,BB_85}
	BB_48: BasicBlock(start=7,end=8) -> {BB_2a,BB_6d}
	BB_49: BasicBlock(start=98,end=98) -> {BB_66,BB_68}
	BB_4: BasicBlock(start=88,end=91) -> {BB_7c,BB_25}
	BB_4a: BasicBlock(start=103,end=103) -> {BB_4c}
	BB_4b: BasicBlock(start=66,end=66) -> {BB_56}
	BB_4c: BasicBlock(start=108,end=108) -> {BB_2c}
	BB_4d: BasicBlock(start=130,end=131) -> {BB_7c,BB_18}
	BB_4e: BasicBlock(start=135,end=136) -> {BB_7c,BB_24}
	BB_4f: BasicBlock(start=80,end=81) -> {BB_7c,BB_70}
	BB_50: BasicBlock(start=167,end=167) -> {BB_7c,BB_74}
	BB_51: BasicBlock(start=35,end=35) -> {BB_7c,BB_73}
	BB_52: BasicBlock(start=162,end=162) -> {BB_7c,BB_7e}
	BB_53: BasicBlock(start=209,end=211) -> {BB_7c,BB_2f}
	BB_54: BasicBlock(start=112,end=114) -> {BB_7c,BB_6}
	BB_55: BasicBlock(start=123,end=123) -> {BB_7c,BB_30}
	BB_56: BasicBlock(start=145,end=147) -> {BB_7c,BB_39}
	BB_57: BasicBlock(start=48,end=48) -> {BB_7c,BB_43}
	BB_58: BasicBlock(start=63,end=63) -> {BB_7c,BB_3a}
	BB_59: BasicBlock(start=150,end=150) -> {BB_72,BB_b}
	BB_5: BasicBlock(start=170,end=171) -> {BB_5a}
	BB_5a: ExitNode(normalReturn=true)
	BB_5b: BasicBlock(start=67,end=69) -> {BB_7c,BB_1f}
	BB_5c: BasicBlock(start=199,end=199) -> {BB_7c,BB_7f}
	BB_5d: BasicBlock(start=182,end=182) -> {BB_45}
	BB_5e: BasicBlock(start=16,end=16) -> {BB_56}
	BB_5f: BasicBlock(start=31,end=33) -> {BB_7c,BB_38}
	BB_60: BasicBlock(start=154,end=155) -> {BB_5a}
	BB_61: BasicBlock(start=11,end=12) -> {BB_7c,BB_32}
	BB_62: BasicBlock(start=72,end=72) -> {BB_7c,BB_34}
	BB_63: BasicBlock(start=175,end=178) -> {BB_16,BB_77}
	BB_64: BasicBlock(start=43,end=43) -> {BB_3e,BB_41}
	BB_65: BasicBlock(start=231,end=231) -> {BB_86}
	BB_66: BasicBlock(start=99,end=102) -> {BB_7c,BB_4a}
	BB_67: BasicBlock(start=87,end=87) -> {BB_4,BB_11}
	BB_68: BasicBlock(start=104,end=107) -> {BB_7c,BB_4c}
	BB_69: BasicBlock(start=40,end=40) -> {BB_7c,BB_33}
	BB_6: BasicBlock(start=115,end=115) -> {BB_7c,BB_1a}
	BB_6a: BasicBlock(start=26,end=27) -> {BB_7c,BB_21}
	BB_6b: BasicBlock(start=158,end=158) -> {BB_15,BB_44}
	BB_6c: BasicBlock(start=186,end=186) -> {BB_45}
	BB_6d: BasicBlock(start=139,end=141) -> {BB_7c,BB_a}
	BB_6e: BasicBlock(start=75,end=76) -> {BB_7c,BB_2d}
	BB_6f: BasicBlock(start=246,end=247) -> {BB_7c,BB_1b}
	BB_70: BasicBlock(start=82,end=82) -> {BB_7c}
	BB_71: BasicBlock(start=214,end=214) -> {BB_7c,BB_84}
	BB_72: BasicBlock(start=151,end=152) -> {BB_5a}
	BB_73: BasicBlock(start=36,end=37) -> {BB_22,BB_5b}
	BB_74: BasicBlock(start=168,end=169) -> {BB_5,BB_46}
	BB_75: BasicBlock(start=30,end=30) -> {BB_7c,BB_5f}
	BB_76: BasicBlock(start=51,end=51) -> {BB_7c,BB_0}
	BB_77: BasicBlock(start=183,end=185) -> {BB_7c,BB_6c}
	BB_78: BasicBlock(start=19,end=20) -> {BB_7c,BB_23}
	BB_79: BasicBlock(start=4,end=6) -> {BB_7c,BB_48}
	BB_7: BasicBlock(start=120,end=120) -> {BB_7c}
	BB_7a: BasicBlock(start=126,end=127) -> {BB_5a}
	BB_7b: BasicBlock(start=195,end=196) -> {BB_5a}
	BB_7c: ExitNode(normalReturn=false)
	BB_7d: BasicBlock(start=15,end=15) -> {BB_7c,BB_5e}
	BB_7e: BasicBlock(start=163,end=163) -> {BB_7c,BB_15}
	BB_7f: BasicBlock(start=200,end=200) -> {BB_71,BB_1e}
	BB_80: BasicBlock(start=111,end=111) -> {BB_54,BB_56}
	BB_81: BasicBlock(start=227,end=227) -> {BB_86}
	BB_82: BasicBlock(start=122,end=122) -> {BB_7c,BB_55}
	BB_83: BasicBlock(start=83,end=84) -> {BB_7c,BB_1d}
	BB_84: BasicBlock(start=215,end=218) -> {BB_47,BB_12}
	BB_85: BasicBlock(start=222,end=224) -> {BB_86,BB_31}
	BB_86: BasicBlock(start=232,end=233) -> {BB_7c,BB_2}
	BB_8: BasicBlock(start=202,end=208) -> {BB_7c,BB_53}
	BB_9: BasicBlock(start=10,end=10) -> {BB_6a,BB_3b,BB_17,BB_40,BB_61,BB_51}
	BB_a: BasicBlock(start=142,end=143) -> {BB_7c,BB_42}
	BB_b: BasicBlock(start=153,end=153) -> {BB_60,BB_29}
	BB_c: BasicBlock(start=174,end=174) -> {BB_7c,BB_63}
	BB_d: BasicBlock(start=42,end=42) -> {BB_7c,BB_64}
	BB_e: BasicBlock(start=25,end=25) -> {BB_56}
	BB_f: BasicBlock(start=189,end=190) -> {BB_3c,BB_6f}
))

java.lang.String composeOneStep(java.lang.String)
AITACode(params=(Parameters(
	1: useSites={4,2,11} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=int = 0,origin=0),IntConst(pc=1,0)),
	1: Assignment(pc=2,DVar(useSites={2},value=int = 2,origin=1),IntConst(pc=2,2)),
	2: Assignment(pc=3,DVar(useSites={4,11},value=an int,origin=2),StaticFunctionCall(pc=3,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),UVar(defSites={0},value=int = 0),UVar(defSites={1},value=int = 2)))),
	3: Assignment(pc=8,DVar(useSites={4},value=int = 0,origin=3),IntConst(pc=8,0)),
	4: Assignment(pc=10,DVar(useSites={6,7},value={java.lang.String, null}[↦10;refId=106],origin=4),VirtualFunctionCall(pc=10,java.lang.String,isInterface=false,java.lang.String substring(int,int),UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),(UVar(defSites={3},value=int = 0),UVar(defSites={2},value=an int)))),
	5: Assignment(pc=15,DVar(useSites={6},value={java.text.Normalizer$Form, null}[↦15;refId=107],origin=5),GetStatic(pc=15,java.text.Normalizer$Form,NFC,java.text.Normalizer$Form)),
	6: Assignment(pc=18,DVar(useSites={14,7},value={java.lang.String, null}[↦18;refId=109],origin=6),StaticFunctionCall(pc=18,java.text.Normalizer,isInterface=false,java.lang.String normalize(java.lang.CharSequence,java.text.Normalizer$Form),(UVar(defSites={4},value={java.lang.String, null}[↦10;refId=106]),UVar(defSites={5},value={java.text.Normalizer$Form, null}[↦15;refId=107])))),
	7: Assignment(pc=24,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=24,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={6},value={java.lang.String, null}[↦18;refId=109]),(UVar(defSites={4},value={java.lang.String, null}[↦10;refId=106])))),
	8: If(pc=27,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	9: Assignment(pc=30,DVar(useSites={10},value=null[↦30],origin=9),NullExpr(pc=30)),
	10: ReturnValue(pc=31,UVar(defSites={9},value=null[↦30])),
	11: Assignment(pc=34,DVar(useSites={15},value={java.lang.String, null}[↦34;refId=113],origin=11),VirtualFunctionCall(pc=34,java.lang.String,isInterface=false,java.lang.String substring(int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={2},value=an int)))),
	12: Assignment(pc=39,DVar(useSites={14,13},value=java.lang.StringBuilder[↦39;refId=114],origin=12),New(pc=39,java.lang.StringBuilder)),
	13: NonVirtualMethodCall(pc=43,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={12},value=java.lang.StringBuilder[↦39;refId=114]),()),
	14: Assignment(pc=47,DVar(useSites={15},value={java.lang.StringBuilder, null}[↦47;refId=117],origin=14),VirtualFunctionCall(pc=47,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={12},value=java.lang.StringBuilder[↦39;refId=114]),(UVar(defSites={6},value=java.lang.String[↦18;refId=109])))),
	15: Assignment(pc=52,DVar(useSites={16},value={java.lang.StringBuilder, null}[↦52;refId=120],origin=15),VirtualFunctionCall(pc=52,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={14},value={java.lang.StringBuilder, null}[↦47;refId=117]),(UVar(defSites={11},value={java.lang.String, null}[↦34;refId=113])))),
	16: Assignment(pc=55,DVar(useSites={17},value={java.lang.String, null}[↦55;refId=123],origin=16),VirtualFunctionCall(pc=55,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={15},value={java.lang.StringBuilder, null}[↦52;refId=120]),())),
	17: ReturnValue(pc=58,UVar(defSites={16},value={java.lang.String, null}[↦55;refId=123]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_c,BB_7}
	BB_1: BasicBlock(start=5,end=6) -> {BB_c,BB_6}
	BB_2: BasicBlock(start=14,end=14) -> {BB_c,BB_d}
	BB_3: BasicBlock(start=9,end=10) -> {BB_8}
	BB_4: BasicBlock(start=17,end=17) -> {BB_8}
	BB_5: BasicBlock(start=12,end=13) -> {BB_c,BB_2}
	BB_6: BasicBlock(start=7,end=7) -> {BB_c,BB_b}
	BB_7: BasicBlock(start=3,end=4) -> {BB_c,BB_1}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=16,end=16) -> {BB_c,BB_4}
	BB_a: BasicBlock(start=11,end=11) -> {BB_c,BB_5}
	BB_b: BasicBlock(start=8,end=8) -> {BB_a,BB_3}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=15) -> {BB_c,BB_9}
))

int x()
AITACode(params=(Parameters(
	0: useSites={0,28,18,14,33,37,3} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={6,1,13},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Assignment(pc=6,DVar(useSites={2},value=int ∈ [0,1],origin=1),StaticFunctionCall(pc=6,java.util.regex.ASCII,isInterface=false,boolean isHexDigit(int),(UVar(defSites={0},value=an int)))),
	2: If(pc=9,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	3: Assignment(pc=13,DVar(useSites={4,9},value=an int,origin=3),VirtualFunctionCall(pc=13,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	4: Assignment(pc=18,DVar(useSites={5},value=int ∈ [0,1],origin=4),StaticFunctionCall(pc=18,java.util.regex.ASCII,isInterface=false,boolean isHexDigit(int),(UVar(defSites={3},value=an int)))),
	5: If(pc=21,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=36),
	6: Assignment(pc=25,DVar(useSites={8},value=an int,origin=6),StaticFunctionCall(pc=25,java.util.regex.ASCII,isInterface=false,int toDigit(int),(UVar(defSites={0},value=an int)))),
	7: Assignment(pc=28,DVar(useSites={8},value=int = 16,origin=7),IntConst(pc=28,16)),
	8: Assignment(pc=30,DVar(useSites={10},value=an int,origin=8),BinaryExpr(pc=30,ComputationalTypeInt,UVar(defSites={6},value=an int),*,UVar(defSites={7},value=int = 16))),
	9: Assignment(pc=32,DVar(useSites={10},value=an int,origin=9),StaticFunctionCall(pc=32,java.util.regex.ASCII,isInterface=false,int toDigit(int),(UVar(defSites={3},value=an int)))),
	10: Assignment(pc=35,DVar(useSites={11},value=an int,origin=10),BinaryExpr(pc=35,ComputationalTypeInt,UVar(defSites={8},value=an int),+,UVar(defSites={9},value=an int))),
	11: ReturnValue(pc=36,UVar(defSites={10},value=an int)),
	12: Assignment(pc=41,DVar(useSites={13},value=int = 123,origin=12),IntConst(pc=41,123)),
	13: If(pc=43,UVar(defSites={0},value=an int),!=,UVar(defSites={12},value=int = 123),target=36),
	14: Assignment(pc=47,DVar(useSites={15},value=an int,origin=14),VirtualFunctionCall(pc=47,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	15: Assignment(pc=50,DVar(useSites={16},value=int ∈ [0,1],origin=15),StaticFunctionCall(pc=50,java.util.regex.ASCII,isInterface=false,boolean isHexDigit(int),(UVar(defSites={14},value=an int)))),
	16: If(pc=53,UVar(defSites={15},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=36),
	17: Assignment(pc=56,DVar(useSites={22,35},value=int = 0,origin=17),IntConst(pc=56,0)),
	18: Assignment(pc=59,DVar(useSites={19,23,31},value=an int,origin=18),VirtualFunctionCall(pc=59,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	19: Assignment(pc=64,DVar(useSites={20},value=int ∈ [0,1],origin=19),StaticFunctionCall(pc=64,java.util.regex.ASCII,isInterface=false,boolean isHexDigit(int),(UVar(defSites={18},value=an int)))),
	20: If(pc=67,UVar(defSites={19},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=30),
	21: Assignment(pc=71,DVar(useSites={22},value=int = 4,origin=21),IntConst(pc=71,4)),
	22: Assignment(pc=72,DVar(useSites={24},value=an int,origin=22),BinaryExpr(pc=72,ComputationalTypeInt,UVar(defSites={24,17},value=an int),<<,UVar(defSites={21},value=int = 4))),
	23: Assignment(pc=74,DVar(useSites={24},value=an int,origin=23),StaticFunctionCall(pc=74,java.util.regex.ASCII,isInterface=false,int toDigit(int),(UVar(defSites={18},value=an int)))),
	24: Assignment(pc=77,DVar(useSites={26,22,35},value=an int,origin=24),BinaryExpr(pc=77,ComputationalTypeInt,UVar(defSites={22},value=an int),+,UVar(defSites={23},value=an int))),
	25: Assignment(pc=80,DVar(useSites={26},value=int = 1114111,origin=25),IntConst(pc=80,1114111)),
	26: If(pc=83,UVar(defSites={24},value=an int),<=,UVar(defSites={25},value=int = 1114111),target=18),
	27: Assignment(pc=87,DVar(useSites={28},value=String("Hexadecimal codepoint is too big")[@87;refId=129],origin=27),StringConst(pc=87,Hexadecimal codepoint is too big)),
	28: Assignment(pc=90,DVar(useSites={29},value={_ <: java.util.regex.PatternSyntaxException, null}[↦90;refId=131],origin=28),VirtualFunctionCall(pc=90,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={27},value=String("Hexadecimal codepoint is too big")[@87;refId=129])))),
	29: Throw(pc=93,UVar(defSites={28},value={_ <: java.util.regex.PatternSyntaxException, null}[↦90;refId=131])),
	30: Assignment(pc=95,DVar(useSites={31},value=int = 125,origin=30),IntConst(pc=95,125)),
	31: If(pc=97,UVar(defSites={18},value=an int),==,UVar(defSites={30},value=int = 125),target=35),
	32: Assignment(pc=101,DVar(useSites={33},value=String("Unclosed hexadecimal escape sequence")[@101;refId=133],origin=32),StringConst(pc=101,Unclosed hexadecimal escape sequence)),
	33: Assignment(pc=104,DVar(useSites={34},value={_ <: java.util.regex.PatternSyntaxException, null}[↦104;refId=135],origin=33),VirtualFunctionCall(pc=104,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={32},value=String("Unclosed hexadecimal escape sequence")[@101;refId=133])))),
	34: Throw(pc=107,UVar(defSites={33},value={_ <: java.util.regex.PatternSyntaxException, null}[↦104;refId=135])),
	35: ReturnValue(pc=109,UVar(defSites={24,17},value=an int)),
	36: Assignment(pc=111,DVar(useSites={37},value=String("Illegal hexadecimal escape sequence")[@111;refId=111],origin=36),StringConst(pc=111,Illegal hexadecimal escape sequence)),
	37: Assignment(pc=114,DVar(useSites={38},value={_ <: java.util.regex.PatternSyntaxException, null}[↦114;refId=113],origin=37),VirtualFunctionCall(pc=114,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={36},value=String("Illegal hexadecimal escape sequence")[@111;refId=111])))),
	38: Throw(pc=117,UVar(defSites={37},value={_ <: java.util.regex.PatternSyntaxException, null}[↦114;refId=113]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1c,BB_5}
	BB_10: BasicBlock(start=21,end=23) -> {BB_1c,BB_3}
	BB_11: BasicBlock(start=17,end=17) -> {BB_16}
	BB_12: BasicBlock(start=32,end=33) -> {BB_1c,BB_13}
	BB_13: BasicBlock(start=34,end=34) -> {BB_1c}
	BB_14: BasicBlock(start=3,end=3) -> {BB_1c,BB_1b}
	BB_15: BasicBlock(start=35,end=35) -> {BB_17}
	BB_16: BasicBlock(start=18,end=18) -> {BB_1c,BB_1a}
	BB_17: ExitNode(normalReturn=true)
	BB_18: BasicBlock(start=36,end=37) -> {BB_1c,BB_f}
	BB_19: BasicBlock(start=30,end=31) -> {BB_12,BB_15}
	BB_1: BasicBlock(start=5,end=5) -> {BB_6,BB_18}
	BB_1a: BasicBlock(start=19,end=19) -> {BB_1c,BB_d}
	BB_1b: BasicBlock(start=4,end=4) -> {BB_1c,BB_1}
	BB_1c: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=10,end=11) -> {BB_17}
	BB_3: BasicBlock(start=24,end=26) -> {BB_16,BB_8}
	BB_4: BasicBlock(start=14,end=14) -> {BB_1c,BB_c}
	BB_5: BasicBlock(start=1,end=1) -> {BB_1c,BB_7}
	BB_6: BasicBlock(start=6,end=6) -> {BB_1c,BB_a}
	BB_7: BasicBlock(start=2,end=2) -> {BB_9,BB_14}
	BB_8: BasicBlock(start=27,end=28) -> {BB_1c,BB_e}
	BB_9: BasicBlock(start=12,end=13) -> {BB_4,BB_18}
	BB_a: BasicBlock(start=7,end=9) -> {BB_1c,BB_2}
	BB_b: BasicBlock(start=16,end=16) -> {BB_11,BB_18}
	BB_c: BasicBlock(start=15,end=15) -> {BB_1c,BB_b}
	BB_d: BasicBlock(start=20,end=20) -> {BB_10,BB_19}
	BB_e: BasicBlock(start=29,end=29) -> {BB_1c}
	BB_f: BasicBlock(start=38,end=38) -> {BB_1c}
))

java.util.regex.Pattern$Node closure(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,72,12,28,2,34,82,58,70,22,46,41,25,5,93,75,27,63} (origin=-1),
	1: useSites={8,22,78,25,89,85,19,15,95} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Switch(pc=6,defaultTarget=95,index=UVar(defSites={0},value=an int),npairs=(IntIntPair(42,21),IntIntPair(43,24),IntIntPair(63,2),IntIntPair(123,27)),
	2: Assignment(pc=49,DVar(useSites={4,11},value=an int,origin=2),VirtualFunctionCall(pc=49,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	3: Assignment(pc=54,DVar(useSites={4},value=int = 63,origin=3),IntConst(pc=54,63)),
	4: If(pc=56,UVar(defSites={2},value=an int),!=,UVar(defSites={3},value=int = 63),target=10),
	5: ExprStmt(pc=60,VirtualFunctionCall(pc=60,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	6: Assignment(pc=64,DVar(useSites={8,9},value=java.util.regex.Pattern$Ques[↦64;refId=123],origin=6),New(pc=64,java.util.regex.Pattern$Ques)),
	7: Assignment(pc=69,DVar(useSites={8},value={java.util.regex.Pattern$Qtype, null}[↦69;refId=124],origin=7),GetStatic(pc=69,java.util.regex.Pattern$Qtype,LAZY,java.util.regex.Pattern$Qtype)),
	8: NonVirtualMethodCall(pc=72,java.util.regex.Pattern$Ques,isInterface=false,void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Qtype),UVar(defSites={6},value=java.util.regex.Pattern$Ques[↦64;refId=123]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={7},value={java.util.regex.Pattern$Qtype, null}[↦69;refId=124]))),
	9: ReturnValue(pc=75,UVar(defSites={6},value=java.util.regex.Pattern$Ques[↦64;refId=123])),
	10: Assignment(pc=77,DVar(useSites={11},value=int = 43,origin=10),IntConst(pc=77,43)),
	11: If(pc=79,UVar(defSites={2},value=an int),!=,UVar(defSites={10},value=int = 43),target=17),
	12: ExprStmt(pc=83,VirtualFunctionCall(pc=83,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	13: Assignment(pc=87,DVar(useSites={16,15},value=java.util.regex.Pattern$Ques[↦87;refId=119],origin=13),New(pc=87,java.util.regex.Pattern$Ques)),
	14: Assignment(pc=92,DVar(useSites={15},value={java.util.regex.Pattern$Qtype, null}[↦92;refId=120],origin=14),GetStatic(pc=92,java.util.regex.Pattern$Qtype,POSSESSIVE,java.util.regex.Pattern$Qtype)),
	15: NonVirtualMethodCall(pc=95,java.util.regex.Pattern$Ques,isInterface=false,void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Qtype),UVar(defSites={13},value=java.util.regex.Pattern$Ques[↦87;refId=119]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={14},value={java.util.regex.Pattern$Qtype, null}[↦92;refId=120]))),
	16: ReturnValue(pc=98,UVar(defSites={13},value=java.util.regex.Pattern$Ques[↦87;refId=119])),
	17: Assignment(pc=99,DVar(useSites={20,19},value=java.util.regex.Pattern$Ques[↦99;refId=115],origin=17),New(pc=99,java.util.regex.Pattern$Ques)),
	18: Assignment(pc=104,DVar(useSites={19},value={java.util.regex.Pattern$Qtype, null}[↦104;refId=116],origin=18),GetStatic(pc=104,java.util.regex.Pattern$Qtype,GREEDY,java.util.regex.Pattern$Qtype)),
	19: NonVirtualMethodCall(pc=107,java.util.regex.Pattern$Ques,isInterface=false,void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Qtype),UVar(defSites={17},value=java.util.regex.Pattern$Ques[↦99;refId=115]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={18},value={java.util.regex.Pattern$Qtype, null}[↦104;refId=116]))),
	20: ReturnValue(pc=110,UVar(defSites={17},value=java.util.regex.Pattern$Ques[↦99;refId=115])),
	21: Assignment(pc=113,DVar(useSites={22},value=int = 0,origin=21),IntConst(pc=113,0)),
	22: Assignment(pc=114,DVar(useSites={23},value={_ <: java.util.regex.Pattern$Node, null}[↦114;refId=129],origin=22),VirtualFunctionCall(pc=114,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node curly(java.util.regex.Pattern$Node,int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={21},value=int = 0)))),
	23: ReturnValue(pc=117,UVar(defSites={22},value={_ <: java.util.regex.Pattern$Node, null}[↦114;refId=129])),
	24: Assignment(pc=120,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=120,1)),
	25: Assignment(pc=121,DVar(useSites={26},value={_ <: java.util.regex.Pattern$Node, null}[↦121;refId=127],origin=25),VirtualFunctionCall(pc=121,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node curly(java.util.regex.Pattern$Node,int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={24},value=int = 1)))),
	26: ReturnValue(pc=124,UVar(defSites={25},value={_ <: java.util.regex.Pattern$Node, null}[↦121;refId=127])),
	27: Assignment(pc=126,DVar(useSites={31},value={int[], null}[↦126;refId=105],origin=27),GetField(pc=126,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	28: Assignment(pc=130,DVar(useSites={30},value=an int,origin=28),GetField(pc=130,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	29: Assignment(pc=133,DVar(useSites={30},value=int = 1,origin=29),IntConst(pc=133,1)),
	30: Assignment(pc=134,DVar(useSites={31},value=an int,origin=30),BinaryExpr(pc=134,ComputationalTypeInt,UVar(defSites={28},value=an int),+,UVar(defSites={29},value=int = 1))),
	31: Assignment(pc=135,DVar(useSites={32,39},value=an int,origin=31),ArrayLoad(pc=135,UVar(defSites={30},value=an int),UVar(defSites={27},value={int[], null}[↦126;refId=105]))),
	32: Assignment(pc=138,DVar(useSites={33},value=int ∈ [0,1],origin=32),StaticFunctionCall(pc=138,java.util.regex.ASCII,isInterface=false,boolean isDigit(int),(UVar(defSites={31},value=an int)))),
	33: If(pc=141,UVar(defSites={32},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=92),
	34: ExprStmt(pc=145,VirtualFunctionCall(pc=145,java.util.regex.Pattern,isInterface=false,int skip(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	35: Assignment(pc=149,DVar(useSites={37},value=int = 0,origin=35),IntConst(pc=149,0)),
	36: Assignment(pc=154,DVar(useSites={37},value=int = 10,origin=36),IntConst(pc=154,10)),
	37: Assignment(pc=156,DVar(useSites={40},value=an int,origin=37),BinaryExpr(pc=156,ComputationalTypeInt,UVar(defSites={40,35},value=an int),*,UVar(defSites={36},value=int = 10))),
	38: Assignment(pc=158,DVar(useSites={39},value=int = 48,origin=38),IntConst(pc=158,48)),
	39: Assignment(pc=160,DVar(useSites={40},value=an int,origin=39),BinaryExpr(pc=160,ComputationalTypeInt,UVar(defSites={41,31},value=an int),-,UVar(defSites={38},value=int = 48))),
	40: Assignment(pc=161,DVar(useSites={66,78,65,89,37,85},value=an int,origin=40),BinaryExpr(pc=161,ComputationalTypeInt,UVar(defSites={37},value=an int),+,UVar(defSites={39},value=an int))),
	41: Assignment(pc=165,DVar(useSites={42,45,61,39},value=an int,origin=41),VirtualFunctionCall(pc=165,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	42: Assignment(pc=170,DVar(useSites={43},value=int ∈ [0,1],origin=42),StaticFunctionCall(pc=170,java.util.regex.ASCII,isInterface=false,boolean isDigit(int),(UVar(defSites={41},value=an int)))),
	43: If(pc=173,UVar(defSites={42},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=36),
	44: Assignment(pc=181,DVar(useSites={45},value=int = 44,origin=44),IntConst(pc=181,44)),
	45: If(pc=183,UVar(defSites={41},value=an int),!=,UVar(defSites={44},value=int = 44),target=60),
	46: Assignment(pc=187,DVar(useSites={56,49,61,51},value=an int,origin=46),VirtualFunctionCall(pc=187,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	47: Assignment(pc=191,DVar(useSites={66,78,65,89,85},value=int = 2147483647,origin=47),IntConst(pc=191,2147483647)),
	48: Assignment(pc=197,DVar(useSites={49},value=int = 125,origin=48),IntConst(pc=197,125)),
	49: If(pc=199,UVar(defSites={46},value=an int),==,UVar(defSites={48},value=int = 125),target=60),
	50: Assignment(pc=202,DVar(useSites={66,54,78,65,89,85},value=int = 0,origin=50),IntConst(pc=202,0)),
	51: Assignment(pc=206,DVar(useSites={52},value=int ∈ [0,1],origin=51),StaticFunctionCall(pc=206,java.util.regex.ASCII,isInterface=false,boolean isDigit(int),(UVar(defSites={58,46},value=an int)))),
	52: If(pc=209,UVar(defSites={51},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=60),
	53: Assignment(pc=214,DVar(useSites={54},value=int = 10,origin=53),IntConst(pc=214,10)),
	54: Assignment(pc=216,DVar(useSites={57},value=an int,origin=54),BinaryExpr(pc=216,ComputationalTypeInt,UVar(defSites={50,57},value=an int),*,UVar(defSites={53},value=int = 10))),
	55: Assignment(pc=218,DVar(useSites={56},value=int = 48,origin=55),IntConst(pc=218,48)),
	56: Assignment(pc=220,DVar(useSites={57},value=an int,origin=56),BinaryExpr(pc=220,ComputationalTypeInt,UVar(defSites={58,46},value=an int),-,UVar(defSites={55},value=int = 48))),
	57: Assignment(pc=221,DVar(useSites={66,54,78,65,89,85},value=an int,origin=57),BinaryExpr(pc=221,ComputationalTypeInt,UVar(defSites={54},value=an int),+,UVar(defSites={56},value=an int))),
	58: Assignment(pc=225,DVar(useSites={56,61,51},value=an int,origin=58),VirtualFunctionCall(pc=225,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	59: Goto(pc=229,target=51),
	60: Assignment(pc=233,DVar(useSites={61},value=int = 125,origin=60),IntConst(pc=233,125)),
	61: If(pc=235,UVar(defSites={58,46,41},value=an int),==,UVar(defSites={60},value=int = 125),target=65),
	62: Assignment(pc=239,DVar(useSites={63},value=String("Unclosed counted closure")[@239;refId=154],origin=62),StringConst(pc=239,Unclosed counted closure)),
	63: Assignment(pc=242,DVar(useSites={64},value={_ <: java.util.regex.PatternSyntaxException, null}[↦242;refId=156],origin=63),VirtualFunctionCall(pc=242,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={62},value=String("Unclosed counted closure")[@239;refId=154])))),
	64: Throw(pc=245,UVar(defSites={63},value={_ <: java.util.regex.PatternSyntaxException, null}[↦242;refId=156])),
	65: Assignment(pc=250,DVar(useSites={67},value=an int,origin=65),BinaryExpr(pc=250,ComputationalTypeInt,UVar(defSites={40},value=an int),|,UVar(defSites={40,50,57,47},value=an int))),
	66: Assignment(pc=255,DVar(useSites={67},value=an int,origin=66),BinaryExpr(pc=255,ComputationalTypeInt,UVar(defSites={40,50,57,47},value=an int),-,UVar(defSites={40},value=an int))),
	67: Assignment(pc=256,DVar(useSites={68},value=an int,origin=67),BinaryExpr(pc=256,ComputationalTypeInt,UVar(defSites={65},value=an int),|,UVar(defSites={66},value=an int))),
	68: If(pc=257,UVar(defSites={67},value=an int),>=,IntConst(pc=-333,0),target=72),
	69: Assignment(pc=261,DVar(useSites={70},value=String("Illegal repetition range")[@261;refId=136],origin=69),StringConst(pc=261,Illegal repetition range)),
	70: Assignment(pc=264,DVar(useSites={71},value={_ <: java.util.regex.PatternSyntaxException, null}[↦264;refId=138],origin=70),VirtualFunctionCall(pc=264,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={69},value=String("Illegal repetition range")[@261;refId=136])))),
	71: Throw(pc=267,UVar(defSites={70},value={_ <: java.util.regex.PatternSyntaxException, null}[↦264;refId=138])),
	72: Assignment(pc=269,DVar(useSites={74,81},value=an int,origin=72),VirtualFunctionCall(pc=269,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	73: Assignment(pc=274,DVar(useSites={74},value=int = 63,origin=73),IntConst(pc=274,63)),
	74: If(pc=276,UVar(defSites={72},value=an int),!=,UVar(defSites={73},value=int = 63),target=80),
	75: ExprStmt(pc=280,VirtualFunctionCall(pc=280,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	76: Assignment(pc=284,DVar(useSites={78,91},value=java.util.regex.Pattern$Curly[↦284;refId=150],origin=76),New(pc=284,java.util.regex.Pattern$Curly)),
	77: Assignment(pc=293,DVar(useSites={78},value={java.util.regex.Pattern$Qtype, null}[↦293;refId=151],origin=77),GetStatic(pc=293,java.util.regex.Pattern$Qtype,LAZY,java.util.regex.Pattern$Qtype)),
	78: NonVirtualMethodCall(pc=296,java.util.regex.Pattern$Curly,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype),UVar(defSites={76},value=java.util.regex.Pattern$Curly[↦284;refId=150]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={40},value=an int),UVar(defSites={40,50,57,47},value=an int),UVar(defSites={77},value={java.util.regex.Pattern$Qtype, null}[↦293;refId=151]))),
	79: Goto(pc=301,target=91),
	80: Assignment(pc=305,DVar(useSites={81},value=int = 43,origin=80),IntConst(pc=305,43)),
	81: If(pc=307,UVar(defSites={72},value=an int),!=,UVar(defSites={80},value=int = 43),target=87),
	82: ExprStmt(pc=311,VirtualFunctionCall(pc=311,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	83: Assignment(pc=315,DVar(useSites={85,91},value=java.util.regex.Pattern$Curly[↦315;refId=145],origin=83),New(pc=315,java.util.regex.Pattern$Curly)),
	84: Assignment(pc=324,DVar(useSites={85},value={java.util.regex.Pattern$Qtype, null}[↦324;refId=146],origin=84),GetStatic(pc=324,java.util.regex.Pattern$Qtype,POSSESSIVE,java.util.regex.Pattern$Qtype)),
	85: NonVirtualMethodCall(pc=327,java.util.regex.Pattern$Curly,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype),UVar(defSites={83},value=java.util.regex.Pattern$Curly[↦315;refId=145]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={40},value=an int),UVar(defSites={40,50,57,47},value=an int),UVar(defSites={84},value={java.util.regex.Pattern$Qtype, null}[↦324;refId=146]))),
	86: Goto(pc=332,target=91),
	87: Assignment(pc=335,DVar(useSites={89,91},value=java.util.regex.Pattern$Curly[↦335;refId=141],origin=87),New(pc=335,java.util.regex.Pattern$Curly)),
	88: Assignment(pc=344,DVar(useSites={89},value={java.util.regex.Pattern$Qtype, null}[↦344;refId=142],origin=88),GetStatic(pc=344,java.util.regex.Pattern$Qtype,GREEDY,java.util.regex.Pattern$Qtype)),
	89: NonVirtualMethodCall(pc=347,java.util.regex.Pattern$Curly,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype),UVar(defSites={87},value=java.util.regex.Pattern$Curly[↦335;refId=141]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={40},value=an int),UVar(defSites={40,50,57,47},value=an int),UVar(defSites={88},value={java.util.regex.Pattern$Qtype, null}[↦344;refId=142]))),
	90: Nop(pc=350),
	91: ReturnValue(pc=354,UVar(defSites={76,83,87},value=java.util.regex.Pattern$Curly[refId=153; values=«java.util.regex.Pattern$Curly[↦335;refId=141], java.util.regex.Pattern$Curly[↦315;refId=145], java.util.regex.Pattern$Curly[↦284;refId=150]»])),
	92: Assignment(pc=356,DVar(useSites={93},value=String("Illegal repetition")[@356;refId=110],origin=92),StringConst(pc=356,Illegal repetition)),
	93: Assignment(pc=359,DVar(useSites={94},value={_ <: java.util.regex.PatternSyntaxException, null}[↦359;refId=112],origin=93),VirtualFunctionCall(pc=359,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={92},value=String("Illegal repetition")[@356;refId=110])))),
	94: Throw(pc=362,UVar(defSites={93},value={_ <: java.util.regex.PatternSyntaxException, null}[↦359;refId=112])),
	95: ReturnValue(pc=364,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=5) -> {BB_33,BB_e}
	BB_10: BasicBlock(start=21,end=22) -> {BB_33,BB_2c}
	BB_11: BasicBlock(start=33,end=33) -> {BB_1b,BB_12}
	BB_12: BasicBlock(start=92,end=93) -> {BB_33,BB_32}
	BB_13: BasicBlock(start=65,end=68) -> {BB_8,BB_29}
	BB_14: BasicBlock(start=9,end=9) -> {BB_25}
	BB_15: BasicBlock(start=53,end=58) -> {BB_33,BB_1d}
	BB_16: BasicBlock(start=73,end=74) -> {BB_23,BB_2d}
	BB_17: BasicBlock(start=2,end=2) -> {BB_33,BB_22}
	BB_18: BasicBlock(start=64,end=64) -> {BB_33}
	BB_19: BasicBlock(start=17,end=19) -> {BB_33,BB_c}
	BB_1: BasicBlock(start=10,end=11) -> {BB_20,BB_19}
	BB_1a: BasicBlock(start=32,end=32) -> {BB_33,BB_11}
	BB_1b: BasicBlock(start=34,end=34) -> {BB_33,BB_24}
	BB_1c: BasicBlock(start=44,end=45) -> {BB_f,BB_d}
	BB_1d: BasicBlock(start=59,end=59) -> {BB_30}
	BB_1e: BasicBlock(start=27,end=31) -> {BB_33,BB_1a}
	BB_1f: BasicBlock(start=71,end=71) -> {BB_33}
	BB_20: BasicBlock(start=12,end=12) -> {BB_33,BB_4}
	BB_21: BasicBlock(start=86,end=86) -> {BB_6}
	BB_22: BasicBlock(start=3,end=4) -> {BB_1,BB_0}
	BB_23: BasicBlock(start=80,end=81) -> {BB_2e,BB_7}
	BB_24: BasicBlock(start=35,end=35) -> {BB_2f}
	BB_25: ExitNode(normalReturn=true)
	BB_26: BasicBlock(start=95,end=95) -> {BB_25}
	BB_27: BasicBlock(start=50,end=50) -> {BB_30}
	BB_28: BasicBlock(start=16,end=16) -> {BB_25}
	BB_29: BasicBlock(start=72,end=72) -> {BB_33,BB_16}
	BB_2: BasicBlock(start=52,end=52) -> {BB_f,BB_15}
	BB_2a: BasicBlock(start=43,end=43) -> {BB_1c,BB_2f}
	BB_2b: BasicBlock(start=26,end=26) -> {BB_25}
	BB_2c: BasicBlock(start=23,end=23) -> {BB_25}
	BB_2d: BasicBlock(start=75,end=75) -> {BB_33,BB_5}
	BB_2e: BasicBlock(start=82,end=82) -> {BB_33,BB_37}
	BB_2f: BasicBlock(start=36,end=41) -> {BB_33,BB_a}
	BB_30: BasicBlock(start=51,end=51) -> {BB_33,BB_2}
	BB_31: BasicBlock(start=79,end=79) -> {BB_6}
	BB_32: BasicBlock(start=94,end=94) -> {BB_33}
	BB_33: ExitNode(normalReturn=false)
	BB_34: BasicBlock(start=47,end=49) -> {BB_f,BB_27}
	BB_35: BasicBlock(start=62,end=63) -> {BB_33,BB_18}
	BB_36: BasicBlock(start=90,end=90) -> {BB_6}
	BB_37: BasicBlock(start=83,end=85) -> {BB_33,BB_21}
	BB_3: BasicBlock(start=1,end=1) -> {BB_1e,BB_17,BB_10,BB_26,BB_b}
	BB_4: BasicBlock(start=13,end=15) -> {BB_33,BB_28}
	BB_5: BasicBlock(start=76,end=78) -> {BB_33,BB_31}
	BB_6: BasicBlock(start=91,end=91) -> {BB_25}
	BB_7: BasicBlock(start=87,end=89) -> {BB_33,BB_36}
	BB_8: BasicBlock(start=69,end=70) -> {BB_33,BB_1f}
	BB_9: BasicBlock(start=0,end=0) -> {BB_33,BB_3}
	BB_a: BasicBlock(start=42,end=42) -> {BB_33,BB_2a}
	BB_b: BasicBlock(start=24,end=25) -> {BB_33,BB_2b}
	BB_c: BasicBlock(start=20,end=20) -> {BB_25}
	BB_d: BasicBlock(start=46,end=46) -> {BB_33,BB_34}
	BB_e: BasicBlock(start=6,end=8) -> {BB_33,BB_14}
	BB_f: BasicBlock(start=60,end=61) -> {BB_13,BB_35}
))

int next()
AITACode(params=(Parameters(
	0: useSites={0,4,1,9,7} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={5},value={int[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={3},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=9,1)),
	3: Assignment(pc=10,DVar(useSites={4,5},value=an int,origin=3),BinaryExpr(pc=10,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={2},value=int = 1))),
	4: PutField(pc=12,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=15,DVar(useSites={9,11},value=an int,origin=5),ArrayLoad(pc=15,UVar(defSites={3},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=103]))),
	6: Assignment(pc=18,DVar(useSites={7},value=int = 4,origin=6),IntConst(pc=18,4)),
	7: Assignment(pc=19,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=19,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={6},value=int = 4)))),
	8: If(pc=22,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	9: Assignment(pc=27,DVar(useSites={11},value=an int,origin=9),VirtualFunctionCall(pc=27,java.util.regex.Pattern,isInterface=false,int peekPastWhitespace(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={5},value=an int)))),
	10: Nop(pc=30),
	11: ReturnValue(pc=32,UVar(defSites={9,5},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_7,BB_2}
	BB_1: BasicBlock(start=10,end=10) -> {BB_5}
	BB_2: BasicBlock(start=6,end=7) -> {BB_7,BB_6}
	BB_3: BasicBlock(start=9,end=9) -> {BB_7,BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=11,end=11) -> {BB_4}
	BB_6: BasicBlock(start=8,end=8) -> {BB_3,BB_5}
	BB_7: ExitNode(normalReturn=false)
))

int N()
AITACode(params=(Parameters(
	0: useSites={0,8,4,34,14,3,11,7,15,31} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Assignment(pc=4,DVar(useSites={2},value=int = 123,origin=1),IntConst(pc=4,123)),
	2: If(pc=6,UVar(defSites={0},value=an int),!=,UVar(defSites={1},value=int = 123),target=33),
	3: Assignment(pc=10,DVar(useSites={16,19},value=an int,origin=3),GetField(pc=10,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	4: Assignment(pc=15,DVar(useSites={6},value=an int,origin=4),VirtualFunctionCall(pc=15,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	5: Assignment(pc=18,DVar(useSites={6},value=int = 125,origin=5),IntConst(pc=18,125)),
	6: If(pc=20,UVar(defSites={4},value=an int),==,UVar(defSites={5},value=int = 125),target=13),
	7: Assignment(pc=24,DVar(useSites={9},value=an int,origin=7),GetField(pc=24,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	8: Assignment(pc=28,DVar(useSites={9},value=an int,origin=8),GetField(pc=28,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	9: If(pc=31,UVar(defSites={7},value=an int),<,UVar(defSites={8},value=an int),target=4),
	10: Assignment(pc=35,DVar(useSites={11},value=String("Unclosed character name escape sequence")[@35;refId=132],origin=10),StringConst(pc=35,Unclosed character name escape sequence)),
	11: Assignment(pc=38,DVar(useSites={12},value={_ <: java.util.regex.PatternSyntaxException, null}[↦38;refId=134],origin=11),VirtualFunctionCall(pc=38,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={10},value=String("Unclosed character name escape sequence")[@35;refId=132])))),
	12: Throw(pc=41,UVar(defSites={11},value={_ <: java.util.regex.PatternSyntaxException, null}[↦38;refId=134])),
	13: Assignment(pc=42,DVar(useSites={20,19,27},value=String(<initialization incomplete>)[@42;refId=109],origin=13),New(pc=42,java.lang.String)),
	14: Assignment(pc=47,DVar(useSites={19},value={int[], null}[↦47;refId=110],origin=14),GetField(pc=47,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	15: Assignment(pc=52,DVar(useSites={16},value=an int,origin=15),GetField(pc=52,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	16: Assignment(pc=56,DVar(useSites={18},value=an int,origin=16),BinaryExpr(pc=56,ComputationalTypeInt,UVar(defSites={15},value=an int),-,UVar(defSites={3},value=an int))),
	17: Assignment(pc=57,DVar(useSites={18},value=int = 1,origin=17),IntConst(pc=57,1)),
	18: Assignment(pc=58,DVar(useSites={19},value=an int,origin=18),BinaryExpr(pc=58,ComputationalTypeInt,UVar(defSites={16},value=an int),-,UVar(defSites={17},value=int = 1))),
	19: NonVirtualMethodCall(pc=59,java.lang.String,isInterface=false,void <init>(int[],int,int),UVar(defSites={13},value=String(<initialization incomplete>)[@42;refId=109]),(UVar(defSites={14},value={int[], null}[↦47;refId=110]),UVar(defSites={3},value=an int),UVar(defSites={18},value=an int))),
	20: Assignment(pc=64,DVar(useSites={21},value=an int,origin=20),StaticFunctionCall(pc=64,java.lang.Character,isInterface=false,int codePointOf(java.lang.String),(UVar(defSites={13},value=java.lang.String[↦42;refId=109])))),
	21: ReturnValue(pc=67,UVar(defSites={20},value=an int)),
	22: CaughtException(pc=68,java.lang.IllegalArgumentException,caused by={exception@20}),
	23: Assignment(pc=70,DVar(useSites={24,26},value=java.lang.StringBuilder[↦70;refId=114],origin=23),New(pc=70,java.lang.StringBuilder)),
	24: NonVirtualMethodCall(pc=74,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={23},value=java.lang.StringBuilder[↦70;refId=114]),()),
	25: Assignment(pc=77,DVar(useSites={26},value=String("Unknown character name [")[@77;refId=116],origin=25),StringConst(pc=77,Unknown character name [)),
	26: Assignment(pc=80,DVar(useSites={27},value={java.lang.StringBuilder, null}[↦80;refId=118],origin=26),VirtualFunctionCall(pc=80,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={23},value=java.lang.StringBuilder[↦70;refId=114]),(UVar(defSites={25},value=String("Unknown character name [")[@77;refId=116])))),
	27: Assignment(pc=84,DVar(useSites={29},value={java.lang.StringBuilder, null}[↦84;refId=121],origin=27),VirtualFunctionCall(pc=84,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={26},value={java.lang.StringBuilder, null}[↦80;refId=118]),(UVar(defSites={13},value=java.lang.String[↦42;refId=109])))),
	28: Assignment(pc=87,DVar(useSites={29},value=String("]")[@87;refId=122],origin=28),StringConst(pc=87,])),
	29: Assignment(pc=90,DVar(useSites={30},value={java.lang.StringBuilder, null}[↦90;refId=125],origin=29),VirtualFunctionCall(pc=90,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={27},value={java.lang.StringBuilder, null}[↦84;refId=121]),(UVar(defSites={28},value=String("]")[@87;refId=122])))),
	30: Assignment(pc=93,DVar(useSites={31},value={java.lang.String, null}[↦93;refId=128],origin=30),VirtualFunctionCall(pc=93,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={29},value={java.lang.StringBuilder, null}[↦90;refId=125]),())),
	31: Assignment(pc=96,DVar(useSites={32},value={_ <: java.util.regex.PatternSyntaxException, null}[↦96;refId=130],origin=31),VirtualFunctionCall(pc=96,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={30},value={java.lang.String, null}[↦93;refId=128])))),
	32: Throw(pc=99,UVar(defSites={31},value={_ <: java.util.regex.PatternSyntaxException, null}[↦96;refId=130])),
	33: Assignment(pc=101,DVar(useSites={34},value=String("Illegal character name escape sequence")[@101;refId=104],origin=33),StringConst(pc=101,Illegal character name escape sequence)),
	34: Assignment(pc=104,DVar(useSites={35},value={_ <: java.util.regex.PatternSyntaxException, null}[↦104;refId=106],origin=34),VirtualFunctionCall(pc=104,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={33},value=String("Illegal character name escape sequence")[@101;refId=104])))),
	35: Throw(pc=107,UVar(defSites={34},value={_ <: java.util.regex.PatternSyntaxException, null}[↦104;refId=106]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_16,BB_4}
	BB_10: BasicBlock(start=33,end=34) -> {BB_16,BB_14}
	BB_11: BasicBlock(start=22,end=24) -> {BB_16,BB_3}
	BB_12: BasicBlock(start=27,end=27) -> {BB_16,BB_e}
	BB_13: BasicBlock(start=3,end=3) -> {BB_15}
	BB_14: BasicBlock(start=35,end=35) -> {BB_16}
	BB_15: BasicBlock(start=4,end=4) -> {BB_16,BB_1}
	BB_16: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=6) -> {BB_5,BB_8}
	BB_2: BasicBlock(start=10,end=11) -> {BB_16,BB_7}
	BB_3: BasicBlock(start=25,end=26) -> {BB_16,BB_12}
	BB_4: BasicBlock(start=1,end=2) -> {BB_10,BB_13}
	BB_5: BasicBlock(start=13,end=19) -> {BB_16,BB_c}
	BB_6: BasicBlock(start=32,end=32) -> {BB_16}
	BB_7: BasicBlock(start=12,end=12) -> {BB_16}
	BB_8: BasicBlock(start=7,end=9) -> {BB_2,BB_15}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=31,end=31) -> {BB_16,BB_6}
	BB_b: BasicBlock(start=30,end=30) -> {BB_16,BB_a}
	BB_c: BasicBlock(start=20,end=20) -> {BB_16,BB_f,BB_d}
	BB_d: CatchNode([-1,21)=>22,java.lang.IllegalArgumentException) -> {BB_11}
	BB_e: BasicBlock(start=28,end=29) -> {BB_16,BB_b}
	BB_f: BasicBlock(start=21,end=21) -> {BB_9}
),exceptionHandlers=(
	ExceptionHandler([-1, 21) -> 22, java.lang.IllegalArgumentException)
))

java.util.regex.Pattern$CharPredicate CIRangeU(int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value={_ <: java.util.regex.Pattern$CIRangeU(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda, null}[↦2;refId=103],origin=0),StaticFunctionCall(pc=2,java.util.regex.Pattern$CIRangeU(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda,isInterface=false,java.util.regex.Pattern$CIRangeU(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda $newInstance(int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value=an int)))),
	1: ReturnValue(pc=7,UVar(defSites={0},value={_ <: java.util.regex.Pattern$CIRangeU(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda, null}[↦2;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate bitsOrSingle(java.util.regex.Pattern$BitClass,int)
AITACode(params=(Parameters(
	0: useSites={32,28,6,3} (origin=-1),
	1: useSites={29} (origin=-2),
	2: useSites={32,1,17,9,25,21,13,29,19,11,27,23,15} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 256,origin=0),IntConst(pc=1,256)),
	1: If(pc=4,UVar(defSites={-3},value=an int),>=,UVar(defSites={0},value=int = 256),target=32),
	2: Assignment(pc=8,DVar(useSites={3},value=int = 2,origin=2),IntConst(pc=8,2)),
	3: Assignment(pc=9,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=9,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={2},value=int = 2)))),
	4: If(pc=12,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=28),
	5: Assignment(pc=16,DVar(useSites={6},value=int = 64,origin=5),IntConst(pc=16,64)),
	6: Assignment(pc=18,DVar(useSites={7},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=18,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={5},value=int = 64)))),
	7: If(pc=21,UVar(defSites={6},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=28),
	8: Assignment(pc=25,DVar(useSites={9},value=int = 255,origin=8),IntConst(pc=25,255)),
	9: If(pc=28,UVar(defSites={-3},value=int ∈ [-2147483648,255]),==,UVar(defSites={8},value=int = 255),target=32),
	10: Assignment(pc=32,DVar(useSites={11},value=int = 181,origin=10),IntConst(pc=32,181)),
	11: If(pc=35,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={10},value=int = 181),target=32),
	12: Assignment(pc=39,DVar(useSites={13},value=int = 73,origin=12),IntConst(pc=39,73)),
	13: If(pc=41,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={12},value=int = 73),target=32),
	14: Assignment(pc=45,DVar(useSites={15},value=int = 105,origin=14),IntConst(pc=45,105)),
	15: If(pc=47,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={14},value=int = 105),target=32),
	16: Assignment(pc=51,DVar(useSites={17},value=int = 83,origin=16),IntConst(pc=51,83)),
	17: If(pc=53,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={16},value=int = 83),target=32),
	18: Assignment(pc=57,DVar(useSites={19},value=int = 115,origin=18),IntConst(pc=57,115)),
	19: If(pc=59,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={18},value=int = 115),target=32),
	20: Assignment(pc=63,DVar(useSites={21},value=int = 75,origin=20),IntConst(pc=63,75)),
	21: If(pc=65,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={20},value=int = 75),target=32),
	22: Assignment(pc=69,DVar(useSites={23},value=int = 107,origin=22),IntConst(pc=69,107)),
	23: If(pc=71,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={22},value=int = 107),target=32),
	24: Assignment(pc=75,DVar(useSites={25},value=int = 197,origin=24),IntConst(pc=75,197)),
	25: If(pc=78,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={24},value=int = 197),target=32),
	26: Assignment(pc=82,DVar(useSites={27},value=int = 229,origin=26),IntConst(pc=82,229)),
	27: If(pc=85,UVar(defSites={-3},value=int ∈ [-2147483648,254]),==,UVar(defSites={26},value=int = 229),target=32),
	28: Assignment(pc=91,DVar(useSites={29},value=an int,origin=28),GetField(pc=91,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	29: ExprStmt(pc=94,VirtualFunctionCall(pc=94,java.util.regex.Pattern$BitClass,isInterface=false,java.util.regex.Pattern$BitClass add(int,int),UVar(defSites={-2},value={java.util.regex.Pattern$BitClass, null}[↦-2;refId=103]),(UVar(defSites={-3},value=int ∈ [-2147483648,255]),UVar(defSites={28},value=an int)))),
	30: Assignment(pc=98,DVar(useSites={31},value=null[↦98],origin=30),NullExpr(pc=98)),
	31: ReturnValue(pc=99,UVar(defSites={30},value=null[↦98])),
	32: Assignment(pc=102,DVar(useSites={33},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦102;refId=107],origin=32),VirtualFunctionCall(pc=102,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate single(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={-3},value=int ∈ [0,2147483647])))),
	33: ReturnValue(pc=105,UVar(defSites={32},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦102;refId=107]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_7,BB_6}
	BB_10: BasicBlock(start=33,end=33) -> {BB_12}
	BB_11: BasicBlock(start=18,end=19) -> {BB_7,BB_5}
	BB_12: ExitNode(normalReturn=true)
	BB_13: BasicBlock(start=4,end=4) -> {BB_f,BB_1}
	BB_14: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=6) -> {BB_14,BB_a}
	BB_2: BasicBlock(start=10,end=11) -> {BB_7,BB_9}
	BB_3: BasicBlock(start=24,end=25) -> {BB_7,BB_c}
	BB_4: BasicBlock(start=14,end=15) -> {BB_7,BB_b}
	BB_5: BasicBlock(start=20,end=21) -> {BB_8,BB_7}
	BB_6: BasicBlock(start=2,end=3) -> {BB_14,BB_13}
	BB_7: BasicBlock(start=32,end=32) -> {BB_14,BB_10}
	BB_8: BasicBlock(start=22,end=23) -> {BB_7,BB_3}
	BB_9: BasicBlock(start=12,end=13) -> {BB_7,BB_4}
	BB_a: BasicBlock(start=7,end=7) -> {BB_d,BB_f}
	BB_b: BasicBlock(start=16,end=17) -> {BB_11,BB_7}
	BB_c: BasicBlock(start=26,end=27) -> {BB_f,BB_7}
	BB_d: BasicBlock(start=8,end=9) -> {BB_7,BB_2}
	BB_e: BasicBlock(start=30,end=31) -> {BB_12}
	BB_f: BasicBlock(start=28,end=29) -> {BB_14,BB_e}
))

java.util.regex.Pattern$BmpCharPredicate Single(int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Single(I)Ljava$util$regex$Pattern$BmpCharPredicate::1$Lambda, null}[↦1;refId=103],origin=0),StaticFunctionCall(pc=1,java.util.regex.Pattern$Single(I)Ljava$util$regex$Pattern$BmpCharPredicate::1$Lambda,isInterface=false,java.util.regex.Pattern$Single(I)Ljava$util$regex$Pattern$BmpCharPredicate::1$Lambda $newInstance(int),(UVar(defSites={-2},value=an int)))),
	1: ReturnValue(pc=6,UVar(defSites={0},value={_ <: java.util.regex.Pattern$Single(I)Ljava$util$regex$Pattern$BmpCharPredicate::1$Lambda, null}[↦1;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$BmpCharPredicate VertWS()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value={_ <: java.util.regex.Pattern$VertWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda, null}[↦0;refId=103],origin=0),StaticFunctionCall(pc=0,java.util.regex.Pattern$VertWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda,isInterface=false,java.util.regex.Pattern$VertWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda $newInstance(),())),
	1: ReturnValue(pc=5,UVar(defSites={0},value={_ <: java.util.regex.Pattern$VertWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda, null}[↦0;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int nextEscaped()
AITACode(params=(Parameters(
	0: useSites={0,4,1} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={5},value={int[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={3},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=9,1)),
	3: Assignment(pc=10,DVar(useSites={4,5},value=an int,origin=3),BinaryExpr(pc=10,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={2},value=int = 1))),
	4: PutField(pc=12,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=15,DVar(useSites={6},value=an int,origin=5),ArrayLoad(pc=15,UVar(defSites={3},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=103]))),
	6: ReturnValue(pc=18,UVar(defSites={5},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=6,end=6) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void mark(int)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={2} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: ArrayStore(pc=9,UVar(defSites={0},value={int[], null}[↦1;refId=103]),UVar(defSites={1},value=an int),UVar(defSites={-2},value=an int)),
	3: Return(pc=10)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=3,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate Range(int,int)
AITACode(params=(Parameters(
	1: useSites={8,6,3} (origin=-2),
	2: useSites={8,6,1,5} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 55296,origin=0),IntConst(pc=1,55296)),
	1: If(pc=4,UVar(defSites={-3},value=an int),<,UVar(defSites={0},value=int = 55296),target=6),
	2: Assignment(pc=8,DVar(useSites={3},value=int = 56319,origin=2),IntConst(pc=8,56319)),
	3: If(pc=11,UVar(defSites={-2},value=an int),<=,UVar(defSites={2},value=int = 56319),target=8),
	4: Assignment(pc=15,DVar(useSites={5},value=int = 65536,origin=4),IntConst(pc=15,65536)),
	5: If(pc=17,UVar(defSites={-3},value=int ∈ [55296,2147483647]),>=,UVar(defSites={4},value=int = 65536),target=8),
	6: Assignment(pc=22,DVar(useSites={7},value={_ <: java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::22$Lambda, null}[↦22;refId=103],origin=6),StaticFunctionCall(pc=22,java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::22$Lambda,isInterface=false,java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::22$Lambda $newInstance(int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value=int ∈ [-2147483648,65535])))),
	7: ReturnValue(pc=27,UVar(defSites={6},value={_ <: java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::22$Lambda, null}[↦22;refId=103])),
	8: Assignment(pc=30,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::30$Lambda, null}[↦30;refId=105],origin=8),StaticFunctionCall(pc=30,java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::30$Lambda,isInterface=false,java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::30$Lambda $newInstance(int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value=int ∈ [55296,2147483647])))),
	9: ReturnValue(pc=35,UVar(defSites={8},value={_ <: java.util.regex.Pattern$Range(II)Ljava$util$regex$Pattern$CharPredicate::30$Lambda, null}[↦30;refId=105]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1,BB_3}
	BB_1: BasicBlock(start=6,end=6) -> {BB_8,BB_4}
	BB_2: BasicBlock(start=9,end=9) -> {BB_5}
	BB_3: BasicBlock(start=2,end=3) -> {BB_6,BB_7}
	BB_4: BasicBlock(start=7,end=7) -> {BB_5}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=8,end=8) -> {BB_8,BB_2}
	BB_7: BasicBlock(start=4,end=5) -> {BB_1,BB_6}
	BB_8: ExitNode(normalReturn=false)
))

boolean lambda$SingleU$10(int,int)
AITACode(params=(Parameters(
	1: useSites={0,3} (origin=-2),
	2: useSites={0,1} (origin=-3)
)),stmts=(
	0: If(pc=2,UVar(defSites={-2},value=an int),==,UVar(defSites={-3},value=an int),target=4),
	1: Assignment(pc=7,DVar(useSites={2},value=an int,origin=1),StaticFunctionCall(pc=7,java.lang.Character,isInterface=false,int toUpperCase(int),(UVar(defSites={-3},value=an int)))),
	2: Assignment(pc=10,DVar(useSites={3},value=an int,origin=2),StaticFunctionCall(pc=10,java.lang.Character,isInterface=false,int toLowerCase(int),(UVar(defSites={1},value=an int)))),
	3: If(pc=13,UVar(defSites={-2},value=an int),!=,UVar(defSites={2},value=an int),target=6),
	4: Assignment(pc=16,DVar(useSites={7},value=int = 1,origin=4),IntConst(pc=16,1)),
	5: Goto(pc=17,target=7),
	6: Assignment(pc=20,DVar(useSites={7},value=int ∈ [0,1],origin=6),IntConst(pc=20,0)),
	7: ReturnValue(pc=21,UVar(defSites={4,6},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_7,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_8,BB_3}
	BB_2: BasicBlock(start=6,end=6) -> {BB_4}
	BB_3: BasicBlock(start=2,end=2) -> {BB_8,BB_5}
	BB_4: BasicBlock(start=7,end=7) -> {BB_6}
	BB_5: BasicBlock(start=3,end=3) -> {BB_7,BB_2}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=4,end=5) -> {BB_4}
	BB_8: ExitNode(normalReturn=false)
))

java.util.regex.Pattern compile(java.lang.String)
AITACode(params=(Parameters(
	1: useSites={2} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2,3},value=java.util.regex.Pattern[↦0;refId=103],origin=0),New(pc=0,java.util.regex.Pattern)),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 0,origin=1),IntConst(pc=5,0)),
	2: NonVirtualMethodCall(pc=6,java.util.regex.Pattern,isInterface=false,void <init>(java.lang.String,int),UVar(defSites={0},value=java.util.regex.Pattern[↦0;refId=103]),(UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),UVar(defSites={1},value=int = 0))),
	3: ReturnValue(pc=9,UVar(defSites={0},value=java.util.regex.Pattern[↦0;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=3,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int parsePastWhitespace(int)
AITACode(params=(Parameters(
	0: useSites={10,6,7,15} (origin=-1),
	1: useSites={0,4,14,17,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),StaticFunctionCall(pc=1,java.util.regex.ASCII,isInterface=false,boolean isSpace(int),(UVar(defSites={-2,11,15},value=an int)))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=8,DVar(useSites={3},value=int = 35,origin=2),IntConst(pc=8,35)),
	3: If(pc=10,UVar(defSites={-2,11,15},value=an int),!=,UVar(defSites={2},value=int = 35),target=17),
	4: Assignment(pc=14,DVar(useSites={5},value=int ∈ [0,1],origin=4),StaticFunctionCall(pc=14,java.util.regex.ASCII,isInterface=false,boolean isSpace(int),(UVar(defSites={-2,11,15},value=an int)))),
	5: If(pc=17,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=13),
	6: Assignment(pc=21,DVar(useSites={11},value={int[], null}[↦21;refId=105],origin=6),GetField(pc=21,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	7: Assignment(pc=26,DVar(useSites={9,11},value=an int,origin=7),GetField(pc=26,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	8: Assignment(pc=30,DVar(useSites={9},value=int = 1,origin=8),IntConst(pc=30,1)),
	9: Assignment(pc=31,DVar(useSites={10},value=an int,origin=9),BinaryExpr(pc=31,ComputationalTypeInt,UVar(defSites={7},value=an int),+,UVar(defSites={8},value=int = 1))),
	10: PutField(pc=32,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={9},value=an int)),
	11: Assignment(pc=35,DVar(useSites={0,4,14,17,3},value=an int,origin=11),ArrayLoad(pc=35,UVar(defSites={7},value=an int),UVar(defSites={6},value={int[], null}[↦21;refId=105]))),
	12: Goto(pc=37,target=4),
	13: Assignment(pc=41,DVar(useSites={14},value=int = 35,origin=13),IntConst(pc=41,35)),
	14: If(pc=43,UVar(defSites={-2,11,15},value=an int),!=,UVar(defSites={13},value=int = 35),target=0),
	15: Assignment(pc=47,DVar(useSites={0,4,14,17,3},value=an int,origin=15),VirtualFunctionCall(pc=47,java.util.regex.Pattern,isInterface=false,int parsePastLine(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	16: Goto(pc=51,target=0),
	17: ReturnValue(pc=55,UVar(defSites={-2,11,15},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_4,BB_3}
	BB_2: BasicBlock(start=1,end=1) -> {BB_b,BB_5}
	BB_3: BasicBlock(start=6,end=11) -> {BB_c,BB_7}
	BB_4: BasicBlock(start=13,end=14) -> {BB_0,BB_a}
	BB_5: BasicBlock(start=2,end=3) -> {BB_6,BB_b}
	BB_6: BasicBlock(start=17,end=17) -> {BB_8}
	BB_7: BasicBlock(start=12,end=12) -> {BB_b}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=16,end=16) -> {BB_0}
	BB_a: BasicBlock(start=15,end=15) -> {BB_c,BB_9}
	BB_b: BasicBlock(start=4,end=4) -> {BB_c,BB_1}
	BB_c: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$BmpCharPredicate HorizWS()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value={_ <: java.util.regex.Pattern$HorizWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda, null}[↦0;refId=103],origin=0),StaticFunctionCall(pc=0,java.util.regex.Pattern$HorizWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda,isInterface=false,java.util.regex.Pattern$HorizWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda $newInstance(),())),
	1: ReturnValue(pc=5,UVar(defSites={0},value={_ <: java.util.regex.Pattern$HorizWS()Ljava$util$regex$Pattern$BmpCharPredicate::0$Lambda, null}[↦0;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int countChars(java.lang.CharSequence,int,int)
AITACode(params=(Parameters(
	1: useSites={52,10,58,25,5,29,3} (origin=-2),
	2: useSites={64,16,40,24,4,44,2,22,17,49,25,5,35,51,39,15} (origin=-3),
	3: useSites={1,11,23,47} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 1,origin=0),IntConst(pc=1,1)),
	1: If(pc=2,UVar(defSites={-4},value=an int),!=,UVar(defSites={0},value=int = 1),target=10),
	2: If(pc=6,UVar(defSites={-3},value=an int),<,IntConst(pc=-333,0),target=10),
	3: Assignment(pc=11,DVar(useSites={4},value=an int,origin=3),VirtualFunctionCall(pc=11,java.lang.CharSequence,isInterface=true,int length(),UVar(defSites={-2},value={_ <: java.lang.CharSequence, null}[↦-1;refId=102]),())),
	4: If(pc=16,UVar(defSites={-3},value=int ∈ [0,2147483647]),>=,UVar(defSites={3},value=an int),target=10),
	5: Assignment(pc=21,DVar(useSites={6},value=int ∈ [0,65535],origin=5),VirtualFunctionCall(pc=21,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-2},value=_ <: java.lang.CharSequence[↦-1;refId=102]),(UVar(defSites={-3},value=int ∈ [0,2147483646])))),
	6: Assignment(pc=26,DVar(useSites={7},value=int ∈ [0,1],origin=6),StaticFunctionCall(pc=26,java.lang.Character,isInterface=false,boolean isHighSurrogate(char),(UVar(defSites={5},value=int ∈ [0,65535])))),
	7: If(pc=29,UVar(defSites={6},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=10),
	8: Assignment(pc=32,DVar(useSites={9},value=int = 1,origin=8),IntConst(pc=32,1)),
	9: ReturnValue(pc=33,UVar(defSites={8},value=int = 1)),
	10: Assignment(pc=35,DVar(useSites={40,28,22,14,17},value=an int,origin=10),VirtualFunctionCall(pc=35,java.lang.CharSequence,isInterface=true,int length(),UVar(defSites={-2},value={_ <: java.lang.CharSequence, null}[↦-1;refId=102]),())),
	11: If(pc=45,UVar(defSites={-4},value=an int),<,IntConst(pc=-333,0),target=37),
	12: Assignment(pc=48,DVar(useSites={13},value=int ∈ [0,1],origin=12),GetStatic(pc=48,java.util.regex.Pattern,$assertionsDisabled,boolean)),
	13: If(pc=51,UVar(defSites={12},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=21),
	14: If(pc=55,UVar(defSites={10},value=an int),!=,IntConst(pc=-333,0),target=16),
	15: If(pc=59,UVar(defSites={-3},value=an int),==,IntConst(pc=-333,0),target=21),
	16: If(pc=63,UVar(defSites={-3},value=an int),<,IntConst(pc=-333,0),target=18),
	17: If(pc=68,UVar(defSites={-3},value=int ∈ [0,2147483647]),<,UVar(defSites={10},value=an int),target=21),
	18: Assignment(pc=71,DVar(useSites={20,19},value=java.lang.AssertionError[↦71;refId=115],origin=18),New(pc=71,java.lang.AssertionError)),
	19: NonVirtualMethodCall(pc=75,java.lang.AssertionError,isInterface=false,void <init>(),UVar(defSites={18},value=java.lang.AssertionError[↦71;refId=115]),()),
	20: Throw(pc=78,UVar(defSites={18},value=java.lang.AssertionError[↦71;refId=115])),
	21: Assignment(pc=79,DVar(useSites={33,23},value=int = 0,origin=21),IntConst(pc=79,0)),
	22: If(pc=85,UVar(defSites={32,24,-3},value=an int),>=,UVar(defSites={10},value=an int),target=35),
	23: If(pc=91,UVar(defSites={33,21},value=an int),>=,UVar(defSites={-4},value=int ∈ [0,2147483647]),target=35),
	24: Assignment(pc=97,DVar(useSites={32,28,22,25,29,35},value=int ∈ [-2147483647,2147483647],origin=24),BinaryExpr(pc=97,ComputationalTypeInt,UVar(defSites={32,24,-3},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=97,1))),
	25: Assignment(pc=100,DVar(useSites={26},value=int ∈ [0,65535],origin=25),VirtualFunctionCall(pc=100,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-2},value=_ <: java.lang.CharSequence[↦-1;refId=102]),(UVar(defSites={32,24,-3},value=int ∈ [-2147483648,2147483646])))),
	26: Assignment(pc=105,DVar(useSites={27},value=int ∈ [0,1],origin=26),StaticFunctionCall(pc=105,java.lang.Character,isInterface=false,boolean isHighSurrogate(char),(UVar(defSites={25},value=int ∈ [0,65535])))),
	27: If(pc=108,UVar(defSites={26},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=33),
	28: If(pc=114,UVar(defSites={24},value=int ∈ [-2147483647,2147483647]),>=,UVar(defSites={10},value=int ∈ [-2147483647,2147483647]),target=33),
	29: Assignment(pc=120,DVar(useSites={30},value=int ∈ [0,65535],origin=29),VirtualFunctionCall(pc=120,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-2},value=_ <: java.lang.CharSequence[↦-1;refId=102]),(UVar(defSites={24},value=int ∈ [-2147483647,2147483646])))),
	30: Assignment(pc=125,DVar(useSites={31},value=int ∈ [0,1],origin=30),StaticFunctionCall(pc=125,java.lang.Character,isInterface=false,boolean isLowSurrogate(char),(UVar(defSites={29},value=int ∈ [0,65535])))),
	31: If(pc=128,UVar(defSites={30},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=33),
	32: Assignment(pc=131,DVar(useSites={24,22,25,35},value=int ∈ [-2147483647,2147483647],origin=32),BinaryExpr(pc=131,ComputationalTypeInt,UVar(defSites={24},value=int ∈ [-2147483647,2147483646]),+,IntConst(pc=131,1))),
	33: Assignment(pc=134,DVar(useSites={34,23},value=an int,origin=33),BinaryExpr(pc=134,ComputationalTypeInt,UVar(defSites={33,21},value=an int),+,IntConst(pc=134,1))),
	34: Goto(pc=137,target=22),
	35: Assignment(pc=143,DVar(useSites={36},value=an int,origin=35),BinaryExpr(pc=143,ComputationalTypeInt,UVar(defSites={32,24,-3},value=an int),-,UVar(defSites={-3},value=an int))),
	36: ReturnValue(pc=144,UVar(defSites={35},value=an int)),
	37: Assignment(pc=145,DVar(useSites={38},value=int ∈ [0,1],origin=37),GetStatic(pc=145,java.util.regex.Pattern,$assertionsDisabled,boolean)),
	38: If(pc=148,UVar(defSites={37},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=44),
	39: If(pc=152,UVar(defSites={-3},value=an int),<,IntConst(pc=-333,0),target=41),
	40: If(pc=157,UVar(defSites={-3},value=int ∈ [0,2147483647]),<=,UVar(defSites={10},value=an int),target=44),
	41: Assignment(pc=160,DVar(useSites={42,43},value=java.lang.AssertionError[↦160;refId=109],origin=41),New(pc=160,java.lang.AssertionError)),
	42: NonVirtualMethodCall(pc=164,java.lang.AssertionError,isInterface=false,void <init>(),UVar(defSites={41},value=java.lang.AssertionError[↦160;refId=109]),()),
	43: Throw(pc=167,UVar(defSites={41},value=java.lang.AssertionError[↦160;refId=109])),
	44: If(pc=169,UVar(defSites={-3},value=an int),!=,IntConst(pc=-333,0),target=47),
	45: Assignment(pc=172,DVar(useSites={46},value=int = 0,origin=45),IntConst(pc=172,0)),
	46: ReturnValue(pc=173,UVar(defSites={45},value=int = 0)),
	47: Assignment(pc=175,DVar(useSites={50},value=an int,origin=47),PrefixExpr(pc=175,ComputationalTypeInt,-,UVar(defSites={-4},value=int ∈ [-2147483648,-1]))),
	48: Assignment(pc=178,DVar(useSites={50,62},value=int = 0,origin=48),IntConst(pc=178,0)),
	49: If(pc=183,UVar(defSites={61,-3,51},value=an int),<=,IntConst(pc=-333,0),target=64),
	50: If(pc=190,UVar(defSites={48,62},value=an int),>=,UVar(defSites={47},value=an int),target=64),
	51: Assignment(pc=194,DVar(useSites={64,52,49,57,61,55},value=int ∈ [0,2147483646],origin=51),BinaryExpr(pc=194,ComputationalTypeInt,UVar(defSites={61,-3,51},value=int ∈ [1,2147483647]),+,IntConst(pc=194,-1))),
	52: Assignment(pc=199,DVar(useSites={53},value=int ∈ [0,65535],origin=52),VirtualFunctionCall(pc=199,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-2},value=_ <: java.lang.CharSequence[↦-1;refId=102]),(UVar(defSites={51},value=int ∈ [0,2147483646])))),
	53: Assignment(pc=204,DVar(useSites={54},value=int ∈ [0,1],origin=53),StaticFunctionCall(pc=204,java.lang.Character,isInterface=false,boolean isLowSurrogate(char),(UVar(defSites={52},value=int ∈ [0,65535])))),
	54: If(pc=207,UVar(defSites={53},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=62),
	55: If(pc=212,UVar(defSites={51},value=int ∈ [0,2147483646]),<=,IntConst(pc=-333,0),target=62),
	56: Assignment(pc=218,DVar(useSites={57},value=int = 1,origin=56),IntConst(pc=218,1)),
	57: Assignment(pc=219,DVar(useSites={58},value=int ∈ [0,2147483645],origin=57),BinaryExpr(pc=219,ComputationalTypeInt,UVar(defSites={51},value=int ∈ [1,2147483646]),-,UVar(defSites={56},value=int = 1))),
	58: Assignment(pc=220,DVar(useSites={59},value=int ∈ [0,65535],origin=58),VirtualFunctionCall(pc=220,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-2},value=_ <: java.lang.CharSequence[↦-1;refId=102]),(UVar(defSites={57},value=int ∈ [0,2147483645])))),
	59: Assignment(pc=225,DVar(useSites={60},value=int ∈ [0,1],origin=59),StaticFunctionCall(pc=225,java.lang.Character,isInterface=false,boolean isHighSurrogate(char),(UVar(defSites={58},value=int ∈ [0,65535])))),
	60: If(pc=228,UVar(defSites={59},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=62),
	61: Assignment(pc=231,DVar(useSites={64,49,51},value=int ∈ [0,2147483646],origin=61),BinaryExpr(pc=231,ComputationalTypeInt,UVar(defSites={51},value=int ∈ [1,2147483646]),+,IntConst(pc=231,-1))),
	62: Assignment(pc=234,DVar(useSites={50,63},value=an int,origin=62),BinaryExpr(pc=234,ComputationalTypeInt,UVar(defSites={48,62},value=an int),+,IntConst(pc=234,1))),
	63: Goto(pc=237,target=49),
	64: Assignment(pc=243,DVar(useSites={65},value=an int,origin=64),BinaryExpr(pc=243,ComputationalTypeInt,UVar(defSites={-3},value=an int),-,UVar(defSites={61,-3,51},value=an int))),
	65: ReturnValue(pc=244,UVar(defSites={64},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_8,BB_6}
	BB_10: BasicBlock(start=28,end=28) -> {BB_12,BB_d}
	BB_11: BasicBlock(start=21,end=21) -> {BB_17}
	BB_12: BasicBlock(start=33,end=34) -> {BB_17}
	BB_13: BasicBlock(start=32,end=32) -> {BB_12}
	BB_14: BasicBlock(start=45,end=46) -> {BB_23}
	BB_15: BasicBlock(start=64,end=65) -> {BB_23}
	BB_16: BasicBlock(start=17,end=17) -> {BB_22,BB_11}
	BB_17: BasicBlock(start=22,end=22) -> {BB_2c,BB_21}
	BB_18: BasicBlock(start=44,end=44) -> {BB_14,BB_31}
	BB_19: BasicBlock(start=59,end=59) -> {BB_30,BB_f}
	BB_1: BasicBlock(start=5,end=5) -> {BB_30,BB_e}
	BB_1a: BasicBlock(start=27,end=27) -> {BB_12,BB_10}
	BB_1b: BasicBlock(start=12,end=13) -> {BB_2,BB_11}
	BB_1c: BasicBlock(start=54,end=54) -> {BB_2b,BB_33}
	BB_1d: BasicBlock(start=49,end=49) -> {BB_15,BB_24}
	BB_1e: BasicBlock(start=7,end=7) -> {BB_7,BB_8}
	BB_1f: BasicBlock(start=39,end=39) -> {BB_5,BB_29}
	BB_20: BasicBlock(start=3,end=3) -> {BB_30,BB_2f}
	BB_21: BasicBlock(start=35,end=36) -> {BB_23}
	BB_22: BasicBlock(start=18,end=19) -> {BB_30,BB_c}
	BB_23: ExitNode(normalReturn=true)
	BB_24: BasicBlock(start=50,end=50) -> {BB_15,BB_2e}
	BB_25: BasicBlock(start=16,end=16) -> {BB_16,BB_22}
	BB_26: BasicBlock(start=31,end=31) -> {BB_12,BB_13}
	BB_27: BasicBlock(start=11,end=11) -> {BB_1b,BB_b}
	BB_28: BasicBlock(start=43,end=43) -> {BB_30}
	BB_29: BasicBlock(start=40,end=40) -> {BB_5,BB_18}
	BB_2: BasicBlock(start=14,end=14) -> {BB_32,BB_25}
	BB_2a: BasicBlock(start=26,end=26) -> {BB_30,BB_1a}
	BB_2b: BasicBlock(start=55,end=55) -> {BB_33,BB_9}
	BB_2c: BasicBlock(start=23,end=23) -> {BB_21,BB_a}
	BB_2d: BasicBlock(start=30,end=30) -> {BB_30,BB_26}
	BB_2e: BasicBlock(start=51,end=52) -> {BB_30,BB_4}
	BB_2f: BasicBlock(start=4,end=4) -> {BB_8,BB_1}
	BB_30: ExitNode(normalReturn=false)
	BB_31: BasicBlock(start=47,end=48) -> {BB_1d}
	BB_32: BasicBlock(start=15,end=15) -> {BB_25,BB_11}
	BB_33: BasicBlock(start=62,end=63) -> {BB_1d}
	BB_3: BasicBlock(start=61,end=61) -> {BB_33}
	BB_4: BasicBlock(start=53,end=53) -> {BB_30,BB_1c}
	BB_5: BasicBlock(start=41,end=42) -> {BB_30,BB_28}
	BB_6: BasicBlock(start=2,end=2) -> {BB_8,BB_20}
	BB_7: BasicBlock(start=8,end=9) -> {BB_23}
	BB_8: BasicBlock(start=10,end=10) -> {BB_30,BB_27}
	BB_9: BasicBlock(start=56,end=58) -> {BB_30,BB_19}
	BB_a: BasicBlock(start=24,end=25) -> {BB_30,BB_2a}
	BB_b: BasicBlock(start=37,end=38) -> {BB_18,BB_1f}
	BB_c: BasicBlock(start=20,end=20) -> {BB_30}
	BB_d: BasicBlock(start=29,end=29) -> {BB_30,BB_2d}
	BB_e: BasicBlock(start=6,end=6) -> {BB_30,BB_1e}
	BB_f: BasicBlock(start=60,end=60) -> {BB_33,BB_3}
))

void lambda$normalizeSlice$0(java.lang.StringBuilder,java.lang.String)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value={java.lang.StringBuilder, null}[↦2;refId=106],origin=0),VirtualFunctionCall(pc=2,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={-2},value={java.lang.StringBuilder, null}[↦-1;refId=102]),(UVar(defSites={-3},value={java.lang.String, null}[↦-2;refId=103])))),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 124,origin=1),IntConst(pc=5,124)),
	2: ExprStmt(pc=7,VirtualFunctionCall(pc=7,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={0},value={java.lang.StringBuilder, null}[↦2;refId=106]),(UVar(defSites={1},value=int = 124)))),
	3: Return(pc=11)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

int escape(boolean,boolean,boolean)
AITACode(params=(Parameters(
	0: useSites={0,32,160,224,16,112,240,8,264,200,40,296,168,24,280,152,88,184,248,132,196,164,100,228,84,212,52,308,116,268,44,284,60,2,66,114,266,42,298,170,106,26,282,90,58,186,198,38,294,230,86,182,118,142,78,238,62,289,97,273,209,177,9,137,73,297,233,89,313,185,37,101,149,213,117,205,301,173,61,125,259,163,99,83,211,243,267,43,283,155,199,111} (origin=-1),
	1: useSites={48,304,4,12,204,98,129,265,41,281,121,69,197,19,147,115,59,295,87,183} (origin=-2),
	2: useSites={104,20,148,76,130,194,226,122,70,278,30,94,257,49,305,5,13,55,175,287} (origin=-3),
	3: useSites={275} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1,7,311},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int skip(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Switch(pc=8,defaultTarget=311,index=UVar(defSites={0},value=an int),npairs=(IntIntPair(48,2),IntIntPair(49,4),IntIntPair(50,4),IntIntPair(51,4),IntIntPair(52,4),IntIntPair(53,4),IntIntPair(54,4),IntIntPair(55,4),IntIntPair(56,4),IntIntPair(57,4),IntIntPair(58,311),IntIntPair(59,311),IntIntPair(60,311),IntIntPair(61,311),IntIntPair(62,311),IntIntPair(63,311),IntIntPair(64,311),IntIntPair(65,12),IntIntPair(66,19),IntIntPair(67,29),IntIntPair(68,30),IntIntPair(69,47),IntIntPair(70,47),IntIntPair(71,48),IntIntPair(72,55),IntIntPair(73,65),IntIntPair(74,65),IntIntPair(75,65),IntIntPair(76,65),IntIntPair(77,65),IntIntPair(78,66),IntIntPair(79,68),IntIntPair(80,68),IntIntPair(81,68),IntIntPair(82,69),IntIntPair(83,76),IntIntPair(84,93),IntIntPair(85,93),IntIntPair(86,94),IntIntPair(87,104),IntIntPair(88,121),IntIntPair(89,128),IntIntPair(90,129),IntIntPair(91,311),IntIntPair(92,311),IntIntPair(93,311),IntIntPair(94,311),IntIntPair(95,311),IntIntPair(96,311),IntIntPair(97,145),IntIntPair(98,147),IntIntPair(99,173),IntIntPair(100,175),IntIntPair(101,189),IntIntPair(102,191),IntIntPair(103,193),IntIntPair(104,194),IntIntPair(105,203),IntIntPair(106,203),IntIntPair(107,204),IntIntPair(108,251),IntIntPair(109,251),IntIntPair(110,252),IntIntPair(111,254),IntIntPair(112,254),IntIntPair(113,254),IntIntPair(114,255),IntIntPair(115,257),IntIntPair(116,271),IntIntPair(117,273),IntIntPair(118,275),IntIntPair(119,287),IntIntPair(120,301),IntIntPair(121,303),IntIntPair(122,304)),
	2: Assignment(pc=325,DVar(useSites={3},value=an int,origin=2),VirtualFunctionCall(pc=325,java.util.regex.Pattern,isInterface=false,int o(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	3: ReturnValue(pc=328,UVar(defSites={2},value=an int)),
	4: If(pc=330,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	5: If(pc=337,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=10),
	6: Assignment(pc=344,DVar(useSites={7},value=int = 48,origin=6),IntConst(pc=344,48)),
	7: Assignment(pc=346,DVar(useSites={8},value=int = 9,origin=7),BinaryExpr(pc=346,ComputationalTypeInt,UVar(defSites={0},value=int = 57),-,UVar(defSites={6},value=int = 48))),
	8: Assignment(pc=347,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦347;refId=250],origin=8),VirtualFunctionCall(pc=347,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node ref(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={7},value=int = 9)))),
	9: PutField(pc=350,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦347;refId=250])),
	10: Assignment(pc=353,DVar(useSites={11},value=int = -1,origin=10),IntConst(pc=353,-1)),
	11: ReturnValue(pc=354,UVar(defSites={10},value=int = -1)),
	12: If(pc=356,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	13: If(pc=363,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=17),
	14: Assignment(pc=367,DVar(useSites={16,15},value=java.util.regex.Pattern$Begin[↦367;refId=247],origin=14),New(pc=367,java.util.regex.Pattern$Begin)),
	15: NonVirtualMethodCall(pc=371,java.util.regex.Pattern$Begin,isInterface=false,void <init>(),UVar(defSites={14},value=java.util.regex.Pattern$Begin[↦367;refId=247]),()),
	16: PutField(pc=374,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={14},value=java.util.regex.Pattern$Begin[↦367;refId=247])),
	17: Assignment(pc=377,DVar(useSites={18},value=int = -1,origin=17),IntConst(pc=377,-1)),
	18: ReturnValue(pc=378,UVar(defSites={17},value=int = -1)),
	19: If(pc=380,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	20: If(pc=387,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=27),
	21: Assignment(pc=391,DVar(useSites={26,25},value=java.util.regex.Pattern$Bound[↦391;refId=244],origin=21),New(pc=391,java.util.regex.Pattern$Bound)),
	22: Assignment(pc=395,DVar(useSites={25},value=an int,origin=22),GetStatic(pc=395,java.util.regex.Pattern$Bound,NONE,int)),
	23: Assignment(pc=399,DVar(useSites={24},value=int = 256,origin=23),IntConst(pc=399,256)),
	24: Assignment(pc=402,DVar(useSites={25},value=int ∈ [0,1],origin=24),VirtualFunctionCall(pc=402,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={23},value=int = 256)))),
	25: NonVirtualMethodCall(pc=405,java.util.regex.Pattern$Bound,isInterface=false,void <init>(int,boolean),UVar(defSites={21},value=java.util.regex.Pattern$Bound[↦391;refId=244]),(UVar(defSites={22},value=an int),UVar(defSites={24},value=int ∈ [0,1]))),
	26: PutField(pc=408,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={21},value=java.util.regex.Pattern$Bound[↦391;refId=244])),
	27: Assignment(pc=411,DVar(useSites={28},value=int = -1,origin=27),IntConst(pc=411,-1)),
	28: ReturnValue(pc=412,UVar(defSites={27},value=int = -1)),
	29: Goto(pc=413,target=312),
	30: If(pc=417,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=45),
	31: Assignment(pc=422,DVar(useSites={32},value=int = 256,origin=31),IntConst(pc=422,256)),
	32: Assignment(pc=425,DVar(useSites={33},value=int ∈ [0,1],origin=32),VirtualFunctionCall(pc=425,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={31},value=int = 256)))),
	33: If(pc=428,UVar(defSites={32},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=36),
	34: Assignment(pc=431,DVar(useSites={37},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦431;refId=240],origin=34),StaticFunctionCall(pc=431,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate DIGIT(),())),
	35: Goto(pc=434,target=37),
	36: Assignment(pc=437,DVar(useSites={37},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=243; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦431;refId=240], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦437;refId=242]»],origin=36),StaticFunctionCall(pc=437,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$BmpCharPredicate ASCII_DIGIT(),())),
	37: PutField(pc=440,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={36,34},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=243; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦431;refId=240], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦437;refId=242]»])),
	38: Assignment(pc=445,DVar(useSites={39},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦445;refId=282],origin=38),GetField(pc=445,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	39: Assignment(pc=448,DVar(useSites={40},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦448;refId=285],origin=39),VirtualFunctionCall(pc=448,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate negate(),UVar(defSites={38},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦445;refId=282]),())),
	40: PutField(pc=453,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={39},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦448;refId=285])),
	41: If(pc=457,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=45),
	42: Assignment(pc=463,DVar(useSites={43},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦463;refId=286],origin=42),GetField(pc=463,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	43: Assignment(pc=466,DVar(useSites={44},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦466;refId=288],origin=43),VirtualFunctionCall(pc=466,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={42},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦463;refId=286])))),
	44: PutField(pc=469,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={43},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦466;refId=288])),
	45: Assignment(pc=472,DVar(useSites={46},value=int = -1,origin=45),IntConst(pc=472,-1)),
	46: ReturnValue(pc=473,UVar(defSites={45},value=int = -1)),
	47: Goto(pc=474,target=312),
	48: If(pc=478,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	49: If(pc=485,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=53),
	50: Assignment(pc=489,DVar(useSites={52,51},value=java.util.regex.Pattern$LastMatch[↦489;refId=236],origin=50),New(pc=489,java.util.regex.Pattern$LastMatch)),
	51: NonVirtualMethodCall(pc=493,java.util.regex.Pattern$LastMatch,isInterface=false,void <init>(),UVar(defSites={50},value=java.util.regex.Pattern$LastMatch[↦489;refId=236]),()),
	52: PutField(pc=496,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={50},value=java.util.regex.Pattern$LastMatch[↦489;refId=236])),
	53: Assignment(pc=499,DVar(useSites={54},value=int = -1,origin=53),IntConst(pc=499,-1)),
	54: ReturnValue(pc=500,UVar(defSites={53},value=int = -1)),
	55: If(pc=502,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=63),
	56: Assignment(pc=506,DVar(useSites={57},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦506;refId=229],origin=56),StaticFunctionCall(pc=506,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$BmpCharPredicate HorizWS(),())),
	57: Assignment(pc=509,DVar(useSites={58},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦509;refId=232],origin=57),VirtualFunctionCall(pc=509,java.util.regex.Pattern$BmpCharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate negate(),UVar(defSites={56},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦506;refId=229]),())),
	58: PutField(pc=514,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={57},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦509;refId=232])),
	59: If(pc=518,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=63),
	60: Assignment(pc=524,DVar(useSites={61},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦524;refId=233],origin=60),GetField(pc=524,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	61: Assignment(pc=527,DVar(useSites={62},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦527;refId=235],origin=61),VirtualFunctionCall(pc=527,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={60},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦524;refId=233])))),
	62: PutField(pc=530,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={61},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦527;refId=235])),
	63: Assignment(pc=533,DVar(useSites={64},value=int = -1,origin=63),IntConst(pc=533,-1)),
	64: ReturnValue(pc=534,UVar(defSites={63},value=int = -1)),
	65: Goto(pc=535,target=312),
	66: Assignment(pc=539,DVar(useSites={67},value=an int,origin=66),VirtualFunctionCall(pc=539,java.util.regex.Pattern,isInterface=false,int N(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	67: ReturnValue(pc=542,UVar(defSites={66},value=an int)),
	68: Goto(pc=543,target=312),
	69: If(pc=547,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	70: If(pc=554,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=74),
	71: Assignment(pc=558,DVar(useSites={72,73},value=java.util.regex.Pattern$LineEnding[↦558;refId=225],origin=71),New(pc=558,java.util.regex.Pattern$LineEnding)),
	72: NonVirtualMethodCall(pc=562,java.util.regex.Pattern$LineEnding,isInterface=false,void <init>(),UVar(defSites={71},value=java.util.regex.Pattern$LineEnding[↦558;refId=225]),()),
	73: PutField(pc=565,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={71},value=java.util.regex.Pattern$LineEnding[↦558;refId=225])),
	74: Assignment(pc=568,DVar(useSites={75},value=int = -1,origin=74),IntConst(pc=568,-1)),
	75: ReturnValue(pc=569,UVar(defSites={74},value=int = -1)),
	76: If(pc=571,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=91),
	77: Assignment(pc=576,DVar(useSites={78},value=int = 256,origin=77),IntConst(pc=576,256)),
	78: Assignment(pc=579,DVar(useSites={79},value=int ∈ [0,1],origin=78),VirtualFunctionCall(pc=579,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={77},value=int = 256)))),
	79: If(pc=582,UVar(defSites={78},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=82),
	80: Assignment(pc=585,DVar(useSites={83},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦585;refId=221],origin=80),StaticFunctionCall(pc=585,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate WHITE_SPACE(),())),
	81: Goto(pc=588,target=83),
	82: Assignment(pc=591,DVar(useSites={83},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=224; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦585;refId=221], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦591;refId=223]»],origin=82),StaticFunctionCall(pc=591,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$BmpCharPredicate ASCII_SPACE(),())),
	83: PutField(pc=594,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={80,82},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=224; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦585;refId=221], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦591;refId=223]»])),
	84: Assignment(pc=599,DVar(useSites={85},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦599;refId=275],origin=84),GetField(pc=599,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	85: Assignment(pc=602,DVar(useSites={86},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦602;refId=278],origin=85),VirtualFunctionCall(pc=602,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate negate(),UVar(defSites={84},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦599;refId=275]),())),
	86: PutField(pc=607,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={85},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦602;refId=278])),
	87: If(pc=611,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=91),
	88: Assignment(pc=617,DVar(useSites={89},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦617;refId=279],origin=88),GetField(pc=617,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	89: Assignment(pc=620,DVar(useSites={90},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦620;refId=281],origin=89),VirtualFunctionCall(pc=620,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={88},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦617;refId=279])))),
	90: PutField(pc=623,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={89},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦620;refId=281])),
	91: Assignment(pc=626,DVar(useSites={92},value=int = -1,origin=91),IntConst(pc=626,-1)),
	92: ReturnValue(pc=627,UVar(defSites={91},value=int = -1)),
	93: Goto(pc=628,target=312),
	94: If(pc=632,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=102),
	95: Assignment(pc=636,DVar(useSites={96},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦636;refId=212],origin=95),StaticFunctionCall(pc=636,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$BmpCharPredicate VertWS(),())),
	96: Assignment(pc=639,DVar(useSites={97},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦639;refId=215],origin=96),VirtualFunctionCall(pc=639,java.util.regex.Pattern$BmpCharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate negate(),UVar(defSites={95},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦636;refId=212]),())),
	97: PutField(pc=644,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={96},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦639;refId=215])),
	98: If(pc=648,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=102),
	99: Assignment(pc=654,DVar(useSites={100},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦654;refId=216],origin=99),GetField(pc=654,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	100: Assignment(pc=657,DVar(useSites={101},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦657;refId=218],origin=100),VirtualFunctionCall(pc=657,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={99},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦654;refId=216])))),
	101: PutField(pc=660,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={100},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦657;refId=218])),
	102: Assignment(pc=663,DVar(useSites={103},value=int = -1,origin=102),IntConst(pc=663,-1)),
	103: ReturnValue(pc=664,UVar(defSites={102},value=int = -1)),
	104: If(pc=666,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=119),
	105: Assignment(pc=671,DVar(useSites={106},value=int = 256,origin=105),IntConst(pc=671,256)),
	106: Assignment(pc=674,DVar(useSites={107},value=int ∈ [0,1],origin=106),VirtualFunctionCall(pc=674,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={105},value=int = 256)))),
	107: If(pc=677,UVar(defSites={106},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=110),
	108: Assignment(pc=680,DVar(useSites={111},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦680;refId=207],origin=108),StaticFunctionCall(pc=680,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate WORD(),())),
	109: Goto(pc=683,target=111),
	110: Assignment(pc=686,DVar(useSites={111},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=210; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦680;refId=207], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦686;refId=209]»],origin=110),StaticFunctionCall(pc=686,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$BmpCharPredicate ASCII_WORD(),())),
	111: PutField(pc=689,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={108,110},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=210; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦680;refId=207], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦686;refId=209]»])),
	112: Assignment(pc=694,DVar(useSites={113},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦694;refId=268],origin=112),GetField(pc=694,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	113: Assignment(pc=697,DVar(useSites={114},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦697;refId=271],origin=113),VirtualFunctionCall(pc=697,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate negate(),UVar(defSites={112},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦694;refId=268]),())),
	114: PutField(pc=702,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={113},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦697;refId=271])),
	115: If(pc=706,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=119),
	116: Assignment(pc=712,DVar(useSites={117},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦712;refId=272],origin=116),GetField(pc=712,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	117: Assignment(pc=715,DVar(useSites={118},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦715;refId=274],origin=117),VirtualFunctionCall(pc=715,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={116},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦712;refId=272])))),
	118: PutField(pc=718,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={117},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦715;refId=274])),
	119: Assignment(pc=721,DVar(useSites={120},value=int = -1,origin=119),IntConst(pc=721,-1)),
	120: ReturnValue(pc=722,UVar(defSites={119},value=int = -1)),
	121: If(pc=724,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	122: If(pc=731,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=126),
	123: Assignment(pc=735,DVar(useSites={124,125},value=java.util.regex.Pattern$XGrapheme[↦735;refId=203],origin=123),New(pc=735,java.util.regex.Pattern$XGrapheme)),
	124: NonVirtualMethodCall(pc=739,java.util.regex.Pattern$XGrapheme,isInterface=false,void <init>(),UVar(defSites={123},value=java.util.regex.Pattern$XGrapheme[↦735;refId=203]),()),
	125: PutField(pc=742,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={123},value=java.util.regex.Pattern$XGrapheme[↦735;refId=203])),
	126: Assignment(pc=745,DVar(useSites={127},value=int = -1,origin=126),IntConst(pc=745,-1)),
	127: ReturnValue(pc=746,UVar(defSites={126},value=int = -1)),
	128: Goto(pc=747,target=312),
	129: If(pc=751,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	130: If(pc=758,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=143),
	131: Assignment(pc=762,DVar(useSites={132},value=int = 1,origin=131),IntConst(pc=762,1)),
	132: Assignment(pc=763,DVar(useSites={133},value=int ∈ [0,1],origin=132),VirtualFunctionCall(pc=763,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={131},value=int = 1)))),
	133: If(pc=766,UVar(defSites={132},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=139),
	134: Assignment(pc=770,DVar(useSites={136,137},value=java.util.regex.Pattern$UnixDollar[↦770;refId=199],origin=134),New(pc=770,java.util.regex.Pattern$UnixDollar)),
	135: Assignment(pc=774,DVar(useSites={136},value=int = 0,origin=135),IntConst(pc=774,0)),
	136: NonVirtualMethodCall(pc=775,java.util.regex.Pattern$UnixDollar,isInterface=false,void <init>(boolean),UVar(defSites={134},value=java.util.regex.Pattern$UnixDollar[↦770;refId=199]),(UVar(defSites={135},value=int = 0))),
	137: PutField(pc=778,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={134},value=java.util.regex.Pattern$UnixDollar[↦770;refId=199])),
	138: Goto(pc=781,target=143),
	139: Assignment(pc=785,DVar(useSites={142,141},value=java.util.regex.Pattern$Dollar[↦785;refId=201],origin=139),New(pc=785,java.util.regex.Pattern$Dollar)),
	140: Assignment(pc=789,DVar(useSites={141},value=int = 0,origin=140),IntConst(pc=789,0)),
	141: NonVirtualMethodCall(pc=790,java.util.regex.Pattern$Dollar,isInterface=false,void <init>(boolean),UVar(defSites={139},value=java.util.regex.Pattern$Dollar[↦785;refId=201]),(UVar(defSites={140},value=int = 0))),
	142: PutField(pc=793,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={139},value=java.util.regex.Pattern$Dollar[↦785;refId=201])),
	143: Assignment(pc=796,DVar(useSites={144},value=int = -1,origin=143),IntConst(pc=796,-1)),
	144: ReturnValue(pc=797,UVar(defSites={143},value=int = -1)),
	145: Assignment(pc=798,DVar(useSites={146},value=int = 7,origin=145),IntConst(pc=798,7)),
	146: ReturnValue(pc=800,UVar(defSites={145},value=int = 7)),
	147: If(pc=802,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	148: If(pc=809,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=171),
	149: Assignment(pc=813,DVar(useSites={151},value=an int,origin=149),VirtualFunctionCall(pc=813,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	150: Assignment(pc=816,DVar(useSites={151},value=int = 123,origin=150),IntConst(pc=816,123)),
	151: If(pc=818,UVar(defSites={149},value=an int),!=,UVar(defSites={150},value=int = 123),target=165),
	152: Assignment(pc=822,DVar(useSites={154},value=an int,origin=152),VirtualFunctionCall(pc=822,java.util.regex.Pattern,isInterface=false,int skip(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	153: Assignment(pc=825,DVar(useSites={154},value=int = 103,origin=153),IntConst(pc=825,103)),
	154: If(pc=827,UVar(defSites={152},value=an int),!=,UVar(defSites={153},value=int = 103),target=163),
	155: Assignment(pc=831,DVar(useSites={157},value=an int,origin=155),VirtualFunctionCall(pc=831,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	156: Assignment(pc=834,DVar(useSites={157},value=int = 125,origin=156),IntConst(pc=834,125)),
	157: If(pc=836,UVar(defSites={155},value=an int),!=,UVar(defSites={156},value=int = 125),target=312),
	158: Assignment(pc=840,DVar(useSites={160,159},value=java.util.regex.Pattern$GraphemeBound[↦840;refId=196],origin=158),New(pc=840,java.util.regex.Pattern$GraphemeBound)),
	159: NonVirtualMethodCall(pc=844,java.util.regex.Pattern$GraphemeBound,isInterface=false,void <init>(),UVar(defSites={158},value=java.util.regex.Pattern$GraphemeBound[↦840;refId=196]),()),
	160: PutField(pc=847,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={158},value=java.util.regex.Pattern$GraphemeBound[↦840;refId=196])),
	161: Assignment(pc=850,DVar(useSites={162},value=int = -1,origin=161),IntConst(pc=850,-1)),
	162: ReturnValue(pc=851,UVar(defSites={161},value=int = -1)),
	163: VirtualMethodCall(pc=853,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	164: VirtualMethodCall(pc=857,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	165: Assignment(pc=861,DVar(useSites={170,169},value=java.util.regex.Pattern$Bound[↦861;refId=265],origin=165),New(pc=861,java.util.regex.Pattern$Bound)),
	166: Assignment(pc=865,DVar(useSites={169},value=an int,origin=166),GetStatic(pc=865,java.util.regex.Pattern$Bound,BOTH,int)),
	167: Assignment(pc=869,DVar(useSites={168},value=int = 256,origin=167),IntConst(pc=869,256)),
	168: Assignment(pc=872,DVar(useSites={169},value=int ∈ [0,1],origin=168),VirtualFunctionCall(pc=872,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={167},value=int = 256)))),
	169: NonVirtualMethodCall(pc=875,java.util.regex.Pattern$Bound,isInterface=false,void <init>(int,boolean),UVar(defSites={165},value=java.util.regex.Pattern$Bound[↦861;refId=265]),(UVar(defSites={166},value=an int),UVar(defSites={168},value=int ∈ [0,1]))),
	170: PutField(pc=878,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={165},value=java.util.regex.Pattern$Bound[↦861;refId=265])),
	171: Assignment(pc=881,DVar(useSites={172},value=int = -1,origin=171),IntConst(pc=881,-1)),
	172: ReturnValue(pc=882,UVar(defSites={171},value=int = -1)),
	173: Assignment(pc=884,DVar(useSites={174},value=an int,origin=173),VirtualFunctionCall(pc=884,java.util.regex.Pattern,isInterface=false,int c(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	174: ReturnValue(pc=887,UVar(defSites={173},value=an int)),
	175: If(pc=889,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=187),
	176: Assignment(pc=894,DVar(useSites={177},value=int = 256,origin=176),IntConst(pc=894,256)),
	177: Assignment(pc=897,DVar(useSites={178},value=int ∈ [0,1],origin=177),VirtualFunctionCall(pc=897,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={176},value=int = 256)))),
	178: If(pc=900,UVar(defSites={177},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=181),
	179: Assignment(pc=903,DVar(useSites={182},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦903;refId=186],origin=179),StaticFunctionCall(pc=903,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate DIGIT(),())),
	180: Goto(pc=906,target=182),
	181: Assignment(pc=909,DVar(useSites={182},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=189; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦903;refId=186], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦909;refId=188]»],origin=181),StaticFunctionCall(pc=909,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$BmpCharPredicate ASCII_DIGIT(),())),
	182: PutField(pc=912,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={181,179},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=189; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦903;refId=186], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦909;refId=188]»])),
	183: If(pc=916,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=187),
	184: Assignment(pc=922,DVar(useSites={185},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦922;refId=262],origin=184),GetField(pc=922,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	185: Assignment(pc=925,DVar(useSites={186},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦925;refId=264],origin=185),VirtualFunctionCall(pc=925,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={184},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦922;refId=262])))),
	186: PutField(pc=928,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={185},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦925;refId=264])),
	187: Assignment(pc=931,DVar(useSites={188},value=int = -1,origin=187),IntConst(pc=931,-1)),
	188: ReturnValue(pc=932,UVar(defSites={187},value=int = -1)),
	189: Assignment(pc=933,DVar(useSites={190},value=int = 27,origin=189),IntConst(pc=933,27)),
	190: ReturnValue(pc=935,UVar(defSites={189},value=int = 27)),
	191: Assignment(pc=936,DVar(useSites={192},value=int = 12,origin=191),IntConst(pc=936,12)),
	192: ReturnValue(pc=938,UVar(defSites={191},value=int = 12)),
	193: Goto(pc=939,target=312),
	194: If(pc=943,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=201),
	195: Assignment(pc=947,DVar(useSites={196},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦947;refId=180],origin=195),StaticFunctionCall(pc=947,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$BmpCharPredicate HorizWS(),())),
	196: PutField(pc=950,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={195},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦947;refId=180])),
	197: If(pc=954,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=201),
	198: Assignment(pc=960,DVar(useSites={199},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦960;refId=181],origin=198),GetField(pc=960,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	199: Assignment(pc=963,DVar(useSites={200},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦963;refId=183],origin=199),VirtualFunctionCall(pc=963,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={198},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦960;refId=181])))),
	200: PutField(pc=966,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={199},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦963;refId=183])),
	201: Assignment(pc=969,DVar(useSites={202},value=int = -1,origin=201),IntConst(pc=969,-1)),
	202: ReturnValue(pc=970,UVar(defSites={201},value=int = -1)),
	203: Goto(pc=971,target=312),
	204: If(pc=975,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	205: Assignment(pc=982,DVar(useSites={207},value=an int,origin=205),VirtualFunctionCall(pc=982,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	206: Assignment(pc=985,DVar(useSites={207},value=int = 60,origin=206),IntConst(pc=985,60)),
	207: If(pc=987,UVar(defSites={205},value=an int),==,UVar(defSites={206},value=int = 60),target=211),
	208: Assignment(pc=991,DVar(useSites={209},value=String("\k is not followed by '<' for named capturing group")[@991;refId=175],origin=208),StringConst(pc=991,\k is not followed by '<' for named capturing group)),
	209: Assignment(pc=993,DVar(useSites={210},value={_ <: java.util.regex.PatternSyntaxException, null}[↦993;refId=177],origin=209),VirtualFunctionCall(pc=993,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={208},value=String("\k is not followed by '<' for named capturing group")[@991;refId=175])))),
	210: Throw(pc=996,UVar(defSites={209},value={_ <: java.util.regex.PatternSyntaxException, null}[↦993;refId=177])),
	211: Assignment(pc=999,DVar(useSites={212},value=an int,origin=211),VirtualFunctionCall(pc=999,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	212: Assignment(pc=1002,DVar(useSites={244,220,234,214},value={java.lang.String, null}[↦1002;refId=128],origin=212),VirtualFunctionCall(pc=1002,java.util.regex.Pattern,isInterface=false,java.lang.String groupname(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={211},value=an int)))),
	213: Assignment(pc=1008,DVar(useSites={214},value={_ <: java.util.Map, null}[↦1008;refId=130],origin=213),VirtualFunctionCall(pc=1008,java.util.regex.Pattern,isInterface=false,java.util.Map namedGroups(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	214: Assignment(pc=1013,DVar(useSites={215},value=int ∈ [0,1],origin=214),VirtualFunctionCall(pc=1013,java.util.Map,isInterface=true,boolean containsKey(java.lang.Object),UVar(defSites={213},value={_ <: java.util.Map, null}[↦1008;refId=130]),(UVar(defSites={212},value={java.lang.String, null}[↦1002;refId=128])))),
	215: If(pc=1018,UVar(defSites={214},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=226),
	216: Assignment(pc=1022,DVar(useSites={217,219},value=java.lang.StringBuilder[↦1022;refId=133],origin=216),New(pc=1022,java.lang.StringBuilder)),
	217: NonVirtualMethodCall(pc=1026,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={216},value=java.lang.StringBuilder[↦1022;refId=133]),()),
	218: Assignment(pc=1029,DVar(useSites={219},value=String("named capturing group <")[@1029;refId=135],origin=218),StringConst(pc=1029,named capturing group <)),
	219: Assignment(pc=1031,DVar(useSites={220},value={java.lang.StringBuilder, null}[↦1031;refId=137],origin=219),VirtualFunctionCall(pc=1031,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={216},value=java.lang.StringBuilder[↦1022;refId=133]),(UVar(defSites={218},value=String("named capturing group <")[@1029;refId=135])))),
	220: Assignment(pc=1036,DVar(useSites={222},value={java.lang.StringBuilder, null}[↦1036;refId=140],origin=220),VirtualFunctionCall(pc=1036,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={219},value={java.lang.StringBuilder, null}[↦1031;refId=137]),(UVar(defSites={212},value={java.lang.String, null}[↦1002;refId=128])))),
	221: Assignment(pc=1039,DVar(useSites={222},value=String("> does not exist")[@1039;refId=141],origin=221),StringConst(pc=1039,> does not exist)),
	222: Assignment(pc=1041,DVar(useSites={223},value={java.lang.StringBuilder, null}[↦1041;refId=144],origin=222),VirtualFunctionCall(pc=1041,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={220},value={java.lang.StringBuilder, null}[↦1036;refId=140]),(UVar(defSites={221},value=String("> does not exist")[@1039;refId=141])))),
	223: Assignment(pc=1044,DVar(useSites={224},value={java.lang.String, null}[↦1044;refId=147],origin=223),VirtualFunctionCall(pc=1044,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={222},value={java.lang.StringBuilder, null}[↦1041;refId=144]),())),
	224: Assignment(pc=1047,DVar(useSites={225},value={_ <: java.util.regex.PatternSyntaxException, null}[↦1047;refId=149],origin=224),VirtualFunctionCall(pc=1047,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={223},value={java.lang.String, null}[↦1044;refId=147])))),
	225: Throw(pc=1050,UVar(defSites={224},value={_ <: java.util.regex.PatternSyntaxException, null}[↦1047;refId=149])),
	226: If(pc=1052,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=249),
	227: Assignment(pc=1056,DVar(useSites={228},value=int = 1,origin=227),IntConst(pc=1056,1)),
	228: PutField(pc=1057,java.util.regex.Pattern,hasGroupRef,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={227},value=int = 1)),
	229: Assignment(pc=1061,DVar(useSites={230},value=int = 2,origin=229),IntConst(pc=1061,2)),
	230: Assignment(pc=1062,DVar(useSites={231},value=int ∈ [0,1],origin=230),VirtualFunctionCall(pc=1062,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={229},value=int = 2)))),
	231: If(pc=1065,UVar(defSites={230},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=242),
	232: Assignment(pc=1069,DVar(useSites={240,239},value=java.util.regex.Pattern$CIBackRef[↦1069;refId=152],origin=232),New(pc=1069,java.util.regex.Pattern$CIBackRef)),
	233: Assignment(pc=1074,DVar(useSites={234},value={_ <: java.util.Map, null}[↦1074;refId=154],origin=233),VirtualFunctionCall(pc=1074,java.util.regex.Pattern,isInterface=false,java.util.Map namedGroups(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	234: Assignment(pc=1079,DVar(useSites={236,235},value={_ <: java.lang.Object, null}[↦1079;refId=157],origin=234),VirtualFunctionCall(pc=1079,java.util.Map,isInterface=true,java.lang.Object get(java.lang.Object),UVar(defSites={233},value={_ <: java.util.Map, null}[↦1074;refId=154]),(UVar(defSites={212},value={java.lang.String, null}[↦1002;refId=128])))),
	235: Checkcast(pc=1084,UVar(defSites={234},value={_ <: java.lang.Object, null}[↦1079;refId=157]),java.lang.Integer),
	236: Assignment(pc=1087,DVar(useSites={239},value=an int,origin=236),VirtualFunctionCall(pc=1087,java.lang.Integer,isInterface=false,int intValue(),UVar(defSites={234},value={java.lang.Integer, null}[↦1079;refId=158]),())),
	237: Assignment(pc=1091,DVar(useSites={238},value=int = 64,origin=237),IntConst(pc=1091,64)),
	238: Assignment(pc=1093,DVar(useSites={239},value=int ∈ [0,1],origin=238),VirtualFunctionCall(pc=1093,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={237},value=int = 64)))),
	239: NonVirtualMethodCall(pc=1096,java.util.regex.Pattern$CIBackRef,isInterface=false,void <init>(int,boolean),UVar(defSites={232},value=java.util.regex.Pattern$CIBackRef[↦1069;refId=152]),(UVar(defSites={236},value=an int),UVar(defSites={238},value=int ∈ [0,1]))),
	240: PutField(pc=1099,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={232},value=java.util.regex.Pattern$CIBackRef[↦1069;refId=152])),
	241: Goto(pc=1102,target=249),
	242: Assignment(pc=1106,DVar(useSites={248,247},value=java.util.regex.Pattern$BackRef[↦1106;refId=164],origin=242),New(pc=1106,java.util.regex.Pattern$BackRef)),
	243: Assignment(pc=1111,DVar(useSites={244},value={_ <: java.util.Map, null}[↦1111;refId=166],origin=243),VirtualFunctionCall(pc=1111,java.util.regex.Pattern,isInterface=false,java.util.Map namedGroups(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	244: Assignment(pc=1116,DVar(useSites={246,245},value={_ <: java.lang.Object, null}[↦1116;refId=169],origin=244),VirtualFunctionCall(pc=1116,java.util.Map,isInterface=true,java.lang.Object get(java.lang.Object),UVar(defSites={243},value={_ <: java.util.Map, null}[↦1111;refId=166]),(UVar(defSites={212},value={java.lang.String, null}[↦1002;refId=128])))),
	245: Checkcast(pc=1121,UVar(defSites={244},value={_ <: java.lang.Object, null}[↦1116;refId=169]),java.lang.Integer),
	246: Assignment(pc=1124,DVar(useSites={247},value=an int,origin=246),VirtualFunctionCall(pc=1124,java.lang.Integer,isInterface=false,int intValue(),UVar(defSites={244},value={java.lang.Integer, null}[↦1116;refId=170]),())),
	247: NonVirtualMethodCall(pc=1127,java.util.regex.Pattern$BackRef,isInterface=false,void <init>(int),UVar(defSites={242},value=java.util.regex.Pattern$BackRef[↦1106;refId=164]),(UVar(defSites={246},value=an int))),
	248: PutField(pc=1130,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={242},value=java.util.regex.Pattern$BackRef[↦1106;refId=164])),
	249: Assignment(pc=1133,DVar(useSites={250},value=int = -1,origin=249),IntConst(pc=1133,-1)),
	250: ReturnValue(pc=1134,UVar(defSites={249},value=int = -1)),
	251: Goto(pc=1135,target=312),
	252: Assignment(pc=1138,DVar(useSites={253},value=int = 10,origin=252),IntConst(pc=1138,10)),
	253: ReturnValue(pc=1140,UVar(defSites={252},value=int = 10)),
	254: Goto(pc=1141,target=312),
	255: Assignment(pc=1144,DVar(useSites={256},value=int = 13,origin=255),IntConst(pc=1144,13)),
	256: ReturnValue(pc=1146,UVar(defSites={255},value=int = 13)),
	257: If(pc=1148,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=269),
	258: Assignment(pc=1153,DVar(useSites={259},value=int = 256,origin=258),IntConst(pc=1153,256)),
	259: Assignment(pc=1156,DVar(useSites={260},value=int ∈ [0,1],origin=259),VirtualFunctionCall(pc=1156,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={258},value=int = 256)))),
	260: If(pc=1159,UVar(defSites={259},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=263),
	261: Assignment(pc=1162,DVar(useSites={264},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1162;refId=121],origin=261),StaticFunctionCall(pc=1162,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate WHITE_SPACE(),())),
	262: Goto(pc=1165,target=264),
	263: Assignment(pc=1168,DVar(useSites={264},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=124; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦1162;refId=121], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦1168;refId=123]»],origin=263),StaticFunctionCall(pc=1168,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$BmpCharPredicate ASCII_SPACE(),())),
	264: PutField(pc=1171,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={261,263},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=124; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦1162;refId=121], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦1168;refId=123]»])),
	265: If(pc=1175,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=269),
	266: Assignment(pc=1181,DVar(useSites={267},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1181;refId=259],origin=266),GetField(pc=1181,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	267: Assignment(pc=1184,DVar(useSites={268},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦1184;refId=261],origin=267),VirtualFunctionCall(pc=1184,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={266},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1181;refId=259])))),
	268: PutField(pc=1187,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={267},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦1184;refId=261])),
	269: Assignment(pc=1190,DVar(useSites={270},value=int = -1,origin=269),IntConst(pc=1190,-1)),
	270: ReturnValue(pc=1191,UVar(defSites={269},value=int = -1)),
	271: Assignment(pc=1192,DVar(useSites={272},value=int = 9,origin=271),IntConst(pc=1192,9)),
	272: ReturnValue(pc=1194,UVar(defSites={271},value=int = 9)),
	273: Assignment(pc=1196,DVar(useSites={274},value=an int,origin=273),VirtualFunctionCall(pc=1196,java.util.regex.Pattern,isInterface=false,int u(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	274: ReturnValue(pc=1199,UVar(defSites={273},value=an int)),
	275: If(pc=1201,UVar(defSites={-4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=278),
	276: Assignment(pc=1204,DVar(useSites={277},value=int = 11,origin=276),IntConst(pc=1204,11)),
	277: ReturnValue(pc=1206,UVar(defSites={276},value=int = 11)),
	278: If(pc=1208,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=285),
	279: Assignment(pc=1212,DVar(useSites={280},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦1212;refId=114],origin=279),StaticFunctionCall(pc=1212,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$BmpCharPredicate VertWS(),())),
	280: PutField(pc=1215,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={279},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦1212;refId=114])),
	281: If(pc=1219,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=285),
	282: Assignment(pc=1225,DVar(useSites={283},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1225;refId=115],origin=282),GetField(pc=1225,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	283: Assignment(pc=1228,DVar(useSites={284},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦1228;refId=117],origin=283),VirtualFunctionCall(pc=1228,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={282},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1225;refId=115])))),
	284: PutField(pc=1231,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={283},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦1228;refId=117])),
	285: Assignment(pc=1234,DVar(useSites={286},value=int = -1,origin=285),IntConst(pc=1234,-1)),
	286: ReturnValue(pc=1235,UVar(defSites={285},value=int = -1)),
	287: If(pc=1237,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=299),
	288: Assignment(pc=1242,DVar(useSites={289},value=int = 256,origin=288),IntConst(pc=1242,256)),
	289: Assignment(pc=1245,DVar(useSites={290},value=int ∈ [0,1],origin=289),VirtualFunctionCall(pc=1245,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={288},value=int = 256)))),
	290: If(pc=1248,UVar(defSites={289},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=293),
	291: Assignment(pc=1251,DVar(useSites={294},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1251;refId=109],origin=291),StaticFunctionCall(pc=1251,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate WORD(),())),
	292: Goto(pc=1254,target=294),
	293: Assignment(pc=1257,DVar(useSites={294},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=112; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦1251;refId=109], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦1257;refId=111]»],origin=293),StaticFunctionCall(pc=1257,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$BmpCharPredicate ASCII_WORD(),())),
	294: PutField(pc=1260,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={293,291},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=112; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦1251;refId=109], {_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦1257;refId=111]»])),
	295: If(pc=1264,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=299),
	296: Assignment(pc=1270,DVar(useSites={297},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1270;refId=256],origin=296),GetField(pc=1270,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	297: Assignment(pc=1273,DVar(useSites={298},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦1273;refId=258],origin=297),VirtualFunctionCall(pc=1273,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={296},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦1270;refId=256])))),
	298: PutField(pc=1276,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={297},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦1273;refId=258])),
	299: Assignment(pc=1279,DVar(useSites={300},value=int = -1,origin=299),IntConst(pc=1279,-1)),
	300: ReturnValue(pc=1280,UVar(defSites={299},value=int = -1)),
	301: Assignment(pc=1282,DVar(useSites={302},value=an int,origin=301),VirtualFunctionCall(pc=1282,java.util.regex.Pattern,isInterface=false,int x(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	302: ReturnValue(pc=1285,UVar(defSites={301},value=an int)),
	303: Goto(pc=1286,target=312),
	304: If(pc=1290,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=312),
	305: If(pc=1297,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=309),
	306: Assignment(pc=1301,DVar(useSites={308,307},value=java.util.regex.Pattern$End[↦1301;refId=104],origin=306),New(pc=1301,java.util.regex.Pattern$End)),
	307: NonVirtualMethodCall(pc=1305,java.util.regex.Pattern$End,isInterface=false,void <init>(),UVar(defSites={306},value=java.util.regex.Pattern$End[↦1301;refId=104]),()),
	308: PutField(pc=1308,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={306},value=java.util.regex.Pattern$End[↦1301;refId=104])),
	309: Assignment(pc=1311,DVar(useSites={310},value=int = -1,origin=309),IntConst(pc=1311,-1)),
	310: ReturnValue(pc=1312,UVar(defSites={309},value=int = -1)),
	311: ReturnValue(pc=1315,UVar(defSites={0},value=an int)),
	312: Assignment(pc=1317,DVar(useSites={313},value=String("Illegal/unsupported escape sequence")[@1317;refId=252],origin=312),StringConst(pc=1317,Illegal/unsupported escape sequence)),
	313: Assignment(pc=1319,DVar(useSites={314},value={_ <: java.util.regex.PatternSyntaxException, null}[↦1319;refId=254],origin=313),VirtualFunctionCall(pc=1319,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={312},value=String("Illegal/unsupported escape sequence")[@1317;refId=252])))),
	314: Throw(pc=1322,UVar(defSites={313},value={_ <: java.util.regex.PatternSyntaxException, null}[↦1319;refId=254]))
),cfg=CFG(
	BB_0: BasicBlock(start=69,end=69) -> {BB_32,BB_3e}
	BB_10: BasicBlock(start=174,end=174) -> {BB_98}
	BB_11: BasicBlock(start=42,end=43) -> {BB_c6,BB_6c}
	BB_12: BasicBlock(start=288,end=289) -> {BB_c6,BB_b3}
	BB_13: BasicBlock(start=301,end=301) -> {BB_c6,BB_3b}
	BB_14: BasicBlock(start=37,end=39) -> {BB_c6,BB_a8}
	BB_15: BasicBlock(start=25,end=25) -> {BB_c6,BB_aa}
	BB_16: BasicBlock(start=257,end=257) -> {BB_b,BB_ab}
	BB_17: BasicBlock(start=52,end=52) -> {BB_4b}
	BB_18: BasicBlock(start=14,end=15) -> {BB_c6,BB_9e}
	BB_19: BasicBlock(start=184,end=185) -> {BB_c6,BB_ad}
	BB_1: BasicBlock(start=101,end=101) -> {BB_3a}
	BB_1a: BasicBlock(start=110,end=110) -> {BB_c6,BB_d9}
	BB_1b: BasicBlock(start=125,end=125) -> {BB_cb}
	BB_1c: BasicBlock(start=196,end=197) -> {BB_38,BB_83}
	BB_1d: BasicBlock(start=189,end=190) -> {BB_98}
	BB_1e: BasicBlock(start=20,end=20) -> {BB_42,BB_70}
	BB_1f: BasicBlock(start=93,end=93) -> {BB_32}
	BB_20: BasicBlock(start=284,end=284) -> {BB_47}
	BB_21: BasicBlock(start=152,end=152) -> {BB_c6,BB_f}
	BB_22: BasicBlock(start=57,end=57) -> {BB_c6,BB_b5}
	BB_23: BasicBlock(start=261,end=261) -> {BB_c6,BB_bb}
	BB_24: BasicBlock(start=29,end=29) -> {BB_32}
	BB_25: BasicBlock(start=216,end=217) -> {BB_c6,BB_a6}
	BB_26: BasicBlock(start=164,end=164) -> {BB_c6,BB_3f}
	BB_27: BasicBlock(start=179,end=179) -> {BB_c6,BB_68}
	BB_28: BasicBlock(start=211,end=211) -> {BB_c6,BB_51}
	BB_29: BasicBlock(start=121,end=121) -> {BB_32,BB_d3}
	BB_2: BasicBlock(start=249,end=250) -> {BB_98}
	BB_2a: BasicBlock(start=147,end=147) -> {BB_32,BB_62}
	BB_2b: BasicBlock(start=280,end=281) -> {BB_47,BB_96}
	BB_2c: BasicBlock(start=221,end=222) -> {BB_c6,BB_89}
	BB_2d: BasicBlock(start=293,end=293) -> {BB_c6,BB_ca}
	BB_2e: BasicBlock(start=133,end=133) -> {BB_af,BB_56}
	BB_2f: BasicBlock(start=116,end=117) -> {BB_c6,BB_6e}
	BB_30: BasicBlock(start=1,end=1) -> {BB_bd,BB_81,BB_1d,BB_5c,BB_72,BB_45,BB_7d,BB_a5,BB_bc,BB_58,BB_53,BB_6b,BB_7c,BB_6f,BB_b9,BB_29,BB_41,BB_c5,BB_13,BB_24,BB_2a,BB_a7,BB_92,BB_c9,BB_7a,BB_b0,BB_94,BB_16,BB_a0,BB_cc,BB_1f,BB_93,BB_d0,BB_90,BB_55,BB_a9,BB_86,BB_0,BB_be,BB_5b,BB_da,BB_50,BB_44}
	BB_31: BasicBlock(start=206,end=207) -> {BB_7e,BB_28}
	BB_32: BasicBlock(start=312,end=313) -> {BB_c6,BB_a1}
	BB_33: BasicBlock(start=74,end=75) -> {BB_98}
	BB_34: BasicBlock(start=292,end=292) -> {BB_ca}
	BB_35: BasicBlock(start=6,end=8) -> {BB_c6,BB_4a}
	BB_36: BasicBlock(start=248,end=248) -> {BB_2}
	BB_37: BasicBlock(start=60,end=61) -> {BB_c6,BB_cd}
	BB_38: BasicBlock(start=201,end=202) -> {BB_98}
	BB_39: BasicBlock(start=220,end=220) -> {BB_c6,BB_2c}
	BB_3: BasicBlock(start=234,end=234) -> {BB_c6,BB_b6}
	BB_3a: BasicBlock(start=102,end=103) -> {BB_98}
	BB_3b: BasicBlock(start=302,end=302) -> {BB_98}
	BB_3c: BasicBlock(start=260,end=260) -> {BB_9a,BB_23}
	BB_3d: BasicBlock(start=160,end=162) -> {BB_98}
	BB_3e: BasicBlock(start=70,end=70) -> {BB_33,BB_71}
	BB_3f: BasicBlock(start=165,end=168) -> {BB_c6,BB_4c}
	BB_40: BasicBlock(start=33,end=33) -> {BB_ba,BB_61}
	BB_41: BasicBlock(start=275,end=275) -> {BB_7,BB_88}
	BB_42: BasicBlock(start=21,end=24) -> {BB_c6,BB_15}
	BB_43: BasicBlock(start=137,end=138) -> {BB_a2}
	BB_44: BasicBlock(start=252,end=253) -> {BB_98}
	BB_45: BasicBlock(start=65,end=65) -> {BB_32}
	BB_46: BasicBlock(start=97,end=98) -> {BB_a4,BB_3a}
	BB_47: BasicBlock(start=285,end=286) -> {BB_98}
	BB_48: BasicBlock(start=224,end=224) -> {BB_c6,BB_4e}
	BB_49: BasicBlock(start=156,end=157) -> {BB_32,BB_ac}
	BB_4: BasicBlock(start=0,end=0) -> {BB_c6,BB_30}
	BB_4a: BasicBlock(start=9,end=9) -> {BB_c}
	BB_4b: BasicBlock(start=53,end=54) -> {BB_98}
	BB_4c: BasicBlock(start=169,end=169) -> {BB_c6,BB_6}
	BB_4d: BasicBlock(start=109,end=109) -> {BB_d9}
	BB_4e: BasicBlock(start=225,end=225) -> {BB_c6}
	BB_4f: BasicBlock(start=77,end=78) -> {BB_c6,BB_c3}
	BB_50: BasicBlock(start=193,end=193) -> {BB_32}
	BB_51: BasicBlock(start=212,end=212) -> {BB_c6,BB_7f}
	BB_52: BasicBlock(start=96,end=96) -> {BB_c6,BB_46}
	BB_53: BasicBlock(start=173,end=173) -> {BB_c6,BB_10}
	BB_54: BasicBlock(start=13,end=13) -> {BB_18,BB_66}
	BB_55: BasicBlock(start=129,end=129) -> {BB_32,BB_87}
	BB_56: BasicBlock(start=134,end=136) -> {BB_c6,BB_43}
	BB_57: BasicBlock(start=73,end=73) -> {BB_33}
	BB_58: BasicBlock(start=2,end=2) -> {BB_c6,BB_8f}
	BB_59: BasicBlock(start=266,end=267) -> {BB_c6,BB_c2}
	BB_5: BasicBlock(start=88,end=89) -> {BB_c6,BB_d8}
	BB_5a: BasicBlock(start=205,end=205) -> {BB_c6,BB_31}
	BB_5b: BasicBlock(start=311,end=311) -> {BB_98}
	BB_5c: BasicBlock(start=128,end=128) -> {BB_32}
	BB_5d: BasicBlock(start=237,end=238) -> {BB_c6,BB_c7}
	BB_5e: BasicBlock(start=105,end=106) -> {BB_c6,BB_c1}
	BB_5f: BasicBlock(start=244,end=244) -> {BB_c6,BB_7b}
	BB_60: BasicBlock(start=298,end=298) -> {BB_8b}
	BB_61: BasicBlock(start=34,end=34) -> {BB_c6,BB_8d}
	BB_62: BasicBlock(start=148,end=148) -> {BB_67,BB_ae}
	BB_63: BasicBlock(start=264,end=265) -> {BB_59,BB_b}
	BB_64: BasicBlock(start=45,end=46) -> {BB_98}
	BB_65: BasicBlock(start=279,end=279) -> {BB_c6,BB_2b}
	BB_66: BasicBlock(start=17,end=18) -> {BB_98}
	BB_67: BasicBlock(start=149,end=149) -> {BB_c6,BB_97}
	BB_68: BasicBlock(start=180,end=180) -> {BB_9d}
	BB_69: BasicBlock(start=296,end=297) -> {BB_c6,BB_60}
	BB_6: BasicBlock(start=170,end=170) -> {BB_ae}
	BB_6a: BasicBlock(start=176,end=177) -> {BB_c6,BB_ce}
	BB_6b: BasicBlock(start=191,end=192) -> {BB_98}
	BB_6c: BasicBlock(start=44,end=44) -> {BB_64}
	BB_6d: BasicBlock(start=291,end=291) -> {BB_c6,BB_34}
	BB_6e: BasicBlock(start=118,end=118) -> {BB_b4}
	BB_6f: BasicBlock(start=204,end=204) -> {BB_32,BB_5a}
	BB_70: BasicBlock(start=27,end=28) -> {BB_98}
	BB_71: BasicBlock(start=71,end=72) -> {BB_c6,BB_57}
	BB_72: BasicBlock(start=12,end=12) -> {BB_32,BB_54}
	BB_73: BasicBlock(start=49,end=49) -> {BB_9b,BB_4b}
	BB_74: BasicBlock(start=236,end=236) -> {BB_c6,BB_5d}
	BB_75: BasicBlock(start=181,end=181) -> {BB_c6,BB_9d}
	BB_76: BasicBlock(start=86,end=87) -> {BB_80,BB_5}
	BB_77: BasicBlock(start=187,end=188) -> {BB_98}
	BB_78: BasicBlock(start=274,end=274) -> {BB_98}
	BB_79: BasicBlock(start=81,end=81) -> {BB_d4}
	BB_7: BasicBlock(start=276,end=277) -> {BB_98}
	BB_7a: BasicBlock(start=76,end=76) -> {BB_80,BB_4f}
	BB_7b: BasicBlock(start=245,end=245) -> {BB_c6,BB_b7}
	BB_7c: BasicBlock(start=303,end=303) -> {BB_32}
	BB_7d: BasicBlock(start=271,end=272) -> {BB_98}
	BB_7e: BasicBlock(start=208,end=209) -> {BB_c6,BB_c0}
	BB_7f: BasicBlock(start=213,end=213) -> {BB_c6,BB_b8}
	BB_80: BasicBlock(start=91,end=92) -> {BB_98}
	BB_81: BasicBlock(start=66,end=66) -> {BB_c6,BB_9c}
	BB_82: BasicBlock(start=155,end=155) -> {BB_c6,BB_49}
	BB_83: BasicBlock(start=198,end=199) -> {BB_c6,BB_d2}
	BB_84: BasicBlock(start=108,end=108) -> {BB_c6,BB_4d}
	BB_85: BasicBlock(start=240,end=241) -> {BB_2}
	BB_86: BasicBlock(start=251,end=251) -> {BB_32}
	BB_87: BasicBlock(start=130,end=130) -> {BB_a2,BB_cf}
	BB_88: BasicBlock(start=278,end=278) -> {BB_47,BB_65}
	BB_89: BasicBlock(start=223,end=223) -> {BB_c6,BB_48}
	BB_8: BasicBlock(start=308,end=308) -> {BB_d5}
	BB_8a: BasicBlock(start=306,end=307) -> {BB_c6,BB_8}
	BB_8b: BasicBlock(start=299,end=300) -> {BB_98}
	BB_8c: BasicBlock(start=80,end=80) -> {BB_c6,BB_79}
	BB_8d: BasicBlock(start=35,end=35) -> {BB_14}
	BB_8e: BasicBlock(start=226,end=226) -> {BB_2,BB_db}
	BB_8f: BasicBlock(start=3,end=3) -> {BB_98}
	BB_90: BasicBlock(start=255,end=256) -> {BB_98}
	BB_91: BasicBlock(start=123,end=124) -> {BB_c6,BB_1b}
	BB_92: BasicBlock(start=194,end=194) -> {BB_c4,BB_38}
	BB_93: BasicBlock(start=145,end=146) -> {BB_98}
	BB_94: BasicBlock(start=48,end=48) -> {BB_32,BB_73}
	BB_95: BasicBlock(start=63,end=64) -> {BB_98}
	BB_96: BasicBlock(start=282,end=283) -> {BB_c6,BB_20}
	BB_97: BasicBlock(start=150,end=151) -> {BB_3f,BB_21}
	BB_98: ExitNode(normalReturn=true)
	BB_99: BasicBlock(start=95,end=95) -> {BB_c6,BB_52}
	BB_9: BasicBlock(start=5,end=5) -> {BB_35,BB_c}
	BB_9a: BasicBlock(start=263,end=263) -> {BB_c6,BB_63}
	BB_9b: BasicBlock(start=50,end=51) -> {BB_c6,BB_17}
	BB_9c: BasicBlock(start=67,end=67) -> {BB_98}
	BB_9d: BasicBlock(start=182,end=183) -> {BB_77,BB_19}
	BB_9e: BasicBlock(start=16,end=16) -> {BB_66}
	BB_9f: BasicBlock(start=31,end=32) -> {BB_c6,BB_40}
	BB_a0: BasicBlock(start=175,end=175) -> {BB_6a,BB_77}
	BB_a1: BasicBlock(start=314,end=314) -> {BB_c6}
	BB_a2: BasicBlock(start=143,end=144) -> {BB_98}
	BB_a3: BasicBlock(start=231,end=231) -> {BB_d7,BB_c8}
	BB_a4: BasicBlock(start=99,end=100) -> {BB_c6,BB_1}
	BB_a5: BasicBlock(start=203,end=203) -> {BB_32}
	BB_a6: BasicBlock(start=218,end=219) -> {BB_c6,BB_39}
	BB_a7: BasicBlock(start=104,end=104) -> {BB_b4,BB_5e}
	BB_a8: BasicBlock(start=40,end=41) -> {BB_64,BB_11}
	BB_a9: BasicBlock(start=304,end=304) -> {BB_32,BB_bf}
	BB_a: BasicBlock(start=247,end=247) -> {BB_c6,BB_36}
	BB_aa: BasicBlock(start=26,end=26) -> {BB_70}
	BB_ab: BasicBlock(start=258,end=259) -> {BB_c6,BB_3c}
	BB_ac: BasicBlock(start=158,end=159) -> {BB_c6,BB_3d}
	BB_ad: BasicBlock(start=186,end=186) -> {BB_77}
	BB_ae: BasicBlock(start=171,end=172) -> {BB_98}
	BB_af: BasicBlock(start=139,end=141) -> {BB_c6,BB_e}
	BB_b0: BasicBlock(start=55,end=55) -> {BB_d,BB_95}
	BB_b1: BasicBlock(start=114,end=115) -> {BB_b4,BB_2f}
	BB_b2: BasicBlock(start=82,end=82) -> {BB_c6,BB_d4}
	BB_b3: BasicBlock(start=290,end=290) -> {BB_2d,BB_6d}
	BB_b4: BasicBlock(start=119,end=120) -> {BB_98}
	BB_b5: BasicBlock(start=58,end=59) -> {BB_37,BB_95}
	BB_b6: BasicBlock(start=235,end=235) -> {BB_c6,BB_74}
	BB_b7: BasicBlock(start=246,end=246) -> {BB_c6,BB_a}
	BB_b8: BasicBlock(start=214,end=214) -> {BB_c6,BB_d6}
	BB_b9: BasicBlock(start=287,end=287) -> {BB_12,BB_8b}
	BB_b: BasicBlock(start=269,end=270) -> {BB_98}
	BB_ba: BasicBlock(start=36,end=36) -> {BB_c6,BB_14}
	BB_bb: BasicBlock(start=262,end=262) -> {BB_63}
	BB_bc: BasicBlock(start=30,end=30) -> {BB_64,BB_9f}
	BB_bd: BasicBlock(start=19,end=19) -> {BB_32,BB_1e}
	BB_be: BasicBlock(start=273,end=273) -> {BB_c6,BB_78}
	BB_bf: BasicBlock(start=305,end=305) -> {BB_8a,BB_d5}
	BB_c0: BasicBlock(start=210,end=210) -> {BB_c6}
	BB_c1: BasicBlock(start=107,end=107) -> {BB_84,BB_1a}
	BB_c2: BasicBlock(start=268,end=268) -> {BB_b}
	BB_c3: BasicBlock(start=79,end=79) -> {BB_8c,BB_b2}
	BB_c4: BasicBlock(start=195,end=195) -> {BB_c6,BB_1c}
	BB_c5: BasicBlock(start=94,end=94) -> {BB_99,BB_3a}
	BB_c6: ExitNode(normalReturn=false)
	BB_c7: BasicBlock(start=239,end=239) -> {BB_c6,BB_85}
	BB_c8: BasicBlock(start=242,end=243) -> {BB_c6,BB_5f}
	BB_c9: BasicBlock(start=4,end=4) -> {BB_32,BB_9}
	BB_c: BasicBlock(start=10,end=11) -> {BB_98}
	BB_ca: BasicBlock(start=294,end=295) -> {BB_69,BB_8b}
	BB_cb: BasicBlock(start=126,end=127) -> {BB_98}
	BB_cc: BasicBlock(start=68,end=68) -> {BB_32}
	BB_cd: BasicBlock(start=62,end=62) -> {BB_95}
	BB_ce: BasicBlock(start=178,end=178) -> {BB_75,BB_27}
	BB_cf: BasicBlock(start=131,end=132) -> {BB_c6,BB_2e}
	BB_d0: BasicBlock(start=47,end=47) -> {BB_32}
	BB_d1: BasicBlock(start=163,end=163) -> {BB_c6,BB_26}
	BB_d2: BasicBlock(start=200,end=200) -> {BB_38}
	BB_d3: BasicBlock(start=122,end=122) -> {BB_91,BB_cb}
	BB_d4: BasicBlock(start=83,end=85) -> {BB_c6,BB_76}
	BB_d5: BasicBlock(start=309,end=310) -> {BB_98}
	BB_d6: BasicBlock(start=215,end=215) -> {BB_25,BB_8e}
	BB_d7: BasicBlock(start=232,end=233) -> {BB_c6,BB_3}
	BB_d8: BasicBlock(start=90,end=90) -> {BB_80}
	BB_d9: BasicBlock(start=111,end=113) -> {BB_c6,BB_b1}
	BB_d: BasicBlock(start=56,end=56) -> {BB_c6,BB_22}
	BB_da: BasicBlock(start=254,end=254) -> {BB_32}
	BB_db: BasicBlock(start=227,end=230) -> {BB_c6,BB_a3}
	BB_e: BasicBlock(start=142,end=142) -> {BB_a2}
	BB_f: BasicBlock(start=153,end=154) -> {BB_d1,BB_82}
))

boolean lambda$SingleS$7(int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: If(pc=2,UVar(defSites={-3},value=an int),!=,UVar(defSites={-2},value=an int),target=3),
	1: Assignment(pc=5,DVar(useSites={4},value=int = 1,origin=1),IntConst(pc=5,1)),
	2: Goto(pc=6,target=4),
	3: Assignment(pc=9,DVar(useSites={4},value=int ∈ [0,1],origin=3),IntConst(pc=9,0)),
	4: ReturnValue(pc=10,UVar(defSites={1,3},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_2,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_4}
	BB_2: BasicBlock(start=3,end=3) -> {BB_4}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_3}
	BB_5: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate SingleU(int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$SingleU(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda, null}[↦1;refId=103],origin=0),StaticFunctionCall(pc=1,java.util.regex.Pattern$SingleU(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda,isInterface=false,java.util.regex.Pattern$SingleU(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda $newInstance(int),(UVar(defSites={-2},value=an int)))),
	1: ReturnValue(pc=6,UVar(defSites={0},value={_ <: java.util.regex.Pattern$SingleU(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda, null}[↦1;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int o()
AITACode(params=(Parameters(
	0: useSites={0,40,54,14,49,7} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={24,4,28,2,42,22,51},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Assignment(pc=6,DVar(useSites={2},value=int = 48,origin=1),IntConst(pc=6,48)),
	2: Assignment(pc=8,DVar(useSites={5},value=an int,origin=2),BinaryExpr(pc=8,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={1},value=int = 48))),
	3: Assignment(pc=9,DVar(useSites={4},value=int = 55,origin=3),IntConst(pc=9,55)),
	4: Assignment(pc=12,DVar(useSites={5},value=an int,origin=4),BinaryExpr(pc=12,ComputationalTypeInt,UVar(defSites={3},value=int = 55),-,UVar(defSites={0},value=an int))),
	5: Assignment(pc=13,DVar(useSites={6},value=an int,origin=5),BinaryExpr(pc=13,ComputationalTypeInt,UVar(defSites={2},value=an int),|,UVar(defSites={4},value=an int))),
	6: If(pc=14,UVar(defSites={5},value=an int),<,IntConst(pc=-333,0),target=53),
	7: Assignment(pc=18,DVar(useSites={32,46,9,11},value=an int,origin=7),VirtualFunctionCall(pc=18,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	8: Assignment(pc=23,DVar(useSites={9},value=int = 48,origin=8),IntConst(pc=23,48)),
	9: Assignment(pc=25,DVar(useSites={12},value=an int,origin=9),BinaryExpr(pc=25,ComputationalTypeInt,UVar(defSites={7},value=an int),-,UVar(defSites={8},value=int = 48))),
	10: Assignment(pc=26,DVar(useSites={11},value=int = 55,origin=10),IntConst(pc=26,55)),
	11: Assignment(pc=29,DVar(useSites={12},value=an int,origin=11),BinaryExpr(pc=29,ComputationalTypeInt,UVar(defSites={10},value=int = 55),-,UVar(defSites={7},value=an int))),
	12: Assignment(pc=30,DVar(useSites={13},value=an int,origin=12),BinaryExpr(pc=30,ComputationalTypeInt,UVar(defSites={9},value=an int),|,UVar(defSites={11},value=an int))),
	13: If(pc=31,UVar(defSites={12},value=an int),<,IntConst(pc=-333,0),target=49),
	14: Assignment(pc=35,DVar(useSites={16,18,37},value=an int,origin=14),VirtualFunctionCall(pc=35,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	15: Assignment(pc=40,DVar(useSites={16},value=int = 48,origin=15),IntConst(pc=40,48)),
	16: Assignment(pc=42,DVar(useSites={19},value=an int,origin=16),BinaryExpr(pc=42,ComputationalTypeInt,UVar(defSites={14},value=an int),-,UVar(defSites={15},value=int = 48))),
	17: Assignment(pc=43,DVar(useSites={18},value=int = 55,origin=17),IntConst(pc=43,55)),
	18: Assignment(pc=46,DVar(useSites={19},value=an int,origin=18),BinaryExpr(pc=46,ComputationalTypeInt,UVar(defSites={17},value=int = 55),-,UVar(defSites={14},value=an int))),
	19: Assignment(pc=47,DVar(useSites={20},value=an int,origin=19),BinaryExpr(pc=47,ComputationalTypeInt,UVar(defSites={16},value=an int),|,UVar(defSites={18},value=an int))),
	20: If(pc=48,UVar(defSites={19},value=an int),<,IntConst(pc=-333,0),target=40),
	21: Assignment(pc=52,DVar(useSites={22},value=int = 48,origin=21),IntConst(pc=52,48)),
	22: Assignment(pc=54,DVar(useSites={25},value=an int,origin=22),BinaryExpr(pc=54,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={21},value=int = 48))),
	23: Assignment(pc=55,DVar(useSites={24},value=int = 51,origin=23),IntConst(pc=55,51)),
	24: Assignment(pc=58,DVar(useSites={25},value=an int,origin=24),BinaryExpr(pc=58,ComputationalTypeInt,UVar(defSites={23},value=int = 51),-,UVar(defSites={0},value=an int))),
	25: Assignment(pc=59,DVar(useSites={26},value=an int,origin=25),BinaryExpr(pc=59,ComputationalTypeInt,UVar(defSites={22},value=an int),|,UVar(defSites={24},value=an int))),
	26: If(pc=60,UVar(defSites={25},value=an int),<,IntConst(pc=-333,0),target=40),
	27: Assignment(pc=64,DVar(useSites={28},value=int = 48,origin=27),IntConst(pc=64,48)),
	28: Assignment(pc=66,DVar(useSites={30},value=an int,origin=28),BinaryExpr(pc=66,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={27},value=int = 48))),
	29: Assignment(pc=67,DVar(useSites={30},value=int = 64,origin=29),IntConst(pc=67,64)),
	30: Assignment(pc=69,DVar(useSites={35},value=an int,origin=30),BinaryExpr(pc=69,ComputationalTypeInt,UVar(defSites={28},value=an int),*,UVar(defSites={29},value=int = 64))),
	31: Assignment(pc=71,DVar(useSites={32},value=int = 48,origin=31),IntConst(pc=71,48)),
	32: Assignment(pc=73,DVar(useSites={34},value=an int,origin=32),BinaryExpr(pc=73,ComputationalTypeInt,UVar(defSites={7},value=an int),-,UVar(defSites={31},value=int = 48))),
	33: Assignment(pc=74,DVar(useSites={34},value=int = 8,origin=33),IntConst(pc=74,8)),
	34: Assignment(pc=76,DVar(useSites={35},value=an int,origin=34),BinaryExpr(pc=76,ComputationalTypeInt,UVar(defSites={32},value=an int),*,UVar(defSites={33},value=int = 8))),
	35: Assignment(pc=77,DVar(useSites={38},value=an int,origin=35),BinaryExpr(pc=77,ComputationalTypeInt,UVar(defSites={30},value=an int),+,UVar(defSites={34},value=an int))),
	36: Assignment(pc=79,DVar(useSites={37},value=int = 48,origin=36),IntConst(pc=79,48)),
	37: Assignment(pc=81,DVar(useSites={38},value=an int,origin=37),BinaryExpr(pc=81,ComputationalTypeInt,UVar(defSites={14},value=an int),-,UVar(defSites={36},value=int = 48))),
	38: Assignment(pc=82,DVar(useSites={39},value=an int,origin=38),BinaryExpr(pc=82,ComputationalTypeInt,UVar(defSites={35},value=an int),+,UVar(defSites={37},value=an int))),
	39: ReturnValue(pc=83,UVar(defSites={38},value=an int)),
	40: VirtualMethodCall(pc=85,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	41: Assignment(pc=89,DVar(useSites={42},value=int = 48,origin=41),IntConst(pc=89,48)),
	42: Assignment(pc=91,DVar(useSites={44},value=an int,origin=42),BinaryExpr(pc=91,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={41},value=int = 48))),
	43: Assignment(pc=92,DVar(useSites={44},value=int = 8,origin=43),IntConst(pc=92,8)),
	44: Assignment(pc=94,DVar(useSites={47},value=an int,origin=44),BinaryExpr(pc=94,ComputationalTypeInt,UVar(defSites={42},value=an int),*,UVar(defSites={43},value=int = 8))),
	45: Assignment(pc=96,DVar(useSites={46},value=int = 48,origin=45),IntConst(pc=96,48)),
	46: Assignment(pc=98,DVar(useSites={47},value=an int,origin=46),BinaryExpr(pc=98,ComputationalTypeInt,UVar(defSites={7},value=an int),-,UVar(defSites={45},value=int = 48))),
	47: Assignment(pc=99,DVar(useSites={48},value=an int,origin=47),BinaryExpr(pc=99,ComputationalTypeInt,UVar(defSites={44},value=an int),+,UVar(defSites={46},value=an int))),
	48: ReturnValue(pc=100,UVar(defSites={47},value=an int)),
	49: VirtualMethodCall(pc=102,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	50: Assignment(pc=106,DVar(useSites={51},value=int = 48,origin=50),IntConst(pc=106,48)),
	51: Assignment(pc=108,DVar(useSites={52},value=an int,origin=51),BinaryExpr(pc=108,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={50},value=int = 48))),
	52: ReturnValue(pc=109,UVar(defSites={51},value=an int)),
	53: Assignment(pc=111,DVar(useSites={54},value=String("Illegal octal escape sequence")[@111;refId=107],origin=53),StringConst(pc=111,Illegal octal escape sequence)),
	54: Assignment(pc=114,DVar(useSites={55},value={_ <: java.util.regex.PatternSyntaxException, null}[↦114;refId=109],origin=54),VirtualFunctionCall(pc=114,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={53},value=String("Illegal octal escape sequence")[@111;refId=107])))),
	55: Throw(pc=117,UVar(defSites={54},value={_ <: java.util.regex.PatternSyntaxException, null}[↦114;refId=109]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_2}
	BB_1: BasicBlock(start=14,end=14) -> {BB_c,BB_d}
	BB_2: BasicBlock(start=1,end=6) -> {BB_4,BB_8}
	BB_3: BasicBlock(start=21,end=26) -> {BB_e,BB_6}
	BB_4: BasicBlock(start=53,end=54) -> {BB_c,BB_f}
	BB_5: BasicBlock(start=41,end=48) -> {BB_9}
	BB_6: BasicBlock(start=27,end=39) -> {BB_9}
	BB_7: BasicBlock(start=49,end=49) -> {BB_c,BB_a}
	BB_8: BasicBlock(start=7,end=7) -> {BB_c,BB_b}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=50,end=52) -> {BB_9}
	BB_b: BasicBlock(start=8,end=13) -> {BB_1,BB_7}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=20) -> {BB_e,BB_3}
	BB_e: BasicBlock(start=40,end=40) -> {BB_c,BB_5}
	BB_f: BasicBlock(start=55,end=55) -> {BB_c}
))

boolean lambda$CIRange$13(int,int,int)
AITACode(params=(Parameters(
	1: useSites={0,8,5} (origin=-2),
	2: useSites={0,8,5} (origin=-3),
	3: useSites={0,4,2,7} (origin=-4)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={1},value=int ∈ [0,1],origin=0),StaticFunctionCall(pc=3,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-4},value=an int),UVar(defSites={-3},value=an int)))),
	1: If(pc=6,UVar(defSites={0},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=10),
	2: Assignment(pc=10,DVar(useSites={3},value=int ∈ [0,1],origin=2),StaticFunctionCall(pc=10,java.util.regex.ASCII,isInterface=false,boolean isAscii(int),(UVar(defSites={-4},value=an int)))),
	3: If(pc=13,UVar(defSites={2},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	4: Assignment(pc=18,DVar(useSites={5},value=an int,origin=4),StaticFunctionCall(pc=18,java.util.regex.ASCII,isInterface=false,int toUpper(int),(UVar(defSites={-4},value=an int)))),
	5: Assignment(pc=22,DVar(useSites={6},value=int ∈ [0,1],origin=5),StaticFunctionCall(pc=22,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={4},value=an int),UVar(defSites={-3},value=an int)))),
	6: If(pc=25,UVar(defSites={5},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=10),
	7: Assignment(pc=30,DVar(useSites={8},value=an int,origin=7),StaticFunctionCall(pc=30,java.util.regex.ASCII,isInterface=false,int toLower(int),(UVar(defSites={-4},value=an int)))),
	8: Assignment(pc=34,DVar(useSites={9},value=int ∈ [0,1],origin=8),StaticFunctionCall(pc=34,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={7},value=an int),UVar(defSites={-3},value=an int)))),
	9: If(pc=37,UVar(defSites={8},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	10: Assignment(pc=40,DVar(useSites={13},value=int = 1,origin=10),IntConst(pc=40,1)),
	11: Goto(pc=41,target=13),
	12: Assignment(pc=44,DVar(useSites={13},value=int ∈ [0,1],origin=12),IntConst(pc=44,0)),
	13: ReturnValue(pc=45,UVar(defSites={12,10},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_e,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_e,BB_4}
	BB_2: BasicBlock(start=10,end=11) -> {BB_6}
	BB_3: BasicBlock(start=1,end=1) -> {BB_2,BB_7}
	BB_4: BasicBlock(start=6,end=6) -> {BB_2,BB_9}
	BB_5: BasicBlock(start=9,end=9) -> {BB_2,BB_8}
	BB_6: BasicBlock(start=13,end=13) -> {BB_b}
	BB_7: BasicBlock(start=2,end=2) -> {BB_e,BB_a}
	BB_8: BasicBlock(start=12,end=12) -> {BB_6}
	BB_9: BasicBlock(start=7,end=7) -> {BB_e,BB_c}
	BB_a: BasicBlock(start=3,end=3) -> {BB_d,BB_8}
	BB_b: ExitNode(normalReturn=true)
	BB_c: BasicBlock(start=8,end=8) -> {BB_e,BB_5}
	BB_d: BasicBlock(start=4,end=4) -> {BB_e,BB_1}
	BB_e: ExitNode(normalReturn=false)
))

int uxxxx()
AITACode(params=(Parameters(
	0: useSites={8,4} (origin=-1)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={16,11},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=2,DVar(useSites={14,3},value=int = 0,origin=1),IntConst(pc=2,0)),
	2: Assignment(pc=5,DVar(useSites={3},value=int = 4,origin=2),IntConst(pc=5,4)),
	3: If(pc=6,UVar(defSites={14,1},value=int ∈ [0,4]),>=,UVar(defSites={2},value=int = 4),target=16),
	4: Assignment(pc=10,DVar(useSites={12,5},value=an int,origin=4),VirtualFunctionCall(pc=10,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	5: Assignment(pc=15,DVar(useSites={6},value=int ∈ [0,1],origin=5),StaticFunctionCall(pc=15,java.util.regex.ASCII,isInterface=false,boolean isHexDigit(int),(UVar(defSites={4},value=an int)))),
	6: If(pc=18,UVar(defSites={5},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=10),
	7: Assignment(pc=22,DVar(useSites={8},value=String("Illegal Unicode escape sequence")[@22;refId=133],origin=7),StringConst(pc=22,Illegal Unicode escape sequence)),
	8: Assignment(pc=25,DVar(useSites={9},value={_ <: java.util.regex.PatternSyntaxException, null}[↦25;refId=135],origin=8),VirtualFunctionCall(pc=25,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={7},value=String("Illegal Unicode escape sequence")[@22;refId=133])))),
	9: Throw(pc=28,UVar(defSites={8},value={_ <: java.util.regex.PatternSyntaxException, null}[↦25;refId=135])),
	10: Assignment(pc=30,DVar(useSites={11},value=int = 16,origin=10),IntConst(pc=30,16)),
	11: Assignment(pc=32,DVar(useSites={13},value=an int,origin=11),BinaryExpr(pc=32,ComputationalTypeInt,UVar(defSites={0,13},value=an int),*,UVar(defSites={10},value=int = 16))),
	12: Assignment(pc=34,DVar(useSites={13},value=an int,origin=12),StaticFunctionCall(pc=34,java.util.regex.ASCII,isInterface=false,int toDigit(int),(UVar(defSites={4},value=an int)))),
	13: Assignment(pc=37,DVar(useSites={16,11},value=an int,origin=13),BinaryExpr(pc=37,ComputationalTypeInt,UVar(defSites={11},value=an int),+,UVar(defSites={12},value=an int))),
	14: Assignment(pc=39,DVar(useSites={3,15},value=int ∈ [1,4],origin=14),BinaryExpr(pc=39,ComputationalTypeInt,UVar(defSites={14,1},value=int ∈ [0,3]),+,IntConst(pc=39,1))),
	15: Goto(pc=42,target=2),
	16: ReturnValue(pc=46,UVar(defSites={0,13},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_6}
	BB_1: BasicBlock(start=5,end=5) -> {BB_b,BB_3}
	BB_2: BasicBlock(start=10,end=12) -> {BB_b,BB_5}
	BB_3: BasicBlock(start=6,end=6) -> {BB_7,BB_2}
	BB_4: BasicBlock(start=9,end=9) -> {BB_b}
	BB_5: BasicBlock(start=13,end=15) -> {BB_6}
	BB_6: BasicBlock(start=2,end=3) -> {BB_a,BB_9}
	BB_7: BasicBlock(start=7,end=8) -> {BB_b,BB_4}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=16,end=16) -> {BB_8}
	BB_a: BasicBlock(start=4,end=4) -> {BB_b,BB_1}
	BB_b: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$Node curly(java.util.regex.Pattern$Node,int)
AITACode(params=(Parameters(
	0: useSites={0,3,11} (origin=-1),
	1: useSites={32,20,26,17,21,27,7,23,15} (origin=-2),
	2: useSites={32,21,27,7,15} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,10},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Assignment(pc=6,DVar(useSites={2},value=int = 63,origin=1),IntConst(pc=6,63)),
	2: If(pc=8,UVar(defSites={0},value=an int),!=,UVar(defSites={1},value=int = 63),target=9),
	3: ExprStmt(pc=12,VirtualFunctionCall(pc=12,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	4: Assignment(pc=16,DVar(useSites={8,7},value=java.util.regex.Pattern$Curly[↦16;refId=121],origin=4),New(pc=16,java.util.regex.Pattern$Curly)),
	5: Assignment(pc=22,DVar(useSites={7},value=int = 2147483647,origin=5),IntConst(pc=22,2147483647)),
	6: Assignment(pc=25,DVar(useSites={7},value={java.util.regex.Pattern$Qtype, null}[↦25;refId=122],origin=6),GetStatic(pc=25,java.util.regex.Pattern$Qtype,LAZY,java.util.regex.Pattern$Qtype)),
	7: NonVirtualMethodCall(pc=28,java.util.regex.Pattern$Curly,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype),UVar(defSites={4},value=java.util.regex.Pattern$Curly[↦16;refId=121]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={5},value=int = 2147483647),UVar(defSites={6},value={java.util.regex.Pattern$Qtype, null}[↦25;refId=122]))),
	8: ReturnValue(pc=31,UVar(defSites={4},value=java.util.regex.Pattern$Curly[↦16;refId=121])),
	9: Assignment(pc=33,DVar(useSites={10},value=int = 43,origin=9),IntConst(pc=33,43)),
	10: If(pc=35,UVar(defSites={0},value=an int),!=,UVar(defSites={9},value=int = 43),target=17),
	11: ExprStmt(pc=39,VirtualFunctionCall(pc=39,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	12: Assignment(pc=43,DVar(useSites={16,15},value=java.util.regex.Pattern$Curly[↦43;refId=117],origin=12),New(pc=43,java.util.regex.Pattern$Curly)),
	13: Assignment(pc=49,DVar(useSites={15},value=int = 2147483647,origin=13),IntConst(pc=49,2147483647)),
	14: Assignment(pc=52,DVar(useSites={15},value={java.util.regex.Pattern$Qtype, null}[↦52;refId=118],origin=14),GetStatic(pc=52,java.util.regex.Pattern$Qtype,POSSESSIVE,java.util.regex.Pattern$Qtype)),
	15: NonVirtualMethodCall(pc=55,java.util.regex.Pattern$Curly,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype),UVar(defSites={12},value=java.util.regex.Pattern$Curly[↦43;refId=117]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={13},value=int = 2147483647),UVar(defSites={14},value={java.util.regex.Pattern$Qtype, null}[↦52;refId=118]))),
	16: ReturnValue(pc=58,UVar(defSites={12},value=java.util.regex.Pattern$Curly[↦43;refId=117])),
	17: Assignment(pc=60,DVar(useSites={18},value=int ∈ [0,1],origin=17),InstanceOf(pc=60,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),java.util.regex.Pattern$BmpCharProperty)),
	18: If(pc=63,UVar(defSites={17},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=23),
	19: Assignment(pc=66,DVar(useSites={22,21},value=java.util.regex.Pattern$BmpCharPropertyGreedy[↦66;refId=105],origin=19),New(pc=66,java.util.regex.Pattern$BmpCharPropertyGreedy)),
	20: Checkcast(pc=71,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),java.util.regex.Pattern$BmpCharProperty),
	21: NonVirtualMethodCall(pc=75,java.util.regex.Pattern$BmpCharPropertyGreedy,isInterface=false,void <init>(java.util.regex.Pattern$BmpCharProperty,int),UVar(defSites={19},value=java.util.regex.Pattern$BmpCharPropertyGreedy[↦66;refId=105]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$BmpCharProperty, null}[↦-2;refId=106]),UVar(defSites={-3},value=an int))),
	22: ReturnValue(pc=78,UVar(defSites={19},value=java.util.regex.Pattern$BmpCharPropertyGreedy[↦66;refId=105])),
	23: Assignment(pc=80,DVar(useSites={24},value=int ∈ [0,1],origin=23),InstanceOf(pc=80,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),java.util.regex.Pattern$CharProperty)),
	24: If(pc=83,UVar(defSites={23},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=29),
	25: Assignment(pc=86,DVar(useSites={28,27},value=java.util.regex.Pattern$CharPropertyGreedy[↦86;refId=109],origin=25),New(pc=86,java.util.regex.Pattern$CharPropertyGreedy)),
	26: Checkcast(pc=91,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),java.util.regex.Pattern$CharProperty),
	27: NonVirtualMethodCall(pc=95,java.util.regex.Pattern$CharPropertyGreedy,isInterface=false,void <init>(java.util.regex.Pattern$CharProperty,int),UVar(defSites={25},value=java.util.regex.Pattern$CharPropertyGreedy[↦86;refId=109]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦-2;refId=110]),UVar(defSites={-3},value=an int))),
	28: ReturnValue(pc=98,UVar(defSites={25},value=java.util.regex.Pattern$CharPropertyGreedy[↦86;refId=109])),
	29: Assignment(pc=99,DVar(useSites={32,33},value=java.util.regex.Pattern$Curly[↦99;refId=113],origin=29),New(pc=99,java.util.regex.Pattern$Curly)),
	30: Assignment(pc=105,DVar(useSites={32},value=int = 2147483647,origin=30),IntConst(pc=105,2147483647)),
	31: Assignment(pc=108,DVar(useSites={32},value={java.util.regex.Pattern$Qtype, null}[↦108;refId=114],origin=31),GetStatic(pc=108,java.util.regex.Pattern$Qtype,GREEDY,java.util.regex.Pattern$Qtype)),
	32: NonVirtualMethodCall(pc=111,java.util.regex.Pattern$Curly,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype),UVar(defSites={29},value=java.util.regex.Pattern$Curly[↦99;refId=113]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={30},value=int = 2147483647),UVar(defSites={31},value={java.util.regex.Pattern$Qtype, null}[↦108;refId=114]))),
	33: ReturnValue(pc=114,UVar(defSites={29},value=java.util.regex.Pattern$Curly[↦99;refId=113]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_14,BB_3}
	BB_10: BasicBlock(start=33,end=33) -> {BB_8}
	BB_11: BasicBlock(start=22,end=22) -> {BB_8}
	BB_12: BasicBlock(start=27,end=27) -> {BB_14,BB_e}
	BB_13: BasicBlock(start=4,end=7) -> {BB_14,BB_c}
	BB_14: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=25,end=26) -> {BB_14,BB_12}
	BB_2: BasicBlock(start=29,end=32) -> {BB_14,BB_10}
	BB_3: BasicBlock(start=1,end=2) -> {BB_4,BB_7}
	BB_4: BasicBlock(start=9,end=10) -> {BB_a,BB_5}
	BB_5: BasicBlock(start=17,end=18) -> {BB_d,BB_b}
	BB_6: BasicBlock(start=12,end=15) -> {BB_14,BB_9}
	BB_7: BasicBlock(start=3,end=3) -> {BB_14,BB_13}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=16,end=16) -> {BB_8}
	BB_a: BasicBlock(start=11,end=11) -> {BB_14,BB_6}
	BB_b: BasicBlock(start=23,end=24) -> {BB_1,BB_2}
	BB_c: BasicBlock(start=8,end=8) -> {BB_8}
	BB_d: BasicBlock(start=19,end=20) -> {BB_14,BB_f}
	BB_e: BasicBlock(start=28,end=28) -> {BB_8}
	BB_f: BasicBlock(start=21,end=21) -> {BB_14,BB_11}
))

void normalizeClazz(java.lang.String,int,int,java.lang.StringBuilder)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4),
	4: useSites={3} (origin=-5)
)),stmts=(
	0: Assignment(pc=4,DVar(useSites={2},value={java.lang.String, null}[↦4;refId=106],origin=0),VirtualFunctionCall(pc=4,java.lang.String,isInterface=false,java.lang.String substring(int,int),UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),(UVar(defSites={-3},value=an int),UVar(defSites={-4},value=an int)))),
	1: Assignment(pc=7,DVar(useSites={2},value={java.text.Normalizer$Form, null}[↦7;refId=107],origin=1),GetStatic(pc=7,java.text.Normalizer$Form,NFC,java.text.Normalizer$Form)),
	2: Assignment(pc=10,DVar(useSites={3},value={java.lang.String, null}[↦10;refId=109],origin=2),StaticFunctionCall(pc=10,java.text.Normalizer,isInterface=false,java.lang.String normalize(java.lang.CharSequence,java.text.Normalizer$Form),(UVar(defSites={0},value={java.lang.String, null}[↦4;refId=106]),UVar(defSites={1},value={java.text.Normalizer$Form, null}[↦7;refId=107])))),
	3: ExprStmt(pc=13,VirtualFunctionCall(pc=13,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={2},value={java.lang.String, null}[↦10;refId=109])))),
	4: Return(pc=17)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_5,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_5,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_5,BB_4}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_3}
	BB_5: ExitNode(normalReturn=false)
))

boolean lambda$SingleI$9(int,int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={0,1} (origin=-4)
)),stmts=(
	0: If(pc=2,UVar(defSites={-4},value=an int),==,UVar(defSites={-2},value=an int),target=2),
	1: If(pc=7,UVar(defSites={-4},value=an int),!=,UVar(defSites={-3},value=an int),target=4),
	2: Assignment(pc=10,DVar(useSites={5},value=int = 1,origin=2),IntConst(pc=10,1)),
	3: Goto(pc=11,target=5),
	4: Assignment(pc=14,DVar(useSites={5},value=int ∈ [0,1],origin=4),IntConst(pc=14,0)),
	5: ReturnValue(pc=15,UVar(defSites={4,2},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_4}
	BB_2: BasicBlock(start=1,end=1) -> {BB_3,BB_5}
	BB_3: BasicBlock(start=2,end=3) -> {BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=4,end=4) -> {BB_1}
	BB_6: ExitNode(normalReturn=false)
))

int peekPastWhitespace(int)
AITACode(params=(Parameters(
	0: useSites={10,6,7,15} (origin=-1),
	1: useSites={0,4,14,17,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),StaticFunctionCall(pc=1,java.util.regex.ASCII,isInterface=false,boolean isSpace(int),(UVar(defSites={-2,11,15},value=an int)))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=8,DVar(useSites={3},value=int = 35,origin=2),IntConst(pc=8,35)),
	3: If(pc=10,UVar(defSites={-2,11,15},value=an int),!=,UVar(defSites={2},value=int = 35),target=17),
	4: Assignment(pc=14,DVar(useSites={5},value=int ∈ [0,1],origin=4),StaticFunctionCall(pc=14,java.util.regex.ASCII,isInterface=false,boolean isSpace(int),(UVar(defSites={-2,11,15},value=an int)))),
	5: If(pc=17,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=13),
	6: Assignment(pc=21,DVar(useSites={11},value={int[], null}[↦21;refId=105],origin=6),GetField(pc=21,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	7: Assignment(pc=26,DVar(useSites={9},value=an int,origin=7),GetField(pc=26,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	8: Assignment(pc=29,DVar(useSites={9},value=int = 1,origin=8),IntConst(pc=29,1)),
	9: Assignment(pc=30,DVar(useSites={10,11},value=an int,origin=9),BinaryExpr(pc=30,ComputationalTypeInt,UVar(defSites={7},value=an int),+,UVar(defSites={8},value=int = 1))),
	10: PutField(pc=32,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={9},value=an int)),
	11: Assignment(pc=35,DVar(useSites={0,4,14,17,3},value=an int,origin=11),ArrayLoad(pc=35,UVar(defSites={9},value=an int),UVar(defSites={6},value={int[], null}[↦21;refId=105]))),
	12: Goto(pc=37,target=4),
	13: Assignment(pc=41,DVar(useSites={14},value=int = 35,origin=13),IntConst(pc=41,35)),
	14: If(pc=43,UVar(defSites={-2,11,15},value=an int),!=,UVar(defSites={13},value=int = 35),target=0),
	15: Assignment(pc=47,DVar(useSites={0,4,14,17,3},value=an int,origin=15),VirtualFunctionCall(pc=47,java.util.regex.Pattern,isInterface=false,int peekPastLine(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	16: Goto(pc=51,target=0),
	17: ReturnValue(pc=55,UVar(defSites={-2,11,15},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_4,BB_3}
	BB_2: BasicBlock(start=1,end=1) -> {BB_b,BB_5}
	BB_3: BasicBlock(start=6,end=11) -> {BB_c,BB_7}
	BB_4: BasicBlock(start=13,end=14) -> {BB_0,BB_a}
	BB_5: BasicBlock(start=2,end=3) -> {BB_6,BB_b}
	BB_6: BasicBlock(start=17,end=17) -> {BB_8}
	BB_7: BasicBlock(start=12,end=12) -> {BB_b}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=16,end=16) -> {BB_0}
	BB_a: BasicBlock(start=15,end=15) -> {BB_c,BB_9}
	BB_b: BasicBlock(start=4,end=4) -> {BB_c,BB_1}
	BB_c: ExitNode(normalReturn=false)
))

boolean lambda$CIRangeU$14(int,int,int)
AITACode(params=(Parameters(
	1: useSites={0,8,5} (origin=-2),
	2: useSites={0,8,5} (origin=-3),
	3: useSites={0,4} (origin=-4)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={1},value=int ∈ [0,1],origin=0),StaticFunctionCall(pc=3,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-4},value=an int),UVar(defSites={-3},value=an int)))),
	1: If(pc=6,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=9,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=9,1)),
	3: ReturnValue(pc=10,UVar(defSites={2},value=int = 1)),
	4: Assignment(pc=12,DVar(useSites={5,7},value=an int,origin=4),StaticFunctionCall(pc=12,java.lang.Character,isInterface=false,int toUpperCase(int),(UVar(defSites={-4},value=an int)))),
	5: Assignment(pc=19,DVar(useSites={6},value=int ∈ [0,1],origin=5),StaticFunctionCall(pc=19,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={4},value=an int),UVar(defSites={-3},value=an int)))),
	6: If(pc=22,UVar(defSites={5},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=10),
	7: Assignment(pc=27,DVar(useSites={8},value=an int,origin=7),StaticFunctionCall(pc=27,java.lang.Character,isInterface=false,int toLowerCase(int),(UVar(defSites={4},value=an int)))),
	8: Assignment(pc=31,DVar(useSites={9},value=int ∈ [0,1],origin=8),StaticFunctionCall(pc=31,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={7},value=an int),UVar(defSites={-3},value=an int)))),
	9: If(pc=34,UVar(defSites={8},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	10: Assignment(pc=37,DVar(useSites={13},value=int = 1,origin=10),IntConst(pc=37,1)),
	11: Goto(pc=38,target=13),
	12: Assignment(pc=41,DVar(useSites={13},value=int ∈ [0,1],origin=12),IntConst(pc=41,0)),
	13: ReturnValue(pc=42,UVar(defSites={12,10},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_d,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_d,BB_4}
	BB_2: BasicBlock(start=10,end=11) -> {BB_6}
	BB_3: BasicBlock(start=1,end=1) -> {BB_7,BB_c}
	BB_4: BasicBlock(start=6,end=6) -> {BB_9,BB_2}
	BB_5: BasicBlock(start=9,end=9) -> {BB_8,BB_2}
	BB_6: BasicBlock(start=13,end=13) -> {BB_a}
	BB_7: BasicBlock(start=2,end=3) -> {BB_a}
	BB_8: BasicBlock(start=12,end=12) -> {BB_6}
	BB_9: BasicBlock(start=7,end=7) -> {BB_d,BB_b}
	BB_a: ExitNode(normalReturn=true)
	BB_b: BasicBlock(start=8,end=8) -> {BB_d,BB_5}
	BB_c: BasicBlock(start=4,end=4) -> {BB_d,BB_1}
	BB_d: ExitNode(normalReturn=false)
))

void unread()
AITACode(params=(Parameters(
	0: useSites={0,3} (origin=-1)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=5,1)),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=6,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={1},value=int = 1))),
	3: PutField(pc=7,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={2},value=an int)),
	4: Return(pc=10)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=4) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

int peekPastLine()
AITACode(params=(Parameters(
	0: useSites={0,8,24,4,18,10,22,14,1,21,19,11,23} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={5},value={int[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={3},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=9,1)),
	3: Assignment(pc=10,DVar(useSites={4,5},value=an int,origin=3),BinaryExpr(pc=10,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={2},value=int = 1))),
	4: PutField(pc=12,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=15,DVar(useSites={8,17,27,7},value=an int,origin=5),ArrayLoad(pc=15,UVar(defSites={3},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=103]))),
	6: Nop(pc=16),
	7: If(pc=18,UVar(defSites={5,15},value=an int),==,IntConst(pc=-333,0),target=17),
	8: Assignment(pc=23,DVar(useSites={9},value=int ∈ [0,1],origin=8),VirtualFunctionCall(pc=23,java.util.regex.Pattern,isInterface=false,boolean isLineSeparator(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={5,15},value=an int)))),
	9: If(pc=26,UVar(defSites={8},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=17),
	10: Assignment(pc=30,DVar(useSites={15},value={int[], null}[↦30;refId=107],origin=10),GetField(pc=30,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	11: Assignment(pc=35,DVar(useSites={13},value=an int,origin=11),GetField(pc=35,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	12: Assignment(pc=38,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=38,1)),
	13: Assignment(pc=39,DVar(useSites={14,15},value=an int,origin=13),BinaryExpr(pc=39,ComputationalTypeInt,UVar(defSites={11},value=an int),+,UVar(defSites={12},value=int = 1))),
	14: PutField(pc=41,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={13},value=an int)),
	15: Assignment(pc=44,DVar(useSites={8,17,27,7},value=an int,origin=15),ArrayLoad(pc=44,UVar(defSites={13},value=an int),UVar(defSites={10},value={int[], null}[↦30;refId=107]))),
	16: Goto(pc=46,target=7),
	17: If(pc=50,UVar(defSites={5,15},value=an int),!=,IntConst(pc=-333,0),target=27),
	18: Assignment(pc=54,DVar(useSites={20},value=an int,origin=18),GetField(pc=54,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	19: Assignment(pc=58,DVar(useSites={20},value=an int,origin=19),GetField(pc=58,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	20: If(pc=61,UVar(defSites={18},value=an int),<=,UVar(defSites={19},value=an int),target=27),
	21: Assignment(pc=66,DVar(useSites={22},value=an int,origin=21),GetField(pc=66,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	22: PutField(pc=69,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={21},value=an int)),
	23: Assignment(pc=73,DVar(useSites={25},value={int[], null}[↦73;refId=110],origin=23),GetField(pc=73,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	24: Assignment(pc=77,DVar(useSites={25},value=an int,origin=24),GetField(pc=77,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	25: Assignment(pc=80,DVar(useSites={27},value=an int,origin=25),ArrayLoad(pc=80,UVar(defSites={24},value=an int),UVar(defSites={23},value={int[], null}[↦73;refId=110]))),
	26: Nop(pc=81),
	27: ReturnValue(pc=83,UVar(defSites={25,5,15},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_b,BB_2}
	BB_1: BasicBlock(start=10,end=15) -> {BB_b,BB_8}
	BB_2: BasicBlock(start=6,end=6) -> {BB_7}
	BB_3: BasicBlock(start=21,end=25) -> {BB_b,BB_9}
	BB_4: BasicBlock(start=9,end=9) -> {BB_5,BB_1}
	BB_5: BasicBlock(start=17,end=17) -> {BB_6,BB_c}
	BB_6: BasicBlock(start=27,end=27) -> {BB_d}
	BB_7: BasicBlock(start=7,end=7) -> {BB_5,BB_a}
	BB_8: BasicBlock(start=16,end=16) -> {BB_7}
	BB_9: BasicBlock(start=26,end=26) -> {BB_6}
	BB_a: BasicBlock(start=8,end=8) -> {BB_b,BB_4}
	BB_b: ExitNode(normalReturn=false)
	BB_c: BasicBlock(start=18,end=20) -> {BB_3,BB_6}
	BB_d: ExitNode(normalReturn=true)
))

int u()
AITACode(params=(Parameters(
	0: useSites={0,8,4,5,19,11} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={20,1,15},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int uxxxx(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Assignment(pc=6,DVar(useSites={2},value=int ∈ [0,65535],origin=1),PrimitiveTypecastExpr(pc=6,CharType,UVar(defSites={0},value=an int))),
	2: Assignment(pc=7,DVar(useSites={3},value=int ∈ [0,1],origin=2),StaticFunctionCall(pc=7,java.lang.Character,isInterface=false,boolean isHighSurrogate(char),(UVar(defSites={1},value=int ∈ [0,65535])))),
	3: If(pc=10,UVar(defSites={2},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=20),
	4: Assignment(pc=14,DVar(useSites={19},value=an int,origin=4),VirtualFunctionCall(pc=14,java.util.regex.Pattern,isInterface=false,int cursor(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	5: Assignment(pc=19,DVar(useSites={7},value=an int,origin=5),VirtualFunctionCall(pc=19,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	6: Assignment(pc=22,DVar(useSites={7},value=int = 92,origin=6),IntConst(pc=22,92)),
	7: If(pc=24,UVar(defSites={5},value=an int),!=,UVar(defSites={6},value=int = 92),target=19),
	8: Assignment(pc=28,DVar(useSites={10},value=an int,origin=8),VirtualFunctionCall(pc=28,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	9: Assignment(pc=31,DVar(useSites={10},value=int = 117,origin=9),IntConst(pc=31,117)),
	10: If(pc=33,UVar(defSites={8},value=an int),!=,UVar(defSites={9},value=int = 117),target=19),
	11: Assignment(pc=37,DVar(useSites={16,12},value=an int,origin=11),VirtualFunctionCall(pc=37,java.util.regex.Pattern,isInterface=false,int uxxxx(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	12: Assignment(pc=42,DVar(useSites={13},value=int ∈ [0,65535],origin=12),PrimitiveTypecastExpr(pc=42,CharType,UVar(defSites={11},value=an int))),
	13: Assignment(pc=43,DVar(useSites={14},value=int ∈ [0,1],origin=13),StaticFunctionCall(pc=43,java.lang.Character,isInterface=false,boolean isLowSurrogate(char),(UVar(defSites={12},value=int ∈ [0,65535])))),
	14: If(pc=46,UVar(defSites={13},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=19),
	15: Assignment(pc=50,DVar(useSites={17},value=int ∈ [0,65535],origin=15),PrimitiveTypecastExpr(pc=50,CharType,UVar(defSites={0},value=an int))),
	16: Assignment(pc=52,DVar(useSites={17},value=int ∈ [0,65535],origin=16),PrimitiveTypecastExpr(pc=52,CharType,UVar(defSites={11},value=an int))),
	17: Assignment(pc=53,DVar(useSites={18},value=an int,origin=17),StaticFunctionCall(pc=53,java.lang.Character,isInterface=false,int toCodePoint(char,char),(UVar(defSites={15},value=int ∈ [0,65535]),UVar(defSites={16},value=int ∈ [0,65535])))),
	18: ReturnValue(pc=56,UVar(defSites={17},value=an int)),
	19: VirtualMethodCall(pc=59,java.util.regex.Pattern,isInterface=false,void setcursor(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={4},value=an int))),
	20: ReturnValue(pc=63,UVar(defSites={0},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_10,BB_4}
	BB_10: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_10,BB_5}
	BB_2: BasicBlock(start=14,end=14) -> {BB_c,BB_b}
	BB_3: BasicBlock(start=20,end=20) -> {BB_e}
	BB_4: BasicBlock(start=1,end=2) -> {BB_10,BB_8}
	BB_5: BasicBlock(start=6,end=7) -> {BB_b,BB_a}
	BB_6: BasicBlock(start=9,end=10) -> {BB_9,BB_b}
	BB_7: BasicBlock(start=12,end=13) -> {BB_10,BB_2}
	BB_8: BasicBlock(start=3,end=3) -> {BB_3,BB_f}
	BB_9: BasicBlock(start=11,end=11) -> {BB_10,BB_7}
	BB_a: BasicBlock(start=8,end=8) -> {BB_10,BB_6}
	BB_b: BasicBlock(start=19,end=19) -> {BB_10,BB_3}
	BB_c: BasicBlock(start=15,end=17) -> {BB_10,BB_d}
	BB_d: BasicBlock(start=18,end=18) -> {BB_e}
	BB_e: ExitNode(normalReturn=true)
	BB_f: BasicBlock(start=4,end=4) -> {BB_10,BB_1}
))

java.util.regex.Matcher matcher(java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,12,2,6,9,5,3} (origin=-1),
	1: useSites={12} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Pattern,compiled,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=11),
	2: MonitorEnter(pc=10,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102])),
	3: Assignment(pc=12,DVar(useSites={4},value=int ∈ [0,1],origin=3),GetField(pc=12,java.util.regex.Pattern,compiled,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	4: If(pc=15,UVar(defSites={3},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=6),
	5: VirtualMethodCall(pc=19,java.util.regex.Pattern,isInterface=false,void compile(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	6: MonitorExit(pc=23,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102])),
	7: Goto(pc=24,target=11),
	8: CaughtException(pc=27,<ANY>,caused by={exception[VM]@6,exception@5,exception[VM]@9}),
	9: MonitorExit(pc=29,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102])),
	10: Throw(pc=31,UVar(defSites={-100006,-1000005,-100009},value=_ <: java.lang.Throwable[refId=111; values=«_ <: java.lang.Throwable[↦-1000019;refId=104], java.lang.IllegalMonitorStateException[↦-100023;refId=108], java.lang.IllegalMonitorStateException[↦-100029;refId=110]»])),
	11: Assignment(pc=32,DVar(useSites={12,13},value=java.util.regex.Matcher[↦32;refId=105],origin=11),New(pc=32,java.util.regex.Matcher)),
	12: NonVirtualMethodCall(pc=38,java.util.regex.Matcher,isInterface=false,void <init>(java.util.regex.Pattern,java.lang.CharSequence),UVar(defSites={11},value=java.util.regex.Matcher[↦32;refId=105]),(UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.lang.CharSequence, null}[↦-2;refId=103]))),
	13: ReturnValue(pc=43,UVar(defSites={11},value=java.util.regex.Matcher[↦32;refId=105]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_9,BB_6}
	BB_1: BasicBlock(start=5,end=5) -> {BB_4,BB_3}
	BB_2: BasicBlock(start=10,end=10) -> {BB_b}
	BB_3: CatchNode([-1,7)=>8,<none>) -> {BB_a}
	BB_4: BasicBlock(start=6,end=6) -> {BB_7,BB_3}
	BB_5: BasicBlock(start=13,end=13) -> {BB_8,BB_b}
	BB_6: BasicBlock(start=2,end=4) -> {BB_1,BB_4}
	BB_7: BasicBlock(start=7,end=7) -> {BB_9}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=11,end=12) -> {BB_b,BB_5}
	BB_a: BasicBlock(start=8,end=9) -> {BB_2,BB_3}
	BB_b: ExitNode(normalReturn=false)
),exceptionHandlers=(
	ExceptionHandler([-1, 7) -> 8, <FINALLY>),
	ExceptionHandler([8, 10) -> 8, <FINALLY>)
))

boolean findSupplementary(int,int)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={8,1,3} (origin=-2),
	2: useSites={1} (origin=-3)
)),stmts=(
	0: Nop(pc=0),
	1: If(pc=4,UVar(defSites={8,-2},value=an int),>=,UVar(defSites={-3},value=an int),target=10),
	2: Assignment(pc=8,DVar(useSites={3},value={int[], null}[↦8;refId=103],origin=2),GetField(pc=8,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	3: Assignment(pc=12,DVar(useSites={4},value=an int,origin=3),ArrayLoad(pc=12,UVar(defSites={8,-2},value=int ∈ [-2147483648,2147483646]),UVar(defSites={2},value={int[], null}[↦8;refId=103]))),
	4: Assignment(pc=13,DVar(useSites={5},value=int ∈ [0,1],origin=4),StaticFunctionCall(pc=13,java.util.regex.Pattern,isInterface=false,boolean isSupplementary(int),(UVar(defSites={3},value=an int)))),
	5: If(pc=16,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=8),
	6: Assignment(pc=19,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=19,1)),
	7: ReturnValue(pc=20,UVar(defSites={6},value=int = 1)),
	8: Assignment(pc=21,DVar(useSites={1,9,3},value=int ∈ [-2147483647,2147483647],origin=8),BinaryExpr(pc=21,ComputationalTypeInt,UVar(defSites={8,-2},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=21,1))),
	9: Goto(pc=24,target=1),
	10: Assignment(pc=27,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=27,0)),
	11: ReturnValue(pc=28,UVar(defSites={10},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_7,BB_4}
	BB_2: BasicBlock(start=10,end=11) -> {BB_6}
	BB_3: BasicBlock(start=1,end=1) -> {BB_2,BB_5}
	BB_4: BasicBlock(start=6,end=7) -> {BB_6}
	BB_5: BasicBlock(start=2,end=3) -> {BB_9,BB_8}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=8,end=9) -> {BB_3}
	BB_8: BasicBlock(start=4,end=4) -> {BB_9,BB_1}
	BB_9: ExitNode(normalReturn=false)
))

void compile()
AITACode(params=(Parameters(
	0: useSites={32,144,80,48,8,136,40,24,88,56,120,4,68,100,148,12,140,108,60,98,146,82,50,114,10,42,26,58,6,70,38,102,150,54,118,14,142,94,62,1,73,105,89,121,133,69,21,85,77,45,109,61,19,11,91,59,123,71,87,15,111,31,63} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 128,origin=0),IntConst(pc=1,128)),
	1: Assignment(pc=4,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=4,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={0},value=int = 128)))),
	2: If(pc=7,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=10),
	3: Assignment(pc=11,DVar(useSites={4},value=int = 16,origin=3),IntConst(pc=11,16)),
	4: Assignment(pc=13,DVar(useSites={5},value=int ∈ [0,1],origin=4),VirtualFunctionCall(pc=13,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={3},value=int = 16)))),
	5: If(pc=16,UVar(defSites={4},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=10),
	6: Assignment(pc=21,DVar(useSites={7},value={java.lang.String, null}[↦21;refId=105],origin=6),GetField(pc=21,java.util.regex.Pattern,pattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	7: Assignment(pc=24,DVar(useSites={8},value={java.lang.String, null}[↦24;refId=107],origin=7),StaticFunctionCall(pc=24,java.util.regex.Pattern,isInterface=false,java.lang.String normalize(java.lang.String),(UVar(defSites={6},value={java.lang.String, null}[↦21;refId=105])))),
	8: PutField(pc=27,java.util.regex.Pattern,normalizedPattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={7},value={java.lang.String, null}[↦24;refId=107])),
	9: Goto(pc=30,target=12),
	10: Assignment(pc=35,DVar(useSites={11},value={java.lang.String, null}[↦35;refId=108],origin=10),GetField(pc=35,java.util.regex.Pattern,pattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	11: PutField(pc=38,java.util.regex.Pattern,normalizedPattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={10},value={java.lang.String, null}[↦35;refId=108])),
	12: Assignment(pc=43,DVar(useSites={13},value={java.lang.String, null}[↦43;refId=109],origin=12),GetField(pc=43,java.util.regex.Pattern,normalizedPattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	13: Assignment(pc=46,DVar(useSites={14},value=an int,origin=13),VirtualFunctionCall(pc=46,java.lang.String,isInterface=false,int length(),UVar(defSites={12},value={java.lang.String, null}[↦43;refId=109]),())),
	14: PutField(pc=49,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={13},value=an int)),
	15: Assignment(pc=54,DVar(useSites={17},value=an int,origin=15),GetField(pc=54,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	16: Assignment(pc=57,DVar(useSites={17},value=int = 2,origin=16),IntConst(pc=57,2)),
	17: Assignment(pc=58,DVar(useSites={18},value=an int,origin=17),BinaryExpr(pc=58,ComputationalTypeInt,UVar(defSites={15},value=an int),+,UVar(defSites={16},value=int = 2))),
	18: Assignment(pc=59,DVar(useSites={19},value=int[][↦59;refId=112],origin=18),NewArray(pc=59,[UVar(defSites={17},value=an int)],int[])),
	19: PutField(pc=61,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={18},value=int[][↦59;refId=112])),
	20: Assignment(pc=65,DVar(useSites={21},value=int = 0,origin=20),IntConst(pc=65,0)),
	21: PutField(pc=66,java.util.regex.Pattern,hasSupplementary,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={20},value=int = 0)),
	22: Assignment(pc=69,DVar(useSites={34,38,33},value=int = 0,origin=22),IntConst(pc=69,0)),
	23: Assignment(pc=71,DVar(useSites={36,25,27},value=int = 0,origin=23),IntConst(pc=71,0)),
	24: Assignment(pc=75,DVar(useSites={25},value=an int,origin=24),GetField(pc=75,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	25: If(pc=78,UVar(defSites={36,23},value=an int),>=,UVar(defSites={24},value=an int),target=38),
	26: Assignment(pc=82,DVar(useSites={27},value={java.lang.String, null}[↦82;refId=385],origin=26),GetField(pc=82,java.util.regex.Pattern,normalizedPattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	27: Assignment(pc=86,DVar(useSites={28,34,35},value=an int,origin=27),VirtualFunctionCall(pc=86,java.lang.String,isInterface=false,int codePointAt(int),UVar(defSites={26},value={java.lang.String, null}[↦82;refId=385]),(UVar(defSites={36,23},value=int ∈ [-2147483648,2147483646])))),
	28: Assignment(pc=91,DVar(useSites={29},value=int ∈ [0,1],origin=28),StaticFunctionCall(pc=91,java.util.regex.Pattern,isInterface=false,boolean isSupplementary(int),(UVar(defSites={27},value=an int)))),
	29: If(pc=94,UVar(defSites={28},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=32),
	30: Assignment(pc=98,DVar(useSites={31},value=int = 1,origin=30),IntConst(pc=98,1)),
	31: PutField(pc=99,java.util.regex.Pattern,hasSupplementary,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={30},value=int = 1)),
	32: Assignment(pc=103,DVar(useSites={34},value={int[], null}[↦103;refId=389],origin=32),GetField(pc=103,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	33: Assignment(pc=107,DVar(useSites={34,38},value=an int,origin=33),BinaryExpr(pc=107,ComputationalTypeInt,UVar(defSites={22,33},value=an int),+,IntConst(pc=107,1))),
	34: ArrayStore(pc=111,UVar(defSites={32},value={int[], null}[↦103;refId=389]),UVar(defSites={22,33},value=an int),UVar(defSites={27},value=an int)),
	35: Assignment(pc=114,DVar(useSites={36},value=an int,origin=35),StaticFunctionCall(pc=114,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={27},value=an int)))),
	36: Assignment(pc=117,DVar(useSites={25,37,27},value=an int,origin=36),BinaryExpr(pc=117,ComputationalTypeInt,UVar(defSites={36,23},value=an int),+,UVar(defSites={35},value=an int))),
	37: Goto(pc=119,target=24),
	38: PutField(pc=124,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={22,33},value=an int)),
	39: Assignment(pc=128,DVar(useSites={40},value=int = 16,origin=39),IntConst(pc=128,16)),
	40: Assignment(pc=130,DVar(useSites={41},value=int ∈ [0,1],origin=40),VirtualFunctionCall(pc=130,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={39},value=int = 16)))),
	41: If(pc=133,UVar(defSites={40},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=43),
	42: VirtualMethodCall(pc=137,java.util.regex.Pattern,isInterface=false,void RemoveQEQuoting(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	43: Assignment(pc=141,DVar(useSites={44},value=int = 32,origin=43),IntConst(pc=141,32)),
	44: Assignment(pc=143,DVar(useSites={45},value=int[][↦143;refId=120;length=32],origin=44),NewArray(pc=143,[UVar(defSites={43},value=int = 32)],int[])),
	45: PutField(pc=145,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={44},value=int[][↦143;refId=120;length=32])),
	46: Assignment(pc=149,DVar(useSites={47},value=int = 10,origin=46),IntConst(pc=149,10)),
	47: Assignment(pc=151,DVar(useSites={48},value=java.util.regex.Pattern$GroupHead[][↦151;refId=121;length=10],origin=47),NewArray(pc=151,[UVar(defSites={46},value=int = 10)],java.util.regex.Pattern$GroupHead[])),
	48: PutField(pc=154,java.util.regex.Pattern,groupNodes,java.util.regex.Pattern$GroupHead[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={47},value=java.util.regex.Pattern$GroupHead[][↦151;refId=121;length=10])),
	49: Assignment(pc=158,DVar(useSites={50},value=null[↦158],origin=49),NullExpr(pc=158)),
	50: PutField(pc=159,java.util.regex.Pattern,namedGroups,java.util.Map,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={49},value=null[↦158])),
	51: Assignment(pc=163,DVar(useSites={54,53},value=java.util.ArrayList[↦163;refId=122],origin=51),New(pc=163,java.util.ArrayList)),
	52: Assignment(pc=167,DVar(useSites={53},value=int = 10,origin=52),IntConst(pc=167,10)),
	53: NonVirtualMethodCall(pc=169,java.util.ArrayList,isInterface=false,void <init>(int),UVar(defSites={51},value=java.util.ArrayList[↦163;refId=122]),(UVar(defSites={52},value=int = 10))),
	54: PutField(pc=172,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={51},value=java.util.ArrayList[↦163;refId=122])),
	55: Assignment(pc=176,DVar(useSites={56},value=int = 16,origin=55),IntConst(pc=176,16)),
	56: Assignment(pc=178,DVar(useSites={57},value=int ∈ [0,1],origin=56),VirtualFunctionCall(pc=178,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={55},value=int = 16)))),
	57: If(pc=181,UVar(defSites={56},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=67),
	58: Assignment(pc=187,DVar(useSites={61},value={int[], null}[↦187;refId=125],origin=58),GetField(pc=187,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	59: Assignment(pc=191,DVar(useSites={61},value=an int,origin=59),GetField(pc=191,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	60: Assignment(pc=195,DVar(useSites={61},value=int ∈ [0,1],origin=60),GetField(pc=195,java.util.regex.Pattern,hasSupplementary,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	61: Assignment(pc=198,DVar(useSites={62},value={_ <: java.util.regex.Pattern$Node, null}[↦198;refId=127],origin=61),VirtualFunctionCall(pc=198,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node newSlice(int[],int,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={58},value={int[], null}[↦187;refId=125]),UVar(defSites={59},value=an int),UVar(defSites={60},value=int ∈ [0,1])))),
	62: PutField(pc=201,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={61},value={_ <: java.util.regex.Pattern$Node, null}[↦198;refId=127])),
	63: Assignment(pc=205,DVar(useSites={65},value={_ <: java.util.regex.Pattern$Node, null}[↦205;refId=128],origin=63),GetField(pc=205,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	64: Assignment(pc=208,DVar(useSites={65},value={_ <: java.util.regex.Pattern$Node, null}[↦208;refId=129],origin=64),GetStatic(pc=208,java.util.regex.Pattern,lastAccept,java.util.regex.Pattern$Node)),
	65: PutField(pc=211,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={63},value={_ <: java.util.regex.Pattern$Node, null}[↦205;refId=128]),UVar(defSites={64},value={_ <: java.util.regex.Pattern$Node, null}[↦208;refId=129])),
	66: Goto(pc=214,target=82),
	67: Assignment(pc=219,DVar(useSites={68},value={_ <: java.util.regex.Pattern$Node, null}[↦219;refId=131],origin=67),GetStatic(pc=219,java.util.regex.Pattern,lastAccept,java.util.regex.Pattern$Node)),
	68: Assignment(pc=222,DVar(useSites={69},value={_ <: java.util.regex.Pattern$Node, null}[↦222;refId=133],origin=68),VirtualFunctionCall(pc=222,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={67},value={_ <: java.util.regex.Pattern$Node, null}[↦219;refId=131])))),
	69: PutField(pc=225,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={68},value={_ <: java.util.regex.Pattern$Node, null}[↦222;refId=133])),
	70: Assignment(pc=229,DVar(useSites={72},value=an int,origin=70),GetField(pc=229,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	71: Assignment(pc=233,DVar(useSites={72},value=an int,origin=71),GetField(pc=233,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	72: If(pc=236,UVar(defSites={70},value=an int),==,UVar(defSites={71},value=an int),target=82),
	73: Assignment(pc=240,DVar(useSites={75},value=an int,origin=73),VirtualFunctionCall(pc=240,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	74: Assignment(pc=243,DVar(useSites={75},value=int = 41,origin=74),IntConst(pc=243,41)),
	75: If(pc=245,UVar(defSites={73},value=an int),!=,UVar(defSites={74},value=int = 41),target=79),
	76: Assignment(pc=249,DVar(useSites={77},value=String("Unmatched closing ')'")[@249;refId=139],origin=76),StringConst(pc=249,Unmatched closing ')')),
	77: Assignment(pc=251,DVar(useSites={78},value={_ <: java.util.regex.PatternSyntaxException, null}[↦251;refId=141],origin=77),VirtualFunctionCall(pc=251,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={76},value=String("Unmatched closing ')'")[@249;refId=139])))),
	78: Throw(pc=254,UVar(defSites={77},value={_ <: java.util.regex.PatternSyntaxException, null}[↦251;refId=141])),
	79: Assignment(pc=256,DVar(useSites={80},value=String("Unexpected internal error")[@256;refId=135],origin=79),StringConst(pc=256,Unexpected internal error)),
	80: Assignment(pc=258,DVar(useSites={81},value={_ <: java.util.regex.PatternSyntaxException, null}[↦258;refId=137],origin=80),VirtualFunctionCall(pc=258,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={79},value=String("Unexpected internal error")[@256;refId=135])))),
	81: Throw(pc=261,UVar(defSites={80},value={_ <: java.util.regex.PatternSyntaxException, null}[↦258;refId=137])),
	82: Assignment(pc=263,DVar(useSites={83},value={_ <: java.util.regex.Pattern$Node, null}[↦263;refId=147],origin=82),GetField(pc=263,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	83: Assignment(pc=266,DVar(useSites={84},value=int ∈ [0,1],origin=83),InstanceOf(pc=266,UVar(defSites={82},value={_ <: java.util.regex.Pattern$Node, null}[↦263;refId=147]),java.util.regex.Pattern$Slice)),
	84: If(pc=269,UVar(defSites={83},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=102),
	85: Assignment(pc=274,DVar(useSites={86},value={_ <: java.util.regex.Pattern$Node, null}[↦274;refId=148],origin=85),GetField(pc=274,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	86: Assignment(pc=277,DVar(useSites={87},value={_ <: java.util.regex.Pattern$Node, null}[↦277;refId=150],origin=86),StaticFunctionCall(pc=277,java.util.regex.Pattern$BnM,isInterface=false,java.util.regex.Pattern$Node optimize(java.util.regex.Pattern$Node),(UVar(defSites={85},value={_ <: java.util.regex.Pattern$Node, null}[↦274;refId=148])))),
	87: PutField(pc=280,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={86},value={_ <: java.util.regex.Pattern$Node, null}[↦277;refId=150])),
	88: Assignment(pc=284,DVar(useSites={90},value={_ <: java.util.regex.Pattern$Node, null}[↦284;refId=151],origin=88),GetField(pc=284,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	89: Assignment(pc=288,DVar(useSites={90},value={_ <: java.util.regex.Pattern$Node, null}[↦288;refId=152],origin=89),GetField(pc=288,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	90: If(pc=291,UVar(defSites={88},value={_ <: java.util.regex.Pattern$Node, null}[↦284;refId=151]),!=,UVar(defSites={89},value={_ <: java.util.regex.Pattern$Node, null}[↦288;refId=152]),target=121),
	91: Assignment(pc=296,DVar(useSites={92},value=int ∈ [0,1],origin=91),GetField(pc=296,java.util.regex.Pattern,hasSupplementary,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	92: If(pc=299,UVar(defSites={91},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=97),
	93: Assignment(pc=302,DVar(useSites={100,95},value=java.util.regex.Pattern$StartS[↦302;refId=153],origin=93),New(pc=302,java.util.regex.Pattern$StartS)),
	94: Assignment(pc=307,DVar(useSites={95},value={_ <: java.util.regex.Pattern$Node, null}[↦307;refId=154],origin=94),GetField(pc=307,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	95: NonVirtualMethodCall(pc=310,java.util.regex.Pattern$StartS,isInterface=false,void <init>(java.util.regex.Pattern$Node),UVar(defSites={93},value=java.util.regex.Pattern$StartS[↦302;refId=153]),(UVar(defSites={94},value={_ <: java.util.regex.Pattern$Node, null}[↦307;refId=154]))),
	96: Goto(pc=313,target=100),
	97: Assignment(pc=316,DVar(useSites={100,99},value=java.util.regex.Pattern$Start[↦316;refId=156],origin=97),New(pc=316,java.util.regex.Pattern$Start)),
	98: Assignment(pc=321,DVar(useSites={99},value={_ <: java.util.regex.Pattern$Node, null}[↦321;refId=157],origin=98),GetField(pc=321,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	99: NonVirtualMethodCall(pc=324,java.util.regex.Pattern$Start,isInterface=false,void <init>(java.util.regex.Pattern$Node),UVar(defSites={97},value=java.util.regex.Pattern$Start[↦316;refId=156]),(UVar(defSites={98},value={_ <: java.util.regex.Pattern$Node, null}[↦321;refId=157]))),
	100: PutField(pc=327,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={97,93},value=_ <: java.util.regex.Pattern$Start[refId=159; values=«java.util.regex.Pattern$StartS[↦302;refId=153], java.util.regex.Pattern$Start[↦316;refId=156]»])),
	101: Goto(pc=330,target=121),
	102: Assignment(pc=334,DVar(useSites={103},value={_ <: java.util.regex.Pattern$Node, null}[↦334;refId=160],origin=102),GetField(pc=334,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	103: Assignment(pc=337,DVar(useSites={104},value=int ∈ [0,1],origin=103),InstanceOf(pc=337,UVar(defSites={102},value={_ <: java.util.regex.Pattern$Node, null}[↦334;refId=160]),java.util.regex.Pattern$Begin)),
	104: If(pc=340,UVar(defSites={103},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=108),
	105: Assignment(pc=344,DVar(useSites={106},value={_ <: java.util.regex.Pattern$Node, null}[↦344;refId=161],origin=105),GetField(pc=344,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	106: Assignment(pc=347,DVar(useSites={107},value=int ∈ [0,1],origin=106),InstanceOf(pc=347,UVar(defSites={105},value={_ <: java.util.regex.Pattern$Node, null}[↦344;refId=161]),java.util.regex.Pattern$First)),
	107: If(pc=350,UVar(defSites={106},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=111),
	108: Assignment(pc=355,DVar(useSites={109},value={_ <: java.util.regex.Pattern$Node, null}[↦355;refId=179],origin=108),GetField(pc=355,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	109: PutField(pc=358,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={108},value={_ <: java.util.regex.Pattern$Node, null}[↦355;refId=179])),
	110: Goto(pc=361,target=121),
	111: Assignment(pc=366,DVar(useSites={112},value=int ∈ [0,1],origin=111),GetField(pc=366,java.util.regex.Pattern,hasSupplementary,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	112: If(pc=369,UVar(defSites={111},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=117),
	113: Assignment(pc=372,DVar(useSites={120,115},value=java.util.regex.Pattern$StartS[↦372;refId=162],origin=113),New(pc=372,java.util.regex.Pattern$StartS)),
	114: Assignment(pc=377,DVar(useSites={115},value={_ <: java.util.regex.Pattern$Node, null}[↦377;refId=163],origin=114),GetField(pc=377,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	115: NonVirtualMethodCall(pc=380,java.util.regex.Pattern$StartS,isInterface=false,void <init>(java.util.regex.Pattern$Node),UVar(defSites={113},value=java.util.regex.Pattern$StartS[↦372;refId=162]),(UVar(defSites={114},value={_ <: java.util.regex.Pattern$Node, null}[↦377;refId=163]))),
	116: Goto(pc=383,target=120),
	117: Assignment(pc=386,DVar(useSites={120,119},value=java.util.regex.Pattern$Start[↦386;refId=165],origin=117),New(pc=386,java.util.regex.Pattern$Start)),
	118: Assignment(pc=391,DVar(useSites={119},value={_ <: java.util.regex.Pattern$Node, null}[↦391;refId=166],origin=118),GetField(pc=391,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	119: NonVirtualMethodCall(pc=394,java.util.regex.Pattern$Start,isInterface=false,void <init>(java.util.regex.Pattern$Node),UVar(defSites={117},value=java.util.regex.Pattern$Start[↦386;refId=165]),(UVar(defSites={118},value={_ <: java.util.regex.Pattern$Node, null}[↦391;refId=166]))),
	120: PutField(pc=397,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={113,117},value=_ <: java.util.regex.Pattern$Start[refId=168; values=«java.util.regex.Pattern$StartS[↦372;refId=162], java.util.regex.Pattern$Start[↦386;refId=165]»])),
	121: Assignment(pc=401,DVar(useSites={122},value=int ∈ [0,1],origin=121),GetField(pc=401,java.util.regex.Pattern,hasGroupRef,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	122: If(pc=404,UVar(defSites={121},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=139),
	123: Assignment(pc=408,DVar(useSites={124},value={_ <: java.util.List, null}[↦408;refId=175],origin=123),GetField(pc=408,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	124: Assignment(pc=411,DVar(useSites={128,126},value={_ <: java.util.Iterator, null}[↦411;refId=178],origin=124),VirtualFunctionCall(pc=411,java.util.List,isInterface=true,java.util.Iterator iterator(),UVar(defSites={123},value={_ <: java.util.List, null}[↦408;refId=175]),())),
	125: Nop(pc=416),
	126: Assignment(pc=418,DVar(useSites={127},value=int ∈ [0,1],origin=126),VirtualFunctionCall(pc=418,java.util.Iterator,isInterface=true,boolean hasNext(),UVar(defSites={124},value={_ <: java.util.Iterator, null}[↦411;refId=178]),())),
	127: If(pc=423,UVar(defSites={126},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=139),
	128: Assignment(pc=427,DVar(useSites={132,130,129,137},value={_ <: java.lang.Object, null}[↦427;refId=187],origin=128),VirtualFunctionCall(pc=427,java.util.Iterator,isInterface=true,java.lang.Object next(),UVar(defSites={124},value=_ <: java.util.Iterator[↦411;refId=178]),())),
	129: Checkcast(pc=432,UVar(defSites={128},value={_ <: java.lang.Object, null}[↦427;refId=187]),java.util.regex.Pattern$Node),
	130: Assignment(pc=439,DVar(useSites={131},value=int ∈ [0,1],origin=130),InstanceOf(pc=439,UVar(defSites={128},value={_ <: java.util.regex.Pattern$Node, null}[↦427;refId=188]),java.util.regex.Pattern$Loop)),
	131: If(pc=442,UVar(defSites={130},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=126),
	132: Checkcast(pc=447,UVar(defSites={128},value={_ <: java.util.regex.Pattern$Node, null}[↦427;refId=188]),java.util.regex.Pattern$Loop),
	133: Assignment(pc=452,DVar(useSites={137,135},value=an int,origin=133),GetField(pc=452,java.util.regex.Pattern,localTCNCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	134: Assignment(pc=456,DVar(useSites={135},value=int = 1,origin=134),IntConst(pc=456,1)),
	135: Assignment(pc=457,DVar(useSites={136},value=an int,origin=135),BinaryExpr(pc=457,ComputationalTypeInt,UVar(defSites={133},value=an int),+,UVar(defSites={134},value=int = 1))),
	136: PutField(pc=458,java.util.regex.Pattern,localTCNCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={135},value=an int)),
	137: PutField(pc=461,java.util.regex.Pattern$Loop,posIndex,int,UVar(defSites={128},value={_ <: java.util.regex.Pattern$Loop, null}[↦427;refId=190]),UVar(defSites={133},value=an int)),
	138: Goto(pc=464,target=126),
	139: Assignment(pc=468,DVar(useSites={140},value=null[↦468],origin=139),NullExpr(pc=468)),
	140: PutField(pc=469,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={139},value=null[↦468])),
	141: Assignment(pc=473,DVar(useSites={142},value=null[↦473],origin=141),NullExpr(pc=473)),
	142: PutField(pc=474,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={141},value=null[↦473])),
	143: Assignment(pc=478,DVar(useSites={144},value=null[↦478],origin=143),NullExpr(pc=478)),
	144: PutField(pc=479,java.util.regex.Pattern,groupNodes,java.util.regex.Pattern$GroupHead[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={143},value=null[↦478])),
	145: Assignment(pc=483,DVar(useSites={146},value=int = 0,origin=145),IntConst(pc=483,0)),
	146: PutField(pc=484,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={145},value=int = 0)),
	147: Assignment(pc=488,DVar(useSites={148},value=int = 1,origin=147),IntConst(pc=488,1)),
	148: PutField(pc=489,java.util.regex.Pattern,compiled,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={147},value=int = 1)),
	149: Assignment(pc=493,DVar(useSites={150},value=null[↦493],origin=149),NullExpr(pc=493)),
	150: PutField(pc=494,java.util.regex.Pattern,topClosureNodes,java.util.List,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={149},value=null[↦493])),
	151: Return(pc=497)
),cfg=CFG(
	BB_0: BasicBlock(start=10,end=11) -> {BB_27}
	BB_10: BasicBlock(start=24,end=25) -> {BB_20,BB_34}
	BB_11: BasicBlock(start=14,end=18) -> {BB_3e,BB_3b}
	BB_12: BasicBlock(start=125,end=125) -> {BB_3c}
	BB_13: BasicBlock(start=93,end=95) -> {BB_3e,BB_3}
	BB_14: BasicBlock(start=57,end=57) -> {BB_37,BB_32}
	BB_15: BasicBlock(start=78,end=78) -> {BB_3e}
	BB_16: BasicBlock(start=29,end=29) -> {BB_4,BB_3a}
	BB_17: BasicBlock(start=132,end=132) -> {BB_3e,BB_18}
	BB_18: BasicBlock(start=133,end=137) -> {BB_3e,BB_b}
	BB_19: BasicBlock(start=116,end=116) -> {BB_e}
	BB_1: BasicBlock(start=121,end=122) -> {BB_35,BB_5}
	BB_1a: BasicBlock(start=74,end=75) -> {BB_2b,BB_3d}
	BB_1b: BasicBlock(start=6,end=7) -> {BB_3e,BB_36}
	BB_1c: BasicBlock(start=117,end=119) -> {BB_3e,BB_e}
	BB_1d: BasicBlock(start=85,end=86) -> {BB_3e,BB_8}
	BB_1e: BasicBlock(start=102,end=104) -> {BB_2e,BB_25}
	BB_1f: BasicBlock(start=28,end=28) -> {BB_3e,BB_16}
	BB_20: BasicBlock(start=38,end=40) -> {BB_3e,BB_22}
	BB_21: BasicBlock(start=129,end=129) -> {BB_3e,BB_2f}
	BB_22: BasicBlock(start=41,end=41) -> {BB_f,BB_7}
	BB_23: BasicBlock(start=73,end=73) -> {BB_3e,BB_1a}
	BB_24: BasicBlock(start=128,end=128) -> {BB_3e,BB_21}
	BB_25: BasicBlock(start=105,end=107) -> {BB_3f,BB_2e}
	BB_26: BasicBlock(start=2,end=2) -> {BB_30,BB_0}
	BB_27: BasicBlock(start=12,end=13) -> {BB_3e,BB_11}
	BB_28: BasicBlock(start=54,end=56) -> {BB_3e,BB_14}
	BB_29: BasicBlock(start=113,end=115) -> {BB_3e,BB_19}
	BB_2: BasicBlock(start=97,end=99) -> {BB_3e,BB_40}
	BB_2a: BasicBlock(start=81,end=81) -> {BB_3e}
	BB_2b: BasicBlock(start=76,end=77) -> {BB_3e,BB_15}
	BB_2c: BasicBlock(start=91,end=92) -> {BB_2,BB_13}
	BB_2d: BasicBlock(start=66,end=66) -> {BB_38}
	BB_2e: BasicBlock(start=108,end=110) -> {BB_1}
	BB_2f: BasicBlock(start=130,end=131) -> {BB_3c,BB_17}
	BB_30: BasicBlock(start=3,end=4) -> {BB_3e,BB_d}
	BB_31: BasicBlock(start=35,end=35) -> {BB_3e,BB_39}
	BB_32: BasicBlock(start=67,end=68) -> {BB_3e,BB_a}
	BB_33: BasicBlock(start=127,end=127) -> {BB_24,BB_35}
	BB_34: BasicBlock(start=26,end=27) -> {BB_3e,BB_1f}
	BB_35: BasicBlock(start=139,end=151) -> {BB_6}
	BB_36: BasicBlock(start=8,end=9) -> {BB_27}
	BB_37: BasicBlock(start=58,end=61) -> {BB_3e,BB_9}
	BB_38: BasicBlock(start=82,end=84) -> {BB_1d,BB_1e}
	BB_39: BasicBlock(start=36,end=37) -> {BB_10}
	BB_3: BasicBlock(start=96,end=96) -> {BB_40}
	BB_3a: BasicBlock(start=30,end=31) -> {BB_4}
	BB_3b: BasicBlock(start=19,end=23) -> {BB_10}
	BB_3c: BasicBlock(start=126,end=126) -> {BB_3e,BB_33}
	BB_3d: BasicBlock(start=79,end=80) -> {BB_3e,BB_2a}
	BB_3e: ExitNode(normalReturn=false)
	BB_3f: BasicBlock(start=111,end=112) -> {BB_29,BB_1c}
	BB_40: BasicBlock(start=100,end=101) -> {BB_1}
	BB_4: BasicBlock(start=32,end=34) -> {BB_3e,BB_31}
	BB_5: BasicBlock(start=123,end=124) -> {BB_3e,BB_12}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=43,end=53) -> {BB_3e,BB_28}
	BB_8: BasicBlock(start=87,end=90) -> {BB_1,BB_2c}
	BB_9: BasicBlock(start=62,end=65) -> {BB_3e,BB_2d}
	BB_a: BasicBlock(start=69,end=72) -> {BB_38,BB_23}
	BB_b: BasicBlock(start=138,end=138) -> {BB_3c}
	BB_c: BasicBlock(start=0,end=1) -> {BB_3e,BB_26}
	BB_d: BasicBlock(start=5,end=5) -> {BB_0,BB_1b}
	BB_e: BasicBlock(start=120,end=120) -> {BB_1}
	BB_f: BasicBlock(start=42,end=42) -> {BB_3e,BB_7}
))

boolean lambda$VertWS$2(int)
AITACode(params=(Parameters(
	1: useSites={1,9,5,3,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 10,origin=0),IntConst(pc=1,10)),
	1: If(pc=3,UVar(defSites={-2},value=an int),<,UVar(defSites={0},value=int = 10),target=4),
	2: Assignment(pc=7,DVar(useSites={3},value=int = 13,origin=2),IntConst(pc=7,13)),
	3: If(pc=9,UVar(defSites={-2},value=int ∈ [10,2147483647]),<=,UVar(defSites={2},value=int = 13),target=10),
	4: Assignment(pc=13,DVar(useSites={5},value=int = 133,origin=4),IntConst(pc=13,133)),
	5: If(pc=16,UVar(defSites={-2},value=an int),==,UVar(defSites={4},value=int = 133),target=10),
	6: Assignment(pc=20,DVar(useSites={7},value=int = 8232,origin=6),IntConst(pc=20,8232)),
	7: If(pc=23,UVar(defSites={-2},value=an int),==,UVar(defSites={6},value=int = 8232),target=10),
	8: Assignment(pc=27,DVar(useSites={9},value=int = 8233,origin=8),IntConst(pc=27,8233)),
	9: If(pc=30,UVar(defSites={-2},value=an int),!=,UVar(defSites={8},value=int = 8233),target=12),
	10: Assignment(pc=33,DVar(useSites={13},value=int = 1,origin=10),IntConst(pc=33,1)),
	11: Goto(pc=34,target=13),
	12: Assignment(pc=37,DVar(useSites={13},value=int ∈ [0,1],origin=12),IntConst(pc=37,0)),
	13: ReturnValue(pc=38,UVar(defSites={12,10},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_8,BB_4}
	BB_1: BasicBlock(start=10,end=11) -> {BB_3}
	BB_2: BasicBlock(start=6,end=7) -> {BB_7,BB_1}
	BB_3: BasicBlock(start=13,end=13) -> {BB_6}
	BB_4: BasicBlock(start=2,end=3) -> {BB_8,BB_1}
	BB_5: BasicBlock(start=12,end=12) -> {BB_3}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=8,end=9) -> {BB_1,BB_5}
	BB_8: BasicBlock(start=4,end=5) -> {BB_1,BB_2}
	BB_9: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$BmpCharPredicate SingleI(int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value={_ <: java.util.regex.Pattern$SingleI(II)Ljava$util$regex$Pattern$BmpCharPredicate::2$Lambda, null}[↦2;refId=103],origin=0),StaticFunctionCall(pc=2,java.util.regex.Pattern$SingleI(II)Ljava$util$regex$Pattern$BmpCharPredicate::2$Lambda,isInterface=false,java.util.regex.Pattern$SingleI(II)Ljava$util$regex$Pattern$BmpCharPredicate::2$Lambda $newInstance(int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value=an int)))),
	1: ReturnValue(pc=7,UVar(defSites={0},value={_ <: java.util.regex.Pattern$SingleI(II)Ljava$util$regex$Pattern$BmpCharPredicate::2$Lambda, null}[↦2;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean lambda$Range$11(int,int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={1},value=int ∈ [0,1],origin=0),StaticFunctionCall(pc=3,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-4},value=an int),UVar(defSites={-3},value=an int)))),
	1: ReturnValue(pc=6,UVar(defSites={0},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.lang.String normalize(java.lang.String)
AITACode(params=(Parameters(
	1: useSites={0,8,17,57,45,29} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={56,2,14,57,7},value=an int,origin=0),VirtualFunctionCall(pc=1,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),())),
	1: Assignment(pc=5,DVar(useSites={2,58,57,45,29},value=java.lang.StringBuilder[↦5;refId=105],origin=1),New(pc=5,java.lang.StringBuilder)),
	2: NonVirtualMethodCall(pc=10,java.lang.StringBuilder,isInterface=false,void <init>(int),UVar(defSites={1},value=java.lang.StringBuilder[↦5;refId=105]),(UVar(defSites={0},value=an int))),
	3: Assignment(pc=14,DVar(useSites={26,38},value=int = 0,origin=3),IntConst(pc=14,0)),
	4: Assignment(pc=16,DVar(useSites={56,28,57,45,29},value=int = 0,origin=4),IntConst(pc=16,0)),
	5: Assignment(pc=19,DVar(useSites={32,40,52,9,27},value=int = 0,origin=5),IntConst(pc=19,0)),
	6: Assignment(pc=22,DVar(useSites={16,48,8,56,20,44,28,57,13,45,29,7,47},value=int = 0,origin=6),IntConst(pc=22,0)),
	7: If(pc=28,UVar(defSites={48,20,6},value=an int),>=,UVar(defSites={0},value=an int),target=50),
	8: Assignment(pc=34,DVar(useSites={24,36,26,38,11},value=int ∈ [0,65535],origin=8),VirtualFunctionCall(pc=34,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={48,20,6},value=int ∈ [-2147483648,2147483646])))),
	9: If(pc=41,UVar(defSites={33,41,5},value=int ∈ [0,65535]),!=,IntConst(pc=-333,0),target=23),
	10: Assignment(pc=46,DVar(useSites={11},value=int = 92,origin=10),IntConst(pc=46,92)),
	11: If(pc=48,UVar(defSites={8},value=int ∈ [0,65535]),!=,UVar(defSites={10},value=int = 92),target=23),
	12: Assignment(pc=53,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=53,1)),
	13: Assignment(pc=54,DVar(useSites={14},value=int ∈ [-2147483647,2147483647],origin=13),BinaryExpr(pc=54,ComputationalTypeInt,UVar(defSites={48,20,6},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={12},value=int = 1))),
	14: If(pc=56,UVar(defSites={13},value=int ∈ [-2147483647,2147483647]),>=,UVar(defSites={0},value=int ∈ [-2147483647,2147483647]),target=23),
	15: Assignment(pc=62,DVar(useSites={16},value=int = 1,origin=15),IntConst(pc=62,1)),
	16: Assignment(pc=63,DVar(useSites={17},value=int ∈ [-2147483647,2147483647],origin=16),BinaryExpr(pc=63,ComputationalTypeInt,UVar(defSites={48,20,6},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={15},value=int = 1))),
	17: Assignment(pc=64,DVar(useSites={19},value=int ∈ [0,65535],origin=17),VirtualFunctionCall(pc=64,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={16},value=int ∈ [-2147483647,2147483647])))),
	18: Assignment(pc=67,DVar(useSites={19},value=int = 92,origin=18),IntConst(pc=67,92)),
	19: If(pc=69,UVar(defSites={17},value=int ∈ [0,65535]),!=,UVar(defSites={18},value=int = 92),target=23),
	20: Assignment(pc=72,DVar(useSites={16,48,8,56,44,28,57,21,13,45,29,7,47},value=an int,origin=20),BinaryExpr(pc=72,ComputationalTypeInt,UVar(defSites={48,20,6},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=72,2))),
	21: Assignment(pc=75,DVar(useSites={26,38},value=int = 0,origin=21),IntConst(pc=75,0)),
	22: Goto(pc=77,target=7),
	23: Assignment(pc=82,DVar(useSites={24},value=int = 91,origin=23),IntConst(pc=82,91)),
	24: If(pc=84,UVar(defSites={8},value=int ∈ [0,65535]),!=,UVar(defSites={23},value=int = 91),target=35),
	25: Assignment(pc=88,DVar(useSites={26},value=int = 92,origin=25),IntConst(pc=88,92)),
	26: If(pc=90,UVar(defSites={8,21,3},value=int ∈ [0,65535]),==,UVar(defSites={25},value=int = 92),target=35),
	27: If(pc=95,UVar(defSites={33,41,5},value=int ∈ [0,65535]),!=,IntConst(pc=-333,0),target=31),
	28: If(pc=102,UVar(defSites={48,4,20,6,47},value=an int),>=,UVar(defSites={48,20,6},value=an int),target=30),
	29: StaticMethodCall(pc=111,java.util.regex.Pattern,isInterface=false,void normalizeSlice(java.lang.String,int,int,java.lang.StringBuilder),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={48,4,20,6,47},value=int ∈ [-2147483648,2147483646]),UVar(defSites={48,20,6},value=int ∈ [-2147483647,2147483647]),UVar(defSites={1},value=java.lang.StringBuilder[↦5;refId=105]))),
	30: Nop(pc=114),
	31: Assignment(pc=120,DVar(useSites={32},value=int = 1,origin=31),IntConst(pc=120,1)),
	32: Assignment(pc=121,DVar(useSites={33},value=int ∈ [1,65536],origin=32),BinaryExpr(pc=121,ComputationalTypeInt,UVar(defSites={33,41,5},value=int ∈ [0,65535]),+,UVar(defSites={31},value=int = 1))),
	33: Assignment(pc=122,DVar(useSites={32,40,52,9,27},value=int ∈ [0,65535],origin=33),PrimitiveTypecastExpr(pc=122,CharType,UVar(defSites={32},value=int ∈ [1,65536]))),
	34: Goto(pc=125,target=48),
	35: Assignment(pc=130,DVar(useSites={36},value=int = 93,origin=35),IntConst(pc=130,93)),
	36: If(pc=132,UVar(defSites={8},value=int ∈ [0,65535]),!=,UVar(defSites={35},value=int = 93),target=48),
	37: Assignment(pc=136,DVar(useSites={38},value=int = 92,origin=37),IntConst(pc=136,92)),
	38: If(pc=138,UVar(defSites={8,21,3},value=int ∈ [0,65535]),==,UVar(defSites={37},value=int = 92),target=48),
	39: Assignment(pc=143,DVar(useSites={40},value=int = 1,origin=39),IntConst(pc=143,1)),
	40: Assignment(pc=144,DVar(useSites={41},value=int ∈ [-1,65534],origin=40),BinaryExpr(pc=144,ComputationalTypeInt,UVar(defSites={33,41,5},value=int ∈ [0,65535]),-,UVar(defSites={39},value=int = 1))),
	41: Assignment(pc=145,DVar(useSites={32,40,52,42,9,27},value=int ∈ [0,65535],origin=41),PrimitiveTypecastExpr(pc=145,CharType,UVar(defSites={40},value=int ∈ [-1,65534]))),
	42: If(pc=150,UVar(defSites={41},value=int ∈ [0,65535]),!=,IntConst(pc=-333,0),target=48),
	43: Assignment(pc=158,DVar(useSites={44},value=int = 1,origin=43),IntConst(pc=158,1)),
	44: Assignment(pc=159,DVar(useSites={45},value=an int,origin=44),BinaryExpr(pc=159,ComputationalTypeInt,UVar(defSites={48,20,6},value=an int),+,UVar(defSites={43},value=int = 1))),
	45: StaticMethodCall(pc=161,java.util.regex.Pattern,isInterface=false,void normalizeClazz(java.lang.String,int,int,java.lang.StringBuilder),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={48,4,20,6,47},value=an int),UVar(defSites={44},value=an int),UVar(defSites={1},value=java.lang.StringBuilder[↦5;refId=105]))),
	46: Assignment(pc=166,DVar(useSites={47},value=int = 1,origin=46),IntConst(pc=166,1)),
	47: Assignment(pc=167,DVar(useSites={56,28,57,45,29},value=an int,origin=47),BinaryExpr(pc=167,ComputationalTypeInt,UVar(defSites={48,20,6},value=an int),+,UVar(defSites={46},value=int = 1))),
	48: Assignment(pc=173,DVar(useSites={16,8,56,20,44,28,49,57,13,45,29,7,47},value=an int,origin=48),BinaryExpr(pc=173,ComputationalTypeInt,UVar(defSites={48,20,6},value=an int),+,IntConst(pc=173,1))),
	49: Goto(pc=176,target=7),
	50: Assignment(pc=179,DVar(useSites={51},value=int ∈ [0,1],origin=50),GetStatic(pc=179,java.util.regex.Pattern,$assertionsDisabled,boolean)),
	51: If(pc=182,UVar(defSites={50},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=56),
	52: If(pc=187,UVar(defSites={33,41,5},value=int ∈ [0,65535]),==,IntConst(pc=-333,0),target=56),
	53: Assignment(pc=190,DVar(useSites={54,55},value=java.lang.AssertionError[↦190;refId=204],origin=53),New(pc=190,java.lang.AssertionError)),
	54: NonVirtualMethodCall(pc=194,java.lang.AssertionError,isInterface=false,void <init>(),UVar(defSites={53},value=java.lang.AssertionError[↦190;refId=204]),()),
	55: Throw(pc=197,UVar(defSites={53},value=java.lang.AssertionError[↦190;refId=204])),
	56: If(pc=201,UVar(defSites={48,4,20,6,47},value=an int),>=,UVar(defSites={0},value=an int),target=58),
	57: StaticMethodCall(pc=209,java.util.regex.Pattern,isInterface=false,void normalizeSlice(java.lang.String,int,int,java.lang.StringBuilder),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={48,4,20,6,47},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=int ∈ [-2147483647,2147483647]),UVar(defSites={1},value=java.lang.StringBuilder[↦5;refId=105]))),
	58: Assignment(pc=213,DVar(useSites={59},value={java.lang.String, null}[↦213;refId=112],origin=58),VirtualFunctionCall(pc=213,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={1},value=java.lang.StringBuilder[↦5;refId=105]),())),
	59: ReturnValue(pc=216,UVar(defSites={58},value={java.lang.String, null}[↦213;refId=112]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_7,BB_2}
	BB_10: BasicBlock(start=29,end=29) -> {BB_7,BB_6}
	BB_11: BasicBlock(start=9,end=9) -> {BB_1f,BB_9}
	BB_12: BasicBlock(start=53,end=54) -> {BB_7,BB_1e}
	BB_13: BasicBlock(start=59,end=59) -> {BB_1b}
	BB_14: BasicBlock(start=27,end=27) -> {BB_3,BB_1d}
	BB_15: BasicBlock(start=7,end=7) -> {BB_1c,BB_20}
	BB_16: BasicBlock(start=39,end=42) -> {BB_19,BB_5}
	BB_17: BasicBlock(start=3,end=6) -> {BB_15}
	BB_18: BasicBlock(start=35,end=36) -> {BB_19,BB_b}
	BB_19: BasicBlock(start=48,end=49) -> {BB_15}
	BB_1: BasicBlock(start=52,end=52) -> {BB_a,BB_12}
	BB_1a: BasicBlock(start=18,end=19) -> {BB_1f,BB_d}
	BB_1b: ExitNode(normalReturn=true)
	BB_1c: BasicBlock(start=50,end=51) -> {BB_a,BB_1}
	BB_1d: BasicBlock(start=31,end=34) -> {BB_19}
	BB_1e: BasicBlock(start=55,end=55) -> {BB_7}
	BB_1f: BasicBlock(start=23,end=24) -> {BB_18,BB_c}
	BB_20: BasicBlock(start=8,end=8) -> {BB_7,BB_11}
	BB_21: BasicBlock(start=58,end=58) -> {BB_7,BB_13}
	BB_2: BasicBlock(start=1,end=2) -> {BB_7,BB_17}
	BB_3: BasicBlock(start=28,end=28) -> {BB_6,BB_10}
	BB_4: BasicBlock(start=12,end=14) -> {BB_1f,BB_8}
	BB_5: BasicBlock(start=43,end=45) -> {BB_7,BB_e}
	BB_6: BasicBlock(start=30,end=30) -> {BB_1d}
	BB_7: ExitNode(normalReturn=false)
	BB_8: BasicBlock(start=15,end=17) -> {BB_7,BB_1a}
	BB_9: BasicBlock(start=10,end=11) -> {BB_1f,BB_4}
	BB_a: BasicBlock(start=56,end=56) -> {BB_21,BB_f}
	BB_b: BasicBlock(start=37,end=38) -> {BB_19,BB_16}
	BB_c: BasicBlock(start=25,end=26) -> {BB_18,BB_14}
	BB_d: BasicBlock(start=20,end=22) -> {BB_15}
	BB_e: BasicBlock(start=46,end=47) -> {BB_19}
	BB_f: BasicBlock(start=57,end=57) -> {BB_7,BB_21}
))

java.util.regex.Pattern$CharPredicate clazz(boolean)
AITACode(params=(Parameters(
	0: useSites={64,80,72,100,44,28,10,26,17,49,41,69,21,51,11,75,91,7,71,47,31} (origin=-1),
	1: useSites={79} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={24,88,56,98,82,90,22,54,97,85,77,61,67,95},value=null[↦0],origin=0),NullExpr(pc=0)),
	1: Assignment(pc=2,DVar(useSites={67},value=null[↦2],origin=1),NullExpr(pc=2)),
	2: Assignment(pc=4,DVar(useSites={4,3,91},value=java.util.regex.Pattern$BitClass[↦4;refId=103],origin=2),New(pc=4,java.util.regex.Pattern$BitClass)),
	3: NonVirtualMethodCall(pc=8,java.util.regex.Pattern$BitClass,isInterface=false,void <init>(),UVar(defSites={2},value=java.util.regex.Pattern$BitClass[↦4;refId=103]),()),
	4: Assignment(pc=15,DVar(useSites={88,56,90,85,61,67},value={_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106],origin=4),StaticFunctionCall(pc=15,java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda,isInterface=false,java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda $newInstance(java.util.regex.Pattern$BitClass),(UVar(defSites={2},value=java.util.regex.Pattern$BitClass[↦4;refId=103])))),
	5: Assignment(pc=22,DVar(useSites={87},value=int = 0,origin=5),IntConst(pc=22,0)),
	6: Assignment(pc=25,DVar(useSites={84,78,53},value=int = 0,origin=6),IntConst(pc=25,0)),
	7: Assignment(pc=29,DVar(useSites={9,19},value=an int,origin=7),VirtualFunctionCall(pc=29,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	8: Assignment(pc=36,DVar(useSites={9},value=int = 94,origin=8),IntConst(pc=36,94)),
	9: If(pc=38,UVar(defSites={7},value=an int),!=,UVar(defSites={8},value=int = 94),target=19),
	10: Assignment(pc=42,DVar(useSites={14},value={int[], null}[↦42;refId=108],origin=10),GetField(pc=42,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	11: Assignment(pc=46,DVar(useSites={13},value=an int,origin=11),GetField(pc=46,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	12: Assignment(pc=49,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=49,1)),
	13: Assignment(pc=50,DVar(useSites={14},value=an int,origin=13),BinaryExpr(pc=50,ComputationalTypeInt,UVar(defSites={11},value=an int),-,UVar(defSites={12},value=int = 1))),
	14: Assignment(pc=51,DVar(useSites={16},value=an int,origin=14),ArrayLoad(pc=51,UVar(defSites={13},value=an int),UVar(defSites={10},value={int[], null}[↦42;refId=108]))),
	15: Assignment(pc=52,DVar(useSites={16},value=int = 91,origin=15),IntConst(pc=52,91)),
	16: If(pc=54,UVar(defSites={14},value=an int),!=,UVar(defSites={15},value=int = 91),target=19),
	17: Assignment(pc=58,DVar(useSites={19},value=an int,origin=17),VirtualFunctionCall(pc=58,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	18: Assignment(pc=63,DVar(useSites={87},value=int = 1,origin=18),IntConst(pc=63,1)),
	19: Switch(pc=68,defaultTarget=91,index=UVar(defSites={100,26,17,51,7,31},value=an int),npairs=(IntIntPair(0,71),IntIntPair(38,28),IntIntPair(91,20),IntIntPair(93,77)),
	20: Assignment(pc=113,DVar(useSites={21},value=int = 1,origin=20),IntConst(pc=113,1)),
	21: Assignment(pc=114,DVar(useSites={24,88,56,98,82,90,22,54,97,85,77,61,67,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=410],origin=21),VirtualFunctionCall(pc=114,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate clazz(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={20},value=int = 1)))),
	22: If(pc=119,UVar(defSites={0,32,24,98,49,41,21,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=363; values=«null[↦0], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),!=,NullExpr(pc=-333),target=24),
	23: Goto(pc=124,target=26),
	24: Assignment(pc=129,DVar(useSites={88,56,98,82,90,22,54,97,25,85,77,61,67,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=415],origin=24),VirtualFunctionCall(pc=129,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate union(java.util.regex.Pattern$CharPredicate),UVar(defSites={0,32,24,98,49,41,21,45,67,91},value=_ <: java.util.regex.Pattern$CharPredicate[refId=411; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),(UVar(defSites={21},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=410])))),
	25: Nop(pc=134),
	26: Assignment(pc=136,DVar(useSites={19},value=an int,origin=26),VirtualFunctionCall(pc=136,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	27: Goto(pc=141,target=19),
	28: Assignment(pc=145,DVar(useSites={30},value=an int,origin=28),VirtualFunctionCall(pc=145,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	29: Assignment(pc=152,DVar(useSites={30},value=int = 38,origin=29),IntConst(pc=152,38)),
	30: If(pc=154,UVar(defSites={28},value=an int),!=,UVar(defSites={29},value=int = 38),target=69),
	31: Assignment(pc=158,DVar(useSites={36,34,38,19},value=an int,origin=31),VirtualFunctionCall(pc=158,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	32: Assignment(pc=163,DVar(useSites={24,88,56,98,82,90,22,54,62,97,85,77,45,61,67,59,39,95},value=null[↦163],origin=32),NullExpr(pc=163)),
	33: Assignment(pc=168,DVar(useSites={34},value=int = 93,origin=33),IntConst(pc=168,93)),
	34: If(pc=170,UVar(defSites={51,31},value=an int),==,UVar(defSites={33},value=int = 93),target=53),
	35: Assignment(pc=175,DVar(useSites={36},value=int = 38,origin=35),IntConst(pc=175,38)),
	36: If(pc=177,UVar(defSites={51,31},value=an int),==,UVar(defSites={35},value=int = 38),target=53),
	37: Assignment(pc=182,DVar(useSites={38},value=int = 91,origin=37),IntConst(pc=182,91)),
	38: If(pc=184,UVar(defSites={51,31},value=an int),!=,UVar(defSites={37},value=int = 91),target=47),
	39: If(pc=189,UVar(defSites={32,49,41,45},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=451; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=386], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=392], null[↦163], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=399]»]),!=,NullExpr(pc=-333),target=43),
	40: Assignment(pc=193,DVar(useSites={41},value=int = 1,origin=40),IntConst(pc=193,1)),
	41: Assignment(pc=194,DVar(useSites={24,88,56,98,82,90,22,54,62,97,85,77,45,61,67,59,39,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=479],origin=41),VirtualFunctionCall(pc=194,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate clazz(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={40},value=int = 1)))),
	42: Goto(pc=199,target=51),
	43: Assignment(pc=205,DVar(useSites={44},value=int = 1,origin=43),IntConst(pc=205,1)),
	44: Assignment(pc=206,DVar(useSites={45},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦206;refId=484],origin=44),VirtualFunctionCall(pc=206,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate clazz(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={43},value=int = 1)))),
	45: Assignment(pc=209,DVar(useSites={24,88,56,98,82,90,22,54,46,62,97,85,77,61,67,59,39,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=486],origin=45),VirtualFunctionCall(pc=209,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate union(java.util.regex.Pattern$CharPredicate),UVar(defSites={32,49,41,45},value=_ <: java.util.regex.Pattern$CharPredicate[refId=477; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=386], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=392], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=399]»]),(UVar(defSites={44},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦206;refId=484])))),
	46: Goto(pc=216,target=51),
	47: VirtualMethodCall(pc=220,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	48: Assignment(pc=224,DVar(useSites={49},value=int = 0,origin=48),IntConst(pc=224,0)),
	49: Assignment(pc=225,DVar(useSites={24,88,56,98,82,90,22,54,62,97,85,77,45,61,67,59,39,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=473],origin=49),VirtualFunctionCall(pc=225,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate clazz(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={48},value=int = 0)))),
	50: Nop(pc=228),
	51: Assignment(pc=231,DVar(useSites={36,34,38,19},value=an int,origin=51),VirtualFunctionCall(pc=231,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	52: Goto(pc=236,target=33),
	53: If(pc=241,UVar(defSites={58,6,93},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=59),
	54: If(pc=245,UVar(defSites={0,32,24,98,49,41,21,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=465; values=«null[↦0], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=311], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=131], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=129], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),!=,NullExpr(pc=-333),target=56),
	55: Goto(pc=253,target=58),
	56: Assignment(pc=259,DVar(useSites={61,67},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦259;refId=519],origin=56),VirtualFunctionCall(pc=259,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate union(java.util.regex.Pattern$CharPredicate),UVar(defSites={0,32,24,98,49,41,21,45,67,91},value=_ <: java.util.regex.Pattern$CharPredicate[refId=515; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=311], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=131], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=129], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),(UVar(defSites={4},value={_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106])))),
	57: Nop(pc=264),
	58: Assignment(pc=265,DVar(useSites={84,78,53},value=int = 0,origin=58),IntConst(pc=265,0)),
	59: If(pc=270,UVar(defSites={32,49,41,45},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=514; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=386], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=392], null[↦163], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=399]»]),==,NullExpr(pc=-333),target=61),
	60: Nop(pc=273),
	61: If(pc=277,UVar(defSites={0,32,24,56,4,98,49,41,21,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=544; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], null[↦0], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=311], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=131], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=129], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦259;refId=444], {_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106]»]),!=,NullExpr(pc=-333),target=67),
	62: If(pc=282,UVar(defSites={32,49,41,45},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=546; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=386], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=392], null[↦163], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=399]»]),!=,NullExpr(pc=-333),target=66),
	63: Assignment(pc=286,DVar(useSites={64},value=String("Bad class syntax")[@286;refId=556],origin=63),StringConst(pc=286,Bad class syntax)),
	64: Assignment(pc=288,DVar(useSites={65},value={_ <: java.util.regex.PatternSyntaxException, null}[↦288;refId=558],origin=64),VirtualFunctionCall(pc=288,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={63},value=String("Bad class syntax")[@286;refId=556])))),
	65: Throw(pc=291,UVar(defSites={64},value={_ <: java.util.regex.PatternSyntaxException, null}[↦288;refId=558])),
	66: Goto(pc=295,target=19),
	67: Assignment(pc=300,DVar(useSites={24,88,56,68,98,82,90,22,54,97,85,77,61,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=563],origin=67),VirtualFunctionCall(pc=300,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate and(java.util.regex.Pattern$CharPredicate),UVar(defSites={0,32,24,56,4,98,49,41,21,45,67,91},value=_ <: java.util.regex.Pattern$CharPredicate[refId=553; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=311], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=131], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=129], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦259;refId=444], {_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106]»]),(UVar(defSites={32,4,1,49,41,21,45,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=548; values=«null[↦2], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=392], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=386], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=399], {_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106]»])))),
	68: Goto(pc=306,target=19),
	69: VirtualMethodCall(pc=310,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	70: Goto(pc=313,target=91),
	71: Assignment(pc=317,DVar(useSites={73},value=an int,origin=71),GetField(pc=317,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	72: Assignment(pc=321,DVar(useSites={73},value=an int,origin=72),GetField(pc=321,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	73: If(pc=324,UVar(defSites={71},value=an int),<,UVar(defSites={72},value=an int),target=91),
	74: Assignment(pc=328,DVar(useSites={75},value=String("Unclosed character class")[@328;refId=424],origin=74),StringConst(pc=328,Unclosed character class)),
	75: Assignment(pc=330,DVar(useSites={76},value={_ <: java.util.regex.PatternSyntaxException, null}[↦330;refId=426],origin=75),VirtualFunctionCall(pc=330,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={74},value=String("Unclosed character class")[@328;refId=424])))),
	76: Throw(pc=333,UVar(defSites={75},value={_ <: java.util.regex.PatternSyntaxException, null}[↦330;refId=426])),
	77: If(pc=335,UVar(defSites={0,32,24,98,49,41,21,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=363; values=«null[↦0], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),!=,NullExpr(pc=-333),target=79),
	78: If(pc=340,UVar(defSites={58,6,93},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=91),
	79: If(pc=344,UVar(defSites={-2},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=82),
	80: ExprStmt(pc=348,VirtualFunctionCall(pc=348,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	81: Nop(pc=351),
	82: If(pc=353,UVar(defSites={0,32,24,98,49,41,21,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=462; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], null[↦0], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),!=,NullExpr(pc=-333),target=84),
	83: Goto(pc=359,target=87),
	84: If(pc=364,UVar(defSites={58,6,93},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=87),
	85: Assignment(pc=370,DVar(useSites={88,90},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦370;refId=510],origin=85),VirtualFunctionCall(pc=370,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate union(java.util.regex.Pattern$CharPredicate),UVar(defSites={0,32,24,98,49,41,21,45,67,91},value=_ <: java.util.regex.Pattern$CharPredicate[refId=506; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),(UVar(defSites={4},value={_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106])))),
	86: Nop(pc=375),
	87: If(pc=378,UVar(defSites={18,5},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=90),
	88: Assignment(pc=382,DVar(useSites={89},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦382;refId=542],origin=88),VirtualFunctionCall(pc=382,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate negate(),UVar(defSites={0,32,24,4,98,49,41,21,85,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=511; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦370;refId=510], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),())),
	89: ReturnValue(pc=387,UVar(defSites={88},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦382;refId=542])),
	90: ReturnValue(pc=389,UVar(defSites={0,32,24,4,98,49,41,21,85,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=511; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦370;refId=510], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$clazz(Z)Ljava$util$regex$Pattern$CharPredicate::15$Lambda, null}[↦15;refId=106], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»])),
	91: Assignment(pc=393,DVar(useSites={24,88,56,92,98,82,90,22,54,97,85,77,61,67,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦393;refId=453],origin=91),VirtualFunctionCall(pc=393,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate range(java.util.regex.Pattern$BitClass),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={2},value=java.util.regex.Pattern$BitClass[↦4;refId=103])))),
	92: If(pc=398,UVar(defSites={91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦393;refId=453]),!=,NullExpr(pc=-333),target=95),
	93: Assignment(pc=401,DVar(useSites={84,78,53},value=int = 1,origin=93),IntConst(pc=401,1)),
	94: Goto(pc=404,target=100),
	95: If(pc=408,UVar(defSites={0,32,24,98,49,41,21,45,67,91},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=403; values=«null[↦0], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),!=,NullExpr(pc=-333),target=97),
	96: Goto(pc=413,target=100),
	97: If(pc=418,UVar(defSites={0,32,24,98,49,41,21,45,67,91},value=_ <: java.util.regex.Pattern$CharPredicate[refId=455; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),==,UVar(defSites={91},value=_ <: java.util.regex.Pattern$CharPredicate[↦393;refId=453]),target=100),
	98: Assignment(pc=423,DVar(useSites={24,88,56,82,90,22,54,97,85,77,61,67,99,95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=460],origin=98),VirtualFunctionCall(pc=423,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate union(java.util.regex.Pattern$CharPredicate),UVar(defSites={0,32,24,98,49,41,21,45,67,91},value=_ <: java.util.regex.Pattern$CharPredicate[refId=455; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦114;refId=113], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦300;refId=362], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦194;refId=176], _ <: java.util.regex.Pattern$CharPredicate[↦393;refId=122], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦129;refId=145], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦225;refId=172], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦209;refId=181], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦423;refId=242]»]),(UVar(defSites={91},value=_ <: java.util.regex.Pattern$CharPredicate[↦393;refId=453])))),
	99: Nop(pc=428),
	100: Assignment(pc=430,DVar(useSites={19},value=an int,origin=100),VirtualFunctionCall(pc=430,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	101: Goto(pc=435,target=19)
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=7) -> {BB_48,BB_41}
	BB_10: BasicBlock(start=46,end=46) -> {BB_44}
	BB_11: BasicBlock(start=93,end=94) -> {BB_4f}
	BB_12: BasicBlock(start=57,end=57) -> {BB_42}
	BB_13: BasicBlock(start=78,end=78) -> {BB_2f,BB_47}
	BB_14: BasicBlock(start=29,end=30) -> {BB_5,BB_3a}
	BB_15: BasicBlock(start=61,end=61) -> {BB_4c,BB_39}
	BB_16: BasicBlock(start=89,end=89) -> {BB_36}
	BB_17: BasicBlock(start=74,end=75) -> {BB_48,BB_2c}
	BB_18: BasicBlock(start=60,end=60) -> {BB_15}
	BB_19: BasicBlock(start=85,end=85) -> {BB_48,BB_2a}
	BB_1: BasicBlock(start=52,end=52) -> {BB_1c}
	BB_1a: BasicBlock(start=28,end=28) -> {BB_48,BB_14}
	BB_1b: BasicBlock(start=70,end=70) -> {BB_2f}
	BB_1c: BasicBlock(start=33,end=34) -> {BB_32,BB_3}
	BB_1d: BasicBlock(start=92,end=92) -> {BB_11,BB_37}
	BB_1e: BasicBlock(start=65,end=65) -> {BB_48}
	BB_1f: BasicBlock(start=97,end=97) -> {BB_2e,BB_4f}
	BB_20: BasicBlock(start=77,end=77) -> {BB_13,BB_47}
	BB_21: BasicBlock(start=96,end=96) -> {BB_4f}
	BB_22: BasicBlock(start=32,end=32) -> {BB_1c}
	BB_23: BasicBlock(start=45,end=45) -> {BB_48,BB_10}
	BB_24: BasicBlock(start=17,end=17) -> {BB_48,BB_35}
	BB_25: BasicBlock(start=22,end=22) -> {BB_40,BB_c}
	BB_26: BasicBlock(start=59,end=59) -> {BB_15,BB_18}
	BB_27: BasicBlock(start=27,end=27) -> {BB_45}
	BB_28: BasicBlock(start=71,end=73) -> {BB_2f,BB_17}
	BB_29: BasicBlock(start=54,end=54) -> {BB_a,BB_3f}
	BB_2: BasicBlock(start=84,end=84) -> {BB_3c,BB_19}
	BB_2a: BasicBlock(start=86,end=86) -> {BB_3c}
	BB_2b: BasicBlock(start=81,end=81) -> {BB_43}
	BB_2c: BasicBlock(start=76,end=76) -> {BB_48}
	BB_2d: BasicBlock(start=39,end=39) -> {BB_3d,BB_4}
	BB_2e: BasicBlock(start=98,end=98) -> {BB_48,BB_3b}
	BB_2f: BasicBlock(start=91,end=91) -> {BB_48,BB_1d}
	BB_30: BasicBlock(start=66,end=66) -> {BB_45}
	BB_31: BasicBlock(start=80,end=80) -> {BB_48,BB_2b}
	BB_32: BasicBlock(start=35,end=36) -> {BB_d,BB_3}
	BB_33: BasicBlock(start=48,end=49) -> {BB_48,BB_38}
	BB_34: BasicBlock(start=63,end=64) -> {BB_48,BB_1e}
	BB_35: BasicBlock(start=18,end=18) -> {BB_45}
	BB_36: ExitNode(normalReturn=true)
	BB_37: BasicBlock(start=95,end=95) -> {BB_1f,BB_21}
	BB_38: BasicBlock(start=50,end=50) -> {BB_44}
	BB_39: BasicBlock(start=67,end=67) -> {BB_48,BB_4b}
	BB_3: BasicBlock(start=53,end=53) -> {BB_29,BB_26}
	BB_3a: BasicBlock(start=31,end=31) -> {BB_48,BB_22}
	BB_3b: BasicBlock(start=99,end=99) -> {BB_4f}
	BB_3c: BasicBlock(start=87,end=87) -> {BB_4d,BB_8}
	BB_3d: BasicBlock(start=40,end=41) -> {BB_48,BB_b}
	BB_3e: BasicBlock(start=26,end=26) -> {BB_48,BB_27}
	BB_3f: BasicBlock(start=55,end=55) -> {BB_42}
	BB_40: BasicBlock(start=23,end=23) -> {BB_3e}
	BB_41: BasicBlock(start=8,end=9) -> {BB_45,BB_9}
	BB_42: BasicBlock(start=58,end=58) -> {BB_26}
	BB_43: BasicBlock(start=82,end=82) -> {BB_4e,BB_2}
	BB_44: BasicBlock(start=51,end=51) -> {BB_48,BB_1}
	BB_45: BasicBlock(start=19,end=19) -> {BB_20,BB_28,BB_f,BB_1a,BB_2f}
	BB_46: BasicBlock(start=4,end=4) -> {BB_48,BB_0}
	BB_47: BasicBlock(start=79,end=79) -> {BB_43,BB_31}
	BB_48: ExitNode(normalReturn=false)
	BB_49: BasicBlock(start=47,end=47) -> {BB_48,BB_33}
	BB_4: BasicBlock(start=43,end=44) -> {BB_48,BB_23}
	BB_4a: BasicBlock(start=15,end=16) -> {BB_45,BB_24}
	BB_4b: BasicBlock(start=68,end=68) -> {BB_45}
	BB_4c: BasicBlock(start=62,end=62) -> {BB_30,BB_34}
	BB_4d: BasicBlock(start=90,end=90) -> {BB_36}
	BB_4e: BasicBlock(start=83,end=83) -> {BB_3c}
	BB_4f: BasicBlock(start=100,end=100) -> {BB_48,BB_6}
	BB_5: BasicBlock(start=69,end=69) -> {BB_48,BB_1b}
	BB_6: BasicBlock(start=101,end=101) -> {BB_45}
	BB_7: BasicBlock(start=0,end=3) -> {BB_48,BB_46}
	BB_8: BasicBlock(start=88,end=88) -> {BB_48,BB_16}
	BB_9: BasicBlock(start=10,end=14) -> {BB_48,BB_4a}
	BB_a: BasicBlock(start=56,end=56) -> {BB_48,BB_12}
	BB_b: BasicBlock(start=42,end=42) -> {BB_44}
	BB_c: BasicBlock(start=24,end=24) -> {BB_48,BB_e}
	BB_d: BasicBlock(start=37,end=38) -> {BB_49,BB_2d}
	BB_e: BasicBlock(start=25,end=25) -> {BB_3e}
	BB_f: BasicBlock(start=20,end=21) -> {BB_48,BB_25}
))

boolean lambda$Single$8(int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: If(pc=2,UVar(defSites={-3},value=an int),!=,UVar(defSites={-2},value=an int),target=3),
	1: Assignment(pc=5,DVar(useSites={4},value=int = 1,origin=1),IntConst(pc=5,1)),
	2: Goto(pc=6,target=4),
	3: Assignment(pc=9,DVar(useSites={4},value=int ∈ [0,1],origin=3),IntConst(pc=9,0)),
	4: ReturnValue(pc=10,UVar(defSites={1,3},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_2,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_4}
	BB_2: BasicBlock(start=3,end=3) -> {BB_4}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_3}
	BB_5: ExitNode(normalReturn=false)
))

boolean hasBaseCharacter(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	1: useSites={0,2} (origin=-2),
	2: useSites={6,17,7} (origin=-3),
	3: useSites={7} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=8,DVar(useSites={6},value=an int,origin=2),GetField(pc=8,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-1;refId=102]))),
	3: Goto(pc=11,target=5),
	4: Assignment(pc=14,DVar(useSites={6},value=an int,origin=4),IntConst(pc=14,0)),
	5: Nop(pc=15),
	6: If(pc=22,UVar(defSites={17,-3},value=an int),<,UVar(defSites={4,2},value=an int),target=19),
	7: Assignment(pc=28,DVar(useSites={8,12},value=an int,origin=7),StaticFunctionCall(pc=28,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-3;refId=103]),UVar(defSites={17,-3},value=an int)))),
	8: Assignment(pc=35,DVar(useSites={9},value=int ∈ [0,1],origin=8),StaticFunctionCall(pc=35,java.lang.Character,isInterface=false,boolean isLetterOrDigit(int),(UVar(defSites={7},value=an int)))),
	9: If(pc=38,UVar(defSites={8},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	10: Assignment(pc=41,DVar(useSites={11},value=int = 1,origin=10),IntConst(pc=41,1)),
	11: ReturnValue(pc=42,UVar(defSites={10},value=int = 1)),
	12: Assignment(pc=45,DVar(useSites={14},value=an int,origin=12),StaticFunctionCall(pc=45,java.lang.Character,isInterface=false,int getType(int),(UVar(defSites={7},value=an int)))),
	13: Assignment(pc=48,DVar(useSites={14},value=int = 6,origin=13),IntConst(pc=48,6)),
	14: If(pc=50,UVar(defSites={12},value=an int),==,UVar(defSites={13},value=int = 6),target=17),
	15: Assignment(pc=56,DVar(useSites={16},value=int = 0,origin=15),IntConst(pc=56,0)),
	16: ReturnValue(pc=57,UVar(defSites={15},value=int = 0)),
	17: Assignment(pc=58,DVar(useSites={18,6,7},value=an int,origin=17),BinaryExpr(pc=58,ComputationalTypeInt,UVar(defSites={17,-3},value=an int),+,IntConst(pc=58,-1))),
	18: Goto(pc=61,target=6),
	19: Assignment(pc=64,DVar(useSites={20},value=int = 0,origin=19),IntConst(pc=64,0)),
	20: ReturnValue(pc=65,UVar(defSites={19},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_10,BB_3}
	BB_10: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_4}
	BB_2: BasicBlock(start=10,end=11) -> {BB_b}
	BB_3: BasicBlock(start=1,end=1) -> {BB_f,BB_7}
	BB_4: BasicBlock(start=6,end=6) -> {BB_d,BB_a}
	BB_5: BasicBlock(start=9,end=9) -> {BB_2,BB_9}
	BB_6: BasicBlock(start=13,end=14) -> {BB_8,BB_e}
	BB_7: BasicBlock(start=2,end=3) -> {BB_1}
	BB_8: BasicBlock(start=17,end=18) -> {BB_4}
	BB_9: BasicBlock(start=12,end=12) -> {BB_10,BB_6}
	BB_a: BasicBlock(start=7,end=7) -> {BB_10,BB_c}
	BB_b: ExitNode(normalReturn=true)
	BB_c: BasicBlock(start=8,end=8) -> {BB_10,BB_5}
	BB_d: BasicBlock(start=19,end=20) -> {BB_b}
	BB_e: BasicBlock(start=15,end=16) -> {BB_b}
	BB_f: BasicBlock(start=4,end=4) -> {BB_1}
))

java.lang.String[] producePermutations(java.lang.String)
AITACode(params=(Parameters(
	1: useSites={0,16,8,76,66,18,82,10,54,30,41,25,13,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={4},value=an int,origin=0),VirtualFunctionCall(pc=1,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),())),
	1: Assignment(pc=5,DVar(useSites={3},value=int = 0,origin=1),IntConst(pc=5,0)),
	2: Assignment(pc=6,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=6,1)),
	3: Assignment(pc=7,DVar(useSites={4},value=an int,origin=3),StaticFunctionCall(pc=7,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={1},value=int = 0),UVar(defSites={2},value=int = 1)))),
	4: If(pc=10,UVar(defSites={0},value=an int),!=,UVar(defSites={3},value=an int),target=10),
	5: Assignment(pc=13,DVar(useSites={6},value=int = 1,origin=5),IntConst(pc=13,1)),
	6: Assignment(pc=14,DVar(useSites={8,9},value=java.lang.String[][↦14;refId=124;length=1],origin=6),NewArray(pc=14,[UVar(defSites={5},value=int = 1)],java.lang.String[])),
	7: Assignment(pc=18,DVar(useSites={8},value=int = 0,origin=7),IntConst(pc=18,0)),
	8: ArrayStore(pc=20,UVar(defSites={6},value=java.lang.String[][↦14;refId=124;length=1]),UVar(defSites={7},value=int = 0),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102])),
	9: ReturnValue(pc=21,UVar(defSites={6},value=java.lang.String[][↦14;refId=124;length=1])),
	10: Assignment(pc=23,DVar(useSites={14},value=an int,origin=10),VirtualFunctionCall(pc=23,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),())),
	11: Assignment(pc=27,DVar(useSites={13},value=int = 0,origin=11),IntConst(pc=27,0)),
	12: Assignment(pc=28,DVar(useSites={13},value=int = 2,origin=12),IntConst(pc=28,2)),
	13: Assignment(pc=29,DVar(useSites={14},value=an int,origin=13),StaticFunctionCall(pc=29,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={11},value=int = 0),UVar(defSites={12},value=int = 2)))),
	14: If(pc=32,UVar(defSites={10},value=an int),!=,UVar(defSites={13},value=an int),target=40),
	15: Assignment(pc=36,DVar(useSites={16},value=int = 0,origin=15),IntConst(pc=36,0)),
	16: Assignment(pc=37,DVar(useSites={20,17,35},value=an int,origin=16),StaticFunctionCall(pc=37,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={15},value=int = 0)))),
	17: Assignment(pc=43,DVar(useSites={18},value=an int,origin=17),StaticFunctionCall(pc=43,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={16},value=an int)))),
	18: Assignment(pc=46,DVar(useSites={34,19},value=an int,origin=18),StaticFunctionCall(pc=46,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={17},value=an int)))),
	19: Assignment(pc=51,DVar(useSites={21},value=an int,origin=19),StaticFunctionCall(pc=51,java.util.regex.Pattern,isInterface=false,int getClass(int),(UVar(defSites={18},value=an int)))),
	20: Assignment(pc=55,DVar(useSites={21},value=an int,origin=20),StaticFunctionCall(pc=55,java.util.regex.Pattern,isInterface=false,int getClass(int),(UVar(defSites={16},value=an int)))),
	21: If(pc=58,UVar(defSites={19},value=an int),!=,UVar(defSites={20},value=an int),target=27),
	22: Assignment(pc=61,DVar(useSites={23},value=int = 1,origin=22),IntConst(pc=61,1)),
	23: Assignment(pc=62,DVar(useSites={26,25},value=java.lang.String[][↦62;refId=123;length=1],origin=23),NewArray(pc=62,[UVar(defSites={22},value=int = 1)],java.lang.String[])),
	24: Assignment(pc=66,DVar(useSites={25},value=int = 0,origin=24),IntConst(pc=66,0)),
	25: ArrayStore(pc=68,UVar(defSites={23},value=java.lang.String[][↦62;refId=123;length=1]),UVar(defSites={24},value=int = 0),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102])),
	26: ReturnValue(pc=69,UVar(defSites={23},value=java.lang.String[][↦62;refId=123;length=1])),
	27: Assignment(pc=70,DVar(useSites={28},value=int = 2,origin=27),IntConst(pc=70,2)),
	28: Assignment(pc=71,DVar(useSites={38,30,39},value=java.lang.String[][↦71;refId=114;length=2],origin=28),NewArray(pc=71,[UVar(defSites={27},value=int = 2)],java.lang.String[])),
	29: Assignment(pc=76,DVar(useSites={30},value=int = 0,origin=29),IntConst(pc=76,0)),
	30: ArrayStore(pc=78,UVar(defSites={28},value=java.lang.String[][↦71;refId=114;length=2]),UVar(defSites={29},value=int = 0),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102])),
	31: Assignment(pc=79,DVar(useSites={34,33,37,35},value=java.lang.StringBuilder[↦79;refId=115],origin=31),New(pc=79,java.lang.StringBuilder)),
	32: Assignment(pc=83,DVar(useSites={33},value=int = 2,origin=32),IntConst(pc=83,2)),
	33: NonVirtualMethodCall(pc=84,java.lang.StringBuilder,isInterface=false,void <init>(int),UVar(defSites={31},value=java.lang.StringBuilder[↦79;refId=115]),(UVar(defSites={32},value=int = 2))),
	34: ExprStmt(pc=92,VirtualFunctionCall(pc=92,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder appendCodePoint(int),UVar(defSites={31},value=java.lang.StringBuilder[↦79;refId=115]),(UVar(defSites={18},value=an int)))),
	35: ExprStmt(pc=99,VirtualFunctionCall(pc=99,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder appendCodePoint(int),UVar(defSites={31},value=java.lang.StringBuilder[↦79;refId=115]),(UVar(defSites={16},value=an int)))),
	36: Assignment(pc=104,DVar(useSites={38},value=int = 1,origin=36),IntConst(pc=104,1)),
	37: Assignment(pc=107,DVar(useSites={38},value={java.lang.String, null}[↦107;refId=122],origin=37),VirtualFunctionCall(pc=107,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={31},value=java.lang.StringBuilder[↦79;refId=115]),())),
	38: ArrayStore(pc=110,UVar(defSites={28},value=java.lang.String[][↦71;refId=114;length=2]),UVar(defSites={36},value=int = 1),UVar(defSites={37},value={java.lang.String, null}[↦107;refId=122])),
	39: ReturnValue(pc=112,UVar(defSites={28},value=java.lang.String[][↦71;refId=114;length=2])),
	40: Assignment(pc=113,DVar(useSites={46,49},value=int = 1,origin=40),IntConst(pc=113,1)),
	41: Assignment(pc=116,DVar(useSites={64,50,53,43},value=an int,origin=41),StaticFunctionCall(pc=116,java.util.regex.Pattern,isInterface=false,int countCodePoints(java.lang.CharSequence),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102])))),
	42: Assignment(pc=120,DVar(useSites={45,43,47},value=int = 1,origin=42),IntConst(pc=120,1)),
	43: If(pc=124,UVar(defSites={42,47},value=int ∈ [0,2147483647]),>=,UVar(defSites={41},value=an int),target=49),
	44: Assignment(pc=129,DVar(useSites={45},value=int = 1,origin=44),IntConst(pc=129,1)),
	45: Assignment(pc=130,DVar(useSites={46},value=int ∈ [1,2147483647],origin=45),BinaryExpr(pc=130,ComputationalTypeInt,UVar(defSites={42,47},value=int ∈ [0,2147483646]),+,UVar(defSites={44},value=int = 1))),
	46: Assignment(pc=131,DVar(useSites={49,47},value=an int,origin=46),BinaryExpr(pc=131,ComputationalTypeInt,UVar(defSites={40,46},value=an int),*,UVar(defSites={45},value=int ∈ [1,2147483647]))),
	47: Assignment(pc=133,DVar(useSites={48,45,43},value=int ∈ [1,2147483647],origin=47),BinaryExpr(pc=133,ComputationalTypeInt,UVar(defSites={42,47},value=int ∈ [0,2147483646]),+,IntConst(pc=133,1))),
	48: Goto(pc=136,target=43),
	49: Assignment(pc=140,DVar(useSites={102,93},value=java.lang.String[][↦140;refId=724],origin=49),NewArray(pc=140,[UVar(defSites={40,46},value=an int)],java.lang.String[])),
	50: Assignment(pc=145,DVar(useSites={56,70,71},value=int[][↦145;refId=726],origin=50),NewArray(pc=145,[UVar(defSites={41},value=an int)],int[])),
	51: Assignment(pc=149,DVar(useSites={56,53,59},value=int = 0,origin=51),IntConst(pc=149,0)),
	52: Assignment(pc=152,DVar(useSites={58,54},value=int = 0,origin=52),IntConst(pc=152,0)),
	53: If(pc=158,UVar(defSites={51,59},value=int ∈ [0,2147483647]),>=,UVar(defSites={41},value=an int),target=61),
	54: Assignment(pc=164,DVar(useSites={57,55},value=an int,origin=54),StaticFunctionCall(pc=164,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={52,58},value=an int)))),
	55: Assignment(pc=175,DVar(useSites={56},value=an int,origin=55),StaticFunctionCall(pc=175,java.util.regex.Pattern,isInterface=false,int getClass(int),(UVar(defSites={54},value=an int)))),
	56: ArrayStore(pc=178,UVar(defSites={50},value=int[][↦145;refId=726]),UVar(defSites={51,59},value=int ∈ [0,2147483646]),UVar(defSites={55},value=an int)),
	57: Assignment(pc=183,DVar(useSites={58},value=an int,origin=57),StaticFunctionCall(pc=183,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={54},value=an int)))),
	58: Assignment(pc=186,DVar(useSites={54,59},value=an int,origin=58),BinaryExpr(pc=186,ComputationalTypeInt,UVar(defSites={52,58},value=an int),+,UVar(defSites={57},value=an int))),
	59: Assignment(pc=189,DVar(useSites={56,60,53},value=int ∈ [1,2147483647],origin=59),BinaryExpr(pc=189,ComputationalTypeInt,UVar(defSites={51,59},value=int ∈ [0,2147483646]),+,IntConst(pc=189,1))),
	60: Goto(pc=192,target=53),
	61: Assignment(pc=195,DVar(useSites={102,93,99,87},value=int = 0,origin=61),IntConst(pc=195,0)),
	62: Assignment(pc=198,DVar(useSites={64,96,68,71},value=int = 0,origin=62),IntConst(pc=198,0)),
	63: Assignment(pc=201,DVar(useSites={66,82,78,97,81,77},value=int = 0,origin=63),IntConst(pc=201,0)),
	64: If(pc=207,UVar(defSites={96,62},value=an int),>=,UVar(defSites={41},value=an int),target=99),
	65: Assignment(pc=213,DVar(useSites={66},value=int = 1,origin=65),IntConst(pc=213,1)),
	66: Assignment(pc=214,DVar(useSites={97,81,77},value=an int,origin=66),StaticFunctionCall(pc=214,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={97,63},value=an int),UVar(defSites={65},value=int = 1)))),
	67: Assignment(pc=221,DVar(useSites={68},value=int = 1,origin=67),IntConst(pc=221,1)),
	68: Assignment(pc=222,DVar(useSites={70,73,69},value=an int,origin=68),BinaryExpr(pc=222,ComputationalTypeInt,UVar(defSites={96,62},value=int ∈ [-2147483648,2147483646]),-,UVar(defSites={67},value=int = 1))),
	69: If(pc=227,UVar(defSites={68,73},value=an int),<,IntConst(pc=-333,0),target=75),
	70: Assignment(pc=234,DVar(useSites={72},value=an int,origin=70),ArrayLoad(pc=234,UVar(defSites={68,73},value=int ∈ [0,2147483647]),UVar(defSites={50},value=int[][↦145;refId=726]))),
	71: Assignment(pc=239,DVar(useSites={72},value=an int,origin=71),ArrayLoad(pc=239,UVar(defSites={96,62},value=an int),UVar(defSites={50},value=int[][↦145;refId=726]))),
	72: If(pc=240,UVar(defSites={70},value=an int),==,UVar(defSites={71},value=an int),target=96),
	73: Assignment(pc=246,DVar(useSites={74,70,69},value=int ∈ [-1,2147483646],origin=73),BinaryExpr(pc=246,ComputationalTypeInt,UVar(defSites={68,73},value=int ∈ [0,2147483647]),+,IntConst(pc=246,-1))),
	74: Goto(pc=249,target=69),
	75: Assignment(pc=252,DVar(useSites={76,78},value=java.lang.StringBuilder[↦252;refId=1281],origin=75),New(pc=252,java.lang.StringBuilder)),
	76: NonVirtualMethodCall(pc=257,java.lang.StringBuilder,isInterface=false,void <init>(java.lang.String),UVar(defSites={75},value=java.lang.StringBuilder[↦252;refId=1281]),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]))),
	77: Assignment(pc=270,DVar(useSites={78},value=an int,origin=77),BinaryExpr(pc=270,ComputationalTypeInt,UVar(defSites={97,63},value=an int),+,UVar(defSites={66},value=an int))),
	78: Assignment(pc=271,DVar(useSites={79},value={java.lang.StringBuilder, null}[↦271;refId=1284],origin=78),VirtualFunctionCall(pc=271,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder delete(int,int),UVar(defSites={75},value=java.lang.StringBuilder[↦252;refId=1281]),(UVar(defSites={97,63},value=an int),UVar(defSites={77},value=an int)))),
	79: Assignment(pc=274,DVar(useSites={80},value={java.lang.String, null}[↦274;refId=1287],origin=79),VirtualFunctionCall(pc=274,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={78},value={java.lang.StringBuilder, null}[↦271;refId=1284]),())),
	80: Assignment(pc=281,DVar(useSites={86,83},value={java.lang.String[], null}[↦281;refId=1289],origin=80),StaticFunctionCall(pc=281,java.util.regex.Pattern,isInterface=false,java.lang.String[] producePermutations(java.lang.String),(UVar(defSites={79},value={java.lang.String, null}[↦274;refId=1287])))),
	81: Assignment(pc=293,DVar(useSites={82},value=an int,origin=81),BinaryExpr(pc=293,ComputationalTypeInt,UVar(defSites={97,63},value=an int),+,UVar(defSites={66},value=an int))),
	82: Assignment(pc=294,DVar(useSites={90},value={java.lang.String, null}[↦294;refId=1291],origin=82),VirtualFunctionCall(pc=294,java.lang.String,isInterface=false,java.lang.String substring(int,int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={97,63},value=an int),UVar(defSites={81},value=an int)))),
	83: Assignment(pc=305,DVar(useSites={85},value=int ∈ [0,2147483647],origin=83),ArrayLength(pc=305,UVar(defSites={80},value={java.lang.String[], null}[↦281;refId=1289]))),
	84: Assignment(pc=308,DVar(useSites={86,94,85},value=int = 0,origin=84),IntConst(pc=308,0)),
	85: If(pc=315,UVar(defSites={84,94},value=int ∈ [0,2147483647]),>=,UVar(defSites={83},value=int ∈ [0,2147483647]),target=96),
	86: Assignment(pc=322,DVar(useSites={91},value={java.lang.String, null}[↦322;refId=1294],origin=86),ArrayLoad(pc=322,UVar(defSites={84,94},value=int ∈ [0,2147483646]),UVar(defSites={80},value=java.lang.String[][↦281;refId=1289]))),
	87: Assignment(pc=328,DVar(useSites={88,102,93,99},value=an int,origin=87),BinaryExpr(pc=328,ComputationalTypeInt,UVar(defSites={61,87},value=an int),+,IntConst(pc=328,1))),
	88: Assignment(pc=331,DVar(useSites={90,89},value=java.lang.StringBuilder[↦331;refId=1295],origin=88),New(pc=331,java.lang.StringBuilder)),
	89: NonVirtualMethodCall(pc=335,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={88},value=java.lang.StringBuilder[↦331;refId=1295]),()),
	90: Assignment(pc=340,DVar(useSites={91},value={java.lang.StringBuilder, null}[↦340;refId=1298],origin=90),VirtualFunctionCall(pc=340,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={88},value=java.lang.StringBuilder[↦331;refId=1295]),(UVar(defSites={82},value={java.lang.String, null}[↦294;refId=1291])))),
	91: Assignment(pc=345,DVar(useSites={92},value={java.lang.StringBuilder, null}[↦345;refId=1301],origin=91),VirtualFunctionCall(pc=345,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={90},value={java.lang.StringBuilder, null}[↦340;refId=1298]),(UVar(defSites={86},value={java.lang.String, null}[↦322;refId=1294])))),
	92: Assignment(pc=348,DVar(useSites={93},value={java.lang.String, null}[↦348;refId=1304],origin=92),VirtualFunctionCall(pc=348,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={91},value={java.lang.StringBuilder, null}[↦345;refId=1301]),())),
	93: ArrayStore(pc=351,UVar(defSites={49},value=java.lang.String[][↦140;refId=724]),UVar(defSites={61,87},value=an int),UVar(defSites={92},value={java.lang.String, null}[↦348;refId=1304])),
	94: Assignment(pc=352,DVar(useSites={86,85,95},value=int ∈ [1,2147483647],origin=94),BinaryExpr(pc=352,ComputationalTypeInt,UVar(defSites={84,94},value=int ∈ [0,2147483646]),+,IntConst(pc=352,1))),
	95: Goto(pc=355,target=85),
	96: Assignment(pc=358,DVar(useSites={64,68,97,71},value=an int,origin=96),BinaryExpr(pc=358,ComputationalTypeInt,UVar(defSites={96,62},value=an int),+,IntConst(pc=358,1))),
	97: Assignment(pc=365,DVar(useSites={66,98,82,78,81,77},value=an int,origin=97),BinaryExpr(pc=365,ComputationalTypeInt,UVar(defSites={97,63},value=an int),+,UVar(defSites={66},value=an int))),
	98: Goto(pc=368,target=64),
	99: Assignment(pc=373,DVar(useSites={102,103},value=java.lang.String[][↦373;refId=1274],origin=99),NewArray(pc=373,[UVar(defSites={61,87},value=an int)],java.lang.String[])),
	100: Assignment(pc=379,DVar(useSites={102},value=int = 0,origin=100),IntConst(pc=379,0)),
	101: Assignment(pc=382,DVar(useSites={102},value=int = 0,origin=101),IntConst(pc=382,0)),
	102: StaticMethodCall(pc=385,java.lang.System,isInterface=false,void arraycopy(java.lang.Object,int,java.lang.Object,int,int),(UVar(defSites={49},value=java.lang.String[][↦140;refId=724]),UVar(defSites={100},value=int = 0),UVar(defSites={99},value=java.lang.String[][↦373;refId=1274]),UVar(defSites={101},value=int = 0),UVar(defSites={61,87},value=an int))),
	103: ReturnValue(pc=390,UVar(defSites={99},value=java.lang.String[][↦373;refId=1274]))
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=9) -> {BB_28}
	BB_10: BasicBlock(start=61,end=63) -> {BB_1a}
	BB_11: BasicBlock(start=1,end=3) -> {BB_3a,BB_37}
	BB_12: BasicBlock(start=38,end=39) -> {BB_28}
	BB_13: BasicBlock(start=70,end=70) -> {BB_3a,BB_1f}
	BB_14: BasicBlock(start=21,end=21) -> {BB_1e,BB_1c}
	BB_15: BasicBlock(start=92,end=92) -> {BB_3a,BB_e}
	BB_16: BasicBlock(start=65,end=66) -> {BB_3a,BB_2a}
	BB_17: BasicBlock(start=77,end=78) -> {BB_3a,BB_38}
	BB_18: BasicBlock(start=96,end=98) -> {BB_1a}
	BB_19: BasicBlock(start=34,end=34) -> {BB_3a,BB_26}
	BB_1: BasicBlock(start=42,end=42) -> {BB_2d}
	BB_1a: BasicBlock(start=64,end=64) -> {BB_16,BB_2e}
	BB_1b: BasicBlock(start=17,end=17) -> {BB_3a,BB_27}
	BB_1c: BasicBlock(start=22,end=26) -> {BB_28}
	BB_1d: BasicBlock(start=44,end=48) -> {BB_2d}
	BB_1e: BasicBlock(start=27,end=33) -> {BB_3a,BB_19}
	BB_1f: BasicBlock(start=71,end=71) -> {BB_3a,BB_2c}
	BB_20: BasicBlock(start=54,end=54) -> {BB_3a,BB_31}
	BB_21: BasicBlock(start=49,end=49) -> {BB_3a,BB_29}
	BB_22: BasicBlock(start=86,end=86) -> {BB_3a,BB_2f}
	BB_23: BasicBlock(start=103,end=103) -> {BB_28}
	BB_24: BasicBlock(start=91,end=91) -> {BB_3a,BB_15}
	BB_25: BasicBlock(start=80,end=80) -> {BB_3a,BB_7}
	BB_26: BasicBlock(start=35,end=35) -> {BB_3a,BB_34}
	BB_27: BasicBlock(start=18,end=18) -> {BB_3a,BB_36}
	BB_28: ExitNode(normalReturn=true)
	BB_29: BasicBlock(start=50,end=50) -> {BB_3a,BB_35}
	BB_2: BasicBlock(start=14,end=14) -> {BB_30,BB_8}
	BB_2a: BasicBlock(start=67,end=68) -> {BB_9}
	BB_2b: BasicBlock(start=11,end=13) -> {BB_3a,BB_2}
	BB_2c: BasicBlock(start=72,end=72) -> {BB_18,BB_6}
	BB_2d: BasicBlock(start=43,end=43) -> {BB_21,BB_1d}
	BB_2e: BasicBlock(start=99,end=99) -> {BB_3a,BB_3d}
	BB_2f: BasicBlock(start=87,end=89) -> {BB_3a,BB_3b}
	BB_30: BasicBlock(start=40,end=41) -> {BB_3a,BB_1}
	BB_31: BasicBlock(start=55,end=55) -> {BB_3a,BB_c}
	BB_32: BasicBlock(start=75,end=76) -> {BB_3a,BB_17}
	BB_33: BasicBlock(start=58,end=60) -> {BB_5}
	BB_34: BasicBlock(start=36,end=37) -> {BB_3a,BB_12}
	BB_35: BasicBlock(start=51,end=52) -> {BB_5}
	BB_36: BasicBlock(start=19,end=19) -> {BB_3a,BB_d}
	BB_37: BasicBlock(start=4,end=4) -> {BB_b,BB_0}
	BB_38: BasicBlock(start=79,end=79) -> {BB_3a,BB_25}
	BB_39: BasicBlock(start=94,end=95) -> {BB_4}
	BB_3: BasicBlock(start=84,end=84) -> {BB_4}
	BB_3a: ExitNode(normalReturn=false)
	BB_3b: BasicBlock(start=90,end=90) -> {BB_3a,BB_24}
	BB_3c: BasicBlock(start=83,end=83) -> {BB_3a,BB_3}
	BB_3d: BasicBlock(start=100,end=102) -> {BB_3a,BB_23}
	BB_4: BasicBlock(start=85,end=85) -> {BB_18,BB_22}
	BB_5: BasicBlock(start=53,end=53) -> {BB_20,BB_10}
	BB_6: BasicBlock(start=73,end=74) -> {BB_9}
	BB_7: BasicBlock(start=81,end=82) -> {BB_3a,BB_3c}
	BB_8: BasicBlock(start=15,end=16) -> {BB_3a,BB_1b}
	BB_9: BasicBlock(start=69,end=69) -> {BB_32,BB_13}
	BB_a: BasicBlock(start=0,end=0) -> {BB_3a,BB_11}
	BB_b: BasicBlock(start=10,end=10) -> {BB_3a,BB_2b}
	BB_c: BasicBlock(start=56,end=56) -> {BB_3a,BB_f}
	BB_d: BasicBlock(start=20,end=20) -> {BB_3a,BB_14}
	BB_e: BasicBlock(start=93,end=93) -> {BB_3a,BB_39}
	BB_f: BasicBlock(start=57,end=57) -> {BB_3a,BB_33}
))

java.util.regex.Pattern$Node atom()
AITACode(params=(Parameters(
	0: useSites={8,72,88,68,36,84,12,60,18,42,26,46,65,33,81,85,53,77,45,29,3,67,43,71,39,87,55,63} (origin=-1)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={80,48,72,88,56,62,17,9,73,7,55},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=2,DVar(useSites={8},value=int = -1,origin=1),IntConst(pc=2,-1)),
	2: Assignment(pc=4,DVar(useSites={88},value=int = 0,origin=2),IntConst(pc=4,0)),
	3: Assignment(pc=7,DVar(useSites={72,74,5},value=an int,origin=3),VirtualFunctionCall(pc=7,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	4: Nop(pc=10),
	5: Switch(pc=14,defaultTarget=71,index=UVar(defSites={60,77,3},value=an int),npairs=(IntIntPair(0,67),IntIntPair(36,11),IntIntPair(40,11),IntIntPair(41,11),IntIntPair(42,6),IntIntPair(43,6),IntIntPair(46,11),IntIntPair(63,6),IntIntPair(91,11),IntIntPair(92,12),IntIntPair(94,11),IntIntPair(123,6),IntIntPair(124,11)),
	6: Assignment(pc=129,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=129,1)),
	7: If(pc=130,UVar(defSites={0,56,73},value=an int),<=,UVar(defSites={6},value=int = 1),target=79),
	8: PutField(pc=135,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={46,1,71},value=an int)),
	9: Assignment(pc=138,DVar(useSites={80,88},value=int ∈ [1,2147483646],origin=9),BinaryExpr(pc=138,ComputationalTypeInt,UVar(defSites={0,56,73},value=int ∈ [2,2147483647]),+,IntConst(pc=138,-1))),
	10: Goto(pc=141,target=79),
	11: Goto(pc=144,target=79),
	12: Assignment(pc=148,DVar(useSites={16,14,21},value=an int,origin=12),VirtualFunctionCall(pc=148,java.util.regex.Pattern,isInterface=false,int nextEscaped(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	13: Assignment(pc=155,DVar(useSites={14},value=int = 112,origin=13),IntConst(pc=155,112)),
	14: If(pc=157,UVar(defSites={12},value=an int),==,UVar(defSites={13},value=int = 112),target=17),
	15: Assignment(pc=162,DVar(useSites={16},value=int = 80,origin=15),IntConst(pc=162,80)),
	16: If(pc=164,UVar(defSites={12},value=an int),!=,UVar(defSites={15},value=int = 80),target=45),
	17: If(pc=168,UVar(defSites={0,56,73},value=an int),<=,IntConst(pc=-333,0),target=20),
	18: VirtualMethodCall(pc=172,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	19: Goto(pc=175,target=79),
	20: Assignment(pc=180,DVar(useSites={21},value=int = 80,origin=20),IntConst(pc=180,80)),
	21: If(pc=182,UVar(defSites={12},value=int ∈ [80,112]),!=,UVar(defSites={20},value=int = 80),target=24),
	22: Assignment(pc=185,DVar(useSites={42,39},value=int = 1,origin=22),IntConst(pc=185,1)),
	23: Goto(pc=186,target=25),
	24: Assignment(pc=189,DVar(useSites={42,39},value=int ∈ [0,1],origin=24),IntConst(pc=189,0)),
	25: Assignment(pc=192,DVar(useSites={42,39},value=int = 1,origin=25),IntConst(pc=192,1)),
	26: Assignment(pc=196,DVar(useSites={28},value=an int,origin=26),VirtualFunctionCall(pc=196,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	27: Assignment(pc=203,DVar(useSites={28},value=int = 123,origin=27),IntConst(pc=203,123)),
	28: If(pc=205,UVar(defSites={26},value=an int),==,UVar(defSites={27},value=int = 123),target=31),
	29: VirtualMethodCall(pc=209,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	30: Goto(pc=212,target=32),
	31: Assignment(pc=215,DVar(useSites={42,39},value=int = 0,origin=31),IntConst(pc=215,0)),
	32: Assignment(pc=219,DVar(useSites={33},value=int = 128,origin=32),IntConst(pc=219,128)),
	33: Assignment(pc=222,DVar(useSites={34},value=int ∈ [0,1],origin=33),VirtualFunctionCall(pc=222,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={32},value=int = 128)))),
	34: If(pc=225,UVar(defSites={33},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=42),
	35: Assignment(pc=229,DVar(useSites={36},value=int = 16,origin=35),IntConst(pc=229,16)),
	36: Assignment(pc=231,DVar(useSites={37},value=int ∈ [0,1],origin=36),VirtualFunctionCall(pc=231,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={35},value=int = 16)))),
	37: If(pc=234,UVar(defSites={36},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=42),
	38: Assignment(pc=237,DVar(useSites={40,41},value=java.util.regex.Pattern$NFCCharProperty[↦237;refId=123],origin=38),New(pc=237,java.util.regex.Pattern$NFCCharProperty)),
	39: Assignment(pc=246,DVar(useSites={40},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦246;refId=125],origin=39),VirtualFunctionCall(pc=246,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate family(boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={25,31},value=int ∈ [0,1]),UVar(defSites={24,22},value=int ∈ [0,1])))),
	40: NonVirtualMethodCall(pc=249,java.util.regex.Pattern$NFCCharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={38},value=java.util.regex.Pattern$NFCCharProperty[↦237;refId=123]),(UVar(defSites={39},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦246;refId=125]))),
	41: ReturnValue(pc=252,UVar(defSites={38},value=java.util.regex.Pattern$NFCCharProperty[↦237;refId=123])),
	42: Assignment(pc=259,DVar(useSites={43},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦259;refId=145],origin=42),VirtualFunctionCall(pc=259,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate family(boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={25,31},value=int ∈ [0,1]),UVar(defSites={24,22},value=int ∈ [0,1])))),
	43: Assignment(pc=262,DVar(useSites={44},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦262;refId=147],origin=43),VirtualFunctionCall(pc=262,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={42},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦259;refId=145])))),
	44: ReturnValue(pc=265,UVar(defSites={43},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦262;refId=147])),
	45: VirtualMethodCall(pc=267,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	46: Assignment(pc=271,DVar(useSites={8,65},value=an int,origin=46),GetField(pc=271,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	47: Assignment(pc=276,DVar(useSites={53},value=int = 0,origin=47),IntConst(pc=276,0)),
	48: If(pc=278,UVar(defSites={0,56,73},value=an int),!=,IntConst(pc=-333,0),target=51),
	49: Assignment(pc=281,DVar(useSites={53},value=int = 1,origin=49),IntConst(pc=281,1)),
	50: Goto(pc=282,target=52),
	51: Assignment(pc=285,DVar(useSites={53},value=int ∈ [0,1],origin=51),IntConst(pc=285,0)),
	52: Assignment(pc=286,DVar(useSites={53},value=int = 0,origin=52),IntConst(pc=286,0)),
	53: Assignment(pc=287,DVar(useSites={54,57,55},value=an int,origin=53),VirtualFunctionCall(pc=287,java.util.regex.Pattern,isInterface=false,int escape(boolean,boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={47},value=int = 0),UVar(defSites={49,51},value=int ∈ [0,1]),UVar(defSites={52},value=int = 0)))),
	54: If(pc=294,UVar(defSites={53},value=an int),<,IntConst(pc=-333,0),target=62),
	55: VirtualMethodCall(pc=301,java.util.regex.Pattern,isInterface=false,void append(int,int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={53},value=int ∈ [0,2147483647]),UVar(defSites={0,56,73},value=an int))),
	56: Assignment(pc=304,DVar(useSites={80,48,72,88,62,17,9,73,57,7,55},value=an int,origin=56),BinaryExpr(pc=304,ComputationalTypeInt,UVar(defSites={0,56,73},value=an int),+,IntConst(pc=304,1))),
	57: Assignment(pc=309,DVar(useSites={58},value=int ∈ [0,1],origin=57),StaticFunctionCall(pc=309,java.util.regex.Pattern,isInterface=false,boolean isSupplementary(int),(UVar(defSites={53},value=int ∈ [0,2147483647])))),
	58: If(pc=312,UVar(defSites={57},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=60),
	59: Assignment(pc=315,DVar(useSites={88},value=int = 1,origin=59),IntConst(pc=315,1)),
	60: Assignment(pc=318,DVar(useSites={72,74,5},value=an int,origin=60),VirtualFunctionCall(pc=318,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	61: Goto(pc=323,target=5),
	62: If(pc=327,UVar(defSites={0,56,73},value=an int),!=,IntConst(pc=-333,0),target=65),
	63: Assignment(pc=331,DVar(useSites={64},value={_ <: java.util.regex.Pattern$Node, null}[↦331;refId=557],origin=63),GetField(pc=331,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	64: ReturnValue(pc=334,UVar(defSites={63},value={_ <: java.util.regex.Pattern$Node, null}[↦331;refId=557])),
	65: PutField(pc=337,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={46},value=an int)),
	66: Goto(pc=340,target=79),
	67: Assignment(pc=344,DVar(useSites={69},value=an int,origin=67),GetField(pc=344,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	68: Assignment(pc=348,DVar(useSites={69},value=an int,origin=68),GetField(pc=348,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	69: If(pc=351,UVar(defSites={67},value=an int),>=,UVar(defSites={68},value=an int),target=79),
	70: Nop(pc=354),
	71: Assignment(pc=358,DVar(useSites={8},value=an int,origin=71),GetField(pc=358,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	72: VirtualMethodCall(pc=366,java.util.regex.Pattern,isInterface=false,void append(int,int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={60,77,3},value=an int),UVar(defSites={0,56,73},value=an int))),
	73: Assignment(pc=369,DVar(useSites={80,48,72,88,56,74,62,17,9,7,55},value=an int,origin=73),BinaryExpr(pc=369,ComputationalTypeInt,UVar(defSites={0,56,73},value=an int),+,IntConst(pc=369,1))),
	74: Assignment(pc=374,DVar(useSites={75},value=int ∈ [0,1],origin=74),StaticFunctionCall(pc=374,java.util.regex.Pattern,isInterface=false,boolean isSupplementary(int),(UVar(defSites={60,77,3},value=an int)))),
	75: If(pc=377,UVar(defSites={74},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=77),
	76: Assignment(pc=380,DVar(useSites={88},value=int = 1,origin=76),IntConst(pc=380,1)),
	77: Assignment(pc=383,DVar(useSites={72,74,5},value=an int,origin=77),VirtualFunctionCall(pc=383,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	78: Goto(pc=388,target=5),
	79: Assignment(pc=392,DVar(useSites={80},value=int = 1,origin=79),IntConst(pc=392,1)),
	80: If(pc=393,UVar(defSites={0,56,9,73},value=an int),!=,UVar(defSites={79},value=int = 1),target=87),
	81: Assignment(pc=399,DVar(useSites={83},value={int[], null}[↦399;refId=561],origin=81),GetField(pc=399,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	82: Assignment(pc=402,DVar(useSites={83},value=int = 0,origin=82),IntConst(pc=402,0)),
	83: Assignment(pc=403,DVar(useSites={84},value=an int,origin=83),ArrayLoad(pc=403,UVar(defSites={82},value=int = 0),UVar(defSites={81},value={int[], null}[↦399;refId=561]))),
	84: Assignment(pc=404,DVar(useSites={85},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦404;refId=565],origin=84),VirtualFunctionCall(pc=404,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate single(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={83},value=an int)))),
	85: Assignment(pc=407,DVar(useSites={86},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦407;refId=567],origin=85),VirtualFunctionCall(pc=407,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={84},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦404;refId=565])))),
	86: ReturnValue(pc=410,UVar(defSites={85},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦407;refId=567])),
	87: Assignment(pc=413,DVar(useSites={88},value={int[], null}[↦413;refId=558],origin=87),GetField(pc=413,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	88: Assignment(pc=418,DVar(useSites={89},value={_ <: java.util.regex.Pattern$Node, null}[↦418;refId=560],origin=88),VirtualFunctionCall(pc=418,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node newSlice(int[],int,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={87},value={int[], null}[↦413;refId=558]),UVar(defSites={0,56,9,73},value=an int),UVar(defSites={76,2,59},value=int ∈ [0,1])))),
	89: ReturnValue(pc=421,UVar(defSites={88},value={_ <: java.util.regex.Pattern$Node, null}[↦418;refId=560]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_3b,BB_39}
	BB_10: BasicBlock(start=78,end=78) -> {BB_1}
	BB_11: BasicBlock(start=29,end=29) -> {BB_3b,BB_36}
	BB_12: BasicBlock(start=61,end=61) -> {BB_1}
	BB_13: BasicBlock(start=89,end=89) -> {BB_2c}
	BB_14: BasicBlock(start=6,end=7) -> {BB_33,BB_3a}
	BB_15: BasicBlock(start=60,end=60) -> {BB_3b,BB_12}
	BB_16: BasicBlock(start=85,end=85) -> {BB_3b,BB_27}
	BB_17: BasicBlock(start=38,end=39) -> {BB_3b,BB_31}
	BB_18: BasicBlock(start=70,end=70) -> {BB_23}
	BB_19: BasicBlock(start=13,end=14) -> {BB_3c,BB_1c}
	BB_1: BasicBlock(start=5,end=5) -> {BB_14,BB_2d,BB_23,BB_24,BB_2f}
	BB_1a: BasicBlock(start=41,end=41) -> {BB_2c}
	BB_1b: BasicBlock(start=45,end=45) -> {BB_3b,BB_f}
	BB_1c: BasicBlock(start=17,end=17) -> {BB_e,BB_2b}
	BB_1d: BasicBlock(start=32,end=33) -> {BB_3b,BB_1e}
	BB_1e: BasicBlock(start=34,end=34) -> {BB_8,BB_a}
	BB_1f: BasicBlock(start=22,end=23) -> {BB_d}
	BB_20: BasicBlock(start=44,end=44) -> {BB_2c}
	BB_21: BasicBlock(start=59,end=59) -> {BB_15}
	BB_22: BasicBlock(start=27,end=28) -> {BB_11,BB_2e}
	BB_23: BasicBlock(start=71,end=72) -> {BB_3b,BB_7}
	BB_24: BasicBlock(start=12,end=12) -> {BB_3b,BB_19}
	BB_25: BasicBlock(start=54,end=54) -> {BB_3d,BB_32}
	BB_26: BasicBlock(start=49,end=50) -> {BB_3}
	BB_27: BasicBlock(start=86,end=86) -> {BB_2c}
	BB_28: BasicBlock(start=81,end=83) -> {BB_3b,BB_4}
	BB_29: BasicBlock(start=76,end=76) -> {BB_6}
	BB_2: BasicBlock(start=56,end=57) -> {BB_3b,BB_35}
	BB_2a: BasicBlock(start=63,end=64) -> {BB_2c}
	BB_2b: BasicBlock(start=18,end=18) -> {BB_3b,BB_38}
	BB_2c: ExitNode(normalReturn=true)
	BB_2d: BasicBlock(start=67,end=69) -> {BB_18,BB_3a}
	BB_2e: BasicBlock(start=31,end=31) -> {BB_1d}
	BB_2f: BasicBlock(start=11,end=11) -> {BB_3a}
	BB_30: BasicBlock(start=43,end=43) -> {BB_3b,BB_20}
	BB_31: BasicBlock(start=40,end=40) -> {BB_3b,BB_1a}
	BB_32: BasicBlock(start=55,end=55) -> {BB_3b,BB_2}
	BB_33: BasicBlock(start=8,end=10) -> {BB_3a}
	BB_34: BasicBlock(start=75,end=75) -> {BB_29,BB_6}
	BB_35: BasicBlock(start=58,end=58) -> {BB_15,BB_21}
	BB_36: BasicBlock(start=30,end=30) -> {BB_1d}
	BB_37: BasicBlock(start=51,end=51) -> {BB_3}
	BB_38: BasicBlock(start=19,end=19) -> {BB_3a}
	BB_39: BasicBlock(start=4,end=4) -> {BB_1}
	BB_3: BasicBlock(start=52,end=53) -> {BB_3b,BB_25}
	BB_3a: BasicBlock(start=79,end=80) -> {BB_28,BB_9}
	BB_3b: ExitNode(normalReturn=false)
	BB_3c: BasicBlock(start=15,end=16) -> {BB_1b,BB_1c}
	BB_3d: BasicBlock(start=62,end=62) -> {BB_2a,BB_5}
	BB_4: BasicBlock(start=84,end=84) -> {BB_3b,BB_16}
	BB_5: BasicBlock(start=65,end=66) -> {BB_3a}
	BB_6: BasicBlock(start=77,end=77) -> {BB_3b,BB_10}
	BB_7: BasicBlock(start=73,end=74) -> {BB_3b,BB_34}
	BB_8: BasicBlock(start=35,end=36) -> {BB_3b,BB_c}
	BB_9: BasicBlock(start=87,end=88) -> {BB_3b,BB_13}
	BB_a: BasicBlock(start=42,end=42) -> {BB_3b,BB_30}
	BB_b: BasicBlock(start=24,end=24) -> {BB_d}
	BB_c: BasicBlock(start=37,end=37) -> {BB_17,BB_a}
	BB_d: BasicBlock(start=25,end=26) -> {BB_3b,BB_22}
	BB_e: BasicBlock(start=20,end=21) -> {BB_1f,BB_b}
	BB_f: BasicBlock(start=46,end=48) -> {BB_26,BB_37}
))

boolean lambda$DOT$5(int)
AITACode(params=(Parameters(
	1: useSites={1,9,5,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 10,origin=0),IntConst(pc=1,10)),
	1: If(pc=3,UVar(defSites={-2},value=an int),==,UVar(defSites={0},value=int = 10),target=12),
	2: Assignment(pc=7,DVar(useSites={3},value=int = 13,origin=2),IntConst(pc=7,13)),
	3: If(pc=9,UVar(defSites={-2},value=an int),==,UVar(defSites={2},value=int = 13),target=12),
	4: Assignment(pc=13,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=13,1)),
	5: Assignment(pc=14,DVar(useSites={7},value=an int,origin=5),BinaryExpr(pc=14,ComputationalTypeInt,UVar(defSites={-2},value=an int),|,UVar(defSites={4},value=int = 1))),
	6: Assignment(pc=15,DVar(useSites={7},value=int = 8233,origin=6),IntConst(pc=15,8233)),
	7: If(pc=18,UVar(defSites={5},value=an int),==,UVar(defSites={6},value=int = 8233),target=12),
	8: Assignment(pc=22,DVar(useSites={9},value=int = 133,origin=8),IntConst(pc=22,133)),
	9: If(pc=25,UVar(defSites={-2},value=an int),==,UVar(defSites={8},value=int = 133),target=12),
	10: Assignment(pc=28,DVar(useSites={13},value=int = 1,origin=10),IntConst(pc=28,1)),
	11: Goto(pc=29,target=13),
	12: Assignment(pc=32,DVar(useSites={13},value=int ∈ [0,1],origin=12),IntConst(pc=32,0)),
	13: ReturnValue(pc=33,UVar(defSites={12,10},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_3}
	BB_1: BasicBlock(start=10,end=11) -> {BB_2}
	BB_2: BasicBlock(start=13,end=13) -> {BB_5}
	BB_3: BasicBlock(start=2,end=3) -> {BB_4,BB_7}
	BB_4: BasicBlock(start=12,end=12) -> {BB_2}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=8,end=9) -> {BB_4,BB_1}
	BB_7: BasicBlock(start=4,end=7) -> {BB_4,BB_6}
	BB_8: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate CIRange(int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value={_ <: java.util.regex.Pattern$CIRange(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda, null}[↦2;refId=103],origin=0),StaticFunctionCall(pc=2,java.util.regex.Pattern$CIRange(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda,isInterface=false,java.util.regex.Pattern$CIRange(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda $newInstance(int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value=an int)))),
	1: ReturnValue(pc=7,UVar(defSites={0},value={_ <: java.util.regex.Pattern$CIRange(II)Ljava$util$regex$Pattern$CharPredicate::2$Lambda, null}[↦2;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$Node newSlice(int[],int,boolean)
AITACode(params=(Parameters(
	0: useSites={2,5} (origin=-1),
	1: useSites={24,38,9} (origin=-2),
	2: useSites={0,8,37,23} (origin=-3),
	3: useSites={42,29,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={20,12,44,34,26,17,39,47,31},value=int[][↦1;refId=104],origin=0),NewArray(pc=1,[UVar(defSites={-3},value=an int)],int[])),
	1: Assignment(pc=6,DVar(useSites={2},value=int = 2,origin=1),IntConst(pc=6,2)),
	2: Assignment(pc=7,DVar(useSites={3},value=int ∈ [0,1],origin=2),VirtualFunctionCall(pc=7,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={1},value=int = 2)))),
	3: If(pc=10,UVar(defSites={2},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=36),
	4: Assignment(pc=14,DVar(useSites={5},value=int = 64,origin=4),IntConst(pc=14,64)),
	5: Assignment(pc=16,DVar(useSites={6},value=int ∈ [0,1],origin=5),VirtualFunctionCall(pc=16,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={4},value=int = 64)))),
	6: If(pc=19,UVar(defSites={5},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=22),
	7: Assignment(pc=22,DVar(useSites={8,12,9,13},value=int = 0,origin=7),IntConst(pc=22,0)),
	8: If(pc=28,UVar(defSites={13,7},value=int ∈ [0,2147483647]),>=,UVar(defSites={-3},value=an int),target=15),
	9: Assignment(pc=38,DVar(useSites={10},value=an int,origin=9),ArrayLoad(pc=38,UVar(defSites={13,7},value=int ∈ [0,2147483646]),UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	10: Assignment(pc=39,DVar(useSites={11},value=an int,origin=10),StaticFunctionCall(pc=39,java.lang.Character,isInterface=false,int toUpperCase(int),(UVar(defSites={9},value=an int)))),
	11: Assignment(pc=42,DVar(useSites={12},value=an int,origin=11),StaticFunctionCall(pc=42,java.lang.Character,isInterface=false,int toLowerCase(int),(UVar(defSites={10},value=an int)))),
	12: ArrayStore(pc=45,UVar(defSites={0},value=int[][↦1;refId=104]),UVar(defSites={13,7},value=int ∈ [0,2147483646]),UVar(defSites={11},value=an int)),
	13: Assignment(pc=46,DVar(useSites={8,12,14,9},value=int ∈ [1,2147483647],origin=13),BinaryExpr(pc=46,ComputationalTypeInt,UVar(defSites={13,7},value=int ∈ [0,2147483646]),+,IntConst(pc=46,1))),
	14: Goto(pc=49,target=8),
	15: If(pc=53,UVar(defSites={-4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=19),
	16: Assignment(pc=56,DVar(useSites={17,21},value=java.util.regex.Pattern$SliceUS[↦56;refId=705],origin=16),New(pc=56,java.util.regex.Pattern$SliceUS)),
	17: NonVirtualMethodCall(pc=62,java.util.regex.Pattern$SliceUS,isInterface=false,void <init>(int[]),UVar(defSites={16},value=java.util.regex.Pattern$SliceUS[↦56;refId=705]),(UVar(defSites={0},value=int[][↦1;refId=104]))),
	18: Goto(pc=65,target=21),
	19: Assignment(pc=68,DVar(useSites={20,21},value=java.util.regex.Pattern$SliceU[↦68;refId=708],origin=19),New(pc=68,java.util.regex.Pattern$SliceU)),
	20: NonVirtualMethodCall(pc=74,java.util.regex.Pattern$SliceU,isInterface=false,void <init>(int[]),UVar(defSites={19},value=java.util.regex.Pattern$SliceU[↦68;refId=708]),(UVar(defSites={0},value=int[][↦1;refId=104]))),
	21: ReturnValue(pc=77,UVar(defSites={16,19},value=_ <: java.util.regex.Pattern$SliceNode[refId=710; values=«java.util.regex.Pattern$SliceUS[↦56;refId=705], java.util.regex.Pattern$SliceU[↦68;refId=708]»])),
	22: Assignment(pc=78,DVar(useSites={24,26,27,23},value=int = 0,origin=22),IntConst(pc=78,0)),
	23: If(pc=84,UVar(defSites={22,27},value=int ∈ [0,2147483647]),>=,UVar(defSites={-3},value=an int),target=29),
	24: Assignment(pc=94,DVar(useSites={25},value=an int,origin=24),ArrayLoad(pc=94,UVar(defSites={22,27},value=int ∈ [0,2147483646]),UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	25: Assignment(pc=95,DVar(useSites={26},value=an int,origin=25),StaticFunctionCall(pc=95,java.util.regex.ASCII,isInterface=false,int toLower(int),(UVar(defSites={24},value=an int)))),
	26: ArrayStore(pc=98,UVar(defSites={0},value=int[][↦1;refId=104]),UVar(defSites={22,27},value=int ∈ [0,2147483646]),UVar(defSites={25},value=an int)),
	27: Assignment(pc=99,DVar(useSites={24,28,26,23},value=int ∈ [1,2147483647],origin=27),BinaryExpr(pc=99,ComputationalTypeInt,UVar(defSites={22,27},value=int ∈ [0,2147483646]),+,IntConst(pc=99,1))),
	28: Goto(pc=102,target=23),
	29: If(pc=106,UVar(defSites={-4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=33),
	30: Assignment(pc=109,DVar(useSites={35,31},value=java.util.regex.Pattern$SliceIS[↦109;refId=716],origin=30),New(pc=109,java.util.regex.Pattern$SliceIS)),
	31: NonVirtualMethodCall(pc=115,java.util.regex.Pattern$SliceIS,isInterface=false,void <init>(int[]),UVar(defSites={30},value=java.util.regex.Pattern$SliceIS[↦109;refId=716]),(UVar(defSites={0},value=int[][↦1;refId=104]))),
	32: Goto(pc=118,target=35),
	33: Assignment(pc=121,DVar(useSites={34,35},value=java.util.regex.Pattern$SliceI[↦121;refId=719],origin=33),New(pc=121,java.util.regex.Pattern$SliceI)),
	34: NonVirtualMethodCall(pc=127,java.util.regex.Pattern$SliceI,isInterface=false,void <init>(int[]),UVar(defSites={33},value=java.util.regex.Pattern$SliceI[↦121;refId=719]),(UVar(defSites={0},value=int[][↦1;refId=104]))),
	35: ReturnValue(pc=130,UVar(defSites={30,33},value=_ <: java.util.regex.Pattern$SliceNode[refId=721; values=«java.util.regex.Pattern$SliceIS[↦109;refId=716], java.util.regex.Pattern$SliceI[↦121;refId=719]»])),
	36: Assignment(pc=131,DVar(useSites={40,38,37,39},value=int = 0,origin=36),IntConst(pc=131,0)),
	37: If(pc=137,UVar(defSites={40,36},value=int ∈ [0,2147483647]),>=,UVar(defSites={-3},value=an int),target=42),
	38: Assignment(pc=147,DVar(useSites={39},value=an int,origin=38),ArrayLoad(pc=147,UVar(defSites={40,36},value=int ∈ [0,2147483646]),UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	39: ArrayStore(pc=148,UVar(defSites={0},value=int[][↦1;refId=104]),UVar(defSites={40,36},value=int ∈ [0,2147483646]),UVar(defSites={38},value=an int)),
	40: Assignment(pc=149,DVar(useSites={38,41,37,39},value=int ∈ [1,2147483647],origin=40),BinaryExpr(pc=149,ComputationalTypeInt,UVar(defSites={40,36},value=int ∈ [0,2147483646]),+,IntConst(pc=149,1))),
	41: Goto(pc=152,target=37),
	42: If(pc=156,UVar(defSites={-4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=46),
	43: Assignment(pc=159,DVar(useSites={48,44},value=java.util.regex.Pattern$SliceS[↦159;refId=726],origin=43),New(pc=159,java.util.regex.Pattern$SliceS)),
	44: NonVirtualMethodCall(pc=165,java.util.regex.Pattern$SliceS,isInterface=false,void <init>(int[]),UVar(defSites={43},value=java.util.regex.Pattern$SliceS[↦159;refId=726]),(UVar(defSites={0},value=int[][↦1;refId=104]))),
	45: Goto(pc=168,target=48),
	46: Assignment(pc=171,DVar(useSites={48,47},value=java.util.regex.Pattern$Slice[↦171;refId=729],origin=46),New(pc=171,java.util.regex.Pattern$Slice)),
	47: NonVirtualMethodCall(pc=177,java.util.regex.Pattern$Slice,isInterface=false,void <init>(int[]),UVar(defSites={46},value=java.util.regex.Pattern$Slice[↦171;refId=729]),(UVar(defSites={0},value=int[][↦1;refId=104]))),
	48: ReturnValue(pc=180,UVar(defSites={46,43},value=_ <: java.util.regex.Pattern$Slice[refId=731; values=«java.util.regex.Pattern$SliceS[↦159;refId=726], java.util.regex.Pattern$Slice[↦171;refId=729]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_27,BB_2}
	BB_10: BasicBlock(start=38,end=38) -> {BB_27,BB_18}
	BB_11: BasicBlock(start=21,end=21) -> {BB_1d}
	BB_12: BasicBlock(start=33,end=34) -> {BB_27,BB_1a}
	BB_13: BasicBlock(start=32,end=32) -> {BB_1a}
	BB_14: BasicBlock(start=45,end=45) -> {BB_1b}
	BB_15: BasicBlock(start=22,end=22) -> {BB_22}
	BB_16: BasicBlock(start=27,end=28) -> {BB_22}
	BB_17: BasicBlock(start=7,end=7) -> {BB_8}
	BB_18: BasicBlock(start=39,end=39) -> {BB_27,BB_20}
	BB_19: BasicBlock(start=3,end=3) -> {BB_26,BB_23}
	BB_1: BasicBlock(start=10,end=10) -> {BB_27,BB_1e}
	BB_1a: BasicBlock(start=35,end=35) -> {BB_1d}
	BB_1b: BasicBlock(start=48,end=48) -> {BB_1d}
	BB_1c: BasicBlock(start=18,end=18) -> {BB_11}
	BB_1d: ExitNode(normalReturn=true)
	BB_1e: BasicBlock(start=11,end=11) -> {BB_27,BB_6}
	BB_1f: BasicBlock(start=43,end=44) -> {BB_27,BB_14}
	BB_20: BasicBlock(start=40,end=41) -> {BB_c}
	BB_21: BasicBlock(start=26,end=26) -> {BB_27,BB_16}
	BB_22: BasicBlock(start=23,end=23) -> {BB_f,BB_b}
	BB_23: BasicBlock(start=36,end=36) -> {BB_c}
	BB_24: BasicBlock(start=30,end=31) -> {BB_27,BB_13}
	BB_25: BasicBlock(start=19,end=20) -> {BB_27,BB_11}
	BB_26: BasicBlock(start=4,end=5) -> {BB_27,BB_3}
	BB_27: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=1,end=2) -> {BB_27,BB_19}
	BB_3: BasicBlock(start=6,end=6) -> {BB_17,BB_15}
	BB_4: BasicBlock(start=9,end=9) -> {BB_27,BB_1}
	BB_5: BasicBlock(start=13,end=14) -> {BB_8}
	BB_6: BasicBlock(start=12,end=12) -> {BB_27,BB_5}
	BB_7: BasicBlock(start=16,end=17) -> {BB_27,BB_1c}
	BB_8: BasicBlock(start=8,end=8) -> {BB_9,BB_4}
	BB_9: BasicBlock(start=15,end=15) -> {BB_7,BB_25}
	BB_a: BasicBlock(start=42,end=42) -> {BB_e,BB_1f}
	BB_b: BasicBlock(start=24,end=24) -> {BB_27,BB_d}
	BB_c: BasicBlock(start=37,end=37) -> {BB_10,BB_a}
	BB_d: BasicBlock(start=25,end=25) -> {BB_27,BB_21}
	BB_e: BasicBlock(start=46,end=47) -> {BB_27,BB_1b}
	BB_f: BasicBlock(start=29,end=29) -> {BB_12,BB_24}
))

void <init>(java.lang.String,int)
AITACode(params=(Parameters(
	0: useSites={0,32,16,24,20,44,14,46,25,29,35,27,39,23,15,31} (origin=-1),
	1: useSites={14} (origin=-2),
	2: useSites={2,9,15} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value=int = -512,origin=1),IntConst(pc=5,-512)),
	2: Assignment(pc=8,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=8,ComputationalTypeInt,UVar(defSites={-3},value=an int),&,UVar(defSites={1},value=int = -512))),
	3: If(pc=9,UVar(defSites={2},value=an int),==,IntConst(pc=-333,0),target=14),
	4: Assignment(pc=12,DVar(useSites={12,13},value=java.lang.IllegalArgumentException[↦12;refId=105],origin=4),New(pc=12,java.lang.IllegalArgumentException)),
	5: Assignment(pc=16,DVar(useSites={8,6},value=java.lang.StringBuilder[↦16;refId=106],origin=5),New(pc=16,java.lang.StringBuilder)),
	6: NonVirtualMethodCall(pc=20,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={5},value=java.lang.StringBuilder[↦16;refId=106]),()),
	7: Assignment(pc=23,DVar(useSites={8},value=String("Unknown flag 0x")[@23;refId=108],origin=7),StringConst(pc=23,Unknown flag 0x)),
	8: Assignment(pc=25,DVar(useSites={10},value={java.lang.StringBuilder, null}[↦25;refId=110],origin=8),VirtualFunctionCall(pc=25,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={5},value=java.lang.StringBuilder[↦16;refId=106]),(UVar(defSites={7},value=String("Unknown flag 0x")[@23;refId=108])))),
	9: Assignment(pc=29,DVar(useSites={10},value={java.lang.String, null}[↦29;refId=112],origin=9),StaticFunctionCall(pc=29,java.lang.Integer,isInterface=false,java.lang.String toHexString(int),(UVar(defSites={-3},value=an int)))),
	10: Assignment(pc=32,DVar(useSites={11},value={java.lang.StringBuilder, null}[↦32;refId=115],origin=10),VirtualFunctionCall(pc=32,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={8},value={java.lang.StringBuilder, null}[↦25;refId=110]),(UVar(defSites={9},value={java.lang.String, null}[↦29;refId=112])))),
	11: Assignment(pc=35,DVar(useSites={12},value={java.lang.String, null}[↦35;refId=118],origin=11),VirtualFunctionCall(pc=35,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={10},value={java.lang.StringBuilder, null}[↦32;refId=115]),())),
	12: NonVirtualMethodCall(pc=38,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={4},value=java.lang.IllegalArgumentException[↦12;refId=105]),(UVar(defSites={11},value={java.lang.String, null}[↦35;refId=118]))),
	13: Throw(pc=41,UVar(defSites={4},value=java.lang.IllegalArgumentException[↦12;refId=105])),
	14: PutField(pc=44,java.util.regex.Pattern,pattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={-2},value={java.lang.String, null}[↦-2;refId=103])),
	15: PutField(pc=49,java.util.regex.Pattern,flags,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={-3},value=an int)),
	16: Assignment(pc=53,DVar(useSites={18},value=an int,origin=16),GetField(pc=53,java.util.regex.Pattern,flags,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	17: Assignment(pc=56,DVar(useSites={18},value=int = 256,origin=17),IntConst(pc=56,256)),
	18: Assignment(pc=59,DVar(useSites={19},value=int ∈ [0,256],origin=18),BinaryExpr(pc=59,ComputationalTypeInt,UVar(defSites={16},value=an int),&,UVar(defSites={17},value=int = 256))),
	19: If(pc=60,UVar(defSites={18},value=int ∈ [0,256]),==,IntConst(pc=-333,0),target=24),
	20: Assignment(pc=65,DVar(useSites={22},value=an int,origin=20),GetField(pc=65,java.util.regex.Pattern,flags,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	21: Assignment(pc=68,DVar(useSites={22},value=int = 64,origin=21),IntConst(pc=68,64)),
	22: Assignment(pc=70,DVar(useSites={23},value=an int,origin=22),BinaryExpr(pc=70,ComputationalTypeInt,UVar(defSites={20},value=an int),|,UVar(defSites={21},value=int = 64))),
	23: PutField(pc=71,java.util.regex.Pattern,flags,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={22},value=an int)),
	24: Assignment(pc=76,DVar(useSites={25},value=an int,origin=24),GetField(pc=76,java.util.regex.Pattern,flags,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	25: PutField(pc=79,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={24},value=an int)),
	26: Assignment(pc=83,DVar(useSites={27},value=int = 1,origin=26),IntConst(pc=83,1)),
	27: PutField(pc=84,java.util.regex.Pattern,capturingGroupCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={26},value=int = 1)),
	28: Assignment(pc=88,DVar(useSites={29},value=int = 0,origin=28),IntConst(pc=88,0)),
	29: PutField(pc=89,java.util.regex.Pattern,localCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={28},value=int = 0)),
	30: Assignment(pc=93,DVar(useSites={31},value=int = 0,origin=30),IntConst(pc=93,0)),
	31: PutField(pc=94,java.util.regex.Pattern,localTCNCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={30},value=int = 0)),
	32: Assignment(pc=98,DVar(useSites={33},value={java.lang.String, null}[↦98;refId=120],origin=32),GetField(pc=98,java.util.regex.Pattern,pattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	33: Assignment(pc=101,DVar(useSites={34},value=int ∈ [0,1],origin=33),VirtualFunctionCall(pc=101,java.lang.String,isInterface=false,boolean isEmpty(),UVar(defSites={32},value={java.lang.String, null}[↦98;refId=120]),())),
	34: If(pc=104,UVar(defSites={33},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=41),
	35: VirtualMethodCall(pc=108,java.util.regex.Pattern,isInterface=false,void compile(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	36: Goto(pc=111,target=47),
	37: CaughtException(pc=114,java.lang.StackOverflowError,caused by={exception@35}),
	38: Assignment(pc=116,DVar(useSites={39},value=String("Stack overflow during pattern compilation")[@116;refId=125],origin=38),StringConst(pc=116,Stack overflow during pattern compilation)),
	39: Assignment(pc=118,DVar(useSites={40},value={_ <: java.util.regex.PatternSyntaxException, null}[↦118;refId=127],origin=39),VirtualFunctionCall(pc=118,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={38},value=String("Stack overflow during pattern compilation")[@116;refId=125])))),
	40: Throw(pc=121,UVar(defSites={39},value={_ <: java.util.regex.PatternSyntaxException, null}[↦118;refId=127])),
	41: Assignment(pc=123,DVar(useSites={44,43},value=java.util.regex.Pattern$Start[↦123;refId=129],origin=41),New(pc=123,java.util.regex.Pattern$Start)),
	42: Assignment(pc=127,DVar(useSites={43},value={_ <: java.util.regex.Pattern$Node, null}[↦127;refId=130],origin=42),GetStatic(pc=127,java.util.regex.Pattern,lastAccept,java.util.regex.Pattern$Node)),
	43: NonVirtualMethodCall(pc=130,java.util.regex.Pattern$Start,isInterface=false,void <init>(java.util.regex.Pattern$Node),UVar(defSites={41},value=java.util.regex.Pattern$Start[↦123;refId=129]),(UVar(defSites={42},value={_ <: java.util.regex.Pattern$Node, null}[↦127;refId=130]))),
	44: PutField(pc=133,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={41},value=java.util.regex.Pattern$Start[↦123;refId=129])),
	45: Assignment(pc=137,DVar(useSites={46},value={_ <: java.util.regex.Pattern$Node, null}[↦137;refId=132],origin=45),GetStatic(pc=137,java.util.regex.Pattern,lastAccept,java.util.regex.Pattern$Node)),
	46: PutField(pc=140,java.util.regex.Pattern,matchRoot,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={45},value={_ <: java.util.regex.Pattern$Node, null}[↦137;refId=132])),
	47: Return(pc=143)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_16,BB_3}
	BB_10: BasicBlock(start=37,end=39) -> {BB_16,BB_c}
	BB_11: BasicBlock(start=20,end=23) -> {BB_f}
	BB_12: CatchNode([35,36)=>37,java.lang.StackOverflowError) -> {BB_10}
	BB_13: BasicBlock(start=13,end=13) -> {BB_16}
	BB_14: BasicBlock(start=41,end=43) -> {BB_16,BB_6}
	BB_15: BasicBlock(start=4,end=6) -> {BB_16,BB_8}
	BB_16: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=10,end=10) -> {BB_16,BB_b}
	BB_2: BasicBlock(start=14,end=19) -> {BB_f,BB_11}
	BB_3: BasicBlock(start=1,end=3) -> {BB_15,BB_2}
	BB_4: BasicBlock(start=9,end=9) -> {BB_16,BB_1}
	BB_5: BasicBlock(start=34,end=34) -> {BB_14,BB_9}
	BB_6: BasicBlock(start=44,end=46) -> {BB_e}
	BB_7: BasicBlock(start=12,end=12) -> {BB_16,BB_13}
	BB_8: BasicBlock(start=7,end=8) -> {BB_16,BB_4}
	BB_9: BasicBlock(start=35,end=35) -> {BB_16,BB_d,BB_12}
	BB_a: ExitNode(normalReturn=true)
	BB_b: BasicBlock(start=11,end=11) -> {BB_16,BB_7}
	BB_c: BasicBlock(start=40,end=40) -> {BB_16}
	BB_d: BasicBlock(start=36,end=36) -> {BB_e}
	BB_e: BasicBlock(start=47,end=47) -> {BB_a}
	BB_f: BasicBlock(start=24,end=33) -> {BB_16,BB_5}
),exceptionHandlers=(
	ExceptionHandler([35, 36) -> 37, java.lang.StackOverflowError)
))

void subFlag()
AITACode(params=(Parameters(
	0: useSites={0,16,8,36,44,28,18,26,6,38,33,41,21,13,3,11,23,31} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Nop(pc=4),
	2: Switch(pc=6,defaultTarget=43,index=UVar(defSites={0,44},value=an int),npairs=(IntIntPair(85,38),IntIntPair(99,28),IntIntPair(100,18),IntIntPair(105,3),IntIntPair(109,8),IntIntPair(115,13),IntIntPair(117,23),IntIntPair(120,33)),
	3: Assignment(pc=82,DVar(useSites={5},value=an int,origin=3),GetField(pc=82,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	4: Assignment(pc=85,DVar(useSites={5},value=int = -3,origin=4),IntConst(pc=85,-3)),
	5: Assignment(pc=87,DVar(useSites={6},value=an int,origin=5),BinaryExpr(pc=87,ComputationalTypeInt,UVar(defSites={3},value=an int),&,UVar(defSites={4},value=int = -3))),
	6: PutField(pc=88,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={5},value=an int)),
	7: Goto(pc=91,target=44),
	8: Assignment(pc=96,DVar(useSites={10},value=an int,origin=8),GetField(pc=96,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	9: Assignment(pc=99,DVar(useSites={10},value=int = -9,origin=9),IntConst(pc=99,-9)),
	10: Assignment(pc=101,DVar(useSites={11},value=an int,origin=10),BinaryExpr(pc=101,ComputationalTypeInt,UVar(defSites={8},value=an int),&,UVar(defSites={9},value=int = -9))),
	11: PutField(pc=102,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={10},value=an int)),
	12: Goto(pc=105,target=44),
	13: Assignment(pc=110,DVar(useSites={15},value=an int,origin=13),GetField(pc=110,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	14: Assignment(pc=113,DVar(useSites={15},value=int = -33,origin=14),IntConst(pc=113,-33)),
	15: Assignment(pc=115,DVar(useSites={16},value=an int,origin=15),BinaryExpr(pc=115,ComputationalTypeInt,UVar(defSites={13},value=an int),&,UVar(defSites={14},value=int = -33))),
	16: PutField(pc=116,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={15},value=an int)),
	17: Goto(pc=119,target=44),
	18: Assignment(pc=124,DVar(useSites={20},value=an int,origin=18),GetField(pc=124,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	19: Assignment(pc=127,DVar(useSites={20},value=int = -2,origin=19),IntConst(pc=127,-2)),
	20: Assignment(pc=129,DVar(useSites={21},value=an int,origin=20),BinaryExpr(pc=129,ComputationalTypeInt,UVar(defSites={18},value=an int),&,UVar(defSites={19},value=int = -2))),
	21: PutField(pc=130,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={20},value=an int)),
	22: Goto(pc=133,target=44),
	23: Assignment(pc=138,DVar(useSites={25},value=an int,origin=23),GetField(pc=138,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	24: Assignment(pc=141,DVar(useSites={25},value=int = -65,origin=24),IntConst(pc=141,-65)),
	25: Assignment(pc=143,DVar(useSites={26},value=an int,origin=25),BinaryExpr(pc=143,ComputationalTypeInt,UVar(defSites={23},value=an int),&,UVar(defSites={24},value=int = -65))),
	26: PutField(pc=144,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={25},value=an int)),
	27: Goto(pc=147,target=44),
	28: Assignment(pc=152,DVar(useSites={30},value=an int,origin=28),GetField(pc=152,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	29: Assignment(pc=155,DVar(useSites={30},value=int = -129,origin=29),IntConst(pc=155,-129)),
	30: Assignment(pc=158,DVar(useSites={31},value=an int,origin=30),BinaryExpr(pc=158,ComputationalTypeInt,UVar(defSites={28},value=an int),&,UVar(defSites={29},value=int = -129))),
	31: PutField(pc=159,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={30},value=an int)),
	32: Goto(pc=162,target=44),
	33: Assignment(pc=167,DVar(useSites={35},value=an int,origin=33),GetField(pc=167,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	34: Assignment(pc=170,DVar(useSites={35},value=int = -5,origin=34),IntConst(pc=170,-5)),
	35: Assignment(pc=172,DVar(useSites={36},value=an int,origin=35),BinaryExpr(pc=172,ComputationalTypeInt,UVar(defSites={33},value=an int),&,UVar(defSites={34},value=int = -5))),
	36: PutField(pc=173,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={35},value=an int)),
	37: Goto(pc=176,target=44),
	38: Assignment(pc=181,DVar(useSites={40},value=an int,origin=38),GetField(pc=181,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	39: Assignment(pc=184,DVar(useSites={40},value=int = -321,origin=39),IntConst(pc=184,-321)),
	40: Assignment(pc=187,DVar(useSites={41},value=an int,origin=40),BinaryExpr(pc=187,ComputationalTypeInt,UVar(defSites={38},value=an int),&,UVar(defSites={39},value=int = -321))),
	41: PutField(pc=188,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={40},value=an int)),
	42: Goto(pc=191,target=44),
	43: Return(pc=194),
	44: Assignment(pc=196,DVar(useSites={2},value=an int,origin=44),VirtualFunctionCall(pc=196,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	45: Goto(pc=200,target=2)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_a,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_3}
	BB_2: BasicBlock(start=13,end=17) -> {BB_5}
	BB_3: BasicBlock(start=2,end=2) -> {BB_e,BB_7,BB_2,BB_6,BB_9,BB_c,BB_b,BB_d,BB_8}
	BB_4: BasicBlock(start=45,end=45) -> {BB_3}
	BB_5: BasicBlock(start=44,end=44) -> {BB_a,BB_4}
	BB_6: BasicBlock(start=3,end=7) -> {BB_5}
	BB_7: BasicBlock(start=43,end=43) -> {BB_f}
	BB_8: BasicBlock(start=23,end=27) -> {BB_5}
	BB_9: BasicBlock(start=8,end=12) -> {BB_5}
	BB_a: ExitNode(normalReturn=false)
	BB_b: BasicBlock(start=33,end=37) -> {BB_5}
	BB_c: BasicBlock(start=28,end=32) -> {BB_5}
	BB_d: BasicBlock(start=38,end=42) -> {BB_5}
	BB_e: BasicBlock(start=18,end=22) -> {BB_5}
	BB_f: ExitNode(normalReturn=true)
))

boolean lambda$clazz$1(java.util.regex.Pattern$BitClass,int)
AITACode(params=(Parameters(
	1: useSites={2} (origin=-2),
	2: useSites={1,3} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 256,origin=0),IntConst(pc=1,256)),
	1: If(pc=4,UVar(defSites={-3},value=an int),>=,UVar(defSites={0},value=int = 256),target=7),
	2: Assignment(pc=8,DVar(useSites={3},value={boolean[], null}[↦8;refId=103],origin=2),GetField(pc=8,java.util.regex.Pattern$BitClass,bits,boolean[],UVar(defSites={-2},value={java.util.regex.Pattern$BitClass, null}[↦-1;refId=102]))),
	3: Assignment(pc=12,DVar(useSites={4},value=int ∈ [0,1],origin=3),ArrayLoad(pc=12,UVar(defSites={-3},value=int ∈ [-2147483648,255]),UVar(defSites={2},value={boolean[], null}[↦8;refId=103]))),
	4: If(pc=13,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=7),
	5: Assignment(pc=16,DVar(useSites={8},value=int = 1,origin=5),IntConst(pc=16,1)),
	6: Goto(pc=17,target=8),
	7: Assignment(pc=20,DVar(useSites={8},value=int ∈ [0,1],origin=7),IntConst(pc=20,0)),
	8: ReturnValue(pc=21,UVar(defSites={5,7},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_2}
	BB_1: BasicBlock(start=5,end=6) -> {BB_6}
	BB_2: BasicBlock(start=2,end=2) -> {BB_8,BB_4}
	BB_3: BasicBlock(start=7,end=7) -> {BB_6}
	BB_4: BasicBlock(start=3,end=3) -> {BB_8,BB_7}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=8,end=8) -> {BB_5}
	BB_7: BasicBlock(start=4,end=4) -> {BB_1,BB_3}
	BB_8: ExitNode(normalReturn=false)
))

boolean isSupplementary(int)
AITACode(params=(Parameters(
	1: useSites={2,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 65536,origin=0),IntConst(pc=1,65536)),
	1: If(pc=3,UVar(defSites={-2},value=an int),>=,UVar(defSites={0},value=int = 65536),target=5),
	2: Assignment(pc=7,DVar(useSites={3},value=int ∈ [0,65535],origin=2),PrimitiveTypecastExpr(pc=7,CharType,UVar(defSites={-2},value=int ∈ [-2147483648,65535]))),
	3: Assignment(pc=8,DVar(useSites={4},value=int ∈ [0,1],origin=3),StaticFunctionCall(pc=8,java.lang.Character,isInterface=false,boolean isSurrogate(char),(UVar(defSites={2},value=int ∈ [0,65535])))),
	4: If(pc=11,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=7),
	5: Assignment(pc=14,DVar(useSites={8},value=int = 1,origin=5),IntConst(pc=14,1)),
	6: Goto(pc=15,target=8),
	7: Assignment(pc=18,DVar(useSites={8},value=int ∈ [0,1],origin=7),IntConst(pc=18,0)),
	8: ReturnValue(pc=19,UVar(defSites={5,7},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_2,BB_1}
	BB_1: BasicBlock(start=5,end=6) -> {BB_5}
	BB_2: BasicBlock(start=2,end=3) -> {BB_7,BB_6}
	BB_3: BasicBlock(start=7,end=7) -> {BB_5}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=8,end=8) -> {BB_4}
	BB_6: BasicBlock(start=4,end=4) -> {BB_3,BB_1}
	BB_7: ExitNode(normalReturn=false)
))

int parsePastLine()
AITACode(params=(Parameters(
	0: useSites={0,8,24,4,18,10,22,14,1,21,19,11,27,23} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={5},value={int[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={5,3},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=10,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=10,1)),
	3: Assignment(pc=11,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=11,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={2},value=int = 1))),
	4: PutField(pc=12,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=15,DVar(useSites={8,30,17,7},value=an int,origin=5),ArrayLoad(pc=15,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=103]))),
	6: Nop(pc=16),
	7: If(pc=18,UVar(defSites={5,15},value=an int),==,IntConst(pc=-333,0),target=17),
	8: Assignment(pc=23,DVar(useSites={9},value=int ∈ [0,1],origin=8),VirtualFunctionCall(pc=23,java.util.regex.Pattern,isInterface=false,boolean isLineSeparator(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={5,15},value=an int)))),
	9: If(pc=26,UVar(defSites={8},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=17),
	10: Assignment(pc=30,DVar(useSites={15},value={int[], null}[↦30;refId=107],origin=10),GetField(pc=30,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	11: Assignment(pc=35,DVar(useSites={13,15},value=an int,origin=11),GetField(pc=35,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	12: Assignment(pc=39,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=39,1)),
	13: Assignment(pc=40,DVar(useSites={14},value=an int,origin=13),BinaryExpr(pc=40,ComputationalTypeInt,UVar(defSites={11},value=an int),+,UVar(defSites={12},value=int = 1))),
	14: PutField(pc=41,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={13},value=an int)),
	15: Assignment(pc=44,DVar(useSites={8,30,17,7},value=an int,origin=15),ArrayLoad(pc=44,UVar(defSites={11},value=an int),UVar(defSites={10},value={int[], null}[↦30;refId=107]))),
	16: Goto(pc=46,target=7),
	17: If(pc=50,UVar(defSites={5,15},value=an int),!=,IntConst(pc=-333,0),target=30),
	18: Assignment(pc=54,DVar(useSites={20},value=an int,origin=18),GetField(pc=54,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	19: Assignment(pc=58,DVar(useSites={20},value=an int,origin=19),GetField(pc=58,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	20: If(pc=61,UVar(defSites={18},value=an int),<=,UVar(defSites={19},value=an int),target=30),
	21: Assignment(pc=66,DVar(useSites={22},value=an int,origin=21),GetField(pc=66,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	22: PutField(pc=69,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={21},value=an int)),
	23: Assignment(pc=73,DVar(useSites={28},value={int[], null}[↦73;refId=110],origin=23),GetField(pc=73,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	24: Assignment(pc=78,DVar(useSites={28,26},value=an int,origin=24),GetField(pc=78,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	25: Assignment(pc=82,DVar(useSites={26},value=int = 1,origin=25),IntConst(pc=82,1)),
	26: Assignment(pc=83,DVar(useSites={27},value=an int,origin=26),BinaryExpr(pc=83,ComputationalTypeInt,UVar(defSites={24},value=an int),+,UVar(defSites={25},value=int = 1))),
	27: PutField(pc=84,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={26},value=an int)),
	28: Assignment(pc=87,DVar(useSites={30},value=an int,origin=28),ArrayLoad(pc=87,UVar(defSites={24},value=an int),UVar(defSites={23},value={int[], null}[↦73;refId=110]))),
	29: Nop(pc=88),
	30: ReturnValue(pc=90,UVar(defSites={28,5,15},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_b,BB_3}
	BB_1: BasicBlock(start=10,end=15) -> {BB_b,BB_8}
	BB_2: BasicBlock(start=29,end=29) -> {BB_a}
	BB_3: BasicBlock(start=6,end=6) -> {BB_7}
	BB_4: BasicBlock(start=21,end=28) -> {BB_b,BB_2}
	BB_5: BasicBlock(start=9,end=9) -> {BB_6,BB_1}
	BB_6: BasicBlock(start=17,end=17) -> {BB_a,BB_c}
	BB_7: BasicBlock(start=7,end=7) -> {BB_6,BB_9}
	BB_8: BasicBlock(start=16,end=16) -> {BB_7}
	BB_9: BasicBlock(start=8,end=8) -> {BB_b,BB_5}
	BB_a: BasicBlock(start=30,end=30) -> {BB_d}
	BB_b: ExitNode(normalReturn=false)
	BB_c: BasicBlock(start=18,end=20) -> {BB_4,BB_a}
	BB_d: ExitNode(normalReturn=true)
))

void accept(int,java.lang.String)
AITACode(params=(Parameters(
	0: useSites={0,4,12,1,9,7} (origin=-1),
	1: useSites={11} (origin=-2),
	2: useSites={12} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={5},value={int[], null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={5,3},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=10,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=10,1)),
	3: Assignment(pc=11,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=11,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={2},value=int = 1))),
	4: PutField(pc=12,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=15,DVar(useSites={9,11},value=an int,origin=5),ArrayLoad(pc=15,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=104]))),
	6: Assignment(pc=18,DVar(useSites={7},value=int = 4,origin=6),IntConst(pc=18,4)),
	7: Assignment(pc=19,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=19,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={6},value=int = 4)))),
	8: If(pc=22,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	9: Assignment(pc=27,DVar(useSites={11},value=an int,origin=9),VirtualFunctionCall(pc=27,java.util.regex.Pattern,isInterface=false,int parsePastWhitespace(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={5},value=an int)))),
	10: Nop(pc=30),
	11: If(pc=33,UVar(defSites={-2},value=an int),==,UVar(defSites={9,5},value=an int),target=14),
	12: Assignment(pc=38,DVar(useSites={13},value={_ <: java.util.regex.PatternSyntaxException, null}[↦38;refId=110],origin=12),VirtualFunctionCall(pc=38,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={-3},value={java.lang.String, null}[↦-3;refId=103])))),
	13: Throw(pc=41,UVar(defSites={12},value={_ <: java.util.regex.PatternSyntaxException, null}[↦38;refId=110])),
	14: Return(pc=42)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_a,BB_3}
	BB_1: BasicBlock(start=10,end=10) -> {BB_8}
	BB_2: BasicBlock(start=14,end=14) -> {BB_7}
	BB_3: BasicBlock(start=6,end=7) -> {BB_a,BB_9}
	BB_4: BasicBlock(start=9,end=9) -> {BB_a,BB_1}
	BB_5: BasicBlock(start=13,end=13) -> {BB_a}
	BB_6: BasicBlock(start=12,end=12) -> {BB_a,BB_5}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=11,end=11) -> {BB_6,BB_2}
	BB_9: BasicBlock(start=8,end=8) -> {BB_4,BB_8}
	BB_a: ExitNode(normalReturn=false)
))

int getClass(int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),StaticFunctionCall(pc=1,sun.text.Normalizer,isInterface=false,int getCombiningClass(int),(UVar(defSites={-2},value=an int)))),
	1: ReturnValue(pc=4,UVar(defSites={0},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean has(int)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),BinaryExpr(pc=5,ComputationalTypeInt,UVar(defSites={0},value=an int),&,UVar(defSites={-2},value=an int))),
	2: If(pc=6,UVar(defSites={1},value=an int),==,IntConst(pc=-333,0),target=5),
	3: Assignment(pc=9,DVar(useSites={6},value=int = 1,origin=3),IntConst(pc=9,1)),
	4: Goto(pc=10,target=6),
	5: Assignment(pc=13,DVar(useSites={6},value=int ∈ [0,1],origin=5),IntConst(pc=13,0)),
	6: ReturnValue(pc=14,UVar(defSites={5,3},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=5,end=5) -> {BB_2}
	BB_2: BasicBlock(start=6,end=6) -> {BB_4}
	BB_3: BasicBlock(start=3,end=4) -> {BB_2}
	BB_4: ExitNode(normalReturn=true)
	BB_5: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate UNIXDOT()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value={_ <: java.util.regex.Pattern$UNIXDOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda, null}[↦0;refId=103],origin=0),StaticFunctionCall(pc=0,java.util.regex.Pattern$UNIXDOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda,isInterface=false,java.util.regex.Pattern$UNIXDOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda $newInstance(),())),
	1: ReturnValue(pc=5,UVar(defSites={0},value={_ <: java.util.regex.Pattern$UNIXDOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda, null}[↦0;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate family(boolean,boolean)
AITACode(params=(Parameters(
	0: useSites={0,40,4,12,108,28,130,146,26,22,150,17,37,21,13,3,19,27,31} (origin=-1),
	1: useSites={2} (origin=-2),
	2: useSites={148} (origin=-3)
)),stmts=(
	0: ExprStmt(pc=1,VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Assignment(pc=5,DVar(useSites={96,134,137,153,151},value=null[↦5],origin=1),NullExpr(pc=5)),
	2: If(pc=9,UVar(defSites={-2},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=19),
	3: Assignment(pc=13,DVar(useSites={5},value={int[], null}[↦13;refId=104],origin=3),GetField(pc=13,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	4: Assignment(pc=17,DVar(useSites={5},value=an int,origin=4),GetField(pc=17,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	5: Assignment(pc=20,DVar(useSites={8,6},value=an int,origin=5),ArrayLoad(pc=20,UVar(defSites={4},value=an int),UVar(defSites={3},value={int[], null}[↦13;refId=104]))),
	6: Assignment(pc=25,DVar(useSites={7},value=int ∈ [0,1],origin=6),StaticFunctionCall(pc=25,java.lang.Character,isInterface=false,boolean isSupplementaryCodePoint(int),(UVar(defSites={5},value=an int)))),
	7: If(pc=28,UVar(defSites={6},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=11),
	8: Assignment(pc=33,DVar(useSites={9},value=int ∈ [0,65535],origin=8),PrimitiveTypecastExpr(pc=33,CharType,UVar(defSites={5},value=an int))),
	9: Assignment(pc=34,DVar(useSites={132,52,114,54,118,142,121,135,47,111},value={java.lang.String, null}[↦34;refId=109],origin=9),StaticFunctionCall(pc=34,java.lang.String,isInterface=false,java.lang.String valueOf(char),(UVar(defSites={8},value=int ∈ [0,65535])))),
	10: Goto(pc=38,target=17),
	11: Assignment(pc=41,DVar(useSites={132,52,114,54,118,142,121,135,15,47,111},value=String(<initialization incomplete>)[@41;refId=110],origin=11),New(pc=41,java.lang.String)),
	12: Assignment(pc=46,DVar(useSites={15},value={int[], null}[↦46;refId=111],origin=12),GetField(pc=46,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	13: Assignment(pc=50,DVar(useSites={15},value=an int,origin=13),GetField(pc=50,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	14: Assignment(pc=53,DVar(useSites={15},value=int = 1,origin=14),IntConst(pc=53,1)),
	15: NonVirtualMethodCall(pc=54,java.lang.String,isInterface=false,void <init>(int[],int,int),UVar(defSites={11},value=String(<initialization incomplete>)[@41;refId=110]),(UVar(defSites={12},value={int[], null}[↦46;refId=111]),UVar(defSites={13},value=an int),UVar(defSites={14},value=int = 1))),
	16: Nop(pc=57),
	17: ExprStmt(pc=59,VirtualFunctionCall(pc=59,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	18: Goto(pc=63,target=46),
	19: Assignment(pc=67,DVar(useSites={44,34,41},value=an int,origin=19),GetField(pc=67,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	20: Assignment(pc=73,DVar(useSites={21},value=int = 125,origin=20),IntConst(pc=73,125)),
	21: VirtualMethodCall(pc=75,java.util.regex.Pattern,isInterface=false,void mark(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={20},value=int = 125))),
	22: Assignment(pc=79,DVar(useSites={24},value=an int,origin=22),VirtualFunctionCall(pc=79,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	23: Assignment(pc=82,DVar(useSites={24},value=int = 125,origin=23),IntConst(pc=82,125)),
	24: If(pc=84,UVar(defSites={22},value=an int),!=,UVar(defSites={23},value=int = 125),target=22),
	25: Assignment(pc=91,DVar(useSites={26},value=int = 0,origin=25),IntConst(pc=91,0)),
	26: VirtualMethodCall(pc=92,java.util.regex.Pattern,isInterface=false,void mark(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={25},value=int = 0))),
	27: Assignment(pc=96,DVar(useSites={41,29,35},value=an int,origin=27),GetField(pc=96,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	28: Assignment(pc=104,DVar(useSites={29},value=an int,origin=28),GetField(pc=104,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	29: If(pc=107,UVar(defSites={27},value=an int),<=,UVar(defSites={28},value=an int),target=33),
	30: Assignment(pc=111,DVar(useSites={31},value=String("Unclosed character family")[@111;refId=126],origin=30),StringConst(pc=111,Unclosed character family)),
	31: Assignment(pc=114,DVar(useSites={32},value={_ <: java.util.regex.PatternSyntaxException, null}[↦114;refId=128],origin=31),VirtualFunctionCall(pc=114,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={30},value=String("Unclosed character family")[@111;refId=126])))),
	32: Throw(pc=117,UVar(defSites={31},value={_ <: java.util.regex.PatternSyntaxException, null}[↦114;refId=128])),
	33: Assignment(pc=120,DVar(useSites={34},value=int = 1,origin=33),IntConst(pc=120,1)),
	34: Assignment(pc=121,DVar(useSites={35},value=an int,origin=34),BinaryExpr(pc=121,ComputationalTypeInt,UVar(defSites={19},value=an int),+,UVar(defSites={33},value=int = 1))),
	35: If(pc=124,UVar(defSites={34},value=an int),<,UVar(defSites={27},value=an int),target=39),
	36: Assignment(pc=128,DVar(useSites={37},value=String("Empty character family")[@128;refId=122],origin=36),StringConst(pc=128,Empty character family)),
	37: Assignment(pc=131,DVar(useSites={38},value={_ <: java.util.regex.PatternSyntaxException, null}[↦131;refId=124],origin=37),VirtualFunctionCall(pc=131,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={36},value=String("Empty character family")[@128;refId=122])))),
	38: Throw(pc=134,UVar(defSites={37},value={_ <: java.util.regex.PatternSyntaxException, null}[↦131;refId=124])),
	39: Assignment(pc=135,DVar(useSites={132,52,44,114,54,118,142,121,135,47,111},value=String(<initialization incomplete>)[@135;refId=118],origin=39),New(pc=135,java.lang.String)),
	40: Assignment(pc=140,DVar(useSites={44},value={int[], null}[↦140;refId=119],origin=40),GetField(pc=140,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	41: Assignment(pc=149,DVar(useSites={43},value=an int,origin=41),BinaryExpr(pc=149,ComputationalTypeInt,UVar(defSites={27},value=int ∈ [-2147483647,2147483647]),-,UVar(defSites={19},value=an int))),
	42: Assignment(pc=150,DVar(useSites={43},value=int = 1,origin=42),IntConst(pc=150,1)),
	43: Assignment(pc=151,DVar(useSites={44},value=an int,origin=43),BinaryExpr(pc=151,ComputationalTypeInt,UVar(defSites={41},value=an int),-,UVar(defSites={42},value=int = 1))),
	44: NonVirtualMethodCall(pc=152,java.lang.String,isInterface=false,void <init>(int[],int,int),UVar(defSites={39},value=String(<initialization incomplete>)[@135;refId=118]),(UVar(defSites={40},value={int[], null}[↦140;refId=119]),UVar(defSites={19},value=an int),UVar(defSites={43},value=an int))),
	45: Nop(pc=155),
	46: Assignment(pc=157,DVar(useSites={47},value=int = 61,origin=46),IntConst(pc=157,61)),
	47: Assignment(pc=159,DVar(useSites={54,49,51},value=an int,origin=47),VirtualFunctionCall(pc=159,java.lang.String,isInterface=false,int indexOf(int),UVar(defSites={9,11,39},value={java.lang.String, null}[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»]),(UVar(defSites={46},value=int = 61)))),
	48: Assignment(pc=166,DVar(useSites={49},value=int = -1,origin=48),IntConst(pc=166,-1)),
	49: If(pc=167,UVar(defSites={47},value=an int),==,UVar(defSites={48},value=int = -1),target=110),
	50: Assignment(pc=173,DVar(useSites={51},value=int = 1,origin=50),IntConst(pc=173,1)),
	51: Assignment(pc=174,DVar(useSites={52},value=an int,origin=51),BinaryExpr(pc=174,ComputationalTypeInt,UVar(defSites={47},value=an int),+,UVar(defSites={50},value=int = 1))),
	52: Assignment(pc=175,DVar(useSites={104,92,90,94},value={java.lang.String, null}[↦175;refId=152],origin=52),VirtualFunctionCall(pc=175,java.lang.String,isInterface=false,java.lang.String substring(int),UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»]),(UVar(defSites={51},value=an int)))),
	53: Assignment(pc=181,DVar(useSites={54},value=int = 0,origin=53),IntConst(pc=181,0)),
	54: Assignment(pc=184,DVar(useSites={56},value={java.lang.String, null}[↦184;refId=154],origin=54),VirtualFunctionCall(pc=184,java.lang.String,isInterface=false,java.lang.String substring(int,int),UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»]),(UVar(defSites={53},value=int = 0),UVar(defSites={47},value=an int)))),
	55: Assignment(pc=187,DVar(useSites={56},value={java.util.Locale, null}[↦187;refId=155],origin=55),GetStatic(pc=187,java.util.Locale,ENGLISH,java.util.Locale)),
	56: Assignment(pc=190,DVar(useSites={76,66,58,86,81,101,61,71},value={java.lang.String, null}[↦190;refId=158],origin=56),VirtualFunctionCall(pc=190,java.lang.String,isInterface=false,java.lang.String toLowerCase(java.util.Locale),UVar(defSites={54},value={java.lang.String, null}[↦184;refId=154]),(UVar(defSites={55},value={java.util.Locale, null}[↦187;refId=155])))),
	57: Assignment(pc=197,DVar(useSites={89},value=int = -1,origin=57),IntConst(pc=197,-1)),
	58: Assignment(pc=202,DVar(useSites={59},value=an int,origin=58),VirtualFunctionCall(pc=202,java.lang.String,isInterface=false,int hashCode(),UVar(defSites={56},value={java.lang.String, null}[↦190;refId=158]),())),
	59: Switch(pc=205,defaultTarget=89,index=UVar(defSites={58},value=an int),npairs=(IntIntPair(-907685685,65),IntIntPair(3292,80),IntIntPair(3664,60),IntIntPair(97633,70),IntIntPair(93832333,75),IntIntPair(1265003125,85)),
	60: Assignment(pc=266,DVar(useSites={61},value=String("sc")[@266;refId=167],origin=60),StringConst(pc=266,sc)),
	61: Assignment(pc=269,DVar(useSites={62},value=int ∈ [0,1],origin=61),VirtualFunctionCall(pc=269,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={56},value=java.lang.String[↦190;refId=158]),(UVar(defSites={60},value=String("sc")[@266;refId=167])))),
	62: If(pc=272,UVar(defSites={61},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=89),
	63: Assignment(pc=275,DVar(useSites={89},value=int = 0,origin=63),IntConst(pc=275,0)),
	64: Goto(pc=278,target=89),
	65: Assignment(pc=283,DVar(useSites={66},value=String("script")[@283;refId=171],origin=65),StringConst(pc=283,script)),
	66: Assignment(pc=286,DVar(useSites={67},value=int ∈ [0,1],origin=66),VirtualFunctionCall(pc=286,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={56},value=java.lang.String[↦190;refId=158]),(UVar(defSites={65},value=String("script")[@283;refId=171])))),
	67: If(pc=289,UVar(defSites={66},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=89),
	68: Assignment(pc=292,DVar(useSites={89},value=int = 1,origin=68),IntConst(pc=292,1)),
	69: Goto(pc=295,target=89),
	70: Assignment(pc=300,DVar(useSites={71},value=String("blk")[@300;refId=165],origin=70),StringConst(pc=300,blk)),
	71: Assignment(pc=303,DVar(useSites={72},value=int ∈ [0,1],origin=71),VirtualFunctionCall(pc=303,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={56},value=java.lang.String[↦190;refId=158]),(UVar(defSites={70},value=String("blk")[@300;refId=165])))),
	72: If(pc=306,UVar(defSites={71},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=89),
	73: Assignment(pc=309,DVar(useSites={89},value=int = 2,origin=73),IntConst(pc=309,2)),
	74: Goto(pc=312,target=89),
	75: Assignment(pc=317,DVar(useSites={76},value=String("block")[@317;refId=163],origin=75),StringConst(pc=317,block)),
	76: Assignment(pc=320,DVar(useSites={77},value=int ∈ [0,1],origin=76),VirtualFunctionCall(pc=320,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={56},value=java.lang.String[↦190;refId=158]),(UVar(defSites={75},value=String("block")[@317;refId=163])))),
	77: If(pc=323,UVar(defSites={76},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=89),
	78: Assignment(pc=326,DVar(useSites={89},value=int = 3,origin=78),IntConst(pc=326,3)),
	79: Goto(pc=329,target=89),
	80: Assignment(pc=334,DVar(useSites={81},value=String("gc")[@334;refId=169],origin=80),StringConst(pc=334,gc)),
	81: Assignment(pc=337,DVar(useSites={82},value=int ∈ [0,1],origin=81),VirtualFunctionCall(pc=337,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={56},value=java.lang.String[↦190;refId=158]),(UVar(defSites={80},value=String("gc")[@334;refId=169])))),
	82: If(pc=340,UVar(defSites={81},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=89),
	83: Assignment(pc=343,DVar(useSites={89},value=int = 4,origin=83),IntConst(pc=343,4)),
	84: Goto(pc=346,target=89),
	85: Assignment(pc=351,DVar(useSites={86},value=String("general_category")[@351;refId=161],origin=85),StringConst(pc=351,general_category)),
	86: Assignment(pc=354,DVar(useSites={87},value=int ∈ [0,1],origin=86),VirtualFunctionCall(pc=354,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={56},value=java.lang.String[↦190;refId=158]),(UVar(defSites={85},value=String("general_category")[@351;refId=161])))),
	87: If(pc=357,UVar(defSites={86},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=89),
	88: Assignment(pc=360,DVar(useSites={89},value=int = 5,origin=88),IntConst(pc=360,5)),
	89: Switch(pc=365,defaultTarget=96,index=UVar(defSites={88,68,78,73,57,83,63},value=int ∈ [-1,5]),npairs=(IntIntPair(0,90),IntIntPair(1,90),IntIntPair(2,92),IntIntPair(3,92),IntIntPair(4,94),IntIntPair(5,94)),
	90: Assignment(pc=406,DVar(useSites={96,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦406;refId=209],origin=90),StaticFunctionCall(pc=406,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forUnicodeScript(java.lang.String),(UVar(defSites={52},value={java.lang.String, null}[↦175;refId=152])))),
	91: Goto(pc=411,target=96),
	92: Assignment(pc=416,DVar(useSites={96,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦416;refId=206],origin=92),StaticFunctionCall(pc=416,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forUnicodeBlock(java.lang.String),(UVar(defSites={52},value={java.lang.String, null}[↦175;refId=152])))),
	93: Goto(pc=421,target=96),
	94: Assignment(pc=426,DVar(useSites={96,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦426;refId=203],origin=94),StaticFunctionCall(pc=426,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forProperty(java.lang.String),(UVar(defSites={52},value={java.lang.String, null}[↦175;refId=152])))),
	95: Nop(pc=429),
	96: If(pc=436,UVar(defSites={92,90,94,1},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=210; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦416;refId=206], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦426;refId=203], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦406;refId=209], null[↦5]»]),!=,NullExpr(pc=-333),target=148),
	97: Assignment(pc=440,DVar(useSites={100,98},value=java.lang.StringBuilder[↦440;refId=235],origin=97),New(pc=440,java.lang.StringBuilder)),
	98: NonVirtualMethodCall(pc=444,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={97},value=java.lang.StringBuilder[↦440;refId=235]),()),
	99: Assignment(pc=447,DVar(useSites={100},value=String("Unknown Unicode property {name=<")[@447;refId=237],origin=99),StringConst(pc=447,Unknown Unicode property {name=<)),
	100: Assignment(pc=450,DVar(useSites={101},value={java.lang.StringBuilder, null}[↦450;refId=239],origin=100),VirtualFunctionCall(pc=450,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={97},value=java.lang.StringBuilder[↦440;refId=235]),(UVar(defSites={99},value=String("Unknown Unicode property {name=<")[@447;refId=237])))),
	101: Assignment(pc=454,DVar(useSites={103},value={java.lang.StringBuilder, null}[↦454;refId=242],origin=101),VirtualFunctionCall(pc=454,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={100},value={java.lang.StringBuilder, null}[↦450;refId=239]),(UVar(defSites={56},value=java.lang.String[↦190;refId=158])))),
	102: Assignment(pc=457,DVar(useSites={103},value=String(">, value=<")[@457;refId=243],origin=102),StringConst(pc=457,>, value=<)),
	103: Assignment(pc=460,DVar(useSites={104},value={java.lang.StringBuilder, null}[↦460;refId=246],origin=103),VirtualFunctionCall(pc=460,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={101},value={java.lang.StringBuilder, null}[↦454;refId=242]),(UVar(defSites={102},value=String(">, value=<")[@457;refId=243])))),
	104: Assignment(pc=465,DVar(useSites={106},value={java.lang.StringBuilder, null}[↦465;refId=249],origin=104),VirtualFunctionCall(pc=465,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={103},value={java.lang.StringBuilder, null}[↦460;refId=246]),(UVar(defSites={52},value={java.lang.String, null}[↦175;refId=152])))),
	105: Assignment(pc=468,DVar(useSites={106},value=String(">}")[@468;refId=250],origin=105),StringConst(pc=468,>})),
	106: Assignment(pc=471,DVar(useSites={107},value={java.lang.StringBuilder, null}[↦471;refId=253],origin=106),VirtualFunctionCall(pc=471,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={104},value={java.lang.StringBuilder, null}[↦465;refId=249]),(UVar(defSites={105},value=String(">}")[@468;refId=250])))),
	107: Assignment(pc=474,DVar(useSites={108},value={java.lang.String, null}[↦474;refId=256],origin=107),VirtualFunctionCall(pc=474,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={106},value={java.lang.StringBuilder, null}[↦471;refId=253]),())),
	108: Assignment(pc=477,DVar(useSites={109},value={_ <: java.util.regex.PatternSyntaxException, null}[↦477;refId=258],origin=108),VirtualFunctionCall(pc=477,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={107},value={java.lang.String, null}[↦474;refId=256])))),
	109: Throw(pc=480,UVar(defSites={108},value={_ <: java.util.regex.PatternSyntaxException, null}[↦477;refId=258])),
	110: Assignment(pc=485,DVar(useSites={111},value=String("In")[@485;refId=132],origin=110),StringConst(pc=485,In)),
	111: Assignment(pc=488,DVar(useSites={112},value=int ∈ [0,1],origin=111),VirtualFunctionCall(pc=488,java.lang.String,isInterface=false,boolean startsWith(java.lang.String),UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»]),(UVar(defSites={110},value=String("In")[@485;refId=132])))),
	112: If(pc=491,UVar(defSites={111},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=117),
	113: Assignment(pc=495,DVar(useSites={114},value=int = 2,origin=113),IntConst(pc=495,2)),
	114: Assignment(pc=496,DVar(useSites={115},value={java.lang.String, null}[↦496;refId=135],origin=114),VirtualFunctionCall(pc=496,java.lang.String,isInterface=false,java.lang.String substring(int),UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»]),(UVar(defSites={113},value=int = 2)))),
	115: Assignment(pc=499,DVar(useSites={137,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦499;refId=137],origin=115),StaticFunctionCall(pc=499,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forUnicodeBlock(java.lang.String),(UVar(defSites={114},value={java.lang.String, null}[↦496;refId=135])))),
	116: Goto(pc=504,target=137),
	117: Assignment(pc=508,DVar(useSites={118},value=String("Is")[@508;refId=138],origin=117),StringConst(pc=508,Is)),
	118: Assignment(pc=511,DVar(useSites={119},value=int ∈ [0,1],origin=118),VirtualFunctionCall(pc=511,java.lang.String,isInterface=false,boolean startsWith(java.lang.String),UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»]),(UVar(defSites={117},value=String("Is")[@508;refId=138])))),
	119: If(pc=514,UVar(defSites={118},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=129),
	120: Assignment(pc=518,DVar(useSites={121},value=int = 2,origin=120),IntConst(pc=518,2)),
	121: Assignment(pc=519,DVar(useSites={124,122,142,127},value={java.lang.String, null}[↦519;refId=141],origin=121),VirtualFunctionCall(pc=519,java.lang.String,isInterface=false,java.lang.String substring(int),UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»]),(UVar(defSites={120},value=int = 2)))),
	122: Assignment(pc=524,DVar(useSites={126,137,153,123,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦524;refId=143],origin=122),StaticFunctionCall(pc=524,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forUnicodeProperty(java.lang.String),(UVar(defSites={121},value={java.lang.String, null}[↦519;refId=141])))),
	123: If(pc=531,UVar(defSites={122},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦524;refId=143]),!=,NullExpr(pc=-333),target=126),
	124: Assignment(pc=535,DVar(useSites={126,137,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦535;refId=145],origin=124),StaticFunctionCall(pc=535,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forProperty(java.lang.String),(UVar(defSites={121},value={java.lang.String, null}[↦519;refId=141])))),
	125: Nop(pc=538),
	126: If(pc=542,UVar(defSites={124,122},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=146; values=«_ <: java.util.regex.Pattern$CharPredicate[↦524;refId=143], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦535;refId=145]»]),!=,NullExpr(pc=-333),target=137),
	127: Assignment(pc=546,DVar(useSites={137,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦546;refId=194],origin=127),StaticFunctionCall(pc=546,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forUnicodeScript(java.lang.String),(UVar(defSites={121},value={java.lang.String, null}[↦519;refId=141])))),
	128: Goto(pc=551,target=137),
	129: Assignment(pc=555,DVar(useSites={130},value=int = 256,origin=129),IntConst(pc=555,256)),
	130: Assignment(pc=558,DVar(useSites={131},value=int ∈ [0,1],origin=130),VirtualFunctionCall(pc=558,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={129},value=int = 256)))),
	131: If(pc=561,UVar(defSites={130},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=134),
	132: Assignment(pc=565,DVar(useSites={134,137,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦565;refId=149],origin=132),StaticFunctionCall(pc=565,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forPOSIXName(java.lang.String),(UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»])))),
	133: Nop(pc=568),
	134: If(pc=572,UVar(defSites={132,1},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=150; values=«null[↦5], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦565;refId=149]»]),!=,NullExpr(pc=-333),target=137),
	135: Assignment(pc=576,DVar(useSites={137,153,151},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦576;refId=199],origin=135),StaticFunctionCall(pc=576,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate forProperty(java.lang.String),(UVar(defSites={9,11,39},value=java.lang.String[refId=121; values=«{java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], java.lang.String[↦135;refId=118]»])))),
	136: Nop(pc=579),
	137: If(pc=583,UVar(defSites={132,124,122,1,115,135,127},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=201; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦499;refId=137], _ <: java.util.regex.Pattern$CharPredicate[↦524;refId=143], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦576;refId=199], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦546;refId=194], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦535;refId=145], _ <: java.util.regex.Pattern$CharPredicate[↦565;refId=149]»]),!=,NullExpr(pc=-333),target=148),
	138: Assignment(pc=587,DVar(useSites={141,139},value=java.lang.StringBuilder[↦587;refId=215],origin=138),New(pc=587,java.lang.StringBuilder)),
	139: NonVirtualMethodCall(pc=591,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={138},value=java.lang.StringBuilder[↦587;refId=215]),()),
	140: Assignment(pc=594,DVar(useSites={141},value=String("Unknown character property name {In/Is")[@594;refId=217],origin=140),StringConst(pc=594,Unknown character property name {In/Is)),
	141: Assignment(pc=597,DVar(useSites={142},value={java.lang.StringBuilder, null}[↦597;refId=219],origin=141),VirtualFunctionCall(pc=597,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={138},value=java.lang.StringBuilder[↦587;refId=215]),(UVar(defSites={140},value=String("Unknown character property name {In/Is")[@594;refId=217])))),
	142: Assignment(pc=601,DVar(useSites={144},value={java.lang.StringBuilder, null}[↦601;refId=222],origin=142),VirtualFunctionCall(pc=601,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={141},value={java.lang.StringBuilder, null}[↦597;refId=219]),(UVar(defSites={9,121,11,39},value={java.lang.String, null}[refId=191; values=«java.lang.String[↦135;refId=118], {java.lang.String, null}[↦34;refId=109], java.lang.String[↦41;refId=110], {java.lang.String, null}[↦519;refId=141]»])))),
	143: Assignment(pc=604,DVar(useSites={144},value=String("}")[@604;refId=223],origin=143),StringConst(pc=604,})),
	144: Assignment(pc=607,DVar(useSites={145},value={java.lang.StringBuilder, null}[↦607;refId=226],origin=144),VirtualFunctionCall(pc=607,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={142},value={java.lang.StringBuilder, null}[↦601;refId=222]),(UVar(defSites={143},value=String("}")[@604;refId=223])))),
	145: Assignment(pc=610,DVar(useSites={146},value={java.lang.String, null}[↦610;refId=229],origin=145),VirtualFunctionCall(pc=610,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={144},value={java.lang.StringBuilder, null}[↦607;refId=226]),())),
	146: Assignment(pc=613,DVar(useSites={147},value={_ <: java.util.regex.PatternSyntaxException, null}[↦613;refId=231],origin=146),VirtualFunctionCall(pc=613,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={145},value={java.lang.String, null}[↦610;refId=229])))),
	147: Throw(pc=616,UVar(defSites={146},value={_ <: java.util.regex.PatternSyntaxException, null}[↦613;refId=231])),
	148: If(pc=618,UVar(defSites={-3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=153),
	149: Assignment(pc=622,DVar(useSites={150},value=int = 1,origin=149),IntConst(pc=622,1)),
	150: PutField(pc=623,java.util.regex.Pattern,hasSupplementary,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={149},value=int = 1)),
	151: Assignment(pc=628,DVar(useSites={153},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦628;refId=262],origin=151),VirtualFunctionCall(pc=628,java.util.regex.Pattern$CharPredicate,isInterface=true,java.util.regex.Pattern$CharPredicate negate(),UVar(defSites={132,92,124,90,122,94,1,115,135,127},value=_ <: java.util.regex.Pattern$CharPredicate[refId=234; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦576;refId=199], _ <: java.util.regex.Pattern$CharPredicate[↦524;refId=143], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦416;refId=206], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦546;refId=194], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦426;refId=203], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦406;refId=209], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦499;refId=137], _ <: java.util.regex.Pattern$CharPredicate[↦565;refId=149], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦535;refId=145]»]),())),
	152: Nop(pc=633),
	153: ReturnValue(pc=637,UVar(defSites={132,92,124,90,122,94,1,115,135,151,127},value={_ <: java.util.regex.Pattern$CharPredicate, null}[refId=263; values=«{_ <: java.util.regex.Pattern$CharPredicate, null}[↦576;refId=199], _ <: java.util.regex.Pattern$CharPredicate[↦524;refId=143], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦416;refId=206], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦628;refId=262], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦546;refId=194], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦426;refId=203], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦406;refId=209], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦499;refId=137], _ <: java.util.regex.Pattern$CharPredicate[↦565;refId=149], {_ <: java.util.regex.Pattern$CharPredicate, null}[↦535;refId=145]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=25,end=26) -> {BB_5c,BB_34}
	BB_10: BasicBlock(start=152,end=152) -> {BB_b}
	BB_11: BasicBlock(start=57,end=58) -> {BB_5c,BB_33}
	BB_12: BasicBlock(start=78,end=79) -> {BB_17}
	BB_13: BasicBlock(start=147,end=147) -> {BB_5c}
	BB_14: BasicBlock(start=132,end=132) -> {BB_5c,BB_18}
	BB_15: BasicBlock(start=116,end=116) -> {BB_20}
	BB_16: BasicBlock(start=1,end=2) -> {BB_3c,BB_59}
	BB_17: BasicBlock(start=89,end=89) -> {BB_5b,BB_62,BB_28,BB_22}
	BB_18: BasicBlock(start=133,end=133) -> {BB_29}
	BB_19: BasicBlock(start=6,end=6) -> {BB_5c,BB_36}
	BB_1: BasicBlock(start=53,end=54) -> {BB_5c,BB_50}
	BB_1a: BasicBlock(start=85,end=86) -> {BB_5c,BB_4e}
	BB_1b: BasicBlock(start=102,end=103) -> {BB_5c,BB_4f}
	BB_1c: BasicBlock(start=60,end=61) -> {BB_5c,BB_61}
	BB_1d: BasicBlock(start=117,end=118) -> {BB_5c,BB_54}
	BB_1e: BasicBlock(start=38,end=38) -> {BB_5c}
	BB_1f: BasicBlock(start=70,end=71) -> {BB_5c,BB_4b}
	BB_20: BasicBlock(start=137,end=137) -> {BB_3,BB_2e}
	BB_21: BasicBlock(start=33,end=35) -> {BB_37,BB_56}
	BB_22: BasicBlock(start=92,end=92) -> {BB_5c,BB_f}
	BB_23: BasicBlock(start=65,end=66) -> {BB_5c,BB_47}
	BB_24: BasicBlock(start=97,end=98) -> {BB_5c,BB_4d}
	BB_25: BasicBlock(start=109,end=109) -> {BB_5c}
	BB_26: BasicBlock(start=124,end=124) -> {BB_5c,BB_d}
	BB_27: BasicBlock(start=77,end=77) -> {BB_12,BB_17}
	BB_28: BasicBlock(start=96,end=96) -> {BB_2e,BB_24}
	BB_29: BasicBlock(start=134,end=134) -> {BB_20,BB_3b}
	BB_2: BasicBlock(start=129,end=130) -> {BB_5c,BB_5f}
	BB_2a: BasicBlock(start=73,end=74) -> {BB_17}
	BB_2b: BasicBlock(start=128,end=128) -> {BB_20}
	BB_2c: BasicBlock(start=105,end=106) -> {BB_5c,BB_5a}
	BB_2d: BasicBlock(start=32,end=32) -> {BB_5c}
	BB_2e: BasicBlock(start=148,end=148) -> {BB_31,BB_b}
	BB_2f: BasicBlock(start=45,end=45) -> {BB_e}
	BB_30: BasicBlock(start=17,end=17) -> {BB_5c,BB_43}
	BB_31: BasicBlock(start=149,end=151) -> {BB_5c,BB_10}
	BB_32: BasicBlock(start=22,end=22) -> {BB_5c,BB_51}
	BB_33: BasicBlock(start=59,end=59) -> {BB_53,BB_23,BB_17,BB_1c,BB_1a,BB_1f,BB_3d}
	BB_34: BasicBlock(start=27,end=29) -> {BB_21,BB_58}
	BB_35: BasicBlock(start=113,end=114) -> {BB_5c,BB_7}
	BB_36: BasicBlock(start=7,end=7) -> {BB_4a,BB_52}
	BB_37: BasicBlock(start=39,end=44) -> {BB_5c,BB_2f}
	BB_38: BasicBlock(start=140,end=141) -> {BB_5c,BB_a}
	BB_39: BasicBlock(start=91,end=91) -> {BB_28}
	BB_3: BasicBlock(start=138,end=139) -> {BB_5c,BB_38}
	BB_3a: BasicBlock(start=108,end=108) -> {BB_5c,BB_25}
	BB_3b: BasicBlock(start=135,end=135) -> {BB_5c,BB_5e}
	BB_3c: BasicBlock(start=3,end=5) -> {BB_5c,BB_19}
	BB_3d: BasicBlock(start=80,end=81) -> {BB_5c,BB_55}
	BB_3e: BasicBlock(start=112,end=112) -> {BB_35,BB_1d}
	BB_3f: BasicBlock(start=123,end=123) -> {BB_5d,BB_26}
	BB_40: BasicBlock(start=145,end=145) -> {BB_5c,BB_57}
	BB_41: BasicBlock(start=48,end=49) -> {BB_c,BB_46}
	BB_42: BasicBlock(start=63,end=64) -> {BB_17}
	BB_43: BasicBlock(start=18,end=18) -> {BB_e}
	BB_44: ExitNode(normalReturn=true)
	BB_45: BasicBlock(start=95,end=95) -> {BB_28}
	BB_46: BasicBlock(start=50,end=52) -> {BB_5c,BB_1}
	BB_47: BasicBlock(start=67,end=67) -> {BB_60,BB_17}
	BB_48: BasicBlock(start=16,end=16) -> {BB_30}
	BB_49: BasicBlock(start=127,end=127) -> {BB_5c,BB_2b}
	BB_4: BasicBlock(start=101,end=101) -> {BB_5c,BB_1b}
	BB_4a: BasicBlock(start=11,end=15) -> {BB_5c,BB_48}
	BB_4b: BasicBlock(start=72,end=72) -> {BB_2a,BB_17}
	BB_4c: BasicBlock(start=143,end=144) -> {BB_5c,BB_40}
	BB_4d: BasicBlock(start=99,end=100) -> {BB_5c,BB_4}
	BB_4e: BasicBlock(start=87,end=87) -> {BB_6,BB_17}
	BB_4f: BasicBlock(start=104,end=104) -> {BB_5c,BB_2c}
	BB_50: BasicBlock(start=55,end=56) -> {BB_5c,BB_11}
	BB_51: BasicBlock(start=23,end=24) -> {BB_32,BB_0}
	BB_52: BasicBlock(start=8,end=9) -> {BB_5c,BB_9}
	BB_53: BasicBlock(start=75,end=76) -> {BB_5c,BB_27}
	BB_54: BasicBlock(start=119,end=119) -> {BB_2,BB_8}
	BB_55: BasicBlock(start=82,end=82) -> {BB_17,BB_64}
	BB_56: BasicBlock(start=36,end=37) -> {BB_5c,BB_1e}
	BB_57: BasicBlock(start=146,end=146) -> {BB_5c,BB_13}
	BB_58: BasicBlock(start=30,end=31) -> {BB_5c,BB_2d}
	BB_59: BasicBlock(start=19,end=21) -> {BB_5c,BB_32}
	BB_5: BasicBlock(start=0,end=0) -> {BB_5c,BB_16}
	BB_5a: BasicBlock(start=107,end=107) -> {BB_5c,BB_3a}
	BB_5b: BasicBlock(start=94,end=94) -> {BB_5c,BB_45}
	BB_5c: ExitNode(normalReturn=false)
	BB_5d: BasicBlock(start=126,end=126) -> {BB_49,BB_20}
	BB_5e: BasicBlock(start=136,end=136) -> {BB_20}
	BB_5f: BasicBlock(start=131,end=131) -> {BB_14,BB_29}
	BB_60: BasicBlock(start=68,end=69) -> {BB_17}
	BB_61: BasicBlock(start=62,end=62) -> {BB_42,BB_17}
	BB_62: BasicBlock(start=90,end=90) -> {BB_5c,BB_39}
	BB_63: BasicBlock(start=122,end=122) -> {BB_5c,BB_3f}
	BB_64: BasicBlock(start=83,end=84) -> {BB_17}
	BB_6: BasicBlock(start=88,end=88) -> {BB_17}
	BB_7: BasicBlock(start=115,end=115) -> {BB_5c,BB_15}
	BB_8: BasicBlock(start=120,end=121) -> {BB_5c,BB_63}
	BB_9: BasicBlock(start=10,end=10) -> {BB_30}
	BB_a: BasicBlock(start=142,end=142) -> {BB_5c,BB_4c}
	BB_b: BasicBlock(start=153,end=153) -> {BB_44}
	BB_c: BasicBlock(start=110,end=111) -> {BB_5c,BB_3e}
	BB_d: BasicBlock(start=125,end=125) -> {BB_5d}
	BB_e: BasicBlock(start=46,end=47) -> {BB_5c,BB_41}
	BB_f: BasicBlock(start=93,end=93) -> {BB_28}
))

int countCodePoints(java.lang.CharSequence)
AITACode(params=(Parameters(
	1: useSites={0,10,6} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={9,3},value=an int,origin=0),VirtualFunctionCall(pc=1,java.lang.CharSequence,isInterface=true,int length(),UVar(defSites={-2},value={_ <: java.lang.CharSequence, null}[↦-1;refId=102]),())),
	1: Assignment(pc=7,DVar(useSites={4,15},value=int = 0,origin=1),IntConst(pc=7,0)),
	2: Assignment(pc=9,DVar(useSites={6,5,3},value=int = 0,origin=2),IntConst(pc=9,0)),
	3: If(pc=13,UVar(defSites={2,5,13},value=int ∈ [0,2147483647]),>=,UVar(defSites={0},value=an int),target=15),
	4: Assignment(pc=16,DVar(useSites={5,15},value=an int,origin=4),BinaryExpr(pc=16,ComputationalTypeInt,UVar(defSites={4,1},value=an int),+,IntConst(pc=16,1))),
	5: Assignment(pc=21,DVar(useSites={10,6,9,13,3},value=int ∈ [1,2147483647],origin=5),BinaryExpr(pc=21,ComputationalTypeInt,UVar(defSites={2,5,13},value=int ∈ [0,2147483646]),+,IntConst(pc=21,1))),
	6: Assignment(pc=24,DVar(useSites={7},value=int ∈ [0,65535],origin=6),VirtualFunctionCall(pc=24,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-2},value=_ <: java.lang.CharSequence[↦-1;refId=102]),(UVar(defSites={2,5,13},value=int ∈ [0,2147483646])))),
	7: Assignment(pc=29,DVar(useSites={8},value=int ∈ [0,1],origin=7),StaticFunctionCall(pc=29,java.lang.Character,isInterface=false,boolean isHighSurrogate(char),(UVar(defSites={6},value=int ∈ [0,65535])))),
	8: If(pc=32,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=3),
	9: If(pc=37,UVar(defSites={5},value=int ∈ [1,2147483647]),>=,UVar(defSites={0},value=int ∈ [1,2147483647]),target=3),
	10: Assignment(pc=42,DVar(useSites={11},value=int ∈ [0,65535],origin=10),VirtualFunctionCall(pc=42,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-2},value=_ <: java.lang.CharSequence[↦-1;refId=102]),(UVar(defSites={5},value=int ∈ [1,2147483646])))),
	11: Assignment(pc=47,DVar(useSites={12},value=int ∈ [0,1],origin=11),StaticFunctionCall(pc=47,java.lang.Character,isInterface=false,boolean isLowSurrogate(char),(UVar(defSites={10},value=int ∈ [0,65535])))),
	12: If(pc=50,UVar(defSites={11},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=3),
	13: Assignment(pc=53,DVar(useSites={6,5,3},value=int ∈ [2,2147483647],origin=13),BinaryExpr(pc=53,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [1,2147483646]),+,IntConst(pc=53,1))),
	14: Goto(pc=56,target=3),
	15: ReturnValue(pc=60,UVar(defSites={4,1},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_d,BB_2}
	BB_1: BasicBlock(start=10,end=10) -> {BB_d,BB_9}
	BB_2: BasicBlock(start=1,end=2) -> {BB_7}
	BB_3: BasicBlock(start=9,end=9) -> {BB_1,BB_7}
	BB_4: BasicBlock(start=13,end=14) -> {BB_7}
	BB_5: BasicBlock(start=12,end=12) -> {BB_4,BB_7}
	BB_6: BasicBlock(start=7,end=7) -> {BB_d,BB_a}
	BB_7: BasicBlock(start=3,end=3) -> {BB_c,BB_b}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=11,end=11) -> {BB_d,BB_5}
	BB_a: BasicBlock(start=8,end=8) -> {BB_3,BB_7}
	BB_b: BasicBlock(start=15,end=15) -> {BB_8}
	BB_c: BasicBlock(start=4,end=6) -> {BB_d,BB_6}
	BB_d: ExitNode(normalReturn=false)
))

java.lang.String groupname(int)
AITACode(params=(Parameters(
	0: useSites={9,5,15} (origin=-1),
	1: useSites={2,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={8,1,17},value=java.lang.StringBuilder[↦0;refId=103],origin=0),New(pc=0,java.lang.StringBuilder)),
	1: NonVirtualMethodCall(pc=4,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={0},value=java.lang.StringBuilder[↦0;refId=103]),()),
	2: Assignment(pc=9,DVar(useSites={3},value=int ∈ [0,1],origin=2),StaticFunctionCall(pc=9,java.util.regex.ASCII,isInterface=false,boolean isAlpha(int),(UVar(defSites={-2},value=an int)))),
	3: If(pc=12,UVar(defSites={2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=7),
	4: Assignment(pc=16,DVar(useSites={5},value=String("capturing group name does not start with a Latin letter")[@16;refId=106],origin=4),StringConst(pc=16,capturing group name does not start with a Latin letter)),
	5: Assignment(pc=19,DVar(useSites={6},value={_ <: java.util.regex.PatternSyntaxException, null}[↦19;refId=108],origin=5),VirtualFunctionCall(pc=19,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={4},value=String("capturing group name does not start with a Latin letter")[@16;refId=106])))),
	6: Throw(pc=22,UVar(defSites={5},value={_ <: java.util.regex.PatternSyntaxException, null}[↦19;refId=108])),
	7: Assignment(pc=25,DVar(useSites={8},value=int ∈ [0,65535],origin=7),PrimitiveTypecastExpr(pc=25,CharType,UVar(defSites={-2,9},value=an int))),
	8: ExprStmt(pc=26,VirtualFunctionCall(pc=26,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={0},value=java.lang.StringBuilder[↦0;refId=103]),(UVar(defSites={7},value=int ∈ [0,65535])))),
	9: Assignment(pc=31,DVar(useSites={10,13,7},value=an int,origin=9),VirtualFunctionCall(pc=31,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	10: Assignment(pc=36,DVar(useSites={11},value=int ∈ [0,1],origin=10),StaticFunctionCall(pc=36,java.util.regex.ASCII,isInterface=false,boolean isAlnum(int),(UVar(defSites={9},value=an int)))),
	11: If(pc=39,UVar(defSites={10},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=7),
	12: Assignment(pc=43,DVar(useSites={13},value=int = 62,origin=12),IntConst(pc=43,62)),
	13: If(pc=45,UVar(defSites={9},value=an int),==,UVar(defSites={12},value=int = 62),target=17),
	14: Assignment(pc=49,DVar(useSites={15},value=String("named capturing group is missing trailing '>'")[@49;refId=116],origin=14),StringConst(pc=49,named capturing group is missing trailing '>')),
	15: Assignment(pc=52,DVar(useSites={16},value={_ <: java.util.regex.PatternSyntaxException, null}[↦52;refId=118],origin=15),VirtualFunctionCall(pc=52,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={14},value=String("named capturing group is missing trailing '>'")[@49;refId=116])))),
	16: Throw(pc=55,UVar(defSites={15},value={_ <: java.util.regex.PatternSyntaxException, null}[↦52;refId=118])),
	17: Assignment(pc=57,DVar(useSites={18},value={java.lang.String, null}[↦57;refId=115],origin=17),VirtualFunctionCall(pc=57,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={0},value=java.lang.StringBuilder[↦0;refId=103]),())),
	18: ReturnValue(pc=60,UVar(defSites={17},value={java.lang.String, null}[↦57;refId=115]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_f,BB_5}
	BB_1: BasicBlock(start=10,end=10) -> {BB_f,BB_b}
	BB_2: BasicBlock(start=14,end=15) -> {BB_f,BB_a}
	BB_3: BasicBlock(start=6,end=6) -> {BB_f}
	BB_4: BasicBlock(start=9,end=9) -> {BB_f,BB_1}
	BB_5: BasicBlock(start=2,end=2) -> {BB_f,BB_9}
	BB_6: BasicBlock(start=17,end=17) -> {BB_f,BB_c}
	BB_7: BasicBlock(start=12,end=13) -> {BB_2,BB_6}
	BB_8: BasicBlock(start=7,end=8) -> {BB_f,BB_4}
	BB_9: BasicBlock(start=3,end=3) -> {BB_8,BB_e}
	BB_a: BasicBlock(start=16,end=16) -> {BB_f}
	BB_b: BasicBlock(start=11,end=11) -> {BB_7,BB_8}
	BB_c: BasicBlock(start=18,end=18) -> {BB_d}
	BB_d: ExitNode(normalReturn=true)
	BB_e: BasicBlock(start=4,end=5) -> {BB_f,BB_3}
	BB_f: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate SingleS(int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$SingleS(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda, null}[↦1;refId=103],origin=0),StaticFunctionCall(pc=1,java.util.regex.Pattern$SingleS(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda,isInterface=false,java.util.regex.Pattern$SingleS(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda $newInstance(int),(UVar(defSites={-2},value=an int)))),
	1: ReturnValue(pc=6,UVar(defSites={0},value={_ <: java.util.regex.Pattern$SingleS(I)Ljava$util$regex$Pattern$CharPredicate::1$Lambda, null}[↦1;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate DOT()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value={_ <: java.util.regex.Pattern$DOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda, null}[↦0;refId=103],origin=0),StaticFunctionCall(pc=0,java.util.regex.Pattern$DOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda,isInterface=false,java.util.regex.Pattern$DOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda $newInstance(),())),
	1: ReturnValue(pc=5,UVar(defSites={0},value={_ <: java.util.regex.Pattern$DOT()Ljava$util$regex$Pattern$CharPredicate::0$Lambda, null}[↦0;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void addFlag()
AITACode(params=(Parameters(
	0: useSites={0,16,8,36,44,28,18,26,6,38,46,33,41,21,13,3,11,43,23,31} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Nop(pc=4),
	2: Switch(pc=6,defaultTarget=45,index=UVar(defSites={0,46},value=an int),npairs=(IntIntPair(45,43),IntIntPair(85,38),IntIntPair(99,28),IntIntPair(100,18),IntIntPair(105,3),IntIntPair(109,8),IntIntPair(115,13),IntIntPair(117,23),IntIntPair(120,33)),
	3: Assignment(pc=90,DVar(useSites={5},value=an int,origin=3),GetField(pc=90,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	4: Assignment(pc=93,DVar(useSites={5},value=int = 2,origin=4),IntConst(pc=93,2)),
	5: Assignment(pc=94,DVar(useSites={6},value=an int,origin=5),BinaryExpr(pc=94,ComputationalTypeInt,UVar(defSites={3},value=an int),|,UVar(defSites={4},value=int = 2))),
	6: PutField(pc=95,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={5},value=an int)),
	7: Goto(pc=98,target=46),
	8: Assignment(pc=103,DVar(useSites={10},value=an int,origin=8),GetField(pc=103,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	9: Assignment(pc=106,DVar(useSites={10},value=int = 8,origin=9),IntConst(pc=106,8)),
	10: Assignment(pc=108,DVar(useSites={11},value=an int,origin=10),BinaryExpr(pc=108,ComputationalTypeInt,UVar(defSites={8},value=an int),|,UVar(defSites={9},value=int = 8))),
	11: PutField(pc=109,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={10},value=an int)),
	12: Goto(pc=112,target=46),
	13: Assignment(pc=117,DVar(useSites={15},value=an int,origin=13),GetField(pc=117,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	14: Assignment(pc=120,DVar(useSites={15},value=int = 32,origin=14),IntConst(pc=120,32)),
	15: Assignment(pc=122,DVar(useSites={16},value=an int,origin=15),BinaryExpr(pc=122,ComputationalTypeInt,UVar(defSites={13},value=an int),|,UVar(defSites={14},value=int = 32))),
	16: PutField(pc=123,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={15},value=an int)),
	17: Goto(pc=126,target=46),
	18: Assignment(pc=131,DVar(useSites={20},value=an int,origin=18),GetField(pc=131,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	19: Assignment(pc=134,DVar(useSites={20},value=int = 1,origin=19),IntConst(pc=134,1)),
	20: Assignment(pc=135,DVar(useSites={21},value=an int,origin=20),BinaryExpr(pc=135,ComputationalTypeInt,UVar(defSites={18},value=an int),|,UVar(defSites={19},value=int = 1))),
	21: PutField(pc=136,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={20},value=an int)),
	22: Goto(pc=139,target=46),
	23: Assignment(pc=144,DVar(useSites={25},value=an int,origin=23),GetField(pc=144,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	24: Assignment(pc=147,DVar(useSites={25},value=int = 64,origin=24),IntConst(pc=147,64)),
	25: Assignment(pc=149,DVar(useSites={26},value=an int,origin=25),BinaryExpr(pc=149,ComputationalTypeInt,UVar(defSites={23},value=an int),|,UVar(defSites={24},value=int = 64))),
	26: PutField(pc=150,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={25},value=an int)),
	27: Goto(pc=153,target=46),
	28: Assignment(pc=158,DVar(useSites={30},value=an int,origin=28),GetField(pc=158,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	29: Assignment(pc=161,DVar(useSites={30},value=int = 128,origin=29),IntConst(pc=161,128)),
	30: Assignment(pc=164,DVar(useSites={31},value=an int,origin=30),BinaryExpr(pc=164,ComputationalTypeInt,UVar(defSites={28},value=an int),|,UVar(defSites={29},value=int = 128))),
	31: PutField(pc=165,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={30},value=an int)),
	32: Goto(pc=168,target=46),
	33: Assignment(pc=173,DVar(useSites={35},value=an int,origin=33),GetField(pc=173,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	34: Assignment(pc=176,DVar(useSites={35},value=int = 4,origin=34),IntConst(pc=176,4)),
	35: Assignment(pc=177,DVar(useSites={36},value=an int,origin=35),BinaryExpr(pc=177,ComputationalTypeInt,UVar(defSites={33},value=an int),|,UVar(defSites={34},value=int = 4))),
	36: PutField(pc=178,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={35},value=an int)),
	37: Goto(pc=181,target=46),
	38: Assignment(pc=186,DVar(useSites={40},value=an int,origin=38),GetField(pc=186,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	39: Assignment(pc=189,DVar(useSites={40},value=int = 320,origin=39),IntConst(pc=189,320)),
	40: Assignment(pc=192,DVar(useSites={41},value=an int,origin=40),BinaryExpr(pc=192,ComputationalTypeInt,UVar(defSites={38},value=an int),|,UVar(defSites={39},value=int = 320))),
	41: PutField(pc=193,java.util.regex.Pattern,flags0,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={40},value=an int)),
	42: Goto(pc=196,target=46),
	43: ExprStmt(pc=200,VirtualFunctionCall(pc=200,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	44: VirtualMethodCall(pc=205,java.util.regex.Pattern,isInterface=false,void subFlag(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	45: Return(pc=208),
	46: Assignment(pc=210,DVar(useSites={2},value=an int,origin=46),VirtualFunctionCall(pc=210,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	47: Goto(pc=214,target=2)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_b,BB_2}
	BB_10: BasicBlock(start=18,end=22) -> {BB_1}
	BB_11: ExitNode(normalReturn=true)
	BB_1: BasicBlock(start=46,end=46) -> {BB_b,BB_c}
	BB_2: BasicBlock(start=1,end=1) -> {BB_4}
	BB_3: BasicBlock(start=13,end=17) -> {BB_1}
	BB_4: BasicBlock(start=2,end=2) -> {BB_e,BB_3,BB_10,BB_5,BB_d,BB_8,BB_a,BB_7,BB_9,BB_f}
	BB_5: BasicBlock(start=45,end=45) -> {BB_11}
	BB_6: BasicBlock(start=44,end=44) -> {BB_b,BB_5}
	BB_7: BasicBlock(start=3,end=7) -> {BB_1}
	BB_8: BasicBlock(start=43,end=43) -> {BB_b,BB_6}
	BB_9: BasicBlock(start=23,end=27) -> {BB_1}
	BB_a: BasicBlock(start=8,end=12) -> {BB_1}
	BB_b: ExitNode(normalReturn=false)
	BB_c: BasicBlock(start=47,end=47) -> {BB_4}
	BB_d: BasicBlock(start=33,end=37) -> {BB_1}
	BB_e: BasicBlock(start=28,end=32) -> {BB_1}
	BB_f: BasicBlock(start=38,end=42) -> {BB_1}
))

boolean lambda$HorizWS$3(int)
AITACode(params=(Parameters(
	1: useSites={1,17,9,5,13,3,19,11,7,15} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 9,origin=0),IntConst(pc=1,9)),
	1: If(pc=3,UVar(defSites={-2},value=an int),==,UVar(defSites={0},value=int = 9),target=20),
	2: Assignment(pc=7,DVar(useSites={3},value=int = 32,origin=2),IntConst(pc=7,32)),
	3: If(pc=9,UVar(defSites={-2},value=an int),==,UVar(defSites={2},value=int = 32),target=20),
	4: Assignment(pc=13,DVar(useSites={5},value=int = 160,origin=4),IntConst(pc=13,160)),
	5: If(pc=16,UVar(defSites={-2},value=an int),==,UVar(defSites={4},value=int = 160),target=20),
	6: Assignment(pc=20,DVar(useSites={7},value=int = 5760,origin=6),IntConst(pc=20,5760)),
	7: If(pc=23,UVar(defSites={-2},value=an int),==,UVar(defSites={6},value=int = 5760),target=20),
	8: Assignment(pc=27,DVar(useSites={9},value=int = 6158,origin=8),IntConst(pc=27,6158)),
	9: If(pc=30,UVar(defSites={-2},value=an int),==,UVar(defSites={8},value=int = 6158),target=20),
	10: Assignment(pc=34,DVar(useSites={11},value=int = 8192,origin=10),IntConst(pc=34,8192)),
	11: If(pc=37,UVar(defSites={-2},value=an int),<,UVar(defSites={10},value=int = 8192),target=14),
	12: Assignment(pc=41,DVar(useSites={13},value=int = 8202,origin=12),IntConst(pc=41,8202)),
	13: If(pc=44,UVar(defSites={-2},value=int ∈ [8192,2147483647]),<=,UVar(defSites={12},value=int = 8202),target=20),
	14: Assignment(pc=48,DVar(useSites={15},value=int = 8239,origin=14),IntConst(pc=48,8239)),
	15: If(pc=51,UVar(defSites={-2},value=an int),==,UVar(defSites={14},value=int = 8239),target=20),
	16: Assignment(pc=55,DVar(useSites={17},value=int = 8287,origin=16),IntConst(pc=55,8287)),
	17: If(pc=58,UVar(defSites={-2},value=an int),==,UVar(defSites={16},value=int = 8287),target=20),
	18: Assignment(pc=62,DVar(useSites={19},value=int = 12288,origin=18),IntConst(pc=62,12288)),
	19: If(pc=65,UVar(defSites={-2},value=an int),!=,UVar(defSites={18},value=int = 12288),target=22),
	20: Assignment(pc=68,DVar(useSites={23},value=int = 1,origin=20),IntConst(pc=68,1)),
	21: Goto(pc=69,target=23),
	22: Assignment(pc=72,DVar(useSites={23},value=int ∈ [0,1],origin=22),IntConst(pc=72,0)),
	23: ReturnValue(pc=73,UVar(defSites={20,22},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_5}
	BB_1: BasicBlock(start=10,end=11) -> {BB_7,BB_2}
	BB_2: BasicBlock(start=14,end=15) -> {BB_3,BB_8}
	BB_3: BasicBlock(start=20,end=21) -> {BB_9}
	BB_4: BasicBlock(start=6,end=7) -> {BB_3,BB_a}
	BB_5: BasicBlock(start=2,end=3) -> {BB_3,BB_d}
	BB_6: BasicBlock(start=22,end=22) -> {BB_9}
	BB_7: BasicBlock(start=12,end=13) -> {BB_3,BB_2}
	BB_8: BasicBlock(start=16,end=17) -> {BB_3,BB_b}
	BB_9: BasicBlock(start=23,end=23) -> {BB_c}
	BB_a: BasicBlock(start=8,end=9) -> {BB_3,BB_1}
	BB_b: BasicBlock(start=18,end=19) -> {BB_6,BB_3}
	BB_c: ExitNode(normalReturn=true)
	BB_d: BasicBlock(start=4,end=5) -> {BB_3,BB_4}
	BB_e: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate range(java.util.regex.Pattern$BitClass)
AITACode(params=(Parameters(
	0: useSites={0,64,32,40,20,84,76,66,58,70,38,22,14,46,17,73,57,53,3,35,43,23,47,95} (origin=-1),
	1: useSites={84,53} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={80,68,84,2,82,42,90,78,53},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	1: Assignment(pc=6,DVar(useSites={2},value=int = 92,origin=1),IntConst(pc=6,92)),
	2: If(pc=8,UVar(defSites={0},value=an int),!=,UVar(defSites={1},value=int = 92),target=40),
	3: Assignment(pc=12,DVar(useSites={9,5,7},value=an int,origin=3),VirtualFunctionCall(pc=12,java.util.regex.Pattern,isInterface=false,int nextEscaped(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	4: Assignment(pc=17,DVar(useSites={5},value=int = 112,origin=4),IntConst(pc=17,112)),
	5: If(pc=19,UVar(defSites={3},value=an int),==,UVar(defSites={4},value=int = 112),target=8),
	6: Assignment(pc=23,DVar(useSites={7},value=int = 80,origin=6),IntConst(pc=23,80)),
	7: If(pc=25,UVar(defSites={3},value=an int),!=,UVar(defSites={6},value=int = 80),target=22),
	8: Assignment(pc=29,DVar(useSites={9},value=int = 80,origin=8),IntConst(pc=29,80)),
	9: If(pc=31,UVar(defSites={3},value=int ∈ [80,112]),!=,UVar(defSites={8},value=int = 80),target=12),
	10: Assignment(pc=34,DVar(useSites={20},value=int = 1,origin=10),IntConst(pc=34,1)),
	11: Goto(pc=35,target=13),
	12: Assignment(pc=38,DVar(useSites={20},value=int ∈ [0,1],origin=12),IntConst(pc=38,0)),
	13: Assignment(pc=40,DVar(useSites={20},value=int = 1,origin=13),IntConst(pc=40,1)),
	14: Assignment(pc=44,DVar(useSites={16},value=an int,origin=14),VirtualFunctionCall(pc=44,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	15: Assignment(pc=49,DVar(useSites={16},value=int = 123,origin=15),IntConst(pc=49,123)),
	16: If(pc=51,UVar(defSites={14},value=an int),==,UVar(defSites={15},value=int = 123),target=19),
	17: VirtualMethodCall(pc=55,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	18: Goto(pc=58,target=20),
	19: Assignment(pc=61,DVar(useSites={20},value=int = 0,origin=19),IntConst(pc=61,0)),
	20: Assignment(pc=68,DVar(useSites={21},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦68;refId=158],origin=20),VirtualFunctionCall(pc=68,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate family(boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={13,19},value=int ∈ [0,1]),UVar(defSites={12,10},value=int ∈ [0,1])))),
	21: ReturnValue(pc=71,UVar(defSites={20},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦68;refId=158])),
	22: Assignment(pc=73,DVar(useSites={26},value={int[], null}[↦73;refId=107],origin=22),GetField(pc=73,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	23: Assignment(pc=77,DVar(useSites={25},value=an int,origin=23),GetField(pc=77,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	24: Assignment(pc=80,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=80,1)),
	25: Assignment(pc=81,DVar(useSites={26},value=an int,origin=25),BinaryExpr(pc=81,ComputationalTypeInt,UVar(defSites={23},value=an int),+,UVar(defSites={24},value=int = 1))),
	26: Assignment(pc=82,DVar(useSites={28},value=an int,origin=26),ArrayLoad(pc=82,UVar(defSites={25},value=an int),UVar(defSites={22},value={int[], null}[↦73;refId=107]))),
	27: Assignment(pc=83,DVar(useSites={28},value=int = 45,origin=27),IntConst(pc=83,45)),
	28: If(pc=85,UVar(defSites={26},value=an int),!=,UVar(defSites={27},value=int = 45),target=31),
	29: Assignment(pc=88,DVar(useSites={35},value=int = 1,origin=29),IntConst(pc=88,1)),
	30: Goto(pc=89,target=32),
	31: Assignment(pc=92,DVar(useSites={35},value=int ∈ [0,1],origin=31),IntConst(pc=92,0)),
	32: VirtualMethodCall(pc=95,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	33: Assignment(pc=99,DVar(useSites={35},value=int = 1,origin=33),IntConst(pc=99,1)),
	34: Assignment(pc=100,DVar(useSites={35},value=int = 1,origin=34),IntConst(pc=100,1)),
	35: Assignment(pc=102,DVar(useSites={80,68,84,82,42,90,78,37,53},value=an int,origin=35),VirtualFunctionCall(pc=102,java.util.regex.Pattern,isInterface=false,int escape(boolean,boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={33},value=int = 1),UVar(defSites={34},value=int = 1),UVar(defSites={29,31},value=int ∈ [0,1])))),
	36: Assignment(pc=107,DVar(useSites={37},value=int = -1,origin=36),IntConst(pc=107,-1)),
	37: If(pc=108,UVar(defSites={35},value=an int),!=,UVar(defSites={36},value=int = -1),target=42),
	38: Assignment(pc=112,DVar(useSites={39},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦112;refId=140],origin=38),GetField(pc=112,java.util.regex.Pattern,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	39: ReturnValue(pc=115,UVar(defSites={38},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦112;refId=140])),
	40: ExprStmt(pc=120,VirtualFunctionCall(pc=120,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	41: Nop(pc=123),
	42: If(pc=125,UVar(defSites={0,35},value=an int),<,IntConst(pc=-333,0),target=86),
	43: Assignment(pc=129,DVar(useSites={45},value=an int,origin=43),VirtualFunctionCall(pc=129,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	44: Assignment(pc=132,DVar(useSites={45},value=int = 45,origin=44),IntConst(pc=132,45)),
	45: If(pc=134,UVar(defSites={43},value=an int),!=,UVar(defSites={44},value=int = 45),target=84),
	46: Assignment(pc=138,DVar(useSites={50},value={int[], null}[↦138;refId=111],origin=46),GetField(pc=138,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	47: Assignment(pc=142,DVar(useSites={49},value=an int,origin=47),GetField(pc=142,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	48: Assignment(pc=145,DVar(useSites={49},value=int = 1,origin=48),IntConst(pc=145,1)),
	49: Assignment(pc=146,DVar(useSites={50},value=an int,origin=49),BinaryExpr(pc=146,ComputationalTypeInt,UVar(defSites={47},value=an int),+,UVar(defSites={48},value=int = 1))),
	50: Assignment(pc=147,DVar(useSites={56,52},value=an int,origin=50),ArrayLoad(pc=147,UVar(defSites={49},value=an int),UVar(defSites={46},value={int[], null}[↦138;refId=111]))),
	51: Assignment(pc=150,DVar(useSites={52},value=int = 91,origin=51),IntConst(pc=150,91)),
	52: If(pc=152,UVar(defSites={50},value=an int),!=,UVar(defSites={51},value=int = 91),target=55),
	53: Assignment(pc=158,DVar(useSites={54},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦158;refId=119],origin=53),VirtualFunctionCall(pc=158,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate bitsOrSingle(java.util.regex.Pattern$BitClass,int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={-2},value={java.util.regex.Pattern$BitClass, null}[↦-2;refId=103]),UVar(defSites={0,35},value=int ∈ [0,2147483647])))),
	54: ReturnValue(pc=161,UVar(defSites={53},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦158;refId=119])),
	55: Assignment(pc=163,DVar(useSites={56},value=int = 93,origin=55),IntConst(pc=163,93)),
	56: If(pc=165,UVar(defSites={50},value=an int),==,UVar(defSites={55},value=int = 93),target=84),
	57: ExprStmt(pc=169,VirtualFunctionCall(pc=169,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	58: Assignment(pc=174,DVar(useSites={80,68,60,82,78},value=an int,origin=58),VirtualFunctionCall(pc=174,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	59: Assignment(pc=181,DVar(useSites={60},value=int = 92,origin=59),IntConst(pc=181,92)),
	60: If(pc=183,UVar(defSites={58},value=an int),!=,UVar(defSites={59},value=int = 92),target=66),
	61: Assignment(pc=187,DVar(useSites={64},value=int = 1,origin=61),IntConst(pc=187,1)),
	62: Assignment(pc=188,DVar(useSites={64},value=int = 0,origin=62),IntConst(pc=188,0)),
	63: Assignment(pc=189,DVar(useSites={64},value=int = 1,origin=63),IntConst(pc=189,1)),
	64: Assignment(pc=190,DVar(useSites={80,68,82,78},value=an int,origin=64),VirtualFunctionCall(pc=190,java.util.regex.Pattern,isInterface=false,int escape(boolean,boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={61},value=int = 1),UVar(defSites={62},value=int = 0),UVar(defSites={63},value=int = 1)))),
	65: Goto(pc=195,target=68),
	66: ExprStmt(pc=199,VirtualFunctionCall(pc=199,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	67: Nop(pc=202),
	68: If(pc=206,UVar(defSites={64,58},value=an int),>=,UVar(defSites={0,35},value=int ∈ [0,2147483647]),target=72),
	69: Assignment(pc=210,DVar(useSites={70},value=String("Illegal character range")[@210;refId=151],origin=69),StringConst(pc=210,Illegal character range)),
	70: Assignment(pc=212,DVar(useSites={71},value={_ <: java.util.regex.PatternSyntaxException, null}[↦212;refId=153],origin=70),VirtualFunctionCall(pc=212,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={69},value=String("Illegal character range")[@210;refId=151])))),
	71: Throw(pc=215,UVar(defSites={70},value={_ <: java.util.regex.PatternSyntaxException, null}[↦212;refId=153])),
	72: Assignment(pc=217,DVar(useSites={73},value=int = 2,origin=72),IntConst(pc=217,2)),
	73: Assignment(pc=218,DVar(useSites={74},value=int ∈ [0,1],origin=73),VirtualFunctionCall(pc=218,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={72},value=int = 2)))),
	74: If(pc=221,UVar(defSites={73},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=82),
	75: Assignment(pc=225,DVar(useSites={76},value=int = 64,origin=75),IntConst(pc=225,64)),
	76: Assignment(pc=227,DVar(useSites={77},value=int ∈ [0,1],origin=76),VirtualFunctionCall(pc=227,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={75},value=int = 64)))),
	77: If(pc=230,UVar(defSites={76},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=80),
	78: Assignment(pc=236,DVar(useSites={79},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦236;refId=146],origin=78),StaticFunctionCall(pc=236,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate CIRangeU(int,int),(UVar(defSites={0,35},value=int ∈ [0,2147483647]),UVar(defSites={64,58},value=int ∈ [0,2147483647])))),
	79: ReturnValue(pc=239,UVar(defSites={78},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦236;refId=146])),
	80: Assignment(pc=243,DVar(useSites={81},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦243;refId=148],origin=80),StaticFunctionCall(pc=243,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate CIRange(int,int),(UVar(defSites={0,35},value=int ∈ [0,2147483647]),UVar(defSites={64,58},value=int ∈ [0,2147483647])))),
	81: ReturnValue(pc=246,UVar(defSites={80},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦243;refId=148])),
	82: Assignment(pc=250,DVar(useSites={83},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦250;refId=150],origin=82),StaticFunctionCall(pc=250,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate Range(int,int),(UVar(defSites={0,35},value=int ∈ [0,2147483647]),UVar(defSites={64,58},value=int ∈ [0,2147483647])))),
	83: ReturnValue(pc=253,UVar(defSites={82},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦250;refId=150])),
	84: Assignment(pc=257,DVar(useSites={85},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦257;refId=142],origin=84),VirtualFunctionCall(pc=257,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate bitsOrSingle(java.util.regex.Pattern$BitClass,int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={-2},value={java.util.regex.Pattern$BitClass, null}[↦-2;refId=103]),UVar(defSites={0,35},value=int ∈ [0,2147483647])))),
	85: ReturnValue(pc=260,UVar(defSites={84},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦257;refId=142])),
	86: Assignment(pc=262,DVar(useSites={89,87},value=java.lang.StringBuilder[↦262;refId=120],origin=86),New(pc=262,java.lang.StringBuilder)),
	87: NonVirtualMethodCall(pc=266,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={86},value=java.lang.StringBuilder[↦262;refId=120]),()),
	88: Assignment(pc=269,DVar(useSites={89},value=String("Unexpected character '")[@269;refId=122],origin=88),StringConst(pc=269,Unexpected character ')),
	89: Assignment(pc=272,DVar(useSites={91},value={java.lang.StringBuilder, null}[↦272;refId=124],origin=89),VirtualFunctionCall(pc=272,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={86},value=java.lang.StringBuilder[↦262;refId=120]),(UVar(defSites={88},value=String("Unexpected character '")[@269;refId=122])))),
	90: Assignment(pc=276,DVar(useSites={91},value=int ∈ [0,65535],origin=90),PrimitiveTypecastExpr(pc=276,CharType,UVar(defSites={0,35},value=int ∈ [-2147483648,-1]))),
	91: Assignment(pc=277,DVar(useSites={93},value={java.lang.StringBuilder, null}[↦277;refId=127],origin=91),VirtualFunctionCall(pc=277,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={89},value={java.lang.StringBuilder, null}[↦272;refId=124]),(UVar(defSites={90},value=int ∈ [0,65535])))),
	92: Assignment(pc=280,DVar(useSites={93},value=String("'")[@280;refId=128],origin=92),StringConst(pc=280,')),
	93: Assignment(pc=282,DVar(useSites={94},value={java.lang.StringBuilder, null}[↦282;refId=131],origin=93),VirtualFunctionCall(pc=282,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={91},value={java.lang.StringBuilder, null}[↦277;refId=127]),(UVar(defSites={92},value=String("'")[@280;refId=128])))),
	94: Assignment(pc=285,DVar(useSites={95},value={java.lang.String, null}[↦285;refId=134],origin=94),VirtualFunctionCall(pc=285,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={93},value={java.lang.StringBuilder, null}[↦282;refId=131]),())),
	95: Assignment(pc=288,DVar(useSites={96},value={_ <: java.util.regex.PatternSyntaxException, null}[↦288;refId=136],origin=95),VirtualFunctionCall(pc=288,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={94},value={java.lang.String, null}[↦285;refId=134])))),
	96: Throw(pc=291,UVar(defSites={95},value={_ <: java.util.regex.PatternSyntaxException, null}[↦288;refId=136]))
),cfg=CFG(
	BB_0: BasicBlock(start=10,end=11) -> {BB_1a}
	BB_10: BasicBlock(start=74,end=74) -> {BB_32,BB_34}
	BB_11: BasicBlock(start=6,end=7) -> {BB_1e,BB_31}
	BB_12: BasicBlock(start=85,end=85) -> {BB_29}
	BB_13: BasicBlock(start=38,end=39) -> {BB_29}
	BB_14: BasicBlock(start=21,end=21) -> {BB_29}
	BB_15: BasicBlock(start=33,end=35) -> {BB_3b,BB_35}
	BB_16: BasicBlock(start=92,end=93) -> {BB_3b,BB_3a}
	BB_17: BasicBlock(start=65,end=65) -> {BB_3d}
	BB_18: BasicBlock(start=77,end=77) -> {BB_27,BB_c}
	BB_19: BasicBlock(start=96,end=96) -> {BB_3b}
	BB_1: BasicBlock(start=42,end=42) -> {BB_2e,BB_25}
	BB_1a: BasicBlock(start=13,end=14) -> {BB_3b,BB_3c}
	BB_1b: BasicBlock(start=41,end=41) -> {BB_1}
	BB_1c: BasicBlock(start=32,end=32) -> {BB_3b,BB_15}
	BB_1d: BasicBlock(start=17,end=17) -> {BB_3b,BB_28}
	BB_1e: BasicBlock(start=22,end=26) -> {BB_3b,BB_21}
	BB_1f: BasicBlock(start=44,end=45) -> {BB_2,BB_a}
	BB_20: BasicBlock(start=59,end=60) -> {BB_e,BB_5}
	BB_21: BasicBlock(start=27,end=28) -> {BB_d,BB_2c}
	BB_22: BasicBlock(start=71,end=71) -> {BB_3b}
	BB_23: BasicBlock(start=12,end=12) -> {BB_1a}
	BB_24: BasicBlock(start=54,end=54) -> {BB_29}
	BB_25: BasicBlock(start=86,end=87) -> {BB_3b,BB_8}
	BB_26: BasicBlock(start=3,end=3) -> {BB_3b,BB_38}
	BB_27: BasicBlock(start=80,end=80) -> {BB_3b,BB_4}
	BB_28: BasicBlock(start=18,end=18) -> {BB_9}
	BB_29: ExitNode(normalReturn=true)
	BB_2: BasicBlock(start=84,end=84) -> {BB_3b,BB_12}
	BB_2a: BasicBlock(start=95,end=95) -> {BB_3b,BB_19}
	BB_2b: BasicBlock(start=67,end=67) -> {BB_3d}
	BB_2c: BasicBlock(start=31,end=31) -> {BB_1c}
	BB_2d: BasicBlock(start=72,end=73) -> {BB_3b,BB_10}
	BB_2e: BasicBlock(start=43,end=43) -> {BB_3b,BB_1f}
	BB_2f: BasicBlock(start=40,end=40) -> {BB_3b,BB_1b}
	BB_30: BasicBlock(start=55,end=56) -> {BB_b,BB_2}
	BB_31: BasicBlock(start=8,end=9) -> {BB_0,BB_23}
	BB_32: BasicBlock(start=75,end=76) -> {BB_3b,BB_18}
	BB_33: BasicBlock(start=58,end=58) -> {BB_3b,BB_20}
	BB_34: BasicBlock(start=82,end=82) -> {BB_3b,BB_3f}
	BB_35: BasicBlock(start=36,end=37) -> {BB_1,BB_13}
	BB_36: BasicBlock(start=51,end=52) -> {BB_30,BB_3}
	BB_37: BasicBlock(start=19,end=19) -> {BB_9}
	BB_38: BasicBlock(start=4,end=5) -> {BB_31,BB_11}
	BB_39: BasicBlock(start=79,end=79) -> {BB_29}
	BB_3: BasicBlock(start=53,end=53) -> {BB_3b,BB_24}
	BB_3a: BasicBlock(start=94,end=94) -> {BB_3b,BB_2a}
	BB_3b: ExitNode(normalReturn=false)
	BB_3c: BasicBlock(start=15,end=16) -> {BB_1d,BB_37}
	BB_3d: BasicBlock(start=68,end=68) -> {BB_2d,BB_6}
	BB_3e: BasicBlock(start=90,end=91) -> {BB_3b,BB_16}
	BB_3f: BasicBlock(start=83,end=83) -> {BB_29}
	BB_4: BasicBlock(start=81,end=81) -> {BB_29}
	BB_5: BasicBlock(start=66,end=66) -> {BB_3b,BB_2b}
	BB_6: BasicBlock(start=69,end=70) -> {BB_3b,BB_22}
	BB_7: BasicBlock(start=0,end=0) -> {BB_3b,BB_f}
	BB_8: BasicBlock(start=88,end=89) -> {BB_3b,BB_3e}
	BB_9: BasicBlock(start=20,end=20) -> {BB_3b,BB_14}
	BB_a: BasicBlock(start=46,end=50) -> {BB_3b,BB_36}
	BB_b: BasicBlock(start=57,end=57) -> {BB_3b,BB_33}
	BB_c: BasicBlock(start=78,end=78) -> {BB_3b,BB_39}
	BB_d: BasicBlock(start=29,end=30) -> {BB_1c}
	BB_e: BasicBlock(start=61,end=64) -> {BB_3b,BB_17}
	BB_f: BasicBlock(start=1,end=2) -> {BB_26,BB_2f}
))

boolean lambda$ALL$4(int)
AITACode(params=(Parameters(
	1: useSites={} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value=int = 1,origin=0),IntConst(pc=0,1)),
	1: ReturnValue(pc=1,UVar(defSites={0},value=int = 1))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

void normalizeSlice(java.lang.String,int,int,java.lang.StringBuilder)
AITACode(params=(Parameters(
	1: useSites={0,14,17,9,29,3,35} (origin=-2),
	2: useSites={16,8,24,12,2,6,14,17,9,3,35,11,27} (origin=-3),
	3: useSites={16,8,28,2,9} (origin=-4),
	4: useSites={56,84,60,54,14,62,9,101,53,99,59,23} (origin=-5)
)),stmts=(
	0: ExprStmt(pc=1,VirtualFunctionCall(pc=1,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),())),
	1: Nop(pc=4),
	2: If(pc=11,UVar(defSites={6,-3},value=an int),>=,UVar(defSites={-4},value=an int),target=8),
	3: Assignment(pc=16,DVar(useSites={4},value=int ∈ [0,65535],origin=3),VirtualFunctionCall(pc=16,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={6,-3},value=int ∈ [-2147483648,2147483646])))),
	4: Assignment(pc=19,DVar(useSites={5},value=int ∈ [0,1],origin=4),StaticFunctionCall(pc=19,java.util.regex.ASCII,isInterface=false,boolean isAscii(int),(UVar(defSites={3},value=int ∈ [0,65535])))),
	5: If(pc=22,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=8),
	6: Assignment(pc=25,DVar(useSites={8,2,3,11,7},value=int ∈ [-2147483647,2147483647],origin=6),BinaryExpr(pc=25,ComputationalTypeInt,UVar(defSites={6,-3},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=25,1))),
	7: Goto(pc=28,target=2),
	8: If(pc=33,UVar(defSites={6,-3},value=an int),!=,UVar(defSites={-4},value=an int),target=11),
	9: ExprStmt(pc=41,VirtualFunctionCall(pc=41,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.CharSequence,int,int),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value=an int)))),
	10: Return(pc=45),
	11: Assignment(pc=46,DVar(useSites={16,24,12,14,17,35,27},value=an int,origin=11),BinaryExpr(pc=46,ComputationalTypeInt,UVar(defSites={6,-3},value=an int),+,IntConst(pc=46,-1))),
	12: If(pc=52,UVar(defSites={11},value=an int),>=,UVar(defSites={-3},value=an int),target=14),
	13: Goto(pc=58,target=16),
	14: ExprStmt(pc=66,VirtualFunctionCall(pc=66,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.CharSequence,int,int),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),UVar(defSites={-3},value=an int),UVar(defSites={11},value=an int)))),
	15: Nop(pc=69),
	16: If(pc=72,UVar(defSites={24,33,-3,11,27},value=an int),>=,UVar(defSites={-4},value=an int),target=103),
	17: Assignment(pc=77,DVar(useSites={26,22,30,19},value=an int,origin=17),VirtualFunctionCall(pc=77,java.lang.String,isInterface=false,int codePointAt(int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={24,33,-3,11,27},value=int ∈ [-2147483648,2147483646])))),
	18: Assignment(pc=82,DVar(useSites={19},value=String(".$|()[]{}^?*+\")[@82;refId=117],origin=18),StringConst(pc=82,.$|()[]{}^?*+\)),
	19: Assignment(pc=86,DVar(useSites={21},value=an int,origin=19),VirtualFunctionCall(pc=86,java.lang.String,isInterface=false,int indexOf(int),UVar(defSites={18},value=String(".$|()[]{}^?*+\")[@82;refId=117]),(UVar(defSites={17},value=an int)))),
	20: Assignment(pc=89,DVar(useSites={21},value=int = -1,origin=20),IntConst(pc=89,-1)),
	21: If(pc=90,UVar(defSites={19},value=an int),==,UVar(defSites={20},value=int = -1),target=26),
	22: Assignment(pc=96,DVar(useSites={23},value=int ∈ [0,65535],origin=22),PrimitiveTypecastExpr(pc=96,CharType,UVar(defSites={17},value=an int))),
	23: ExprStmt(pc=97,VirtualFunctionCall(pc=97,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={22},value=int ∈ [0,65535])))),
	24: Assignment(pc=101,DVar(useSites={16,17,25,35,27},value=int ∈ [-2147483647,2147483647],origin=24),BinaryExpr(pc=101,ComputationalTypeInt,UVar(defSites={24,33,-3,11,27},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=101,1))),
	25: Goto(pc=104,target=16),
	26: Assignment(pc=110,DVar(useSites={27},value=an int,origin=26),StaticFunctionCall(pc=110,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={17},value=an int)))),
	27: Assignment(pc=113,DVar(useSites={16,24,28,33,17,29,35},value=an int,origin=27),BinaryExpr(pc=113,ComputationalTypeInt,UVar(defSites={24,33,-3,11,27},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={26},value=an int))),
	28: If(pc=119,UVar(defSites={33,27},value=an int),>=,UVar(defSites={-4},value=int ∈ [-2147483647,2147483647]),target=35),
	29: Assignment(pc=125,DVar(useSites={32,30},value=an int,origin=29),VirtualFunctionCall(pc=125,java.lang.String,isInterface=false,int codePointAt(int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={33,27},value=int ∈ [-2147483648,2147483646])))),
	30: Assignment(pc=134,DVar(useSites={31},value=int ∈ [0,1],origin=30),StaticFunctionCall(pc=134,java.util.regex.Grapheme,isInterface=false,boolean isBoundary(int,int),(UVar(defSites={17,29},value=an int),UVar(defSites={29},value=an int)))),
	31: If(pc=137,UVar(defSites={30},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=35),
	32: Assignment(pc=151,DVar(useSites={33},value=an int,origin=32),StaticFunctionCall(pc=151,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={29},value=an int)))),
	33: Assignment(pc=154,DVar(useSites={16,24,28,34,17,29,35,27},value=an int,origin=33),BinaryExpr(pc=154,ComputationalTypeInt,UVar(defSites={33,27},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={32},value=an int))),
	34: Goto(pc=157,target=28),
	35: Assignment(pc=164,DVar(useSites={92,66,50,74,86,65,37,101},value={java.lang.String, null}[↦164;refId=133],origin=35),VirtualFunctionCall(pc=164,java.lang.String,isInterface=false,java.lang.String substring(int,int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={24,33,-3,11,27},value=int ∈ [-2147483648,2147483646]),UVar(defSites={33,27},value=an int)))),
	36: Assignment(pc=171,DVar(useSites={37},value={java.text.Normalizer$Form, null}[↦171;refId=134],origin=36),GetStatic(pc=171,java.text.Normalizer$Form,NFD,java.text.Normalizer$Form)),
	37: Assignment(pc=174,DVar(useSites={68,44,42,38,86,77,51,95},value={java.lang.String, null}[↦174;refId=136],origin=37),StaticFunctionCall(pc=174,java.text.Normalizer,isInterface=false,java.lang.String normalize(java.lang.CharSequence,java.text.Normalizer$Form),(UVar(defSites={35},value={java.lang.String, null}[↦164;refId=133]),UVar(defSites={36},value={java.text.Normalizer$Form, null}[↦171;refId=134])))),
	38: Assignment(pc=184,DVar(useSites={40},value=an int,origin=38),VirtualFunctionCall(pc=184,java.lang.String,isInterface=false,int length(),UVar(defSites={37},value={java.lang.String, null}[↦174;refId=136]),())),
	39: Assignment(pc=187,DVar(useSites={40},value=int = 1,origin=39),IntConst(pc=187,1)),
	40: If(pc=188,UVar(defSites={38},value=an int),<=,UVar(defSites={39},value=int = 1),target=64),
	41: Assignment(pc=193,DVar(useSites={42},value=int = 0,origin=41),IntConst(pc=193,0)),
	42: Assignment(pc=194,DVar(useSites={43},value=an int,origin=42),VirtualFunctionCall(pc=194,java.lang.String,isInterface=false,int codePointAt(int),UVar(defSites={37},value=java.lang.String[↦174;refId=136]),(UVar(defSites={41},value=int = 0)))),
	43: Assignment(pc=203,DVar(useSites={44},value=an int,origin=43),StaticFunctionCall(pc=203,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={42},value=an int)))),
	44: Assignment(pc=206,DVar(useSites={45},value=an int,origin=44),VirtualFunctionCall(pc=206,java.lang.String,isInterface=false,int codePointAt(int),UVar(defSites={37},value=java.lang.String[↦174;refId=136]),(UVar(defSites={43},value=an int)))),
	45: Assignment(pc=213,DVar(useSites={47},value=an int,origin=45),StaticFunctionCall(pc=213,java.lang.Character,isInterface=false,int getType(int),(UVar(defSites={44},value=an int)))),
	46: Assignment(pc=216,DVar(useSites={47},value=int = 6,origin=46),IntConst(pc=216,6)),
	47: If(pc=218,UVar(defSites={45},value=an int),!=,UVar(defSites={46},value=int = 6),target=64),
	48: Assignment(pc=221,DVar(useSites={50,49,51,55},value=java.util.LinkedHashSet[↦221;refId=143],origin=48),New(pc=221,java.util.LinkedHashSet)),
	49: NonVirtualMethodCall(pc=225,java.util.LinkedHashSet,isInterface=false,void <init>(),UVar(defSites={48},value=java.util.LinkedHashSet[↦221;refId=143]),()),
	50: ExprStmt(pc=234,VirtualFunctionCall(pc=234,java.util.Set,isInterface=true,boolean add(java.lang.Object),UVar(defSites={48},value=java.util.LinkedHashSet[↦221;refId=143]),(UVar(defSites={35},value={java.lang.String, null}[↦164;refId=133])))),
	51: StaticMethodCall(pc=244,java.util.regex.Pattern,isInterface=false,void produceEquivalentAlternation(java.lang.String,java.util.Set),(UVar(defSites={37},value=java.lang.String[↦174;refId=136]),UVar(defSites={48},value=java.util.LinkedHashSet[↦221;refId=143]))),
	52: Assignment(pc=248,DVar(useSites={53},value=String("(?:")[@248;refId=147],origin=52),StringConst(pc=248,(?:)),
	53: ExprStmt(pc=250,VirtualFunctionCall(pc=250,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={52},value=String("(?:")[@248;refId=147])))),
	54: Assignment(pc=257,DVar(useSites={55},value={_ <: java.util.regex.Pattern$normalizeSlice(Ljava$lang$String:IILjava$lang$StringBuilder:)V:257$Lambda, null}[↦257;refId=152],origin=54),StaticFunctionCall(pc=257,java.util.regex.Pattern$normalizeSlice(Ljava$lang$String:IILjava$lang$StringBuilder:)V:257$Lambda,isInterface=false,java.util.regex.Pattern$normalizeSlice(Ljava$lang$String:IILjava$lang$StringBuilder:)V:257$Lambda $newInstance(java.lang.StringBuilder),(UVar(defSites={-5},value=java.lang.StringBuilder[↦-4;refId=103])))),
	55: VirtualMethodCall(pc=262,java.util.Set,isInterface=true,void forEach(java.util.function.Consumer),UVar(defSites={48},value=java.util.LinkedHashSet[↦221;refId=143]),(UVar(defSites={54},value={_ <: java.util.regex.Pattern$normalizeSlice(Ljava$lang$String:IILjava$lang$StringBuilder:)V:257$Lambda, null}[↦257;refId=152]))),
	56: Assignment(pc=269,DVar(useSites={58},value=an int,origin=56),VirtualFunctionCall(pc=269,java.lang.StringBuilder,isInterface=false,int length(),UVar(defSites={-5},value=java.lang.StringBuilder[↦-4;refId=103]),())),
	57: Assignment(pc=272,DVar(useSites={58},value=int = 1,origin=57),IntConst(pc=272,1)),
	58: Assignment(pc=273,DVar(useSites={60},value=an int,origin=58),BinaryExpr(pc=273,ComputationalTypeInt,UVar(defSites={56},value=an int),-,UVar(defSites={57},value=int = 1))),
	59: Assignment(pc=275,DVar(useSites={60},value=an int,origin=59),VirtualFunctionCall(pc=275,java.lang.StringBuilder,isInterface=false,int length(),UVar(defSites={-5},value=java.lang.StringBuilder[↦-4;refId=103]),())),
	60: ExprStmt(pc=278,VirtualFunctionCall(pc=278,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder delete(int,int),UVar(defSites={-5},value=java.lang.StringBuilder[↦-4;refId=103]),(UVar(defSites={58},value=an int),UVar(defSites={59},value=an int)))),
	61: Assignment(pc=283,DVar(useSites={62},value=String(")")[@283;refId=158],origin=61),StringConst(pc=283,))),
	62: ExprStmt(pc=285,VirtualFunctionCall(pc=285,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={-5},value=java.lang.StringBuilder[↦-4;refId=103]),(UVar(defSites={61},value=String(")")[@283;refId=158])))),
	63: Goto(pc=289,target=16),
	64: Assignment(pc=294,DVar(useSites={65},value={java.text.Normalizer$Form, null}[↦294;refId=161],origin=64),GetStatic(pc=294,java.text.Normalizer$Form,NFC,java.text.Normalizer$Form)),
	65: Assignment(pc=297,DVar(useSites={80,68,66},value={java.lang.String, null}[↦297;refId=163],origin=65),StaticFunctionCall(pc=297,java.text.Normalizer,isInterface=false,java.lang.String normalize(java.lang.CharSequence,java.text.Normalizer$Form),(UVar(defSites={35},value={java.lang.String, null}[↦164;refId=133]),UVar(defSites={64},value={java.text.Normalizer$Form, null}[↦294;refId=161])))),
	66: Assignment(pc=306,DVar(useSites={67},value=int ∈ [0,1],origin=66),VirtualFunctionCall(pc=306,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={35},value={java.lang.String, null}[↦164;refId=133]),(UVar(defSites={65},value={java.lang.String, null}[↦297;refId=163])))),
	67: If(pc=309,UVar(defSites={66},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=86),
	68: Assignment(pc=316,DVar(useSites={69},value=int ∈ [0,1],origin=68),VirtualFunctionCall(pc=316,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={37},value=java.lang.String[↦174;refId=136]),(UVar(defSites={65},value={java.lang.String, null}[↦297;refId=163])))),
	69: If(pc=319,UVar(defSites={68},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=86),
	70: Assignment(pc=323,DVar(useSites={73,71},value=java.lang.StringBuilder[↦323;refId=167],origin=70),New(pc=323,java.lang.StringBuilder)),
	71: NonVirtualMethodCall(pc=327,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={70},value=java.lang.StringBuilder[↦323;refId=167]),()),
	72: Assignment(pc=330,DVar(useSites={73},value=String("(?:")[@330;refId=169],origin=72),StringConst(pc=330,(?:)),
	73: Assignment(pc=332,DVar(useSites={74},value={java.lang.StringBuilder, null}[↦332;refId=171],origin=73),VirtualFunctionCall(pc=332,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={70},value=java.lang.StringBuilder[↦323;refId=167]),(UVar(defSites={72},value=String("(?:")[@330;refId=169])))),
	74: Assignment(pc=337,DVar(useSites={76},value={java.lang.StringBuilder, null}[↦337;refId=174],origin=74),VirtualFunctionCall(pc=337,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={73},value={java.lang.StringBuilder, null}[↦332;refId=171]),(UVar(defSites={35},value=java.lang.String[↦164;refId=133])))),
	75: Assignment(pc=340,DVar(useSites={76},value=String("|")[@340;refId=175],origin=75),StringConst(pc=340,|)),
	76: Assignment(pc=342,DVar(useSites={77},value={java.lang.StringBuilder, null}[↦342;refId=178],origin=76),VirtualFunctionCall(pc=342,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={74},value={java.lang.StringBuilder, null}[↦337;refId=174]),(UVar(defSites={75},value=String("|")[@340;refId=175])))),
	77: Assignment(pc=347,DVar(useSites={79},value={java.lang.StringBuilder, null}[↦347;refId=181],origin=77),VirtualFunctionCall(pc=347,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={76},value={java.lang.StringBuilder, null}[↦342;refId=178]),(UVar(defSites={37},value=java.lang.String[↦174;refId=136])))),
	78: Assignment(pc=350,DVar(useSites={79},value=String("|")[@350;refId=182],origin=78),StringConst(pc=350,|)),
	79: Assignment(pc=352,DVar(useSites={80},value={java.lang.StringBuilder, null}[↦352;refId=185],origin=79),VirtualFunctionCall(pc=352,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={77},value={java.lang.StringBuilder, null}[↦347;refId=181]),(UVar(defSites={78},value=String("|")[@350;refId=182])))),
	80: Assignment(pc=357,DVar(useSites={82},value={java.lang.StringBuilder, null}[↦357;refId=188],origin=80),VirtualFunctionCall(pc=357,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={79},value={java.lang.StringBuilder, null}[↦352;refId=185]),(UVar(defSites={65},value={java.lang.String, null}[↦297;refId=163])))),
	81: Assignment(pc=360,DVar(useSites={82},value=String(")")[@360;refId=189],origin=81),StringConst(pc=360,))),
	82: Assignment(pc=362,DVar(useSites={83},value={java.lang.StringBuilder, null}[↦362;refId=192],origin=82),VirtualFunctionCall(pc=362,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={80},value={java.lang.StringBuilder, null}[↦357;refId=188]),(UVar(defSites={81},value=String(")")[@360;refId=189])))),
	83: Assignment(pc=365,DVar(useSites={84},value={java.lang.String, null}[↦365;refId=195],origin=83),VirtualFunctionCall(pc=365,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={82},value={java.lang.StringBuilder, null}[↦362;refId=192]),())),
	84: ExprStmt(pc=368,VirtualFunctionCall(pc=368,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={83},value={java.lang.String, null}[↦365;refId=195])))),
	85: Goto(pc=372,target=16),
	86: Assignment(pc=379,DVar(useSites={87},value=int ∈ [0,1],origin=86),VirtualFunctionCall(pc=379,java.lang.String,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={35},value=java.lang.String[↦164;refId=133]),(UVar(defSites={37},value=java.lang.String[↦174;refId=136])))),
	87: If(pc=382,UVar(defSites={86},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=101),
	88: Assignment(pc=386,DVar(useSites={89,91},value=java.lang.StringBuilder[↦386;refId=200],origin=88),New(pc=386,java.lang.StringBuilder)),
	89: NonVirtualMethodCall(pc=390,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={88},value=java.lang.StringBuilder[↦386;refId=200]),()),
	90: Assignment(pc=393,DVar(useSites={91},value=String("(?:")[@393;refId=202],origin=90),StringConst(pc=393,(?:)),
	91: Assignment(pc=395,DVar(useSites={92},value={java.lang.StringBuilder, null}[↦395;refId=204],origin=91),VirtualFunctionCall(pc=395,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={88},value=java.lang.StringBuilder[↦386;refId=200]),(UVar(defSites={90},value=String("(?:")[@393;refId=202])))),
	92: Assignment(pc=400,DVar(useSites={94},value={java.lang.StringBuilder, null}[↦400;refId=207],origin=92),VirtualFunctionCall(pc=400,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={91},value={java.lang.StringBuilder, null}[↦395;refId=204]),(UVar(defSites={35},value=java.lang.String[↦164;refId=133])))),
	93: Assignment(pc=403,DVar(useSites={94},value=String("|")[@403;refId=208],origin=93),StringConst(pc=403,|)),
	94: Assignment(pc=405,DVar(useSites={95},value={java.lang.StringBuilder, null}[↦405;refId=211],origin=94),VirtualFunctionCall(pc=405,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={92},value={java.lang.StringBuilder, null}[↦400;refId=207]),(UVar(defSites={93},value=String("|")[@403;refId=208])))),
	95: Assignment(pc=410,DVar(useSites={97},value={java.lang.StringBuilder, null}[↦410;refId=214],origin=95),VirtualFunctionCall(pc=410,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={94},value={java.lang.StringBuilder, null}[↦405;refId=211]),(UVar(defSites={37},value=java.lang.String[↦174;refId=136])))),
	96: Assignment(pc=413,DVar(useSites={97},value=String(")")[@413;refId=215],origin=96),StringConst(pc=413,))),
	97: Assignment(pc=415,DVar(useSites={98},value={java.lang.StringBuilder, null}[↦415;refId=218],origin=97),VirtualFunctionCall(pc=415,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={95},value={java.lang.StringBuilder, null}[↦410;refId=214]),(UVar(defSites={96},value=String(")")[@413;refId=215])))),
	98: Assignment(pc=418,DVar(useSites={99},value={java.lang.String, null}[↦418;refId=221],origin=98),VirtualFunctionCall(pc=418,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={97},value={java.lang.StringBuilder, null}[↦415;refId=218]),())),
	99: ExprStmt(pc=421,VirtualFunctionCall(pc=421,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={98},value={java.lang.String, null}[↦418;refId=221])))),
	100: Goto(pc=425,target=16),
	101: ExprStmt(pc=431,VirtualFunctionCall(pc=431,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={-5},value={java.lang.StringBuilder, null}[↦-4;refId=103]),(UVar(defSites={35},value=java.lang.String[↦164;refId=133])))),
	102: Goto(pc=435,target=16),
	103: Return(pc=438)
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=5) -> {BB_17,BB_44}
	BB_10: BasicBlock(start=93,end=94) -> {BB_4a,BB_38}
	BB_11: BasicBlock(start=57,end=59) -> {BB_4a,BB_18}
	BB_12: BasicBlock(start=78,end=79) -> {BB_4a,BB_32}
	BB_13: BasicBlock(start=29,end=29) -> {BB_4a,BB_47}
	BB_14: BasicBlock(start=61,end=62) -> {BB_4a,BB_35}
	BB_15: BasicBlock(start=1,end=1) -> {BB_5}
	BB_16: BasicBlock(start=74,end=74) -> {BB_4a,BB_45}
	BB_17: BasicBlock(start=6,end=7) -> {BB_5}
	BB_18: BasicBlock(start=60,end=60) -> {BB_4a,BB_14}
	BB_19: BasicBlock(start=85,end=85) -> {BB_3b}
	BB_1: BasicBlock(start=24,end=25) -> {BB_3b}
	BB_1a: BasicBlock(start=102,end=102) -> {BB_3b}
	BB_1b: BasicBlock(start=70,end=71) -> {BB_4a,BB_3e}
	BB_1c: BasicBlock(start=33,end=34) -> {BB_1d}
	BB_1d: BasicBlock(start=28,end=28) -> {BB_33,BB_13}
	BB_1e: BasicBlock(start=38,end=38) -> {BB_4a,BB_2d}
	BB_1f: BasicBlock(start=77,end=77) -> {BB_4a,BB_12}
	BB_20: BasicBlock(start=96,end=97) -> {BB_4a,BB_2e}
	BB_21: BasicBlock(start=13,end=13) -> {BB_3b}
	BB_22: BasicBlock(start=41,end=42) -> {BB_4a,BB_3f}
	BB_23: BasicBlock(start=32,end=32) -> {BB_4a,BB_1c}
	BB_24: BasicBlock(start=45,end=45) -> {BB_4a,BB_f}
	BB_25: BasicBlock(start=64,end=65) -> {BB_4a,BB_30}
	BB_26: BasicBlock(start=17,end=17) -> {BB_4a,BB_36}
	BB_27: BasicBlock(start=22,end=23) -> {BB_4a,BB_1}
	BB_28: BasicBlock(start=44,end=44) -> {BB_4a,BB_24}
	BB_29: BasicBlock(start=27,end=27) -> {BB_1d}
	BB_2: BasicBlock(start=84,end=84) -> {BB_4a,BB_19}
	BB_2a: BasicBlock(start=54,end=54) -> {BB_4a,BB_43}
	BB_2b: BasicBlock(start=86,end=86) -> {BB_4a,BB_41}
	BB_2c: BasicBlock(start=81,end=82) -> {BB_4a,BB_4e}
	BB_2d: BasicBlock(start=39,end=40) -> {BB_25,BB_22}
	BB_2e: BasicBlock(start=98,end=98) -> {BB_4a,BB_40}
	BB_2f: BasicBlock(start=103,end=103) -> {BB_37}
	BB_30: BasicBlock(start=66,end=66) -> {BB_4a,BB_3a}
	BB_31: BasicBlock(start=3,end=3) -> {BB_4a,BB_49}
	BB_32: BasicBlock(start=80,end=80) -> {BB_4a,BB_2c}
	BB_33: BasicBlock(start=35,end=35) -> {BB_4a,BB_46}
	BB_34: BasicBlock(start=48,end=49) -> {BB_4a,BB_39}
	BB_35: BasicBlock(start=63,end=63) -> {BB_3b}
	BB_36: BasicBlock(start=18,end=19) -> {BB_4a,BB_e}
	BB_37: ExitNode(normalReturn=true)
	BB_38: BasicBlock(start=95,end=95) -> {BB_4a,BB_20}
	BB_39: BasicBlock(start=50,end=50) -> {BB_4a,BB_48}
	BB_3: BasicBlock(start=92,end=92) -> {BB_4a,BB_10}
	BB_3a: BasicBlock(start=67,end=67) -> {BB_4c,BB_2b}
	BB_3b: BasicBlock(start=16,end=16) -> {BB_2f,BB_26}
	BB_3c: BasicBlock(start=31,end=31) -> {BB_33,BB_23}
	BB_3d: BasicBlock(start=11,end=12) -> {BB_d,BB_21}
	BB_3e: BasicBlock(start=72,end=73) -> {BB_4a,BB_16}
	BB_3f: BasicBlock(start=43,end=43) -> {BB_4a,BB_28}
	BB_40: BasicBlock(start=99,end=99) -> {BB_4a,BB_4f}
	BB_41: BasicBlock(start=87,end=87) -> {BB_7,BB_9}
	BB_42: BasicBlock(start=26,end=26) -> {BB_4a,BB_29}
	BB_43: BasicBlock(start=55,end=55) -> {BB_4a,BB_b}
	BB_44: BasicBlock(start=8,end=8) -> {BB_4,BB_3d}
	BB_45: BasicBlock(start=75,end=76) -> {BB_4a,BB_1f}
	BB_46: BasicBlock(start=36,end=37) -> {BB_4a,BB_1e}
	BB_47: BasicBlock(start=30,end=30) -> {BB_4a,BB_3c}
	BB_48: BasicBlock(start=51,end=51) -> {BB_4a,BB_c}
	BB_49: BasicBlock(start=4,end=4) -> {BB_4a,BB_0}
	BB_4: BasicBlock(start=9,end=9) -> {BB_4a,BB_a}
	BB_4a: ExitNode(normalReturn=false)
	BB_4b: BasicBlock(start=15,end=15) -> {BB_3b}
	BB_4c: BasicBlock(start=68,end=68) -> {BB_4a,BB_6}
	BB_4d: BasicBlock(start=90,end=91) -> {BB_4a,BB_3}
	BB_4e: BasicBlock(start=83,end=83) -> {BB_4a,BB_2}
	BB_4f: BasicBlock(start=100,end=100) -> {BB_3b}
	BB_5: BasicBlock(start=2,end=2) -> {BB_31,BB_44}
	BB_6: BasicBlock(start=69,end=69) -> {BB_1b,BB_2b}
	BB_7: BasicBlock(start=101,end=101) -> {BB_4a,BB_1a}
	BB_8: BasicBlock(start=0,end=0) -> {BB_4a,BB_15}
	BB_9: BasicBlock(start=88,end=89) -> {BB_4a,BB_4d}
	BB_a: BasicBlock(start=10,end=10) -> {BB_37}
	BB_b: BasicBlock(start=56,end=56) -> {BB_4a,BB_11}
	BB_c: BasicBlock(start=52,end=53) -> {BB_4a,BB_2a}
	BB_d: BasicBlock(start=14,end=14) -> {BB_4a,BB_4b}
	BB_e: BasicBlock(start=20,end=21) -> {BB_27,BB_42}
	BB_f: BasicBlock(start=46,end=47) -> {BB_25,BB_34}
))

void RemoveQEQuoting()
AITACode(params=(Parameters(
	0: useSites={0,38,73,105,5,109,99,11,87,31} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={20,97,25,37,3},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={96,80,4,68,60,66,34,82,6,70,46,17,9,105,69,21,53,13,45,61,51,107,27,23,95},value=int = 0,origin=1),IntConst(pc=5,0)),
	2: Assignment(pc=9,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=9,1)),
	3: Assignment(pc=10,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=10,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={2},value=int = 1))),
	4: If(pc=11,UVar(defSites={1,17,9},value=an int),>=,UVar(defSites={3},value=an int),target=19),
	5: Assignment(pc=15,DVar(useSites={6},value={int[], null}[↦15;refId=579],origin=5),GetField(pc=15,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	6: Assignment(pc=19,DVar(useSites={8},value=an int,origin=6),ArrayLoad(pc=19,UVar(defSites={1,17,9},value=int ∈ [-2147483648,2147483646]),UVar(defSites={5},value={int[], null}[↦15;refId=579]))),
	7: Assignment(pc=20,DVar(useSites={8},value=int = 92,origin=7),IntConst(pc=20,92)),
	8: If(pc=22,UVar(defSites={6},value=an int),==,UVar(defSites={7},value=int = 92),target=11),
	9: Assignment(pc=25,DVar(useSites={96,80,4,68,60,66,34,82,10,6,70,46,17,105,69,21,53,13,45,61,51,107,27,23,95},value=int ∈ [-2147483647,2147483647],origin=9),BinaryExpr(pc=25,ComputationalTypeInt,UVar(defSites={1,17,9},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=25,1))),
	10: Goto(pc=28,target=2),
	11: Assignment(pc=32,DVar(useSites={14},value={int[], null}[↦32;refId=582],origin=11),GetField(pc=32,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	12: Assignment(pc=36,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=36,1)),
	13: Assignment(pc=37,DVar(useSites={14},value=int ∈ [-2147483647,2147483647],origin=13),BinaryExpr(pc=37,ComputationalTypeInt,UVar(defSites={1,17,9},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={12},value=int = 1))),
	14: Assignment(pc=38,DVar(useSites={16},value=an int,origin=14),ArrayLoad(pc=38,UVar(defSites={13},value=int ∈ [-2147483647,2147483647]),UVar(defSites={11},value={int[], null}[↦32;refId=582]))),
	15: Assignment(pc=39,DVar(useSites={16},value=int = 81,origin=15),IntConst(pc=39,81)),
	16: If(pc=41,UVar(defSites={14},value=an int),==,UVar(defSites={15},value=int = 81),target=19),
	17: Assignment(pc=44,DVar(useSites={96,80,4,68,60,66,34,18,82,6,70,46,9,105,69,21,53,13,45,61,51,107,27,23,95},value=an int,origin=17),BinaryExpr(pc=44,ComputationalTypeInt,UVar(defSites={1,17,9},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=44,2))),
	18: Goto(pc=47,target=2),
	19: Assignment(pc=52,DVar(useSites={20},value=int = 1,origin=19),IntConst(pc=52,1)),
	20: Assignment(pc=53,DVar(useSites={21},value=an int,origin=20),BinaryExpr(pc=53,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={19},value=int = 1))),
	21: If(pc=54,UVar(defSites={1,17,9},value=an int),<,UVar(defSites={20},value=an int),target=23),
	22: Return(pc=57),
	23: Assignment(pc=60,DVar(useSites={40,25,37,39},value=an int,origin=23),BinaryExpr(pc=60,ComputationalTypeInt,UVar(defSites={1,17,9},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=60,2))),
	24: Assignment(pc=64,DVar(useSites={26},value=int = 3,origin=24),IntConst(pc=64,3)),
	25: Assignment(pc=67,DVar(useSites={26},value=an int,origin=25),BinaryExpr(pc=67,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={23},value=an int))),
	26: Assignment(pc=68,DVar(useSites={27},value=an int,origin=26),BinaryExpr(pc=68,ComputationalTypeInt,UVar(defSites={24},value=int = 3),*,UVar(defSites={25},value=an int))),
	27: Assignment(pc=69,DVar(useSites={29},value=an int,origin=27),BinaryExpr(pc=69,ComputationalTypeInt,UVar(defSites={1,17,9},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={26},value=an int))),
	28: Assignment(pc=70,DVar(useSites={29},value=int = 2,origin=28),IntConst(pc=70,2)),
	29: Assignment(pc=71,DVar(useSites={30},value=an int,origin=29),BinaryExpr(pc=71,ComputationalTypeInt,UVar(defSites={27},value=an int),+,UVar(defSites={28},value=int = 2))),
	30: Assignment(pc=72,DVar(useSites={96,56,68,108,34,82,70,102,46,85,53,61,59},value=int[][↦72;refId=610],origin=30),NewArray(pc=72,[UVar(defSites={29},value=an int)],int[])),
	31: Assignment(pc=77,DVar(useSites={34},value={int[], null}[↦77;refId=612],origin=31),GetField(pc=77,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	32: Assignment(pc=80,DVar(useSites={34},value=int = 0,origin=32),IntConst(pc=80,0)),
	33: Assignment(pc=83,DVar(useSites={34},value=int = 0,origin=33),IntConst(pc=83,0)),
	34: StaticMethodCall(pc=85,java.lang.System,isInterface=false,void arraycopy(java.lang.Object,int,java.lang.Object,int,int),(UVar(defSites={31},value={int[], null}[↦77;refId=612]),UVar(defSites={32},value=int = 0),UVar(defSites={30},value=int[][↦72;refId=610]),UVar(defSites={33},value=int = 0),UVar(defSites={1,17,9},value=int ∈ [-2147483648,2147483646]))),
	35: Assignment(pc=88,DVar(useSites={72,65},value=int = 1,origin=35),IntConst(pc=88,1)),
	36: Assignment(pc=91,DVar(useSites={50},value=int = 1,origin=36),IntConst(pc=91,1)),
	37: If(pc=96,UVar(defSites={100,77,91,39,23},value=an int),>=,UVar(defSites={0},value=an int),target=105),
	38: Assignment(pc=100,DVar(useSites={40},value={int[], null}[↦100;refId=587],origin=38),GetField(pc=100,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	39: Assignment(pc=104,DVar(useSites={40,88,100,74,97,37,101,77,91},value=int ∈ [-2147483647,2147483647],origin=39),BinaryExpr(pc=104,ComputationalTypeInt,UVar(defSites={100,77,91,39,23},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=104,1))),
	40: Assignment(pc=107,DVar(useSites={64,96,48,70,46,41,61,43},value=an int,origin=40),ArrayLoad(pc=107,UVar(defSites={100,77,91,39,23},value=int ∈ [-2147483648,2147483646]),UVar(defSites={38},value={int[], null}[↦100;refId=587]))),
	41: Assignment(pc=112,DVar(useSites={42},value=int ∈ [0,1],origin=41),StaticFunctionCall(pc=112,java.util.regex.ASCII,isInterface=false,boolean isAscii(int),(UVar(defSites={40},value=an int)))),
	42: If(pc=115,UVar(defSites={41},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=45),
	43: Assignment(pc=120,DVar(useSites={44},value=int ∈ [0,1],origin=43),StaticFunctionCall(pc=120,java.util.regex.ASCII,isInterface=false,boolean isAlpha(int),(UVar(defSites={40},value=an int)))),
	44: If(pc=123,UVar(defSites={43},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=48),
	45: Assignment(pc=129,DVar(useSites={96,80,68,60,66,82,70,46,105,69,53,61,51,107,95},value=an int,origin=45),BinaryExpr(pc=129,ComputationalTypeInt,UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),+,IntConst(pc=129,1))),
	46: ArrayStore(pc=134,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),UVar(defSites={40},value=an int)),
	47: Goto(pc=135,target=103),
	48: Assignment(pc=140,DVar(useSites={49},value=int ∈ [0,1],origin=48),StaticFunctionCall(pc=140,java.util.regex.ASCII,isInterface=false,boolean isDigit(int),(UVar(defSites={40},value=an int)))),
	49: If(pc=143,UVar(defSites={48},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=63),
	50: If(pc=148,UVar(defSites={36,93,103},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=60),
	51: Assignment(pc=154,DVar(useSites={56,54},value=an int,origin=51),BinaryExpr(pc=154,ComputationalTypeInt,UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),+,IntConst(pc=154,1))),
	52: Assignment(pc=157,DVar(useSites={53},value=int = 92,origin=52),IntConst(pc=157,92)),
	53: ArrayStore(pc=159,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),UVar(defSites={52},value=int = 92)),
	54: Assignment(pc=163,DVar(useSites={57,59},value=an int,origin=54),BinaryExpr(pc=163,ComputationalTypeInt,UVar(defSites={51},value=an int),+,IntConst(pc=163,1))),
	55: Assignment(pc=166,DVar(useSites={56},value=int = 120,origin=55),IntConst(pc=166,120)),
	56: ArrayStore(pc=168,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={51},value=an int),UVar(defSites={55},value=int = 120)),
	57: Assignment(pc=172,DVar(useSites={60,61},value=an int,origin=57),BinaryExpr(pc=172,ComputationalTypeInt,UVar(defSites={54},value=an int),+,IntConst(pc=172,1))),
	58: Assignment(pc=175,DVar(useSites={59},value=int = 51,origin=58),IntConst(pc=175,51)),
	59: ArrayStore(pc=177,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={54},value=an int),UVar(defSites={58},value=int = 51)),
	60: Assignment(pc=181,DVar(useSites={96,80,68,66,82,70,46,105,69,53,45,61,51,107,95},value=an int,origin=60),BinaryExpr(pc=181,ComputationalTypeInt,UVar(defSites={60,98,1,17,9,57,69,45,83,95},value=an int),+,IntConst(pc=181,1))),
	61: ArrayStore(pc=186,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={60,98,1,17,9,57,69,45,83,95},value=an int),UVar(defSites={40},value=an int)),
	62: Goto(pc=187,target=103),
	63: Assignment(pc=192,DVar(useSites={64},value=int = 92,origin=63),IntConst(pc=192,92)),
	64: If(pc=194,UVar(defSites={40},value=an int),==,UVar(defSites={63},value=int = 92),target=72),
	65: If(pc=199,UVar(defSites={92,78,35},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=69),
	66: Assignment(pc=205,DVar(useSites={70,69},value=an int,origin=66),BinaryExpr(pc=205,ComputationalTypeInt,UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),+,IntConst(pc=205,1))),
	67: Assignment(pc=208,DVar(useSites={68},value=int = 92,origin=67),IntConst(pc=208,92)),
	68: ArrayStore(pc=210,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),UVar(defSites={67},value=int = 92)),
	69: Assignment(pc=214,DVar(useSites={96,80,68,60,66,82,70,46,105,53,45,61,51,107,95},value=an int,origin=69),BinaryExpr(pc=214,ComputationalTypeInt,UVar(defSites={60,66,98,1,17,9,69,45,83,95},value=an int),+,IntConst(pc=214,1))),
	70: ArrayStore(pc=219,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={60,66,98,1,17,9,69,45,83,95},value=an int),UVar(defSites={40},value=an int)),
	71: Goto(pc=220,target=103),
	72: If(pc=225,UVar(defSites={92,78,35},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=87),
	73: Assignment(pc=229,DVar(useSites={74},value={int[], null}[↦229;refId=596],origin=73),GetField(pc=229,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	74: Assignment(pc=233,DVar(useSites={76},value=an int,origin=74),ArrayLoad(pc=233,UVar(defSites={39},value=int ∈ [-2147483647,2147483647]),UVar(defSites={73},value={int[], null}[↦229;refId=596]))),
	75: Assignment(pc=234,DVar(useSites={76},value=int = 69,origin=75),IntConst(pc=234,69)),
	76: If(pc=236,UVar(defSites={74},value=an int),!=,UVar(defSites={75},value=int = 69),target=80),
	77: Assignment(pc=239,DVar(useSites={40,37,39},value=an int,origin=77),BinaryExpr(pc=239,ComputationalTypeInt,UVar(defSites={39},value=int ∈ [-2147483647,2147483647]),+,IntConst(pc=239,1))),
	78: Assignment(pc=242,DVar(useSites={72,65},value=int = 0,origin=78),IntConst(pc=242,0)),
	79: Goto(pc=245,target=103),
	80: Assignment(pc=251,DVar(useSites={85,83},value=an int,origin=80),BinaryExpr(pc=251,ComputationalTypeInt,UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),+,IntConst(pc=251,1))),
	81: Assignment(pc=254,DVar(useSites={82},value=int = 92,origin=81),IntConst(pc=254,92)),
	82: ArrayStore(pc=256,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),UVar(defSites={81},value=int = 92)),
	83: Assignment(pc=260,DVar(useSites={96,80,68,60,66,82,70,46,105,69,53,45,61,51,107,95},value=an int,origin=83),BinaryExpr(pc=260,ComputationalTypeInt,UVar(defSites={80},value=an int),+,IntConst(pc=260,1))),
	84: Assignment(pc=263,DVar(useSites={85},value=int = 92,origin=84),IntConst(pc=263,92)),
	85: ArrayStore(pc=265,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={80},value=an int),UVar(defSites={84},value=int = 92)),
	86: Goto(pc=266,target=103),
	87: Assignment(pc=270,DVar(useSites={88},value={int[], null}[↦270;refId=601],origin=87),GetField(pc=270,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	88: Assignment(pc=274,DVar(useSites={90},value=an int,origin=88),ArrayLoad(pc=274,UVar(defSites={39},value=int ∈ [-2147483647,2147483647]),UVar(defSites={87},value={int[], null}[↦270;refId=601]))),
	89: Assignment(pc=275,DVar(useSites={90},value=int = 81,origin=89),IntConst(pc=275,81)),
	90: If(pc=277,UVar(defSites={88},value=an int),!=,UVar(defSites={89},value=int = 81),target=95),
	91: Assignment(pc=280,DVar(useSites={40,37,39},value=an int,origin=91),BinaryExpr(pc=280,ComputationalTypeInt,UVar(defSites={39},value=int ∈ [-2147483647,2147483647]),+,IntConst(pc=280,1))),
	92: Assignment(pc=283,DVar(useSites={72,65},value=int = 1,origin=92),IntConst(pc=283,1)),
	93: Assignment(pc=286,DVar(useSites={50},value=int = 1,origin=93),IntConst(pc=286,1)),
	94: Goto(pc=289,target=37),
	95: Assignment(pc=295,DVar(useSites={96,80,68,60,66,98,82,70,102,46,105,69,53,45,61,51,107},value=an int,origin=95),BinaryExpr(pc=295,ComputationalTypeInt,UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),+,IntConst(pc=295,1))),
	96: ArrayStore(pc=300,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),UVar(defSites={40},value=int = 92)),
	97: If(pc=303,UVar(defSites={39},value=int ∈ [-2147483647,2147483647]),==,UVar(defSites={0},value=int ∈ [-2147483647,2147483647]),target=103),
	98: Assignment(pc=309,DVar(useSites={96,80,68,60,66,82,70,46,105,69,53,45,61,51,107,95},value=an int,origin=98),BinaryExpr(pc=309,ComputationalTypeInt,UVar(defSites={95},value=an int),+,IntConst(pc=309,1))),
	99: Assignment(pc=313,DVar(useSites={101},value={int[], null}[↦313;refId=605],origin=99),GetField(pc=313,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	100: Assignment(pc=317,DVar(useSites={40,37,39},value=an int,origin=100),BinaryExpr(pc=317,ComputationalTypeInt,UVar(defSites={39},value=int ∈ [-2147483647,2147483647]),+,IntConst(pc=317,1))),
	101: Assignment(pc=320,DVar(useSites={102},value=an int,origin=101),ArrayLoad(pc=320,UVar(defSites={39},value=int ∈ [-2147483647,2147483647]),UVar(defSites={99},value={int[], null}[↦313;refId=605]))),
	102: ArrayStore(pc=321,UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={95},value=an int),UVar(defSites={101},value=an int)),
	103: Assignment(pc=322,DVar(useSites={50},value=int = 0,origin=103),IntConst(pc=322,0)),
	104: Goto(pc=325,target=37),
	105: PutField(pc=330,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int)),
	106: Assignment(pc=337,DVar(useSites={107},value=int = 2,origin=106),IntConst(pc=337,2)),
	107: Assignment(pc=338,DVar(useSites={108},value=an int,origin=107),BinaryExpr(pc=338,ComputationalTypeInt,UVar(defSites={60,98,1,17,9,69,45,83,95},value=an int),+,UVar(defSites={106},value=int = 2))),
	108: Assignment(pc=339,DVar(useSites={109},value={int[], null}[↦339;refId=586],origin=108),StaticFunctionCall(pc=339,java.util.Arrays,isInterface=false,int[] copyOf(int[],int),(UVar(defSites={30},value=int[][↦72;refId=109]),UVar(defSites={107},value=an int)))),
	109: PutField(pc=342,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={108},value={int[], null}[↦339;refId=586])),
	110: Return(pc=345)
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=6) -> {BB_9,BB_20}
	BB_10: BasicBlock(start=102,end=102) -> {BB_9,BB_22}
	BB_11: BasicBlock(start=65,end=65) -> {BB_24,BB_b}
	BB_12: BasicBlock(start=97,end=97) -> {BB_22,BB_21}
	BB_13: BasicBlock(start=109,end=110) -> {BB_29}
	BB_14: BasicBlock(start=77,end=79) -> {BB_22}
	BB_15: BasicBlock(start=73,end=74) -> {BB_9,BB_8}
	BB_16: BasicBlock(start=105,end=108) -> {BB_9,BB_13}
	BB_17: BasicBlock(start=2,end=4) -> {BB_31,BB_0}
	BB_18: BasicBlock(start=45,end=46) -> {BB_9,BB_32}
	BB_19: BasicBlock(start=17,end=18) -> {BB_17}
	BB_1: BasicBlock(start=57,end=59) -> {BB_9,BB_f}
	BB_1a: BasicBlock(start=22,end=22) -> {BB_29}
	BB_1b: BasicBlock(start=44,end=44) -> {BB_27,BB_18}
	BB_1c: BasicBlock(start=71,end=71) -> {BB_22}
	BB_1d: BasicBlock(start=54,end=56) -> {BB_9,BB_1}
	BB_1e: BasicBlock(start=49,end=49) -> {BB_2b,BB_28}
	BB_1f: BasicBlock(start=86,end=86) -> {BB_22}
	BB_20: BasicBlock(start=7,end=8) -> {BB_4,BB_2d}
	BB_21: BasicBlock(start=98,end=101) -> {BB_9,BB_10}
	BB_22: BasicBlock(start=103,end=104) -> {BB_e}
	BB_23: BasicBlock(start=91,end=94) -> {BB_e}
	BB_24: BasicBlock(start=66,end=68) -> {BB_9,BB_b}
	BB_25: BasicBlock(start=80,end=82) -> {BB_9,BB_a}
	BB_26: BasicBlock(start=35,end=36) -> {BB_e}
	BB_27: BasicBlock(start=48,end=48) -> {BB_9,BB_1e}
	BB_28: BasicBlock(start=63,end=64) -> {BB_11,BB_2e}
	BB_29: ExitNode(normalReturn=true)
	BB_2: BasicBlock(start=89,end=90) -> {BB_23,BB_2a}
	BB_2a: BasicBlock(start=95,end=96) -> {BB_9,BB_12}
	BB_2b: BasicBlock(start=50,end=50) -> {BB_f,BB_30}
	BB_2c: BasicBlock(start=31,end=34) -> {BB_9,BB_26}
	BB_2d: BasicBlock(start=11,end=14) -> {BB_9,BB_33}
	BB_2e: BasicBlock(start=72,end=72) -> {BB_15,BB_6}
	BB_2f: BasicBlock(start=43,end=43) -> {BB_9,BB_1b}
	BB_30: BasicBlock(start=51,end=53) -> {BB_9,BB_1d}
	BB_31: BasicBlock(start=19,end=21) -> {BB_7,BB_1a}
	BB_32: BasicBlock(start=47,end=47) -> {BB_22}
	BB_33: BasicBlock(start=15,end=16) -> {BB_19,BB_31}
	BB_34: BasicBlock(start=62,end=62) -> {BB_22}
	BB_3: BasicBlock(start=38,end=40) -> {BB_9,BB_5}
	BB_4: BasicBlock(start=9,end=10) -> {BB_17}
	BB_5: BasicBlock(start=41,end=41) -> {BB_9,BB_d}
	BB_6: BasicBlock(start=87,end=88) -> {BB_9,BB_2}
	BB_7: BasicBlock(start=23,end=30) -> {BB_9,BB_2c}
	BB_8: BasicBlock(start=75,end=76) -> {BB_25,BB_14}
	BB_9: ExitNode(normalReturn=false)
	BB_a: BasicBlock(start=83,end=85) -> {BB_9,BB_1f}
	BB_b: BasicBlock(start=69,end=70) -> {BB_9,BB_1c}
	BB_c: BasicBlock(start=0,end=1) -> {BB_17}
	BB_d: BasicBlock(start=42,end=42) -> {BB_2f,BB_18}
	BB_e: BasicBlock(start=37,end=37) -> {BB_16,BB_3}
	BB_f: BasicBlock(start=60,end=61) -> {BB_9,BB_34}
))

java.util.Map namedGroups()
AITACode(params=(Parameters(
	0: useSites={0,5} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={6,1},value={_ <: java.util.Map, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,namedGroups,java.util.Map,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: If(pc=6,UVar(defSites={0},value={_ <: java.util.Map, null}[↦1;refId=103]),!=,NullExpr(pc=-333),target=6),
	2: Assignment(pc=10,DVar(useSites={4,6,5},value=java.util.HashMap[↦10;refId=104],origin=2),New(pc=10,java.util.HashMap)),
	3: Assignment(pc=14,DVar(useSites={4},value=int = 2,origin=3),IntConst(pc=14,2)),
	4: NonVirtualMethodCall(pc=15,java.util.HashMap,isInterface=false,void <init>(int),UVar(defSites={2},value=java.util.HashMap[↦10;refId=104]),(UVar(defSites={3},value=int = 2))),
	5: PutField(pc=20,java.util.regex.Pattern,namedGroups,java.util.Map,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={2},value=java.util.HashMap[↦10;refId=104])),
	6: ReturnValue(pc=24,UVar(defSites={0,2},value=_ <: java.util.Map[refId=106; values=«_ <: java.util.Map[↦1;refId=103], java.util.HashMap[↦10;refId=104]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_2}
	BB_2: BasicBlock(start=6,end=6) -> {BB_4}
	BB_3: BasicBlock(start=2,end=4) -> {BB_5,BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$Node sequence(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={64,40,24,56,4,12,44,124,2,98,50,26,86,54,129,81,9,137,89,57,121,37,53,77,109,61,19,75,91,59,123,23,15,47,111,127} (origin=-1),
	1: useSites={136,135} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={130,138,6,134},value=null[↦0],origin=0),NullExpr(pc=0)),
	1: Assignment(pc=2,DVar(useSites={8,136,132,137},value=null[↦2],origin=1),NullExpr(pc=2)),
	2: Assignment(pc=8,DVar(useSites={116,3},value=an int,origin=2),VirtualFunctionCall(pc=8,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	3: Switch(pc=15,defaultTarget=127,index=UVar(defSites={2},value=an int),npairs=(IntIntPair(0,123),IntIntPair(36,75),IntIntPair(40,4),IntIntPair(41,108),IntIntPair(42,111),IntIntPair(43,111),IntIntPair(46,89),IntIntPair(63,111),IntIntPair(91,11),IntIntPair(92,26),IntIntPair(93,109),IntIntPair(94,59),IntIntPair(124,108),IntIntPair(125,109)),
	4: Assignment(pc=137,DVar(useSites={8,130,138,6,134,5},value={_ <: java.util.regex.Pattern$Node, null}[↦137;refId=261],origin=4),VirtualFunctionCall(pc=137,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node group0(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	5: If(pc=144,UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦137;refId=261]),==,NullExpr(pc=-333),target=2),
	6: If(pc=151,UVar(defSites={0,4,129},value={_ <: java.util.regex.Pattern$Node, null}[refId=193; values=«null[↦0], {_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], _ <: java.util.regex.Pattern$Node[↦137;refId=169]»]),!=,NullExpr(pc=-333),target=8),
	7: Goto(pc=157,target=9),
	8: PutField(pc=163,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={1,129,9},value={_ <: java.util.regex.Pattern$Node, null}[refId=194; values=«null[↦2], {_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], {_ <: java.util.regex.Pattern$Node, null}[↦167;refId=192]»]),UVar(defSites={4},value=_ <: java.util.regex.Pattern$Node[↦137;refId=261])),
	9: Assignment(pc=167,DVar(useSites={8,136,132,137},value={_ <: java.util.regex.Pattern$Node, null}[↦167;refId=300],origin=9),GetField(pc=167,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	10: Goto(pc=171,target=2),
	11: Assignment(pc=175,DVar(useSites={12},value=int = 128,origin=11),IntConst(pc=175,128)),
	12: Assignment(pc=178,DVar(useSites={13},value=int ∈ [0,1],origin=12),VirtualFunctionCall(pc=178,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={11},value=int = 128)))),
	13: If(pc=181,UVar(defSites={12},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=22),
	14: Assignment(pc=185,DVar(useSites={15},value=int = 16,origin=14),IntConst(pc=185,16)),
	15: Assignment(pc=187,DVar(useSites={16},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=187,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={14},value=int = 16)))),
	16: If(pc=190,UVar(defSites={15},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=22),
	17: Assignment(pc=193,DVar(useSites={20,129},value=java.util.regex.Pattern$NFCCharProperty[↦193;refId=218],origin=17),New(pc=193,java.util.regex.Pattern$NFCCharProperty)),
	18: Assignment(pc=198,DVar(useSites={19},value=int = 1,origin=18),IntConst(pc=198,1)),
	19: Assignment(pc=199,DVar(useSites={20},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦199;refId=220],origin=19),VirtualFunctionCall(pc=199,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate clazz(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={18},value=int = 1)))),
	20: NonVirtualMethodCall(pc=202,java.util.regex.Pattern$NFCCharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={17},value=java.util.regex.Pattern$NFCCharProperty[↦193;refId=218]),(UVar(defSites={19},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦199;refId=220]))),
	21: Goto(pc=207,target=129),
	22: Assignment(pc=212,DVar(useSites={23},value=int = 1,origin=22),IntConst(pc=212,1)),
	23: Assignment(pc=213,DVar(useSites={24},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦213;refId=292],origin=23),VirtualFunctionCall(pc=213,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate clazz(boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={22},value=int = 1)))),
	24: Assignment(pc=216,DVar(useSites={129},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦216;refId=294],origin=24),VirtualFunctionCall(pc=216,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={23},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦213;refId=292])))),
	25: Goto(pc=221,target=129),
	26: Assignment(pc=225,DVar(useSites={28,30,33},value=an int,origin=26),VirtualFunctionCall(pc=225,java.util.regex.Pattern,isInterface=false,int nextEscaped(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	27: Assignment(pc=232,DVar(useSites={28},value=int = 112,origin=27),IntConst(pc=232,112)),
	28: If(pc=234,UVar(defSites={26},value=an int),==,UVar(defSites={27},value=int = 112),target=31),
	29: Assignment(pc=239,DVar(useSites={30},value=int = 80,origin=29),IntConst(pc=239,80)),
	30: If(pc=241,UVar(defSites={26},value=an int),!=,UVar(defSites={29},value=int = 80),target=56),
	31: Assignment(pc=244,DVar(useSites={50,53},value=int = 1,origin=31),IntConst(pc=244,1)),
	32: Assignment(pc=249,DVar(useSites={33},value=int = 80,origin=32),IntConst(pc=249,80)),
	33: If(pc=251,UVar(defSites={26},value=int ∈ [80,112]),!=,UVar(defSites={32},value=int = 80),target=36),
	34: Assignment(pc=254,DVar(useSites={50,53},value=int = 1,origin=34),IntConst(pc=254,1)),
	35: Goto(pc=255,target=37),
	36: Assignment(pc=258,DVar(useSites={50,53},value=int ∈ [0,1],origin=36),IntConst(pc=258,0)),
	37: Assignment(pc=262,DVar(useSites={39},value=an int,origin=37),VirtualFunctionCall(pc=262,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	38: Assignment(pc=269,DVar(useSites={39},value=int = 123,origin=38),IntConst(pc=269,123)),
	39: If(pc=271,UVar(defSites={37},value=an int),==,UVar(defSites={38},value=int = 123),target=42),
	40: VirtualMethodCall(pc=275,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	41: Goto(pc=278,target=43),
	42: Assignment(pc=281,DVar(useSites={50,53},value=int = 0,origin=42),IntConst(pc=281,0)),
	43: Assignment(pc=285,DVar(useSites={44},value=int = 128,origin=43),IntConst(pc=285,128)),
	44: Assignment(pc=288,DVar(useSites={45},value=int ∈ [0,1],origin=44),VirtualFunctionCall(pc=288,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={43},value=int = 128)))),
	45: If(pc=291,UVar(defSites={44},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=53),
	46: Assignment(pc=295,DVar(useSites={47},value=int = 16,origin=46),IntConst(pc=295,16)),
	47: Assignment(pc=297,DVar(useSites={48},value=int ∈ [0,1],origin=47),VirtualFunctionCall(pc=297,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={46},value=int = 16)))),
	48: If(pc=300,UVar(defSites={47},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=53),
	49: Assignment(pc=303,DVar(useSites={129,51},value=java.util.regex.Pattern$NFCCharProperty[↦303;refId=328],origin=49),New(pc=303,java.util.regex.Pattern$NFCCharProperty)),
	50: Assignment(pc=312,DVar(useSites={51},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦312;refId=330],origin=50),VirtualFunctionCall(pc=312,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate family(boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={42,31},value=int ∈ [0,1]),UVar(defSites={36,34},value=int ∈ [0,1])))),
	51: NonVirtualMethodCall(pc=315,java.util.regex.Pattern$NFCCharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={49},value=java.util.regex.Pattern$NFCCharProperty[↦303;refId=328]),(UVar(defSites={50},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦312;refId=330]))),
	52: Goto(pc=320,target=129),
	53: Assignment(pc=329,DVar(useSites={54},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦329;refId=334],origin=53),VirtualFunctionCall(pc=329,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate family(boolean,boolean),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={42,31},value=int ∈ [0,1]),UVar(defSites={36,34},value=int ∈ [0,1])))),
	54: Assignment(pc=332,DVar(useSites={129},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦332;refId=336],origin=54),VirtualFunctionCall(pc=332,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={53},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦329;refId=334])))),
	55: Goto(pc=337,target=129),
	56: VirtualMethodCall(pc=341,java.util.regex.Pattern,isInterface=false,void unread(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),()),
	57: Assignment(pc=345,DVar(useSites={129},value={_ <: java.util.regex.Pattern$Node, null}[↦345;refId=214],origin=57),VirtualFunctionCall(pc=345,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node atom(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	58: Goto(pc=350,target=129),
	59: ExprStmt(pc=354,VirtualFunctionCall(pc=354,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	60: Assignment(pc=359,DVar(useSites={61},value=int = 8,origin=60),IntConst(pc=359,8)),
	61: Assignment(pc=361,DVar(useSites={62},value=int ∈ [0,1],origin=61),VirtualFunctionCall(pc=361,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={60},value=int = 8)))),
	62: If(pc=364,UVar(defSites={61},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=72),
	63: Assignment(pc=368,DVar(useSites={64},value=int = 1,origin=63),IntConst(pc=368,1)),
	64: Assignment(pc=369,DVar(useSites={65},value=int ∈ [0,1],origin=64),VirtualFunctionCall(pc=369,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={63},value=int = 1)))),
	65: If(pc=372,UVar(defSites={64},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=69),
	66: Assignment(pc=375,DVar(useSites={129,67},value=java.util.regex.Pattern$UnixCaret[↦375;refId=199],origin=66),New(pc=375,java.util.regex.Pattern$UnixCaret)),
	67: NonVirtualMethodCall(pc=379,java.util.regex.Pattern$UnixCaret,isInterface=false,void <init>(),UVar(defSites={66},value=java.util.regex.Pattern$UnixCaret[↦375;refId=199]),()),
	68: Goto(pc=384,target=129),
	69: Assignment(pc=387,DVar(useSites={70,129},value=java.util.regex.Pattern$Caret[↦387;refId=202],origin=69),New(pc=387,java.util.regex.Pattern$Caret)),
	70: NonVirtualMethodCall(pc=391,java.util.regex.Pattern$Caret,isInterface=false,void <init>(),UVar(defSites={69},value=java.util.regex.Pattern$Caret[↦387;refId=202]),()),
	71: Goto(pc=396,target=129),
	72: Assignment(pc=399,DVar(useSites={129,73},value=java.util.regex.Pattern$Begin[↦399;refId=205],origin=72),New(pc=399,java.util.regex.Pattern$Begin)),
	73: NonVirtualMethodCall(pc=403,java.util.regex.Pattern$Begin,isInterface=false,void <init>(),UVar(defSites={72},value=java.util.regex.Pattern$Begin[↦399;refId=205]),()),
	74: Goto(pc=408,target=129),
	75: ExprStmt(pc=412,VirtualFunctionCall(pc=412,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	76: Assignment(pc=417,DVar(useSites={77},value=int = 1,origin=76),IntConst(pc=417,1)),
	77: Assignment(pc=418,DVar(useSites={78},value=int ∈ [0,1],origin=77),VirtualFunctionCall(pc=418,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={76},value=int = 1)))),
	78: If(pc=421,UVar(defSites={77},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=84),
	79: Assignment(pc=424,DVar(useSites={82,129},value=java.util.regex.Pattern$UnixDollar[↦424;refId=269],origin=79),New(pc=424,java.util.regex.Pattern$UnixDollar)),
	80: Assignment(pc=429,DVar(useSites={81},value=int = 8,origin=80),IntConst(pc=429,8)),
	81: Assignment(pc=431,DVar(useSites={82},value=int ∈ [0,1],origin=81),VirtualFunctionCall(pc=431,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={80},value=int = 8)))),
	82: NonVirtualMethodCall(pc=434,java.util.regex.Pattern$UnixDollar,isInterface=false,void <init>(boolean),UVar(defSites={79},value=java.util.regex.Pattern$UnixDollar[↦424;refId=269]),(UVar(defSites={81},value=int ∈ [0,1]))),
	83: Goto(pc=439,target=129),
	84: Assignment(pc=442,DVar(useSites={129,87},value=java.util.regex.Pattern$Dollar[↦442;refId=273],origin=84),New(pc=442,java.util.regex.Pattern$Dollar)),
	85: Assignment(pc=447,DVar(useSites={86},value=int = 8,origin=85),IntConst(pc=447,8)),
	86: Assignment(pc=449,DVar(useSites={87},value=int ∈ [0,1],origin=86),VirtualFunctionCall(pc=449,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={85},value=int = 8)))),
	87: NonVirtualMethodCall(pc=452,java.util.regex.Pattern$Dollar,isInterface=false,void <init>(boolean),UVar(defSites={84},value=java.util.regex.Pattern$Dollar[↦442;refId=273]),(UVar(defSites={86},value=int ∈ [0,1]))),
	88: Goto(pc=457,target=129),
	89: ExprStmt(pc=461,VirtualFunctionCall(pc=461,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	90: Assignment(pc=466,DVar(useSites={91},value=int = 32,origin=90),IntConst(pc=466,32)),
	91: Assignment(pc=468,DVar(useSites={92},value=int ∈ [0,1],origin=91),VirtualFunctionCall(pc=468,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={90},value=int = 32)))),
	92: If(pc=471,UVar(defSites={91},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=97),
	93: Assignment(pc=474,DVar(useSites={129,95},value=java.util.regex.Pattern$CharProperty[↦474;refId=225],origin=93),New(pc=474,java.util.regex.Pattern$CharProperty)),
	94: Assignment(pc=478,DVar(useSites={95},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦478;refId=227],origin=94),StaticFunctionCall(pc=478,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate ALL(),())),
	95: NonVirtualMethodCall(pc=481,java.util.regex.Pattern$CharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={93},value=java.util.regex.Pattern$CharProperty[↦474;refId=225]),(UVar(defSites={94},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦478;refId=227]))),
	96: Goto(pc=486,target=129),
	97: Assignment(pc=490,DVar(useSites={98},value=int = 1,origin=97),IntConst(pc=490,1)),
	98: Assignment(pc=491,DVar(useSites={99},value=int ∈ [0,1],origin=98),VirtualFunctionCall(pc=491,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={97},value=int = 1)))),
	99: If(pc=494,UVar(defSites={98},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=104),
	100: Assignment(pc=497,DVar(useSites={102,129},value=java.util.regex.Pattern$CharProperty[↦497;refId=231],origin=100),New(pc=497,java.util.regex.Pattern$CharProperty)),
	101: Assignment(pc=501,DVar(useSites={102},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦501;refId=233],origin=101),StaticFunctionCall(pc=501,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate UNIXDOT(),())),
	102: NonVirtualMethodCall(pc=504,java.util.regex.Pattern$CharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={100},value=java.util.regex.Pattern$CharProperty[↦497;refId=231]),(UVar(defSites={101},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦501;refId=233]))),
	103: Goto(pc=509,target=129),
	104: Assignment(pc=512,DVar(useSites={106,129},value=java.util.regex.Pattern$CharProperty[↦512;refId=236],origin=104),New(pc=512,java.util.regex.Pattern$CharProperty)),
	105: Assignment(pc=516,DVar(useSites={106},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦516;refId=238],origin=105),StaticFunctionCall(pc=516,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate DOT(),())),
	106: NonVirtualMethodCall(pc=519,java.util.regex.Pattern$CharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={104},value=java.util.regex.Pattern$CharProperty[↦512;refId=236]),(UVar(defSites={105},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦516;refId=238]))),
	107: Goto(pc=524,target=129),
	108: Goto(pc=527,target=134),
	109: Assignment(pc=531,DVar(useSites={129},value={_ <: java.util.regex.Pattern$Node, null}[↦531;refId=209],origin=109),VirtualFunctionCall(pc=531,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node atom(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	110: Goto(pc=536,target=129),
	111: ExprStmt(pc=540,VirtualFunctionCall(pc=540,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	112: Assignment(pc=545,DVar(useSites={113,115},value=java.lang.StringBuilder[↦545;refId=242],origin=112),New(pc=545,java.lang.StringBuilder)),
	113: NonVirtualMethodCall(pc=549,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={112},value=java.lang.StringBuilder[↦545;refId=242]),()),
	114: Assignment(pc=552,DVar(useSites={115},value=String("Dangling meta character '")[@552;refId=244],origin=114),StringConst(pc=552,Dangling meta character ')),
	115: Assignment(pc=554,DVar(useSites={117},value={java.lang.StringBuilder, null}[↦554;refId=246],origin=115),VirtualFunctionCall(pc=554,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={112},value=java.lang.StringBuilder[↦545;refId=242]),(UVar(defSites={114},value=String("Dangling meta character '")[@552;refId=244])))),
	116: Assignment(pc=559,DVar(useSites={117},value=int = 63,origin=116),PrimitiveTypecastExpr(pc=559,CharType,UVar(defSites={2},value=int = 63))),
	117: Assignment(pc=560,DVar(useSites={119},value={java.lang.StringBuilder, null}[↦560;refId=249],origin=117),VirtualFunctionCall(pc=560,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={115},value={java.lang.StringBuilder, null}[↦554;refId=246]),(UVar(defSites={116},value=int = 63)))),
	118: Assignment(pc=563,DVar(useSites={119},value=String("'")[@563;refId=250],origin=118),StringConst(pc=563,')),
	119: Assignment(pc=565,DVar(useSites={120},value={java.lang.StringBuilder, null}[↦565;refId=253],origin=119),VirtualFunctionCall(pc=565,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={117},value={java.lang.StringBuilder, null}[↦560;refId=249]),(UVar(defSites={118},value=String("'")[@563;refId=250])))),
	120: Assignment(pc=568,DVar(useSites={121},value={java.lang.String, null}[↦568;refId=256],origin=120),VirtualFunctionCall(pc=568,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={119},value={java.lang.StringBuilder, null}[↦565;refId=253]),())),
	121: Assignment(pc=571,DVar(useSites={122},value={_ <: java.util.regex.PatternSyntaxException, null}[↦571;refId=258],origin=121),VirtualFunctionCall(pc=571,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={120},value={java.lang.String, null}[↦568;refId=256])))),
	122: Throw(pc=574,UVar(defSites={121},value={_ <: java.util.regex.PatternSyntaxException, null}[↦571;refId=258])),
	123: Assignment(pc=576,DVar(useSites={125},value=an int,origin=123),GetField(pc=576,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	124: Assignment(pc=580,DVar(useSites={125},value=an int,origin=124),GetField(pc=580,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	125: If(pc=583,UVar(defSites={123},value=an int),>=,UVar(defSites={124},value=an int),target=134),
	126: Nop(pc=586),
	127: Assignment(pc=590,DVar(useSites={129},value={_ <: java.util.regex.Pattern$Node, null}[↦590;refId=289],origin=127),VirtualFunctionCall(pc=590,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node atom(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	128: Nop(pc=593),
	129: Assignment(pc=598,DVar(useSites={8,136,132,130,138,6,134,137},value={_ <: java.util.regex.Pattern$Node, null}[↦598;refId=318],origin=129),VirtualFunctionCall(pc=598,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node closure(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={72,104,24,100,84,66,54,17,49,57,69,109,93,79,127},value={_ <: java.util.regex.Pattern$Node, null}[refId=316; values=«java.util.regex.Pattern$CharProperty[↦512;refId=236], java.util.regex.Pattern$UnixDollar[↦424;refId=269], {_ <: java.util.regex.Pattern$CharProperty, null}[↦216;refId=294], {_ <: java.util.regex.Pattern$CharProperty, null}[↦332;refId=315], java.util.regex.Pattern$CharProperty[↦474;refId=225], java.util.regex.Pattern$Dollar[↦442;refId=273], {_ <: java.util.regex.Pattern$Node, null}[↦590;refId=289], {_ <: java.util.regex.Pattern$Node, null}[↦345;refId=214], java.util.regex.Pattern$NFCCharProperty[↦193;refId=218], java.util.regex.Pattern$CharProperty[↦497;refId=231], java.util.regex.Pattern$UnixCaret[↦375;refId=199], java.util.regex.Pattern$Caret[↦387;refId=202], {_ <: java.util.regex.Pattern$Node, null}[↦531;refId=209], java.util.regex.Pattern$Begin[↦399;refId=205], java.util.regex.Pattern$NFCCharProperty[↦303;refId=305]»])))),
	130: If(pc=604,UVar(defSites={0,4,129},value={_ <: java.util.regex.Pattern$Node, null}[refId=193; values=«null[↦0], {_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], _ <: java.util.regex.Pattern$Node[↦137;refId=169]»]),!=,NullExpr(pc=-333),target=132),
	131: Goto(pc=612,target=2),
	132: PutField(pc=618,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={1,129,9},value={_ <: java.util.regex.Pattern$Node, null}[refId=194; values=«null[↦2], {_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], {_ <: java.util.regex.Pattern$Node, null}[↦167;refId=192]»]),UVar(defSites={129},value={_ <: java.util.regex.Pattern$Node, null}[↦598;refId=318])),
	133: Goto(pc=624,target=2),
	134: If(pc=628,UVar(defSites={0,4,129},value={_ <: java.util.regex.Pattern$Node, null}[refId=193; values=«null[↦0], {_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], _ <: java.util.regex.Pattern$Node[↦137;refId=169]»]),!=,NullExpr(pc=-333),target=136),
	135: ReturnValue(pc=632,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	136: PutField(pc=635,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={1,129,9},value={_ <: java.util.regex.Pattern$Node, null}[refId=194; values=«null[↦2], {_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], {_ <: java.util.regex.Pattern$Node, null}[↦167;refId=192]»]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	137: PutField(pc=640,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={1,129,9},value=_ <: java.util.regex.Pattern$Node[refId=299; values=«{_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], {_ <: java.util.regex.Pattern$Node, null}[↦167;refId=192]»])),
	138: ReturnValue(pc=644,UVar(defSites={0,4,129},value=_ <: java.util.regex.Pattern$Node[refId=296; values=«{_ <: java.util.regex.Pattern$Node, null}[↦598;refId=184], _ <: java.util.regex.Pattern$Node[↦137;refId=169]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=56,end=56) -> {BB_5c,BB_10}
	BB_10: BasicBlock(start=57,end=57) -> {BB_5c,BB_55}
	BB_11: BasicBlock(start=78,end=78) -> {BB_5b,BB_15}
	BB_12: BasicBlock(start=29,end=30) -> {BB_0,BB_48}
	BB_13: BasicBlock(start=106,end=106) -> {BB_5c,BB_59}
	BB_14: BasicBlock(start=121,end=121) -> {BB_5c,BB_62}
	BB_15: BasicBlock(start=84,end=86) -> {BB_5c,BB_4d}
	BB_16: BasicBlock(start=132,end=132) -> {BB_5c,BB_1a}
	BB_17: BasicBlock(start=116,end=117) -> {BB_5c,BB_34}
	BB_18: BasicBlock(start=74,end=74) -> {BB_29}
	BB_19: BasicBlock(start=89,end=89) -> {BB_5c,BB_65}
	BB_1: BasicBlock(start=69,end=70) -> {BB_5c,BB_35}
	BB_1a: BasicBlock(start=133,end=133) -> {BB_2d}
	BB_1b: BasicBlock(start=6,end=6) -> {BB_53,BB_39}
	BB_1c: BasicBlock(start=60,end=61) -> {BB_5c,BB_61}
	BB_1d: BasicBlock(start=102,end=102) -> {BB_5c,BB_3a}
	BB_1e: BasicBlock(start=38,end=39) -> {BB_4f,BB_6}
	BB_1f: BasicBlock(start=21,end=21) -> {BB_29}
	BB_20: BasicBlock(start=137,end=138) -> {BB_44}
	BB_21: BasicBlock(start=92,end=92) -> {BB_f,BB_23}
	BB_22: BasicBlock(start=65,end=65) -> {BB_1,BB_3b}
	BB_23: BasicBlock(start=97,end=98) -> {BB_5c,BB_4c}
	BB_24: BasicBlock(start=9,end=10) -> {BB_2d}
	BB_25: BasicBlock(start=53,end=53) -> {BB_5c,BB_36}
	BB_26: BasicBlock(start=109,end=109) -> {BB_5c,BB_c}
	BB_27: BasicBlock(start=96,end=96) -> {BB_29}
	BB_28: BasicBlock(start=13,end=13) -> {BB_b,BB_31}
	BB_29: BasicBlock(start=129,end=129) -> {BB_5c,BB_3d}
	BB_2: BasicBlock(start=0,end=1) -> {BB_2d}
	BB_2a: BasicBlock(start=41,end=41) -> {BB_4b}
	BB_2b: BasicBlock(start=134,end=134) -> {BB_5e,BB_3e}
	BB_2c: BasicBlock(start=128,end=128) -> {BB_29}
	BB_2d: BasicBlock(start=2,end=2) -> {BB_5c,BB_3f}
	BB_2e: BasicBlock(start=34,end=35) -> {BB_8}
	BB_2f: BasicBlock(start=45,end=45) -> {BB_e,BB_25}
	BB_30: BasicBlock(start=17,end=19) -> {BB_5c,BB_d}
	BB_31: BasicBlock(start=22,end=23) -> {BB_5c,BB_7}
	BB_32: BasicBlock(start=27,end=28) -> {BB_48,BB_12}
	BB_33: BasicBlock(start=59,end=59) -> {BB_5c,BB_1c}
	BB_34: BasicBlock(start=118,end=119) -> {BB_5c,BB_5}
	BB_35: BasicBlock(start=71,end=71) -> {BB_29}
	BB_36: BasicBlock(start=54,end=54) -> {BB_5c,BB_51}
	BB_37: BasicBlock(start=49,end=50) -> {BB_5c,BB_58}
	BB_38: BasicBlock(start=76,end=77) -> {BB_5c,BB_11}
	BB_39: BasicBlock(start=7,end=7) -> {BB_24}
	BB_3: BasicBlock(start=88,end=88) -> {BB_29}
	BB_3a: BasicBlock(start=103,end=103) -> {BB_29}
	BB_3b: BasicBlock(start=66,end=67) -> {BB_5c,BB_60}
	BB_3c: BasicBlock(start=108,end=108) -> {BB_2b}
	BB_3d: BasicBlock(start=130,end=130) -> {BB_16,BB_5f}
	BB_3e: BasicBlock(start=135,end=135) -> {BB_44}
	BB_3f: BasicBlock(start=3,end=3) -> {BB_5a,BB_41,BB_49,BB_66,BB_47,BB_19,BB_26,BB_54,BB_3c,BB_33,BB_50}
	BB_40: BasicBlock(start=112,end=113) -> {BB_5c,BB_52}
	BB_41: BasicBlock(start=123,end=125) -> {BB_5d,BB_2b}
	BB_42: BasicBlock(start=48,end=48) -> {BB_25,BB_37}
	BB_43: BasicBlock(start=63,end=64) -> {BB_5c,BB_22}
	BB_44: ExitNode(normalReturn=true)
	BB_45: BasicBlock(start=95,end=95) -> {BB_5c,BB_27}
	BB_46: BasicBlock(start=16,end=16) -> {BB_31,BB_30}
	BB_47: BasicBlock(start=127,end=127) -> {BB_5c,BB_2c}
	BB_48: BasicBlock(start=31,end=33) -> {BB_57,BB_2e}
	BB_49: BasicBlock(start=11,end=12) -> {BB_5c,BB_28}
	BB_4: BasicBlock(start=5,end=5) -> {BB_1b,BB_2d}
	BB_4a: BasicBlock(start=72,end=73) -> {BB_5c,BB_18}
	BB_4b: BasicBlock(start=43,end=44) -> {BB_5c,BB_2f}
	BB_4c: BasicBlock(start=99,end=99) -> {BB_4e,BB_64}
	BB_4d: BasicBlock(start=87,end=87) -> {BB_5c,BB_3}
	BB_4e: BasicBlock(start=104,end=105) -> {BB_5c,BB_13}
	BB_4f: BasicBlock(start=40,end=40) -> {BB_5c,BB_2a}
	BB_50: BasicBlock(start=26,end=26) -> {BB_5c,BB_32}
	BB_51: BasicBlock(start=55,end=55) -> {BB_29}
	BB_52: BasicBlock(start=114,end=115) -> {BB_5c,BB_17}
	BB_53: BasicBlock(start=8,end=8) -> {BB_5c,BB_24}
	BB_54: BasicBlock(start=75,end=75) -> {BB_5c,BB_38}
	BB_55: BasicBlock(start=58,end=58) -> {BB_29}
	BB_56: BasicBlock(start=82,end=82) -> {BB_5c,BB_63}
	BB_57: BasicBlock(start=36,end=36) -> {BB_8}
	BB_58: BasicBlock(start=51,end=51) -> {BB_5c,BB_a}
	BB_59: BasicBlock(start=107,end=107) -> {BB_29}
	BB_5: BasicBlock(start=120,end=120) -> {BB_5c,BB_14}
	BB_5a: BasicBlock(start=4,end=4) -> {BB_5c,BB_4}
	BB_5b: BasicBlock(start=79,end=81) -> {BB_5c,BB_56}
	BB_5c: ExitNode(normalReturn=false)
	BB_5d: BasicBlock(start=126,end=126) -> {BB_47}
	BB_5e: BasicBlock(start=136,end=136) -> {BB_5c,BB_20}
	BB_5f: BasicBlock(start=131,end=131) -> {BB_2d}
	BB_60: BasicBlock(start=68,end=68) -> {BB_29}
	BB_61: BasicBlock(start=62,end=62) -> {BB_4a,BB_43}
	BB_62: BasicBlock(start=122,end=122) -> {BB_5c}
	BB_63: BasicBlock(start=83,end=83) -> {BB_29}
	BB_64: BasicBlock(start=100,end=101) -> {BB_5c,BB_1d}
	BB_65: BasicBlock(start=90,end=91) -> {BB_5c,BB_21}
	BB_66: BasicBlock(start=111,end=111) -> {BB_5c,BB_40}
	BB_6: BasicBlock(start=42,end=42) -> {BB_4b}
	BB_7: BasicBlock(start=24,end=24) -> {BB_5c,BB_9}
	BB_8: BasicBlock(start=37,end=37) -> {BB_5c,BB_1e}
	BB_9: BasicBlock(start=25,end=25) -> {BB_29}
	BB_a: BasicBlock(start=52,end=52) -> {BB_29}
	BB_b: BasicBlock(start=14,end=15) -> {BB_5c,BB_46}
	BB_c: BasicBlock(start=110,end=110) -> {BB_29}
	BB_d: BasicBlock(start=20,end=20) -> {BB_5c,BB_1f}
	BB_e: BasicBlock(start=46,end=47) -> {BB_5c,BB_42}
	BB_f: BasicBlock(start=93,end=94) -> {BB_5c,BB_45}
))

java.util.regex.Pattern$CharProperty newCharProperty(java.util.regex.Pattern$CharPredicate)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={0,10,6,3,7} (origin=-2)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦-2;refId=103]),!=,NullExpr(pc=-333),target=3),
	1: Assignment(pc=4,DVar(useSites={2},value=null[↦4],origin=1),NullExpr(pc=4)),
	2: ReturnValue(pc=5,UVar(defSites={1},value=null[↦4])),
	3: Assignment(pc=7,DVar(useSites={4},value=int ∈ [0,1],origin=3),InstanceOf(pc=7,UVar(defSites={-2},value=_ <: java.util.regex.Pattern$CharPredicate[↦-2;refId=103]),java.util.regex.Pattern$BmpCharPredicate)),
	4: If(pc=10,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=9),
	5: Assignment(pc=13,DVar(useSites={8,7},value=java.util.regex.Pattern$BmpCharProperty[↦13;refId=104],origin=5),New(pc=13,java.util.regex.Pattern$BmpCharProperty)),
	6: Checkcast(pc=18,UVar(defSites={-2},value=_ <: java.util.regex.Pattern$CharPredicate[↦-2;refId=103]),java.util.regex.Pattern$BmpCharPredicate),
	7: NonVirtualMethodCall(pc=21,java.util.regex.Pattern$BmpCharProperty,isInterface=false,void <init>(java.util.regex.Pattern$BmpCharPredicate),UVar(defSites={5},value=java.util.regex.Pattern$BmpCharProperty[↦13;refId=104]),(UVar(defSites={-2},value=_ <: java.util.regex.Pattern$BmpCharPredicate[↦-2;refId=105]))),
	8: ReturnValue(pc=24,UVar(defSites={5},value=java.util.regex.Pattern$BmpCharProperty[↦13;refId=104])),
	9: Assignment(pc=25,DVar(useSites={10,11},value=java.util.regex.Pattern$CharProperty[↦25;refId=108],origin=9),New(pc=25,java.util.regex.Pattern$CharProperty)),
	10: NonVirtualMethodCall(pc=30,java.util.regex.Pattern$CharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={9},value=java.util.regex.Pattern$CharProperty[↦25;refId=108]),(UVar(defSites={-2},value=_ <: java.util.regex.Pattern$CharPredicate[↦-2;refId=103]))),
	11: ReturnValue(pc=33,UVar(defSites={9},value=java.util.regex.Pattern$CharProperty[↦25;refId=108]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_2,BB_5}
	BB_1: BasicBlock(start=5,end=6) -> {BB_9,BB_4}
	BB_2: BasicBlock(start=1,end=2) -> {BB_6}
	BB_3: BasicBlock(start=9,end=10) -> {BB_9,BB_7}
	BB_4: BasicBlock(start=7,end=7) -> {BB_9,BB_8}
	BB_5: BasicBlock(start=3,end=4) -> {BB_3,BB_1}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=11,end=11) -> {BB_6}
	BB_8: BasicBlock(start=8,end=8) -> {BB_6}
	BB_9: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$Node createGroup(boolean)
AITACode(params=(Parameters(
	0: useSites={0,6,14,9,21,3,15} (origin=-1),
	1: useSites={18,5} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2,13,11},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern,localCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=6,1)),
	2: Assignment(pc=7,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=7,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={1},value=int = 1))),
	3: PutField(pc=8,java.util.regex.Pattern,localCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={2},value=an int)),
	4: Assignment(pc=12,DVar(useSites={20,22,13},value=int = 0,origin=4),IntConst(pc=12,0)),
	5: If(pc=15,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=10),
	6: Assignment(pc=20,DVar(useSites={8,20,22,13},value=an int,origin=6),GetField(pc=20,java.util.regex.Pattern,capturingGroupCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	7: Assignment(pc=24,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=24,1)),
	8: Assignment(pc=25,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=25,ComputationalTypeInt,UVar(defSites={6},value=an int),+,UVar(defSites={7},value=int = 1))),
	9: PutField(pc=26,java.util.regex.Pattern,capturingGroupCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={8},value=an int)),
	10: Assignment(pc=30,DVar(useSites={22,17,11,23},value=java.util.regex.Pattern$GroupHead[↦30;refId=103],origin=10),New(pc=30,java.util.regex.Pattern$GroupHead)),
	11: NonVirtualMethodCall(pc=35,java.util.regex.Pattern$GroupHead,isInterface=false,void <init>(int),UVar(defSites={10},value=java.util.regex.Pattern$GroupHead[↦30;refId=103]),(UVar(defSites={0},value=an int))),
	12: Assignment(pc=41,DVar(useSites={14,13},value=java.util.regex.Pattern$GroupTail[↦41;refId=105],origin=12),New(pc=41,java.util.regex.Pattern$GroupTail)),
	13: NonVirtualMethodCall(pc=47,java.util.regex.Pattern$GroupTail,isInterface=false,void <init>(int,int),UVar(defSites={12},value=java.util.regex.Pattern$GroupTail[↦41;refId=105]),(UVar(defSites={0},value=an int),UVar(defSites={4,6},value=an int))),
	14: PutField(pc=50,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={12},value=java.util.regex.Pattern$GroupTail[↦41;refId=105])),
	15: Assignment(pc=56,DVar(useSites={16,17},value={_ <: java.util.regex.Pattern$Node, null}[↦56;refId=107],origin=15),GetField(pc=56,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	16: Checkcast(pc=59,UVar(defSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦56;refId=107]),java.util.regex.Pattern$GroupTail),
	17: PutField(pc=62,java.util.regex.Pattern$GroupHead,tail,java.util.regex.Pattern$GroupTail,UVar(defSites={10},value=java.util.regex.Pattern$GroupHead[↦30;refId=103]),UVar(defSites={15},value={java.util.regex.Pattern$GroupTail, null}[↦56;refId=108])),
	18: If(pc=66,UVar(defSites={-2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=23),
	19: Assignment(pc=70,DVar(useSites={20},value=int = 10,origin=19),IntConst(pc=70,10)),
	20: If(pc=72,UVar(defSites={4,6},value=an int),>=,UVar(defSites={19},value=int = 10),target=23),
	21: Assignment(pc=76,DVar(useSites={22},value={java.util.regex.Pattern$GroupHead[], null}[↦76;refId=110],origin=21),GetField(pc=76,java.util.regex.Pattern,groupNodes,java.util.regex.Pattern$GroupHead[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	22: ArrayStore(pc=82,UVar(defSites={21},value={java.util.regex.Pattern$GroupHead[], null}[↦76;refId=110]),UVar(defSites={4,6},value=int ∈ [-2147483648,9]),UVar(defSites={10},value=java.util.regex.Pattern$GroupHead[↦30;refId=103])),
	23: ReturnValue(pc=85,UVar(defSites={10},value=java.util.regex.Pattern$GroupHead[↦30;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=10,end=11) -> {BB_a,BB_6}
	BB_2: BasicBlock(start=14,end=16) -> {BB_a,BB_5}
	BB_3: BasicBlock(start=6,end=9) -> {BB_1}
	BB_4: BasicBlock(start=21,end=22) -> {BB_a,BB_8}
	BB_5: BasicBlock(start=17,end=18) -> {BB_9,BB_8}
	BB_6: BasicBlock(start=12,end=13) -> {BB_a,BB_2}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=23,end=23) -> {BB_7}
	BB_9: BasicBlock(start=19,end=20) -> {BB_8,BB_4}
	BB_a: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate ALL()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value={_ <: java.util.regex.Pattern$ALL()Ljava$util$regex$Pattern$CharPredicate::0$Lambda, null}[↦0;refId=103],origin=0),StaticFunctionCall(pc=0,java.util.regex.Pattern$ALL()Ljava$util$regex$Pattern$CharPredicate::0$Lambda,isInterface=false,java.util.regex.Pattern$ALL()Ljava$util$regex$Pattern$CharPredicate::0$Lambda $newInstance(),())),
	1: ReturnValue(pc=5,UVar(defSites={0},value={_ <: java.util.regex.Pattern$ALL()Ljava$util$regex$Pattern$CharPredicate::0$Lambda, null}[↦0;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void setcursor(int)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: PutField(pc=2,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={-2},value=an int)),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

boolean lambda$Range$12(int,int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={1},value=int ∈ [0,1],origin=0),StaticFunctionCall(pc=3,java.util.regex.Pattern,isInterface=false,boolean inRange(int,int,int),(UVar(defSites={-2},value=an int),UVar(defSites={-4},value=an int),UVar(defSites={-3},value=an int)))),
	1: ReturnValue(pc=6,UVar(defSites={0},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void produceEquivalentAlternation(java.lang.String,java.util.Set)
AITACode(params=(Parameters(
	1: useSites={8,2,9,5,3} (origin=-2),
	2: useSites={20,5,23} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=int = 0,origin=0),IntConst(pc=1,0)),
	1: Assignment(pc=2,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=2,1)),
	2: Assignment(pc=3,DVar(useSites={8,4,9},value=an int,origin=2),StaticFunctionCall(pc=3,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),UVar(defSites={0},value=int = 0),UVar(defSites={1},value=int = 1)))),
	3: Assignment(pc=8,DVar(useSites={4},value=an int,origin=3),VirtualFunctionCall(pc=8,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value={java.lang.String, null}[↦-1;refId=102]),())),
	4: If(pc=12,UVar(defSites={3},value=an int),!=,UVar(defSites={2},value=an int),target=7),
	5: ExprStmt(pc=17,VirtualFunctionCall(pc=17,java.util.Set,isInterface=true,boolean add(java.lang.Object),UVar(defSites={-3},value={_ <: java.util.Set, null}[↦-2;refId=103]),(UVar(defSites={-2},value=java.lang.String[↦-1;refId=102])))),
	6: Return(pc=23),
	7: Assignment(pc=25,DVar(useSites={8},value=int = 0,origin=7),IntConst(pc=25,0)),
	8: Assignment(pc=27,DVar(useSites={16},value={java.lang.String, null}[↦27;refId=108],origin=8),VirtualFunctionCall(pc=27,java.lang.String,isInterface=false,java.lang.String substring(int,int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={7},value=int = 0),UVar(defSites={2},value=an int)))),
	9: Assignment(pc=33,DVar(useSites={10},value={java.lang.String, null}[↦33;refId=110],origin=9),VirtualFunctionCall(pc=33,java.lang.String,isInterface=false,java.lang.String substring(int),UVar(defSites={-2},value=java.lang.String[↦-1;refId=102]),(UVar(defSites={2},value=an int)))),
	10: Assignment(pc=40,DVar(useSites={12,17},value={java.lang.String[], null}[↦40;refId=112],origin=10),StaticFunctionCall(pc=40,java.util.regex.Pattern,isInterface=false,java.lang.String[] producePermutations(java.lang.String),(UVar(defSites={9},value={java.lang.String, null}[↦33;refId=110])))),
	11: Assignment(pc=45,DVar(useSites={24,17,13},value=int = 0,origin=11),IntConst(pc=45,0)),
	12: Assignment(pc=52,DVar(useSites={13},value=int ∈ [0,2147483647],origin=12),ArrayLength(pc=52,UVar(defSites={10},value={java.lang.String[], null}[↦40;refId=112]))),
	13: If(pc=53,UVar(defSites={24,11},value=an int),>=,UVar(defSites={12},value=int ∈ [0,2147483647]),target=26),
	14: Assignment(pc=56,DVar(useSites={16,15},value=java.lang.StringBuilder[↦56;refId=494],origin=14),New(pc=56,java.lang.StringBuilder)),
	15: NonVirtualMethodCall(pc=60,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={14},value=java.lang.StringBuilder[↦56;refId=494]),()),
	16: Assignment(pc=64,DVar(useSites={18},value={java.lang.StringBuilder, null}[↦64;refId=497],origin=16),VirtualFunctionCall(pc=64,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={14},value=java.lang.StringBuilder[↦56;refId=494]),(UVar(defSites={8},value={java.lang.String, null}[↦27;refId=108])))),
	17: Assignment(pc=71,DVar(useSites={18},value={java.lang.String, null}[↦71;refId=499],origin=17),ArrayLoad(pc=71,UVar(defSites={24,11},value=int ∈ [-2147483648,2147483646]),UVar(defSites={10},value=java.lang.String[][↦40;refId=112]))),
	18: Assignment(pc=72,DVar(useSites={19},value={java.lang.StringBuilder, null}[↦72;refId=502],origin=18),VirtualFunctionCall(pc=72,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={16},value={java.lang.StringBuilder, null}[↦64;refId=497]),(UVar(defSites={17},value={java.lang.String, null}[↦71;refId=499])))),
	19: Assignment(pc=75,DVar(useSites={20,21},value={java.lang.String, null}[↦75;refId=505],origin=19),VirtualFunctionCall(pc=75,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={18},value={java.lang.StringBuilder, null}[↦72;refId=502]),())),
	20: ExprStmt(pc=83,VirtualFunctionCall(pc=83,java.util.Set,isInterface=true,boolean add(java.lang.Object),UVar(defSites={-3},value={_ <: java.util.Set, null}[↦-2;refId=103]),(UVar(defSites={19},value={java.lang.String, null}[↦75;refId=505])))),
	21: Assignment(pc=91,DVar(useSites={22,23},value={java.lang.String, null}[↦91;refId=509],origin=21),StaticFunctionCall(pc=91,java.util.regex.Pattern,isInterface=false,java.lang.String composeOneStep(java.lang.String),(UVar(defSites={19},value={java.lang.String, null}[↦75;refId=505])))),
	22: If(pc=98,UVar(defSites={21},value={java.lang.String, null}[↦91;refId=509]),==,NullExpr(pc=-333),target=24),
	23: StaticMethodCall(pc=104,java.util.regex.Pattern,isInterface=false,void produceEquivalentAlternation(java.lang.String,java.util.Set),(UVar(defSites={21},value=java.lang.String[↦91;refId=509]),UVar(defSites={-3},value=_ <: java.util.Set[↦-2;refId=103]))),
	24: Assignment(pc=107,DVar(useSites={17,25,13},value=an int,origin=24),BinaryExpr(pc=107,ComputationalTypeInt,UVar(defSites={24,11},value=an int),+,IntConst(pc=107,1))),
	25: Goto(pc=110,target=12),
	26: Return(pc=113)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_17,BB_e}
	BB_10: BasicBlock(start=11,end=11) -> {BB_c}
	BB_11: BasicBlock(start=19,end=19) -> {BB_17,BB_5}
	BB_12: BasicBlock(start=18,end=18) -> {BB_17,BB_11}
	BB_13: ExitNode(normalReturn=true)
	BB_14: BasicBlock(start=26,end=26) -> {BB_13}
	BB_15: BasicBlock(start=23,end=23) -> {BB_17,BB_3}
	BB_16: BasicBlock(start=4,end=4) -> {BB_d,BB_1}
	BB_17: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_17,BB_6}
	BB_2: BasicBlock(start=10,end=10) -> {BB_17,BB_10}
	BB_3: BasicBlock(start=24,end=25) -> {BB_c}
	BB_4: BasicBlock(start=14,end=15) -> {BB_17,BB_f}
	BB_5: BasicBlock(start=20,end=20) -> {BB_17,BB_7}
	BB_6: BasicBlock(start=6,end=6) -> {BB_13}
	BB_7: BasicBlock(start=21,end=21) -> {BB_17,BB_b}
	BB_8: BasicBlock(start=9,end=9) -> {BB_17,BB_2}
	BB_9: BasicBlock(start=13,end=13) -> {BB_4,BB_14}
	BB_a: BasicBlock(start=17,end=17) -> {BB_17,BB_12}
	BB_b: BasicBlock(start=22,end=22) -> {BB_15,BB_3}
	BB_c: BasicBlock(start=12,end=12) -> {BB_17,BB_9}
	BB_d: BasicBlock(start=7,end=8) -> {BB_17,BB_8}
	BB_e: BasicBlock(start=3,end=3) -> {BB_17,BB_16}
	BB_f: BasicBlock(start=16,end=16) -> {BB_17,BB_a}
))

boolean isLineSeparator(int)
AITACode(params=(Parameters(
	0: useSites={1} (origin=-1),
	1: useSites={4,12,18,10,14} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 1,origin=0),IntConst(pc=1,1)),
	1: Assignment(pc=2,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=2,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={0},value=int = 1)))),
	2: If(pc=5,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=9),
	3: Assignment(pc=9,DVar(useSites={4},value=int = 10,origin=3),IntConst(pc=9,10)),
	4: If(pc=11,UVar(defSites={-2},value=an int),!=,UVar(defSites={3},value=int = 10),target=7),
	5: Assignment(pc=14,DVar(useSites={8},value=int = 1,origin=5),IntConst(pc=14,1)),
	6: Goto(pc=15,target=8),
	7: Assignment(pc=18,DVar(useSites={8},value=int ∈ [0,1],origin=7),IntConst(pc=18,0)),
	8: ReturnValue(pc=19,UVar(defSites={5,7},value=int ∈ [0,1])),
	9: Assignment(pc=21,DVar(useSites={10},value=int = 10,origin=9),IntConst(pc=21,10)),
	10: If(pc=23,UVar(defSites={-2},value=an int),==,UVar(defSites={9},value=int = 10),target=19),
	11: Assignment(pc=27,DVar(useSites={12},value=int = 13,origin=11),IntConst(pc=27,13)),
	12: If(pc=29,UVar(defSites={-2},value=an int),==,UVar(defSites={11},value=int = 13),target=19),
	13: Assignment(pc=33,DVar(useSites={14},value=int = 1,origin=13),IntConst(pc=33,1)),
	14: Assignment(pc=34,DVar(useSites={16},value=an int,origin=14),BinaryExpr(pc=34,ComputationalTypeInt,UVar(defSites={-2},value=an int),|,UVar(defSites={13},value=int = 1))),
	15: Assignment(pc=35,DVar(useSites={16},value=int = 8233,origin=15),IntConst(pc=35,8233)),
	16: If(pc=38,UVar(defSites={14},value=an int),==,UVar(defSites={15},value=int = 8233),target=19),
	17: Assignment(pc=42,DVar(useSites={18},value=int = 133,origin=17),IntConst(pc=42,133)),
	18: If(pc=45,UVar(defSites={-2},value=an int),!=,UVar(defSites={17},value=int = 133),target=21),
	19: Assignment(pc=48,DVar(useSites={22},value=int = 1,origin=19),IntConst(pc=48,1)),
	20: Goto(pc=49,target=22),
	21: Assignment(pc=52,DVar(useSites={22},value=int ∈ [0,1],origin=21),IntConst(pc=52,0)),
	22: ReturnValue(pc=53,UVar(defSites={21,19},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_e,BB_5}
	BB_1: BasicBlock(start=5,end=6) -> {BB_c}
	BB_2: BasicBlock(start=21,end=21) -> {BB_7}
	BB_3: BasicBlock(start=9,end=10) -> {BB_d,BB_b}
	BB_4: BasicBlock(start=13,end=16) -> {BB_d,BB_6}
	BB_5: BasicBlock(start=2,end=2) -> {BB_9,BB_3}
	BB_6: BasicBlock(start=17,end=18) -> {BB_d,BB_2}
	BB_7: BasicBlock(start=22,end=22) -> {BB_a}
	BB_8: BasicBlock(start=7,end=7) -> {BB_c}
	BB_9: BasicBlock(start=3,end=4) -> {BB_8,BB_1}
	BB_a: ExitNode(normalReturn=true)
	BB_b: BasicBlock(start=11,end=12) -> {BB_4,BB_d}
	BB_c: BasicBlock(start=8,end=8) -> {BB_a}
	BB_d: BasicBlock(start=19,end=20) -> {BB_7}
	BB_e: ExitNode(normalReturn=false)
))

java.util.regex.PatternSyntaxException error(java.lang.String)
AITACode(params=(Parameters(
	0: useSites={2,1} (origin=-1),
	1: useSites={5} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={6,5},value=java.util.regex.PatternSyntaxException[↦0;refId=104],origin=0),New(pc=0,java.util.regex.PatternSyntaxException)),
	1: Assignment(pc=6,DVar(useSites={5},value={java.lang.String, null}[↦6;refId=105],origin=1),GetField(pc=6,java.util.regex.Pattern,normalizedPattern,java.lang.String,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=10,DVar(useSites={4},value=an int,origin=2),GetField(pc=10,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	3: Assignment(pc=13,DVar(useSites={4},value=int = 1,origin=3),IntConst(pc=13,1)),
	4: Assignment(pc=14,DVar(useSites={5},value=an int,origin=4),BinaryExpr(pc=14,ComputationalTypeInt,UVar(defSites={2},value=an int),-,UVar(defSites={3},value=int = 1))),
	5: NonVirtualMethodCall(pc=15,java.util.regex.PatternSyntaxException,isInterface=false,void <init>(java.lang.String,java.lang.String,int),UVar(defSites={0},value=java.util.regex.PatternSyntaxException[↦0;refId=104]),(UVar(defSites={-2},value={java.lang.String, null}[↦-2;refId=103]),UVar(defSites={1},value={java.lang.String, null}[↦6;refId=105]),UVar(defSites={4},value=an int))),
	6: ReturnValue(pc=18,UVar(defSites={0},value=java.util.regex.PatternSyntaxException[↦0;refId=104]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=6,end=6) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$CharPredicate single(int)
AITACode(params=(Parameters(
	0: useSites={4,1} (origin=-1),
	1: useSites={20,18,6,22,14,13,11} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 2,origin=0),IntConst(pc=1,2)),
	1: Assignment(pc=2,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=2,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={0},value=int = 2)))),
	2: If(pc=5,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=18),
	3: Assignment(pc=9,DVar(useSites={4},value=int = 64,origin=3),IntConst(pc=9,64)),
	4: Assignment(pc=11,DVar(useSites={5},value=int ∈ [0,1],origin=4),VirtualFunctionCall(pc=11,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={3},value=int = 64)))),
	5: If(pc=14,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	6: Assignment(pc=18,DVar(useSites={8,7},value=an int,origin=6),StaticFunctionCall(pc=18,java.lang.Character,isInterface=false,int toUpperCase(int),(UVar(defSites={-2},value=an int)))),
	7: Assignment(pc=23,DVar(useSites={8,9},value=an int,origin=7),StaticFunctionCall(pc=23,java.lang.Character,isInterface=false,int toLowerCase(int),(UVar(defSites={6},value=an int)))),
	8: If(pc=29,UVar(defSites={6},value=an int),==,UVar(defSites={7},value=an int),target=18),
	9: Assignment(pc=33,DVar(useSites={10},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦33;refId=108],origin=9),StaticFunctionCall(pc=33,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate SingleU(int),(UVar(defSites={7},value=an int)))),
	10: ReturnValue(pc=36,UVar(defSites={9},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦33;refId=108])),
	11: Assignment(pc=38,DVar(useSites={12},value=int ∈ [0,1],origin=11),StaticFunctionCall(pc=38,java.util.regex.ASCII,isInterface=false,boolean isAscii(int),(UVar(defSites={-2},value=an int)))),
	12: If(pc=41,UVar(defSites={11},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=18),
	13: Assignment(pc=45,DVar(useSites={16,15},value=an int,origin=13),StaticFunctionCall(pc=45,java.util.regex.ASCII,isInterface=false,int toLower(int),(UVar(defSites={-2},value=an int)))),
	14: Assignment(pc=50,DVar(useSites={16,15},value=an int,origin=14),StaticFunctionCall(pc=50,java.util.regex.ASCII,isInterface=false,int toUpper(int),(UVar(defSites={-2},value=an int)))),
	15: If(pc=56,UVar(defSites={13},value=an int),==,UVar(defSites={14},value=an int),target=18),
	16: Assignment(pc=61,DVar(useSites={17},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦61;refId=113],origin=16),StaticFunctionCall(pc=61,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$BmpCharPredicate SingleI(int,int),(UVar(defSites={13},value=an int),UVar(defSites={14},value=an int)))),
	17: ReturnValue(pc=64,UVar(defSites={16},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦61;refId=113])),
	18: Assignment(pc=66,DVar(useSites={19},value=int ∈ [0,1],origin=18),StaticFunctionCall(pc=66,java.util.regex.Pattern,isInterface=false,boolean isSupplementary(int),(UVar(defSites={-2},value=an int)))),
	19: If(pc=69,UVar(defSites={18},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=22),
	20: Assignment(pc=73,DVar(useSites={21},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦73;refId=116],origin=20),StaticFunctionCall(pc=73,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$CharPredicate SingleS(int),(UVar(defSites={-2},value=an int)))),
	21: ReturnValue(pc=76,UVar(defSites={20},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦73;refId=116])),
	22: Assignment(pc=78,DVar(useSites={23},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦78;refId=118],origin=22),StaticFunctionCall(pc=78,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$BmpCharPredicate Single(int),(UVar(defSites={-2},value=an int)))),
	23: ReturnValue(pc=81,UVar(defSites={22},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦78;refId=118]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_14,BB_9}
	BB_10: BasicBlock(start=11,end=11) -> {BB_14,BB_c}
	BB_11: BasicBlock(start=23,end=23) -> {BB_17}
	BB_12: BasicBlock(start=8,end=8) -> {BB_7,BB_16}
	BB_13: BasicBlock(start=19,end=19) -> {BB_4,BB_b}
	BB_14: ExitNode(normalReturn=false)
	BB_15: BasicBlock(start=15,end=15) -> {BB_16,BB_f}
	BB_16: BasicBlock(start=18,end=18) -> {BB_14,BB_13}
	BB_17: ExitNode(normalReturn=true)
	BB_1: BasicBlock(start=5,end=5) -> {BB_5,BB_10}
	BB_2: BasicBlock(start=10,end=10) -> {BB_17}
	BB_3: BasicBlock(start=14,end=14) -> {BB_14,BB_15}
	BB_4: BasicBlock(start=20,end=20) -> {BB_14,BB_6}
	BB_5: BasicBlock(start=6,end=6) -> {BB_14,BB_d}
	BB_6: BasicBlock(start=21,end=21) -> {BB_17}
	BB_7: BasicBlock(start=9,end=9) -> {BB_14,BB_2}
	BB_8: BasicBlock(start=13,end=13) -> {BB_14,BB_3}
	BB_9: BasicBlock(start=2,end=2) -> {BB_e,BB_16}
	BB_a: BasicBlock(start=17,end=17) -> {BB_17}
	BB_b: BasicBlock(start=22,end=22) -> {BB_14,BB_11}
	BB_c: BasicBlock(start=12,end=12) -> {BB_8,BB_16}
	BB_d: BasicBlock(start=7,end=7) -> {BB_14,BB_12}
	BB_e: BasicBlock(start=3,end=4) -> {BB_14,BB_1}
	BB_f: BasicBlock(start=16,end=16) -> {BB_14,BB_a}
))

java.util.regex.Pattern$Node expr(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={4,26,30,5} (origin=-1),
	1: useSites={4,12,19,11} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={16,24,6,29,19},value=null[↦0],origin=0),NullExpr(pc=0)),
	1: Assignment(pc=2,DVar(useSites={22},value=null[↦2],origin=1),NullExpr(pc=2)),
	2: Assignment(pc=4,DVar(useSites={16,17},value=null[↦4],origin=2),NullExpr(pc=4)),
	3: Assignment(pc=7,DVar(useSites={8,24,22,15},value=null[↦7],origin=3),NullExpr(pc=7)),
	4: Assignment(pc=12,DVar(useSites={16,24,12,6,17,29,19},value={_ <: java.util.regex.Pattern$Node, null}[↦12;refId=131],origin=4),VirtualFunctionCall(pc=12,java.util.regex.Pattern,isInterface=false,java.util.regex.Pattern$Node sequence(java.util.regex.Pattern$Node),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])))),
	5: Assignment(pc=18,DVar(useSites={22,15},value={_ <: java.util.regex.Pattern$Node, null}[↦18;refId=132],origin=5),GetField(pc=18,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	6: If(pc=24,UVar(defSites={0,4,23},value={_ <: java.util.regex.Pattern$Node, null}[refId=128; values=«null[↦0], {_ <: java.util.regex.Pattern$Node, null}[↦12;refId=112], java.util.regex.Pattern$Branch[↦107;refId=120]»]),!=,NullExpr(pc=-333),target=8),
	7: Goto(pc=33,target=26),
	8: If(pc=38,UVar(defSites={9,3},value={java.util.regex.Pattern$BranchConn, null}[refId=125; values=«null[↦7], java.util.regex.Pattern$BranchConn[↦41;refId=114]»]),!=,NullExpr(pc=-333),target=12),
	9: Assignment(pc=41,DVar(useSites={8,24,10,22,11,15},value=java.util.regex.Pattern$BranchConn[↦41;refId=138],origin=9),New(pc=41,java.util.regex.Pattern$BranchConn)),
	10: NonVirtualMethodCall(pc=45,java.util.regex.Pattern$BranchConn,isInterface=false,void <init>(),UVar(defSites={9},value=java.util.regex.Pattern$BranchConn[↦41;refId=138]),()),
	11: PutField(pc=53,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={9},value=java.util.regex.Pattern$BranchConn[↦41;refId=138]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	12: If(pc=59,UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦12;refId=131]),!=,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),target=15),
	13: Assignment(pc=62,DVar(useSites={24,17},value=null[↦62],origin=13),NullExpr(pc=62)),
	14: Goto(pc=65,target=16),
	15: PutField(pc=72,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦18;refId=132]),UVar(defSites={9,3},value=java.util.regex.Pattern$BranchConn[↦41;refId=138])),
	16: If(pc=78,UVar(defSites={0,4,23},value=_ <: java.util.regex.Pattern$Node[refId=142; values=«{_ <: java.util.regex.Pattern$Node, null}[↦12;refId=112], java.util.regex.Pattern$Branch[↦107;refId=120]»]),!=,UVar(defSites={2,23},value={java.util.regex.Pattern$Branch, null}[refId=124; values=«null[↦4], java.util.regex.Pattern$Branch[↦107;refId=120]»]),target=19),
	17: VirtualMethodCall(pc=85,java.util.regex.Pattern$Branch,isInterface=false,void add(java.util.regex.Pattern$Node),UVar(defSites={2,23},value={java.util.regex.Pattern$Branch, null}[refId=124; values=«null[↦4], java.util.regex.Pattern$Branch[↦107;refId=120]»]),(UVar(defSites={4,13},value={_ <: java.util.regex.Pattern$Node, null}[refId=143; values=«null[↦62], {_ <: java.util.regex.Pattern$Node, null}[↦12;refId=131]»]))),
	18: Goto(pc=88,target=26),
	19: If(pc=93,UVar(defSites={0,4,23},value=_ <: java.util.regex.Pattern$Node[refId=142; values=«{_ <: java.util.regex.Pattern$Node, null}[↦12;refId=112], java.util.regex.Pattern$Branch[↦107;refId=120]»]),!=,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),target=22),
	20: Assignment(pc=96,DVar(useSites={24},value=null[↦96],origin=20),NullExpr(pc=96)),
	21: Goto(pc=98,target=23),
	22: PutField(pc=104,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={1,5},value={_ <: java.util.regex.Pattern$Node, null}[refId=110; values=«null[↦2], {_ <: java.util.regex.Pattern$Node, null}[↦18;refId=106]»]),UVar(defSites={9,3},value=java.util.regex.Pattern$BranchConn[↦41;refId=138])),
	23: Assignment(pc=107,DVar(useSites={16,24,6,17,29,19},value=java.util.regex.Pattern$Branch[↦107;refId=154],origin=23),New(pc=107,java.util.regex.Pattern$Branch)),
	24: NonVirtualMethodCall(pc=116,java.util.regex.Pattern$Branch,isInterface=false,void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Node,java.util.regex.Pattern$Node),UVar(defSites={23},value=java.util.regex.Pattern$Branch[↦107;refId=154]),(UVar(defSites={0,4,20,23},value={_ <: java.util.regex.Pattern$Node, null}[refId=146; values=«{_ <: java.util.regex.Pattern$Node, null}[↦12;refId=112], null[↦96], java.util.regex.Pattern$Branch[↦107;refId=120]»]),UVar(defSites={4,13},value={_ <: java.util.regex.Pattern$Node, null}[refId=147; values=«{_ <: java.util.regex.Pattern$Node, null}[↦12;refId=131], null[↦62]»]),UVar(defSites={9,3},value=java.util.regex.Pattern$BranchConn[↦41;refId=138]))),
	25: Nop(pc=119),
	26: Assignment(pc=124,DVar(useSites={28},value=an int,origin=26),VirtualFunctionCall(pc=124,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	27: Assignment(pc=127,DVar(useSites={28},value=int = 124,origin=27),IntConst(pc=127,124)),
	28: If(pc=129,UVar(defSites={26},value=an int),==,UVar(defSites={27},value=int = 124),target=30),
	29: ReturnValue(pc=133,UVar(defSites={0,4,23},value={_ <: java.util.regex.Pattern$Node, null}[refId=122; values=«{_ <: java.util.regex.Pattern$Node, null}[↦12;refId=112], java.util.regex.Pattern$Branch[↦107;refId=120]»])),
	30: ExprStmt(pc=135,VirtualFunctionCall(pc=135,java.util.regex.Pattern,isInterface=false,int next(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	31: Goto(pc=139,target=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_17}
	BB_10: ExitNode(normalReturn=true)
	BB_11: BasicBlock(start=16,end=16) -> {BB_5,BB_16}
	BB_12: BasicBlock(start=31,end=31) -> {BB_17}
	BB_13: BasicBlock(start=26,end=26) -> {BB_18,BB_e}
	BB_14: BasicBlock(start=23,end=24) -> {BB_18,BB_2}
	BB_15: BasicBlock(start=30,end=30) -> {BB_18,BB_12}
	BB_16: BasicBlock(start=19,end=19) -> {BB_b,BB_d}
	BB_17: BasicBlock(start=4,end=4) -> {BB_18,BB_1}
	BB_18: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=6) -> {BB_9,BB_7}
	BB_2: BasicBlock(start=25,end=25) -> {BB_13}
	BB_3: BasicBlock(start=9,end=10) -> {BB_18,BB_8}
	BB_4: BasicBlock(start=13,end=14) -> {BB_11}
	BB_5: BasicBlock(start=17,end=17) -> {BB_18,BB_f}
	BB_6: BasicBlock(start=12,end=12) -> {BB_a,BB_4}
	BB_7: BasicBlock(start=7,end=7) -> {BB_13}
	BB_8: BasicBlock(start=11,end=11) -> {BB_6}
	BB_9: BasicBlock(start=8,end=8) -> {BB_6,BB_3}
	BB_a: BasicBlock(start=15,end=15) -> {BB_18,BB_11}
	BB_b: BasicBlock(start=20,end=21) -> {BB_14}
	BB_c: BasicBlock(start=29,end=29) -> {BB_10}
	BB_d: BasicBlock(start=22,end=22) -> {BB_18,BB_14}
	BB_e: BasicBlock(start=27,end=28) -> {BB_c,BB_15}
	BB_f: BasicBlock(start=18,end=18) -> {BB_13}
))

int c()
AITACode(params=(Parameters(
	0: useSites={0,8,1,3} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern,patternLength,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: If(pc=8,UVar(defSites={0},value=an int),>=,UVar(defSites={1},value=an int),target=7),
	3: Assignment(pc=12,DVar(useSites={5},value=an int,origin=3),VirtualFunctionCall(pc=12,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	4: Assignment(pc=15,DVar(useSites={5},value=int = 64,origin=4),IntConst(pc=15,64)),
	5: Assignment(pc=17,DVar(useSites={6},value=an int,origin=5),BinaryExpr(pc=17,ComputationalTypeInt,UVar(defSites={3},value=an int),^,UVar(defSites={4},value=int = 64))),
	6: ReturnValue(pc=18,UVar(defSites={5},value=an int)),
	7: Assignment(pc=20,DVar(useSites={8},value=String("Illegal control escape sequence")[@20;refId=103],origin=7),StringConst(pc=20,Illegal control escape sequence)),
	8: Assignment(pc=23,DVar(useSites={9},value={_ <: java.util.regex.PatternSyntaxException, null}[↦23;refId=105],origin=8),VirtualFunctionCall(pc=23,java.util.regex.Pattern,isInterface=false,java.util.regex.PatternSyntaxException error(java.lang.String),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={7},value=String("Illegal control escape sequence")[@20;refId=103])))),
	9: Throw(pc=26,UVar(defSites={8},value={_ <: java.util.regex.PatternSyntaxException, null}[↦23;refId=105]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_2,BB_3}
	BB_1: BasicBlock(start=9,end=9) -> {BB_6}
	BB_2: BasicBlock(start=7,end=8) -> {BB_6,BB_1}
	BB_3: BasicBlock(start=3,end=3) -> {BB_6,BB_5}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=4,end=6) -> {BB_4}
	BB_6: ExitNode(normalReturn=false)
))

boolean lambda$UNIXDOT$6(int)
AITACode(params=(Parameters(
	1: useSites={1} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 10,origin=0),IntConst(pc=1,10)),
	1: If(pc=3,UVar(defSites={-2},value=an int),==,UVar(defSites={0},value=int = 10),target=4),
	2: Assignment(pc=6,DVar(useSites={5},value=int = 1,origin=2),IntConst(pc=6,1)),
	3: Goto(pc=7,target=5),
	4: Assignment(pc=10,DVar(useSites={5},value=int ∈ [0,1],origin=4),IntConst(pc=10,0)),
	5: ReturnValue(pc=11,UVar(defSites={4,2},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=2,end=3) -> {BB_1}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_1}
	BB_5: ExitNode(normalReturn=false)
))

boolean inRange(int,int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0,1} (origin=-3),
	3: useSites={1} (origin=-4)
)),stmts=(
	0: If(pc=2,UVar(defSites={-2},value=an int),>,UVar(defSites={-3},value=an int),target=4),
	1: If(pc=7,UVar(defSites={-3},value=an int),>,UVar(defSites={-4},value=an int),target=4),
	2: Assignment(pc=10,DVar(useSites={5},value=int = 1,origin=2),IntConst(pc=10,1)),
	3: Goto(pc=11,target=5),
	4: Assignment(pc=14,DVar(useSites={5},value=int ∈ [0,1],origin=4),IntConst(pc=14,0)),
	5: ReturnValue(pc=15,UVar(defSites={4,2},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_5,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_4}
	BB_2: BasicBlock(start=1,end=1) -> {BB_3,BB_5}
	BB_3: BasicBlock(start=2,end=3) -> {BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=4,end=4) -> {BB_1}
	BB_6: ExitNode(normalReturn=false)
))

java.util.regex.Pattern$Node ref(int)
AITACode(params=(Parameters(
	0: useSites={20,2,26,22,9,15} (origin=-1),
	1: useSites={30,5,27} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: If(pc=3,UVar(defSites={0,17,13},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=19),
	2: Assignment(pc=7,DVar(useSites={3,7},value=an int,origin=2),VirtualFunctionCall(pc=7,java.util.regex.Pattern,isInterface=false,int peek(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	3: Switch(pc=12,defaultTarget=17,index=UVar(defSites={2},value=an int),npairs=(IntIntPair(48,4),IntIntPair(49,4),IntIntPair(50,4),IntIntPair(51,4),IntIntPair(52,4),IntIntPair(53,4),IntIntPair(54,4),IntIntPair(55,4),IntIntPair(56,4),IntIntPair(57,4)),
	4: Assignment(pc=69,DVar(useSites={5},value=int = 10,origin=4),IntConst(pc=69,10)),
	5: Assignment(pc=71,DVar(useSites={8},value=an int,origin=5),BinaryExpr(pc=71,ComputationalTypeInt,UVar(defSites={8,-2},value=an int),*,UVar(defSites={4},value=int = 10))),
	6: Assignment(pc=73,DVar(useSites={7},value=int = 48,origin=6),IntConst(pc=73,48)),
	7: Assignment(pc=75,DVar(useSites={8},value=int = 9,origin=7),BinaryExpr(pc=75,ComputationalTypeInt,UVar(defSites={2},value=int = 57),-,UVar(defSites={6},value=int = 48))),
	8: Assignment(pc=76,DVar(useSites={12,30,5,27},value=an int,origin=8),BinaryExpr(pc=76,ComputationalTypeInt,UVar(defSites={5},value=an int),+,UVar(defSites={7},value=int = 9))),
	9: Assignment(pc=80,DVar(useSites={11},value=an int,origin=9),GetField(pc=80,java.util.regex.Pattern,capturingGroupCount,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	10: Assignment(pc=83,DVar(useSites={11},value=int = 1,origin=10),IntConst(pc=83,1)),
	11: Assignment(pc=84,DVar(useSites={12},value=an int,origin=11),BinaryExpr(pc=84,ComputationalTypeInt,UVar(defSites={9},value=an int),-,UVar(defSites={10},value=int = 1))),
	12: If(pc=87,UVar(defSites={11},value=an int),>=,UVar(defSites={8},value=an int),target=15),
	13: Assignment(pc=90,DVar(useSites={1},value=int = 1,origin=13),IntConst(pc=90,1)),
	14: Goto(pc=92,target=1),
	15: ExprStmt(pc=99,VirtualFunctionCall(pc=99,java.util.regex.Pattern,isInterface=false,int read(),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),())),
	16: Goto(pc=103,target=1),
	17: Assignment(pc=106,DVar(useSites={1},value=int = 1,origin=17),IntConst(pc=106,1)),
	18: Goto(pc=108,target=1),
	19: Assignment(pc=112,DVar(useSites={20},value=int = 1,origin=19),IntConst(pc=112,1)),
	20: PutField(pc=113,java.util.regex.Pattern,hasGroupRef,boolean,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={19},value=int = 1)),
	21: Assignment(pc=117,DVar(useSites={22},value=int = 2,origin=21),IntConst(pc=117,2)),
	22: Assignment(pc=118,DVar(useSites={23},value=int ∈ [0,1],origin=22),VirtualFunctionCall(pc=118,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={21},value=int = 2)))),
	23: If(pc=121,UVar(defSites={22},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=29),
	24: Assignment(pc=124,DVar(useSites={28,27},value=java.util.regex.Pattern$CIBackRef[↦124;refId=108],origin=24),New(pc=124,java.util.regex.Pattern$CIBackRef)),
	25: Assignment(pc=130,DVar(useSites={26},value=int = 64,origin=25),IntConst(pc=130,64)),
	26: Assignment(pc=132,DVar(useSites={27},value=int ∈ [0,1],origin=26),VirtualFunctionCall(pc=132,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={25},value=int = 64)))),
	27: NonVirtualMethodCall(pc=135,java.util.regex.Pattern$CIBackRef,isInterface=false,void <init>(int,boolean),UVar(defSites={24},value=java.util.regex.Pattern$CIBackRef[↦124;refId=108]),(UVar(defSites={8,-2},value=an int),UVar(defSites={26},value=int ∈ [0,1]))),
	28: ReturnValue(pc=138,UVar(defSites={24},value=java.util.regex.Pattern$CIBackRef[↦124;refId=108])),
	29: Assignment(pc=139,DVar(useSites={30,31},value=java.util.regex.Pattern$BackRef[↦139;refId=111],origin=29),New(pc=139,java.util.regex.Pattern$BackRef)),
	30: NonVirtualMethodCall(pc=144,java.util.regex.Pattern$BackRef,isInterface=false,void <init>(int),UVar(defSites={29},value=java.util.regex.Pattern$BackRef[↦139;refId=111]),(UVar(defSites={8,-2},value=an int))),
	31: ReturnValue(pc=147,UVar(defSites={29},value=java.util.regex.Pattern$BackRef[↦139;refId=111]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3}
	BB_10: BasicBlock(start=4,end=12) -> {BB_5,BB_d}
	BB_11: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=24,end=26) -> {BB_11,BB_8}
	BB_2: BasicBlock(start=29,end=30) -> {BB_11,BB_f}
	BB_3: BasicBlock(start=1,end=1) -> {BB_6,BB_c}
	BB_4: BasicBlock(start=28,end=28) -> {BB_a}
	BB_5: BasicBlock(start=13,end=14) -> {BB_3}
	BB_6: BasicBlock(start=2,end=2) -> {BB_11,BB_9}
	BB_7: BasicBlock(start=17,end=18) -> {BB_3}
	BB_8: BasicBlock(start=27,end=27) -> {BB_11,BB_4}
	BB_9: BasicBlock(start=3,end=3) -> {BB_10,BB_7}
	BB_a: ExitNode(normalReturn=true)
	BB_b: BasicBlock(start=23,end=23) -> {BB_1,BB_2}
	BB_c: BasicBlock(start=19,end=22) -> {BB_11,BB_b}
	BB_d: BasicBlock(start=15,end=15) -> {BB_11,BB_e}
	BB_e: BasicBlock(start=16,end=16) -> {BB_3}
	BB_f: BasicBlock(start=31,end=31) -> {BB_a}
))

int read()
AITACode(params=(Parameters(
	0: useSites={0,4,1,9,7} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={5},value={int[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={5,3},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=10,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=10,1)),
	3: Assignment(pc=11,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=11,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={2},value=int = 1))),
	4: PutField(pc=12,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=15,DVar(useSites={9,11},value=an int,origin=5),ArrayLoad(pc=15,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=103]))),
	6: Assignment(pc=18,DVar(useSites={7},value=int = 4,origin=6),IntConst(pc=18,4)),
	7: Assignment(pc=19,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=19,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={6},value=int = 4)))),
	8: If(pc=22,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	9: Assignment(pc=27,DVar(useSites={11},value=an int,origin=9),VirtualFunctionCall(pc=27,java.util.regex.Pattern,isInterface=false,int parsePastWhitespace(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={5},value=an int)))),
	10: Nop(pc=30),
	11: ReturnValue(pc=32,UVar(defSites={9,5},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_7,BB_2}
	BB_1: BasicBlock(start=10,end=10) -> {BB_5}
	BB_2: BasicBlock(start=6,end=7) -> {BB_7,BB_6}
	BB_3: BasicBlock(start=9,end=9) -> {BB_7,BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=11,end=11) -> {BB_4}
	BB_6: BasicBlock(start=8,end=8) -> {BB_3,BB_5}
	BB_7: ExitNode(normalReturn=false)
))

void append(int,int)
AITACode(params=(Parameters(
	0: useSites={0,10,9,5} (origin=-1),
	1: useSites={11} (origin=-2),
	2: useSites={8,2,3,11} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value={int[], null}[↦2;refId=103],origin=0),GetField(pc=2,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=5,UVar(defSites={0},value={int[], null}[↦2;refId=103]))),
	2: If(pc=6,UVar(defSites={-3},value=an int),<,UVar(defSites={1},value=int ∈ [0,2147483647]),target=10),
	3: Assignment(pc=11,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=11,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [0,2147483647]),+,UVar(defSites={-3},value=int ∈ [0,2147483647]))),
	4: Assignment(pc=12,DVar(useSites={8,9},value=int[][↦12;refId=105],origin=4),NewArray(pc=12,[UVar(defSites={3},value=an int)],int[])),
	5: Assignment(pc=16,DVar(useSites={8},value={int[], null}[↦16;refId=107],origin=5),GetField(pc=16,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	6: Assignment(pc=19,DVar(useSites={8},value=int = 0,origin=6),IntConst(pc=19,0)),
	7: Assignment(pc=21,DVar(useSites={8},value=int = 0,origin=7),IntConst(pc=21,0)),
	8: StaticMethodCall(pc=23,java.lang.System,isInterface=false,void arraycopy(java.lang.Object,int,java.lang.Object,int,int),(UVar(defSites={5},value={int[], null}[↦16;refId=107]),UVar(defSites={6},value=int = 0),UVar(defSites={4},value=int[][↦12;refId=105]),UVar(defSites={7},value=int = 0),UVar(defSites={-3},value=int ∈ [0,2147483647]))),
	9: PutField(pc=28,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),UVar(defSites={4},value=int[][↦12;refId=105])),
	10: Assignment(pc=32,DVar(useSites={11},value={int[], null}[↦32;refId=111],origin=10),GetField(pc=32,java.util.regex.Pattern,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	11: ArrayStore(pc=37,UVar(defSites={10},value={int[], null}[↦32;refId=111]),UVar(defSites={-3},value=an int),UVar(defSites={-2},value=an int)),
	12: Return(pc=38)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_8,BB_4}
	BB_1: BasicBlock(start=5,end=8) -> {BB_8,BB_3}
	BB_2: BasicBlock(start=10,end=11) -> {BB_8,BB_5}
	BB_3: BasicBlock(start=9,end=9) -> {BB_2}
	BB_4: BasicBlock(start=2,end=2) -> {BB_6,BB_2}
	BB_5: BasicBlock(start=12,end=12) -> {BB_7}
	BB_6: BasicBlock(start=3,end=4) -> {BB_8,BB_1}
	BB_7: ExitNode(normalReturn=true)
	BB_8: ExitNode(normalReturn=false)
))

int peek()
AITACode(params=(Parameters(
	0: useSites={0,4,6,1} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Pattern,temp,int[],UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern,cursor,int,UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={8,6},value=an int,origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=103]))),
	3: Assignment(pc=11,DVar(useSites={4},value=int = 4,origin=3),IntConst(pc=11,4)),
	4: Assignment(pc=12,DVar(useSites={5},value=int ∈ [0,1],origin=4),VirtualFunctionCall(pc=12,java.util.regex.Pattern,isInterface=false,boolean has(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={3},value=int = 4)))),
	5: If(pc=15,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=8),
	6: Assignment(pc=20,DVar(useSites={8},value=an int,origin=6),VirtualFunctionCall(pc=20,java.util.regex.Pattern,isInterface=false,int peekPastWhitespace(int),UVar(defSites={-1},value=java.util.regex.Pattern[↦-1;refId=102]),(UVar(defSites={2},value=an int)))),
	7: Nop(pc=23),
	8: ReturnValue(pc=25,UVar(defSites={2,6},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_7,BB_4}
	BB_1: BasicBlock(start=5,end=5) -> {BB_6,BB_2}
	BB_2: BasicBlock(start=6,end=6) -> {BB_7,BB_3}
	BB_3: BasicBlock(start=7,end=7) -> {BB_6}
	BB_4: BasicBlock(start=3,end=4) -> {BB_7,BB_1}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=8,end=8) -> {BB_5}
	BB_7: ExitNode(normalReturn=false)
))

