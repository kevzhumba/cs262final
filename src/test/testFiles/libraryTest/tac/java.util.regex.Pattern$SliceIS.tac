boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,28,14} (origin=-1),
	1: useSites={4,20,29,7,23} (origin=-2),
	2: useSites={10,5,29,19} (origin=-3),
	3: useSites={10,29} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,13,11},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$SliceIS,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceIS[↦-1;refId=102]))),
	1: Assignment(pc=9,DVar(useSites={26,13,3,11},value=int = 0,origin=1),IntConst(pc=9,0)),
	2: Assignment(pc=16,DVar(useSites={3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=16,UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: If(pc=17,UVar(defSites={26,1},value=an int),>=,UVar(defSites={2},value=int ∈ [0,2147483647]),target=28),
	4: Assignment(pc=23,DVar(useSites={5},value=an int,origin=4),GetField(pc=23,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	5: If(pc=26,UVar(defSites={-3,19},value=an int),<,UVar(defSites={4},value=an int),target=10),
	6: Assignment(pc=30,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=30,1)),
	7: PutField(pc=31,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={6},value=int = 1)),
	8: Assignment(pc=34,DVar(useSites={9},value=int = 0,origin=8),IntConst(pc=34,0)),
	9: ReturnValue(pc=35,UVar(defSites={8},value=int = 0)),
	10: Assignment(pc=39,DVar(useSites={12,18,14},value=an int,origin=10),StaticFunctionCall(pc=39,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3,19},value=int ∈ [-2147483648,2147483646])))),
	11: Assignment(pc=48,DVar(useSites={12},value=an int,origin=11),ArrayLoad(pc=48,UVar(defSites={26,1},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	12: If(pc=51,UVar(defSites={11},value=an int),==,UVar(defSites={10},value=an int),target=18),
	13: Assignment(pc=58,DVar(useSites={15},value=an int,origin=13),ArrayLoad(pc=58,UVar(defSites={26,1},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	14: Assignment(pc=62,DVar(useSites={15},value=an int,origin=14),VirtualFunctionCall(pc=62,java.util.regex.Pattern$SliceIS,isInterface=false,int toLower(int),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceIS[↦-1;refId=102]),(UVar(defSites={10},value=an int)))),
	15: If(pc=65,UVar(defSites={13},value=an int),==,UVar(defSites={14},value=an int),target=18),
	16: Assignment(pc=68,DVar(useSites={17},value=int = 0,origin=16),IntConst(pc=68,0)),
	17: ReturnValue(pc=69,UVar(defSites={16},value=int = 0)),
	18: Assignment(pc=74,DVar(useSites={19},value=an int,origin=18),StaticFunctionCall(pc=74,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={10},value=an int)))),
	19: Assignment(pc=77,DVar(useSites={20,10,5,21,29},value=an int,origin=19),BinaryExpr(pc=77,ComputationalTypeInt,UVar(defSites={-3,19},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={18},value=an int))),
	20: Assignment(pc=83,DVar(useSites={21},value=an int,origin=20),GetField(pc=83,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	21: If(pc=86,UVar(defSites={19},value=an int),<=,UVar(defSites={20},value=an int),target=26),
	22: Assignment(pc=90,DVar(useSites={23},value=int = 1,origin=22),IntConst(pc=90,1)),
	23: PutField(pc=91,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={22},value=int = 1)),
	24: Assignment(pc=94,DVar(useSites={25},value=int = 0,origin=24),IntConst(pc=94,0)),
	25: ReturnValue(pc=95,UVar(defSites={24},value=int = 0)),
	26: Assignment(pc=96,DVar(useSites={13,3,11,27},value=an int,origin=26),BinaryExpr(pc=96,ComputationalTypeInt,UVar(defSites={26,1},value=an int),+,IntConst(pc=96,1))),
	27: Goto(pc=99,target=2),
	28: Assignment(pc=103,DVar(useSites={29},value={_ <: java.util.regex.Pattern$Node, null}[↦103;refId=317],origin=28),GetField(pc=103,java.util.regex.Pattern$SliceIS,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceIS[↦-1;refId=102]))),
	29: Assignment(pc=110,DVar(useSites={30},value=int ∈ [0,1],origin=29),VirtualFunctionCall(pc=110,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦103;refId=317]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3,19},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	30: ReturnValue(pc=113,UVar(defSites={29},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_7}
	BB_10: ExitNode(normalReturn=true)
	BB_11: BasicBlock(start=30,end=30) -> {BB_10}
	BB_12: BasicBlock(start=19,end=21) -> {BB_d,BB_8}
	BB_13: BasicBlock(start=4,end=4) -> {BB_14,BB_1}
	BB_14: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_2,BB_4}
	BB_2: BasicBlock(start=10,end=10) -> {BB_14,BB_c}
	BB_3: BasicBlock(start=14,end=14) -> {BB_14,BB_e}
	BB_4: BasicBlock(start=6,end=9) -> {BB_10}
	BB_5: BasicBlock(start=28,end=29) -> {BB_14,BB_11}
	BB_6: BasicBlock(start=13,end=13) -> {BB_14,BB_3}
	BB_7: BasicBlock(start=2,end=2) -> {BB_14,BB_a}
	BB_8: BasicBlock(start=22,end=25) -> {BB_10}
	BB_9: BasicBlock(start=12,end=12) -> {BB_f,BB_6}
	BB_a: BasicBlock(start=3,end=3) -> {BB_13,BB_5}
	BB_b: BasicBlock(start=16,end=17) -> {BB_10}
	BB_c: BasicBlock(start=11,end=11) -> {BB_14,BB_9}
	BB_d: BasicBlock(start=26,end=27) -> {BB_7}
	BB_e: BasicBlock(start=15,end=15) -> {BB_b,BB_f}
	BB_f: BasicBlock(start=18,end=18) -> {BB_14,BB_12}
))

int toLower(int)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),StaticFunctionCall(pc=1,java.util.regex.ASCII,isInterface=false,int toLower(int),(UVar(defSites={-2},value=an int)))),
	1: ReturnValue(pc=4,UVar(defSites={0},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void <init>(int[])
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=2,java.util.regex.Pattern$SliceNode,isInterface=false,void <init>(int[]),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceIS[↦-1;refId=102]),(UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

