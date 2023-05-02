void <init>(java.util.regex.Pattern$Node,int,int)
AITACode(params=(Parameters(
	0: useSites={0,2,1,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3),
	3: useSites={3} (origin=-4)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Behind,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: PutField(pc=11,java.util.regex.Pattern$Behind,rmax,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]),UVar(defSites={-3},value=an int)),
	3: PutField(pc=16,java.util.regex.Pattern$Behind,rmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]),UVar(defSites={-4},value=an int)),
	4: Return(pc=19)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=4) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={16,20,27,7} (origin=-1),
	1: useSites={0,24,4,12,28,2,10,25,21,11,15} (origin=-2),
	2: useSites={8,28,17,11} (origin=-3),
	3: useSites={28,21} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={24},value=an int,origin=0),GetField(pc=1,java.util.regex.Matcher,from,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={18,26},value=int = 0,origin=1),IntConst(pc=6,0)),
	2: Assignment(pc=10,DVar(useSites={3},value=int ∈ [0,1],origin=2),GetField(pc=10,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	3: If(pc=13,UVar(defSites={2},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=6),
	4: Assignment(pc=17,DVar(useSites={9},value=an int,origin=4),GetField(pc=17,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	5: Goto(pc=20,target=7),
	6: Assignment(pc=23,DVar(useSites={9},value=an int,origin=6),IntConst(pc=23,0)),
	7: Assignment(pc=28,DVar(useSites={8},value=an int,origin=7),GetField(pc=28,java.util.regex.Pattern$Behind,rmax,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]))),
	8: Assignment(pc=31,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=31,ComputationalTypeInt,UVar(defSites={-3},value=an int),-,UVar(defSites={7},value=an int))),
	9: Assignment(pc=34,DVar(useSites={19},value=an int,origin=9),StaticFunctionCall(pc=34,java.lang.Math,isInterface=false,int max(int,int),(UVar(defSites={8},value=an int),UVar(defSites={4,6},value=an int)))),
	10: Assignment(pc=40,DVar(useSites={25},value=an int,origin=10),GetField(pc=40,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	11: PutField(pc=47,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int)),
	12: Assignment(pc=51,DVar(useSites={13},value=int ∈ [0,1],origin=12),GetField(pc=51,java.util.regex.Matcher,transparentBounds,boolean,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	13: If(pc=54,UVar(defSites={12},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=16),
	14: Assignment(pc=58,DVar(useSites={15},value=int = 0,origin=14),IntConst(pc=58,0)),
	15: PutField(pc=59,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={14},value=int = 0)),
	16: Assignment(pc=64,DVar(useSites={17},value=an int,origin=16),GetField(pc=64,java.util.regex.Pattern$Behind,rmin,int,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]))),
	17: Assignment(pc=67,DVar(useSites={22,21,19},value=an int,origin=17),BinaryExpr(pc=67,ComputationalTypeInt,UVar(defSites={-3},value=an int),-,UVar(defSites={16},value=an int))),
	18: If(pc=72,UVar(defSites={1,21},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=24),
	19: If(pc=79,UVar(defSites={22,17},value=an int),<,UVar(defSites={9},value=an int),target=24),
	20: Assignment(pc=83,DVar(useSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦83;refId=110],origin=20),GetField(pc=83,java.util.regex.Pattern$Behind,cond,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]))),
	21: Assignment(pc=90,DVar(useSites={18,26},value=int ∈ [0,1],origin=21),VirtualFunctionCall(pc=90,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={20},value={_ <: java.util.regex.Pattern$Node, null}[↦83;refId=110]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={22,17},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	22: Assignment(pc=95,DVar(useSites={21,19,23},value=an int,origin=22),BinaryExpr(pc=95,ComputationalTypeInt,UVar(defSites={22,17},value=an int),+,IntConst(pc=95,-1))),
	23: Goto(pc=98,target=18),
	24: PutField(pc=104,java.util.regex.Matcher,from,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={0},value=an int)),
	25: PutField(pc=110,java.util.regex.Matcher,lookbehindTo,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={10},value=an int)),
	26: If(pc=115,UVar(defSites={1,21},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=32),
	27: Assignment(pc=119,DVar(useSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦119;refId=113],origin=27),GetField(pc=119,java.util.regex.Pattern$Behind,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$Behind[↦-1;refId=102]))),
	28: Assignment(pc=125,DVar(useSites={29},value=int ∈ [0,1],origin=28),VirtualFunctionCall(pc=125,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦119;refId=113]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	29: If(pc=128,UVar(defSites={28},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=32),
	30: Assignment(pc=131,DVar(useSites={33},value=int = 1,origin=30),IntConst(pc=131,1)),
	31: Goto(pc=132,target=33),
	32: Assignment(pc=135,DVar(useSites={33},value=int ∈ [0,1],origin=32),IntConst(pc=135,0)),
	33: ReturnValue(pc=136,UVar(defSites={32,30},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_13,BB_4}
	BB_10: BasicBlock(start=30,end=31) -> {BB_6}
	BB_11: BasicBlock(start=19,end=19) -> {BB_a,BB_2}
	BB_12: BasicBlock(start=4,end=5) -> {BB_8}
	BB_13: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=10,end=13) -> {BB_9,BB_3}
	BB_2: BasicBlock(start=24,end=26) -> {BB_d,BB_7}
	BB_3: BasicBlock(start=14,end=15) -> {BB_9}
	BB_4: BasicBlock(start=1,end=3) -> {BB_12,BB_5}
	BB_5: BasicBlock(start=6,end=6) -> {BB_8}
	BB_6: BasicBlock(start=33,end=33) -> {BB_f}
	BB_7: BasicBlock(start=32,end=32) -> {BB_6}
	BB_8: BasicBlock(start=7,end=9) -> {BB_13,BB_1}
	BB_9: BasicBlock(start=16,end=17) -> {BB_e}
	BB_a: BasicBlock(start=20,end=21) -> {BB_13,BB_c}
	BB_b: BasicBlock(start=29,end=29) -> {BB_10,BB_7}
	BB_c: BasicBlock(start=22,end=23) -> {BB_e}
	BB_d: BasicBlock(start=27,end=28) -> {BB_13,BB_b}
	BB_e: BasicBlock(start=18,end=18) -> {BB_2,BB_11}
	BB_f: ExitNode(normalReturn=true)
))

