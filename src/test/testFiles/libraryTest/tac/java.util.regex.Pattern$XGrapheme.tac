boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={6} (origin=-1),
	1: useSites={0,5,3,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=5,1)),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=6,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={1},value=int = 1))),
	3: PutField(pc=7,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={2},value=an int)),
	4: Assignment(pc=11,DVar(useSites={5},value=int = 0,origin=4),IntConst(pc=11,0)),
	5: PutField(pc=12,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={4},value=int = 0)),
	6: Assignment(pc=16,DVar(useSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=105],origin=6),GetField(pc=16,java.util.regex.Pattern$XGrapheme,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$XGrapheme[↦-1;refId=102]))),
	7: Assignment(pc=20,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=20,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=105]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	8: ReturnValue(pc=23,UVar(defSites={7},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=1,end=7) -> {BB_4,BB_3}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=8,end=8) -> {BB_2}
	BB_4: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={13} (origin=-1),
	1: useSites={0,14,17,5} (origin=-2),
	2: useSites={4,2,1} (origin=-3),
	3: useSites={2,14,7} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: If(pc=5,UVar(defSites={-3},value=an int),>=,UVar(defSites={0},value=an int),target=16),
	2: Assignment(pc=10,DVar(useSites={8,3},value=an int,origin=2),StaticFunctionCall(pc=10,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3},value=int ∈ [-2147483648,2147483646])))),
	3: Assignment(pc=18,DVar(useSites={4},value=an int,origin=3),StaticFunctionCall(pc=18,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={2},value=an int)))),
	4: Assignment(pc=21,DVar(useSites={6,14,11,7},value=an int,origin=4),BinaryExpr(pc=21,ComputationalTypeInt,UVar(defSites={-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={3},value=an int))),
	5: Assignment(pc=25,DVar(useSites={6},value=an int,origin=5),GetField(pc=25,java.util.regex.Matcher,to,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	6: If(pc=28,UVar(defSites={4,11},value=an int),>=,UVar(defSites={5},value=an int),target=13),
	7: Assignment(pc=33,DVar(useSites={8,10},value=an int,origin=7),StaticFunctionCall(pc=33,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={4,11},value=int ∈ [-2147483648,2147483646])))),
	8: Assignment(pc=42,DVar(useSites={9},value=int ∈ [0,1],origin=8),StaticFunctionCall(pc=42,java.util.regex.Grapheme,isInterface=false,boolean isBoundary(int,int),(UVar(defSites={2,7},value=an int),UVar(defSites={7},value=an int)))),
	9: If(pc=45,UVar(defSites={8},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=13),
	10: Assignment(pc=58,DVar(useSites={11},value=an int,origin=10),StaticFunctionCall(pc=58,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={7},value=an int)))),
	11: Assignment(pc=61,DVar(useSites={12,6,14,7},value=an int,origin=11),BinaryExpr(pc=61,ComputationalTypeInt,UVar(defSites={4,11},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={10},value=an int))),
	12: Goto(pc=63,target=5),
	13: Assignment(pc=67,DVar(useSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦67;refId=111],origin=13),GetField(pc=67,java.util.regex.Pattern$XGrapheme,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$XGrapheme[↦-1;refId=102]))),
	14: Assignment(pc=73,DVar(useSites={15},value=int ∈ [0,1],origin=14),VirtualFunctionCall(pc=73,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦67;refId=111]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={4,11},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	15: ReturnValue(pc=76,UVar(defSites={14},value=int ∈ [0,1])),
	16: Assignment(pc=78,DVar(useSites={17},value=int = 1,origin=16),IntConst(pc=78,1)),
	17: PutField(pc=79,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={16},value=int = 1)),
	18: Assignment(pc=82,DVar(useSites={19},value=int = 0,origin=18),IntConst(pc=82,0)),
	19: ReturnValue(pc=83,UVar(defSites={18},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_f,BB_3}
	BB_1: BasicBlock(start=5,end=6) -> {BB_5,BB_7}
	BB_2: BasicBlock(start=10,end=10) -> {BB_f,BB_b}
	BB_3: BasicBlock(start=1,end=1) -> {BB_6,BB_a}
	BB_4: BasicBlock(start=9,end=9) -> {BB_2,BB_5}
	BB_5: BasicBlock(start=13,end=14) -> {BB_f,BB_d}
	BB_6: BasicBlock(start=2,end=2) -> {BB_f,BB_8}
	BB_7: BasicBlock(start=7,end=7) -> {BB_f,BB_c}
	BB_8: BasicBlock(start=3,end=3) -> {BB_f,BB_e}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=16,end=19) -> {BB_9}
	BB_b: BasicBlock(start=11,end=12) -> {BB_1}
	BB_c: BasicBlock(start=8,end=8) -> {BB_f,BB_4}
	BB_d: BasicBlock(start=15,end=15) -> {BB_9}
	BB_e: BasicBlock(start=4,end=4) -> {BB_1}
	BB_f: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$XGrapheme[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

