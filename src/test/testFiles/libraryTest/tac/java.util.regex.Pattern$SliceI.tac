boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,22} (origin=-1),
	1: useSites={8,24,5} (origin=-2),
	2: useSites={4,11,23} (origin=-3),
	3: useSites={24,12} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1,13,15},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$SliceI,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceI[↦-1;refId=102]))),
	1: Assignment(pc=8,DVar(useSites={3,23},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=8,UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	2: Assignment(pc=11,DVar(useSites={4,20,13,3,11,15},value=int = 0,origin=2),IntConst(pc=11,0)),
	3: If(pc=18,UVar(defSites={20,2},value=an int),>=,UVar(defSites={1},value=int ∈ [0,2147483647]),target=22),
	4: Assignment(pc=24,DVar(useSites={6},value=an int,origin=4),BinaryExpr(pc=24,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={20,2},value=int ∈ [-2147483648,2147483646]))),
	5: Assignment(pc=26,DVar(useSites={6},value=an int,origin=5),GetField(pc=26,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	6: If(pc=29,UVar(defSites={4},value=an int),<,UVar(defSites={5},value=an int),target=11),
	7: Assignment(pc=33,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=33,1)),
	8: PutField(pc=34,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={7},value=int = 1)),
	9: Assignment(pc=37,DVar(useSites={10},value=int = 0,origin=9),IntConst(pc=37,0)),
	10: ReturnValue(pc=38,UVar(defSites={9},value=int = 0)),
	11: Assignment(pc=43,DVar(useSites={12},value=an int,origin=11),BinaryExpr(pc=43,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={20,2},value=int ∈ [-2147483648,2147483646]))),
	12: Assignment(pc=44,DVar(useSites={16,14},value=int ∈ [0,65535],origin=12),VirtualFunctionCall(pc=44,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={11},value=an int)))),
	13: Assignment(pc=55,DVar(useSites={14},value=an int,origin=13),ArrayLoad(pc=55,UVar(defSites={20,2},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	14: If(pc=58,UVar(defSites={13},value=an int),==,UVar(defSites={12},value=int ∈ [0,65535]),target=20),
	15: Assignment(pc=65,DVar(useSites={17},value=an int,origin=15),ArrayLoad(pc=65,UVar(defSites={20,2},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	16: Assignment(pc=68,DVar(useSites={17},value=an int,origin=16),StaticFunctionCall(pc=68,java.util.regex.ASCII,isInterface=false,int toLower(int),(UVar(defSites={12},value=int ∈ [0,65535])))),
	17: If(pc=71,UVar(defSites={15},value=an int),==,UVar(defSites={16},value=an int),target=20),
	18: Assignment(pc=74,DVar(useSites={19},value=int = 0,origin=18),IntConst(pc=74,0)),
	19: ReturnValue(pc=75,UVar(defSites={18},value=int = 0)),
	20: Assignment(pc=76,DVar(useSites={4,21,13,3,11,15},value=an int,origin=20),BinaryExpr(pc=76,ComputationalTypeInt,UVar(defSites={20,2},value=an int),+,IntConst(pc=76,1))),
	21: Goto(pc=79,target=3),
	22: Assignment(pc=83,DVar(useSites={24},value={_ <: java.util.regex.Pattern$Node, null}[↦83;refId=296],origin=22),GetField(pc=83,java.util.regex.Pattern$SliceI,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceI[↦-1;refId=102]))),
	23: Assignment(pc=90,DVar(useSites={24},value=an int,origin=23),BinaryExpr(pc=90,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={1},value=int ∈ [0,2147483647]))),
	24: Assignment(pc=92,DVar(useSites={25},value=int ∈ [0,1],origin=24),VirtualFunctionCall(pc=92,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={22},value={_ <: java.util.regex.Pattern$Node, null}[↦83;refId=296]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={23},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	25: ReturnValue(pc=95,UVar(defSites={24},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_11,BB_6}
	BB_10: BasicBlock(start=4,end=5) -> {BB_11,BB_4}
	BB_11: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=25,end=25) -> {BB_f}
	BB_2: BasicBlock(start=14,end=14) -> {BB_3,BB_d}
	BB_3: BasicBlock(start=20,end=21) -> {BB_a}
	BB_4: BasicBlock(start=6,end=6) -> {BB_9,BB_c}
	BB_5: BasicBlock(start=13,end=13) -> {BB_11,BB_2}
	BB_6: BasicBlock(start=2,end=2) -> {BB_a}
	BB_7: BasicBlock(start=17,end=17) -> {BB_3,BB_e}
	BB_8: BasicBlock(start=22,end=24) -> {BB_11,BB_1}
	BB_9: BasicBlock(start=7,end=10) -> {BB_f}
	BB_a: BasicBlock(start=3,end=3) -> {BB_8,BB_10}
	BB_b: BasicBlock(start=16,end=16) -> {BB_11,BB_7}
	BB_c: BasicBlock(start=11,end=12) -> {BB_11,BB_5}
	BB_d: BasicBlock(start=15,end=15) -> {BB_11,BB_b}
	BB_e: BasicBlock(start=18,end=19) -> {BB_f}
	BB_f: ExitNode(normalReturn=true)
))

void <init>(int[])
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=2,java.util.regex.Pattern$SliceNode,isInterface=false,void <init>(int[]),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceI[↦-1;refId=102]),(UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

