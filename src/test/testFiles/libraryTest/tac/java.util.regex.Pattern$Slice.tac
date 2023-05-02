boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,19} (origin=-1),
	1: useSites={8,5,21} (origin=-2),
	2: useSites={4,20,12} (origin=-3),
	3: useSites={21,13} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1,11},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$Slice,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Slice[↦-1;refId=102]))),
	1: Assignment(pc=8,DVar(useSites={20,3},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=8,UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	2: Assignment(pc=11,DVar(useSites={4,12,17,3,11},value=int = 0,origin=2),IntConst(pc=11,0)),
	3: If(pc=18,UVar(defSites={2,17},value=int ∈ [0,2147483647]),>=,UVar(defSites={1},value=int ∈ [0,2147483647]),target=19),
	4: Assignment(pc=24,DVar(useSites={6},value=an int,origin=4),BinaryExpr(pc=24,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={2,17},value=int ∈ [0,2147483646]))),
	5: Assignment(pc=26,DVar(useSites={6},value=an int,origin=5),GetField(pc=26,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	6: If(pc=29,UVar(defSites={4},value=an int),<,UVar(defSites={5},value=an int),target=11),
	7: Assignment(pc=33,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=33,1)),
	8: PutField(pc=34,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={7},value=int = 1)),
	9: Assignment(pc=37,DVar(useSites={10},value=int = 0,origin=9),IntConst(pc=37,0)),
	10: ReturnValue(pc=38,UVar(defSites={9},value=int = 0)),
	11: Assignment(pc=43,DVar(useSites={14},value=an int,origin=11),ArrayLoad(pc=43,UVar(defSites={2,17},value=int ∈ [0,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	12: Assignment(pc=48,DVar(useSites={13},value=an int,origin=12),BinaryExpr(pc=48,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={2,17},value=int ∈ [0,2147483646]))),
	13: Assignment(pc=49,DVar(useSites={14},value=int ∈ [0,65535],origin=13),VirtualFunctionCall(pc=49,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={12},value=an int)))),
	14: If(pc=54,UVar(defSites={11},value=an int),==,UVar(defSites={13},value=int ∈ [0,65535]),target=17),
	15: Assignment(pc=57,DVar(useSites={16},value=int = 0,origin=15),IntConst(pc=57,0)),
	16: ReturnValue(pc=58,UVar(defSites={15},value=int = 0)),
	17: Assignment(pc=59,DVar(useSites={4,12,18,3,11},value=int ∈ [1,2147483647],origin=17),BinaryExpr(pc=59,ComputationalTypeInt,UVar(defSites={2,17},value=int ∈ [0,2147483646]),+,IntConst(pc=59,1))),
	18: Goto(pc=62,target=3),
	19: Assignment(pc=66,DVar(useSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦66;refId=247],origin=19),GetField(pc=66,java.util.regex.Pattern$Slice,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Slice[↦-1;refId=102]))),
	20: Assignment(pc=73,DVar(useSites={21},value=an int,origin=20),BinaryExpr(pc=73,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={1},value=int ∈ [0,2147483647]))),
	21: Assignment(pc=75,DVar(useSites={22},value=int ∈ [0,1],origin=21),VirtualFunctionCall(pc=75,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={19},value={_ <: java.util.regex.Pattern$Node, null}[↦66;refId=247]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={20},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	22: ReturnValue(pc=78,UVar(defSites={21},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_e,BB_3}
	BB_1: BasicBlock(start=14,end=14) -> {BB_c,BB_4}
	BB_2: BasicBlock(start=6,end=6) -> {BB_7,BB_a}
	BB_3: BasicBlock(start=2,end=2) -> {BB_8}
	BB_4: BasicBlock(start=17,end=18) -> {BB_8}
	BB_5: BasicBlock(start=22,end=22) -> {BB_9}
	BB_6: BasicBlock(start=12,end=13) -> {BB_e,BB_1}
	BB_7: BasicBlock(start=7,end=10) -> {BB_9}
	BB_8: BasicBlock(start=3,end=3) -> {BB_b,BB_d}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=11,end=11) -> {BB_e,BB_6}
	BB_b: BasicBlock(start=19,end=21) -> {BB_e,BB_5}
	BB_c: BasicBlock(start=15,end=16) -> {BB_9}
	BB_d: BasicBlock(start=4,end=5) -> {BB_e,BB_2}
	BB_e: ExitNode(normalReturn=false)
))

void <init>(int[])
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=2,java.util.regex.Pattern$SliceNode,isInterface=false,void <init>(int[]),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Slice[↦-1;refId=102]),(UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

