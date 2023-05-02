boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={20,12,22,1,17,3,15} (origin=-1),
	1: useSites={4,20,6,22,15} (origin=-2),
	2: useSites={4,20,22,15} (origin=-3),
	3: useSites={4,20,22,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={20,2,10,22,15},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$Curly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	2: If(pc=9,UVar(defSites={0,10},value=int ∈ [0,2147483647]),>=,UVar(defSites={1},value=an int),target=12),
	3: Assignment(pc=13,DVar(useSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦13;refId=332],origin=3),GetField(pc=13,java.util.regex.Pattern$Curly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	4: Assignment(pc=19,DVar(useSites={5},value=int ∈ [0,1],origin=4),VirtualFunctionCall(pc=19,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={3},value={_ <: java.util.regex.Pattern$Node, null}[↦13;refId=332]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={6,-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	5: If(pc=22,UVar(defSites={4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=8),
	6: Assignment(pc=26,DVar(useSites={4,20,22,15},value=an int,origin=6),GetField(pc=26,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	7: Goto(pc=30,target=10),
	8: Assignment(pc=33,DVar(useSites={9},value=int = 0,origin=8),IntConst(pc=33,0)),
	9: ReturnValue(pc=34,UVar(defSites={8},value=int = 0)),
	10: Assignment(pc=35,DVar(useSites={20,2,22,11,15},value=int ∈ [1,2147483647],origin=10),BinaryExpr(pc=35,ComputationalTypeInt,UVar(defSites={0,10},value=int ∈ [0,2147483646]),+,IntConst(pc=35,1))),
	11: Goto(pc=38,target=1),
	12: Assignment(pc=42,DVar(useSites={14},value={java.util.regex.Pattern$Qtype, null}[↦42;refId=325],origin=12),GetField(pc=42,java.util.regex.Pattern$Curly,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	13: Assignment(pc=45,DVar(useSites={14},value={java.util.regex.Pattern$Qtype, null}[↦45;refId=326],origin=13),GetStatic(pc=45,java.util.regex.Pattern$Qtype,GREEDY,java.util.regex.Pattern$Qtype)),
	14: If(pc=48,UVar(defSites={12},value={java.util.regex.Pattern$Qtype, null}[↦42;refId=325]),!=,UVar(defSites={13},value={java.util.regex.Pattern$Qtype, null}[↦45;refId=326]),target=17),
	15: Assignment(pc=57,DVar(useSites={16},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=57,java.util.regex.Pattern$Curly,isInterface=false,boolean match0(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={6,-3},value=an int),UVar(defSites={0,10},value=int ∈ [0,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	16: ReturnValue(pc=60,UVar(defSites={15},value=int ∈ [0,1])),
	17: Assignment(pc=62,DVar(useSites={19},value={java.util.regex.Pattern$Qtype, null}[↦62;refId=327],origin=17),GetField(pc=62,java.util.regex.Pattern$Curly,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	18: Assignment(pc=65,DVar(useSites={19},value={java.util.regex.Pattern$Qtype, null}[↦65;refId=328],origin=18),GetStatic(pc=65,java.util.regex.Pattern$Qtype,LAZY,java.util.regex.Pattern$Qtype)),
	19: If(pc=68,UVar(defSites={17},value={java.util.regex.Pattern$Qtype, null}[↦62;refId=327]),!=,UVar(defSites={18},value={java.util.regex.Pattern$Qtype, null}[↦65;refId=328]),target=22),
	20: Assignment(pc=77,DVar(useSites={21},value=int ∈ [0,1],origin=20),VirtualFunctionCall(pc=77,java.util.regex.Pattern$Curly,isInterface=false,boolean match1(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={6,-3},value=an int),UVar(defSites={0,10},value=int ∈ [0,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	21: ReturnValue(pc=80,UVar(defSites={20},value=int ∈ [0,1])),
	22: Assignment(pc=87,DVar(useSites={23},value=int ∈ [0,1],origin=22),VirtualFunctionCall(pc=87,java.util.regex.Pattern$Curly,isInterface=false,boolean match2(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={6,-3},value=an int),UVar(defSites={0,10},value=int ∈ [0,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	23: ReturnValue(pc=90,UVar(defSites={22},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4}
	BB_10: ExitNode(normalReturn=false)
	BB_11: BasicBlock(start=15,end=15) -> {BB_10,BB_d}
	BB_1: BasicBlock(start=5,end=5) -> {BB_f,BB_5}
	BB_2: BasicBlock(start=10,end=11) -> {BB_4}
	BB_3: BasicBlock(start=20,end=20) -> {BB_10,BB_6}
	BB_4: BasicBlock(start=1,end=2) -> {BB_b,BB_9}
	BB_5: BasicBlock(start=6,end=6) -> {BB_10,BB_a}
	BB_6: BasicBlock(start=21,end=21) -> {BB_c}
	BB_7: BasicBlock(start=17,end=19) -> {BB_8,BB_3}
	BB_8: BasicBlock(start=22,end=22) -> {BB_10,BB_e}
	BB_9: BasicBlock(start=12,end=14) -> {BB_7,BB_11}
	BB_a: BasicBlock(start=7,end=7) -> {BB_2}
	BB_b: BasicBlock(start=3,end=4) -> {BB_10,BB_1}
	BB_c: ExitNode(normalReturn=true)
	BB_d: BasicBlock(start=16,end=16) -> {BB_c}
	BB_e: BasicBlock(start=23,end=23) -> {BB_c}
	BB_f: BasicBlock(start=8,end=9) -> {BB_c}
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={8,18,30,5,37,31} (origin=-1),
	1: useSites={0,24,4,36,28,2,6,38,14,1,33,17,21,13,3,27,7} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={10,11},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={20,22},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	2: Assignment(pc=11,DVar(useSites={15},value=int ∈ [0,1],origin=2),GetField(pc=11,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	3: Assignment(pc=17,DVar(useSites={33},value=int ∈ [0,1],origin=3),GetField(pc=17,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	4: VirtualMethodCall(pc=23,java.util.regex.Pattern$TreeInfo,isInterface=false,void reset(),UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),()),
	5: Assignment(pc=27,DVar(useSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=106],origin=5),GetField(pc=27,java.util.regex.Pattern$Curly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	6: ExprStmt(pc=31,VirtualFunctionCall(pc=31,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=106]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	7: Assignment(pc=36,DVar(useSites={9},value=an int,origin=7),GetField(pc=36,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	8: Assignment(pc=40,DVar(useSites={9},value=an int,origin=8),GetField(pc=40,java.util.regex.Pattern$Curly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	9: Assignment(pc=43,DVar(useSites={10},value=an int,origin=9),BinaryExpr(pc=43,ComputationalTypeInt,UVar(defSites={7},value=an int),*,UVar(defSites={8},value=an int))),
	10: Assignment(pc=45,DVar(useSites={13,11},value=an int,origin=10),BinaryExpr(pc=45,ComputationalTypeInt,UVar(defSites={9},value=an int),+,UVar(defSites={0},value=an int))),
	11: If(pc=51,UVar(defSites={10},value=an int),>=,UVar(defSites={0},value=an int),target=13),
	12: Assignment(pc=54,DVar(useSites={13},value=int = 268435455,origin=12),IntConst(pc=54,268435455)),
	13: PutField(pc=61,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={12,10},value=an int)),
	14: Assignment(pc=67,DVar(useSites={15},value=int ∈ [0,1],origin=14),GetField(pc=67,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	15: Assignment(pc=70,DVar(useSites={16},value=int ∈ [0,1],origin=15),BinaryExpr(pc=70,ComputationalTypeInt,UVar(defSites={2},value=int ∈ [0,1]),&,UVar(defSites={14},value=int ∈ [0,1]))),
	16: If(pc=71,UVar(defSites={15},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=26),
	17: Assignment(pc=75,DVar(useSites={19},value=an int,origin=17),GetField(pc=75,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	18: Assignment(pc=79,DVar(useSites={19},value=an int,origin=18),GetField(pc=79,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	19: Assignment(pc=82,DVar(useSites={20},value=an int,origin=19),BinaryExpr(pc=82,ComputationalTypeInt,UVar(defSites={17},value=an int),*,UVar(defSites={18},value=an int))),
	20: Assignment(pc=84,DVar(useSites={22,21},value=an int,origin=20),BinaryExpr(pc=84,ComputationalTypeInt,UVar(defSites={19},value=an int),+,UVar(defSites={1},value=an int))),
	21: PutField(pc=90,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={20},value=an int)),
	22: If(pc=96,UVar(defSites={20},value=an int),>=,UVar(defSites={1},value=an int),target=28),
	23: Assignment(pc=100,DVar(useSites={24},value=int = 0,origin=23),IntConst(pc=100,0)),
	24: PutField(pc=101,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={23},value=int = 0)),
	25: Goto(pc=104,target=28),
	26: Assignment(pc=108,DVar(useSites={27},value=int = 0,origin=26),IntConst(pc=108,0)),
	27: PutField(pc=109,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={26},value=int = 0)),
	28: Assignment(pc=113,DVar(useSites={29},value=int ∈ [0,1],origin=28),GetField(pc=113,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	29: If(pc=116,UVar(defSites={28},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=35),
	30: Assignment(pc=120,DVar(useSites={32},value=an int,origin=30),GetField(pc=120,java.util.regex.Pattern$Curly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	31: Assignment(pc=124,DVar(useSites={32},value=an int,origin=31),GetField(pc=124,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	32: If(pc=127,UVar(defSites={30},value=an int),!=,UVar(defSites={31},value=an int),target=35),
	33: PutField(pc=133,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={3},value=int ∈ [0,1])),
	34: Goto(pc=136,target=37),
	35: Assignment(pc=140,DVar(useSites={36},value=int = 0,origin=35),IntConst(pc=140,0)),
	36: PutField(pc=141,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={35},value=int = 0)),
	37: Assignment(pc=145,DVar(useSites={38},value={_ <: java.util.regex.Pattern$Node, null}[↦145;refId=109],origin=37),GetField(pc=145,java.util.regex.Pattern$Curly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	38: Assignment(pc=149,DVar(useSites={39},value=int ∈ [0,1],origin=38),VirtualFunctionCall(pc=149,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={37},value={_ <: java.util.regex.Pattern$Node, null}[↦145;refId=109]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	39: ReturnValue(pc=152,UVar(defSites={38},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_a,BB_3}
	BB_10: BasicBlock(start=23,end=25) -> {BB_b}
	BB_1: BasicBlock(start=5,end=6) -> {BB_a,BB_d}
	BB_2: BasicBlock(start=37,end=38) -> {BB_a,BB_e}
	BB_3: BasicBlock(start=1,end=4) -> {BB_a,BB_1}
	BB_4: BasicBlock(start=13,end=16) -> {BB_5,BB_f}
	BB_5: BasicBlock(start=17,end=22) -> {BB_b,BB_10}
	BB_6: BasicBlock(start=12,end=12) -> {BB_4}
	BB_7: BasicBlock(start=35,end=36) -> {BB_2}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=30,end=32) -> {BB_c,BB_7}
	BB_a: ExitNode(normalReturn=false)
	BB_b: BasicBlock(start=28,end=29) -> {BB_7,BB_9}
	BB_c: BasicBlock(start=33,end=34) -> {BB_2}
	BB_d: BasicBlock(start=7,end=11) -> {BB_4,BB_6}
	BB_e: BasicBlock(start=39,end=39) -> {BB_8}
	BB_f: BasicBlock(start=26,end=27) -> {BB_b}
))

void <init>(java.util.regex.Pattern$Node,int,int,java.util.regex.Pattern$Qtype)
AITACode(params=(Parameters(
	0: useSites={0,4,2,1,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={3} (origin=-3),
	3: useSites={4} (origin=-4),
	4: useSites={2} (origin=-5)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Curly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: PutField(pc=12,java.util.regex.Pattern$Curly,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),UVar(defSites={-5},value={java.util.regex.Pattern$Qtype, null}[↦-5;refId=104])),
	3: PutField(pc=17,java.util.regex.Pattern$Curly,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),UVar(defSites={-3},value=an int)),
	4: PutField(pc=22,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),UVar(defSites={-4},value=an int)),
	5: Return(pc=25)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=5) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match1(java.util.regex.Matcher,int,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,9,5} (origin=-1),
	1: useSites={18,10,14,1} (origin=-2),
	2: useSites={10,1,15} (origin=-3),
	3: useSites={6,19} (origin=-4),
	4: useSites={10,1} (origin=-5)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Pattern$Curly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	1: Assignment(pc=8,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=8,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={0},value={_ <: java.util.regex.Pattern$Node, null}[↦1;refId=105]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={18,-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	2: If(pc=11,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=5),
	3: Assignment(pc=14,DVar(useSites={4},value=int = 1,origin=3),IntConst(pc=14,1)),
	4: ReturnValue(pc=15,UVar(defSites={3},value=int = 1)),
	5: Assignment(pc=18,DVar(useSites={6},value=an int,origin=5),GetField(pc=18,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	6: If(pc=21,UVar(defSites={-4,19},value=an int),<,UVar(defSites={5},value=an int),target=9),
	7: Assignment(pc=24,DVar(useSites={8},value=int = 0,origin=7),IntConst(pc=24,0)),
	8: ReturnValue(pc=25,UVar(defSites={7},value=int = 0)),
	9: Assignment(pc=27,DVar(useSites={10},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=108],origin=9),GetField(pc=27,java.util.regex.Pattern$Curly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	10: Assignment(pc=34,DVar(useSites={11},value=int ∈ [0,1],origin=10),VirtualFunctionCall(pc=34,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦27;refId=108]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={18,-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	11: If(pc=37,UVar(defSites={10},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=14),
	12: Assignment(pc=40,DVar(useSites={13},value=int = 0,origin=12),IntConst(pc=40,0)),
	13: ReturnValue(pc=41,UVar(defSites={12},value=int = 0)),
	14: Assignment(pc=44,DVar(useSites={15},value=an int,origin=14),GetField(pc=44,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	15: If(pc=47,UVar(defSites={18,-3},value=an int),!=,UVar(defSites={14},value=an int),target=18),
	16: Assignment(pc=50,DVar(useSites={17},value=int = 0,origin=16),IntConst(pc=50,0)),
	17: ReturnValue(pc=51,UVar(defSites={16},value=int = 0)),
	18: Assignment(pc=53,DVar(useSites={10,1,15},value=an int,origin=18),GetField(pc=53,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	19: Assignment(pc=57,DVar(useSites={20,6},value=int ∈ [-2147483647,2147483647],origin=19),BinaryExpr(pc=57,ComputationalTypeInt,UVar(defSites={-4,19},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=57,1))),
	20: Goto(pc=60,target=0)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_a,BB_4}
	BB_1: BasicBlock(start=5,end=6) -> {BB_6,BB_3}
	BB_2: BasicBlock(start=14,end=14) -> {BB_a,BB_b}
	BB_3: BasicBlock(start=9,end=10) -> {BB_a,BB_9}
	BB_4: BasicBlock(start=2,end=2) -> {BB_1,BB_7}
	BB_5: BasicBlock(start=12,end=13) -> {BB_d}
	BB_6: BasicBlock(start=7,end=8) -> {BB_d}
	BB_7: BasicBlock(start=3,end=4) -> {BB_d}
	BB_8: BasicBlock(start=16,end=17) -> {BB_d}
	BB_9: BasicBlock(start=11,end=11) -> {BB_5,BB_2}
	BB_a: ExitNode(normalReturn=false)
	BB_b: BasicBlock(start=15,end=15) -> {BB_c,BB_8}
	BB_c: BasicBlock(start=18,end=20) -> {BB_0}
	BB_d: ExitNode(normalReturn=true)
))

boolean match2(java.util.regex.Matcher,int,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,2,10} (origin=-1),
	1: useSites={5,3,11,7} (origin=-2),
	2: useSites={6,3,11} (origin=-3),
	3: useSites={8,1} (origin=-4),
	4: useSites={3,11} (origin=-5)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	1: If(pc=5,UVar(defSites={8,-4},value=an int),>=,UVar(defSites={0},value=an int),target=10),
	2: Assignment(pc=9,DVar(useSites={3},value={_ <: java.util.regex.Pattern$Node, null}[↦9;refId=105],origin=2),GetField(pc=9,java.util.regex.Pattern$Curly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	3: Assignment(pc=16,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=16,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={2},value={_ <: java.util.regex.Pattern$Node, null}[↦9;refId=105]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3,7},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	4: If(pc=19,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=10),
	5: Assignment(pc=27,DVar(useSites={6},value=an int,origin=5),GetField(pc=27,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	6: If(pc=30,UVar(defSites={-3,7},value=an int),==,UVar(defSites={5},value=an int),target=10),
	7: Assignment(pc=37,DVar(useSites={6,3,11},value=an int,origin=7),GetField(pc=37,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	8: Assignment(pc=41,DVar(useSites={1,9},value=int ∈ [-2147483647,2147483647],origin=8),BinaryExpr(pc=41,ComputationalTypeInt,UVar(defSites={8,-4},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=41,1))),
	9: Goto(pc=44,target=0),
	10: Assignment(pc=48,DVar(useSites={11},value={_ <: java.util.regex.Pattern$Node, null}[↦48;refId=109],origin=10),GetField(pc=48,java.util.regex.Pattern$Curly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	11: Assignment(pc=55,DVar(useSites={12},value=int ∈ [0,1],origin=11),VirtualFunctionCall(pc=55,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={10},value={_ <: java.util.regex.Pattern$Node, null}[↦48;refId=109]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3,7},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	12: ReturnValue(pc=58,UVar(defSites={11},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_9,BB_3}
	BB_2: BasicBlock(start=10,end=11) -> {BB_9,BB_5}
	BB_3: BasicBlock(start=6,end=6) -> {BB_6,BB_2}
	BB_4: BasicBlock(start=2,end=3) -> {BB_9,BB_8}
	BB_5: BasicBlock(start=12,end=12) -> {BB_7}
	BB_6: BasicBlock(start=7,end=9) -> {BB_0}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=4,end=4) -> {BB_1,BB_2}
	BB_9: ExitNode(normalReturn=false)
))

boolean match0(java.util.regex.Matcher,int,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={0,32,24,2,42,5,13,15} (origin=-1),
	1: useSites={16,8,24,6,33,21,3,19,11,43} (origin=-2),
	2: useSites={6,9,3,43} (origin=-3),
	3: useSites={12,1,31} (origin=-4),
	4: useSites={16,24,6,33,3,43} (origin=-5)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	1: If(pc=5,UVar(defSites={-4},value=an int),<,UVar(defSites={0},value=an int),target=5),
	2: Assignment(pc=9,DVar(useSites={3},value={_ <: java.util.regex.Pattern$Node, null}[↦9;refId=109],origin=2),GetField(pc=9,java.util.regex.Pattern$Curly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	3: Assignment(pc=16,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=16,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={2},value={_ <: java.util.regex.Pattern$Node, null}[↦9;refId=109]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	4: ReturnValue(pc=19,UVar(defSites={3},value=int ∈ [0,1])),
	5: Assignment(pc=24,DVar(useSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦24;refId=105],origin=5),GetField(pc=24,java.util.regex.Pattern$Curly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	6: Assignment(pc=31,DVar(useSites={7},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=31,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦24;refId=105]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	7: If(pc=34,UVar(defSites={6},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=42),
	8: Assignment(pc=38,DVar(useSites={9},value=an int,origin=8),GetField(pc=38,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	9: Assignment(pc=42,DVar(useSites={28,18,10,37},value=an int,origin=9),BinaryExpr(pc=42,ComputationalTypeInt,UVar(defSites={8},value=an int),-,UVar(defSites={-3},value=an int))),
	10: If(pc=47,UVar(defSites={9},value=an int),==,IntConst(pc=-333,0),target=42),
	11: Assignment(pc=54,DVar(useSites={16,28,18,33,37},value=an int,origin=11),GetField(pc=54,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	12: Assignment(pc=58,DVar(useSites={38,14,29,23,31},value=int ∈ [-2147483647,2147483647],origin=12),BinaryExpr(pc=58,ComputationalTypeInt,UVar(defSites={-4},value=int ∈ [-2147483648,2147483646]),+,IntConst(pc=58,1))),
	13: Assignment(pc=63,DVar(useSites={14},value=an int,origin=13),GetField(pc=63,java.util.regex.Pattern$Curly,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	14: If(pc=66,UVar(defSites={12,29},value=int ∈ [-2147483647,2147483647]),>=,UVar(defSites={13},value=an int),target=31),
	15: Assignment(pc=70,DVar(useSites={16},value={_ <: java.util.regex.Pattern$Node, null}[↦70;refId=115],origin=15),GetField(pc=70,java.util.regex.Pattern$Curly,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	16: Assignment(pc=77,DVar(useSites={17},value=int ∈ [0,1],origin=16),VirtualFunctionCall(pc=77,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦70;refId=115]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={28,11},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	17: If(pc=80,UVar(defSites={16},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=31),
	18: Assignment(pc=89,DVar(useSites={20},value=an int,origin=18),BinaryExpr(pc=89,ComputationalTypeInt,UVar(defSites={28,11},value=an int),+,UVar(defSites={9},value=an int))),
	19: Assignment(pc=91,DVar(useSites={20},value=an int,origin=19),GetField(pc=91,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	20: If(pc=94,UVar(defSites={18},value=an int),==,UVar(defSites={19},value=an int),target=28),
	21: Assignment(pc=100,DVar(useSites={24},value=an int,origin=21),GetField(pc=100,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	22: Assignment(pc=104,DVar(useSites={23},value=int = 1,origin=22),IntConst(pc=104,1)),
	23: Assignment(pc=105,DVar(useSites={24},value=int ∈ [-2147483646,2147483647],origin=23),BinaryExpr(pc=105,ComputationalTypeInt,UVar(defSites={12,29},value=int ∈ [-2147483647,2147483646]),+,UVar(defSites={22},value=int = 1))),
	24: Assignment(pc=108,DVar(useSites={25},value=int ∈ [0,1],origin=24),VirtualFunctionCall(pc=108,java.util.regex.Pattern$Curly,isInterface=false,boolean match0(java.util.regex.Matcher,int,int,java.lang.CharSequence),UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={21},value=an int),UVar(defSites={23},value=int ∈ [-2147483646,2147483647]),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	25: If(pc=111,UVar(defSites={24},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=31),
	26: Assignment(pc=114,DVar(useSites={27},value=int = 1,origin=26),IntConst(pc=114,1)),
	27: ReturnValue(pc=115,UVar(defSites={26},value=int = 1)),
	28: Assignment(pc=119,DVar(useSites={16,18,33,37,29},value=an int,origin=28),BinaryExpr(pc=119,ComputationalTypeInt,UVar(defSites={28,11},value=an int),+,UVar(defSites={9},value=an int))),
	29: Assignment(pc=121,DVar(useSites={38,14,30,23,31},value=int ∈ [-2147483646,2147483647],origin=29),BinaryExpr(pc=121,ComputationalTypeInt,UVar(defSites={12,29},value=int ∈ [-2147483647,2147483646]),+,IntConst(pc=121,1))),
	30: Goto(pc=124,target=13),
	31: If(pc=130,UVar(defSites={12,38,29},value=an int),<,UVar(defSites={-4},value=int ∈ [-2147483648,2147483646]),target=40),
	32: Assignment(pc=134,DVar(useSites={33},value={_ <: java.util.regex.Pattern$Node, null}[↦134;refId=122],origin=32),GetField(pc=134,java.util.regex.Pattern$Curly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	33: Assignment(pc=141,DVar(useSites={34},value=int ∈ [0,1],origin=33),VirtualFunctionCall(pc=141,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={32},value={_ <: java.util.regex.Pattern$Node, null}[↦134;refId=122]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={28,37,11},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	34: If(pc=144,UVar(defSites={33},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=37),
	35: Assignment(pc=147,DVar(useSites={36},value=int = 1,origin=35),IntConst(pc=147,1)),
	36: ReturnValue(pc=148,UVar(defSites={35},value=int = 1)),
	37: Assignment(pc=152,DVar(useSites={38,33},value=an int,origin=37),BinaryExpr(pc=152,ComputationalTypeInt,UVar(defSites={28,37,11},value=an int),-,UVar(defSites={9},value=an int))),
	38: Assignment(pc=154,DVar(useSites={39,31},value=an int,origin=38),BinaryExpr(pc=154,ComputationalTypeInt,UVar(defSites={12,38,29},value=an int),+,IntConst(pc=154,-1))),
	39: Goto(pc=157,target=31),
	40: Assignment(pc=160,DVar(useSites={41},value=int = 0,origin=40),IntConst(pc=160,0)),
	41: ReturnValue(pc=161,UVar(defSites={40},value=int = 0)),
	42: Assignment(pc=163,DVar(useSites={43},value={_ <: java.util.regex.Pattern$Node, null}[↦163;refId=112],origin=42),GetField(pc=163,java.util.regex.Pattern$Curly,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Curly[↦-1;refId=102]))),
	43: Assignment(pc=170,DVar(useSites={44},value=int ∈ [0,1],origin=43),VirtualFunctionCall(pc=170,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={42},value={_ <: java.util.regex.Pattern$Node, null}[↦163;refId=112]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-5},value={_ <: java.lang.CharSequence, null}[↦-5;refId=104])))),
	44: ReturnValue(pc=173,UVar(defSites={43},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_10: BasicBlock(start=21,end=24) -> {BB_19,BB_e}
	BB_11: BasicBlock(start=17,end=17) -> {BB_14,BB_8}
	BB_12: BasicBlock(start=32,end=33) -> {BB_19,BB_13}
	BB_13: BasicBlock(start=34,end=34) -> {BB_d,BB_7}
	BB_14: BasicBlock(start=18,end=20) -> {BB_f,BB_10}
	BB_15: ExitNode(normalReturn=true)
	BB_16: BasicBlock(start=40,end=41) -> {BB_15}
	BB_17: BasicBlock(start=26,end=27) -> {BB_15}
	BB_18: BasicBlock(start=4,end=4) -> {BB_15}
	BB_19: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=6) -> {BB_19,BB_6}
	BB_2: BasicBlock(start=9,end=10) -> {BB_c,BB_9}
	BB_3: BasicBlock(start=13,end=14) -> {BB_b,BB_8}
	BB_4: BasicBlock(start=2,end=3) -> {BB_19,BB_18}
	BB_5: BasicBlock(start=44,end=44) -> {BB_15}
	BB_6: BasicBlock(start=7,end=7) -> {BB_c,BB_a}
	BB_7: BasicBlock(start=35,end=36) -> {BB_15}
	BB_8: BasicBlock(start=31,end=31) -> {BB_16,BB_12}
	BB_9: BasicBlock(start=11,end=12) -> {BB_3}
	BB_a: BasicBlock(start=8,end=8) -> {BB_19,BB_2}
	BB_b: BasicBlock(start=15,end=16) -> {BB_19,BB_11}
	BB_c: BasicBlock(start=42,end=43) -> {BB_19,BB_5}
	BB_d: BasicBlock(start=37,end=39) -> {BB_8}
	BB_e: BasicBlock(start=25,end=25) -> {BB_17,BB_8}
	BB_f: BasicBlock(start=28,end=30) -> {BB_3}
))

