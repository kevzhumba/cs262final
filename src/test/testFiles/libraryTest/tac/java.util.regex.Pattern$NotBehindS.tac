void <init>(java.util.regex.Pattern$Node,int,int)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4)
)),stmts=(
	0: NonVirtualMethodCall(pc=4,java.util.regex.Pattern$NotBehind,isInterface=false,void <init>(java.util.regex.Pattern$Node,int,int),UVar(defSites={-1},value=java.util.regex.Pattern$NotBehindS[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value=an int))),
	1: Return(pc=7)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,24,36,3} (origin=-1),
	1: useSites={16,20,34,6,33,17,9,25,37,11,7} (origin=-2),
	2: useSites={16,2,14,5,37,21} (origin=-3),
	3: useSites={28,2,25,5,37} (origin=-4)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={1},value=an int,origin=0),GetField(pc=3,java.util.regex.Pattern$NotBehindS,rmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$NotBehindS[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),PrefixExpr(pc=6,ComputationalTypeInt,-,UVar(defSites={0},value=an int))),
	2: Assignment(pc=7,DVar(useSites={14},value=an int,origin=2),StaticFunctionCall(pc=7,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3},value=an int),UVar(defSites={1},value=an int)))),
	3: Assignment(pc=15,DVar(useSites={4},value=an int,origin=3),GetField(pc=15,java.util.regex.Pattern$NotBehindS,rmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$NotBehindS[↦-1;refId=102]))),
	4: Assignment(pc=18,DVar(useSites={5},value=an int,origin=4),PrefixExpr(pc=18,ComputationalTypeInt,-,UVar(defSites={3},value=an int))),
	5: Assignment(pc=19,DVar(useSites={21},value=an int,origin=5),StaticFunctionCall(pc=19,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={-3},value=an int),UVar(defSites={4},value=an int)))),
	6: Assignment(pc=25,DVar(useSites={33},value=an int,origin=6),GetField(pc=25,java.util.regex.Matcher,from,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	7: Assignment(pc=31,DVar(useSites={34},value=an int,origin=7),GetField(pc=31,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	8: Assignment(pc=36,DVar(useSites={22,35},value=int = 0,origin=8),IntConst(pc=36,0)),
	9: Assignment(pc=40,DVar(useSites={10},value=int ∈ [0,1],origin=9),GetField(pc=40,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	10: If(pc=43,UVar(defSites={9},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=13),
	11: Assignment(pc=47,DVar(useSites={15},value=an int,origin=11),GetField(pc=47,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	12: Goto(pc=50,target=14),
	13: Assignment(pc=53,DVar(useSites={15},value=an int,origin=13),IntConst(pc=53,0)),
	14: Assignment(pc=59,DVar(useSites={15},value=an int,origin=14),BinaryExpr(pc=59,ComputationalTypeInt,UVar(defSites={-3},value=an int),-,UVar(defSites={2},value=an int))),
	15: Assignment(pc=62,DVar(useSites={26,23},value=an int,origin=15),StaticFunctionCall(pc=62,java.lang.Math,isInterface=false,int max(int,int),(UVar(defSites={14},value=an int),UVar(defSites={13,11},value=an int)))),
	16: PutField(pc=69,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int)),
	17: Assignment(pc=73,DVar(useSites={18},value=int ∈ [0,1],origin=17),GetField(pc=73,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	18: If(pc=76,UVar(defSites={17},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=21),
	19: Assignment(pc=80,DVar(useSites={20},value=int = 0,origin=19),IntConst(pc=80,0)),
	20: PutField(pc=81,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={19},value=int = 0)),
	21: Assignment(pc=87,DVar(useSites={28,26,25,23,31},value=an int,origin=21),BinaryExpr(pc=87,ComputationalTypeInt,UVar(defSites={-3},value=an int),-,UVar(defSites={5},value=an int))),
	22: If(pc=92,UVar(defSites={8,25},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=33),
	23: If(pc=99,UVar(defSites={21,31},value=an int),<,UVar(defSites={15},value=an int),target=33),
	24: Assignment(pc=103,DVar(useSites={25},value={_ <: java.util.regex.Pattern$Node, null}[↦103;refId=116],origin=24),GetField(pc=103,java.util.regex.Pattern$NotBehindS,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$NotBehindS[↦-1;refId=102]))),
	25: Assignment(pc=110,DVar(useSites={22,35},value=int ∈ [0,1],origin=25),VirtualFunctionCall(pc=110,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={24},value={_ <: java.util.regex.Pattern$Node, null}[↦103;refId=116]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={21,31},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	26: If(pc=121,UVar(defSites={21,31},value=an int),<=,UVar(defSites={15},value=an int),target=30),
	27: Assignment(pc=127,DVar(useSites={28},value=int = -1,origin=27),IntConst(pc=127,-1)),
	28: Assignment(pc=128,DVar(useSites={31},value=an int,origin=28),StaticFunctionCall(pc=128,java.util.regex.Pattern,isInterface=false,int countChars(java.lang.CharSequence,int,int),(UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104]),UVar(defSites={21,31},value=int ∈ [-2147483647,2147483647]),UVar(defSites={27},value=int = -1)))),
	29: Goto(pc=131,target=31),
	30: Assignment(pc=134,DVar(useSites={31},value=an int,origin=30),IntConst(pc=134,1)),
	31: Assignment(pc=135,DVar(useSites={32,28,26,25,23},value=an int,origin=31),BinaryExpr(pc=135,ComputationalTypeInt,UVar(defSites={21,31},value=an int),-,UVar(defSites={28,30},value=an int))),
	32: Goto(pc=138,target=22),
	33: PutField(pc=144,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={6},value=an int)),
	34: PutField(pc=150,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={7},value=an int)),
	35: If(pc=155,UVar(defSites={8,25},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=41),
	36: Assignment(pc=159,DVar(useSites={37},value={_ <: java.util.regex.Pattern$Node, null}[↦159;refId=120],origin=36),GetField(pc=159,java.util.regex.Pattern$NotBehindS,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$NotBehindS[↦-1;refId=102]))),
	37: Assignment(pc=165,DVar(useSites={38},value=int ∈ [0,1],origin=37),VirtualFunctionCall(pc=165,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={36},value={_ <: java.util.regex.Pattern$Node, null}[↦159;refId=120]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	38: If(pc=168,UVar(defSites={37},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=41),
	39: Assignment(pc=171,DVar(useSites={42},value=int = 1,origin=39),IntConst(pc=171,1)),
	40: Goto(pc=172,target=42),
	41: Assignment(pc=175,DVar(useSites={42},value=int ∈ [0,1],origin=41),IntConst(pc=175,0)),
	42: ReturnValue(pc=176,UVar(defSites={41,39},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_7,BB_4}
	BB_10: BasicBlock(start=27,end=28) -> {BB_7,BB_2}
	BB_11: BasicBlock(start=7,end=10) -> {BB_6,BB_d}
	BB_12: BasicBlock(start=39,end=40) -> {BB_8}
	BB_13: BasicBlock(start=16,end=18) -> {BB_b,BB_19}
	BB_14: BasicBlock(start=31,end=32) -> {BB_f}
	BB_15: BasicBlock(start=26,end=26) -> {BB_10,BB_18}
	BB_16: BasicBlock(start=23,end=23) -> {BB_9,BB_c}
	BB_17: BasicBlock(start=36,end=37) -> {BB_7,BB_a}
	BB_18: BasicBlock(start=30,end=30) -> {BB_14}
	BB_19: BasicBlock(start=19,end=20) -> {BB_b}
	BB_1: BasicBlock(start=14,end=15) -> {BB_7,BB_13}
	BB_2: BasicBlock(start=29,end=29) -> {BB_14}
	BB_3: BasicBlock(start=6,end=6) -> {BB_7,BB_11}
	BB_4: BasicBlock(start=3,end=5) -> {BB_7,BB_3}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=11,end=12) -> {BB_1}
	BB_7: ExitNode(normalReturn=false)
	BB_8: BasicBlock(start=42,end=42) -> {BB_5}
	BB_9: BasicBlock(start=24,end=25) -> {BB_7,BB_15}
	BB_a: BasicBlock(start=38,end=38) -> {BB_12,BB_e}
	BB_b: BasicBlock(start=21,end=21) -> {BB_f}
	BB_c: BasicBlock(start=33,end=35) -> {BB_17,BB_e}
	BB_d: BasicBlock(start=13,end=13) -> {BB_1}
	BB_e: BasicBlock(start=41,end=41) -> {BB_8}
	BB_f: BasicBlock(start=22,end=22) -> {BB_c,BB_16}
))

