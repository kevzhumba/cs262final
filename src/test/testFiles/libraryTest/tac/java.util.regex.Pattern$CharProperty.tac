void <init>(java.util.regex.Pattern$CharPredicate)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharProperty[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$CharProperty,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharProperty[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦-2;refId=103])),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={8} (origin=-1),
	1: useSites={0,4,9,3,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=5,1)),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=6,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={1},value=int = 1))),
	3: PutField(pc=7,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={2},value=an int)),
	4: Assignment(pc=12,DVar(useSites={6},value=an int,origin=4),GetField(pc=12,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	5: Assignment(pc=15,DVar(useSites={6},value=int = 1,origin=5),IntConst(pc=15,1)),
	6: Assignment(pc=16,DVar(useSites={7},value=an int,origin=6),BinaryExpr(pc=16,ComputationalTypeInt,UVar(defSites={4},value=an int),+,UVar(defSites={5},value=int = 1))),
	7: PutField(pc=17,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={6},value=an int)),
	8: Assignment(pc=21,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦21;refId=105],origin=8),GetField(pc=21,java.util.regex.Pattern$CharProperty,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharProperty[↦-1;refId=102]))),
	9: Assignment(pc=25,DVar(useSites={10},value=int ∈ [0,1],origin=9),VirtualFunctionCall(pc=25,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦21;refId=105]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	10: ReturnValue(pc=28,UVar(defSites={9},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=10,end=10) -> {BB_3}
	BB_2: BasicBlock(start=1,end=9) -> {BB_4,BB_1}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={6,3} (origin=-1),
	1: useSites={0,16,9} (origin=-2),
	2: useSites={8,2,1} (origin=-3),
	3: useSites={2,9} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=5,UVar(defSites={-3},value=an int),>=,UVar(defSites={0},value=an int),target=15),
	2: Assignment(pc=10,DVar(useSites={4,7},value=an int,origin=2),StaticFunctionCall(pc=10,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	3: Assignment(pc=16,DVar(useSites={4},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦16;refId=107],origin=3),GetField(pc=16,java.util.regex.Pattern$CharProperty,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharProperty[↦-1;refId=102]))),
	4: Assignment(pc=21,DVar(useSites={5},value=int ∈ [0,1],origin=4),VirtualFunctionCall(pc=21,java.util.regex.Pattern$CharPredicate,isInterface=true,boolean is(int),UVar(defSites={3},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦16;refId=107]),(UVar(defSites={2},value=an int)))),
	5: If(pc=26,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=13),
	6: Assignment(pc=30,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦30;refId=110],origin=6),GetField(pc=30,java.util.regex.Pattern$CharProperty,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharProperty[↦-1;refId=102]))),
	7: Assignment(pc=37,DVar(useSites={8},value=an int,origin=7),StaticFunctionCall(pc=37,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={2},value=an int)))),
	8: Assignment(pc=40,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=40,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={7},value=an int))),
	9: Assignment(pc=42,DVar(useSites={10},value=int ∈ [0,1],origin=9),VirtualFunctionCall(pc=42,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦30;refId=110]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={8},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	10: If(pc=45,UVar(defSites={9},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=13),
	11: Assignment(pc=48,DVar(useSites={14},value=int = 1,origin=11),IntConst(pc=48,1)),
	12: Goto(pc=49,target=14),
	13: Assignment(pc=52,DVar(useSites={14},value=int ∈ [0,1],origin=13),IntConst(pc=52,0)),
	14: ReturnValue(pc=53,UVar(defSites={13,11},value=int ∈ [0,1])),
	15: Assignment(pc=55,DVar(useSites={16},value=int = 1,origin=15),IntConst(pc=55,1)),
	16: PutField(pc=56,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={15},value=int = 1)),
	17: Assignment(pc=59,DVar(useSites={18},value=int = 0,origin=17),IntConst(pc=59,0)),
	18: ReturnValue(pc=60,UVar(defSites={17},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_4}
	BB_1: BasicBlock(start=5,end=5) -> {BB_6,BB_5}
	BB_2: BasicBlock(start=10,end=10) -> {BB_a,BB_6}
	BB_3: BasicBlock(start=14,end=14) -> {BB_9}
	BB_4: BasicBlock(start=1,end=1) -> {BB_7,BB_d}
	BB_5: BasicBlock(start=6,end=7) -> {BB_c,BB_b}
	BB_6: BasicBlock(start=13,end=13) -> {BB_3}
	BB_7: BasicBlock(start=2,end=2) -> {BB_c,BB_8}
	BB_8: BasicBlock(start=3,end=4) -> {BB_c,BB_1}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=11,end=12) -> {BB_3}
	BB_b: BasicBlock(start=8,end=9) -> {BB_c,BB_2}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=18) -> {BB_9}
))

