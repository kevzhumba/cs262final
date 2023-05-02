boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={16,4,14} (origin=-1),
	1: useSites={1,17,13} (origin=-2),
	2: useSites={8,17,5,21,3,11} (origin=-3),
	3: useSites={17,5} (origin=-4)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={22,9,15},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=4,DVar(useSites={3,11},value=an int,origin=1),GetField(pc=4,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	2: Nop(pc=7),
	3: If(pc=12,UVar(defSites={8,-3},value=an int),>=,UVar(defSites={1},value=an int),target=11),
	4: Assignment(pc=16,DVar(useSites={6},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦16;refId=250],origin=4),GetField(pc=16,java.util.regex.Pattern$BmpCharPropertyGreedy,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=java.util.regex.Pattern$BmpCharPropertyGreedy[↦-1;refId=102]))),
	5: Assignment(pc=21,DVar(useSites={6},value=int ∈ [0,65535],origin=5),VirtualFunctionCall(pc=21,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={8,-3},value=int ∈ [-2147483648,2147483646])))),
	6: Assignment(pc=26,DVar(useSites={7},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=26,java.util.regex.Pattern$CharPredicate,isInterface=true,boolean is(int),UVar(defSites={4},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦16;refId=250]),(UVar(defSites={5},value=int ∈ [0,65535])))),
	7: If(pc=31,UVar(defSites={6},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	8: Assignment(pc=34,DVar(useSites={17,9,5,21,3,11},value=int ∈ [-2147483647,2147483647],origin=8),BinaryExpr(pc=34,ComputationalTypeInt,UVar(defSites={8,-3},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=34,1))),
	9: Assignment(pc=37,DVar(useSites={10,22,15},value=an int,origin=9),BinaryExpr(pc=37,ComputationalTypeInt,UVar(defSites={0,9},value=an int),+,IntConst(pc=37,1))),
	10: Goto(pc=40,target=3),
	11: If(pc=46,UVar(defSites={8,-3},value=an int),<,UVar(defSites={1},value=an int),target=14),
	12: Assignment(pc=50,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=50,1)),
	13: PutField(pc=51,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={12},value=int = 1)),
	14: Assignment(pc=57,DVar(useSites={15},value=an int,origin=14),GetField(pc=57,java.util.regex.Pattern$BmpCharPropertyGreedy,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$BmpCharPropertyGreedy[↦-1;refId=102]))),
	15: If(pc=60,UVar(defSites={0,22,9},value=an int),<,UVar(defSites={14},value=an int),target=24),
	16: Assignment(pc=64,DVar(useSites={17},value={_ <: java.util.regex.Pattern$Node, null}[↦64;refId=212],origin=16),GetField(pc=64,java.util.regex.Pattern$BmpCharPropertyGreedy,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$BmpCharPropertyGreedy[↦-1;refId=102]))),
	17: Assignment(pc=70,DVar(useSites={18},value=int ∈ [0,1],origin=17),VirtualFunctionCall(pc=70,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={16},value={_ <: java.util.regex.Pattern$Node, null}[↦64;refId=212]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={8,21,-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	18: If(pc=73,UVar(defSites={17},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=21),
	19: Assignment(pc=76,DVar(useSites={20},value=int = 1,origin=19),IntConst(pc=76,1)),
	20: ReturnValue(pc=77,UVar(defSites={19},value=int = 1)),
	21: Assignment(pc=78,DVar(useSites={22,17},value=an int,origin=21),BinaryExpr(pc=78,ComputationalTypeInt,UVar(defSites={8,21,-3},value=an int),+,IntConst(pc=78,-1))),
	22: Assignment(pc=81,DVar(useSites={23,15},value=an int,origin=22),BinaryExpr(pc=81,ComputationalTypeInt,UVar(defSites={0,22,9},value=an int),+,IntConst(pc=81,-1))),
	23: Goto(pc=84,target=14),
	24: Assignment(pc=87,DVar(useSites={25},value=int = 0,origin=24),IntConst(pc=87,0)),
	25: ReturnValue(pc=88,UVar(defSites={24},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_10,BB_5}
	BB_10: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=24,end=25) -> {BB_e}
	BB_2: BasicBlock(start=14,end=15) -> {BB_1,BB_9}
	BB_3: BasicBlock(start=6,end=6) -> {BB_10,BB_7}
	BB_4: BasicBlock(start=21,end=23) -> {BB_2}
	BB_5: BasicBlock(start=2,end=2) -> {BB_8}
	BB_6: BasicBlock(start=12,end=13) -> {BB_2}
	BB_7: BasicBlock(start=7,end=7) -> {BB_b,BB_a}
	BB_8: BasicBlock(start=3,end=3) -> {BB_a,BB_f}
	BB_9: BasicBlock(start=16,end=17) -> {BB_10,BB_d}
	BB_a: BasicBlock(start=11,end=11) -> {BB_2,BB_6}
	BB_b: BasicBlock(start=8,end=10) -> {BB_8}
	BB_c: BasicBlock(start=19,end=20) -> {BB_e}
	BB_d: BasicBlock(start=18,end=18) -> {BB_c,BB_4}
	BB_e: ExitNode(normalReturn=true)
	BB_f: BasicBlock(start=4,end=5) -> {BB_10,BB_3}
))

void <init>(java.util.regex.Pattern$BmpCharProperty,int)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=3,java.util.regex.Pattern$CharPropertyGreedy,isInterface=false,void <init>(java.util.regex.Pattern$CharProperty,int),UVar(defSites={-1},value=java.util.regex.Pattern$BmpCharPropertyGreedy[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$BmpCharProperty, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int))),
	1: Return(pc=6)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

