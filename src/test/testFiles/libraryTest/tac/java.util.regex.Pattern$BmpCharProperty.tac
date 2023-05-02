boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={2,6} (origin=-1),
	1: useSites={0,16,9} (origin=-2),
	2: useSites={8,1,3} (origin=-3),
	3: useSites={9,3} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=5,UVar(defSites={-3},value=an int),>=,UVar(defSites={0},value=an int),target=15),
	2: Assignment(pc=9,DVar(useSites={4},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦9;refId=106],origin=2),GetField(pc=9,java.util.regex.Pattern$BmpCharProperty,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BmpCharProperty[↦-1;refId=102]))),
	3: Assignment(pc=14,DVar(useSites={4},value=int ∈ [0,65535],origin=3),VirtualFunctionCall(pc=14,java.lang.CharSequence,isInterface=true,char charAt(int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),(UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	4: Assignment(pc=19,DVar(useSites={5},value=int ∈ [0,1],origin=4),VirtualFunctionCall(pc=19,java.util.regex.Pattern$CharPredicate,isInterface=true,boolean is(int),UVar(defSites={2},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦9;refId=106]),(UVar(defSites={3},value=int ∈ [0,65535])))),
	5: If(pc=24,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=13),
	6: Assignment(pc=28,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦28;refId=111],origin=6),GetField(pc=28,java.util.regex.Pattern$BmpCharProperty,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BmpCharProperty[↦-1;refId=102]))),
	7: Assignment(pc=33,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=33,1)),
	8: Assignment(pc=34,DVar(useSites={9},value=int ∈ [-2147483647,2147483647],origin=8),BinaryExpr(pc=34,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={7},value=int = 1))),
	9: Assignment(pc=36,DVar(useSites={10},value=int ∈ [0,1],origin=9),VirtualFunctionCall(pc=36,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦28;refId=111]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={8},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value=_ <: java.lang.CharSequence[↦-4;refId=104])))),
	10: If(pc=39,UVar(defSites={9},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=13),
	11: Assignment(pc=42,DVar(useSites={14},value=int = 1,origin=11),IntConst(pc=42,1)),
	12: Goto(pc=43,target=14),
	13: Assignment(pc=46,DVar(useSites={14},value=int ∈ [0,1],origin=13),IntConst(pc=46,0)),
	14: ReturnValue(pc=47,UVar(defSites={13,11},value=int ∈ [0,1])),
	15: Assignment(pc=49,DVar(useSites={16},value=int = 1,origin=15),IntConst(pc=49,1)),
	16: PutField(pc=50,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={15},value=int = 1)),
	17: Assignment(pc=53,DVar(useSites={18},value=int = 0,origin=17),IntConst(pc=53,0)),
	18: ReturnValue(pc=54,UVar(defSites={17},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_4}
	BB_1: BasicBlock(start=5,end=5) -> {BB_6,BB_5}
	BB_2: BasicBlock(start=10,end=10) -> {BB_9,BB_6}
	BB_3: BasicBlock(start=14,end=14) -> {BB_8}
	BB_4: BasicBlock(start=1,end=1) -> {BB_a,BB_7}
	BB_5: BasicBlock(start=6,end=9) -> {BB_c,BB_2}
	BB_6: BasicBlock(start=13,end=13) -> {BB_3}
	BB_7: BasicBlock(start=2,end=3) -> {BB_c,BB_b}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=11,end=12) -> {BB_3}
	BB_a: BasicBlock(start=15,end=18) -> {BB_8}
	BB_b: BasicBlock(start=4,end=4) -> {BB_c,BB_1}
	BB_c: ExitNode(normalReturn=false)
))

void <init>(java.util.regex.Pattern$BmpCharPredicate)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=2,java.util.regex.Pattern$CharProperty,isInterface=false,void <init>(java.util.regex.Pattern$CharPredicate),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$BmpCharProperty[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$BmpCharPredicate, null}[↦-2;refId=103]))),
	1: Return(pc=5)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

