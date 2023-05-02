boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={20} (origin=-1),
	1: useSites={0,2,1,9,5,21} (origin=-2),
	2: useSites={12,14,21,7} (origin=-3),
	3: useSites={21,15} (origin=-4)
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
	12: If(pc=44,UVar(defSites={-3},value=an int),<=,UVar(defSites={0,4},value=an int),target=20),
	13: Assignment(pc=49,DVar(useSites={14},value=int = 1,origin=13),IntConst(pc=49,1)),
	14: Assignment(pc=50,DVar(useSites={15},value=int ∈ [-2147483648,2147483646],origin=14),BinaryExpr(pc=50,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),-,UVar(defSites={13},value=int = 1))),
	15: Assignment(pc=51,DVar(useSites={17},value=int ∈ [0,65535],origin=15),VirtualFunctionCall(pc=51,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={14},value=int ∈ [-2147483648,2147483646])))),
	16: Assignment(pc=60,DVar(useSites={17},value=int = 10,origin=16),IntConst(pc=60,10)),
	17: If(pc=62,UVar(defSites={15},value=int ∈ [0,65535]),==,UVar(defSites={16},value=int = 10),target=20),
	18: Assignment(pc=65,DVar(useSites={19},value=int = 0,origin=18),IntConst(pc=65,0)),
	19: ReturnValue(pc=66,UVar(defSites={18},value=int = 0)),
	20: Assignment(pc=68,DVar(useSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦68;refId=109],origin=20),GetField(pc=68,java.util.regex.Pattern$UnixCaret,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$UnixCaret[↦-1;refId=102]))),
	21: Assignment(pc=74,DVar(useSites={22},value=int ∈ [0,1],origin=21),VirtualFunctionCall(pc=74,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={20},value={_ <: java.util.regex.Pattern$Node, null}[↦68;refId=109]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	22: ReturnValue(pc=77,UVar(defSites={21},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_d,BB_2}
	BB_1: BasicBlock(start=20,end=21) -> {BB_d,BB_5}
	BB_2: BasicBlock(start=1,end=3) -> {BB_7,BB_c}
	BB_3: BasicBlock(start=6,end=6) -> {BB_7}
	BB_4: BasicBlock(start=13,end=15) -> {BB_d,BB_8}
	BB_5: BasicBlock(start=22,end=22) -> {BB_b}
	BB_6: BasicBlock(start=12,end=12) -> {BB_1,BB_4}
	BB_7: BasicBlock(start=7,end=7) -> {BB_9,BB_6}
	BB_8: BasicBlock(start=16,end=17) -> {BB_a,BB_1}
	BB_9: BasicBlock(start=8,end=11) -> {BB_b}
	BB_a: BasicBlock(start=18,end=19) -> {BB_b}
	BB_b: ExitNode(normalReturn=true)
	BB_c: BasicBlock(start=4,end=5) -> {BB_d,BB_3}
	BB_d: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$UnixCaret[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

