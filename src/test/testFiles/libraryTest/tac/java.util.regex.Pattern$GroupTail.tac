void <init>(int,int)
AITACode(params=(Parameters(
	0: useSites={0,1,3} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$GroupTail,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]),UVar(defSites={-2},value=an int)),
	2: Assignment(pc=12,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=12,ComputationalTypeInt,UVar(defSites={-3},value=an int),+,UVar(defSites={-3},value=an int))),
	3: PutField(pc=13,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]),UVar(defSites={2},value=an int)),
	4: Return(pc=16)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=4) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={16,8,20,26,1,5,13,29} (origin=-1),
	1: useSites={0,4,12,28,25,21,35,7,15} (origin=-2),
	2: useSites={21,35,19} (origin=-3),
	3: useSites={21} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern$GroupTail,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={14,3},value=an int,origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: If(pc=13,UVar(defSites={2},value=an int),<,IntConst(pc=-333,0),target=35),
	4: Assignment(pc=17,DVar(useSites={6},value={int[], null}[↦17;refId=109],origin=4),GetField(pc=17,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	5: Assignment(pc=21,DVar(useSites={6},value=an int,origin=5),GetField(pc=21,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	6: Assignment(pc=24,DVar(useSites={27},value=an int,origin=6),ArrayLoad(pc=24,UVar(defSites={5},value=an int),UVar(defSites={4},value={int[], null}[↦17;refId=109]))),
	7: Assignment(pc=28,DVar(useSites={11},value={int[], null}[↦28;refId=112],origin=7),GetField(pc=28,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	8: Assignment(pc=32,DVar(useSites={10},value=an int,origin=8),GetField(pc=32,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	9: Assignment(pc=35,DVar(useSites={10},value=int = 1,origin=9),IntConst(pc=35,1)),
	10: Assignment(pc=36,DVar(useSites={11},value=an int,origin=10),BinaryExpr(pc=36,ComputationalTypeInt,UVar(defSites={8},value=an int),+,UVar(defSites={9},value=int = 1))),
	11: Assignment(pc=37,DVar(useSites={32},value=an int,origin=11),ArrayLoad(pc=37,UVar(defSites={10},value=an int),UVar(defSites={7},value={int[], null}[↦28;refId=112]))),
	12: Assignment(pc=41,DVar(useSites={14},value={int[], null}[↦41;refId=115],origin=12),GetField(pc=41,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	13: Assignment(pc=45,DVar(useSites={14},value=an int,origin=13),GetField(pc=45,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	14: ArrayStore(pc=50,UVar(defSites={12},value={int[], null}[↦41;refId=115]),UVar(defSites={13},value=an int),UVar(defSites={2},value=int ∈ [0,2147483647])),
	15: Assignment(pc=52,DVar(useSites={19},value={int[], null}[↦52;refId=118],origin=15),GetField(pc=52,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	16: Assignment(pc=56,DVar(useSites={18},value=an int,origin=16),GetField(pc=56,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	17: Assignment(pc=59,DVar(useSites={18},value=int = 1,origin=17),IntConst(pc=59,1)),
	18: Assignment(pc=60,DVar(useSites={19},value=an int,origin=18),BinaryExpr(pc=60,ComputationalTypeInt,UVar(defSites={16},value=an int),+,UVar(defSites={17},value=int = 1))),
	19: ArrayStore(pc=62,UVar(defSites={15},value={int[], null}[↦52;refId=118]),UVar(defSites={18},value=an int),UVar(defSites={-3},value=an int)),
	20: Assignment(pc=64,DVar(useSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦64;refId=121],origin=20),GetField(pc=64,java.util.regex.Pattern$GroupTail,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	21: Assignment(pc=70,DVar(useSites={22},value=int ∈ [0,1],origin=21),VirtualFunctionCall(pc=70,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={20},value={_ <: java.util.regex.Pattern$Node, null}[↦64;refId=121]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	22: If(pc=73,UVar(defSites={21},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=25),
	23: Assignment(pc=76,DVar(useSites={24},value=int = 1,origin=23),IntConst(pc=76,1)),
	24: ReturnValue(pc=77,UVar(defSites={23},value=int = 1)),
	25: Assignment(pc=79,DVar(useSites={27},value={int[], null}[↦79;refId=124],origin=25),GetField(pc=79,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	26: Assignment(pc=83,DVar(useSites={27},value=an int,origin=26),GetField(pc=83,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	27: ArrayStore(pc=88,UVar(defSites={25},value={int[], null}[↦79;refId=124]),UVar(defSites={26},value=an int),UVar(defSites={6},value=an int)),
	28: Assignment(pc=90,DVar(useSites={32},value={int[], null}[↦90;refId=127],origin=28),GetField(pc=90,java.util.regex.Matcher,groups,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	29: Assignment(pc=94,DVar(useSites={31},value=an int,origin=29),GetField(pc=94,java.util.regex.Pattern$GroupTail,groupIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupTail[↦-1;refId=102]))),
	30: Assignment(pc=97,DVar(useSites={31},value=int = 1,origin=30),IntConst(pc=97,1)),
	31: Assignment(pc=98,DVar(useSites={32},value=an int,origin=31),BinaryExpr(pc=98,ComputationalTypeInt,UVar(defSites={29},value=an int),+,UVar(defSites={30},value=int = 1))),
	32: ArrayStore(pc=101,UVar(defSites={28},value={int[], null}[↦90;refId=127]),UVar(defSites={31},value=an int),UVar(defSites={11},value=an int)),
	33: Assignment(pc=102,DVar(useSites={34},value=int = 0,origin=33),IntConst(pc=102,0)),
	34: ReturnValue(pc=103,UVar(defSites={33},value=int = 0)),
	35: PutField(pc=106,java.util.regex.Matcher,last,int,UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int)),
	36: Assignment(pc=109,DVar(useSites={37},value=int = 1,origin=36),IntConst(pc=109,1)),
	37: ReturnValue(pc=110,UVar(defSites={36},value=int = 1))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_f,BB_3}
	BB_1: BasicBlock(start=25,end=27) -> {BB_f,BB_a}
	BB_2: BasicBlock(start=20,end=21) -> {BB_f,BB_4}
	BB_3: BasicBlock(start=1,end=2) -> {BB_f,BB_c}
	BB_4: BasicBlock(start=22,end=22) -> {BB_8,BB_1}
	BB_5: BasicBlock(start=12,end=14) -> {BB_f,BB_9}
	BB_6: BasicBlock(start=7,end=11) -> {BB_f,BB_5}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=23,end=24) -> {BB_7}
	BB_9: BasicBlock(start=15,end=19) -> {BB_f,BB_2}
	BB_a: BasicBlock(start=28,end=32) -> {BB_f,BB_b}
	BB_b: BasicBlock(start=33,end=34) -> {BB_7}
	BB_c: BasicBlock(start=3,end=3) -> {BB_e,BB_d}
	BB_d: BasicBlock(start=35,end=37) -> {BB_7}
	BB_e: BasicBlock(start=4,end=6) -> {BB_f,BB_6}
	BB_f: ExitNode(normalReturn=false)
))

