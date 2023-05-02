boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={35} (origin=-1),
	1: useSites={0,36,2,1,9,5} (origin=-2),
	2: useSites={36,12,14,30,7} (origin=-3),
	3: useSites={36,30,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={12},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,from,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=7,DVar(useSites={7},value=an int,origin=1),GetField(pc=7,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	2: Assignment(pc=13,DVar(useSites={3},value=int ∈ [0,1],origin=2),GetField(pc=13,java.util.regex.Matcher,anchoringBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: If(pc=16,UVar(defSites={2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=7),
	4: Assignment(pc=19,DVar(useSites={12},value=int = 0,origin=4),IntConst(pc=19,0)),
	5: Assignment(pc=23,DVar(useSites={7},value=an int,origin=5),VirtualFunctionCall(pc=23,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	6: Nop(pc=26),
	7: If(pc=31,UVar(defSites={-3},value=an int),!=,UVar(defSites={1,5},value=an int),target=12),
	8: Assignment(pc=35,DVar(useSites={9},value=int = 1,origin=8),IntConst(pc=35,1)),
	9: PutField(pc=36,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={8},value=int = 1)),
	10: Assignment(pc=39,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=39,0)),
	11: ReturnValue(pc=40,UVar(defSites={10},value=int = 0)),
	12: If(pc=44,UVar(defSites={-3},value=an int),<=,UVar(defSites={0,4},value=an int),target=35),
	13: Assignment(pc=49,DVar(useSites={14},value=int = 1,origin=13),IntConst(pc=49,1)),
	14: Assignment(pc=50,DVar(useSites={15},value=int ∈ [-2147483648,2147483646],origin=14),BinaryExpr(pc=50,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),-,UVar(defSites={13},value=int = 1))),
	15: Assignment(pc=51,DVar(useSites={17,25,21,29,19},value=int ∈ [0,65535],origin=15),VirtualFunctionCall(pc=51,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={14},value=int ∈ [-2147483648,2147483646])))),
	16: Assignment(pc=60,DVar(useSites={17},value=int = 10,origin=16),IntConst(pc=60,10)),
	17: If(pc=62,UVar(defSites={15},value=int ∈ [0,65535]),==,UVar(defSites={16},value=int = 10),target=28),
	18: Assignment(pc=67,DVar(useSites={19},value=int = 13,origin=18),IntConst(pc=67,13)),
	19: If(pc=69,UVar(defSites={15},value=int ∈ [0,65535]),==,UVar(defSites={18},value=int = 13),target=28),
	20: Assignment(pc=74,DVar(useSites={21},value=int = 1,origin=20),IntConst(pc=74,1)),
	21: Assignment(pc=75,DVar(useSites={23},value=int ∈ [0,131071],origin=21),BinaryExpr(pc=75,ComputationalTypeInt,UVar(defSites={15},value=int ∈ [0,65535]),|,UVar(defSites={20},value=int = 1))),
	22: Assignment(pc=76,DVar(useSites={23},value=int = 8233,origin=22),IntConst(pc=76,8233)),
	23: If(pc=79,UVar(defSites={21},value=int ∈ [0,131071]),==,UVar(defSites={22},value=int = 8233),target=28),
	24: Assignment(pc=84,DVar(useSites={25},value=int = 133,origin=24),IntConst(pc=84,133)),
	25: If(pc=87,UVar(defSites={15},value=int ∈ [0,65535]),==,UVar(defSites={24},value=int = 133),target=28),
	26: Assignment(pc=90,DVar(useSites={27},value=int = 0,origin=26),IntConst(pc=90,0)),
	27: ReturnValue(pc=91,UVar(defSites={26},value=int = 0)),
	28: Assignment(pc=94,DVar(useSites={29},value=int = 13,origin=28),IntConst(pc=94,13)),
	29: If(pc=96,UVar(defSites={15},value=int ∈ [0,65535]),!=,UVar(defSites={28},value=int = 13),target=35),
	30: Assignment(pc=101,DVar(useSites={32},value=int ∈ [0,65535],origin=30),VirtualFunctionCall(pc=101,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),(UVar(defSites={-3},value=int ∈ [-2147483647,2147483647])))),
	31: Assignment(pc=106,DVar(useSites={32},value=int = 10,origin=31),IntConst(pc=106,10)),
	32: If(pc=108,UVar(defSites={30},value=int ∈ [0,65535]),!=,UVar(defSites={31},value=int = 10),target=35),
	33: Assignment(pc=111,DVar(useSites={34},value=int = 0,origin=33),IntConst(pc=111,0)),
	34: ReturnValue(pc=112,UVar(defSites={33},value=int = 0)),
	35: Assignment(pc=114,DVar(useSites={36},value={_ <: java.util.regex.Pattern$Node, null}[↦114;refId=109],origin=35),GetField(pc=114,java.util.regex.Pattern$Caret,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Caret[↦-1;refId=102]))),
	36: Assignment(pc=120,DVar(useSites={37},value=int ∈ [0,1],origin=36),VirtualFunctionCall(pc=120,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={35},value={_ <: java.util.regex.Pattern$Node, null}[↦114;refId=109]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	37: ReturnValue(pc=123,UVar(defSites={36},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_14,BB_2}
	BB_10: ExitNode(normalReturn=true)
	BB_11: BasicBlock(start=16,end=17) -> {BB_d,BB_f}
	BB_12: BasicBlock(start=31,end=32) -> {BB_7,BB_e}
	BB_13: BasicBlock(start=4,end=5) -> {BB_14,BB_3}
	BB_14: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=20,end=23) -> {BB_d,BB_b}
	BB_2: BasicBlock(start=1,end=3) -> {BB_6,BB_13}
	BB_3: BasicBlock(start=6,end=6) -> {BB_6}
	BB_4: BasicBlock(start=13,end=15) -> {BB_14,BB_11}
	BB_5: BasicBlock(start=12,end=12) -> {BB_7,BB_4}
	BB_6: BasicBlock(start=7,end=7) -> {BB_9,BB_5}
	BB_7: BasicBlock(start=35,end=36) -> {BB_14,BB_c}
	BB_8: BasicBlock(start=26,end=27) -> {BB_10}
	BB_9: BasicBlock(start=8,end=11) -> {BB_10}
	BB_a: BasicBlock(start=30,end=30) -> {BB_14,BB_12}
	BB_b: BasicBlock(start=24,end=25) -> {BB_d,BB_8}
	BB_c: BasicBlock(start=37,end=37) -> {BB_10}
	BB_d: BasicBlock(start=28,end=29) -> {BB_7,BB_a}
	BB_e: BasicBlock(start=33,end=34) -> {BB_10}
	BB_f: BasicBlock(start=18,end=19) -> {BB_1,BB_d}
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Caret[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

