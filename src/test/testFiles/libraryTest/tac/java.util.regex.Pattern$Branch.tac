boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={12,6,9,27} (origin=-1),
	1: useSites={0,32,16,8,40,36,20,2,18,26,38,14,30,1,33,29,35} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={24},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={25},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	2: Assignment(pc=11,DVar(useSites={37,21},value=int ∈ [0,1],origin=2),GetField(pc=11,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	3: Assignment(pc=16,DVar(useSites={24,17},value=int = 2147483647,origin=3),IntConst(pc=16,2147483647)),
	4: Assignment(pc=20,DVar(useSites={25,19},value=int = -1,origin=4),IntConst(pc=20,-1)),
	5: Assignment(pc=23,DVar(useSites={10,22,13,7},value=int = 0,origin=5),IntConst(pc=23,0)),
	6: Assignment(pc=29,DVar(useSites={7},value=an int,origin=6),GetField(pc=29,java.util.regex.Pattern$Branch,size,int,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	7: If(pc=32,UVar(defSites={22,5},value=an int),>=,UVar(defSites={6},value=an int),target=24),
	8: VirtualMethodCall(pc=36,java.util.regex.Pattern$TreeInfo,isInterface=false,void reset(),UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),()),
	9: Assignment(pc=40,DVar(useSites={10},value={_ <: java.util.regex.Pattern$Node[], null}[↦40;refId=511],origin=9),GetField(pc=40,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	10: Assignment(pc=45,DVar(useSites={11},value={_ <: java.util.regex.Pattern$Node, null}[↦45;refId=514],origin=10),ArrayLoad(pc=45,UVar(defSites={22,5},value=int ∈ [-2147483648,2147483646]),UVar(defSites={9},value={_ <: java.util.regex.Pattern$Node[], null}[↦40;refId=511]))),
	11: If(pc=46,UVar(defSites={10},value={_ <: java.util.regex.Pattern$Node, null}[↦45;refId=514]),==,NullExpr(pc=-333),target=16),
	12: Assignment(pc=50,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node[], null}[↦50;refId=515],origin=12),GetField(pc=50,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	13: Assignment(pc=55,DVar(useSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦55;refId=518],origin=13),ArrayLoad(pc=55,UVar(defSites={22,5},value=int ∈ [-2147483648,2147483646]),UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node[], null}[↦50;refId=515]))),
	14: ExprStmt(pc=57,VirtualFunctionCall(pc=57,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦55;refId=518]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	15: Nop(pc=60),
	16: Assignment(pc=64,DVar(useSites={17},value=an int,origin=16),GetField(pc=64,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	17: Assignment(pc=67,DVar(useSites={24,18},value=an int,origin=17),StaticFunctionCall(pc=67,java.lang.Math,isInterface=false,int min(int,int),(UVar(defSites={17,3},value=an int),UVar(defSites={16},value=an int)))),
	18: Assignment(pc=75,DVar(useSites={19},value=an int,origin=18),GetField(pc=75,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	19: Assignment(pc=78,DVar(useSites={20,25},value=an int,origin=19),StaticFunctionCall(pc=78,java.lang.Math,isInterface=false,int max(int,int),(UVar(defSites={4,19},value=an int),UVar(defSites={18},value=an int)))),
	20: Assignment(pc=86,DVar(useSites={21},value=int ∈ [0,1],origin=20),GetField(pc=86,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	21: Assignment(pc=89,DVar(useSites={22,37},value=int ∈ [0,1],origin=21),BinaryExpr(pc=89,ComputationalTypeInt,UVar(defSites={2,21},value=int ∈ [0,1]),&,UVar(defSites={20},value=int ∈ [0,1]))),
	22: Assignment(pc=92,DVar(useSites={10,13,7,23},value=an int,origin=22),BinaryExpr(pc=92,ComputationalTypeInt,UVar(defSites={22,5},value=an int),+,IntConst(pc=92,1))),
	23: Goto(pc=95,target=6),
	24: Assignment(pc=101,DVar(useSites={31},value=an int,origin=24),BinaryExpr(pc=101,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={17,3},value=an int))),
	25: Assignment(pc=106,DVar(useSites={34},value=an int,origin=25),BinaryExpr(pc=106,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={4,19},value=an int))),
	26: VirtualMethodCall(pc=109,java.util.regex.Pattern$TreeInfo,isInterface=false,void reset(),UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),()),
	27: Assignment(pc=113,DVar(useSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦113;refId=505],origin=27),GetField(pc=113,java.util.regex.Pattern$Branch,conn,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	28: Assignment(pc=116,DVar(useSites={29},value={_ <: java.util.regex.Pattern$Node, null}[↦116;refId=506],origin=28),GetField(pc=116,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦113;refId=505]))),
	29: ExprStmt(pc=120,VirtualFunctionCall(pc=120,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={28},value={_ <: java.util.regex.Pattern$Node, null}[↦116;refId=506]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	30: Assignment(pc=126,DVar(useSites={31},value=an int,origin=30),GetField(pc=126,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	31: Assignment(pc=130,DVar(useSites={32},value=an int,origin=31),BinaryExpr(pc=130,ComputationalTypeInt,UVar(defSites={30},value=an int),+,UVar(defSites={24},value=an int))),
	32: PutField(pc=131,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={31},value=an int)),
	33: Assignment(pc=136,DVar(useSites={34},value=an int,origin=33),GetField(pc=136,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	34: Assignment(pc=140,DVar(useSites={35},value=an int,origin=34),BinaryExpr(pc=140,ComputationalTypeInt,UVar(defSites={33},value=an int),+,UVar(defSites={25},value=an int))),
	35: PutField(pc=141,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={34},value=an int)),
	36: Assignment(pc=146,DVar(useSites={37},value=int ∈ [0,1],origin=36),GetField(pc=146,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	37: Assignment(pc=151,DVar(useSites={38},value=int ∈ [0,1],origin=37),BinaryExpr(pc=151,ComputationalTypeInt,UVar(defSites={36},value=int ∈ [0,1]),&,UVar(defSites={2,21},value=int ∈ [0,1]))),
	38: PutField(pc=152,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={37},value=int ∈ [0,1])),
	39: Assignment(pc=156,DVar(useSites={40},value=int = 0,origin=39),IntConst(pc=156,0)),
	40: PutField(pc=157,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={39},value=int = 0)),
	41: Assignment(pc=160,DVar(useSites={42},value=int = 0,origin=41),IntConst(pc=160,0)),
	42: ReturnValue(pc=161,UVar(defSites={41},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_c,BB_3}
	BB_10: BasicBlock(start=18,end=19) -> {BB_c,BB_e}
	BB_11: ExitNode(normalReturn=true)
	BB_1: BasicBlock(start=24,end=26) -> {BB_c,BB_6}
	BB_2: BasicBlock(start=14,end=14) -> {BB_c,BB_d}
	BB_3: BasicBlock(start=1,end=5) -> {BB_4}
	BB_4: BasicBlock(start=6,end=7) -> {BB_1,BB_a}
	BB_5: BasicBlock(start=9,end=10) -> {BB_c,BB_9}
	BB_6: BasicBlock(start=27,end=28) -> {BB_c,BB_f}
	BB_7: BasicBlock(start=12,end=13) -> {BB_c,BB_2}
	BB_8: BasicBlock(start=16,end=17) -> {BB_c,BB_10}
	BB_9: BasicBlock(start=11,end=11) -> {BB_7,BB_8}
	BB_a: BasicBlock(start=8,end=8) -> {BB_c,BB_5}
	BB_b: BasicBlock(start=30,end=42) -> {BB_11}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=15) -> {BB_8}
	BB_e: BasicBlock(start=20,end=23) -> {BB_4}
	BB_f: BasicBlock(start=29,end=29) -> {BB_c,BB_b}
))

void add(java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,16,4,20,12,1,17,9,15} (origin=-1),
	1: useSites={21} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={3},value=an int,origin=0),GetField(pc=1,java.util.regex.Pattern$Branch,size,int,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value={_ <: java.util.regex.Pattern$Node[], null}[↦5;refId=104],origin=1),GetField(pc=5,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=8,UVar(defSites={1},value={_ <: java.util.regex.Pattern$Node[], null}[↦5;refId=104]))),
	3: If(pc=9,UVar(defSites={0},value=an int),<,UVar(defSites={2},value=int ∈ [0,2147483647]),target=16),
	4: Assignment(pc=13,DVar(useSites={5},value={_ <: java.util.regex.Pattern$Node[], null}[↦13;refId=106],origin=4),GetField(pc=13,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	5: Assignment(pc=16,DVar(useSites={7},value=int ∈ [0,2147483647],origin=5),ArrayLength(pc=16,UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node[], null}[↦13;refId=106]))),
	6: Assignment(pc=17,DVar(useSites={7},value=int = 2,origin=6),IntConst(pc=17,2)),
	7: Assignment(pc=18,DVar(useSites={8},value=an int,origin=7),BinaryExpr(pc=18,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,2147483647]),*,UVar(defSites={6},value=int = 2))),
	8: Assignment(pc=19,DVar(useSites={14,15},value=java.util.regex.Pattern$Node[][↦19;refId=108],origin=8),NewArray(pc=19,[UVar(defSites={7},value=an int)],java.util.regex.Pattern$Node[])),
	9: Assignment(pc=24,DVar(useSites={14},value={_ <: java.util.regex.Pattern$Node[], null}[↦24;refId=110],origin=9),GetField(pc=24,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	10: Assignment(pc=27,DVar(useSites={14},value=int = 0,origin=10),IntConst(pc=27,0)),
	11: Assignment(pc=29,DVar(useSites={14},value=int = 0,origin=11),IntConst(pc=29,0)),
	12: Assignment(pc=31,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node[], null}[↦31;refId=111],origin=12),GetField(pc=31,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	13: Assignment(pc=34,DVar(useSites={14},value=int ∈ [0,2147483647],origin=13),ArrayLength(pc=34,UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node[], null}[↦31;refId=111]))),
	14: StaticMethodCall(pc=35,java.lang.System,isInterface=false,void arraycopy(java.lang.Object,int,java.lang.Object,int,int),(UVar(defSites={9},value={_ <: java.util.regex.Pattern$Node[], null}[↦24;refId=110]),UVar(defSites={10},value=int = 0),UVar(defSites={8},value=java.util.regex.Pattern$Node[][↦19;refId=108]),UVar(defSites={11},value=int = 0),UVar(defSites={13},value=int ∈ [0,2147483647]))),
	15: PutField(pc=40,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]),UVar(defSites={8},value=java.util.regex.Pattern$Node[][↦19;refId=108])),
	16: Assignment(pc=44,DVar(useSites={21},value={_ <: java.util.regex.Pattern$Node[], null}[↦44;refId=116],origin=16),GetField(pc=44,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	17: Assignment(pc=49,DVar(useSites={21,19},value=an int,origin=17),GetField(pc=49,java.util.regex.Pattern$Branch,size,int,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	18: Assignment(pc=53,DVar(useSites={19},value=int = 1,origin=18),IntConst(pc=53,1)),
	19: Assignment(pc=54,DVar(useSites={20},value=an int,origin=19),BinaryExpr(pc=54,ComputationalTypeInt,UVar(defSites={17},value=an int),+,UVar(defSites={18},value=int = 1))),
	20: PutField(pc=55,java.util.regex.Pattern$Branch,size,int,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]),UVar(defSites={19},value=an int)),
	21: ArrayStore(pc=59,UVar(defSites={16},value={_ <: java.util.regex.Pattern$Node[], null}[↦44;refId=116]),UVar(defSites={17},value=an int),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	22: Return(pc=60)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_a,BB_5}
	BB_1: BasicBlock(start=14,end=14) -> {BB_a,BB_8}
	BB_2: BasicBlock(start=6,end=8) -> {BB_a,BB_3}
	BB_3: BasicBlock(start=9,end=13) -> {BB_a,BB_1}
	BB_4: BasicBlock(start=22,end=22) -> {BB_6}
	BB_5: BasicBlock(start=3,end=3) -> {BB_9,BB_7}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=16,end=21) -> {BB_a,BB_4}
	BB_8: BasicBlock(start=15,end=15) -> {BB_7}
	BB_9: BasicBlock(start=4,end=5) -> {BB_a,BB_2}
	BB_a: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={12,6,1,3} (origin=-1),
	1: useSites={8,14} (origin=-2),
	2: useSites={8,14} (origin=-3),
	3: useSites={8,14} (origin=-4)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={4,2,18,13},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$Branch,size,int,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	2: If(pc=9,UVar(defSites={0,18},value=an int),>=,UVar(defSites={1},value=an int),target=20),
	3: Assignment(pc=13,DVar(useSites={4},value={_ <: java.util.regex.Pattern$Node[], null}[↦13;refId=420],origin=3),GetField(pc=13,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	4: Assignment(pc=18,DVar(useSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦18;refId=423],origin=4),ArrayLoad(pc=18,UVar(defSites={0,18},value=int ∈ [-2147483648,2147483646]),UVar(defSites={3},value={_ <: java.util.regex.Pattern$Node[], null}[↦13;refId=420]))),
	5: If(pc=19,UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦18;refId=423]),!=,NullExpr(pc=-333),target=12),
	6: Assignment(pc=23,DVar(useSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦23;refId=424],origin=6),GetField(pc=23,java.util.regex.Pattern$Branch,conn,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	7: Assignment(pc=26,DVar(useSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦26;refId=425],origin=7),GetField(pc=26,java.util.regex.Pattern$Node,next,java.util.regex.Pattern$Node,UVar(defSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦23;refId=424]))),
	8: Assignment(pc=32,DVar(useSites={9},value=int ∈ [0,1],origin=8),VirtualFunctionCall(pc=32,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦26;refId=425]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	9: If(pc=35,UVar(defSites={8},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=18),
	10: Assignment(pc=38,DVar(useSites={11},value=int = 1,origin=10),IntConst(pc=38,1)),
	11: ReturnValue(pc=39,UVar(defSites={10},value=int = 1)),
	12: Assignment(pc=41,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node[], null}[↦41;refId=429],origin=12),GetField(pc=41,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	13: Assignment(pc=46,DVar(useSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦46;refId=432],origin=13),ArrayLoad(pc=46,UVar(defSites={0,18},value=int ∈ [-2147483648,2147483646]),UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node[], null}[↦41;refId=429]))),
	14: Assignment(pc=50,DVar(useSites={15},value=int ∈ [0,1],origin=14),VirtualFunctionCall(pc=50,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦46;refId=432]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	15: If(pc=53,UVar(defSites={14},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=18),
	16: Assignment(pc=56,DVar(useSites={17},value=int = 1,origin=16),IntConst(pc=56,1)),
	17: ReturnValue(pc=57,UVar(defSites={16},value=int = 1)),
	18: Assignment(pc=58,DVar(useSites={4,2,13,19},value=an int,origin=18),BinaryExpr(pc=58,ComputationalTypeInt,UVar(defSites={0,18},value=an int),+,IntConst(pc=58,1))),
	19: Goto(pc=61,target=1),
	20: Assignment(pc=64,DVar(useSites={21},value=int = 0,origin=20),IntConst(pc=64,0)),
	21: ReturnValue(pc=65,UVar(defSites={20},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_5}
	BB_1: BasicBlock(start=5,end=5) -> {BB_8,BB_6}
	BB_2: BasicBlock(start=10,end=11) -> {BB_f}
	BB_3: BasicBlock(start=14,end=14) -> {BB_c,BB_d}
	BB_4: BasicBlock(start=20,end=21) -> {BB_f}
	BB_5: BasicBlock(start=1,end=2) -> {BB_4,BB_9}
	BB_6: BasicBlock(start=6,end=7) -> {BB_c,BB_b}
	BB_7: BasicBlock(start=9,end=9) -> {BB_e,BB_2}
	BB_8: BasicBlock(start=12,end=13) -> {BB_c,BB_3}
	BB_9: BasicBlock(start=3,end=4) -> {BB_c,BB_1}
	BB_a: BasicBlock(start=16,end=17) -> {BB_f}
	BB_b: BasicBlock(start=8,end=8) -> {BB_c,BB_7}
	BB_c: ExitNode(normalReturn=false)
	BB_d: BasicBlock(start=15,end=15) -> {BB_a,BB_e}
	BB_e: BasicBlock(start=18,end=19) -> {BB_5}
	BB_f: ExitNode(normalReturn=true)
))

void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Node,java.util.regex.Pattern$Node)
AITACode(params=(Parameters(
	0: useSites={0,10,6,5,3,7} (origin=-1),
	1: useSites={9} (origin=-2),
	2: useSites={12} (origin=-3),
	3: useSites={6} (origin=-4)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 2,origin=1),IntConst(pc=5,2)),
	2: Assignment(pc=6,DVar(useSites={3},value=java.util.regex.Pattern$Node[][↦6;refId=107;length=2],origin=2),NewArray(pc=6,[UVar(defSites={1},value=int = 2)],java.util.regex.Pattern$Node[])),
	3: PutField(pc=9,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]),UVar(defSites={2},value=java.util.regex.Pattern$Node[][↦6;refId=107;length=2])),
	4: Assignment(pc=13,DVar(useSites={5},value=int = 2,origin=4),IntConst(pc=13,2)),
	5: PutField(pc=14,java.util.regex.Pattern$Branch,size,int,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]),UVar(defSites={4},value=int = 2)),
	6: PutField(pc=19,java.util.regex.Pattern$Branch,conn,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]),UVar(defSites={-4},value={_ <: java.util.regex.Pattern$Node, null}[↦-4;refId=105])),
	7: Assignment(pc=23,DVar(useSites={9},value={_ <: java.util.regex.Pattern$Node[], null}[↦23;refId=108],origin=7),GetField(pc=23,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	8: Assignment(pc=26,DVar(useSites={9},value=int = 0,origin=8),IntConst(pc=26,0)),
	9: ArrayStore(pc=28,UVar(defSites={7},value={_ <: java.util.regex.Pattern$Node[], null}[↦23;refId=108]),UVar(defSites={8},value=int = 0),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	10: Assignment(pc=30,DVar(useSites={12},value={_ <: java.util.regex.Pattern$Node[], null}[↦30;refId=112],origin=10),GetField(pc=30,java.util.regex.Pattern$Branch,atoms,java.util.regex.Pattern$Node[],UVar(defSites={-1},value=java.util.regex.Pattern$Branch[↦-1;refId=102]))),
	11: Assignment(pc=33,DVar(useSites={12},value=int = 1,origin=11),IntConst(pc=33,1)),
	12: ArrayStore(pc=35,UVar(defSites={10},value={_ <: java.util.regex.Pattern$Node[], null}[↦30;refId=112]),UVar(defSites={11},value=int = 1),UVar(defSites={-3},value={_ <: java.util.regex.Pattern$Node, null}[↦-3;refId=104])),
	13: Return(pc=36)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_5,BB_2}
	BB_1: BasicBlock(start=10,end=12) -> {BB_5,BB_3}
	BB_2: BasicBlock(start=1,end=9) -> {BB_5,BB_1}
	BB_3: BasicBlock(start=13,end=13) -> {BB_4}
	BB_4: ExitNode(normalReturn=true)
	BB_5: ExitNode(normalReturn=false)
))

