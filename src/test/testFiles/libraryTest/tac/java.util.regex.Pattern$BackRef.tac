void <init>(int)
AITACode(params=(Parameters(
	0: useSites={0,2} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BackRef[↦-1;refId=102]),()),
	1: Assignment(pc=7,DVar(useSites={2},value=an int,origin=1),BinaryExpr(pc=7,ComputationalTypeInt,UVar(defSites={-2},value=an int),+,UVar(defSites={-2},value=an int))),
	2: PutField(pc=8,java.util.regex.Pattern$BackRef,groupIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BackRef[↦-1;refId=102]),UVar(defSites={1},value=an int)),
	3: Return(pc=11)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={4,30,1} (origin=-1),
	1: useSites={0,32,16,13,3} (origin=-2),
	2: useSites={12,21,31} (origin=-3),
	3: useSites={32,24,22} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern$BackRef,groupIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BackRef[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={8,9,23},value=an int,origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: Assignment(pc=12,DVar(useSites={7},value={int[], null}[↦12;refId=109],origin=3),GetField(pc=12,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	4: Assignment(pc=16,DVar(useSites={6},value=an int,origin=4),GetField(pc=16,java.util.regex.Pattern$BackRef,groupIndex,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BackRef[↦-1;refId=102]))),
	5: Assignment(pc=19,DVar(useSites={6},value=int = 1,origin=5),IntConst(pc=19,1)),
	6: Assignment(pc=20,DVar(useSites={7},value=an int,origin=6),BinaryExpr(pc=20,ComputationalTypeInt,UVar(defSites={4},value=an int),+,UVar(defSites={5},value=int = 1))),
	7: Assignment(pc=21,DVar(useSites={8},value=an int,origin=7),ArrayLoad(pc=21,UVar(defSites={6},value=an int),UVar(defSites={3},value={int[], null}[↦12;refId=109]))),
	8: Assignment(pc=28,DVar(useSites={20,12,31},value=an int,origin=8),BinaryExpr(pc=28,ComputationalTypeInt,UVar(defSites={7},value=an int),-,UVar(defSites={2},value=an int))),
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
	19: Assignment(pc=56,DVar(useSites={20,28,21,23},value=int = 0,origin=19),IntConst(pc=56,0)),
	20: If(pc=63,UVar(defSites={28,19},value=int ∈ [0,2147483647]),>=,UVar(defSites={8},value=an int),target=30),
	21: Assignment(pc=70,DVar(useSites={22},value=an int,origin=21),BinaryExpr(pc=70,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={28,19},value=int ∈ [0,2147483646]))),
	22: Assignment(pc=71,DVar(useSites={25},value=int ∈ [0,65535],origin=22),VirtualFunctionCall(pc=71,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={21},value=an int)))),
	23: Assignment(pc=81,DVar(useSites={24},value=an int,origin=23),BinaryExpr(pc=81,ComputationalTypeInt,UVar(defSites={2},value=int ∈ [0,2147483647]),+,UVar(defSites={28,19},value=int ∈ [0,2147483646]))),
	24: Assignment(pc=82,DVar(useSites={25},value=int ∈ [0,65535],origin=24),VirtualFunctionCall(pc=82,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104]),(UVar(defSites={23},value=an int)))),
	25: If(pc=87,UVar(defSites={22},value=int ∈ [0,65535]),==,UVar(defSites={24},value=int ∈ [0,65535]),target=28),
	26: Assignment(pc=90,DVar(useSites={27},value=int = 0,origin=26),IntConst(pc=90,0)),
	27: ReturnValue(pc=91,UVar(defSites={26},value=int = 0)),
	28: Assignment(pc=92,DVar(useSites={20,21,29,23},value=int ∈ [1,2147483647],origin=28),BinaryExpr(pc=92,ComputationalTypeInt,UVar(defSites={28,19},value=int ∈ [0,2147483646]),+,IntConst(pc=92,1))),
	29: Goto(pc=95,target=20),
	30: Assignment(pc=99,DVar(useSites={32},value={_ <: java.util.regex.Pattern$Node, null}[↦99;refId=232],origin=30),GetField(pc=99,java.util.regex.Pattern$BackRef,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BackRef[↦-1;refId=102]))),
	31: Assignment(pc=106,DVar(useSites={32},value=an int,origin=31),BinaryExpr(pc=106,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={8},value=an int))),
	32: Assignment(pc=108,DVar(useSites={33},value=int ∈ [0,1],origin=32),VirtualFunctionCall(pc=108,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={30},value={_ <: java.util.regex.Pattern$Node, null}[↦99;refId=232]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={31},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	33: ReturnValue(pc=111,UVar(defSites={32},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_9,BB_4}
	BB_10: BasicBlock(start=30,end=32) -> {BB_9,BB_d}
	BB_11: BasicBlock(start=19,end=19) -> {BB_3}
	BB_1: BasicBlock(start=10,end=11) -> {BB_7}
	BB_2: BasicBlock(start=25,end=25) -> {BB_b,BB_e}
	BB_3: BasicBlock(start=20,end=20) -> {BB_c,BB_10}
	BB_4: BasicBlock(start=1,end=2) -> {BB_9,BB_6}
	BB_5: BasicBlock(start=12,end=14) -> {BB_11,BB_a}
	BB_6: BasicBlock(start=3,end=7) -> {BB_9,BB_8}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=8,end=9) -> {BB_1,BB_5}
	BB_9: ExitNode(normalReturn=false)
	BB_a: BasicBlock(start=15,end=18) -> {BB_7}
	BB_b: BasicBlock(start=28,end=29) -> {BB_3}
	BB_c: BasicBlock(start=21,end=22) -> {BB_9,BB_f}
	BB_d: BasicBlock(start=33,end=33) -> {BB_7}
	BB_e: BasicBlock(start=26,end=27) -> {BB_7}
	BB_f: BasicBlock(start=23,end=24) -> {BB_9,BB_2}
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={1,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=1,0)),
	1: PutField(pc=2,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]),UVar(defSites={0},value=int = 0)),
	2: Assignment(pc=6,DVar(useSites={3},value={_ <: java.util.regex.Pattern$Node, null}[↦6;refId=105],origin=2),GetField(pc=6,java.util.regex.Pattern$BackRef,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BackRef[↦-1;refId=102]))),
	3: Assignment(pc=10,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=10,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={2},value={_ <: java.util.regex.Pattern$Node, null}[↦6;refId=105]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	4: ReturnValue(pc=13,UVar(defSites={3},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=2,end=3) -> {BB_4,BB_3}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=4,end=4) -> {BB_2}
	BB_4: ExitNode(normalReturn=false)
))

