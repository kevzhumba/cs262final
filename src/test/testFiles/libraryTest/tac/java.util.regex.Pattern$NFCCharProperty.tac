boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={6} (origin=-1),
	1: useSites={0,5,3,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=5,1)),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=6,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={1},value=int = 1))),
	3: PutField(pc=7,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={2},value=an int)),
	4: Assignment(pc=11,DVar(useSites={5},value=int = 0,origin=4),IntConst(pc=11,0)),
	5: PutField(pc=12,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={4},value=int = 0)),
	6: Assignment(pc=16,DVar(useSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=105],origin=6),GetField(pc=16,java.util.regex.Pattern$NFCCharProperty,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NFCCharProperty[↦-1;refId=102]))),
	7: Assignment(pc=20,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=20,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=105]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	8: ReturnValue(pc=23,UVar(defSites={7},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=1,end=7) -> {BB_4,BB_3}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=8,end=8) -> {BB_2}
	BB_4: ExitNode(normalReturn=false)
))

void <init>(java.util.regex.Pattern$CharPredicate)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NFCCharProperty[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$NFCCharProperty,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NFCCharProperty[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦-2;refId=103])),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={32,18,37,15} (origin=-1),
	1: useSites={0,38,46,5,19,51} (origin=-2),
	2: useSites={24,4,2,1,21,13} (origin=-3),
	3: useSites={2,42,38,19,7,23} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=5,UVar(defSites={-3},value=an int),>=,UVar(defSites={0},value=an int),target=50),
	2: Assignment(pc=10,DVar(useSites={16,8,3},value=an int,origin=2),StaticFunctionCall(pc=10,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	3: Assignment(pc=17,DVar(useSites={4,21,13},value=an int,origin=3),StaticFunctionCall(pc=17,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={2},value=an int)))),
	4: Assignment(pc=25,DVar(useSites={24,44,42,6,38,22,14,19,11,7,47},value=an int,origin=4),BinaryExpr(pc=25,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={3},value=an int))),
	5: Assignment(pc=31,DVar(useSites={6},value=an int,origin=5),GetField(pc=31,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	6: If(pc=34,UVar(defSites={4,11},value=an int),>=,UVar(defSites={5},value=an int),target=13),
	7: Assignment(pc=40,DVar(useSites={16,8,10},value=an int,origin=7),StaticFunctionCall(pc=40,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={4,11},value=int ∈ [-2147483648,2147483646])))),
	8: Assignment(pc=49,DVar(useSites={9},value=int ∈ [0,1],origin=8),StaticFunctionCall(pc=49,java.util.regex.Grapheme,isInterface=false,boolean isBoundary(int,int),(UVar(defSites={2,7},value=an int),UVar(defSites={7},value=an int)))),
	9: If(pc=52,UVar(defSites={8},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=13),
	10: Assignment(pc=66,DVar(useSites={11},value=an int,origin=10),StaticFunctionCall(pc=66,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={7},value=an int)))),
	11: Assignment(pc=69,DVar(useSites={24,12,44,42,6,38,22,14,19,7,47},value=an int,origin=11),BinaryExpr(pc=69,ComputationalTypeInt,UVar(defSites={4,11},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={10},value=an int))),
	12: Goto(pc=72,target=5),
	13: Assignment(pc=78,DVar(useSites={14},value=an int,origin=13),BinaryExpr(pc=78,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={3},value=an int))),
	14: If(pc=81,UVar(defSites={13},value=an int),!=,UVar(defSites={4,11},value=an int),target=21),
	15: Assignment(pc=85,DVar(useSites={16},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦85;refId=111],origin=15),GetField(pc=85,java.util.regex.Pattern$NFCCharProperty,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NFCCharProperty[↦-1;refId=102]))),
	16: Assignment(pc=90,DVar(useSites={17},value=int ∈ [0,1],origin=16),VirtualFunctionCall(pc=90,java.util.regex.Pattern$CharPredicate,isInterface=true,boolean is(int),UVar(defSites={15},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦85;refId=111]),(UVar(defSites={2,7},value=an int)))),
	17: If(pc=95,UVar(defSites={16},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=46),
	18: Assignment(pc=99,DVar(useSites={19},value={_ <: java.util.regex.Pattern$Node, null}[↦99;refId=114],origin=18),GetField(pc=99,java.util.regex.Pattern$NFCCharProperty,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NFCCharProperty[↦-1;refId=102]))),
	19: Assignment(pc=106,DVar(useSites={20},value=int ∈ [0,1],origin=19),VirtualFunctionCall(pc=106,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={18},value={_ <: java.util.regex.Pattern$Node, null}[↦99;refId=114]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={4,11},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	20: ReturnValue(pc=109,UVar(defSites={19},value=int ∈ [0,1])),
	21: Assignment(pc=113,DVar(useSites={22},value=an int,origin=21),BinaryExpr(pc=113,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={3},value=an int))),
	22: If(pc=116,UVar(defSites={21},value=an int),>=,UVar(defSites={4,44,11},value=an int),target=46),
	23: Assignment(pc=120,DVar(useSites={24},value={java.lang.String, null}[↦120;refId=119],origin=23),VirtualFunctionCall(pc=120,java.lang.CharSequence,isInterface=true,java.lang.String toString(),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),())),
	24: Assignment(pc=128,DVar(useSites={26},value={java.lang.String, null}[↦128;refId=122],origin=24),VirtualFunctionCall(pc=128,java.lang.String,isInterface=false,java.lang.String substring(int,int),UVar(defSites={23},value={java.lang.String, null}[↦120;refId=119]),(UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),UVar(defSites={4,44,11},value=int ∈ [-2147483647,2147483647])))),
	25: Assignment(pc=131,DVar(useSites={26},value={java.text.Normalizer$Form, null}[↦131;refId=123],origin=25),GetStatic(pc=131,java.text.Normalizer$Form,NFC,java.text.Normalizer$Form)),
	26: Assignment(pc=134,DVar(useSites={28,34,29},value={java.lang.String, null}[↦134;refId=125],origin=26),StaticFunctionCall(pc=134,java.text.Normalizer,isInterface=false,java.lang.String normalize(java.lang.CharSequence,java.text.Normalizer$Form),(UVar(defSites={24},value={java.lang.String, null}[↦128;refId=122]),UVar(defSites={25},value={java.text.Normalizer$Form, null}[↦131;refId=123])))),
	27: Assignment(pc=141,DVar(useSites={29},value=int = 0,origin=27),IntConst(pc=141,0)),
	28: Assignment(pc=144,DVar(useSites={29},value=an int,origin=28),VirtualFunctionCall(pc=144,java.lang.String,isInterface=false,int length(),UVar(defSites={26},value={java.lang.String, null}[↦134;refId=125]),())),
	29: Assignment(pc=147,DVar(useSites={31},value=an int,origin=29),VirtualFunctionCall(pc=147,java.lang.String,isInterface=false,int codePointCount(int,int),UVar(defSites={26},value=java.lang.String[↦134;refId=125]),(UVar(defSites={27},value=int = 0),UVar(defSites={28},value=an int)))),
	30: Assignment(pc=150,DVar(useSites={31},value=int = 1,origin=30),IntConst(pc=150,1)),
	31: If(pc=151,UVar(defSites={29},value=an int),!=,UVar(defSites={30},value=int = 1),target=42),
	32: Assignment(pc=155,DVar(useSites={35},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦155;refId=129],origin=32),GetField(pc=155,java.util.regex.Pattern$NFCCharProperty,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NFCCharProperty[↦-1;refId=102]))),
	33: Assignment(pc=160,DVar(useSites={34},value=int = 0,origin=33),IntConst(pc=160,0)),
	34: Assignment(pc=161,DVar(useSites={35},value=an int,origin=34),VirtualFunctionCall(pc=161,java.lang.String,isInterface=false,int codePointAt(int),UVar(defSites={26},value=java.lang.String[↦134;refId=125]),(UVar(defSites={33},value=int = 0)))),
	35: Assignment(pc=164,DVar(useSites={36},value=int ∈ [0,1],origin=35),VirtualFunctionCall(pc=164,java.util.regex.Pattern$CharPredicate,isInterface=true,boolean is(int),UVar(defSites={32},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦155;refId=129]),(UVar(defSites={34},value=an int)))),
	36: If(pc=169,UVar(defSites={35},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=42),
	37: Assignment(pc=173,DVar(useSites={38},value={_ <: java.util.regex.Pattern$Node, null}[↦173;refId=133],origin=37),GetField(pc=173,java.util.regex.Pattern$NFCCharProperty,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NFCCharProperty[↦-1;refId=102]))),
	38: Assignment(pc=180,DVar(useSites={39},value=int ∈ [0,1],origin=38),VirtualFunctionCall(pc=180,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={37},value={_ <: java.util.regex.Pattern$Node, null}[↦173;refId=133]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={4,44,11},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	39: If(pc=183,UVar(defSites={38},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=42),
	40: Assignment(pc=186,DVar(useSites={41},value=int = 1,origin=40),IntConst(pc=186,1)),
	41: ReturnValue(pc=187,UVar(defSites={40},value=int = 1)),
	42: Assignment(pc=191,DVar(useSites={43},value=an int,origin=42),StaticFunctionCall(pc=191,java.lang.Character,isInterface=false,int codePointBefore(java.lang.CharSequence,int),(UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),UVar(defSites={4,44,11},value=int ∈ [-2147483647,2147483647])))),
	43: Assignment(pc=200,DVar(useSites={44},value=an int,origin=43),StaticFunctionCall(pc=200,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={42},value=an int)))),
	44: Assignment(pc=203,DVar(useSites={24,42,38,22,45,47},value=an int,origin=44),BinaryExpr(pc=203,ComputationalTypeInt,UVar(defSites={4,44,11},value=int ∈ [-2147483647,2147483647]),-,UVar(defSites={43},value=an int))),
	45: Goto(pc=206,target=21),
	46: Assignment(pc=212,DVar(useSites={47},value=an int,origin=46),GetField(pc=212,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	47: If(pc=215,UVar(defSites={4,44,11},value=an int),>=,UVar(defSites={46},value=an int),target=50),
	48: Assignment(pc=218,DVar(useSites={49},value=int = 0,origin=48),IntConst(pc=218,0)),
	49: ReturnValue(pc=219,UVar(defSites={48},value=int = 0)),
	50: Assignment(pc=221,DVar(useSites={51},value=int = 1,origin=50),IntConst(pc=221,1)),
	51: PutField(pc=222,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={50},value=int = 1)),
	52: Assignment(pc=225,DVar(useSites={53},value=int = 0,origin=52),IntConst(pc=225,0)),
	53: ReturnValue(pc=226,UVar(defSites={52},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_24,BB_3}
	BB_10: BasicBlock(start=46,end=47) -> {BB_8,BB_1a}
	BB_11: BasicBlock(start=29,end=29) -> {BB_24,BB_22}
	BB_12: BasicBlock(start=32,end=34) -> {BB_24,BB_19}
	BB_13: BasicBlock(start=17,end=17) -> {BB_1b,BB_10}
	BB_14: BasicBlock(start=44,end=45) -> {BB_4}
	BB_15: BasicBlock(start=27,end=28) -> {BB_24,BB_11}
	BB_16: BasicBlock(start=7,end=7) -> {BB_24,BB_9}
	BB_17: BasicBlock(start=39,end=39) -> {BB_b,BB_1f}
	BB_18: BasicBlock(start=3,end=3) -> {BB_24,BB_23}
	BB_19: BasicBlock(start=35,end=35) -> {BB_24,BB_21}
	BB_1: BasicBlock(start=5,end=6) -> {BB_16,BB_6}
	BB_1a: BasicBlock(start=48,end=49) -> {BB_1c}
	BB_1b: BasicBlock(start=18,end=19) -> {BB_24,BB_f}
	BB_1c: ExitNode(normalReturn=true)
	BB_1d: BasicBlock(start=11,end=12) -> {BB_1}
	BB_1e: BasicBlock(start=43,end=43) -> {BB_24,BB_14}
	BB_1f: BasicBlock(start=40,end=41) -> {BB_1c}
	BB_20: BasicBlock(start=23,end=23) -> {BB_24,BB_c}
	BB_21: BasicBlock(start=36,end=36) -> {BB_d,BB_b}
	BB_22: BasicBlock(start=30,end=31) -> {BB_b,BB_12}
	BB_23: BasicBlock(start=4,end=4) -> {BB_1}
	BB_24: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=10,end=10) -> {BB_24,BB_1d}
	BB_3: BasicBlock(start=1,end=1) -> {BB_7,BB_8}
	BB_4: BasicBlock(start=21,end=22) -> {BB_10,BB_20}
	BB_5: BasicBlock(start=9,end=9) -> {BB_6,BB_2}
	BB_6: BasicBlock(start=13,end=14) -> {BB_a,BB_4}
	BB_7: BasicBlock(start=2,end=2) -> {BB_24,BB_18}
	BB_8: BasicBlock(start=50,end=53) -> {BB_1c}
	BB_9: BasicBlock(start=8,end=8) -> {BB_24,BB_5}
	BB_a: BasicBlock(start=15,end=16) -> {BB_24,BB_13}
	BB_b: BasicBlock(start=42,end=42) -> {BB_24,BB_1e}
	BB_c: BasicBlock(start=24,end=24) -> {BB_24,BB_e}
	BB_d: BasicBlock(start=37,end=38) -> {BB_24,BB_17}
	BB_e: BasicBlock(start=25,end=26) -> {BB_24,BB_15}
	BB_f: BasicBlock(start=20,end=20) -> {BB_1c}
))

