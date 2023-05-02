boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={1,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=1,0)),
	1: PutField(pc=2,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]),UVar(defSites={0},value=int = 0)),
	2: Assignment(pc=6,DVar(useSites={3},value={_ <: java.util.regex.Pattern$Node, null}[↦6;refId=105],origin=2),GetField(pc=6,java.util.regex.Pattern$CIBackRef,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]))),
	3: Assignment(pc=10,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=10,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={2},value={_ <: java.util.regex.Pattern$Node, null}[↦6;refId=105]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	4: ReturnValue(pc=13,UVar(defSites={3},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=2,end=3) -> {BB_4,BB_3}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=4,end=4) -> {BB_2}
	BB_4: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={24,4,1,45} (origin=-1),
	1: useSites={0,16,13,3,47} (origin=-2),
	2: useSites={40,12,46,21} (origin=-3),
	3: useSites={22,21,47} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern$CIBackRef,groupIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={8,42,22,9},value=an int,origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: Assignment(pc=12,DVar(useSites={7},value={int[], null}[↦12;refId=109],origin=3),GetField(pc=12,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	4: Assignment(pc=16,DVar(useSites={6},value=an int,origin=4),GetField(pc=16,java.util.regex.Pattern$CIBackRef,groupIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]))),
	5: Assignment(pc=19,DVar(useSites={6},value=int = 1,origin=5),IntConst(pc=19,1)),
	6: Assignment(pc=20,DVar(useSites={7},value=an int,origin=6),BinaryExpr(pc=20,ComputationalTypeInt,UVar(defSites={4},value=an int),+,UVar(defSites={5},value=int = 1))),
	7: Assignment(pc=21,DVar(useSites={8},value=an int,origin=7),ArrayLoad(pc=21,UVar(defSites={6},value=an int),UVar(defSites={3},value={int[], null}[↦12;refId=109]))),
	8: Assignment(pc=28,DVar(useSites={20,12,46},value=an int,origin=8),BinaryExpr(pc=28,ComputationalTypeInt,UVar(defSites={7},value=an int),-,UVar(defSites={2},value=an int))),
	9: If(pc=33,UVar(defSites={2},value=an int),>=,IntConst(pc=-333,0),target=12),
	10: Assignment(pc=36,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=36,0)),
	11: ReturnValue(pc=37,UVar(defSites={10},value=int = 0)),
	12: Assignment(pc=41,DVar(useSites={14},value=an int,origin=12),BinaryExpr(pc=41,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={8},value=an int))),
	13: Assignment(pc=43,DVar(useSites={14},value=an int,origin=13),GetField(pc=43,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	14: If(pc=46,UVar(defSites={12},value=an int),<=,UVar(defSites={13},value=an int),target=19),
	15: Assignment(pc=50,DVar(useSites={16},value=int = 1,origin=15),IntConst(pc=50,1)),
	16: PutField(pc=51,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={15},value=int = 1)),
	17: Assignment(pc=54,DVar(useSites={18},value=int = 0,origin=17),IntConst(pc=54,0)),
	18: ReturnValue(pc=55,UVar(defSites={17},value=int = 0)),
	19: Assignment(pc=59,DVar(useSites={20,43},value=int = 0,origin=19),IntConst(pc=59,0)),
	20: If(pc=66,UVar(defSites={19,43},value=an int),>=,UVar(defSites={8},value=an int),target=45),
	21: Assignment(pc=72,DVar(useSites={34,26,39,23},value=an int,origin=21),StaticFunctionCall(pc=72,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={40,-3},value=an int)))),
	22: Assignment(pc=80,DVar(useSites={41,35,27,23},value=an int,origin=22),StaticFunctionCall(pc=80,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={2,42},value=an int)))),
	23: If(pc=89,UVar(defSites={21},value=an int),==,UVar(defSites={22},value=an int),target=39),
	24: Assignment(pc=93,DVar(useSites={25},value=int ∈ [0,1],origin=24),GetField(pc=93,java.util.regex.Pattern$CIBackRef,doUnicodeCase,boolean,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]))),
	25: If(pc=96,UVar(defSites={24},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=34),
	26: Assignment(pc=101,DVar(useSites={28,29},value=an int,origin=26),StaticFunctionCall(pc=101,java.lang.Character,isInterface=false,int toUpperCase(int),(UVar(defSites={21},value=an int)))),
	27: Assignment(pc=108,DVar(useSites={28,30},value=an int,origin=27),StaticFunctionCall(pc=108,java.lang.Character,isInterface=false,int toUpperCase(int),(UVar(defSites={22},value=an int)))),
	28: If(pc=117,UVar(defSites={26},value=an int),==,UVar(defSites={27},value=an int),target=39),
	29: Assignment(pc=122,DVar(useSites={31},value=an int,origin=29),StaticFunctionCall(pc=122,java.lang.Character,isInterface=false,int toLowerCase(int),(UVar(defSites={26},value=an int)))),
	30: Assignment(pc=127,DVar(useSites={31},value=an int,origin=30),StaticFunctionCall(pc=127,java.lang.Character,isInterface=false,int toLowerCase(int),(UVar(defSites={27},value=an int)))),
	31: If(pc=130,UVar(defSites={29},value=an int),==,UVar(defSites={30},value=an int),target=39),
	32: Assignment(pc=133,DVar(useSites={33},value=int = 0,origin=32),IntConst(pc=133,0)),
	33: ReturnValue(pc=134,UVar(defSites={32},value=int = 0)),
	34: Assignment(pc=140,DVar(useSites={36},value=an int,origin=34),StaticFunctionCall(pc=140,java.util.regex.ASCII,isInterface=false,int toLower(int),(UVar(defSites={21},value=an int)))),
	35: Assignment(pc=145,DVar(useSites={36},value=an int,origin=35),StaticFunctionCall(pc=145,java.util.regex.ASCII,isInterface=false,int toLower(int),(UVar(defSites={22},value=an int)))),
	36: If(pc=148,UVar(defSites={34},value=an int),==,UVar(defSites={35},value=an int),target=39),
	37: Assignment(pc=151,DVar(useSites={38},value=int = 0,origin=37),IntConst(pc=151,0)),
	38: ReturnValue(pc=152,UVar(defSites={37},value=int = 0)),
	39: Assignment(pc=157,DVar(useSites={40},value=an int,origin=39),StaticFunctionCall(pc=157,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={21},value=an int)))),
	40: Assignment(pc=160,DVar(useSites={41,21},value=an int,origin=40),BinaryExpr(pc=160,ComputationalTypeInt,UVar(defSites={40,-3},value=an int),+,UVar(defSites={39},value=an int))),
	41: Assignment(pc=167,DVar(useSites={42},value=an int,origin=41),StaticFunctionCall(pc=167,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={22},value=an int)))),
	42: Assignment(pc=170,DVar(useSites={22,43},value=an int,origin=42),BinaryExpr(pc=170,ComputationalTypeInt,UVar(defSites={2,42},value=an int),+,UVar(defSites={41},value=an int))),
	43: Assignment(pc=173,DVar(useSites={20,44},value=an int,origin=43),BinaryExpr(pc=173,ComputationalTypeInt,UVar(defSites={19,43},value=an int),+,IntConst(pc=173,1))),
	44: Goto(pc=176,target=20),
	45: Assignment(pc=180,DVar(useSites={47},value={_ <: java.util.regex.Pattern$Node, null}[↦180;refId=385],origin=45),GetField(pc=180,java.util.regex.Pattern$CIBackRef,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]))),
	46: Assignment(pc=187,DVar(useSites={47},value=an int,origin=46),BinaryExpr(pc=187,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={8},value=an int))),
	47: Assignment(pc=189,DVar(useSites={48},value=int ∈ [0,1],origin=47),VirtualFunctionCall(pc=189,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={45},value={_ <: java.util.regex.Pattern$Node, null}[↦180;refId=385]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={46},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	48: ReturnValue(pc=192,UVar(defSites={47},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_7,BB_2}
	BB_10: BasicBlock(start=45,end=47) -> {BB_7,BB_17}
	BB_11: BasicBlock(start=32,end=33) -> {BB_18}
	BB_12: BasicBlock(start=34,end=34) -> {BB_7,BB_16}
	BB_13: BasicBlock(start=22,end=22) -> {BB_7,BB_1b}
	BB_14: BasicBlock(start=27,end=27) -> {BB_7,BB_e}
	BB_15: BasicBlock(start=3,end=7) -> {BB_7,BB_6}
	BB_16: BasicBlock(start=35,end=35) -> {BB_7,BB_1c}
	BB_17: BasicBlock(start=48,end=48) -> {BB_18}
	BB_18: ExitNode(normalReturn=true)
	BB_19: BasicBlock(start=40,end=41) -> {BB_7,BB_9}
	BB_1: BasicBlock(start=10,end=11) -> {BB_18}
	BB_1a: BasicBlock(start=26,end=26) -> {BB_7,BB_14}
	BB_1b: BasicBlock(start=23,end=23) -> {BB_a,BB_4}
	BB_1c: BasicBlock(start=36,end=36) -> {BB_4,BB_b}
	BB_1d: BasicBlock(start=30,end=30) -> {BB_7,BB_5}
	BB_1e: BasicBlock(start=19,end=19) -> {BB_c}
	BB_2: BasicBlock(start=1,end=2) -> {BB_7,BB_15}
	BB_3: BasicBlock(start=12,end=14) -> {BB_1e,BB_8}
	BB_4: BasicBlock(start=39,end=39) -> {BB_7,BB_19}
	BB_5: BasicBlock(start=31,end=31) -> {BB_4,BB_11}
	BB_6: BasicBlock(start=8,end=9) -> {BB_1,BB_3}
	BB_7: ExitNode(normalReturn=false)
	BB_8: BasicBlock(start=15,end=18) -> {BB_18}
	BB_9: BasicBlock(start=42,end=44) -> {BB_c}
	BB_a: BasicBlock(start=24,end=25) -> {BB_12,BB_1a}
	BB_b: BasicBlock(start=37,end=38) -> {BB_18}
	BB_c: BasicBlock(start=20,end=20) -> {BB_f,BB_10}
	BB_d: BasicBlock(start=29,end=29) -> {BB_7,BB_1d}
	BB_e: BasicBlock(start=28,end=28) -> {BB_d,BB_4}
	BB_f: BasicBlock(start=21,end=21) -> {BB_7,BB_13}
))

void <init>(int,boolean)
AITACode(params=(Parameters(
	0: useSites={0,2,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={3} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]),()),
	1: Assignment(pc=7,DVar(useSites={2},value=an int,origin=1),BinaryExpr(pc=7,ComputationalTypeInt,UVar(defSites={-2},value=an int),+,UVar(defSites={-2},value=an int))),
	2: PutField(pc=8,java.util.regex.Pattern$CIBackRef,groupIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]),UVar(defSites={1},value=an int)),
	3: PutField(pc=13,java.util.regex.Pattern$CIBackRef,doUnicodeCase,boolean,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CIBackRef[↦-1;refId=102]),UVar(defSites={-3},value=int ∈ [0,1])),
	4: Return(pc=16)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=4) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

