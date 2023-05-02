void <init>(int,boolean)
AITACode(params=(Parameters(
	0: useSites={0,2,1} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Bound,type,int,UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]),UVar(defSites={-2},value=an int)),
	2: PutField(pc=11,java.util.regex.Pattern$Bound,useUWORD,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]),UVar(defSites={-3},value=int ∈ [0,1])),
	3: Return(pc=14)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean isWord(int)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={6,3,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Pattern$Bound,useUWORD,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=5),
	2: Assignment(pc=7,DVar(useSites={3},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦7;refId=104],origin=2),StaticFunctionCall(pc=7,java.util.regex.CharPredicates,isInterface=false,java.util.regex.Pattern$CharPredicate WORD(),())),
	3: Assignment(pc=11,DVar(useSites={12},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=11,java.util.regex.Pattern$CharPredicate,isInterface=true,boolean is(int),UVar(defSites={2},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦7;refId=104]),(UVar(defSites={-2},value=an int)))),
	4: Goto(pc=16,target=12),
	5: Assignment(pc=20,DVar(useSites={6},value=int = 95,origin=5),IntConst(pc=20,95)),
	6: If(pc=22,UVar(defSites={-2},value=an int),==,UVar(defSites={5},value=int = 95),target=9),
	7: Assignment(pc=26,DVar(useSites={8},value=int ∈ [0,1],origin=7),StaticFunctionCall(pc=26,java.lang.Character,isInterface=false,boolean isLetterOrDigit(int),(UVar(defSites={-2},value=an int)))),
	8: If(pc=29,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	9: Assignment(pc=32,DVar(useSites={12},value=int = 1,origin=9),IntConst(pc=32,1)),
	10: Goto(pc=33,target=12),
	11: Assignment(pc=36,DVar(useSites={12},value=int ∈ [0,1],origin=11),IntConst(pc=36,0)),
	12: ReturnValue(pc=37,UVar(defSites={9,3,11},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1,BB_3}
	BB_1: BasicBlock(start=5,end=6) -> {BB_2,BB_5}
	BB_2: BasicBlock(start=9,end=10) -> {BB_4}
	BB_3: BasicBlock(start=2,end=2) -> {BB_b,BB_6}
	BB_4: BasicBlock(start=12,end=12) -> {BB_7}
	BB_5: BasicBlock(start=7,end=7) -> {BB_b,BB_9}
	BB_6: BasicBlock(start=3,end=3) -> {BB_b,BB_a}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=11,end=11) -> {BB_4}
	BB_9: BasicBlock(start=8,end=8) -> {BB_2,BB_8}
	BB_a: BasicBlock(start=4,end=4) -> {BB_4}
	BB_b: ExitNode(normalReturn=false)
))

void <clinit>()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value=int = 1,origin=0),IntConst(pc=0,1)),
	1: PutStatic(pc=1,java.util.regex.Pattern$Bound,LEFT,int,UVar(defSites={0},value=int = 1)),
	2: Assignment(pc=4,DVar(useSites={3},value=int = 2,origin=2),IntConst(pc=4,2)),
	3: PutStatic(pc=5,java.util.regex.Pattern$Bound,RIGHT,int,UVar(defSites={2},value=int = 2)),
	4: Assignment(pc=8,DVar(useSites={5},value=int = 3,origin=4),IntConst(pc=8,3)),
	5: PutStatic(pc=9,java.util.regex.Pattern$Bound,BOTH,int,UVar(defSites={4},value=int = 3)),
	6: Assignment(pc=12,DVar(useSites={7},value=int = 4,origin=6),IntConst(pc=12,4)),
	7: PutStatic(pc=13,java.util.regex.Pattern$Bound,NONE,int,UVar(defSites={6},value=int = 4)),
	8: Return(pc=16)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=8) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,4,1} (origin=-1),
	1: useSites={0,5} (origin=-2),
	2: useSites={0,5} (origin=-3),
	3: useSites={0,5} (origin=-4)
)),stmts=(
	0: Assignment(pc=4,DVar(useSites={2},value=an int,origin=0),VirtualFunctionCall(pc=4,java.util.regex.Pattern$Bound,isInterface=false,int check(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	1: Assignment(pc=8,DVar(useSites={2},value=an int,origin=1),GetField(pc=8,java.util.regex.Pattern$Bound,type,int,UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]))),
	2: Assignment(pc=11,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=11,ComputationalTypeInt,UVar(defSites={0},value=an int),&,UVar(defSites={1},value=an int))),
	3: If(pc=12,UVar(defSites={2},value=an int),<=,IntConst(pc=-333,0),target=9),
	4: Assignment(pc=16,DVar(useSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=106],origin=4),GetField(pc=16,java.util.regex.Pattern$Bound,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]))),
	5: Assignment(pc=22,DVar(useSites={6},value=int ∈ [0,1],origin=5),VirtualFunctionCall(pc=22,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=106]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	6: If(pc=25,UVar(defSites={5},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=9),
	7: Assignment(pc=28,DVar(useSites={10},value=int = 1,origin=7),IntConst(pc=28,1)),
	8: Goto(pc=29,target=10),
	9: Assignment(pc=32,DVar(useSites={10},value=int ∈ [0,1],origin=9),IntConst(pc=32,0)),
	10: ReturnValue(pc=33,UVar(defSites={9,7},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_8,BB_2}
	BB_1: BasicBlock(start=10,end=10) -> {BB_6}
	BB_2: BasicBlock(start=1,end=3) -> {BB_4,BB_7}
	BB_3: BasicBlock(start=6,end=6) -> {BB_4,BB_5}
	BB_4: BasicBlock(start=9,end=9) -> {BB_1}
	BB_5: BasicBlock(start=7,end=8) -> {BB_1}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=4,end=5) -> {BB_8,BB_3}
	BB_8: ExitNode(normalReturn=false)
))

int check(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={10,26} (origin=-1),
	1: useSites={40,2,6,38,1,17,3,31} (origin=-2),
	2: useSites={16,8,24,9,25,31} (origin=-3),
	3: useSites={17,9,25,31} (origin=-4)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={41},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=4,DVar(useSites={8},value=an int,origin=1),GetField(pc=4,java.util.regex.Matcher,from,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	2: Assignment(pc=10,DVar(useSites={24},value=an int,origin=2),GetField(pc=10,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: Assignment(pc=16,DVar(useSites={4},value=int ∈ [0,1],origin=3),GetField(pc=16,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	4: If(pc=19,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=8),
	5: Assignment(pc=22,DVar(useSites={8},value=int = 0,origin=5),IntConst(pc=22,0)),
	6: Assignment(pc=26,DVar(useSites={24},value=an int,origin=6),VirtualFunctionCall(pc=26,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	7: Nop(pc=29),
	8: If(pc=34,UVar(defSites={-3},value=an int),<=,UVar(defSites={1,5},value=an int),target=23),
	9: Assignment(pc=39,DVar(useSites={12,10},value=an int,origin=9),StaticFunctionCall(pc=39,java.lang.Character,isInterface=false,int codePointBefore(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3},value=int ∈ [-2147483647,2147483647])))),
	10: Assignment(pc=47,DVar(useSites={11},value=int ∈ [0,1],origin=10),VirtualFunctionCall(pc=47,java.util.regex.Pattern$Bound,isInterface=false,boolean isWord(int),UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]),(UVar(defSites={9},value=an int)))),
	11: If(pc=50,UVar(defSites={10},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=19),
	12: Assignment(pc=55,DVar(useSites={14},value=an int,origin=12),StaticFunctionCall(pc=55,java.lang.Character,isInterface=false,int getType(int),(UVar(defSites={9},value=an int)))),
	13: Assignment(pc=58,DVar(useSites={14},value=int = 6,origin=13),IntConst(pc=58,6)),
	14: If(pc=60,UVar(defSites={12},value=an int),!=,UVar(defSites={13},value=int = 6),target=21),
	15: Assignment(pc=65,DVar(useSites={16},value=int = 1,origin=15),IntConst(pc=65,1)),
	16: Assignment(pc=66,DVar(useSites={17},value=int ∈ [-2147483648,2147483646],origin=16),BinaryExpr(pc=66,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),-,UVar(defSites={15},value=int = 1))),
	17: Assignment(pc=68,DVar(useSites={18},value=int ∈ [0,1],origin=17),StaticFunctionCall(pc=68,java.util.regex.Pattern,isInterface=false,boolean hasBaseCharacter(java.util.regex.Matcher,int,java.lang.CharSequence),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={16},value=int ∈ [-2147483648,2147483646]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	18: If(pc=71,UVar(defSites={17},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=21),
	19: Assignment(pc=74,DVar(useSites={41},value=int = 1,origin=19),IntConst(pc=74,1)),
	20: Goto(pc=75,target=22),
	21: Assignment(pc=78,DVar(useSites={41},value=int ∈ [0,1],origin=21),IntConst(pc=78,0)),
	22: Nop(pc=79),
	23: Assignment(pc=81,DVar(useSites={41,43},value=int = 0,origin=23),IntConst(pc=81,0)),
	24: If(pc=87,UVar(defSites={-3},value=an int),>=,UVar(defSites={2,6},value=an int),target=37),
	25: Assignment(pc=92,DVar(useSites={28,26},value=an int,origin=25),StaticFunctionCall(pc=92,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	26: Assignment(pc=100,DVar(useSites={27},value=int ∈ [0,1],origin=26),VirtualFunctionCall(pc=100,java.util.regex.Pattern$Bound,isInterface=false,boolean isWord(int),UVar(defSites={-1},value=java.util.regex.Pattern$Bound[↦-1;refId=102]),(UVar(defSites={25},value=an int)))),
	27: If(pc=103,UVar(defSites={26},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=33),
	28: Assignment(pc=108,DVar(useSites={30},value=an int,origin=28),StaticFunctionCall(pc=108,java.lang.Character,isInterface=false,int getType(int),(UVar(defSites={25},value=an int)))),
	29: Assignment(pc=111,DVar(useSites={30},value=int = 6,origin=29),IntConst(pc=111,6)),
	30: If(pc=113,UVar(defSites={28},value=an int),!=,UVar(defSites={29},value=int = 6),target=35),
	31: Assignment(pc=119,DVar(useSites={32},value=int ∈ [0,1],origin=31),StaticFunctionCall(pc=119,java.util.regex.Pattern,isInterface=false,boolean hasBaseCharacter(java.util.regex.Matcher,int,java.lang.CharSequence),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	32: If(pc=122,UVar(defSites={31},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=35),
	33: Assignment(pc=125,DVar(useSites={41,43},value=int = 1,origin=33),IntConst(pc=125,1)),
	34: Goto(pc=126,target=36),
	35: Assignment(pc=129,DVar(useSites={41,43},value=int ∈ [0,1],origin=35),IntConst(pc=129,0)),
	36: Goto(pc=132,target=41),
	37: Assignment(pc=136,DVar(useSites={38},value=int = 1,origin=37),IntConst(pc=136,1)),
	38: PutField(pc=137,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={37},value=int = 1)),
	39: Assignment(pc=141,DVar(useSites={40},value=int = 1,origin=39),IntConst(pc=141,1)),
	40: PutField(pc=142,java.util.regex.Matcher,requireEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={39},value=int = 1)),
	41: Assignment(pc=149,DVar(useSites={42},value=int ∈ [0,1],origin=41),BinaryExpr(pc=149,ComputationalTypeInt,UVar(defSites={0,21,19},value=int ∈ [0,1]),^,UVar(defSites={33,35,23},value=int ∈ [0,1]))),
	42: If(pc=150,UVar(defSites={41},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=48),
	43: If(pc=155,UVar(defSites={33,35,23},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=46),
	44: Assignment(pc=158,DVar(useSites={49},value=an int,origin=44),GetStatic(pc=158,java.util.regex.Pattern$Bound,LEFT,int)),
	45: Goto(pc=161,target=49),
	46: Assignment(pc=164,DVar(useSites={49},value=an int,origin=46),GetStatic(pc=164,java.util.regex.Pattern$Bound,RIGHT,int)),
	47: Goto(pc=167,target=49),
	48: Assignment(pc=170,DVar(useSites={49},value=an int,origin=48),GetStatic(pc=170,java.util.regex.Pattern$Bound,NONE,int)),
	49: ReturnValue(pc=173,UVar(defSites={48,44,46},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_a,BB_4}
	BB_10: BasicBlock(start=28,end=28) -> {BB_a,BB_f}
	BB_11: BasicBlock(start=21,end=21) -> {BB_15}
	BB_12: BasicBlock(start=33,end=34) -> {BB_21}
	BB_13: BasicBlock(start=13,end=14) -> {BB_11,BB_b}
	BB_14: BasicBlock(start=41,end=42) -> {BB_1a,BB_1e}
	BB_15: BasicBlock(start=22,end=22) -> {BB_20}
	BB_16: BasicBlock(start=44,end=45) -> {BB_19}
	BB_17: BasicBlock(start=27,end=27) -> {BB_10,BB_12}
	BB_18: BasicBlock(start=12,end=12) -> {BB_a,BB_13}
	BB_19: BasicBlock(start=49,end=49) -> {BB_1c}
	BB_1: BasicBlock(start=5,end=6) -> {BB_a,BB_6}
	BB_1a: BasicBlock(start=48,end=48) -> {BB_19}
	BB_1b: BasicBlock(start=18,end=18) -> {BB_22,BB_11}
	BB_1c: ExitNode(normalReturn=true)
	BB_1d: BasicBlock(start=11,end=11) -> {BB_22,BB_18}
	BB_1e: BasicBlock(start=43,end=43) -> {BB_e,BB_16}
	BB_1f: BasicBlock(start=26,end=26) -> {BB_a,BB_17}
	BB_20: BasicBlock(start=23,end=24) -> {BB_d,BB_c}
	BB_21: BasicBlock(start=36,end=36) -> {BB_14}
	BB_22: BasicBlock(start=19,end=20) -> {BB_15}
	BB_2: BasicBlock(start=10,end=10) -> {BB_a,BB_1d}
	BB_3: BasicBlock(start=9,end=9) -> {BB_a,BB_2}
	BB_4: BasicBlock(start=2,end=4) -> {BB_1,BB_9}
	BB_5: BasicBlock(start=32,end=32) -> {BB_7,BB_12}
	BB_6: BasicBlock(start=7,end=7) -> {BB_9}
	BB_7: BasicBlock(start=35,end=35) -> {BB_21}
	BB_8: BasicBlock(start=31,end=31) -> {BB_a,BB_5}
	BB_9: BasicBlock(start=8,end=8) -> {BB_20,BB_3}
	BB_a: ExitNode(normalReturn=false)
	BB_b: BasicBlock(start=15,end=17) -> {BB_a,BB_1b}
	BB_c: BasicBlock(start=37,end=40) -> {BB_14}
	BB_d: BasicBlock(start=25,end=25) -> {BB_a,BB_1f}
	BB_e: BasicBlock(start=46,end=47) -> {BB_19}
	BB_f: BasicBlock(start=29,end=30) -> {BB_8,BB_7}
))

