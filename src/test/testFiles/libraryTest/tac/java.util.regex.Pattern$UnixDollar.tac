void <init>(boolean)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$UnixDollar[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$UnixDollar,multiline,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$UnixDollar[↦-1;refId=102]),UVar(defSites={-2},value=int ∈ [0,1])),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={16,18,9,27} (origin=-1),
	1: useSites={0,24,4,28,2,26,19} (origin=-2),
	2: useSites={28,6,5,13,19} (origin=-3),
	3: useSites={28,6,19} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Matcher,anchoringBounds,boolean,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=8,DVar(useSites={12,5},value=an int,origin=2),GetField(pc=8,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: Goto(pc=11,target=5),
	4: Assignment(pc=15,DVar(useSites={12,5},value=an int,origin=4),VirtualFunctionCall(pc=15,java.util.regex.Matcher,isInterface=false,int getTextLength(),UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),())),
	5: If(pc=23,UVar(defSites={-3},value=an int),>=,UVar(defSites={4,2},value=an int),target=23),
	6: Assignment(pc=28,DVar(useSites={8},value=int ∈ [0,65535],origin=6),VirtualFunctionCall(pc=28,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	7: Assignment(pc=37,DVar(useSites={8},value=int = 10,origin=7),IntConst(pc=37,10)),
	8: If(pc=39,UVar(defSites={6},value=int ∈ [0,65535]),!=,UVar(defSites={7},value=int = 10),target=21),
	9: Assignment(pc=43,DVar(useSites={10},value=int ∈ [0,1],origin=9),GetField(pc=43,java.util.regex.Pattern$UnixDollar,multiline,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$UnixDollar[↦-1;refId=102]))),
	10: If(pc=46,UVar(defSites={9},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=16),
	11: Assignment(pc=52,DVar(useSites={12},value=int = 1,origin=11),IntConst(pc=52,1)),
	12: Assignment(pc=53,DVar(useSites={13},value=int ∈ [-2147483648,2147483646],origin=12),BinaryExpr(pc=53,ComputationalTypeInt,UVar(defSites={4,2},value=int ∈ [-2147483647,2147483647]),-,UVar(defSites={11},value=int = 1))),
	13: If(pc=54,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),==,UVar(defSites={12},value=int ∈ [-2147483648,2147483646]),target=16),
	14: Assignment(pc=57,DVar(useSites={15},value=int = 0,origin=14),IntConst(pc=57,0)),
	15: ReturnValue(pc=58,UVar(defSites={14},value=int = 0)),
	16: Assignment(pc=60,DVar(useSites={17},value=int ∈ [0,1],origin=16),GetField(pc=60,java.util.regex.Pattern$UnixDollar,multiline,boolean,UVar(defSites={-1},value=java.util.regex.Pattern$UnixDollar[↦-1;refId=102]))),
	17: If(pc=63,UVar(defSites={16},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=23),
	18: Assignment(pc=67,DVar(useSites={19},value={_ <: java.util.regex.Pattern$Node, null}[↦67;refId=112],origin=18),GetField(pc=67,java.util.regex.Pattern$UnixDollar,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$UnixDollar[↦-1;refId=102]))),
	19: Assignment(pc=73,DVar(useSites={20},value=int ∈ [0,1],origin=19),VirtualFunctionCall(pc=73,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={18},value={_ <: java.util.regex.Pattern$Node, null}[↦67;refId=112]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	20: ReturnValue(pc=76,UVar(defSites={19},value=int ∈ [0,1])),
	21: Assignment(pc=77,DVar(useSites={22},value=int = 0,origin=21),IntConst(pc=77,0)),
	22: ReturnValue(pc=78,UVar(defSites={21},value=int = 0)),
	23: Assignment(pc=80,DVar(useSites={24},value=int = 1,origin=23),IntConst(pc=80,1)),
	24: PutField(pc=81,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={23},value=int = 1)),
	25: Assignment(pc=85,DVar(useSites={26},value=int = 1,origin=25),IntConst(pc=85,1)),
	26: PutField(pc=86,java.util.regex.Matcher,requireEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={25},value=int = 1)),
	27: Assignment(pc=90,DVar(useSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦90;refId=109],origin=27),GetField(pc=90,java.util.regex.Pattern$UnixDollar,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$UnixDollar[↦-1;refId=102]))),
	28: Assignment(pc=96,DVar(useSites={29},value=int ∈ [0,1],origin=28),VirtualFunctionCall(pc=96,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦90;refId=109]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	29: ReturnValue(pc=99,UVar(defSites={28},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_11,BB_3}
	BB_10: BasicBlock(start=4,end=4) -> {BB_11,BB_1}
	BB_11: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_4,BB_b}
	BB_2: BasicBlock(start=14,end=15) -> {BB_f}
	BB_3: BasicBlock(start=1,end=1) -> {BB_10,BB_7}
	BB_4: BasicBlock(start=6,end=6) -> {BB_11,BB_8}
	BB_5: BasicBlock(start=21,end=22) -> {BB_f}
	BB_6: BasicBlock(start=9,end=10) -> {BB_a,BB_9}
	BB_7: BasicBlock(start=2,end=3) -> {BB_1}
	BB_8: BasicBlock(start=7,end=8) -> {BB_6,BB_5}
	BB_9: BasicBlock(start=16,end=17) -> {BB_e,BB_b}
	BB_a: BasicBlock(start=11,end=13) -> {BB_2,BB_9}
	BB_b: BasicBlock(start=23,end=28) -> {BB_11,BB_d}
	BB_c: BasicBlock(start=20,end=20) -> {BB_f}
	BB_d: BasicBlock(start=29,end=29) -> {BB_f}
	BB_e: BasicBlock(start=18,end=19) -> {BB_11,BB_c}
	BB_f: ExitNode(normalReturn=true)
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={2,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.regex.Pattern$UnixDollar,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$UnixDollar[↦-1;refId=102]))),
	1: ExprStmt(pc=5,VirtualFunctionCall(pc=5,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={0},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104]),(UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103])))),
	2: Assignment(pc=10,DVar(useSites={3},value=int ∈ [0,1],origin=2),GetField(pc=10,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	3: ReturnValue(pc=13,UVar(defSites={2},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

