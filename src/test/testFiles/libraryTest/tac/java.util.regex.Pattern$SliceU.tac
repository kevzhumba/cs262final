boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,23} (origin=-1),
	1: useSites={8,25,5} (origin=-2),
	2: useSites={24,4,11} (origin=-3),
	3: useSites={12,25} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1,13,15},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$SliceU,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern$SliceU[↦-1;refId=102]))),
	1: Assignment(pc=8,DVar(useSites={24,3},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=8,UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	2: Assignment(pc=11,DVar(useSites={4,21,13,3,11,15},value=int = 0,origin=2),IntConst(pc=11,0)),
	3: If(pc=18,UVar(defSites={2,21},value=an int),>=,UVar(defSites={1},value=int ∈ [0,2147483647]),target=23),
	4: Assignment(pc=24,DVar(useSites={6},value=an int,origin=4),BinaryExpr(pc=24,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={2,21},value=int ∈ [-2147483648,2147483646]))),
	5: Assignment(pc=26,DVar(useSites={6},value=an int,origin=5),GetField(pc=26,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	6: If(pc=29,UVar(defSites={4},value=an int),<,UVar(defSites={5},value=an int),target=11),
	7: Assignment(pc=33,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=33,1)),
	8: PutField(pc=34,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={7},value=int = 1)),
	9: Assignment(pc=37,DVar(useSites={10},value=int = 0,origin=9),IntConst(pc=37,0)),
	10: ReturnValue(pc=38,UVar(defSites={9},value=int = 0)),
	11: Assignment(pc=43,DVar(useSites={12},value=an int,origin=11),BinaryExpr(pc=43,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={2,21},value=int ∈ [-2147483648,2147483646]))),
	12: Assignment(pc=44,DVar(useSites={16,14},value=int ∈ [0,65535],origin=12),VirtualFunctionCall(pc=44,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={11},value=an int)))),
	13: Assignment(pc=55,DVar(useSites={14},value=an int,origin=13),ArrayLoad(pc=55,UVar(defSites={2,21},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	14: If(pc=58,UVar(defSites={13},value=an int),==,UVar(defSites={12},value=int ∈ [0,65535]),target=21),
	15: Assignment(pc=65,DVar(useSites={18},value=an int,origin=15),ArrayLoad(pc=65,UVar(defSites={2,21},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	16: Assignment(pc=68,DVar(useSites={17},value=an int,origin=16),StaticFunctionCall(pc=68,java.lang.Character,isInterface=false,int toUpperCase(int),(UVar(defSites={12},value=int ∈ [0,65535])))),
	17: Assignment(pc=71,DVar(useSites={18},value=an int,origin=17),StaticFunctionCall(pc=71,java.lang.Character,isInterface=false,int toLowerCase(int),(UVar(defSites={16},value=an int)))),
	18: If(pc=74,UVar(defSites={15},value=an int),==,UVar(defSites={17},value=an int),target=21),
	19: Assignment(pc=77,DVar(useSites={20},value=int = 0,origin=19),IntConst(pc=77,0)),
	20: ReturnValue(pc=78,UVar(defSites={19},value=int = 0)),
	21: Assignment(pc=79,DVar(useSites={4,22,13,3,11,15},value=an int,origin=21),BinaryExpr(pc=79,ComputationalTypeInt,UVar(defSites={2,21},value=an int),+,IntConst(pc=79,1))),
	22: Goto(pc=82,target=3),
	23: Assignment(pc=86,DVar(useSites={25},value={_ <: java.util.regex.Pattern$Node, null}[↦86;refId=317],origin=23),GetField(pc=86,java.util.regex.Pattern$SliceU,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$SliceU[↦-1;refId=102]))),
	24: Assignment(pc=93,DVar(useSites={25},value=an int,origin=24),BinaryExpr(pc=93,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={1},value=int ∈ [0,2147483647]))),
	25: Assignment(pc=95,DVar(useSites={26},value=int ∈ [0,1],origin=25),VirtualFunctionCall(pc=95,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={23},value={_ <: java.util.regex.Pattern$Node, null}[↦86;refId=317]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={24},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	26: ReturnValue(pc=98,UVar(defSites={25},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_12,BB_5}
	BB_10: BasicBlock(start=23,end=25) -> {BB_12,BB_f}
	BB_11: BasicBlock(start=4,end=5) -> {BB_12,BB_2}
	BB_12: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=14,end=14) -> {BB_c,BB_3}
	BB_2: BasicBlock(start=6,end=6) -> {BB_7,BB_a}
	BB_3: BasicBlock(start=21,end=22) -> {BB_8}
	BB_4: BasicBlock(start=13,end=13) -> {BB_12,BB_1}
	BB_5: BasicBlock(start=2,end=2) -> {BB_8}
	BB_6: BasicBlock(start=17,end=17) -> {BB_12,BB_d}
	BB_7: BasicBlock(start=7,end=10) -> {BB_e}
	BB_8: BasicBlock(start=3,end=3) -> {BB_11,BB_10}
	BB_9: BasicBlock(start=16,end=16) -> {BB_12,BB_6}
	BB_a: BasicBlock(start=11,end=12) -> {BB_12,BB_4}
	BB_b: BasicBlock(start=19,end=20) -> {BB_e}
	BB_c: BasicBlock(start=15,end=15) -> {BB_12,BB_9}
	BB_d: BasicBlock(start=18,end=18) -> {BB_b,BB_3}
	BB_e: ExitNode(normalReturn=true)
	BB_f: BasicBlock(start=26,end=26) -> {BB_e}
))

void <init>(int[])
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=2,java.util.regex.Pattern$SliceNode,isInterface=false,void <init>(int[]),UVar(defSites={-1},value=java.util.regex.Pattern$SliceU[↦-1;refId=102]),(UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

