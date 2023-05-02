void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Begin[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={6} (origin=-1),
	1: useSites={0,2,10,9,13,7,15} (origin=-2),
	2: useSites={12,9,5,7} (origin=-3),
	3: useSites={7} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.regex.Matcher,anchoringBounds,boolean,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=8,DVar(useSites={5},value=an int,origin=2),GetField(pc=8,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: Goto(pc=11,target=5),
	4: Assignment(pc=14,DVar(useSites={5},value=an int,origin=4),IntConst(pc=14,0)),
	5: If(pc=20,UVar(defSites={-3},value=an int),!=,UVar(defSites={4,2},value=an int),target=19),
	6: Assignment(pc=24,DVar(useSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦24;refId=106],origin=6),GetField(pc=24,java.util.regex.Pattern$Begin,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Begin[↦-1;refId=102]))),
	7: Assignment(pc=30,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=30,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦24;refId=106]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	8: If(pc=33,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=19),
	9: PutField(pc=38,java.util.regex.Matcher,first,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int)),
	10: Assignment(pc=42,DVar(useSites={12},value={int[], null}[↦42;refId=109],origin=10),GetField(pc=42,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	11: Assignment(pc=45,DVar(useSites={12},value=int = 0,origin=11),IntConst(pc=45,0)),
	12: ArrayStore(pc=47,UVar(defSites={10},value={int[], null}[↦42;refId=109]),UVar(defSites={11},value=int = 0),UVar(defSites={-3},value=an int)),
	13: Assignment(pc=49,DVar(useSites={16},value={int[], null}[↦49;refId=112],origin=13),GetField(pc=49,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	14: Assignment(pc=52,DVar(useSites={16},value=int = 1,origin=14),IntConst(pc=52,1)),
	15: Assignment(pc=54,DVar(useSites={16},value=an int,origin=15),GetField(pc=54,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	16: ArrayStore(pc=57,UVar(defSites={13},value={int[], null}[↦49;refId=112]),UVar(defSites={14},value=int = 1),UVar(defSites={15},value=an int)),
	17: Assignment(pc=58,DVar(useSites={18},value=int = 1,origin=17),IntConst(pc=58,1)),
	18: ReturnValue(pc=59,UVar(defSites={17},value=int = 1)),
	19: Assignment(pc=60,DVar(useSites={20},value=int = 0,origin=19),IntConst(pc=60,0)),
	20: ReturnValue(pc=61,UVar(defSites={19},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_a,BB_3}
	BB_2: BasicBlock(start=1,end=1) -> {BB_b,BB_6}
	BB_3: BasicBlock(start=6,end=7) -> {BB_c,BB_9}
	BB_4: BasicBlock(start=9,end=12) -> {BB_c,BB_5}
	BB_5: BasicBlock(start=13,end=16) -> {BB_c,BB_7}
	BB_6: BasicBlock(start=2,end=3) -> {BB_1}
	BB_7: BasicBlock(start=17,end=18) -> {BB_8}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=8,end=8) -> {BB_4,BB_a}
	BB_a: BasicBlock(start=19,end=20) -> {BB_8}
	BB_b: BasicBlock(start=4,end=4) -> {BB_1}
	BB_c: ExitNode(normalReturn=false)
))

