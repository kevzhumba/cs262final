void <init>(java.util.regex.Pattern$CharProperty,int)
AITACode(params=(Parameters(
	0: useSites={0,2,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={3} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]),()),
	1: Assignment(pc=6,DVar(useSites={2},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦6;refId=105],origin=1),GetField(pc=6,java.util.regex.Pattern$CharProperty,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-2},value={_ <: java.util.regex.Pattern$CharProperty, null}[↦-2;refId=103]))),
	2: PutField(pc=9,java.util.regex.Pattern$CharPropertyGreedy,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]),UVar(defSites={1},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦6;refId=105])),
	3: PutField(pc=14,java.util.regex.Pattern$CharPropertyGreedy,cmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]),UVar(defSites={-3},value=an int)),
	4: Return(pc=17)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=2,end=4) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={12,1} (origin=-1),
	1: useSites={0,4,6,9,13,3,11} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$CharPropertyGreedy,cmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=9,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={1},value=an int))),
	3: PutField(pc=10,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={2},value=an int)),
	4: Assignment(pc=14,DVar(useSites={5},value=int ∈ [0,1],origin=4),GetField(pc=14,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	5: If(pc=17,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=10),
	6: Assignment(pc=22,DVar(useSites={8},value=an int,origin=6),GetField(pc=22,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	7: Assignment(pc=25,DVar(useSites={8},value=int = 2147483647,origin=7),IntConst(pc=25,2147483647)),
	8: Assignment(pc=27,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=27,ComputationalTypeInt,UVar(defSites={6},value=an int),+,UVar(defSites={7},value=int = 2147483647))),
	9: PutField(pc=28,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={8},value=an int)),
	10: Assignment(pc=32,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=32,0)),
	11: PutField(pc=33,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={10},value=int = 0)),
	12: Assignment(pc=37,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦37;refId=105],origin=12),GetField(pc=37,java.util.regex.Pattern$CharPropertyGreedy,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]))),
	13: Assignment(pc=41,DVar(useSites={14},value=int ∈ [0,1],origin=13),VirtualFunctionCall(pc=41,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node, null}[↦37;refId=105]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	14: ReturnValue(pc=44,UVar(defSites={13},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_6,BB_3}
	BB_1: BasicBlock(start=10,end=13) -> {BB_6,BB_2}
	BB_2: BasicBlock(start=14,end=14) -> {BB_5}
	BB_3: BasicBlock(start=1,end=5) -> {BB_4,BB_1}
	BB_4: BasicBlock(start=6,end=9) -> {BB_1}
	BB_5: ExitNode(normalReturn=true)
	BB_6: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={22,17,5,15} (origin=-1),
	1: useSites={18,14,1} (origin=-2),
	2: useSites={4,12,28,18,26,9,3} (origin=-3),
	3: useSites={4,18,26} (origin=-4)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={16,10,29,23},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=4,DVar(useSites={12,3},value=an int,origin=1),GetField(pc=4,java.util.regex.Matcher,to,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	2: Nop(pc=7),
	3: If(pc=12,UVar(defSites={9,-3},value=an int),>=,UVar(defSites={1},value=an int),target=12),
	4: Assignment(pc=17,DVar(useSites={8,6},value=an int,origin=4),StaticFunctionCall(pc=17,java.lang.Character,isInterface=false,int codePointAt(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={9,-3},value=int ∈ [-2147483648,2147483646])))),
	5: Assignment(pc=23,DVar(useSites={6},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦23;refId=277],origin=5),GetField(pc=23,java.util.regex.Pattern$CharPropertyGreedy,predicate,java.util.regex.Pattern$CharPredicate,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]))),
	6: Assignment(pc=28,DVar(useSites={7},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=28,java.util.regex.Pattern$CharPredicate,isInterface=true,boolean is(int),UVar(defSites={5},value={_ <: java.util.regex.Pattern$CharPredicate, null}[↦23;refId=277]),(UVar(defSites={4},value=an int)))),
	7: If(pc=33,UVar(defSites={6},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	8: Assignment(pc=42,DVar(useSites={9},value=an int,origin=8),StaticFunctionCall(pc=42,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={4},value=an int)))),
	9: Assignment(pc=45,DVar(useSites={4,12,28,18,10,26,3},value=an int,origin=9),BinaryExpr(pc=45,ComputationalTypeInt,UVar(defSites={9,-3},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={8},value=an int))),
	10: Assignment(pc=47,DVar(useSites={16,29,11,23},value=an int,origin=10),BinaryExpr(pc=47,ComputationalTypeInt,UVar(defSites={0,10},value=an int),+,IntConst(pc=47,1))),
	11: Goto(pc=50,target=3),
	12: If(pc=56,UVar(defSites={9,-3},value=an int),<,UVar(defSites={1},value=an int),target=15),
	13: Assignment(pc=60,DVar(useSites={14},value=int = 1,origin=13),IntConst(pc=60,1)),
	14: PutField(pc=61,java.util.regex.Matcher,hitEnd,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={13},value=int = 1)),
	15: Assignment(pc=67,DVar(useSites={16},value=an int,origin=15),GetField(pc=67,java.util.regex.Pattern$CharPropertyGreedy,cmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]))),
	16: If(pc=70,UVar(defSites={0,10,29},value=an int),<,UVar(defSites={15},value=an int),target=31),
	17: Assignment(pc=74,DVar(useSites={18},value={_ <: java.util.regex.Pattern$Node, null}[↦74;refId=236],origin=17),GetField(pc=74,java.util.regex.Pattern$CharPropertyGreedy,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]))),
	18: Assignment(pc=80,DVar(useSites={19},value=int ∈ [0,1],origin=18),VirtualFunctionCall(pc=80,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={17},value={_ <: java.util.regex.Pattern$Node, null}[↦74;refId=236]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={28,9,-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	19: If(pc=83,UVar(defSites={18},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=22),
	20: Assignment(pc=86,DVar(useSites={21},value=int = 1,origin=20),IntConst(pc=86,1)),
	21: ReturnValue(pc=87,UVar(defSites={20},value=int = 1)),
	22: Assignment(pc=91,DVar(useSites={23},value=an int,origin=22),GetField(pc=91,java.util.regex.Pattern$CharPropertyGreedy,cmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$CharPropertyGreedy[↦-1;refId=102]))),
	23: If(pc=94,UVar(defSites={0,10,29},value=an int),!=,UVar(defSites={22},value=an int),target=26),
	24: Assignment(pc=97,DVar(useSites={25},value=int = 0,origin=24),IntConst(pc=97,0)),
	25: ReturnValue(pc=98,UVar(defSites={24},value=int = 0)),
	26: Assignment(pc=101,DVar(useSites={27},value=an int,origin=26),StaticFunctionCall(pc=101,java.lang.Character,isInterface=false,int codePointBefore(java.lang.CharSequence,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={28,9,-3},value=an int)))),
	27: Assignment(pc=109,DVar(useSites={28},value=an int,origin=27),StaticFunctionCall(pc=109,java.lang.Character,isInterface=false,int charCount(int),(UVar(defSites={26},value=an int)))),
	28: Assignment(pc=112,DVar(useSites={18,26,29},value=an int,origin=28),BinaryExpr(pc=112,ComputationalTypeInt,UVar(defSites={28,9,-3},value=an int),-,UVar(defSites={27},value=an int))),
	29: Assignment(pc=114,DVar(useSites={16,30,23},value=an int,origin=29),BinaryExpr(pc=114,ComputationalTypeInt,UVar(defSites={0,10,29},value=an int),+,IntConst(pc=114,-1))),
	30: Goto(pc=117,target=15),
	31: Assignment(pc=120,DVar(useSites={32},value=int = 0,origin=31),IntConst(pc=120,0)),
	32: ReturnValue(pc=121,UVar(defSites={31},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_15,BB_7}
	BB_10: BasicBlock(start=19,end=19) -> {BB_12,BB_3}
	BB_11: BasicBlock(start=15,end=16) -> {BB_d,BB_8}
	BB_12: BasicBlock(start=22,end=23) -> {BB_2,BB_e}
	BB_13: BasicBlock(start=27,end=27) -> {BB_15,BB_4}
	BB_14: BasicBlock(start=4,end=4) -> {BB_15,BB_1}
	BB_15: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=6) -> {BB_15,BB_a}
	BB_2: BasicBlock(start=24,end=25) -> {BB_c}
	BB_3: BasicBlock(start=20,end=21) -> {BB_c}
	BB_4: BasicBlock(start=28,end=30) -> {BB_11}
	BB_5: BasicBlock(start=9,end=11) -> {BB_b}
	BB_6: BasicBlock(start=13,end=14) -> {BB_11}
	BB_7: BasicBlock(start=2,end=2) -> {BB_b}
	BB_8: BasicBlock(start=17,end=18) -> {BB_15,BB_10}
	BB_9: BasicBlock(start=12,end=12) -> {BB_11,BB_6}
	BB_a: BasicBlock(start=7,end=7) -> {BB_f,BB_9}
	BB_b: BasicBlock(start=3,end=3) -> {BB_9,BB_14}
	BB_c: ExitNode(normalReturn=true)
	BB_d: BasicBlock(start=31,end=32) -> {BB_c}
	BB_e: BasicBlock(start=26,end=26) -> {BB_15,BB_13}
	BB_f: BasicBlock(start=8,end=8) -> {BB_15,BB_5}
))

