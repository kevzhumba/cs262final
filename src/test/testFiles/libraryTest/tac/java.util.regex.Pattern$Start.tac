boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={1,5,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.regex.Pattern$Start,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]))),
	1: ExprStmt(pc=5,VirtualFunctionCall(pc=5,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={0},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=104]),(UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103])))),
	2: Assignment(pc=10,DVar(useSites={3},value=int = 0,origin=2),IntConst(pc=10,0)),
	3: PutField(pc=11,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]),UVar(defSites={2},value=int = 0)),
	4: Assignment(pc=15,DVar(useSites={5},value=int = 0,origin=4),IntConst(pc=15,0)),
	5: PutField(pc=16,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={4},value=int = 0)),
	6: Assignment(pc=19,DVar(useSites={7},value=int = 0,origin=6),IntConst(pc=19,0)),
	7: ReturnValue(pc=20,UVar(defSites={6},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=2,end=3) -> {BB_4,BB_3}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=4,end=7) -> {BB_2}
	BB_4: ExitNode(normalReturn=false)
))

void <init>(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,4,1,7} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Start,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: Assignment(pc=9,DVar(useSites={6,5,3},value=java.util.regex.Pattern$TreeInfo[↦9;refId=105],origin=2),New(pc=9,java.util.regex.Pattern$TreeInfo)),
	3: NonVirtualMethodCall(pc=13,java.util.regex.Pattern$TreeInfo,isInterface=false,void <init>(),UVar(defSites={2},value=java.util.regex.Pattern$TreeInfo[↦9;refId=105]),()),
	4: Assignment(pc=18,DVar(useSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦18;refId=107],origin=4),GetField(pc=18,java.util.regex.Pattern$Start,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]))),
	5: ExprStmt(pc=22,VirtualFunctionCall(pc=22,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦18;refId=107]),(UVar(defSites={2},value=java.util.regex.Pattern$TreeInfo[↦9;refId=105])))),
	6: Assignment(pc=28,DVar(useSites={7},value=an int,origin=6),GetField(pc=28,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={2},value=java.util.regex.Pattern$TreeInfo[↦9;refId=105]))),
	7: PutField(pc=31,java.util.regex.Pattern$Start,minLength,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]),UVar(defSites={6},value=an int)),
	8: Return(pc=34)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_5,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_5,BB_4}
	BB_2: BasicBlock(start=6,end=8) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=5) -> {BB_5,BB_2}
	BB_5: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={12,1,9} (origin=-1),
	1: useSites={0,16,8,20,18,22,5,13,29,15} (origin=-2),
	2: useSites={26,13,3,11,15} (origin=-3),
	3: useSites={13} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$Start,minLength,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=9,ComputationalTypeInt,UVar(defSites={0},value=an int),-,UVar(defSites={1},value=an int))),
	3: If(pc=10,UVar(defSites={-3},value=an int),<=,UVar(defSites={2},value=an int),target=8),
	4: Assignment(pc=14,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=14,1)),
	5: PutField(pc=15,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={4},value=int = 1)),
	6: Assignment(pc=18,DVar(useSites={7},value=int = 0,origin=6),IntConst(pc=18,0)),
	7: ReturnValue(pc=19,UVar(defSites={6},value=int = 0)),
	8: Assignment(pc=21,DVar(useSites={10},value=an int,origin=8),GetField(pc=21,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	9: Assignment(pc=25,DVar(useSites={10},value=an int,origin=9),GetField(pc=25,java.util.regex.Pattern$Start,minLength,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]))),
	10: Assignment(pc=28,DVar(useSites={11},value=an int,origin=10),BinaryExpr(pc=28,ComputationalTypeInt,UVar(defSites={8},value=an int),-,UVar(defSites={9},value=an int))),
	11: If(pc=34,UVar(defSites={26,-3},value=an int),>,UVar(defSites={10},value=an int),target=28),
	12: Assignment(pc=38,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦38;refId=106],origin=12),GetField(pc=38,java.util.regex.Pattern$Start,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Start[↦-1;refId=102]))),
	13: Assignment(pc=44,DVar(useSites={14},value=int ∈ [0,1],origin=13),VirtualFunctionCall(pc=44,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node, null}[↦38;refId=106]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={26,-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	14: If(pc=47,UVar(defSites={13},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=26),
	15: PutField(pc=52,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={26,-3},value=an int)),
	16: Assignment(pc=56,DVar(useSites={19},value={int[], null}[↦56;refId=109],origin=16),GetField(pc=56,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	17: Assignment(pc=59,DVar(useSites={19},value=int = 0,origin=17),IntConst(pc=59,0)),
	18: Assignment(pc=61,DVar(useSites={19},value=an int,origin=18),GetField(pc=61,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	19: ArrayStore(pc=64,UVar(defSites={16},value={int[], null}[↦56;refId=109]),UVar(defSites={17},value=int = 0),UVar(defSites={18},value=an int)),
	20: Assignment(pc=66,DVar(useSites={23},value={int[], null}[↦66;refId=112],origin=20),GetField(pc=66,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	21: Assignment(pc=69,DVar(useSites={23},value=int = 1,origin=21),IntConst(pc=69,1)),
	22: Assignment(pc=71,DVar(useSites={23},value=an int,origin=22),GetField(pc=71,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	23: ArrayStore(pc=74,UVar(defSites={20},value={int[], null}[↦66;refId=112]),UVar(defSites={21},value=int = 1),UVar(defSites={22},value=an int)),
	24: Assignment(pc=75,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=75,1)),
	25: ReturnValue(pc=76,UVar(defSites={24},value=int = 1)),
	26: Assignment(pc=77,DVar(useSites={13,11,27,15},value=an int,origin=26),BinaryExpr(pc=77,ComputationalTypeInt,UVar(defSites={26,-3},value=an int),+,IntConst(pc=77,1))),
	27: Goto(pc=80,target=11),
	28: Assignment(pc=84,DVar(useSites={29},value=int = 1,origin=28),IntConst(pc=84,1)),
	29: PutField(pc=85,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={28},value=int = 1)),
	30: Assignment(pc=88,DVar(useSites={31},value=int = 0,origin=30),IntConst(pc=88,0)),
	31: ReturnValue(pc=89,UVar(defSites={30},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_d,BB_4}
	BB_1: BasicBlock(start=24,end=25) -> {BB_7}
	BB_2: BasicBlock(start=14,end=14) -> {BB_b,BB_9}
	BB_3: BasicBlock(start=20,end=23) -> {BB_d,BB_1}
	BB_4: BasicBlock(start=1,end=3) -> {BB_a,BB_c}
	BB_5: BasicBlock(start=28,end=31) -> {BB_7}
	BB_6: BasicBlock(start=12,end=13) -> {BB_d,BB_2}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=11,end=11) -> {BB_6,BB_5}
	BB_9: BasicBlock(start=26,end=27) -> {BB_8}
	BB_a: BasicBlock(start=8,end=10) -> {BB_8}
	BB_b: BasicBlock(start=15,end=19) -> {BB_d,BB_3}
	BB_c: BasicBlock(start=4,end=7) -> {BB_7}
	BB_d: ExitNode(normalReturn=false)
))

