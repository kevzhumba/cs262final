int getTextLength()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.lang.CharSequence, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Matcher,text,java.lang.CharSequence,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: Assignment(pc=4,DVar(useSites={2},value=an int,origin=1),VirtualFunctionCall(pc=4,java.lang.CharSequence,isInterface=true,int length(),UVar(defSites={0},value={_ <: java.lang.CharSequence, null}[↦1;refId=103]),())),
	2: ReturnValue(pc=9,UVar(defSites={1},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.lang.StringBuilder appendExpandedReplacement(java.lang.String,java.lang.StringBuilder)
AITACode(params=(Parameters(
	0: useSites={88,132,124,130,118,73,131,127} (origin=-1),
	1: useSites={20,26,1,33,13,109,3,35,107,7} (origin=-2),
	2: useSites={138,14,133,135} (origin=-3)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={136,2,6,3,19},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=4,DVar(useSites={2},value=an int,origin=1),VirtualFunctionCall(pc=4,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value={java.lang.String, null}[↦-2;refId=103]),())),
	2: If(pc=7,UVar(defSites={0,136,104,122,93,15},value=an int),>=,UVar(defSites={1},value=an int),target=138),
	3: Assignment(pc=12,DVar(useSites={18,5,135},value=int ∈ [0,65535],origin=3),VirtualFunctionCall(pc=12,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),(UVar(defSites={0,136,104,122,93,15},value=int ∈ [-2147483648,2147483646])))),
	4: Assignment(pc=19,DVar(useSites={5},value=int = 92,origin=4),IntConst(pc=19,92)),
	5: If(pc=21,UVar(defSites={3},value=int ∈ [0,65535]),!=,UVar(defSites={4},value=int = 92),target=17),
	6: Assignment(pc=24,DVar(useSites={8,13,15},value=int ∈ [-2147483647,2147483647],origin=6),BinaryExpr(pc=24,ComputationalTypeInt,UVar(defSites={0,136,104,122,93,15},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=24,1))),
	7: Assignment(pc=29,DVar(useSites={8},value=an int,origin=7),VirtualFunctionCall(pc=29,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),())),
	8: If(pc=32,UVar(defSites={6},value=int ∈ [-2147483647,2147483647]),!=,UVar(defSites={7},value=an int),target=13),
	9: Assignment(pc=35,DVar(useSites={12,11},value=java.lang.IllegalArgumentException[↦35;refId=1379],origin=9),New(pc=35,java.lang.IllegalArgumentException)),
	10: Assignment(pc=39,DVar(useSites={11},value=String("character to be escaped is missing")[@39;refId=1380],origin=10),StringConst(pc=39,character to be escaped is missing)),
	11: NonVirtualMethodCall(pc=41,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={9},value=java.lang.IllegalArgumentException[↦35;refId=1379]),(UVar(defSites={10},value=String("character to be escaped is missing")[@39;refId=1380]))),
	12: Throw(pc=44,UVar(defSites={9},value=java.lang.IllegalArgumentException[↦35;refId=1379])),
	13: Assignment(pc=47,DVar(useSites={14},value=int ∈ [0,65535],origin=13),VirtualFunctionCall(pc=47,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),(UVar(defSites={6},value=int ∈ [-2147483647,2147483647])))),
	14: ExprStmt(pc=55,VirtualFunctionCall(pc=55,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={-3},value={java.lang.StringBuilder, null}[↦-3;refId=104]),(UVar(defSites={13},value=int ∈ [0,65535])))),
	15: Assignment(pc=59,DVar(useSites={136,2,6,3,19},value=an int,origin=15),BinaryExpr(pc=59,ComputationalTypeInt,UVar(defSites={6},value=int ∈ [-2147483647,2147483647]),+,IntConst(pc=59,1))),
	16: Goto(pc=62,target=1),
	17: Assignment(pc=67,DVar(useSites={18},value=int = 36,origin=17),IntConst(pc=67,36)),
	18: If(pc=69,UVar(defSites={3},value=int ∈ [0,65535]),!=,UVar(defSites={17},value=int = 36),target=135),
	19: Assignment(pc=72,DVar(useSites={104,26,21,29},value=int ∈ [-2147483647,2147483647],origin=19),BinaryExpr(pc=72,ComputationalTypeInt,UVar(defSites={0,136,104,122,93,15},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=72,1))),
	20: Assignment(pc=77,DVar(useSites={21},value=an int,origin=20),VirtualFunctionCall(pc=77,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),())),
	21: If(pc=80,UVar(defSites={19},value=int ∈ [-2147483647,2147483647]),!=,UVar(defSites={20},value=an int),target=26),
	22: Assignment(pc=83,DVar(useSites={24,25},value=java.lang.IllegalArgumentException[↦83;refId=1371],origin=22),New(pc=83,java.lang.IllegalArgumentException)),
	23: Assignment(pc=87,DVar(useSites={24},value=String("Illegal group reference: group index is missing")[@87;refId=1372],origin=23),StringConst(pc=87,Illegal group reference: group index is missing)),
	24: NonVirtualMethodCall(pc=89,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={22},value=java.lang.IllegalArgumentException[↦83;refId=1371]),(UVar(defSites={23},value=String("Illegal group reference: group index is missing")[@87;refId=1372]))),
	25: Throw(pc=92,UVar(defSites={22},value=java.lang.IllegalArgumentException[↦83;refId=1371])),
	26: Assignment(pc=95,DVar(useSites={96,52,28},value=int ∈ [0,65535],origin=26),VirtualFunctionCall(pc=95,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),(UVar(defSites={19},value=int ∈ [-2147483647,2147483647])))),
	27: Assignment(pc=105,DVar(useSites={28},value=int = 123,origin=27),IntConst(pc=105,123)),
	28: If(pc=107,UVar(defSites={26},value=int ∈ [0,65535]),!=,UVar(defSites={27},value=int = 123),target=95),
	29: Assignment(pc=110,DVar(useSites={34,93,35,43},value=an int,origin=29),BinaryExpr(pc=110,ComputationalTypeInt,UVar(defSites={19},value=int ∈ [-2147483647,2147483647]),+,IntConst(pc=110,1))),
	30: Assignment(pc=113,DVar(useSites={42,57,45,31},value=java.lang.StringBuilder[↦113;refId=1369],origin=30),New(pc=113,java.lang.StringBuilder)),
	31: NonVirtualMethodCall(pc=117,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={30},value=java.lang.StringBuilder[↦113;refId=1369]),()),
	32: Nop(pc=120),
	33: Assignment(pc=124,DVar(useSites={34},value=an int,origin=33),VirtualFunctionCall(pc=124,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),())),
	34: If(pc=127,UVar(defSites={29,43},value=an int),>=,UVar(defSites={33},value=an int),target=45),
	35: Assignment(pc=132,DVar(useSites={40,36,52,42,38},value=int ∈ [0,65535],origin=35),VirtualFunctionCall(pc=132,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),(UVar(defSites={29,43},value=int ∈ [-2147483648,2147483646])))),
	36: Assignment(pc=139,DVar(useSites={37},value=int ∈ [0,1],origin=36),StaticFunctionCall(pc=139,java.util.regex.ASCII,isInterface=false,boolean isLower(int),(UVar(defSites={35},value=int ∈ [0,65535])))),
	37: If(pc=142,UVar(defSites={36},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=42),
	38: Assignment(pc=147,DVar(useSites={39},value=int ∈ [0,1],origin=38),StaticFunctionCall(pc=147,java.util.regex.ASCII,isInterface=false,boolean isUpper(int),(UVar(defSites={35},value=int ∈ [0,65535])))),
	39: If(pc=150,UVar(defSites={38},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=42),
	40: Assignment(pc=155,DVar(useSites={41},value=int ∈ [0,1],origin=40),StaticFunctionCall(pc=155,java.util.regex.ASCII,isInterface=false,boolean isDigit(int),(UVar(defSites={35},value=int ∈ [0,65535])))),
	41: If(pc=158,UVar(defSites={40},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=45),
	42: ExprStmt(pc=165,VirtualFunctionCall(pc=165,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={30},value=java.lang.StringBuilder[↦113;refId=113]),(UVar(defSites={35},value=int ∈ [0,65535])))),
	43: Assignment(pc=169,DVar(useSites={44,34,93,35},value=an int,origin=43),BinaryExpr(pc=169,ComputationalTypeInt,UVar(defSites={29,43},value=an int),+,IntConst(pc=169,1))),
	44: Goto(pc=172,target=33),
	45: Assignment(pc=177,DVar(useSites={46},value=an int,origin=45),VirtualFunctionCall(pc=177,java.lang.StringBuilder,isInterface=false,int length(),UVar(defSites={30},value=java.lang.StringBuilder[↦113;refId=113]),())),
	46: If(pc=180,UVar(defSites={45},value=an int),!=,IntConst(pc=-333,0),target=51),
	47: Assignment(pc=183,DVar(useSites={50,49},value=java.lang.IllegalArgumentException[↦183;refId=1391],origin=47),New(pc=183,java.lang.IllegalArgumentException)),
	48: Assignment(pc=187,DVar(useSites={49},value=String("named capturing group has 0 length name")[@187;refId=1392],origin=48),StringConst(pc=187,named capturing group has 0 length name)),
	49: NonVirtualMethodCall(pc=189,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={47},value=java.lang.IllegalArgumentException[↦183;refId=1391]),(UVar(defSites={48},value=String("named capturing group has 0 length name")[@187;refId=1392]))),
	50: Throw(pc=192,UVar(defSites={47},value=java.lang.IllegalArgumentException[↦183;refId=1391])),
	51: Assignment(pc=195,DVar(useSites={52},value=int = 125,origin=51),IntConst(pc=195,125)),
	52: If(pc=197,UVar(defSites={26,35},value=int ∈ [0,65535]),==,UVar(defSites={51},value=int = 125),target=57),
	53: Assignment(pc=200,DVar(useSites={56,55},value=java.lang.IllegalArgumentException[↦200;refId=1450],origin=53),New(pc=200,java.lang.IllegalArgumentException)),
	54: Assignment(pc=204,DVar(useSites={55},value=String("named capturing group is missing trailing '}'")[@204;refId=1451],origin=54),StringConst(pc=204,named capturing group is missing trailing '}')),
	55: NonVirtualMethodCall(pc=206,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={53},value=java.lang.IllegalArgumentException[↦200;refId=1450]),(UVar(defSites={54},value=String("named capturing group is missing trailing '}'")[@204;refId=1451]))),
	56: Throw(pc=209,UVar(defSites={53},value=java.lang.IllegalArgumentException[↦200;refId=1450])),
	57: Assignment(pc=212,DVar(useSites={82,90,67,75,59},value={java.lang.String, null}[↦212;refId=1395],origin=57),VirtualFunctionCall(pc=212,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={30},value=java.lang.StringBuilder[↦113;refId=113]),())),
	58: Assignment(pc=219,DVar(useSites={59},value=int = 0,origin=58),IntConst(pc=219,0)),
	59: Assignment(pc=220,DVar(useSites={60},value=int ∈ [0,65535],origin=59),VirtualFunctionCall(pc=220,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={57},value={java.lang.String, null}[↦212;refId=1395]),(UVar(defSites={58},value=int = 0)))),
	60: Assignment(pc=223,DVar(useSites={61},value=int ∈ [0,1],origin=60),StaticFunctionCall(pc=223,java.util.regex.ASCII,isInterface=false,boolean isDigit(int),(UVar(defSites={59},value=int ∈ [0,65535])))),
	61: If(pc=226,UVar(defSites={60},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=73),
	62: Assignment(pc=229,DVar(useSites={72,71},value=java.lang.IllegalArgumentException[↦229;refId=1399],origin=62),New(pc=229,java.lang.IllegalArgumentException)),
	63: Assignment(pc=233,DVar(useSites={64,66},value=java.lang.StringBuilder[↦233;refId=1400],origin=63),New(pc=233,java.lang.StringBuilder)),
	64: NonVirtualMethodCall(pc=237,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={63},value=java.lang.StringBuilder[↦233;refId=1400]),()),
	65: Assignment(pc=240,DVar(useSites={66},value=String("capturing group name {")[@240;refId=1402],origin=65),StringConst(pc=240,capturing group name {)),
	66: Assignment(pc=242,DVar(useSites={67},value={java.lang.StringBuilder, null}[↦242;refId=1404],origin=66),VirtualFunctionCall(pc=242,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={63},value=java.lang.StringBuilder[↦233;refId=1400]),(UVar(defSites={65},value=String("capturing group name {")[@240;refId=1402])))),
	67: Assignment(pc=247,DVar(useSites={69},value={java.lang.StringBuilder, null}[↦247;refId=1407],origin=67),VirtualFunctionCall(pc=247,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={66},value={java.lang.StringBuilder, null}[↦242;refId=1404]),(UVar(defSites={57},value=java.lang.String[↦212;refId=1395])))),
	68: Assignment(pc=250,DVar(useSites={69},value=String("} starts with digit character")[@250;refId=1408],origin=68),StringConst(pc=250,} starts with digit character)),
	69: Assignment(pc=252,DVar(useSites={70},value={java.lang.StringBuilder, null}[↦252;refId=1411],origin=69),VirtualFunctionCall(pc=252,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={67},value={java.lang.StringBuilder, null}[↦247;refId=1407]),(UVar(defSites={68},value=String("} starts with digit character")[@250;refId=1408])))),
	70: Assignment(pc=255,DVar(useSites={71},value={java.lang.String, null}[↦255;refId=1414],origin=70),VirtualFunctionCall(pc=255,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={69},value={java.lang.StringBuilder, null}[↦252;refId=1411]),())),
	71: NonVirtualMethodCall(pc=258,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={62},value=java.lang.IllegalArgumentException[↦229;refId=1399]),(UVar(defSites={70},value={java.lang.String, null}[↦255;refId=1414]))),
	72: Throw(pc=261,UVar(defSites={62},value=java.lang.IllegalArgumentException[↦229;refId=1399])),
	73: Assignment(pc=263,DVar(useSites={74},value={java.util.regex.Pattern, null}[↦263;refId=1416],origin=73),GetField(pc=263,java.util.regex.Matcher,parentPattern,java.util.regex.Pattern,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	74: Assignment(pc=266,DVar(useSites={75},value={_ <: java.util.Map, null}[↦266;refId=1419],origin=74),VirtualFunctionCall(pc=266,java.util.regex.Pattern,isInterface=false,java.util.Map namedGroups(),UVar(defSites={73},value={java.util.regex.Pattern, null}[↦263;refId=1416]),())),
	75: Assignment(pc=271,DVar(useSites={76},value=int ∈ [0,1],origin=75),VirtualFunctionCall(pc=271,java.util.Map,isInterface=true,boolean containsKey(java.lang.Object),UVar(defSites={74},value={_ <: java.util.Map, null}[↦266;refId=1419]),(UVar(defSites={57},value=java.lang.String[↦212;refId=1395])))),
	76: If(pc=276,UVar(defSites={75},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=88),
	77: Assignment(pc=279,DVar(useSites={86,87},value=java.lang.IllegalArgumentException[↦279;refId=1422],origin=77),New(pc=279,java.lang.IllegalArgumentException)),
	78: Assignment(pc=283,DVar(useSites={81,79},value=java.lang.StringBuilder[↦283;refId=1423],origin=78),New(pc=283,java.lang.StringBuilder)),
	79: NonVirtualMethodCall(pc=287,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={78},value=java.lang.StringBuilder[↦283;refId=1423]),()),
	80: Assignment(pc=290,DVar(useSites={81},value=String("No group with name {")[@290;refId=1425],origin=80),StringConst(pc=290,No group with name {)),
	81: Assignment(pc=292,DVar(useSites={82},value={java.lang.StringBuilder, null}[↦292;refId=1427],origin=81),VirtualFunctionCall(pc=292,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={78},value=java.lang.StringBuilder[↦283;refId=1423]),(UVar(defSites={80},value=String("No group with name {")[@290;refId=1425])))),
	82: Assignment(pc=297,DVar(useSites={84},value={java.lang.StringBuilder, null}[↦297;refId=1430],origin=82),VirtualFunctionCall(pc=297,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={81},value={java.lang.StringBuilder, null}[↦292;refId=1427]),(UVar(defSites={57},value=java.lang.String[↦212;refId=1395])))),
	83: Assignment(pc=300,DVar(useSites={84},value=String("}")[@300;refId=1431],origin=83),StringConst(pc=300,})),
	84: Assignment(pc=302,DVar(useSites={85},value={java.lang.StringBuilder, null}[↦302;refId=1434],origin=84),VirtualFunctionCall(pc=302,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={82},value={java.lang.StringBuilder, null}[↦297;refId=1430]),(UVar(defSites={83},value=String("}")[@300;refId=1431])))),
	85: Assignment(pc=305,DVar(useSites={86},value={java.lang.String, null}[↦305;refId=1437],origin=85),VirtualFunctionCall(pc=305,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={84},value={java.lang.StringBuilder, null}[↦302;refId=1434]),())),
	86: NonVirtualMethodCall(pc=308,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={77},value=java.lang.IllegalArgumentException[↦279;refId=1422]),(UVar(defSites={85},value={java.lang.String, null}[↦305;refId=1437]))),
	87: Throw(pc=311,UVar(defSites={77},value=java.lang.IllegalArgumentException[↦279;refId=1422])),
	88: Assignment(pc=313,DVar(useSites={89},value={java.util.regex.Pattern, null}[↦313;refId=1439],origin=88),GetField(pc=313,java.util.regex.Matcher,parentPattern,java.util.regex.Pattern,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	89: Assignment(pc=316,DVar(useSites={90},value={_ <: java.util.Map, null}[↦316;refId=1442],origin=89),VirtualFunctionCall(pc=316,java.util.regex.Pattern,isInterface=false,java.util.Map namedGroups(),UVar(defSites={88},value={java.util.regex.Pattern, null}[↦313;refId=1439]),())),
	90: Assignment(pc=321,DVar(useSites={92,91},value={_ <: java.lang.Object, null}[↦321;refId=1445],origin=90),VirtualFunctionCall(pc=321,java.util.Map,isInterface=true,java.lang.Object get(java.lang.Object),UVar(defSites={89},value={_ <: java.util.Map, null}[↦316;refId=1442]),(UVar(defSites={57},value=java.lang.String[↦212;refId=1395])))),
	91: Checkcast(pc=326,UVar(defSites={90},value={_ <: java.lang.Object, null}[↦321;refId=1445]),java.lang.Integer),
	92: Assignment(pc=329,DVar(useSites={132,124,131,127},value=an int,origin=92),VirtualFunctionCall(pc=329,java.lang.Integer,isInterface=false,int intValue(),UVar(defSites={90},value={java.lang.Integer, null}[↦321;refId=1446]),())),
	93: Assignment(pc=334,DVar(useSites={136,2,6,3,19},value=an int,origin=93),BinaryExpr(pc=334,ComputationalTypeInt,UVar(defSites={29,43},value=an int),+,IntConst(pc=334,1))),
	94: Goto(pc=337,target=124),
	95: Assignment(pc=342,DVar(useSites={96},value=int = 48,origin=95),IntConst(pc=342,48)),
	96: Assignment(pc=344,DVar(useSites={132,116,124,97,131,99,127},value=int ∈ [-48,65487],origin=96),BinaryExpr(pc=344,ComputationalTypeInt,UVar(defSites={26},value=int ∈ [0,65535]),-,UVar(defSites={95},value=int = 48))),
	97: If(pc=349,UVar(defSites={96},value=int ∈ [-48,65487]),<,IntConst(pc=-333,0),target=100),
	98: Assignment(pc=354,DVar(useSites={99},value=int = 9,origin=98),IntConst(pc=354,9)),
	99: If(pc=356,UVar(defSites={96},value=int ∈ [0,65487]),<=,UVar(defSites={98},value=int = 9),target=104),
	100: Assignment(pc=359,DVar(useSites={102,103},value=java.lang.IllegalArgumentException[↦359;refId=126],origin=100),New(pc=359,java.lang.IllegalArgumentException)),
	101: Assignment(pc=363,DVar(useSites={102},value=String("Illegal group reference")[@363;refId=127],origin=101),StringConst(pc=363,Illegal group reference)),
	102: NonVirtualMethodCall(pc=365,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={100},value=java.lang.IllegalArgumentException[↦359;refId=126]),(UVar(defSites={101},value=String("Illegal group reference")[@363;refId=127]))),
	103: Throw(pc=368,UVar(defSites={100},value=java.lang.IllegalArgumentException[↦359;refId=126])),
	104: Assignment(pc=369,DVar(useSites={136,108,2,122,6,109,3,19},value=an int,origin=104),BinaryExpr(pc=369,ComputationalTypeInt,UVar(defSites={19},value=int ∈ [-2147483647,2147483647]),+,IntConst(pc=369,1))),
	105: Assignment(pc=372,DVar(useSites={106},value=int = 0,origin=105),IntConst(pc=372,0)),
	106: If(pc=377,UVar(defSites={120,105},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=124),
	107: Assignment(pc=382,DVar(useSites={108},value=an int,origin=107),VirtualFunctionCall(pc=382,java.lang.String,isInterface=false,int length(),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),())),
	108: If(pc=385,UVar(defSites={104,122},value=an int),>=,UVar(defSites={107},value=an int),target=124),
	109: Assignment(pc=393,DVar(useSites={111},value=int ∈ [0,65535],origin=109),VirtualFunctionCall(pc=393,java.lang.String,isInterface=false,char charAt(int),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103]),(UVar(defSites={104,122},value=int ∈ [-2147483648,2147483646])))),
	110: Assignment(pc=396,DVar(useSites={111},value=int = 48,origin=110),IntConst(pc=396,48)),
	111: Assignment(pc=398,DVar(useSites={112,114,117},value=int ∈ [-48,65487],origin=111),BinaryExpr(pc=398,ComputationalTypeInt,UVar(defSites={109},value=int ∈ [0,65535]),-,UVar(defSites={110},value=int = 48))),
	112: If(pc=403,UVar(defSites={111},value=int ∈ [-48,65487]),<,IntConst(pc=-333,0),target=124),
	113: Assignment(pc=408,DVar(useSites={114},value=int = 9,origin=113),IntConst(pc=408,9)),
	114: If(pc=410,UVar(defSites={111},value=int ∈ [0,65487]),>,UVar(defSites={113},value=int = 9),target=124),
	115: Assignment(pc=418,DVar(useSites={116},value=int = 10,origin=115),IntConst(pc=418,10)),
	116: Assignment(pc=420,DVar(useSites={117},value=an int,origin=116),BinaryExpr(pc=420,ComputationalTypeInt,UVar(defSites={96,117},value=an int),*,UVar(defSites={115},value=int = 10))),
	117: Assignment(pc=423,DVar(useSites={132,116,124,131,119,127},value=an int,origin=117),BinaryExpr(pc=423,ComputationalTypeInt,UVar(defSites={116},value=an int),+,UVar(defSites={111},value=int ∈ [0,9]))),
	118: Assignment(pc=427,DVar(useSites={119},value=an int,origin=118),VirtualFunctionCall(pc=427,java.util.regex.Matcher,isInterface=false,int groupCount(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	119: If(pc=432,UVar(defSites={118},value=an int),>=,UVar(defSites={117},value=an int),target=122),
	120: Assignment(pc=435,DVar(useSites={106},value=int = 1,origin=120),IntConst(pc=435,1)),
	121: Goto(pc=438,target=106),
	122: Assignment(pc=445,DVar(useSites={136,108,2,6,109,3,19,123},value=int ∈ [-2147483647,2147483647],origin=122),BinaryExpr(pc=445,ComputationalTypeInt,UVar(defSites={104,122},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=445,1))),
	123: Goto(pc=448,target=106),
	124: Assignment(pc=454,DVar(useSites={126},value=an int,origin=124),VirtualFunctionCall(pc=454,java.util.regex.Matcher,isInterface=false,int start(int),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={96,92,117},value=an int)))),
	125: Assignment(pc=457,DVar(useSites={126},value=int = -1,origin=125),IntConst(pc=457,-1)),
	126: If(pc=458,UVar(defSites={124},value=an int),==,UVar(defSites={125},value=int = -1),target=137),
	127: Assignment(pc=464,DVar(useSites={129},value=an int,origin=127),VirtualFunctionCall(pc=464,java.util.regex.Matcher,isInterface=false,int end(int),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={96,92,117},value=an int)))),
	128: Assignment(pc=467,DVar(useSites={129},value=int = -1,origin=128),IntConst(pc=467,-1)),
	129: If(pc=468,UVar(defSites={127},value=an int),==,UVar(defSites={128},value=int = -1),target=137),
	130: Assignment(pc=473,DVar(useSites={133},value={_ <: java.lang.CharSequence, null}[↦473;refId=1384],origin=130),GetField(pc=473,java.util.regex.Matcher,text,java.lang.CharSequence,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	131: Assignment(pc=479,DVar(useSites={133},value=an int,origin=131),VirtualFunctionCall(pc=479,java.util.regex.Matcher,isInterface=false,int start(int),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={96,92,117},value=an int)))),
	132: Assignment(pc=485,DVar(useSites={133},value=an int,origin=132),VirtualFunctionCall(pc=485,java.util.regex.Matcher,isInterface=false,int end(int),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={96,92,117},value=an int)))),
	133: ExprStmt(pc=488,VirtualFunctionCall(pc=488,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.CharSequence,int,int),UVar(defSites={-3},value={java.lang.StringBuilder, null}[↦-3;refId=104]),(UVar(defSites={130},value={_ <: java.lang.CharSequence, null}[↦473;refId=1384]),UVar(defSites={131},value=an int),UVar(defSites={132},value=an int)))),
	134: Goto(pc=492,target=1),
	135: ExprStmt(pc=498,VirtualFunctionCall(pc=498,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(char),UVar(defSites={-3},value={java.lang.StringBuilder, null}[↦-3;refId=104]),(UVar(defSites={3},value=int ∈ [0,65535])))),
	136: Assignment(pc=502,DVar(useSites={2,6,137,3,19},value=an int,origin=136),BinaryExpr(pc=502,ComputationalTypeInt,UVar(defSites={0,136,104,122,93,15},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=502,1))),
	137: Goto(pc=505,target=1),
	138: ReturnValue(pc=509,UVar(defSites={-3},value={java.lang.StringBuilder, null}[↦-3;refId=104]))
),cfg=CFG(
	BB_0: BasicBlock(start=56,end=56) -> {BB_55}
	BB_10: BasicBlock(start=29,end=31) -> {BB_55,BB_2c}
	BB_11: BasicBlock(start=61,end=61) -> {BB_27,BB_59}
	BB_12: BasicBlock(start=132,end=132) -> {BB_55,BB_13}
	BB_13: BasicBlock(start=133,end=133) -> {BB_55,BB_26}
	BB_14: BasicBlock(start=1,end=1) -> {BB_55,BB_29}
	BB_15: BasicBlock(start=6,end=7) -> {BB_55,BB_4a}
	BB_16: BasicBlock(start=60,end=60) -> {BB_55,BB_11}
	BB_17: BasicBlock(start=85,end=85) -> {BB_55,BB_32}
	BB_18: BasicBlock(start=38,end=38) -> {BB_55,BB_35}
	BB_19: BasicBlock(start=70,end=70) -> {BB_55,BB_30}
	BB_1: BasicBlock(start=106,end=106) -> {BB_52,BB_22}
	BB_1a: BasicBlock(start=33,end=33) -> {BB_55,BB_2d}
	BB_1b: BasicBlock(start=21,end=21) -> {BB_49,BB_2e}
	BB_1c: BasicBlock(start=137,end=137) -> {BB_14}
	BB_1d: BasicBlock(start=92,end=92) -> {BB_55,BB_e}
	BB_1e: BasicBlock(start=65,end=66) -> {BB_55,BB_42}
	BB_1f: BasicBlock(start=9,end=11) -> {BB_55,BB_31}
	BB_20: BasicBlock(start=53,end=55) -> {BB_55,BB_0}
	BB_21: BasicBlock(start=109,end=109) -> {BB_55,BB_b}
	BB_22: BasicBlock(start=124,end=124) -> {BB_55,BB_c}
	BB_23: BasicBlock(start=77,end=79) -> {BB_55,BB_3d}
	BB_24: BasicBlock(start=13,end=13) -> {BB_55,BB_a}
	BB_25: BasicBlock(start=41,end=41) -> {BB_7,BB_2a}
	BB_26: BasicBlock(start=134,end=134) -> {BB_14}
	BB_27: BasicBlock(start=73,end=74) -> {BB_55,BB_4b}
	BB_28: BasicBlock(start=128,end=129) -> {BB_1c,BB_3a}
	BB_29: BasicBlock(start=2,end=2) -> {BB_2,BB_3c}
	BB_2: BasicBlock(start=138,end=138) -> {BB_3f}
	BB_2a: BasicBlock(start=45,end=45) -> {BB_55,BB_d}
	BB_2b: BasicBlock(start=17,end=18) -> {BB_51,BB_3b}
	BB_2c: BasicBlock(start=32,end=32) -> {BB_1a}
	BB_2d: BasicBlock(start=34,end=34) -> {BB_3e,BB_2a}
	BB_2e: BasicBlock(start=22,end=24) -> {BB_55,BB_9}
	BB_2f: BasicBlock(start=27,end=28) -> {BB_40,BB_10}
	BB_30: BasicBlock(start=71,end=71) -> {BB_55,BB_44}
	BB_31: BasicBlock(start=12,end=12) -> {BB_55}
	BB_32: BasicBlock(start=86,end=86) -> {BB_55,BB_46}
	BB_33: BasicBlock(start=113,end=114) -> {BB_5,BB_22}
	BB_34: BasicBlock(start=76,end=76) -> {BB_4,BB_23}
	BB_35: BasicBlock(start=39,end=39) -> {BB_7,BB_48}
	BB_36: BasicBlock(start=98,end=99) -> {BB_47,BB_5d}
	BB_37: BasicBlock(start=103,end=103) -> {BB_55}
	BB_38: BasicBlock(start=91,end=91) -> {BB_55,BB_1d}
	BB_39: BasicBlock(start=108,end=108) -> {BB_21,BB_22}
	BB_3: BasicBlock(start=0,end=0) -> {BB_14}
	BB_3a: BasicBlock(start=130,end=131) -> {BB_55,BB_12}
	BB_3b: BasicBlock(start=135,end=135) -> {BB_55,BB_54}
	BB_3c: BasicBlock(start=3,end=3) -> {BB_55,BB_53}
	BB_3d: BasicBlock(start=80,end=81) -> {BB_55,BB_4c}
	BB_3e: BasicBlock(start=35,end=35) -> {BB_55,BB_4f}
	BB_3f: ExitNode(normalReturn=true)
	BB_40: BasicBlock(start=95,end=97) -> {BB_36,BB_5d}
	BB_41: BasicBlock(start=50,end=50) -> {BB_55}
	BB_42: BasicBlock(start=67,end=67) -> {BB_55,BB_58}
	BB_43: BasicBlock(start=127,end=127) -> {BB_55,BB_28}
	BB_44: BasicBlock(start=72,end=72) -> {BB_55}
	BB_45: BasicBlock(start=43,end=44) -> {BB_1a}
	BB_46: BasicBlock(start=87,end=87) -> {BB_55}
	BB_47: BasicBlock(start=104,end=105) -> {BB_1}
	BB_48: BasicBlock(start=40,end=40) -> {BB_55,BB_25}
	BB_49: BasicBlock(start=26,end=26) -> {BB_55,BB_2f}
	BB_4: BasicBlock(start=88,end=89) -> {BB_55,BB_5a}
	BB_4a: BasicBlock(start=8,end=8) -> {BB_24,BB_1f}
	BB_4b: BasicBlock(start=75,end=75) -> {BB_55,BB_34}
	BB_4c: BasicBlock(start=82,end=82) -> {BB_55,BB_5c}
	BB_4d: BasicBlock(start=119,end=119) -> {BB_5b,BB_6}
	BB_4e: BasicBlock(start=58,end=59) -> {BB_55,BB_16}
	BB_4f: BasicBlock(start=36,end=36) -> {BB_55,BB_8}
	BB_50: BasicBlock(start=51,end=52) -> {BB_20,BB_f}
	BB_51: BasicBlock(start=19,end=20) -> {BB_55,BB_1b}
	BB_52: BasicBlock(start=107,end=107) -> {BB_55,BB_39}
	BB_53: BasicBlock(start=4,end=5) -> {BB_15,BB_2b}
	BB_54: BasicBlock(start=136,end=136) -> {BB_1c}
	BB_55: ExitNode(normalReturn=false)
	BB_56: BasicBlock(start=47,end=49) -> {BB_55,BB_41}
	BB_57: BasicBlock(start=15,end=16) -> {BB_14}
	BB_58: BasicBlock(start=68,end=69) -> {BB_55,BB_19}
	BB_59: BasicBlock(start=62,end=64) -> {BB_55,BB_1e}
	BB_5: BasicBlock(start=115,end=118) -> {BB_55,BB_4d}
	BB_5a: BasicBlock(start=90,end=90) -> {BB_55,BB_38}
	BB_5b: BasicBlock(start=122,end=123) -> {BB_1}
	BB_5c: BasicBlock(start=83,end=84) -> {BB_55,BB_17}
	BB_5d: BasicBlock(start=100,end=102) -> {BB_55,BB_37}
	BB_6: BasicBlock(start=120,end=121) -> {BB_1}
	BB_7: BasicBlock(start=42,end=42) -> {BB_55,BB_45}
	BB_8: BasicBlock(start=37,end=37) -> {BB_7,BB_18}
	BB_9: BasicBlock(start=25,end=25) -> {BB_55}
	BB_a: BasicBlock(start=14,end=14) -> {BB_55,BB_57}
	BB_b: BasicBlock(start=110,end=112) -> {BB_33,BB_22}
	BB_c: BasicBlock(start=125,end=126) -> {BB_1c,BB_43}
	BB_d: BasicBlock(start=46,end=46) -> {BB_50,BB_56}
	BB_e: BasicBlock(start=93,end=94) -> {BB_22}
	BB_f: BasicBlock(start=57,end=57) -> {BB_55,BB_4e}
))

java.lang.String replaceFirst(java.lang.String)
AITACode(params=(Parameters(
	0: useSites={8,6,14,5,13} (origin=-1),
	1: useSites={0,13} (origin=-2)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={java.lang.String, null}[↦-2;refId=103]),!=,NullExpr(pc=-333),target=5),
	1: Assignment(pc=4,DVar(useSites={4,3},value=java.lang.NullPointerException[↦4;refId=104],origin=1),New(pc=4,java.lang.NullPointerException)),
	2: Assignment(pc=8,DVar(useSites={3},value=String("replacement")[@8;refId=105],origin=2),StringConst(pc=8,replacement)),
	3: NonVirtualMethodCall(pc=10,java.lang.NullPointerException,isInterface=false,void <init>(java.lang.String),UVar(defSites={1},value=java.lang.NullPointerException[↦4;refId=104]),(UVar(defSites={2},value=String("replacement")[@8;refId=105]))),
	4: Throw(pc=13,UVar(defSites={1},value=java.lang.NullPointerException[↦4;refId=104])),
	5: ExprStmt(pc=15,VirtualFunctionCall(pc=15,java.util.regex.Matcher,isInterface=false,java.util.regex.Matcher reset(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	6: Assignment(pc=20,DVar(useSites={7},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=20,java.util.regex.Matcher,isInterface=false,boolean find(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	7: If(pc=23,UVar(defSites={6},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=11),
	8: Assignment(pc=27,DVar(useSites={9},value={_ <: java.lang.CharSequence, null}[↦27;refId=110],origin=8),GetField(pc=27,java.util.regex.Matcher,text,java.lang.CharSequence,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	9: Assignment(pc=30,DVar(useSites={10},value={java.lang.String, null}[↦30;refId=113],origin=9),VirtualFunctionCall(pc=30,java.lang.CharSequence,isInterface=true,java.lang.String toString(),UVar(defSites={8},value={_ <: java.lang.CharSequence, null}[↦27;refId=110]),())),
	10: ReturnValue(pc=35,UVar(defSites={9},value={java.lang.String, null}[↦30;refId=113])),
	11: Assignment(pc=36,DVar(useSites={12,14,13,15},value=java.lang.StringBuilder[↦36;refId=114],origin=11),New(pc=36,java.lang.StringBuilder)),
	12: NonVirtualMethodCall(pc=40,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={11},value=java.lang.StringBuilder[↦36;refId=114]),()),
	13: ExprStmt(pc=47,VirtualFunctionCall(pc=47,java.util.regex.Matcher,isInterface=false,java.util.regex.Matcher appendReplacement(java.lang.StringBuilder,java.lang.String),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={11},value=java.lang.StringBuilder[↦36;refId=114]),UVar(defSites={-2},value=java.lang.String[↦-2;refId=103])))),
	14: ExprStmt(pc=53,VirtualFunctionCall(pc=53,java.util.regex.Matcher,isInterface=false,java.lang.StringBuilder appendTail(java.lang.StringBuilder),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={11},value=java.lang.StringBuilder[↦36;refId=114])))),
	15: Assignment(pc=58,DVar(useSites={16},value={java.lang.String, null}[↦58;refId=121],origin=15),VirtualFunctionCall(pc=58,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={11},value=java.lang.StringBuilder[↦36;refId=114]),())),
	16: ReturnValue(pc=61,UVar(defSites={15},value={java.lang.String, null}[↦58;refId=121]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=5,end=5) -> {BB_e,BB_5}
	BB_2: BasicBlock(start=10,end=10) -> {BB_8}
	BB_3: BasicBlock(start=14,end=14) -> {BB_e,BB_c}
	BB_4: BasicBlock(start=1,end=3) -> {BB_e,BB_d}
	BB_5: BasicBlock(start=6,end=6) -> {BB_e,BB_7}
	BB_6: BasicBlock(start=13,end=13) -> {BB_e,BB_3}
	BB_7: BasicBlock(start=7,end=7) -> {BB_a,BB_b}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=16,end=16) -> {BB_8}
	BB_a: BasicBlock(start=11,end=12) -> {BB_e,BB_6}
	BB_b: BasicBlock(start=8,end=9) -> {BB_e,BB_2}
	BB_c: BasicBlock(start=15,end=15) -> {BB_e,BB_9}
	BB_d: BasicBlock(start=4,end=4) -> {BB_e}
	BB_e: ExitNode(normalReturn=false)
))

int groupCount()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={java.util.regex.Pattern, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.regex.Matcher,parentPattern,java.util.regex.Pattern,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: Assignment(pc=4,DVar(useSites={3},value=an int,origin=1),GetField(pc=4,java.util.regex.Pattern,capturingGroupCount,int,UVar(defSites={0},value={java.util.regex.Pattern, null}[↦1;refId=103]))),
	2: Assignment(pc=7,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=7,1)),
	3: Assignment(pc=8,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=8,ComputationalTypeInt,UVar(defSites={1},value=an int),-,UVar(defSites={2},value=int = 1))),
	4: ReturnValue(pc=9,UVar(defSites={3},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=4) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int start()
AITACode(params=(Parameters(
	0: useSites={0,6} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=an int),>=,IntConst(pc=-333,0),target=6),
	2: Assignment(pc=7,DVar(useSites={4,5},value=java.lang.IllegalStateException[↦7;refId=103],origin=2),New(pc=7,java.lang.IllegalStateException)),
	3: Assignment(pc=11,DVar(useSites={4},value=String("No match available")[@11;refId=104],origin=3),StringConst(pc=11,No match available)),
	4: NonVirtualMethodCall(pc=13,java.lang.IllegalStateException,isInterface=false,void <init>(java.lang.String),UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103]),(UVar(defSites={3},value=String("No match available")[@11;refId=104]))),
	5: Throw(pc=16,UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103])),
	6: Assignment(pc=18,DVar(useSites={7},value=an int,origin=6),GetField(pc=18,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	7: ReturnValue(pc=21,UVar(defSites={6},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_2,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_5}
	BB_2: BasicBlock(start=6,end=7) -> {BB_4}
	BB_3: BasicBlock(start=2,end=4) -> {BB_5,BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: ExitNode(normalReturn=false)
))

java.lang.StringBuilder appendTail(java.lang.StringBuilder)
AITACode(params=(Parameters(
	0: useSites={0,2,1} (origin=-1),
	1: useSites={4,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={3},value={_ <: java.lang.CharSequence, null}[↦2;refId=104],origin=0),GetField(pc=2,java.util.regex.Matcher,text,java.lang.CharSequence,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={3},value=an int,origin=1),GetField(pc=6,java.util.regex.Matcher,lastAppendPosition,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	2: Assignment(pc=10,DVar(useSites={3},value=an int,origin=2),VirtualFunctionCall(pc=10,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	3: ExprStmt(pc=13,VirtualFunctionCall(pc=13,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.CharSequence,int,int),UVar(defSites={-2},value={java.lang.StringBuilder, null}[↦-2;refId=103]),(UVar(defSites={0},value={_ <: java.lang.CharSequence, null}[↦2;refId=104]),UVar(defSites={1},value=an int),UVar(defSites={2},value=an int)))),
	4: ReturnValue(pc=18,UVar(defSites={-2},value=java.lang.StringBuilder[↦-2;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=3,end=3) -> {BB_4,BB_3}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=4,end=4) -> {BB_2}
	BB_4: ExitNode(normalReturn=false)
))

java.util.regex.Matcher appendReplacement(java.lang.StringBuilder,java.lang.String)
AITACode(params=(Parameters(
	0: useSites={0,16,8,20,10,14,9,19,11,15} (origin=-1),
	1: useSites={12,13} (origin=-2),
	2: useSites={8} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=an int),>=,IntConst(pc=-333,0),target=6),
	2: Assignment(pc=7,DVar(useSites={4,5},value=java.lang.IllegalStateException[↦7;refId=105],origin=2),New(pc=7,java.lang.IllegalStateException)),
	3: Assignment(pc=11,DVar(useSites={4},value=String("No match available")[@11;refId=106],origin=3),StringConst(pc=11,No match available)),
	4: NonVirtualMethodCall(pc=13,java.lang.IllegalStateException,isInterface=false,void <init>(java.lang.String),UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=105]),(UVar(defSites={3},value=String("No match available")[@11;refId=106]))),
	5: Throw(pc=16,UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=105])),
	6: Assignment(pc=17,DVar(useSites={8,13,7},value=java.lang.StringBuilder[↦17;refId=108],origin=6),New(pc=17,java.lang.StringBuilder)),
	7: NonVirtualMethodCall(pc=21,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={6},value=java.lang.StringBuilder[↦17;refId=108]),()),
	8: ExprStmt(pc=28,VirtualFunctionCall(pc=28,java.util.regex.Matcher,isInterface=false,java.lang.StringBuilder appendExpandedReplacement(java.lang.String,java.lang.StringBuilder),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={-3},value={java.lang.String, null}[↦-3;refId=104]),UVar(defSites={6},value=java.lang.StringBuilder[↦17;refId=108])))),
	9: Assignment(pc=34,DVar(useSites={12},value={_ <: java.lang.CharSequence, null}[↦34;refId=112],origin=9),GetField(pc=34,java.util.regex.Matcher,text,java.lang.CharSequence,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	10: Assignment(pc=38,DVar(useSites={12},value=an int,origin=10),GetField(pc=38,java.util.regex.Matcher,lastAppendPosition,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	11: Assignment(pc=42,DVar(useSites={12},value=an int,origin=11),GetField(pc=42,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	12: ExprStmt(pc=45,VirtualFunctionCall(pc=45,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.CharSequence,int,int),UVar(defSites={-2},value={java.lang.StringBuilder, null}[↦-2;refId=103]),(UVar(defSites={9},value={_ <: java.lang.CharSequence, null}[↦34;refId=112]),UVar(defSites={10},value=an int),UVar(defSites={11},value=an int)))),
	13: ExprStmt(pc=51,VirtualFunctionCall(pc=51,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.CharSequence),UVar(defSites={-2},value=java.lang.StringBuilder[↦-2;refId=103]),(UVar(defSites={6},value=java.lang.StringBuilder[↦17;refId=108])))),
	14: Assignment(pc=57,DVar(useSites={15},value=an int,origin=14),GetField(pc=57,java.util.regex.Matcher,last,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	15: PutField(pc=60,java.util.regex.Matcher,lastAppendPosition,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={14},value=an int)),
	16: Assignment(pc=65,DVar(useSites={18},value=an int,origin=16),GetField(pc=65,java.util.regex.Matcher,modCount,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	17: Assignment(pc=68,DVar(useSites={18},value=int = 1,origin=17),IntConst(pc=68,1)),
	18: Assignment(pc=69,DVar(useSites={19},value=an int,origin=18),BinaryExpr(pc=69,ComputationalTypeInt,UVar(defSites={16},value=an int),+,UVar(defSites={17},value=int = 1))),
	19: PutField(pc=70,java.util.regex.Matcher,modCount,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={18},value=an int)),
	20: ReturnValue(pc=74,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_6}
	BB_1: BasicBlock(start=5,end=5) -> {BB_9}
	BB_2: BasicBlock(start=14,end=20) -> {BB_7}
	BB_3: BasicBlock(start=6,end=7) -> {BB_9,BB_8}
	BB_4: BasicBlock(start=9,end=12) -> {BB_9,BB_5}
	BB_5: BasicBlock(start=13,end=13) -> {BB_9,BB_2}
	BB_6: BasicBlock(start=2,end=4) -> {BB_9,BB_1}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=8,end=8) -> {BB_9,BB_4}
	BB_9: ExitNode(normalReturn=false)
))

boolean find(int)
AITACode(params=(Parameters(
	0: useSites={0,8,7} (origin=-1),
	1: useSites={8,2,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=an int,origin=0),VirtualFunctionCall(pc=1,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	1: If(pc=6,UVar(defSites={-2},value=an int),<,IntConst(pc=-333,0),target=3),
	2: If(pc=11,UVar(defSites={-2},value=int ∈ [0,2147483647]),<=,UVar(defSites={0},value=an int),target=7),
	3: Assignment(pc=14,DVar(useSites={6,5},value=java.lang.IndexOutOfBoundsException[↦14;refId=107],origin=3),New(pc=14,java.lang.IndexOutOfBoundsException)),
	4: Assignment(pc=18,DVar(useSites={5},value=String("Illegal start index")[@18;refId=108],origin=4),StringConst(pc=18,Illegal start index)),
	5: NonVirtualMethodCall(pc=20,java.lang.IndexOutOfBoundsException,isInterface=false,void <init>(java.lang.String),UVar(defSites={3},value=java.lang.IndexOutOfBoundsException[↦14;refId=107]),(UVar(defSites={4},value=String("Illegal start index")[@18;refId=108]))),
	6: Throw(pc=23,UVar(defSites={3},value=java.lang.IndexOutOfBoundsException[↦14;refId=107])),
	7: ExprStmt(pc=25,VirtualFunctionCall(pc=25,java.util.regex.Matcher,isInterface=false,java.util.regex.Matcher reset(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	8: Assignment(pc=31,DVar(useSites={9},value=int ∈ [0,1],origin=8),VirtualFunctionCall(pc=31,java.util.regex.Matcher,isInterface=false,boolean search(int),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={-2},value=int ∈ [0,2147483647])))),
	9: ReturnValue(pc=34,UVar(defSites={8},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_9,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_6,BB_4}
	BB_2: BasicBlock(start=6,end=6) -> {BB_9}
	BB_3: BasicBlock(start=9,end=9) -> {BB_7}
	BB_4: BasicBlock(start=2,end=2) -> {BB_5,BB_6}
	BB_5: BasicBlock(start=7,end=7) -> {BB_9,BB_8}
	BB_6: BasicBlock(start=3,end=5) -> {BB_9,BB_2}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=8,end=8) -> {BB_9,BB_3}
	BB_9: ExitNode(normalReturn=false)
))

int end(int)
AITACode(params=(Parameters(
	0: useSites={0,18,7} (origin=-1),
	1: useSites={8,20,6,14} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=an int),>=,IntConst(pc=-333,0),target=6),
	2: Assignment(pc=7,DVar(useSites={4,5},value=java.lang.IllegalStateException[↦7;refId=103],origin=2),New(pc=7,java.lang.IllegalStateException)),
	3: Assignment(pc=11,DVar(useSites={4},value=String("No match available")[@11;refId=104],origin=3),StringConst(pc=11,No match available)),
	4: NonVirtualMethodCall(pc=13,java.lang.IllegalStateException,isInterface=false,void <init>(java.lang.String),UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103]),(UVar(defSites={3},value=String("No match available")[@11;refId=104]))),
	5: Throw(pc=16,UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103])),
	6: If(pc=18,UVar(defSites={-2},value=an int),<,IntConst(pc=-333,0),target=9),
	7: Assignment(pc=23,DVar(useSites={8},value=an int,origin=7),VirtualFunctionCall(pc=23,java.util.regex.Matcher,isInterface=false,int groupCount(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	8: If(pc=26,UVar(defSites={-2},value=int ∈ [0,2147483647]),<=,UVar(defSites={7},value=an int),target=18),
	9: Assignment(pc=29,DVar(useSites={16,17},value=java.lang.IndexOutOfBoundsException[↦29;refId=110],origin=9),New(pc=29,java.lang.IndexOutOfBoundsException)),
	10: Assignment(pc=33,DVar(useSites={13,11},value=java.lang.StringBuilder[↦33;refId=111],origin=10),New(pc=33,java.lang.StringBuilder)),
	11: NonVirtualMethodCall(pc=37,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={10},value=java.lang.StringBuilder[↦33;refId=111]),()),
	12: Assignment(pc=40,DVar(useSites={13},value=String("No group ")[@40;refId=113],origin=12),StringConst(pc=40,No group )),
	13: Assignment(pc=42,DVar(useSites={14},value={java.lang.StringBuilder, null}[↦42;refId=115],origin=13),VirtualFunctionCall(pc=42,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={10},value=java.lang.StringBuilder[↦33;refId=111]),(UVar(defSites={12},value=String("No group ")[@40;refId=113])))),
	14: Assignment(pc=46,DVar(useSites={15},value={java.lang.StringBuilder, null}[↦46;refId=118],origin=14),VirtualFunctionCall(pc=46,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(int),UVar(defSites={13},value={java.lang.StringBuilder, null}[↦42;refId=115]),(UVar(defSites={-2},value=an int)))),
	15: Assignment(pc=49,DVar(useSites={16},value={java.lang.String, null}[↦49;refId=121],origin=15),VirtualFunctionCall(pc=49,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={14},value={java.lang.StringBuilder, null}[↦46;refId=118]),())),
	16: NonVirtualMethodCall(pc=52,java.lang.IndexOutOfBoundsException,isInterface=false,void <init>(java.lang.String),UVar(defSites={9},value=java.lang.IndexOutOfBoundsException[↦29;refId=110]),(UVar(defSites={15},value={java.lang.String, null}[↦49;refId=121]))),
	17: Throw(pc=55,UVar(defSites={9},value=java.lang.IndexOutOfBoundsException[↦29;refId=110])),
	18: Assignment(pc=57,DVar(useSites={23},value={int[], null}[↦57;refId=107],origin=18),GetField(pc=57,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	19: Assignment(pc=61,DVar(useSites={20},value=int = 2,origin=19),IntConst(pc=61,2)),
	20: Assignment(pc=62,DVar(useSites={22},value=an int,origin=20),BinaryExpr(pc=62,ComputationalTypeInt,UVar(defSites={-2},value=int ∈ [0,2147483647]),*,UVar(defSites={19},value=int = 2))),
	21: Assignment(pc=63,DVar(useSites={22},value=int = 1,origin=21),IntConst(pc=63,1)),
	22: Assignment(pc=64,DVar(useSites={23},value=an int,origin=22),BinaryExpr(pc=64,ComputationalTypeInt,UVar(defSites={20},value=an int),+,UVar(defSites={21},value=int = 1))),
	23: Assignment(pc=65,DVar(useSites={24},value=an int,origin=23),ArrayLoad(pc=65,UVar(defSites={22},value=an int),UVar(defSites={18},value={int[], null}[↦57;refId=107]))),
	24: ReturnValue(pc=66,UVar(defSites={23},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_6}
	BB_1: BasicBlock(start=5,end=5) -> {BB_c}
	BB_2: BasicBlock(start=24,end=24) -> {BB_f}
	BB_3: BasicBlock(start=14,end=14) -> {BB_c,BB_d}
	BB_4: BasicBlock(start=6,end=6) -> {BB_9,BB_5}
	BB_5: BasicBlock(start=9,end=11) -> {BB_c,BB_8}
	BB_6: BasicBlock(start=2,end=4) -> {BB_c,BB_1}
	BB_7: BasicBlock(start=17,end=17) -> {BB_c}
	BB_8: BasicBlock(start=12,end=13) -> {BB_c,BB_3}
	BB_9: BasicBlock(start=7,end=7) -> {BB_c,BB_b}
	BB_a: BasicBlock(start=16,end=16) -> {BB_c,BB_7}
	BB_b: BasicBlock(start=8,end=8) -> {BB_e,BB_5}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=15) -> {BB_c,BB_a}
	BB_e: BasicBlock(start=18,end=23) -> {BB_c,BB_2}
	BB_f: ExitNode(normalReturn=true)
))

int end()
AITACode(params=(Parameters(
	0: useSites={0,6} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=an int),>=,IntConst(pc=-333,0),target=6),
	2: Assignment(pc=7,DVar(useSites={4,5},value=java.lang.IllegalStateException[↦7;refId=103],origin=2),New(pc=7,java.lang.IllegalStateException)),
	3: Assignment(pc=11,DVar(useSites={4},value=String("No match available")[@11;refId=104],origin=3),StringConst(pc=11,No match available)),
	4: NonVirtualMethodCall(pc=13,java.lang.IllegalStateException,isInterface=false,void <init>(java.lang.String),UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103]),(UVar(defSites={3},value=String("No match available")[@11;refId=104]))),
	5: Throw(pc=16,UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103])),
	6: Assignment(pc=18,DVar(useSites={7},value=an int,origin=6),GetField(pc=18,java.util.regex.Matcher,last,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	7: ReturnValue(pc=21,UVar(defSites={6},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_2,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_5}
	BB_2: BasicBlock(start=6,end=7) -> {BB_4}
	BB_3: BasicBlock(start=2,end=4) -> {BB_5,BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: ExitNode(normalReturn=false)
))

int start(int)
AITACode(params=(Parameters(
	0: useSites={0,18,7} (origin=-1),
	1: useSites={8,20,6,14} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=an int),>=,IntConst(pc=-333,0),target=6),
	2: Assignment(pc=7,DVar(useSites={4,5},value=java.lang.IllegalStateException[↦7;refId=103],origin=2),New(pc=7,java.lang.IllegalStateException)),
	3: Assignment(pc=11,DVar(useSites={4},value=String("No match available")[@11;refId=104],origin=3),StringConst(pc=11,No match available)),
	4: NonVirtualMethodCall(pc=13,java.lang.IllegalStateException,isInterface=false,void <init>(java.lang.String),UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103]),(UVar(defSites={3},value=String("No match available")[@11;refId=104]))),
	5: Throw(pc=16,UVar(defSites={2},value=java.lang.IllegalStateException[↦7;refId=103])),
	6: If(pc=18,UVar(defSites={-2},value=an int),<,IntConst(pc=-333,0),target=9),
	7: Assignment(pc=23,DVar(useSites={8},value=an int,origin=7),VirtualFunctionCall(pc=23,java.util.regex.Matcher,isInterface=false,int groupCount(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	8: If(pc=26,UVar(defSites={-2},value=int ∈ [0,2147483647]),<=,UVar(defSites={7},value=an int),target=18),
	9: Assignment(pc=29,DVar(useSites={16,17},value=java.lang.IndexOutOfBoundsException[↦29;refId=110],origin=9),New(pc=29,java.lang.IndexOutOfBoundsException)),
	10: Assignment(pc=33,DVar(useSites={13,11},value=java.lang.StringBuilder[↦33;refId=111],origin=10),New(pc=33,java.lang.StringBuilder)),
	11: NonVirtualMethodCall(pc=37,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={10},value=java.lang.StringBuilder[↦33;refId=111]),()),
	12: Assignment(pc=40,DVar(useSites={13},value=String("No group ")[@40;refId=113],origin=12),StringConst(pc=40,No group )),
	13: Assignment(pc=42,DVar(useSites={14},value={java.lang.StringBuilder, null}[↦42;refId=115],origin=13),VirtualFunctionCall(pc=42,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={10},value=java.lang.StringBuilder[↦33;refId=111]),(UVar(defSites={12},value=String("No group ")[@40;refId=113])))),
	14: Assignment(pc=46,DVar(useSites={15},value={java.lang.StringBuilder, null}[↦46;refId=118],origin=14),VirtualFunctionCall(pc=46,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(int),UVar(defSites={13},value={java.lang.StringBuilder, null}[↦42;refId=115]),(UVar(defSites={-2},value=an int)))),
	15: Assignment(pc=49,DVar(useSites={16},value={java.lang.String, null}[↦49;refId=121],origin=15),VirtualFunctionCall(pc=49,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={14},value={java.lang.StringBuilder, null}[↦46;refId=118]),())),
	16: NonVirtualMethodCall(pc=52,java.lang.IndexOutOfBoundsException,isInterface=false,void <init>(java.lang.String),UVar(defSites={9},value=java.lang.IndexOutOfBoundsException[↦29;refId=110]),(UVar(defSites={15},value={java.lang.String, null}[↦49;refId=121]))),
	17: Throw(pc=55,UVar(defSites={9},value=java.lang.IndexOutOfBoundsException[↦29;refId=110])),
	18: Assignment(pc=57,DVar(useSites={21},value={int[], null}[↦57;refId=107],origin=18),GetField(pc=57,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	19: Assignment(pc=61,DVar(useSites={20},value=int = 2,origin=19),IntConst(pc=61,2)),
	20: Assignment(pc=62,DVar(useSites={21},value=an int,origin=20),BinaryExpr(pc=62,ComputationalTypeInt,UVar(defSites={-2},value=int ∈ [0,2147483647]),*,UVar(defSites={19},value=int = 2))),
	21: Assignment(pc=63,DVar(useSites={22},value=an int,origin=21),ArrayLoad(pc=63,UVar(defSites={20},value=an int),UVar(defSites={18},value={int[], null}[↦57;refId=107]))),
	22: ReturnValue(pc=64,UVar(defSites={21},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_5}
	BB_1: BasicBlock(start=5,end=5) -> {BB_c}
	BB_2: BasicBlock(start=14,end=14) -> {BB_c,BB_d}
	BB_3: BasicBlock(start=6,end=6) -> {BB_9,BB_4}
	BB_4: BasicBlock(start=9,end=11) -> {BB_c,BB_8}
	BB_5: BasicBlock(start=2,end=4) -> {BB_c,BB_1}
	BB_6: BasicBlock(start=17,end=17) -> {BB_c}
	BB_7: BasicBlock(start=22,end=22) -> {BB_f}
	BB_8: BasicBlock(start=12,end=13) -> {BB_c,BB_2}
	BB_9: BasicBlock(start=7,end=7) -> {BB_c,BB_b}
	BB_a: BasicBlock(start=16,end=16) -> {BB_c,BB_6}
	BB_b: BasicBlock(start=8,end=8) -> {BB_e,BB_4}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=15) -> {BB_c,BB_a}
	BB_e: BasicBlock(start=18,end=21) -> {BB_c,BB_7}
	BB_f: ExitNode(normalReturn=true)
))

java.util.regex.Matcher reset()
AITACode(params=(Parameters(
	0: useSites={16,40,28,10,42,46,1,41,25,5,37,45,3,19,7,39,31} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = -1,origin=0),IntConst(pc=1,-1)),
	1: PutField(pc=2,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={0},value=int = -1)),
	2: Assignment(pc=6,DVar(useSites={3},value=int = 0,origin=2),IntConst(pc=6,0)),
	3: PutField(pc=7,java.util.regex.Matcher,last,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={2},value=int = 0)),
	4: Assignment(pc=11,DVar(useSites={5},value=int = -1,origin=4),IntConst(pc=11,-1)),
	5: PutField(pc=12,java.util.regex.Matcher,oldLast,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={4},value=int = -1)),
	6: Assignment(pc=15,DVar(useSites={12,9,13},value=int = 0,origin=6),IntConst(pc=15,0)),
	7: Assignment(pc=19,DVar(useSites={8},value={int[], null}[↦19;refId=433],origin=7),GetField(pc=19,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	8: Assignment(pc=22,DVar(useSites={9},value=int ∈ [0,2147483647],origin=8),ArrayLength(pc=22,UVar(defSites={7},value={int[], null}[↦19;refId=433]))),
	9: If(pc=23,UVar(defSites={6,13},value=int ∈ [0,2147483647]),>=,UVar(defSites={8},value=int ∈ [0,2147483647]),target=15),
	10: Assignment(pc=27,DVar(useSites={12},value={int[], null}[↦27;refId=435],origin=10),GetField(pc=27,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	11: Assignment(pc=31,DVar(useSites={12},value=int = -1,origin=11),IntConst(pc=31,-1)),
	12: ArrayStore(pc=32,UVar(defSites={10},value={int[], null}[↦27;refId=435]),UVar(defSites={6,13},value=int ∈ [0,2147483646]),UVar(defSites={11},value=int = -1)),
	13: Assignment(pc=33,DVar(useSites={12,14,9},value=int ∈ [1,2147483647],origin=13),BinaryExpr(pc=33,ComputationalTypeInt,UVar(defSites={6,13},value=int ∈ [0,2147483646]),+,IntConst(pc=33,1))),
	14: Goto(pc=36,target=7),
	15: Assignment(pc=39,DVar(useSites={18,22,21},value=int = 0,origin=15),IntConst(pc=39,0)),
	16: Assignment(pc=43,DVar(useSites={17},value={int[], null}[↦43;refId=438],origin=16),GetField(pc=43,java.util.regex.Matcher,locals,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	17: Assignment(pc=46,DVar(useSites={18},value=int ∈ [0,2147483647],origin=17),ArrayLength(pc=46,UVar(defSites={16},value={int[], null}[↦43;refId=438]))),
	18: If(pc=47,UVar(defSites={22,15},value=int ∈ [0,2147483647]),>=,UVar(defSites={17},value=int ∈ [0,2147483647]),target=24),
	19: Assignment(pc=51,DVar(useSites={21},value={int[], null}[↦51;refId=440],origin=19),GetField(pc=51,java.util.regex.Matcher,locals,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	20: Assignment(pc=55,DVar(useSites={21},value=int = -1,origin=20),IntConst(pc=55,-1)),
	21: ArrayStore(pc=56,UVar(defSites={19},value={int[], null}[↦51;refId=440]),UVar(defSites={22,15},value=int ∈ [0,2147483646]),UVar(defSites={20},value=int = -1)),
	22: Assignment(pc=57,DVar(useSites={18,21,23},value=int ∈ [1,2147483647],origin=22),BinaryExpr(pc=57,ComputationalTypeInt,UVar(defSites={22,15},value=int ∈ [0,2147483646]),+,IntConst(pc=57,1))),
	23: Goto(pc=60,target=16),
	24: Assignment(pc=63,DVar(useSites={32,34,29,27},value=int = 0,origin=24),IntConst(pc=63,0)),
	25: Assignment(pc=67,DVar(useSites={26},value={_ <: java.util.regex.IntHashSet[], null}[↦67;refId=586],origin=25),GetField(pc=67,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	26: Assignment(pc=70,DVar(useSites={27},value=int ∈ [0,2147483647],origin=26),ArrayLength(pc=70,UVar(defSites={25},value={_ <: java.util.regex.IntHashSet[], null}[↦67;refId=586]))),
	27: If(pc=71,UVar(defSites={24,34},value=an int),>=,UVar(defSites={26},value=int ∈ [0,2147483647]),target=36),
	28: Assignment(pc=75,DVar(useSites={29},value={_ <: java.util.regex.IntHashSet[], null}[↦75;refId=589],origin=28),GetField(pc=75,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	29: Assignment(pc=79,DVar(useSites={30},value={_ <: java.util.regex.IntHashSet, null}[↦79;refId=592],origin=29),ArrayLoad(pc=79,UVar(defSites={24,34},value=int ∈ [-2147483648,2147483646]),UVar(defSites={28},value={_ <: java.util.regex.IntHashSet[], null}[↦75;refId=589]))),
	30: If(pc=80,UVar(defSites={29},value={_ <: java.util.regex.IntHashSet, null}[↦79;refId=592]),==,NullExpr(pc=-333),target=34),
	31: Assignment(pc=84,DVar(useSites={32},value={_ <: java.util.regex.IntHashSet[], null}[↦84;refId=593],origin=31),GetField(pc=84,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	32: Assignment(pc=88,DVar(useSites={33},value={_ <: java.util.regex.IntHashSet, null}[↦88;refId=596],origin=32),ArrayLoad(pc=88,UVar(defSites={24,34},value=int ∈ [-2147483648,2147483646]),UVar(defSites={31},value={_ <: java.util.regex.IntHashSet[], null}[↦84;refId=593]))),
	33: VirtualMethodCall(pc=89,java.util.regex.IntHashSet,isInterface=false,void clear(),UVar(defSites={32},value={_ <: java.util.regex.IntHashSet, null}[↦88;refId=596]),()),
	34: Assignment(pc=92,DVar(useSites={32,29,35,27},value=an int,origin=34),BinaryExpr(pc=92,ComputationalTypeInt,UVar(defSites={24,34},value=an int),+,IntConst(pc=92,1))),
	35: Goto(pc=95,target=25),
	36: Assignment(pc=99,DVar(useSites={37},value=int = 0,origin=36),IntConst(pc=99,0)),
	37: PutField(pc=100,java.util.regex.Matcher,lastAppendPosition,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={36},value=int = 0)),
	38: Assignment(pc=104,DVar(useSites={39},value=int = 0,origin=38),IntConst(pc=104,0)),
	39: PutField(pc=105,java.util.regex.Matcher,from,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={38},value=int = 0)),
	40: Assignment(pc=110,DVar(useSites={41},value=an int,origin=40),VirtualFunctionCall(pc=110,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	41: PutField(pc=113,java.util.regex.Matcher,to,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={40},value=an int)),
	42: Assignment(pc=118,DVar(useSites={44},value=an int,origin=42),GetField(pc=118,java.util.regex.Matcher,modCount,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	43: Assignment(pc=121,DVar(useSites={44},value=int = 1,origin=43),IntConst(pc=121,1)),
	44: Assignment(pc=122,DVar(useSites={45},value=an int,origin=44),BinaryExpr(pc=122,ComputationalTypeInt,UVar(defSites={42},value=an int),+,UVar(defSites={43},value=int = 1))),
	45: PutField(pc=123,java.util.regex.Matcher,modCount,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={44},value=an int)),
	46: ReturnValue(pc=127,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=6) -> {BB_4}
	BB_10: ExitNode(normalReturn=true)
	BB_11: BasicBlock(start=16,end=17) -> {BB_5,BB_f}
	BB_12: BasicBlock(start=31,end=32) -> {BB_5,BB_a}
	BB_13: BasicBlock(start=36,end=40) -> {BB_5,BB_c}
	BB_14: BasicBlock(start=30,end=30) -> {BB_3,BB_12}
	BB_15: BasicBlock(start=19,end=21) -> {BB_5,BB_d}
	BB_1: BasicBlock(start=10,end=12) -> {BB_5,BB_b}
	BB_2: BasicBlock(start=9,end=9) -> {BB_1,BB_6}
	BB_3: BasicBlock(start=34,end=35) -> {BB_8}
	BB_4: BasicBlock(start=7,end=8) -> {BB_5,BB_2}
	BB_5: ExitNode(normalReturn=false)
	BB_6: BasicBlock(start=15,end=15) -> {BB_11}
	BB_7: BasicBlock(start=24,end=24) -> {BB_8}
	BB_8: BasicBlock(start=25,end=26) -> {BB_5,BB_e}
	BB_9: BasicBlock(start=28,end=29) -> {BB_5,BB_14}
	BB_a: BasicBlock(start=33,end=33) -> {BB_5,BB_3}
	BB_b: BasicBlock(start=13,end=14) -> {BB_4}
	BB_c: BasicBlock(start=41,end=46) -> {BB_10}
	BB_d: BasicBlock(start=22,end=23) -> {BB_11}
	BB_e: BasicBlock(start=27,end=27) -> {BB_13,BB_9}
	BB_f: BasicBlock(start=18,end=18) -> {BB_15,BB_7}
))

boolean search(int)
AITACode(params=(Parameters(
	0: useSites={8,40,24,36,12,44,18,46,30,1,49,9,37,13,45,3,43,27,39,15} (origin=-1),
	1: useSites={8,40,4,13} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=1,0)),
	1: PutField(pc=2,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={0},value=int = 0)),
	2: Assignment(pc=6,DVar(useSites={3},value=int = 0,origin=2),IntConst(pc=6,0)),
	3: PutField(pc=7,java.util.regex.Matcher,requireEnd,boolean,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={2},value=int = 0)),
	4: If(pc=11,UVar(defSites={-2},value=an int),>=,IntConst(pc=-333,0),target=7),
	5: Assignment(pc=14,DVar(useSites={8,40,13},value=int = 0,origin=5),IntConst(pc=14,0)),
	6: Goto(pc=15,target=8),
	7: Nop(pc=18),
	8: PutField(pc=22,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={-2,5},value=int ∈ [0,2147483647])),
	9: Assignment(pc=27,DVar(useSites={10},value=an int,origin=9),GetField(pc=27,java.util.regex.Matcher,oldLast,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	10: If(pc=30,UVar(defSites={9},value=an int),>=,IntConst(pc=-333,0),target=12),
	11: Goto(pc=34,target=13),
	12: Assignment(pc=38,DVar(useSites={13},value=an int,origin=12),GetField(pc=38,java.util.regex.Matcher,oldLast,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	13: PutField(pc=41,java.util.regex.Matcher,oldLast,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={12,-2,5},value=an int)),
	14: Assignment(pc=44,DVar(useSites={20,17,21},value=int = 0,origin=14),IntConst(pc=44,0)),
	15: Assignment(pc=48,DVar(useSites={16},value={int[], null}[↦48;refId=383],origin=15),GetField(pc=48,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	16: Assignment(pc=51,DVar(useSites={17},value=int ∈ [0,2147483647],origin=16),ArrayLength(pc=51,UVar(defSites={15},value={int[], null}[↦48;refId=383]))),
	17: If(pc=52,UVar(defSites={14,21},value=int ∈ [0,2147483647]),>=,UVar(defSites={16},value=int ∈ [0,2147483647]),target=23),
	18: Assignment(pc=56,DVar(useSites={20},value={int[], null}[↦56;refId=385],origin=18),GetField(pc=56,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	19: Assignment(pc=60,DVar(useSites={20},value=int = -1,origin=19),IntConst(pc=60,-1)),
	20: ArrayStore(pc=61,UVar(defSites={18},value={int[], null}[↦56;refId=385]),UVar(defSites={14,21},value=int ∈ [0,2147483646]),UVar(defSites={19},value=int = -1)),
	21: Assignment(pc=62,DVar(useSites={20,22,17},value=int ∈ [1,2147483647],origin=21),BinaryExpr(pc=62,ComputationalTypeInt,UVar(defSites={14,21},value=int ∈ [0,2147483646]),+,IntConst(pc=62,1))),
	22: Goto(pc=65,target=15),
	23: Assignment(pc=68,DVar(useSites={28,26,33,31},value=int = 0,origin=23),IntConst(pc=68,0)),
	24: Assignment(pc=72,DVar(useSites={25},value={_ <: java.util.regex.IntHashSet[], null}[↦72;refId=586],origin=24),GetField(pc=72,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	25: Assignment(pc=75,DVar(useSites={26},value=int ∈ [0,2147483647],origin=25),ArrayLength(pc=75,UVar(defSites={24},value={_ <: java.util.regex.IntHashSet[], null}[↦72;refId=586]))),
	26: If(pc=76,UVar(defSites={33,23},value=an int),>=,UVar(defSites={25},value=int ∈ [0,2147483647]),target=35),
	27: Assignment(pc=80,DVar(useSites={28},value={_ <: java.util.regex.IntHashSet[], null}[↦80;refId=594],origin=27),GetField(pc=80,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	28: Assignment(pc=84,DVar(useSites={29},value={_ <: java.util.regex.IntHashSet, null}[↦84;refId=597],origin=28),ArrayLoad(pc=84,UVar(defSites={33,23},value=int ∈ [-2147483648,2147483646]),UVar(defSites={27},value={_ <: java.util.regex.IntHashSet[], null}[↦80;refId=594]))),
	29: If(pc=85,UVar(defSites={28},value={_ <: java.util.regex.IntHashSet, null}[↦84;refId=597]),==,NullExpr(pc=-333),target=33),
	30: Assignment(pc=89,DVar(useSites={31},value={_ <: java.util.regex.IntHashSet[], null}[↦89;refId=598],origin=30),GetField(pc=89,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	31: Assignment(pc=93,DVar(useSites={32},value={_ <: java.util.regex.IntHashSet, null}[↦93;refId=601],origin=31),ArrayLoad(pc=93,UVar(defSites={33,23},value=int ∈ [-2147483648,2147483646]),UVar(defSites={30},value={_ <: java.util.regex.IntHashSet[], null}[↦89;refId=598]))),
	32: VirtualMethodCall(pc=94,java.util.regex.IntHashSet,isInterface=false,void clear(),UVar(defSites={31},value={_ <: java.util.regex.IntHashSet, null}[↦93;refId=601]),()),
	33: Assignment(pc=97,DVar(useSites={28,34,26,31},value=an int,origin=33),BinaryExpr(pc=97,ComputationalTypeInt,UVar(defSites={33,23},value=an int),+,IntConst(pc=97,1))),
	34: Goto(pc=100,target=24),
	35: Assignment(pc=104,DVar(useSites={36},value=int = 0,origin=35),IntConst(pc=104,0)),
	36: PutField(pc=105,java.util.regex.Matcher,acceptMode,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={35},value=int = 0)),
	37: Assignment(pc=109,DVar(useSites={38},value={java.util.regex.Pattern, null}[↦109;refId=588],origin=37),GetField(pc=109,java.util.regex.Matcher,parentPattern,java.util.regex.Pattern,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	38: Assignment(pc=112,DVar(useSites={40},value={_ <: java.util.regex.Pattern$Node, null}[↦112;refId=589],origin=38),GetField(pc=112,java.util.regex.Pattern,root,java.util.regex.Pattern$Node,UVar(defSites={37},value={java.util.regex.Pattern, null}[↦109;refId=588]))),
	39: Assignment(pc=118,DVar(useSites={40},value={_ <: java.lang.CharSequence, null}[↦118;refId=591],origin=39),GetField(pc=118,java.util.regex.Matcher,text,java.lang.CharSequence,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	40: Assignment(pc=121,DVar(useSites={50,41},value=int ∈ [0,1],origin=40),VirtualFunctionCall(pc=121,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={38},value={_ <: java.util.regex.Pattern$Node, null}[↦112;refId=589]),(UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={-2,5},value=int ∈ [0,2147483647]),UVar(defSites={39},value={_ <: java.lang.CharSequence, null}[↦118;refId=591])))),
	41: If(pc=126,UVar(defSites={40},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=44),
	42: Assignment(pc=130,DVar(useSites={43},value=int = -1,origin=42),IntConst(pc=130,-1)),
	43: PutField(pc=131,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={42},value=int = -1)),
	44: Assignment(pc=136,DVar(useSites={45},value=an int,origin=44),GetField(pc=136,java.util.regex.Matcher,last,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	45: PutField(pc=139,java.util.regex.Matcher,oldLast,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={44},value=an int)),
	46: Assignment(pc=144,DVar(useSites={48},value=an int,origin=46),GetField(pc=144,java.util.regex.Matcher,modCount,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	47: Assignment(pc=147,DVar(useSites={48},value=int = 1,origin=47),IntConst(pc=147,1)),
	48: Assignment(pc=148,DVar(useSites={49},value=an int,origin=48),BinaryExpr(pc=148,ComputationalTypeInt,UVar(defSites={46},value=an int),+,UVar(defSites={47},value=int = 1))),
	49: PutField(pc=149,java.util.regex.Matcher,modCount,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={48},value=an int)),
	50: ReturnValue(pc=153,UVar(defSites={40},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=4) -> {BB_14,BB_1}
	BB_10: BasicBlock(start=32,end=32) -> {BB_8,BB_d}
	BB_11: BasicBlock(start=17,end=17) -> {BB_19,BB_16}
	BB_12: BasicBlock(start=44,end=50) -> {BB_17}
	BB_13: BasicBlock(start=27,end=28) -> {BB_8,BB_2}
	BB_14: BasicBlock(start=7,end=7) -> {BB_6}
	BB_15: BasicBlock(start=39,end=40) -> {BB_8,BB_f}
	BB_16: BasicBlock(start=18,end=20) -> {BB_8,BB_c}
	BB_17: ExitNode(normalReturn=true)
	BB_18: BasicBlock(start=26,end=26) -> {BB_4,BB_13}
	BB_19: BasicBlock(start=23,end=23) -> {BB_b}
	BB_1: BasicBlock(start=5,end=6) -> {BB_6}
	BB_2: BasicBlock(start=29,end=29) -> {BB_7,BB_d}
	BB_3: BasicBlock(start=12,end=12) -> {BB_e}
	BB_4: BasicBlock(start=35,end=38) -> {BB_8,BB_15}
	BB_5: BasicBlock(start=11,end=11) -> {BB_e}
	BB_6: BasicBlock(start=8,end=10) -> {BB_5,BB_3}
	BB_7: BasicBlock(start=30,end=31) -> {BB_8,BB_10}
	BB_8: ExitNode(normalReturn=false)
	BB_9: BasicBlock(start=15,end=16) -> {BB_8,BB_11}
	BB_a: BasicBlock(start=42,end=43) -> {BB_12}
	BB_b: BasicBlock(start=24,end=25) -> {BB_8,BB_18}
	BB_c: BasicBlock(start=21,end=22) -> {BB_9}
	BB_d: BasicBlock(start=33,end=34) -> {BB_b}
	BB_e: BasicBlock(start=13,end=14) -> {BB_9}
	BB_f: BasicBlock(start=41,end=41) -> {BB_12,BB_a}
))

void <init>(java.util.regex.Pattern,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,16,8,4,12,2,10,26,6,14,30,29,23,15} (origin=-1),
	1: useSites={24,17,27,15} (origin=-2),
	2: useSites={16} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 0,origin=1),IntConst(pc=5,0)),
	2: PutField(pc=6,java.util.regex.Matcher,acceptMode,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={1},value=int = 0)),
	3: Assignment(pc=10,DVar(useSites={4},value=int = -1,origin=3),IntConst(pc=10,-1)),
	4: PutField(pc=11,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={3},value=int = -1)),
	5: Assignment(pc=15,DVar(useSites={6},value=int = 0,origin=5),IntConst(pc=15,0)),
	6: PutField(pc=16,java.util.regex.Matcher,last,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={5},value=int = 0)),
	7: Assignment(pc=20,DVar(useSites={8},value=int = -1,origin=7),IntConst(pc=20,-1)),
	8: PutField(pc=21,java.util.regex.Matcher,oldLast,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={7},value=int = -1)),
	9: Assignment(pc=25,DVar(useSites={10},value=int = 0,origin=9),IntConst(pc=25,0)),
	10: PutField(pc=26,java.util.regex.Matcher,lastAppendPosition,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={9},value=int = 0)),
	11: Assignment(pc=30,DVar(useSites={12},value=int = 0,origin=11),IntConst(pc=30,0)),
	12: PutField(pc=31,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={11},value=int = 0)),
	13: Assignment(pc=35,DVar(useSites={14},value=int = 1,origin=13),IntConst(pc=35,1)),
	14: PutField(pc=36,java.util.regex.Matcher,anchoringBounds,boolean,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={13},value=int = 1)),
	15: PutField(pc=41,java.util.regex.Matcher,parentPattern,java.util.regex.Pattern,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={-2},value={java.util.regex.Pattern, null}[↦-2;refId=103])),
	16: PutField(pc=46,java.util.regex.Matcher,text,java.lang.CharSequence,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={-3},value={_ <: java.lang.CharSequence, null}[↦-3;refId=104])),
	17: Assignment(pc=50,DVar(useSites={19},value=an int,origin=17),GetField(pc=50,java.util.regex.Pattern,capturingGroupCount,int,UVar(defSites={-2},value={java.util.regex.Pattern, null}[↦-2;refId=103]))),
	18: Assignment(pc=53,DVar(useSites={19},value=int = 10,origin=18),IntConst(pc=53,10)),
	19: Assignment(pc=55,DVar(useSites={21},value=an int,origin=19),StaticFunctionCall(pc=55,java.lang.Math,isInterface=false,int max(int,int),(UVar(defSites={17},value=an int),UVar(defSites={18},value=int = 10)))),
	20: Assignment(pc=61,DVar(useSites={21},value=int = 2,origin=20),IntConst(pc=61,2)),
	21: Assignment(pc=62,DVar(useSites={22},value=an int,origin=21),BinaryExpr(pc=62,ComputationalTypeInt,UVar(defSites={19},value=an int),*,UVar(defSites={20},value=int = 2))),
	22: Assignment(pc=63,DVar(useSites={23},value=int[][↦63;refId=108],origin=22),NewArray(pc=63,[UVar(defSites={21},value=an int)],int[])),
	23: PutField(pc=65,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={22},value=int[][↦63;refId=108])),
	24: Assignment(pc=70,DVar(useSites={25},value=an int,origin=24),GetField(pc=70,java.util.regex.Pattern,localCount,int,UVar(defSites={-2},value=java.util.regex.Pattern[↦-2;refId=103]))),
	25: Assignment(pc=73,DVar(useSites={26},value=int[][↦73;refId=110],origin=25),NewArray(pc=73,[UVar(defSites={24},value=an int)],int[])),
	26: PutField(pc=75,java.util.regex.Matcher,locals,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={25},value=int[][↦73;refId=110])),
	27: Assignment(pc=80,DVar(useSites={28},value=an int,origin=27),GetField(pc=80,java.util.regex.Pattern,localTCNCount,int,UVar(defSites={-2},value=java.util.regex.Pattern[↦-2;refId=103]))),
	28: Assignment(pc=83,DVar(useSites={29},value=java.util.regex.IntHashSet[][↦83;refId=112],origin=28),NewArray(pc=83,[UVar(defSites={27},value=an int)],java.util.regex.IntHashSet[])),
	29: PutField(pc=86,java.util.regex.Matcher,localsPos,java.util.regex.IntHashSet[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),UVar(defSites={28},value=java.util.regex.IntHashSet[][↦83;refId=112])),
	30: ExprStmt(pc=90,VirtualFunctionCall(pc=90,java.util.regex.Matcher,isInterface=false,java.util.regex.Matcher reset(),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),())),
	31: Return(pc=94)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=17) -> {BB_3,BB_6}
	BB_2: BasicBlock(start=31,end=31) -> {BB_7}
	BB_3: ExitNode(normalReturn=false)
	BB_4: BasicBlock(start=20,end=22) -> {BB_3,BB_9}
	BB_5: BasicBlock(start=29,end=30) -> {BB_3,BB_2}
	BB_6: BasicBlock(start=18,end=19) -> {BB_3,BB_4}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=26,end=28) -> {BB_3,BB_5}
	BB_9: BasicBlock(start=23,end=25) -> {BB_3,BB_8}
))

boolean find()
AITACode(params=(Parameters(
	0: useSites={0,4,20,10,6,1,13,7} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={8,20,2,5,3},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,last,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	1: Assignment(pc=7,DVar(useSites={2},value=an int,origin=1),GetField(pc=7,java.util.regex.Matcher,first,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	2: If(pc=10,UVar(defSites={0},value=an int),!=,UVar(defSites={1},value=an int),target=4),
	3: Assignment(pc=13,DVar(useSites={8,20,5},value=an int,origin=3),BinaryExpr(pc=13,ComputationalTypeInt,UVar(defSites={0},value=an int),+,IntConst(pc=13,1))),
	4: Assignment(pc=18,DVar(useSites={5},value=an int,origin=4),GetField(pc=18,java.util.regex.Matcher,from,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	5: If(pc=21,UVar(defSites={0,3},value=an int),>=,UVar(defSites={4},value=an int),target=7),
	6: Assignment(pc=25,DVar(useSites={8,20},value=an int,origin=6),GetField(pc=25,java.util.regex.Matcher,from,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	7: Assignment(pc=31,DVar(useSites={8},value=an int,origin=7),GetField(pc=31,java.util.regex.Matcher,to,int,UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	8: If(pc=34,UVar(defSites={0,6,3},value=an int),<=,UVar(defSites={7},value=an int),target=20),
	9: Assignment(pc=37,DVar(useSites={16,12,15},value=int = 0,origin=9),IntConst(pc=37,0)),
	10: Assignment(pc=41,DVar(useSites={11},value={int[], null}[↦41;refId=204],origin=10),GetField(pc=41,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	11: Assignment(pc=44,DVar(useSites={12},value=int ∈ [0,2147483647],origin=11),ArrayLength(pc=44,UVar(defSites={10},value={int[], null}[↦41;refId=204]))),
	12: If(pc=45,UVar(defSites={16,9},value=int ∈ [0,2147483647]),>=,UVar(defSites={11},value=int ∈ [0,2147483647]),target=18),
	13: Assignment(pc=49,DVar(useSites={15},value={int[], null}[↦49;refId=206],origin=13),GetField(pc=49,java.util.regex.Matcher,groups,int[],UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]))),
	14: Assignment(pc=53,DVar(useSites={15},value=int = -1,origin=14),IntConst(pc=53,-1)),
	15: ArrayStore(pc=54,UVar(defSites={13},value={int[], null}[↦49;refId=206]),UVar(defSites={16,9},value=int ∈ [0,2147483646]),UVar(defSites={14},value=int = -1)),
	16: Assignment(pc=55,DVar(useSites={12,17,15},value=int ∈ [1,2147483647],origin=16),BinaryExpr(pc=55,ComputationalTypeInt,UVar(defSites={16,9},value=int ∈ [0,2147483646]),+,IntConst(pc=55,1))),
	17: Goto(pc=58,target=10),
	18: Assignment(pc=61,DVar(useSites={19},value=int = 0,origin=18),IntConst(pc=61,0)),
	19: ReturnValue(pc=62,UVar(defSites={18},value=int = 0)),
	20: Assignment(pc=65,DVar(useSites={21},value=int ∈ [0,1],origin=20),VirtualFunctionCall(pc=65,java.util.regex.Matcher,isInterface=false,boolean search(int),UVar(defSites={-1},value=java.util.regex.Matcher[↦-1;refId=102]),(UVar(defSites={0,6,3},value=an int)))),
	21: ReturnValue(pc=68,UVar(defSites={20},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_d,BB_9}
	BB_1: BasicBlock(start=10,end=11) -> {BB_e,BB_7}
	BB_2: BasicBlock(start=20,end=20) -> {BB_e,BB_4}
	BB_3: BasicBlock(start=6,end=6) -> {BB_8}
	BB_4: BasicBlock(start=21,end=21) -> {BB_c}
	BB_5: BasicBlock(start=9,end=9) -> {BB_1}
	BB_6: BasicBlock(start=13,end=15) -> {BB_e,BB_a}
	BB_7: BasicBlock(start=12,end=12) -> {BB_6,BB_b}
	BB_8: BasicBlock(start=7,end=8) -> {BB_5,BB_2}
	BB_9: BasicBlock(start=3,end=3) -> {BB_d}
	BB_a: BasicBlock(start=16,end=17) -> {BB_1}
	BB_b: BasicBlock(start=18,end=19) -> {BB_c}
	BB_c: ExitNode(normalReturn=true)
	BB_d: BasicBlock(start=4,end=5) -> {BB_3,BB_8}
	BB_e: ExitNode(normalReturn=false)
))

