boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,25} (origin=-1),
	1: useSites={4,20,26,17,7} (origin=-2),
	2: useSites={16,10,26,5} (origin=-3),
	3: useSites={10,26} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,11},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$SliceS,buffer,int[],UVar(defSites={-1},value=java.util.regex.Pattern$SliceS[↦-1;refId=102]))),
	1: Assignment(pc=9,DVar(useSites={3,11,23},value=int = 0,origin=1),IntConst(pc=9,0)),
	2: Assignment(pc=16,DVar(useSites={3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=16,UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: If(pc=17,UVar(defSites={1,23},value=int ∈ [0,2147483647]),>=,UVar(defSites={2},value=int ∈ [0,2147483647]),target=25),
	4: Assignment(pc=23,DVar(useSites={5},value=an int,origin=4),GetField(pc=23,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	5: If(pc=26,UVar(defSites={16,-3},value=an int),<,UVar(defSites={4},value=an int),target=10),
	6: Assignment(pc=30,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=30,1)),
	7: PutField(pc=31,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={6},value=int = 1)),
	8: Assignment(pc=34,DVar(useSites={9},value=int = 0,origin=8),IntConst(pc=34,0)),
	9: ReturnValue(pc=35,UVar(defSites={8},value=int = 0)),
	10: Assignment(pc=39,DVar(useSites={12,15},value=an int,origin=10),StaticFunctionCall(pc=39,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={16,-3},value=int ∈ [-2147483648,2147483646])))),
	11: Assignment(pc=48,DVar(useSites={12},value=an int,origin=11),ArrayLoad(pc=48,UVar(defSites={1,23},value=int ∈ [0,2147483646]),UVar(defSites={0},value=int[][↦1;refId=105]))),
	12: If(pc=51,UVar(defSites={11},value=an int),==,UVar(defSites={10},value=an int),target=15),
	13: Assignment(pc=54,DVar(useSites={14},value=int = 0,origin=13),IntConst(pc=54,0)),
	14: ReturnValue(pc=55,UVar(defSites={13},value=int = 0)),
	15: Assignment(pc=60,DVar(useSites={16},value=an int,origin=15),StaticFunctionCall(pc=60,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={10},value=an int)))),
	16: Assignment(pc=63,DVar(useSites={18,10,26,17,5},value=an int,origin=16),BinaryExpr(pc=63,ComputationalTypeInt,UVar(defSites={16,-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={15},value=an int))),
	17: Assignment(pc=69,DVar(useSites={18},value=an int,origin=17),GetField(pc=69,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	18: If(pc=72,UVar(defSites={16},value=an int),<=,UVar(defSites={17},value=an int),target=23),
	19: Assignment(pc=76,DVar(useSites={20},value=int = 1,origin=19),IntConst(pc=76,1)),
	20: PutField(pc=77,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={19},value=int = 1)),
	21: Assignment(pc=80,DVar(useSites={22},value=int = 0,origin=21),IntConst(pc=80,0)),
	22: ReturnValue(pc=81,UVar(defSites={21},value=int = 0)),
	23: Assignment(pc=82,DVar(useSites={24,3,11},value=int ∈ [1,2147483647],origin=23),BinaryExpr(pc=82,ComputationalTypeInt,UVar(defSites={1,23},value=int ∈ [0,2147483646]),+,IntConst(pc=82,1))),
	24: Goto(pc=85,target=2),
	25: Assignment(pc=89,DVar(useSites={26},value={_ <: java.util.regex.Pattern$Node, null}[↦89;refId=267],origin=25),GetField(pc=89,java.util.regex.Pattern$SliceS,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$SliceS[↦-1;refId=102]))),
	26: Assignment(pc=96,DVar(useSites={27},value=int ∈ [0,1],origin=26),VirtualFunctionCall(pc=96,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={25},value={_ <: java.util.regex.Pattern$Node, null}[↦89;refId=267]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={16,-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	27: ReturnValue(pc=99,UVar(defSites={26},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_6}
	BB_10: BasicBlock(start=4,end=4) -> {BB_11,BB_1}
	BB_11: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_2,BB_4}
	BB_2: BasicBlock(start=10,end=10) -> {BB_11,BB_c}
	BB_3: BasicBlock(start=25,end=26) -> {BB_11,BB_7}
	BB_4: BasicBlock(start=6,end=9) -> {BB_a}
	BB_5: BasicBlock(start=13,end=14) -> {BB_a}
	BB_6: BasicBlock(start=2,end=2) -> {BB_11,BB_9}
	BB_7: BasicBlock(start=27,end=27) -> {BB_a}
	BB_8: BasicBlock(start=12,end=12) -> {BB_f,BB_5}
	BB_9: BasicBlock(start=3,end=3) -> {BB_3,BB_10}
	BB_a: ExitNode(normalReturn=true)
	BB_b: BasicBlock(start=16,end=18) -> {BB_d,BB_e}
	BB_c: BasicBlock(start=11,end=11) -> {BB_11,BB_8}
	BB_d: BasicBlock(start=23,end=24) -> {BB_6}
	BB_e: BasicBlock(start=19,end=22) -> {BB_a}
	BB_f: BasicBlock(start=15,end=15) -> {BB_11,BB_b}
))

void <init>(int[])
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=2,java.util.regex.Pattern$Slice,isInterface=false,void <init>(int[]),UVar(defSites={-1},value=java.util.regex.Pattern$SliceS[↦-1;refId=102]),(UVar(defSites={-2},value={int[], null}[↦-2;refId=103]))),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

