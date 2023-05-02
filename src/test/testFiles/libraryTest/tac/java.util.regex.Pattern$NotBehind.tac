void <init>(java.util.regex.Pattern$Node,int,int)
AITACode(params=(Parameters(
	0: useSites={0,2,1,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3),
	3: useSites={3} (origin=-4)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$NotBehind,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: PutField(pc=11,java.util.regex.Pattern$NotBehind,rmax,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]),UVar(defSites={-3},value=an int)),
	3: PutField(pc=16,java.util.regex.Pattern$NotBehind,rmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]),UVar(defSites={-4},value=an int)),
	4: Return(pc=19)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=4) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={16,8,20,27} (origin=-1),
	1: useSites={0,24,12,28,1,25,5,21,3,11,15} (origin=-2),
	2: useSites={28,17,9,11} (origin=-3),
	3: useSites={28,21} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={25},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=7,DVar(useSites={24},value=an int,origin=1),GetField(pc=7,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	2: Assignment(pc=12,DVar(useSites={18,26},value=int = 0,origin=2),IntConst(pc=12,0)),
	3: Assignment(pc=16,DVar(useSites={4},value=int ∈ [0,1],origin=3),GetField(pc=16,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	4: If(pc=19,UVar(defSites={3},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=7),
	5: Assignment(pc=23,DVar(useSites={10},value=an int,origin=5),GetField(pc=23,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	6: Goto(pc=26,target=8),
	7: Assignment(pc=29,DVar(useSites={10},value=an int,origin=7),IntConst(pc=29,0)),
	8: Assignment(pc=34,DVar(useSites={9},value=an int,origin=8),GetField(pc=34,java.util.regex.Pattern$NotBehind,rmax,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]))),
	9: Assignment(pc=37,DVar(useSites={10},value=an int,origin=9),BinaryExpr(pc=37,ComputationalTypeInt,UVar(defSites={-3},value=an int),-,UVar(defSites={8},value=an int))),
	10: Assignment(pc=40,DVar(useSites={19},value=an int,origin=10),StaticFunctionCall(pc=40,java.lang.Math,isInterface=false,int max(int,int),(UVar(defSites={9},value=an int),UVar(defSites={5,7},value=an int)))),
	11: PutField(pc=47,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int)),
	12: Assignment(pc=51,DVar(useSites={13},value=int ∈ [0,1],origin=12),GetField(pc=51,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	13: If(pc=54,UVar(defSites={12},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=16),
	14: Assignment(pc=58,DVar(useSites={15},value=int = 0,origin=14),IntConst(pc=58,0)),
	15: PutField(pc=59,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={14},value=int = 0)),
	16: Assignment(pc=64,DVar(useSites={17},value=an int,origin=16),GetField(pc=64,java.util.regex.Pattern$NotBehind,rmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]))),
	17: Assignment(pc=67,DVar(useSites={22,21,19},value=an int,origin=17),BinaryExpr(pc=67,ComputationalTypeInt,UVar(defSites={-3},value=an int),-,UVar(defSites={16},value=an int))),
	18: If(pc=72,UVar(defSites={2,21},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=24),
	19: If(pc=79,UVar(defSites={22,17},value=an int),<,UVar(defSites={10},value=an int),target=24),
	20: Assignment(pc=83,DVar(useSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦83;refId=113],origin=20),GetField(pc=83,java.util.regex.Pattern$NotBehind,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]))),
	21: Assignment(pc=90,DVar(useSites={18,26},value=int ∈ [0,1],origin=21),VirtualFunctionCall(pc=90,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={20},value={_ <: java.util.regex.Pattern$Node, null}[↦83;refId=113]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={22,17},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	22: Assignment(pc=95,DVar(useSites={21,19,23},value=an int,origin=22),BinaryExpr(pc=95,ComputationalTypeInt,UVar(defSites={22,17},value=an int),+,IntConst(pc=95,-1))),
	23: Goto(pc=98,target=18),
	24: PutField(pc=104,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={1},value=an int)),
	25: PutField(pc=110,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={0},value=an int)),
	26: If(pc=115,UVar(defSites={2,21},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=32),
	27: Assignment(pc=119,DVar(useSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦119;refId=116],origin=27),GetField(pc=119,java.util.regex.Pattern$NotBehind,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$NotBehind[↦-1;refId=102]))),
	28: Assignment(pc=125,DVar(useSites={29},value=int ∈ [0,1],origin=28),VirtualFunctionCall(pc=125,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦119;refId=116]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	29: If(pc=128,UVar(defSites={28},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=32),
	30: Assignment(pc=131,DVar(useSites={33},value=int = 1,origin=30),IntConst(pc=131,1)),
	31: Goto(pc=132,target=33),
	32: Assignment(pc=135,DVar(useSites={33},value=int ∈ [0,1],origin=32),IntConst(pc=135,0)),
	33: ReturnValue(pc=136,UVar(defSites={32,30},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_b,BB_4}
	BB_10: BasicBlock(start=18,end=18) -> {BB_2,BB_13}
	BB_11: ExitNode(normalReturn=true)
	BB_12: BasicBlock(start=30,end=31) -> {BB_5}
	BB_13: BasicBlock(start=19,end=19) -> {BB_c,BB_2}
	BB_1: BasicBlock(start=5,end=6) -> {BB_a}
	BB_2: BasicBlock(start=24,end=26) -> {BB_f,BB_6}
	BB_3: BasicBlock(start=14,end=15) -> {BB_8}
	BB_4: BasicBlock(start=1,end=4) -> {BB_1,BB_7}
	BB_5: BasicBlock(start=33,end=33) -> {BB_11}
	BB_6: BasicBlock(start=32,end=32) -> {BB_5}
	BB_7: BasicBlock(start=7,end=7) -> {BB_a}
	BB_8: BasicBlock(start=16,end=17) -> {BB_10}
	BB_9: BasicBlock(start=11,end=13) -> {BB_8,BB_3}
	BB_a: BasicBlock(start=8,end=10) -> {BB_b,BB_9}
	BB_b: ExitNode(normalReturn=false)
	BB_c: BasicBlock(start=20,end=21) -> {BB_b,BB_e}
	BB_d: BasicBlock(start=29,end=29) -> {BB_12,BB_6}
	BB_e: BasicBlock(start=22,end=23) -> {BB_10}
	BB_f: BasicBlock(start=27,end=28) -> {BB_b,BB_d}
))

