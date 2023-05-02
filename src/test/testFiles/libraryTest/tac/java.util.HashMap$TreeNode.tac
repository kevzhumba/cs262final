void moveRootToFront(java.util.HashMap$Node[],java.util.HashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={8,2,1,11} (origin=-2),
	2: useSites={0,20,12,10,26,6,21,13,11,23} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-3},value={java.util.HashMap$TreeNode, null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=31),
	1: If(pc=5,UVar(defSites={-2},value={_ <: java.util.HashMap$Node[], null}[↦-1;refId=102]),==,NullExpr(pc=-333),target=31),
	2: Assignment(pc=9,DVar(useSites={5,3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=9,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[][↦-1;refId=102]))),
	3: If(pc=12,UVar(defSites={2},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=31),
	4: Assignment(pc=16,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=16,1)),
	5: Assignment(pc=17,DVar(useSites={7},value=int ∈ [0,2147483646],origin=5),BinaryExpr(pc=17,ComputationalTypeInt,UVar(defSites={2},value=int ∈ [1,2147483647]),-,UVar(defSites={4},value=int = 1))),
	6: Assignment(pc=19,DVar(useSites={7},value=an int,origin=6),GetField(pc=19,java.util.HashMap$TreeNode,hash,int,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]))),
	7: Assignment(pc=22,DVar(useSites={8,11},value=int ∈ [0,2147483646],origin=7),BinaryExpr(pc=22,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,2147483646]),&,UVar(defSites={6},value=an int))),
	8: Assignment(pc=26,DVar(useSites={20,10,9,21,19},value={_ <: java.util.HashMap$Node, null}[↦26;refId=105],origin=8),ArrayLoad(pc=26,UVar(defSites={7},value=int ∈ [0,2147483646]),UVar(defSites={-2},value=_ <: java.util.HashMap$Node[][↦-1;refId=102]))),
	9: Checkcast(pc=27,UVar(defSites={8},value={_ <: java.util.HashMap$Node, null}[↦26;refId=105]),java.util.HashMap$TreeNode),
	10: If(pc=35,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),==,UVar(defSites={8},value={java.util.HashMap$TreeNode, null}[↦26;refId=106]),target=24),
	11: ArrayStore(pc=41,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[][↦-1;refId=102]),UVar(defSites={7},value=int ∈ [0,2147483646]),UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103])),
	12: Assignment(pc=43,DVar(useSites={16,18,17},value={java.util.HashMap$TreeNode, null}[↦43;refId=109],origin=12),GetField(pc=43,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]))),
	13: Assignment(pc=49,DVar(useSites={16,18,14,15},value={_ <: java.util.HashMap$Node, null}[↦49;refId=110],origin=13),GetField(pc=49,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]))),
	14: If(pc=55,UVar(defSites={13},value={_ <: java.util.HashMap$Node, null}[↦49;refId=110]),==,NullExpr(pc=-333),target=17),
	15: Checkcast(pc=60,UVar(defSites={13},value=_ <: java.util.HashMap$Node[↦49;refId=110]),java.util.HashMap$TreeNode),
	16: PutField(pc=65,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={13},value=java.util.HashMap$TreeNode[↦49;refId=111]),UVar(defSites={12},value={java.util.HashMap$TreeNode, null}[↦43;refId=109])),
	17: If(pc=70,UVar(defSites={12},value={java.util.HashMap$TreeNode, null}[↦43;refId=109]),==,NullExpr(pc=-333),target=19),
	18: PutField(pc=77,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={12},value=java.util.HashMap$TreeNode[↦43;refId=109]),UVar(defSites={13},value={java.util.HashMap$TreeNode, null}[↦49;refId=111])),
	19: If(pc=82,UVar(defSites={8},value={java.util.HashMap$TreeNode, null}[↦26;refId=106]),==,NullExpr(pc=-333),target=21),
	20: PutField(pc=88,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={8},value=java.util.HashMap$TreeNode[↦26;refId=106]),UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103])),
	21: PutField(pc=94,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),UVar(defSites={8},value={java.util.HashMap$TreeNode, null}[↦26;refId=106])),
	22: Assignment(pc=98,DVar(useSites={23},value=null[↦98],origin=22),NullExpr(pc=98)),
	23: PutField(pc=99,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),UVar(defSites={22},value=null[↦98])),
	24: Assignment(pc=102,DVar(useSites={25},value=int ∈ [0,1],origin=24),GetStatic(pc=102,java.util.HashMap$TreeNode,$assertionsDisabled,boolean)),
	25: If(pc=105,UVar(defSites={24},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=31),
	26: Assignment(pc=109,DVar(useSites={27},value=int ∈ [0,1],origin=26),StaticFunctionCall(pc=109,java.util.HashMap$TreeNode,isInterface=false,boolean checkInvariants(java.util.HashMap$TreeNode),(UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103])))),
	27: If(pc=112,UVar(defSites={26},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=31),
	28: Assignment(pc=115,DVar(useSites={30,29},value=java.lang.AssertionError[↦115;refId=114],origin=28),New(pc=115,java.lang.AssertionError)),
	29: NonVirtualMethodCall(pc=119,java.lang.AssertionError,isInterface=false,void <init>(),UVar(defSites={28},value=java.lang.AssertionError[↦115;refId=114]),()),
	30: Throw(pc=122,UVar(defSites={28},value=java.lang.AssertionError[↦115;refId=114])),
	31: Return(pc=123)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_12}
	BB_10: ExitNode(normalReturn=true)
	BB_11: BasicBlock(start=16,end=16) -> {BB_7}
	BB_12: BasicBlock(start=31,end=31) -> {BB_10}
	BB_13: BasicBlock(start=30,end=30) -> {BB_16}
	BB_14: BasicBlock(start=19,end=19) -> {BB_3,BB_e}
	BB_15: BasicBlock(start=4,end=8) -> {BB_16,BB_5}
	BB_16: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=10,end=10) -> {BB_a,BB_2}
	BB_2: BasicBlock(start=24,end=25) -> {BB_b,BB_12}
	BB_3: BasicBlock(start=20,end=20) -> {BB_e}
	BB_4: BasicBlock(start=1,end=1) -> {BB_6,BB_12}
	BB_5: BasicBlock(start=9,end=9) -> {BB_16,BB_1}
	BB_6: BasicBlock(start=2,end=3) -> {BB_12,BB_15}
	BB_7: BasicBlock(start=17,end=17) -> {BB_14,BB_f}
	BB_8: BasicBlock(start=27,end=27) -> {BB_d,BB_12}
	BB_9: BasicBlock(start=12,end=14) -> {BB_7,BB_c}
	BB_a: BasicBlock(start=11,end=11) -> {BB_16,BB_9}
	BB_b: BasicBlock(start=26,end=26) -> {BB_16,BB_8}
	BB_c: BasicBlock(start=15,end=15) -> {BB_16,BB_11}
	BB_d: BasicBlock(start=28,end=29) -> {BB_16,BB_13}
	BB_e: BasicBlock(start=21,end=23) -> {BB_2}
	BB_f: BasicBlock(start=18,end=18) -> {BB_14}
))

java.util.HashMap$TreeNode balanceInsertion(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={40,54,67,11,27} (origin=-2),
	2: useSites={2,26,6,1,5,53} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 1,origin=0),IntConst(pc=1,1)),
	1: PutField(pc=2,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={-3},value={java.util.HashMap$TreeNode, null}[↦-2;refId=103]),UVar(defSites={0},value=int = 1)),
	2: Assignment(pc=6,DVar(useSites={48,36,52,28,34,26,6,54,9,25,5,21,53,13,61,3,27,7,55,63},value={java.util.HashMap$TreeNode, null}[↦6;refId=200],origin=2),GetField(pc=6,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={2,9,-3},value=java.util.HashMap$TreeNode[refId=171; values=«java.util.HashMap$TreeNode[↦-2;refId=103], java.util.HashMap$TreeNode[↦29;refId=106], java.util.HashMap$TreeNode[↦6;refId=116]»]))),
	3: If(pc=11,UVar(defSites={2},value={java.util.HashMap$TreeNode, null}[↦6;refId=200]),!=,NullExpr(pc=-333),target=7),
	4: Assignment(pc=15,DVar(useSites={5},value=int = 0,origin=4),IntConst(pc=15,0)),
	5: PutField(pc=16,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={2,9,-3},value=java.util.HashMap$TreeNode[refId=171; values=«java.util.HashMap$TreeNode[↦-2;refId=103], java.util.HashMap$TreeNode[↦29;refId=106], java.util.HashMap$TreeNode[↦6;refId=116]»]),UVar(defSites={4},value=int = 0)),
	6: ReturnValue(pc=20,UVar(defSites={2,9,-3},value=java.util.HashMap$TreeNode[refId=171; values=«java.util.HashMap$TreeNode[↦-2;refId=103], java.util.HashMap$TreeNode[↦29;refId=106], java.util.HashMap$TreeNode[↦6;refId=116]»])),
	7: Assignment(pc=22,DVar(useSites={8},value=int ∈ [0,1],origin=7),GetField(pc=22,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]))),
	8: If(pc=25,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	9: Assignment(pc=29,DVar(useSites={64,40,12,2,66,50,10,26,6,14,5,37,53,67,39,23},value={java.util.HashMap$TreeNode, null}[↦29;refId=202],origin=9),GetField(pc=29,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]))),
	10: If(pc=34,UVar(defSites={9},value={java.util.HashMap$TreeNode, null}[↦29;refId=202]),!=,NullExpr(pc=-333),target=12),
	11: ReturnValue(pc=38,UVar(defSites={40,54,-2,67,27},value={java.util.HashMap$TreeNode, null}[refId=201; values=«{java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦238;refId=167], {java.util.HashMap$TreeNode, null}[↦196;refId=112], {java.util.HashMap$TreeNode, null}[↦143;refId=177], {java.util.HashMap$TreeNode, null}[↦101;refId=123]»])),
	12: Assignment(pc=41,DVar(useSites={42,46,13,43},value={java.util.HashMap$TreeNode, null}[↦41;refId=204],origin=12),GetField(pc=41,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={9},value=java.util.HashMap$TreeNode[↦29;refId=202]))),
	13: If(pc=47,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]),!=,UVar(defSites={12},value={java.util.HashMap$TreeNode, null}[↦41;refId=204]),target=42),
	14: Assignment(pc=51,DVar(useSites={16,19,15},value={java.util.HashMap$TreeNode, null}[↦51;refId=210],origin=14),GetField(pc=51,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={9},value=java.util.HashMap$TreeNode[↦29;refId=202]))),
	15: If(pc=57,UVar(defSites={14},value={java.util.HashMap$TreeNode, null}[↦51;refId=210]),==,NullExpr(pc=-333),target=25),
	16: Assignment(pc=62,DVar(useSites={17},value=int ∈ [0,1],origin=16),GetField(pc=62,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={14},value=java.util.HashMap$TreeNode[↦51;refId=210]))),
	17: If(pc=65,UVar(defSites={16},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=25),
	18: Assignment(pc=70,DVar(useSites={19},value=int = 0,origin=18),IntConst(pc=70,0)),
	19: PutField(pc=71,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={14},value=java.util.HashMap$TreeNode[↦51;refId=210]),UVar(defSites={18},value=int = 0)),
	20: Assignment(pc=75,DVar(useSites={21},value=int = 0,origin=20),IntConst(pc=75,0)),
	21: PutField(pc=76,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]),UVar(defSites={20},value=int = 0)),
	22: Assignment(pc=80,DVar(useSites={23},value=int = 1,origin=22),IntConst(pc=80,1)),
	23: PutField(pc=81,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={9},value=java.util.HashMap$TreeNode[↦29;refId=202]),UVar(defSites={22},value=int = 1)),
	24: Goto(pc=86,target=2),
	25: Assignment(pc=91,DVar(useSites={26},value={java.util.HashMap$TreeNode, null}[↦91;refId=245],origin=25),GetField(pc=91,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]))),
	26: If(pc=94,UVar(defSites={2,9,-3},value=java.util.HashMap$TreeNode[refId=212; values=«java.util.HashMap$TreeNode[↦-2;refId=103], java.util.HashMap$TreeNode[↦29;refId=106], java.util.HashMap$TreeNode[↦6;refId=116]»]),!=,UVar(defSites={25},value={java.util.HashMap$TreeNode, null}[↦91;refId=245]),target=34),
	27: Assignment(pc=101,DVar(useSites={40,28,54,67,11},value={java.util.HashMap$TreeNode, null}[↦101;refId=251],origin=27),StaticFunctionCall(pc=101,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateLeft(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.HashMap$TreeNode, null}[refId=211; values=«{java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦238;refId=167], {java.util.HashMap$TreeNode, null}[↦196;refId=112], {java.util.HashMap$TreeNode, null}[↦143;refId=177], {java.util.HashMap$TreeNode, null}[↦101;refId=123]»]),UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200])))),
	28: Assignment(pc=106,DVar(useSites={32,36,34,29},value={java.util.HashMap$TreeNode, null}[↦106;refId=252],origin=28),GetField(pc=106,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]))),
	29: If(pc=111,UVar(defSites={28},value={java.util.HashMap$TreeNode, null}[↦106;refId=252]),!=,NullExpr(pc=-333),target=32),
	30: Assignment(pc=114,DVar(useSites={40,37,39},value=null[↦114],origin=30),NullExpr(pc=114)),
	31: Goto(pc=115,target=33),
	32: Assignment(pc=119,DVar(useSites={40,37,39},value={java.util.HashMap$TreeNode, null}[refId=254; values=«null[↦114], {java.util.HashMap$TreeNode, null}[↦119;refId=253]»],origin=32),GetField(pc=119,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={28},value=java.util.HashMap$TreeNode[↦106;refId=252]))),
	33: Nop(pc=122),
	34: If(pc=124,UVar(defSites={28,2},value={java.util.HashMap$TreeNode, null}[refId=248; values=«{java.util.HashMap$TreeNode, null}[↦106;refId=124], java.util.HashMap$TreeNode[↦6;refId=200]»]),==,NullExpr(pc=-333),target=2),
	35: Assignment(pc=128,DVar(useSites={36},value=int = 0,origin=35),IntConst(pc=128,0)),
	36: PutField(pc=129,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={28,2},value=java.util.HashMap$TreeNode[refId=248; values=«{java.util.HashMap$TreeNode, null}[↦106;refId=124], java.util.HashMap$TreeNode[↦6;refId=200]»]),UVar(defSites={35},value=int = 0)),
	37: If(pc=133,UVar(defSites={32,30,9},value={java.util.HashMap$TreeNode, null}[refId=249; values=«null[↦114], {java.util.HashMap$TreeNode, null}[↦119;refId=125], java.util.HashMap$TreeNode[↦29;refId=202]»]),==,NullExpr(pc=-333),target=2),
	38: Assignment(pc=137,DVar(useSites={39},value=int = 1,origin=38),IntConst(pc=137,1)),
	39: PutField(pc=138,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={32,30,9},value=java.util.HashMap$TreeNode[refId=268; values=«{java.util.HashMap$TreeNode, null}[↦119;refId=125], java.util.HashMap$TreeNode[↦29;refId=202]»]),UVar(defSites={38},value=int = 1)),
	40: Assignment(pc=143,DVar(useSites={54,41,67,11,27},value={java.util.HashMap$TreeNode, null}[↦143;refId=272],origin=40),StaticFunctionCall(pc=143,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateRight(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.HashMap$TreeNode, null}[refId=246; values=«{java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦238;refId=167], {java.util.HashMap$TreeNode, null}[↦196;refId=112], {java.util.HashMap$TreeNode, null}[↦101;refId=123], {java.util.HashMap$TreeNode, null}[↦143;refId=177]»]),UVar(defSites={32,30,9},value=java.util.HashMap$TreeNode[refId=268; values=«{java.util.HashMap$TreeNode, null}[↦119;refId=125], java.util.HashMap$TreeNode[↦29;refId=202]»])))),
	41: Goto(pc=147,target=2),
	42: If(pc=152,UVar(defSites={12},value={java.util.HashMap$TreeNode, null}[↦41;refId=204]),==,NullExpr(pc=-333),target=52),
	43: Assignment(pc=157,DVar(useSites={44},value=int ∈ [0,1],origin=43),GetField(pc=157,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={12},value=java.util.HashMap$TreeNode[↦41;refId=204]))),
	44: If(pc=160,UVar(defSites={43},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=52),
	45: Assignment(pc=165,DVar(useSites={46},value=int = 0,origin=45),IntConst(pc=165,0)),
	46: PutField(pc=166,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={12},value=java.util.HashMap$TreeNode[↦41;refId=204]),UVar(defSites={45},value=int = 0)),
	47: Assignment(pc=170,DVar(useSites={48},value=int = 0,origin=47),IntConst(pc=170,0)),
	48: PutField(pc=171,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]),UVar(defSites={47},value=int = 0)),
	49: Assignment(pc=175,DVar(useSites={50},value=int = 1,origin=49),IntConst(pc=175,1)),
	50: PutField(pc=176,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={9},value=java.util.HashMap$TreeNode[↦29;refId=202]),UVar(defSites={49},value=int = 1)),
	51: Goto(pc=181,target=2),
	52: Assignment(pc=186,DVar(useSites={53},value={java.util.HashMap$TreeNode, null}[↦186;refId=235],origin=52),GetField(pc=186,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]))),
	53: If(pc=189,UVar(defSites={2,9,-3},value=java.util.HashMap$TreeNode[refId=206; values=«java.util.HashMap$TreeNode[↦-2;refId=103], java.util.HashMap$TreeNode[↦29;refId=106], java.util.HashMap$TreeNode[↦6;refId=116]»]),!=,UVar(defSites={52},value={java.util.HashMap$TreeNode, null}[↦186;refId=235]),target=61),
	54: Assignment(pc=196,DVar(useSites={40,67,11,27,55},value={java.util.HashMap$TreeNode, null}[↦196;refId=241],origin=54),StaticFunctionCall(pc=196,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateRight(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.HashMap$TreeNode, null}[refId=205; values=«{java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦238;refId=167], {java.util.HashMap$TreeNode, null}[↦196;refId=112], {java.util.HashMap$TreeNode, null}[↦143;refId=177], {java.util.HashMap$TreeNode, null}[↦101;refId=123]»]),UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200])))),
	55: Assignment(pc=201,DVar(useSites={56,61,59,63},value={java.util.HashMap$TreeNode, null}[↦201;refId=242],origin=55),GetField(pc=201,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦6;refId=200]))),
	56: If(pc=206,UVar(defSites={55},value={java.util.HashMap$TreeNode, null}[↦201;refId=242]),!=,NullExpr(pc=-333),target=59),
	57: Assignment(pc=209,DVar(useSites={64,66,67},value=null[↦209],origin=57),NullExpr(pc=209)),
	58: Goto(pc=210,target=60),
	59: Assignment(pc=214,DVar(useSites={64,66,67},value={java.util.HashMap$TreeNode, null}[refId=244; values=«null[↦209], {java.util.HashMap$TreeNode, null}[↦214;refId=243]»],origin=59),GetField(pc=214,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={55},value=java.util.HashMap$TreeNode[↦201;refId=242]))),
	60: Nop(pc=217),
	61: If(pc=219,UVar(defSites={2,55},value={java.util.HashMap$TreeNode, null}[refId=238; values=«{java.util.HashMap$TreeNode, null}[↦201;refId=113], java.util.HashMap$TreeNode[↦6;refId=200]»]),==,NullExpr(pc=-333),target=2),
	62: Assignment(pc=223,DVar(useSites={63},value=int = 0,origin=62),IntConst(pc=223,0)),
	63: PutField(pc=224,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={2,55},value=java.util.HashMap$TreeNode[refId=238; values=«{java.util.HashMap$TreeNode, null}[↦201;refId=113], java.util.HashMap$TreeNode[↦6;refId=200]»]),UVar(defSites={62},value=int = 0)),
	64: If(pc=228,UVar(defSites={9,57,59},value={java.util.HashMap$TreeNode, null}[refId=239; values=«null[↦209], {java.util.HashMap$TreeNode, null}[↦214;refId=114], java.util.HashMap$TreeNode[↦29;refId=202]»]),==,NullExpr(pc=-333),target=2),
	65: Assignment(pc=232,DVar(useSites={66},value=int = 1,origin=65),IntConst(pc=232,1)),
	66: PutField(pc=233,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={9,57,59},value=java.util.HashMap$TreeNode[refId=258; values=«{java.util.HashMap$TreeNode, null}[↦214;refId=114], java.util.HashMap$TreeNode[↦29;refId=202]»]),UVar(defSites={65},value=int = 1)),
	67: Assignment(pc=238,DVar(useSites={40,68,54,11,27},value={java.util.HashMap$TreeNode, null}[↦238;refId=262],origin=67),StaticFunctionCall(pc=238,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateLeft(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.HashMap$TreeNode, null}[refId=236; values=«{java.util.HashMap$TreeNode, null}[↦238;refId=167], {java.util.HashMap$TreeNode, null}[↦196;refId=112], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦101;refId=123], {java.util.HashMap$TreeNode, null}[↦143;refId=177]»]),UVar(defSites={9,57,59},value=java.util.HashMap$TreeNode[refId=258; values=«{java.util.HashMap$TreeNode, null}[↦214;refId=114], java.util.HashMap$TreeNode[↦29;refId=202]»])))),
	68: Goto(pc=242,target=2)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_20,BB_7}
	BB_10: BasicBlock(start=14,end=15) -> {BB_a,BB_e}
	BB_11: BasicBlock(start=33,end=33) -> {BB_16}
	BB_12: BasicBlock(start=28,end=29) -> {BB_c,BB_15}
	BB_13: BasicBlock(start=38,end=40) -> {BB_20,BB_6}
	BB_14: BasicBlock(start=45,end=51) -> {BB_7}
	BB_15: BasicBlock(start=32,end=32) -> {BB_11}
	BB_16: BasicBlock(start=34,end=34) -> {BB_7,BB_9}
	BB_17: BasicBlock(start=59,end=59) -> {BB_3}
	BB_18: BasicBlock(start=27,end=27) -> {BB_20,BB_12}
	BB_19: BasicBlock(start=12,end=13) -> {BB_10,BB_d}
	BB_1: BasicBlock(start=57,end=58) -> {BB_3}
	BB_1a: BasicBlock(start=54,end=54) -> {BB_20,BB_b}
	BB_1b: BasicBlock(start=18,end=24) -> {BB_7}
	BB_1c: ExitNode(normalReturn=true)
	BB_1d: BasicBlock(start=11,end=11) -> {BB_1c}
	BB_1e: BasicBlock(start=43,end=44) -> {BB_f,BB_14}
	BB_1f: BasicBlock(start=4,end=6) -> {BB_1c}
	BB_20: ExitNode(normalReturn=false)
	BB_21: BasicBlock(start=68,end=68) -> {BB_7}
	BB_22: BasicBlock(start=62,end=64) -> {BB_7,BB_4}
	BB_2: BasicBlock(start=61,end=61) -> {BB_22,BB_7}
	BB_3: BasicBlock(start=60,end=60) -> {BB_2}
	BB_4: BasicBlock(start=65,end=67) -> {BB_20,BB_21}
	BB_5: BasicBlock(start=9,end=10) -> {BB_1d,BB_19}
	BB_6: BasicBlock(start=41,end=41) -> {BB_7}
	BB_7: BasicBlock(start=2,end=3) -> {BB_1f,BB_8}
	BB_8: BasicBlock(start=7,end=8) -> {BB_5,BB_1d}
	BB_9: BasicBlock(start=35,end=37) -> {BB_13,BB_7}
	BB_a: BasicBlock(start=16,end=17) -> {BB_1b,BB_e}
	BB_b: BasicBlock(start=55,end=56) -> {BB_1,BB_17}
	BB_c: BasicBlock(start=30,end=31) -> {BB_11}
	BB_d: BasicBlock(start=42,end=42) -> {BB_f,BB_1e}
	BB_e: BasicBlock(start=25,end=26) -> {BB_18,BB_16}
	BB_f: BasicBlock(start=52,end=53) -> {BB_1a,BB_2}
))

java.util.HashMap$TreeNode root()
AITACode(params=(Parameters(
	0: useSites={1,3} (origin=-1)
)),stmts=(
	0: Nop(pc=0),
	1: Assignment(pc=3,DVar(useSites={2,3},value={java.util.HashMap$TreeNode, null}[↦3;refId=105],origin=1),GetField(pc=3,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={1,-1},value=java.util.HashMap$TreeNode[refId=104; values=«java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦3;refId=103]»]))),
	2: If(pc=8,UVar(defSites={1},value={java.util.HashMap$TreeNode, null}[↦3;refId=105]),!=,NullExpr(pc=-333),target=4),
	3: ReturnValue(pc=12,UVar(defSites={1,-1},value=java.util.HashMap$TreeNode[refId=104; values=«java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦3;refId=103]»])),
	4: Goto(pc=15,target=1)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_1}
	BB_5: ExitNode(normalReturn=false)
))

boolean checkInvariants(java.util.HashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={0,8,4,20,2,18,1,33,25,13,3,35,27,39} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={16,17,19},value={java.util.HashMap$TreeNode, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-2},value={java.util.HashMap$TreeNode, null}[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={24,50,42,26,49,41,23},value={java.util.HashMap$TreeNode, null}[↦6;refId=105],origin=1),GetField(pc=6,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	2: Assignment(pc=11,DVar(useSites={32,44,34,54,45,55,31},value={java.util.HashMap$TreeNode, null}[↦11;refId=106],origin=2),GetField(pc=11,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	3: Assignment(pc=16,DVar(useSites={6,7},value={java.util.HashMap$TreeNode, null}[↦16;refId=107],origin=3),GetField(pc=16,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	4: Assignment(pc=22,DVar(useSites={12,5,11},value={_ <: java.util.HashMap$Node, null}[↦22;refId=108],origin=4),GetField(pc=22,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	5: Checkcast(pc=25,UVar(defSites={4},value={_ <: java.util.HashMap$Node, null}[↦22;refId=108]),java.util.HashMap$TreeNode),
	6: If(pc=32,UVar(defSites={3},value={java.util.HashMap$TreeNode, null}[↦16;refId=107]),==,NullExpr(pc=-333),target=11),
	7: Assignment(pc=37,DVar(useSites={8},value={_ <: java.util.HashMap$Node, null}[↦37;refId=111],origin=7),GetField(pc=37,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={3},value=java.util.HashMap$TreeNode[↦16;refId=107]))),
	8: If(pc=41,UVar(defSites={7},value={_ <: java.util.HashMap$Node, null}[↦37;refId=111]),==,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]),target=11),
	9: Assignment(pc=44,DVar(useSites={10},value=int = 0,origin=9),IntConst(pc=44,0)),
	10: ReturnValue(pc=45,UVar(defSites={9},value=int = 0)),
	11: If(pc=48,UVar(defSites={4},value={java.util.HashMap$TreeNode, null}[↦22;refId=109]),==,NullExpr(pc=-333),target=16),
	12: Assignment(pc=53,DVar(useSites={13},value={java.util.HashMap$TreeNode, null}[↦53;refId=112],origin=12),GetField(pc=53,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={4},value=java.util.HashMap$TreeNode[↦22;refId=109]))),
	13: If(pc=57,UVar(defSites={12},value={java.util.HashMap$TreeNode, null}[↦53;refId=112]),==,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]),target=16),
	14: Assignment(pc=60,DVar(useSites={15},value=int = 0,origin=14),IntConst(pc=60,0)),
	15: ReturnValue(pc=61,UVar(defSites={14},value=int = 0)),
	16: If(pc=63,UVar(defSites={0},value={java.util.HashMap$TreeNode, null}[↦1;refId=103]),==,NullExpr(pc=-333),target=23),
	17: Assignment(pc=68,DVar(useSites={18},value={java.util.HashMap$TreeNode, null}[↦68;refId=113],origin=17),GetField(pc=68,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={0},value=java.util.HashMap$TreeNode[↦1;refId=103]))),
	18: If(pc=71,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]),==,UVar(defSites={17},value={java.util.HashMap$TreeNode, null}[↦68;refId=113]),target=23),
	19: Assignment(pc=76,DVar(useSites={20},value={java.util.HashMap$TreeNode, null}[↦76;refId=114],origin=19),GetField(pc=76,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={0},value=java.util.HashMap$TreeNode[↦1;refId=103]))),
	20: If(pc=79,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]),==,UVar(defSites={19},value={java.util.HashMap$TreeNode, null}[↦76;refId=114]),target=23),
	21: Assignment(pc=82,DVar(useSites={22},value=int = 0,origin=21),IntConst(pc=82,0)),
	22: ReturnValue(pc=83,UVar(defSites={21},value=int = 0)),
	23: If(pc=85,UVar(defSites={1},value={java.util.HashMap$TreeNode, null}[↦6;refId=105]),==,NullExpr(pc=-333),target=31),
	24: Assignment(pc=89,DVar(useSites={25},value={java.util.HashMap$TreeNode, null}[↦89;refId=115],origin=24),GetField(pc=89,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦6;refId=105]))),
	25: If(pc=93,UVar(defSites={24},value={java.util.HashMap$TreeNode, null}[↦89;refId=115]),!=,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]),target=29),
	26: Assignment(pc=97,DVar(useSites={28},value=an int,origin=26),GetField(pc=97,java.util.HashMap$TreeNode,hash,int,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦6;refId=105]))),
	27: Assignment(pc=101,DVar(useSites={28},value=an int,origin=27),GetField(pc=101,java.util.HashMap$TreeNode,hash,int,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	28: If(pc=104,UVar(defSites={26},value=an int),<=,UVar(defSites={27},value=an int),target=31),
	29: Assignment(pc=107,DVar(useSites={30},value=int = 0,origin=29),IntConst(pc=107,0)),
	30: ReturnValue(pc=108,UVar(defSites={29},value=int = 0)),
	31: If(pc=110,UVar(defSites={2},value={java.util.HashMap$TreeNode, null}[↦11;refId=106]),==,NullExpr(pc=-333),target=39),
	32: Assignment(pc=114,DVar(useSites={33},value={java.util.HashMap$TreeNode, null}[↦114;refId=116],origin=32),GetField(pc=114,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦11;refId=106]))),
	33: If(pc=118,UVar(defSites={32},value={java.util.HashMap$TreeNode, null}[↦114;refId=116]),!=,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]),target=37),
	34: Assignment(pc=122,DVar(useSites={36},value=an int,origin=34),GetField(pc=122,java.util.HashMap$TreeNode,hash,int,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦11;refId=106]))),
	35: Assignment(pc=126,DVar(useSites={36},value=an int,origin=35),GetField(pc=126,java.util.HashMap$TreeNode,hash,int,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	36: If(pc=129,UVar(defSites={34},value=an int),>=,UVar(defSites={35},value=an int),target=39),
	37: Assignment(pc=132,DVar(useSites={38},value=int = 0,origin=37),IntConst(pc=132,0)),
	38: ReturnValue(pc=133,UVar(defSites={37},value=int = 0)),
	39: Assignment(pc=135,DVar(useSites={40},value=int ∈ [0,1],origin=39),GetField(pc=135,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={-2},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	40: If(pc=138,UVar(defSites={39},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=49),
	41: If(pc=142,UVar(defSites={1},value={java.util.HashMap$TreeNode, null}[↦6;refId=105]),==,NullExpr(pc=-333),target=49),
	42: Assignment(pc=146,DVar(useSites={43},value=int ∈ [0,1],origin=42),GetField(pc=146,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦6;refId=105]))),
	43: If(pc=149,UVar(defSites={42},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=49),
	44: If(pc=153,UVar(defSites={2},value={java.util.HashMap$TreeNode, null}[↦11;refId=106]),==,NullExpr(pc=-333),target=49),
	45: Assignment(pc=157,DVar(useSites={46},value=int ∈ [0,1],origin=45),GetField(pc=157,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.HashMap$TreeNode[↦11;refId=106]))),
	46: If(pc=160,UVar(defSites={45},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=49),
	47: Assignment(pc=163,DVar(useSites={48},value=int = 0,origin=47),IntConst(pc=163,0)),
	48: ReturnValue(pc=164,UVar(defSites={47},value=int = 0)),
	49: If(pc=166,UVar(defSites={1},value={java.util.HashMap$TreeNode, null}[↦6;refId=105]),==,NullExpr(pc=-333),target=54),
	50: Assignment(pc=170,DVar(useSites={51},value=int ∈ [0,1],origin=50),StaticFunctionCall(pc=170,java.util.HashMap$TreeNode,isInterface=false,boolean checkInvariants(java.util.HashMap$TreeNode),(UVar(defSites={1},value=java.util.HashMap$TreeNode[↦6;refId=105])))),
	51: If(pc=173,UVar(defSites={50},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=54),
	52: Assignment(pc=176,DVar(useSites={53},value=int = 0,origin=52),IntConst(pc=176,0)),
	53: ReturnValue(pc=177,UVar(defSites={52},value=int = 0)),
	54: If(pc=179,UVar(defSites={2},value={java.util.HashMap$TreeNode, null}[↦11;refId=106]),==,NullExpr(pc=-333),target=59),
	55: Assignment(pc=183,DVar(useSites={56},value=int ∈ [0,1],origin=55),StaticFunctionCall(pc=183,java.util.HashMap$TreeNode,isInterface=false,boolean checkInvariants(java.util.HashMap$TreeNode),(UVar(defSites={2},value=java.util.HashMap$TreeNode[↦11;refId=106])))),
	56: If(pc=186,UVar(defSites={55},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=59),
	57: Assignment(pc=189,DVar(useSites={58},value=int = 0,origin=57),IntConst(pc=189,0)),
	58: ReturnValue(pc=190,UVar(defSites={57},value=int = 0)),
	59: Assignment(pc=191,DVar(useSites={60},value=int = 1,origin=59),IntConst(pc=191,1)),
	60: ReturnValue(pc=192,UVar(defSites={59},value=int = 1))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_9,BB_2}
	BB_10: BasicBlock(start=57,end=58) -> {BB_7}
	BB_11: BasicBlock(start=29,end=30) -> {BB_7}
	BB_12: BasicBlock(start=45,end=46) -> {BB_1a,BB_a}
	BB_13: BasicBlock(start=17,end=18) -> {BB_22,BB_24}
	BB_14: BasicBlock(start=32,end=33) -> {BB_d,BB_15}
	BB_15: BasicBlock(start=34,end=36) -> {BB_d,BB_1c}
	BB_16: BasicBlock(start=44,end=44) -> {BB_12,BB_1a}
	BB_17: BasicBlock(start=59,end=60) -> {BB_7}
	BB_18: BasicBlock(start=12,end=13) -> {BB_f,BB_1e}
	BB_19: BasicBlock(start=54,end=54) -> {BB_21,BB_17}
	BB_1: BasicBlock(start=56,end=56) -> {BB_10,BB_17}
	BB_1a: BasicBlock(start=49,end=49) -> {BB_19,BB_1d}
	BB_1b: BasicBlock(start=7,end=8) -> {BB_5,BB_8}
	BB_1c: BasicBlock(start=39,end=40) -> {BB_1a,BB_6}
	BB_1d: BasicBlock(start=50,end=50) -> {BB_9,BB_23}
	BB_1e: BasicBlock(start=16,end=16) -> {BB_22,BB_13}
	BB_1f: BasicBlock(start=31,end=31) -> {BB_1c,BB_14}
	BB_20: BasicBlock(start=26,end=28) -> {BB_1f,BB_11}
	BB_21: BasicBlock(start=55,end=55) -> {BB_9,BB_1}
	BB_22: BasicBlock(start=23,end=23) -> {BB_c,BB_1f}
	BB_23: BasicBlock(start=51,end=51) -> {BB_e,BB_19}
	BB_24: BasicBlock(start=19,end=20) -> {BB_22,BB_4}
	BB_2: BasicBlock(start=1,end=5) -> {BB_9,BB_3}
	BB_3: BasicBlock(start=6,end=6) -> {BB_8,BB_1b}
	BB_4: BasicBlock(start=21,end=22) -> {BB_7}
	BB_5: BasicBlock(start=9,end=10) -> {BB_7}
	BB_6: BasicBlock(start=41,end=41) -> {BB_b,BB_1a}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=11,end=11) -> {BB_1e,BB_18}
	BB_9: ExitNode(normalReturn=false)
	BB_a: BasicBlock(start=47,end=48) -> {BB_7}
	BB_b: BasicBlock(start=42,end=43) -> {BB_16,BB_1a}
	BB_c: BasicBlock(start=24,end=25) -> {BB_20,BB_11}
	BB_d: BasicBlock(start=37,end=38) -> {BB_7}
	BB_e: BasicBlock(start=52,end=53) -> {BB_7}
	BB_f: BasicBlock(start=14,end=15) -> {BB_7}
))

int tieBreakOrder(java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	1: useSites={0,8,2} (origin=-2),
	2: useSites={4,1,9} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-1;refId=102]),==,NullExpr(pc=-333),target=8),
	1: If(pc=5,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=8),
	2: Assignment(pc=9,DVar(useSites={3},value={java.lang.Class, null}[↦9;refId=105],origin=2),VirtualFunctionCall(pc=9,java.lang.Object,isInterface=false,java.lang.Class getClass(),UVar(defSites={-2},value=_ <: java.lang.Object[↦-1;refId=102]),())),
	3: Assignment(pc=12,DVar(useSites={6},value={java.lang.String, null}[↦12;refId=108],origin=3),VirtualFunctionCall(pc=12,java.lang.Class,isInterface=false,java.lang.String getName(),UVar(defSites={2},value={java.lang.Class, null}[↦9;refId=105]),())),
	4: Assignment(pc=16,DVar(useSites={5},value={java.lang.Class, null}[↦16;refId=110],origin=4),VirtualFunctionCall(pc=16,java.lang.Object,isInterface=false,java.lang.Class getClass(),UVar(defSites={-3},value=_ <: java.lang.Object[↦-2;refId=103]),())),
	5: Assignment(pc=19,DVar(useSites={6},value={java.lang.String, null}[↦19;refId=113],origin=5),VirtualFunctionCall(pc=19,java.lang.Class,isInterface=false,java.lang.String getName(),UVar(defSites={4},value={java.lang.Class, null}[↦16;refId=110]),())),
	6: Assignment(pc=22,DVar(useSites={7,15},value=an int,origin=6),VirtualFunctionCall(pc=22,java.lang.String,isInterface=false,int compareTo(java.lang.String),UVar(defSites={3},value={java.lang.String, null}[↦12;refId=108]),(UVar(defSites={5},value={java.lang.String, null}[↦19;refId=113])))),
	7: If(pc=27,UVar(defSites={6},value=an int),!=,IntConst(pc=-333,0),target=15),
	8: Assignment(pc=31,DVar(useSites={10},value=an int,origin=8),StaticFunctionCall(pc=31,java.lang.System,isInterface=false,int identityHashCode(java.lang.Object),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-1;refId=102])))),
	9: Assignment(pc=35,DVar(useSites={10},value=an int,origin=9),StaticFunctionCall(pc=35,java.lang.System,isInterface=false,int identityHashCode(java.lang.Object),(UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	10: If(pc=38,UVar(defSites={8},value=an int),>,UVar(defSites={9},value=an int),target=13),
	11: Assignment(pc=41,DVar(useSites={15},value=int = -1,origin=11),IntConst(pc=41,-1)),
	12: Goto(pc=42,target=14),
	13: Assignment(pc=45,DVar(useSites={15},value=int ∈ [-1,1],origin=13),IntConst(pc=45,1)),
	14: Nop(pc=46),
	15: ReturnValue(pc=48,UVar(defSites={6,13,11},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_d}
	BB_10: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_10,BB_5}
	BB_2: BasicBlock(start=10,end=10) -> {BB_c,BB_7}
	BB_3: BasicBlock(start=14,end=14) -> {BB_e}
	BB_4: BasicBlock(start=1,end=1) -> {BB_8,BB_d}
	BB_5: BasicBlock(start=6,end=6) -> {BB_10,BB_9}
	BB_6: BasicBlock(start=9,end=9) -> {BB_10,BB_2}
	BB_7: BasicBlock(start=13,end=13) -> {BB_3}
	BB_8: BasicBlock(start=2,end=2) -> {BB_10,BB_a}
	BB_9: BasicBlock(start=7,end=7) -> {BB_d,BB_e}
	BB_a: BasicBlock(start=3,end=3) -> {BB_10,BB_f}
	BB_b: ExitNode(normalReturn=true)
	BB_c: BasicBlock(start=11,end=12) -> {BB_3}
	BB_d: BasicBlock(start=8,end=8) -> {BB_10,BB_6}
	BB_e: BasicBlock(start=15,end=15) -> {BB_b}
	BB_f: BasicBlock(start=4,end=4) -> {BB_10,BB_1}
))

void treeify(java.util.HashMap$Node[])
AITACode(params=(Parameters(
	0: useSites={32,16,40,36,44,2,34,6,38,14,1,17,9,41,5,13,11,7} (origin=-1),
	1: useSites={44} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={32,16,40,36,44,34,38,17,41,7},value=null[↦0],origin=0),NullExpr(pc=0)),
	1: If(pc=5,UVar(defSites={2,-1},value={java.util.HashMap$TreeNode, null}[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]),==,NullExpr(pc=-333),target=44),
	2: Assignment(pc=9,DVar(useSites={32,16,40,36,44,34,6,38,14,1,17,9,41,5,13,3,11,7},value={_ <: java.util.HashMap$Node, null}[↦9;refId=210],origin=2),GetField(pc=9,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]))),
	3: Checkcast(pc=12,UVar(defSites={2},value={_ <: java.util.HashMap$Node, null}[↦9;refId=210]),java.util.HashMap$TreeNode),
	4: Assignment(pc=19,DVar(useSites={6,5},value=null[↦19],origin=4),NullExpr(pc=19)),
	5: PutField(pc=21,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]),UVar(defSites={4},value=null[↦19])),
	6: PutField(pc=24,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]),UVar(defSites={4},value=null[↦19])),
	7: If(pc=28,UVar(defSites={0,2,41,-1},value={java.util.HashMap$TreeNode, null}[refId=200; values=«{java.util.HashMap$TreeNode, null}[↦9;refId=110], null[↦0], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]),!=,NullExpr(pc=-333),target=13),
	8: Assignment(pc=32,DVar(useSites={9},value=null[↦32],origin=8),NullExpr(pc=32)),
	9: PutField(pc=33,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]),UVar(defSites={8},value=null[↦32])),
	10: Assignment(pc=37,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=37,0)),
	11: PutField(pc=38,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]),UVar(defSites={10},value=int = 0)),
	12: Goto(pc=43,target=43),
	13: Assignment(pc=47,DVar(useSites={25,29,27},value={_ <: java.lang.Object, null}[↦47;refId=216],origin=13),GetField(pc=47,java.util.HashMap$TreeNode,key,java.lang.Object,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]))),
	14: Assignment(pc=53,DVar(useSites={18,21},value=an int,origin=14),GetField(pc=53,java.util.HashMap$TreeNode,hash,int,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=115; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]))),
	15: Assignment(pc=58,DVar(useSites={24,27},value=null[↦58],origin=15),NullExpr(pc=58)),
	16: Assignment(pc=66,DVar(useSites={29,27},value={_ <: java.lang.Object, null}[↦66;refId=221],origin=16),GetField(pc=66,java.util.HashMap$TreeNode,key,java.lang.Object,UVar(defSites={0,32,2,34,41,-1},value=java.util.HashMap$TreeNode[refId=219; values=«{java.util.HashMap$TreeNode, null}[↦162;refId=195], {java.util.HashMap$TreeNode, null}[↦154;refId=190], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]))),
	17: Assignment(pc=73,DVar(useSites={18,21},value=an int,origin=17),GetField(pc=73,java.util.HashMap$TreeNode,hash,int,UVar(defSites={0,32,2,34,41,-1},value=java.util.HashMap$TreeNode[refId=219; values=«{java.util.HashMap$TreeNode, null}[↦162;refId=195], {java.util.HashMap$TreeNode, null}[↦154;refId=190], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]))),
	18: If(pc=81,UVar(defSites={17},value=an int),<=,UVar(defSites={14},value=an int),target=21),
	19: Assignment(pc=84,DVar(useSites={37,31},value=int = -1,origin=19),IntConst(pc=84,-1)),
	20: Goto(pc=87,target=31),
	21: If(pc=94,UVar(defSites={17},value=an int),>=,UVar(defSites={14},value=an int),target=24),
	22: Assignment(pc=97,DVar(useSites={37,31},value=int = 1,origin=22),IntConst(pc=97,1)),
	23: Goto(pc=100,target=31),
	24: If(pc=105,UVar(defSites={25,15},value={java.lang.Class, null}[refId=205; values=«null[↦58], {java.lang.Class, null}[↦110;refId=162]»]),!=,NullExpr(pc=-333),target=27),
	25: Assignment(pc=110,DVar(useSites={24,26,27},value={java.lang.Class, null}[↦110;refId=226],origin=25),StaticFunctionCall(pc=110,java.util.HashMap,isInterface=false,java.lang.Class comparableClassFor(java.lang.Object),(UVar(defSites={13},value={_ <: java.lang.Object, null}[↦47;refId=216])))),
	26: If(pc=116,UVar(defSites={25},value={java.lang.Class, null}[↦110;refId=226]),==,NullExpr(pc=-333),target=29),
	27: Assignment(pc=125,DVar(useSites={28,37,31},value=an int,origin=27),StaticFunctionCall(pc=125,java.util.HashMap,isInterface=false,int compareComparables(java.lang.Class,java.lang.Object,java.lang.Object),(UVar(defSites={25,15},value=java.lang.Class[↦110;refId=226]),UVar(defSites={13},value={_ <: java.lang.Object, null}[↦47;refId=216]),UVar(defSites={16},value={_ <: java.lang.Object, null}[↦66;refId=221])))),
	28: If(pc=131,UVar(defSites={27},value=an int),!=,IntConst(pc=-333,0),target=31),
	29: Assignment(pc=138,DVar(useSites={37,31},value=an int,origin=29),StaticFunctionCall(pc=138,java.util.HashMap$TreeNode,isInterface=false,int tieBreakOrder(java.lang.Object,java.lang.Object),(UVar(defSites={13},value={_ <: java.lang.Object, null}[↦47;refId=216]),UVar(defSites={16},value={_ <: java.lang.Object, null}[↦66;refId=221])))),
	30: Nop(pc=141),
	31: If(pc=149,UVar(defSites={22,29,19,27},value=an int),>,IntConst(pc=-333,0),target=34),
	32: Assignment(pc=154,DVar(useSites={16,40,36,34,38,33,17,35},value={java.util.HashMap$TreeNode, null}[↦154;refId=253],origin=32),GetField(pc=154,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={0,32,2,34,41,-1},value=java.util.HashMap$TreeNode[refId=236; values=«{java.util.HashMap$TreeNode, null}[↦162;refId=195], {java.util.HashMap$TreeNode, null}[↦154;refId=190], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]))),
	33: Goto(pc=157,target=35),
	34: Assignment(pc=162,DVar(useSites={32,16,40,36,38,17,35},value={java.util.HashMap$TreeNode, null}[refId=260; values=«{java.util.HashMap$TreeNode, null}[↦154;refId=253], {java.util.HashMap$TreeNode, null}[↦162;refId=259]»],origin=34),GetField(pc=162,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={0,32,2,34,41,-1},value=java.util.HashMap$TreeNode[refId=236; values=«{java.util.HashMap$TreeNode, null}[↦162;refId=195], {java.util.HashMap$TreeNode, null}[↦154;refId=190], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]))),
	35: If(pc=168,UVar(defSites={32,34},value={java.util.HashMap$TreeNode, null}[refId=260; values=«{java.util.HashMap$TreeNode, null}[↦154;refId=253], {java.util.HashMap$TreeNode, null}[↦162;refId=259]»]),!=,NullExpr(pc=-333),target=16),
	36: PutField(pc=174,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=256; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»]),UVar(defSites={0,32,2,34,41,-1},value=java.util.HashMap$TreeNode[refId=258; values=«{java.util.HashMap$TreeNode, null}[↦162;refId=195], {java.util.HashMap$TreeNode, null}[↦154;refId=190], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»])),
	37: If(pc=179,UVar(defSites={22,29,19,27},value=an int),>,IntConst(pc=-333,0),target=40),
	38: PutField(pc=185,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={0,32,2,34,41,-1},value=java.util.HashMap$TreeNode[refId=258; values=«{java.util.HashMap$TreeNode, null}[↦162;refId=195], {java.util.HashMap$TreeNode, null}[↦154;refId=190], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]),UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=256; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»])),
	39: Goto(pc=188,target=41),
	40: PutField(pc=194,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={0,32,2,34,41,-1},value=java.util.HashMap$TreeNode[refId=258; values=«{java.util.HashMap$TreeNode, null}[↦162;refId=195], {java.util.HashMap$TreeNode, null}[↦154;refId=190], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]),UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=256; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»])),
	41: Assignment(pc=199,DVar(useSites={32,16,40,36,44,34,42,38,17,7},value={java.util.HashMap$TreeNode, null}[↦199;refId=274],origin=41),StaticFunctionCall(pc=199,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode balanceInsertion(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={0,2,41,-1},value=java.util.HashMap$TreeNode[refId=269; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]),UVar(defSites={2,-1},value=java.util.HashMap$TreeNode[refId=270; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦9;refId=110]»])))),
	42: Goto(pc=203,target=43),
	43: Goto(pc=212,target=1),
	44: StaticMethodCall(pc=217,java.util.HashMap$TreeNode,isInterface=false,void moveRootToFront(java.util.HashMap$Node[],java.util.HashMap$TreeNode),(UVar(defSites={-2},value={_ <: java.util.HashMap$Node[], null}[↦-2;refId=103]),UVar(defSites={0,2,41,-1},value={java.util.HashMap$TreeNode, null}[refId=209; values=«null[↦9], null[↦0], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=174]»]))),
	45: Return(pc=220)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_2}
	BB_10: BasicBlock(start=45,end=45) -> {BB_5}
	BB_11: BasicBlock(start=32,end=33) -> {BB_4}
	BB_12: BasicBlock(start=34,end=34) -> {BB_4}
	BB_13: BasicBlock(start=22,end=23) -> {BB_17}
	BB_14: BasicBlock(start=44,end=44) -> {BB_1e,BB_10}
	BB_15: BasicBlock(start=27,end=27) -> {BB_1e,BB_c}
	BB_16: BasicBlock(start=16,end=18) -> {BB_1c,BB_b}
	BB_17: BasicBlock(start=31,end=31) -> {BB_12,BB_11}
	BB_18: BasicBlock(start=40,end=40) -> {BB_f}
	BB_19: BasicBlock(start=26,end=26) -> {BB_1,BB_15}
	BB_1: BasicBlock(start=29,end=29) -> {BB_1e,BB_1b}
	BB_1a: BasicBlock(start=36,end=37) -> {BB_d,BB_18}
	BB_1b: BasicBlock(start=30,end=30) -> {BB_17}
	BB_1c: BasicBlock(start=19,end=20) -> {BB_17}
	BB_1d: BasicBlock(start=4,end=7) -> {BB_e,BB_7}
	BB_1e: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=1,end=1) -> {BB_3,BB_14}
	BB_3: BasicBlock(start=2,end=3) -> {BB_1e,BB_1d}
	BB_4: BasicBlock(start=35,end=35) -> {BB_16,BB_1a}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=43,end=43) -> {BB_2}
	BB_7: BasicBlock(start=8,end=12) -> {BB_6}
	BB_8: BasicBlock(start=42,end=42) -> {BB_6}
	BB_9: BasicBlock(start=24,end=24) -> {BB_a,BB_15}
	BB_a: BasicBlock(start=25,end=25) -> {BB_1e,BB_19}
	BB_b: BasicBlock(start=21,end=21) -> {BB_13,BB_9}
	BB_c: BasicBlock(start=28,end=28) -> {BB_1,BB_17}
	BB_d: BasicBlock(start=38,end=39) -> {BB_f}
	BB_e: BasicBlock(start=13,end=15) -> {BB_16}
	BB_f: BasicBlock(start=41,end=41) -> {BB_1e,BB_8}
))

void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3),
	3: useSites={0} (origin=-4),
	4: useSites={0} (origin=-5)
)),stmts=(
	0: NonVirtualMethodCall(pc=6,java.util.LinkedHashMap$Entry,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={-5},value={_ <: java.util.HashMap$Node, null}[↦-5;refId=105]))),
	1: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.HashMap$Node untreeify(java.util.HashMap)
AITACode(params=(Parameters(
	0: useSites={8,4,2} (origin=-1),
	1: useSites={4} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={10},value=null[↦0],origin=0),NullExpr(pc=0)),
	1: Assignment(pc=2,DVar(useSites={5,7},value=null[↦2],origin=1),NullExpr(pc=2)),
	2: If(pc=9,UVar(defSites={8,-1},value={_ <: java.util.HashMap$Node, null}[refId=110; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {_ <: java.util.HashMap$Node, null}[↦42;refId=107]»]),==,NullExpr(pc=-333),target=10),
	3: Assignment(pc=15,DVar(useSites={4},value=null[↦15],origin=3),NullExpr(pc=15)),
	4: Assignment(pc=16,DVar(useSites={10,5,7},value={_ <: java.util.HashMap$Node, null}[↦16;refId=113],origin=4),VirtualFunctionCall(pc=16,java.util.HashMap,isInterface=false,java.util.HashMap$Node replacementNode(java.util.HashMap$Node,java.util.HashMap$Node),UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103]),(UVar(defSites={8,-1},value=_ <: java.util.HashMap$Node[refId=110; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {_ <: java.util.HashMap$Node, null}[↦42;refId=107]»]),UVar(defSites={3},value=null[↦15])))),
	5: If(pc=22,UVar(defSites={4,1},value={_ <: java.util.HashMap$Node, null}[refId=109; values=«null[↦2], {_ <: java.util.HashMap$Node, null}[↦16;refId=106]»]),!=,NullExpr(pc=-333),target=7),
	6: Goto(pc=28,target=8),
	7: PutField(pc=34,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={4,1},value=_ <: java.util.HashMap$Node[↦16;refId=106]),UVar(defSites={4},value={_ <: java.util.HashMap$Node, null}[↦16;refId=113])),
	8: Assignment(pc=42,DVar(useSites={4,2,9},value={_ <: java.util.HashMap$Node, null}[↦42;refId=115],origin=8),GetField(pc=42,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={8,-1},value=_ <: java.util.HashMap$Node[refId=110; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {_ <: java.util.HashMap$Node, null}[↦42;refId=107]»]))),
	9: Goto(pc=47,target=2),
	10: ReturnValue(pc=51,UVar(defSites={0,4},value={_ <: java.util.HashMap$Node, null}[refId=108; values=«null[↦0], {_ <: java.util.HashMap$Node, null}[↦16;refId=106]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3,BB_5}
	BB_2: BasicBlock(start=10,end=10) -> {BB_7}
	BB_3: BasicBlock(start=6,end=6) -> {BB_8}
	BB_4: BasicBlock(start=2,end=2) -> {BB_6,BB_2}
	BB_5: BasicBlock(start=7,end=7) -> {BB_8}
	BB_6: BasicBlock(start=3,end=4) -> {BB_9,BB_1}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=8,end=9) -> {BB_4}
	BB_9: ExitNode(normalReturn=false)
))

void split(java.util.HashMap,java.util.HashMap$Node[],int,int)
AITACode(params=(Parameters(
	0: useSites={32,20,44,34,10,26,6,14,33,17,21,45,29,35,11,43,7,39,23,15} (origin=-1),
	1: useSites={29,39} (origin=-2),
	2: useSites={32,40,34,30,45,43} (origin=-3),
	3: useSites={32,42,38,30} (origin=-4),
	4: useSites={12,42,38} (origin=-5)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={32,44,34,26,29},value=null[↦3],origin=0),NullExpr(pc=3)),
	1: Assignment(pc=6,DVar(useSites={14,17,15},value=null[↦6],origin=1),NullExpr(pc=6)),
	2: Assignment(pc=9,DVar(useSites={33,45,35,43,39},value=null[↦9],origin=2),NullExpr(pc=9)),
	3: Assignment(pc=12,DVar(useSites={20,21,23},value=null[↦12],origin=3),NullExpr(pc=12)),
	4: Assignment(pc=15,DVar(useSites={28,18},value=int = 0,origin=4),IntConst(pc=15,0)),
	5: Assignment(pc=18,DVar(useSites={24,37},value=int = 0,origin=5),IntConst(pc=18,0)),
	6: If(pc=27,UVar(defSites={7,-1},value={java.util.HashMap$TreeNode, null}[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»]),==,NullExpr(pc=-333),target=26),
	7: Assignment(pc=32,DVar(useSites={32,8,20,44,34,10,26,6,14,33,17,21,45,29,35,11,43,39,23,15},value={_ <: java.util.HashMap$Node, null}[↦32;refId=1362],origin=7),GetField(pc=32,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={7,-1},value=java.util.HashMap$TreeNode[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»]))),
	8: Checkcast(pc=35,UVar(defSites={7},value={_ <: java.util.HashMap$Node, null}[↦32;refId=1362]),java.util.HashMap$TreeNode),
	9: Assignment(pc=42,DVar(useSites={10},value=null[↦42],origin=9),NullExpr(pc=42)),
	10: PutField(pc=43,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={7,-1},value=java.util.HashMap$TreeNode[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»]),UVar(defSites={9},value=null[↦42])),
	11: Assignment(pc=48,DVar(useSites={12},value=an int,origin=11),GetField(pc=48,java.util.HashMap$TreeNode,hash,int,UVar(defSites={7,-1},value=java.util.HashMap$TreeNode[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»]))),
	12: Assignment(pc=53,DVar(useSites={13},value=an int,origin=12),BinaryExpr(pc=53,ComputationalTypeInt,UVar(defSites={11},value=an int),&,UVar(defSites={-5},value=an int))),
	13: If(pc=54,UVar(defSites={12},value=an int),!=,IntConst(pc=-333,0),target=20),
	14: PutField(pc=62,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={7,-1},value=java.util.HashMap$TreeNode[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»]),UVar(defSites={1,7,-1},value={java.util.HashMap$TreeNode, null}[refId=136; values=«java.util.HashMap$TreeNode[↦-1;refId=102], null[↦6], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»])),
	15: If(pc=65,UVar(defSites={1,7,-1},value={java.util.HashMap$TreeNode, null}[refId=136; values=«java.util.HashMap$TreeNode[↦-1;refId=102], null[↦6], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),!=,NullExpr(pc=-333),target=17),
	16: Goto(pc=72,target=18),
	17: PutField(pc=79,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={1,7,-1},value=java.util.HashMap$TreeNode[refId=1365; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),UVar(defSites={7,-1},value=java.util.HashMap$TreeNode[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»])),
	18: Assignment(pc=86,DVar(useSites={28,19},value=an int,origin=18),BinaryExpr(pc=86,ComputationalTypeInt,UVar(defSites={4,18},value=an int),+,IntConst(pc=86,1))),
	19: Goto(pc=89,target=25),
	20: PutField(pc=97,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={7,-1},value=java.util.HashMap$TreeNode[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»]),UVar(defSites={3,7,-1},value={java.util.HashMap$TreeNode, null}[refId=1360; values=«null[↦12], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1227]»])),
	21: If(pc=100,UVar(defSites={3,7,-1},value={java.util.HashMap$TreeNode, null}[refId=1360; values=«null[↦12], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1227]»]),!=,NullExpr(pc=-333),target=23),
	22: Goto(pc=107,target=24),
	23: PutField(pc=114,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={3,7,-1},value=java.util.HashMap$TreeNode[refId=1375; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1227]»]),UVar(defSites={7,-1},value=java.util.HashMap$TreeNode[refId=1361; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=1295]»])),
	24: Assignment(pc=121,DVar(useSites={25,37},value=an int,origin=24),BinaryExpr(pc=121,ComputationalTypeInt,UVar(defSites={24,5},value=an int),+,IntConst(pc=121,1))),
	25: Goto(pc=128,target=6),
	26: If(pc=133,UVar(defSites={0,7,-1},value={java.util.HashMap$TreeNode, null}[refId=135; values=«java.util.HashMap$TreeNode[↦-1;refId=102], null[↦3], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),==,NullExpr(pc=-333),target=35),
	27: Assignment(pc=138,DVar(useSites={28},value=int = 6,origin=27),IntConst(pc=138,6)),
	28: If(pc=140,UVar(defSites={4,18},value=an int),>,UVar(defSites={27},value=int = 6),target=32),
	29: Assignment(pc=148,DVar(useSites={30},value={_ <: java.util.HashMap$Node, null}[↦148;refId=1399],origin=29),VirtualFunctionCall(pc=148,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$Node untreeify(java.util.HashMap),UVar(defSites={0,7,-1},value=java.util.HashMap$TreeNode[refId=1386; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),(UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103])))),
	30: ArrayStore(pc=151,UVar(defSites={-3},value={_ <: java.util.HashMap$Node[], null}[↦-3;refId=104]),UVar(defSites={-4},value=an int),UVar(defSites={29},value={_ <: java.util.HashMap$Node, null}[↦148;refId=1399])),
	31: Goto(pc=152,target=35),
	32: ArrayStore(pc=159,UVar(defSites={-3},value={_ <: java.util.HashMap$Node[], null}[↦-3;refId=104]),UVar(defSites={-4},value=an int),UVar(defSites={0,7,-1},value=java.util.HashMap$TreeNode[refId=1386; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»])),
	33: If(pc=162,UVar(defSites={2,7,-1},value={java.util.HashMap$TreeNode, null}[refId=137; values=«null[↦9], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),==,NullExpr(pc=-333),target=35),
	34: VirtualMethodCall(pc=168,java.util.HashMap$TreeNode,isInterface=false,void treeify(java.util.HashMap$Node[]),UVar(defSites={0,7,-1},value=java.util.HashMap$TreeNode[refId=1386; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),(UVar(defSites={-3},value=_ <: java.util.HashMap$Node[][↦-3;refId=104]))),
	35: If(pc=173,UVar(defSites={2,7,-1},value={java.util.HashMap$TreeNode, null}[refId=166; values=«null[↦9], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),==,NullExpr(pc=-333),target=46),
	36: Assignment(pc=178,DVar(useSites={37},value=int = 6,origin=36),IntConst(pc=178,6)),
	37: If(pc=180,UVar(defSites={24,5},value=an int),>,UVar(defSites={36},value=int = 6),target=42),
	38: Assignment(pc=187,DVar(useSites={40},value=an int,origin=38),BinaryExpr(pc=187,ComputationalTypeInt,UVar(defSites={-4},value=an int),+,UVar(defSites={-5},value=an int))),
	39: Assignment(pc=191,DVar(useSites={40},value={_ <: java.util.HashMap$Node, null}[↦191;refId=1421],origin=39),VirtualFunctionCall(pc=191,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$Node untreeify(java.util.HashMap),UVar(defSites={2,7,-1},value=java.util.HashMap$TreeNode[refId=1414; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),(UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103])))),
	40: ArrayStore(pc=194,UVar(defSites={-3},value={_ <: java.util.HashMap$Node[], null}[↦-3;refId=104]),UVar(defSites={38},value=an int),UVar(defSites={39},value={_ <: java.util.HashMap$Node, null}[↦191;refId=1421])),
	41: Goto(pc=195,target=46),
	42: Assignment(pc=202,DVar(useSites={43},value=an int,origin=42),BinaryExpr(pc=202,ComputationalTypeInt,UVar(defSites={-4},value=an int),+,UVar(defSites={-5},value=an int))),
	43: ArrayStore(pc=205,UVar(defSites={-3},value={_ <: java.util.HashMap$Node[], null}[↦-3;refId=104]),UVar(defSites={42},value=an int),UVar(defSites={2,7,-1},value=java.util.HashMap$TreeNode[refId=1414; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»])),
	44: If(pc=208,UVar(defSites={0,7,-1},value={java.util.HashMap$TreeNode, null}[refId=165; values=«null[↦3], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),==,NullExpr(pc=-333),target=46),
	45: VirtualMethodCall(pc=214,java.util.HashMap$TreeNode,isInterface=false,void treeify(java.util.HashMap$Node[]),UVar(defSites={2,7,-1},value=java.util.HashMap$TreeNode[refId=1414; values=«java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦32;refId=106]»]),(UVar(defSites={-3},value=_ <: java.util.HashMap$Node[][↦-3;refId=104]))),
	46: Return(pc=217)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_2}
	BB_10: BasicBlock(start=45,end=45) -> {BB_7,BB_c}
	BB_11: BasicBlock(start=17,end=17) -> {BB_17}
	BB_12: BasicBlock(start=32,end=32) -> {BB_7,BB_f}
	BB_13: BasicBlock(start=34,end=34) -> {BB_7,BB_6}
	BB_14: BasicBlock(start=22,end=22) -> {BB_9}
	BB_15: BasicBlock(start=44,end=44) -> {BB_c,BB_10}
	BB_16: BasicBlock(start=27,end=28) -> {BB_12,BB_d}
	BB_17: BasicBlock(start=18,end=19) -> {BB_a}
	BB_18: ExitNode(normalReturn=true)
	BB_19: BasicBlock(start=16,end=16) -> {BB_17}
	BB_1: BasicBlock(start=14,end=15) -> {BB_19,BB_11}
	BB_1a: BasicBlock(start=31,end=31) -> {BB_6}
	BB_1b: BasicBlock(start=40,end=40) -> {BB_7,BB_4}
	BB_1c: BasicBlock(start=26,end=26) -> {BB_16,BB_6}
	BB_1d: BasicBlock(start=23,end=23) -> {BB_9}
	BB_1e: BasicBlock(start=36,end=37) -> {BB_8,BB_e}
	BB_1f: BasicBlock(start=30,end=30) -> {BB_7,BB_1a}
	BB_2: BasicBlock(start=6,end=6) -> {BB_5,BB_1c}
	BB_3: BasicBlock(start=9,end=13) -> {BB_b,BB_1}
	BB_4: BasicBlock(start=41,end=41) -> {BB_c}
	BB_5: BasicBlock(start=7,end=8) -> {BB_7,BB_3}
	BB_6: BasicBlock(start=35,end=35) -> {BB_1e,BB_c}
	BB_7: ExitNode(normalReturn=false)
	BB_8: BasicBlock(start=42,end=43) -> {BB_7,BB_15}
	BB_9: BasicBlock(start=24,end=24) -> {BB_a}
	BB_a: BasicBlock(start=25,end=25) -> {BB_2}
	BB_b: BasicBlock(start=20,end=21) -> {BB_1d,BB_14}
	BB_c: BasicBlock(start=46,end=46) -> {BB_18}
	BB_d: BasicBlock(start=29,end=29) -> {BB_7,BB_1f}
	BB_e: BasicBlock(start=38,end=39) -> {BB_7,BB_1b}
	BB_f: BasicBlock(start=33,end=33) -> {BB_13,BB_6}
))

void <clinit>()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value=Class<java.util.HashMap>[↦0;refId=102],origin=0),ClassConst(pc=0,java.util.HashMap)),
	1: Assignment(pc=2,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=2,java.lang.Class,isInterface=false,boolean desiredAssertionStatus(),UVar(defSites={0},value=Class<java.util.HashMap>[↦0;refId=102]),())),
	2: If(pc=5,UVar(defSites={1},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=5),
	3: Assignment(pc=8,DVar(useSites={6},value=int = 1,origin=3),IntConst(pc=8,1)),
	4: Goto(pc=9,target=6),
	5: Assignment(pc=12,DVar(useSites={6},value=int ∈ [0,1],origin=5),IntConst(pc=12,0)),
	6: PutStatic(pc=13,java.util.HashMap$TreeNode,$assertionsDisabled,boolean,UVar(defSites={5,3},value=int ∈ [0,1])),
	7: Return(pc=16)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_6,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_2}
	BB_2: BasicBlock(start=6,end=7) -> {BB_5}
	BB_3: BasicBlock(start=2,end=2) -> {BB_4,BB_1}
	BB_4: BasicBlock(start=3,end=4) -> {BB_2}
	BB_5: ExitNode(normalReturn=true)
	BB_6: ExitNode(normalReturn=false)
))

java.util.HashMap$TreeNode balanceDeletion(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={0,8,24,52,12,2,82,6,14,110,1,129,81,109,3,51,11,7,71,23} (origin=-2),
	2: useSites={0,8,24,52,82,6,14,110,1,3,11,7} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),==,NullExpr(pc=-333),target=2),
	1: If(pc=6,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),!=,UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=464; values=«{java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),target=3),
	2: ReturnValue(pc=10,UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=506; values=«{java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»])),
	3: Assignment(pc=12,DVar(useSites={0,128,80,8,24,120,4,68,52,82,6,70,22,14,110,62,126,1,129,81,117,13,11,59,7,71,23,15},value={java.util.HashMap$TreeNode, null}[↦12;refId=508],origin=3),GetField(pc=12,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]))),
	4: If(pc=17,UVar(defSites={3},value={java.util.HashMap$TreeNode, null}[↦12;refId=508]),!=,NullExpr(pc=-333),target=8),
	5: Assignment(pc=21,DVar(useSites={6},value=int = 0,origin=5),IntConst(pc=21,0)),
	6: PutField(pc=22,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),UVar(defSites={5},value=int = 0)),
	7: ReturnValue(pc=26,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»])),
	8: Assignment(pc=28,DVar(useSites={9},value=int ∈ [0,1],origin=8),GetField(pc=28,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]))),
	9: If(pc=31,UVar(defSites={8},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=13),
	10: Assignment(pc=35,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=35,0)),
	11: PutField(pc=36,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),UVar(defSites={10},value=int = 0)),
	12: ReturnValue(pc=40,UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=464; values=«{java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»])),
	13: Assignment(pc=42,DVar(useSites={88,116,108,74,90,122,14,78,121,109,99,75,91},value={java.util.HashMap$TreeNode, null}[↦42;refId=509],origin=13),GetField(pc=42,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={3},value=java.util.HashMap$TreeNode[↦12;refId=508]))),
	14: If(pc=48,UVar(defSites={13},value={java.util.HashMap$TreeNode, null}[↦42;refId=509]),!=,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),target=74),
	15: Assignment(pc=52,DVar(useSites={64,32,16,20,50,58,30,33,17,41,51,63},value={java.util.HashMap$TreeNode, null}[↦52;refId=523],origin=15),GetField(pc=52,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={3},value=java.util.HashMap$TreeNode[↦12;refId=508]))),
	16: If(pc=58,UVar(defSites={15},value={java.util.HashMap$TreeNode, null}[↦52;refId=523]),==,NullExpr(pc=-333),target=30),
	17: Assignment(pc=63,DVar(useSites={18},value=int ∈ [0,1],origin=17),GetField(pc=63,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={15},value=java.util.HashMap$TreeNode[↦52;refId=523]))),
	18: If(pc=66,UVar(defSites={17},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=30),
	19: Assignment(pc=71,DVar(useSites={20},value=int = 0,origin=19),IntConst(pc=71,0)),
	20: PutField(pc=72,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={15},value=java.util.HashMap$TreeNode[↦52;refId=523]),UVar(defSites={19},value=int = 0)),
	21: Assignment(pc=76,DVar(useSites={22},value=int = 1,origin=21),IntConst(pc=76,1)),
	22: PutField(pc=77,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={3},value=java.util.HashMap$TreeNode[↦12;refId=508]),UVar(defSites={21},value=int = 1)),
	23: Assignment(pc=82,DVar(useSites={0,8,24,52,12,2,82,6,14,110,1,129,81,109,3,51,11,7,71},value={java.util.HashMap$TreeNode, null}[↦82;refId=531],origin=23),StaticFunctionCall(pc=82,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateLeft(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=464; values=«{java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),UVar(defSites={3},value=java.util.HashMap$TreeNode[↦12;refId=508])))),
	24: Assignment(pc=87,DVar(useSites={0,8,68,52,28,82,6,70,14,110,62,1,25,3,11,59,7,71},value={java.util.HashMap$TreeNode, null}[↦87;refId=532],origin=24),GetField(pc=87,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]))),
	25: If(pc=92,UVar(defSites={24},value={java.util.HashMap$TreeNode, null}[↦87;refId=532]),!=,NullExpr(pc=-333),target=28),
	26: Assignment(pc=95,DVar(useSites={64,32,50,58,30,33,41,51,63},value=null[↦95],origin=26),NullExpr(pc=95)),
	27: Goto(pc=96,target=29),
	28: Assignment(pc=100,DVar(useSites={64,32,50,58,30,33,41,51,63},value={java.util.HashMap$TreeNode, null}[refId=535; values=«null[↦95], {java.util.HashMap$TreeNode, null}[↦100;refId=534]»],origin=28),GetField(pc=100,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={24},value=java.util.HashMap$TreeNode[↦87;refId=532]))),
	29: Nop(pc=103),
	30: If(pc=107,UVar(defSites={28,26,15},value={java.util.HashMap$TreeNode, null}[refId=529; values=«null[↦95], {java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523]»]),!=,NullExpr(pc=-333),target=32),
	31: Goto(pc=112,target=0),
	32: Assignment(pc=117,DVar(useSites={48,38,46,37},value={java.util.HashMap$TreeNode, null}[↦117;refId=599],origin=32),GetField(pc=117,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={28,26,15},value=java.util.HashMap$TreeNode[refId=596; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523]»]))),
	33: Assignment(pc=124,DVar(useSites={44,34,35,43},value={java.util.HashMap$TreeNode, null}[↦124;refId=600],origin=33),GetField(pc=124,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={28,26,15},value=java.util.HashMap$TreeNode[refId=596; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523]»]))),
	34: If(pc=131,UVar(defSites={33},value={java.util.HashMap$TreeNode, null}[↦124;refId=600]),==,NullExpr(pc=-333),target=37),
	35: Assignment(pc=136,DVar(useSites={36},value=int ∈ [0,1],origin=35),GetField(pc=136,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={33},value=java.util.HashMap$TreeNode[↦124;refId=600]))),
	36: If(pc=139,UVar(defSites={35},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=43),
	37: If(pc=144,UVar(defSites={32},value={java.util.HashMap$TreeNode, null}[↦117;refId=599]),==,NullExpr(pc=-333),target=40),
	38: Assignment(pc=149,DVar(useSites={39},value=int ∈ [0,1],origin=38),GetField(pc=149,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={32},value=java.util.HashMap$TreeNode[↦117;refId=599]))),
	39: If(pc=152,UVar(defSites={38},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=43),
	40: Assignment(pc=157,DVar(useSites={41},value=int = 1,origin=40),IntConst(pc=157,1)),
	41: PutField(pc=158,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={28,26,15},value=java.util.HashMap$TreeNode[refId=674; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523]»]),UVar(defSites={40},value=int = 1)),
	42: Goto(pc=163,target=0),
	43: If(pc=168,UVar(defSites={33},value={java.util.HashMap$TreeNode, null}[↦124;refId=600]),==,NullExpr(pc=-333),target=46),
	44: Assignment(pc=173,DVar(useSites={45},value=int ∈ [0,1],origin=44),GetField(pc=173,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={33},value=java.util.HashMap$TreeNode[↦124;refId=600]))),
	45: If(pc=176,UVar(defSites={44},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=58),
	46: If(pc=181,UVar(defSites={32},value={java.util.HashMap$TreeNode, null}[↦117;refId=599]),==,NullExpr(pc=-333),target=49),
	47: Assignment(pc=186,DVar(useSites={48},value=int = 0,origin=47),IntConst(pc=186,0)),
	48: PutField(pc=187,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={32},value=java.util.HashMap$TreeNode[↦117;refId=599]),UVar(defSites={47},value=int = 0)),
	49: Assignment(pc=192,DVar(useSites={50},value=int = 1,origin=49),IntConst(pc=192,1)),
	50: PutField(pc=193,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={28,26,15},value=java.util.HashMap$TreeNode[refId=743; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523]»]),UVar(defSites={49},value=int = 1)),
	51: Assignment(pc=199,DVar(useSites={0,8,24,52,12,2,82,6,14,110,1,129,81,109,3,11,7,71,23},value={java.util.HashMap$TreeNode, null}[↦199;refId=777],origin=51),StaticFunctionCall(pc=199,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateRight(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=741; values=«{java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),UVar(defSites={28,26,15},value=java.util.HashMap$TreeNode[refId=743; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523]»])))),
	52: Assignment(pc=204,DVar(useSites={56,68,70,62,53,59,71},value={java.util.HashMap$TreeNode, null}[↦204;refId=778],origin=52),GetField(pc=204,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=742; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]))),
	53: If(pc=209,UVar(defSites={52},value={java.util.HashMap$TreeNode, null}[↦204;refId=778]),!=,NullExpr(pc=-333),target=56),
	54: Assignment(pc=212,DVar(useSites={64,58,63},value=null[↦212],origin=54),NullExpr(pc=212)),
	55: Goto(pc=213,target=57),
	56: Assignment(pc=217,DVar(useSites={64,58,63},value={java.util.HashMap$TreeNode, null}[refId=780; values=«null[↦212], {java.util.HashMap$TreeNode, null}[↦217;refId=779]»],origin=56),GetField(pc=217,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={52},value=java.util.HashMap$TreeNode[↦204;refId=778]))),
	57: Nop(pc=220),
	58: If(pc=224,UVar(defSites={56,28,26,54,15},value={java.util.HashMap$TreeNode, null}[refId=687; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523], null[↦212], {java.util.HashMap$TreeNode, null}[↦217;refId=282]»]),==,NullExpr(pc=-333),target=68),
	59: If(pc=230,UVar(defSites={24,52,3},value={java.util.HashMap$TreeNode, null}[refId=686; values=«{java.util.HashMap$TreeNode, null}[↦87;refId=439], java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦204;refId=281]»]),!=,NullExpr(pc=-333),target=62),
	60: Assignment(pc=233,DVar(useSites={63},value=int = 0,origin=60),IntConst(pc=233,0)),
	61: Goto(pc=234,target=63),
	62: Assignment(pc=238,DVar(useSites={63},value=int ∈ [0,1],origin=62),GetField(pc=238,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={24,52,3},value=java.util.HashMap$TreeNode[refId=686; values=«{java.util.HashMap$TreeNode, null}[↦87;refId=439], java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦204;refId=281]»]))),
	63: PutField(pc=241,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={56,28,26,54,15},value=java.util.HashMap$TreeNode[refId=751; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523], {java.util.HashMap$TreeNode, null}[↦217;refId=282]»]),UVar(defSites={60,62},value=int ∈ [0,1])),
	64: Assignment(pc=246,DVar(useSites={65,67},value={java.util.HashMap$TreeNode, null}[↦246;refId=786],origin=64),GetField(pc=246,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={56,28,26,54,15},value=java.util.HashMap$TreeNode[refId=751; values=«{java.util.HashMap$TreeNode, null}[↦100;refId=441], {java.util.HashMap$TreeNode, null}[↦52;refId=523], {java.util.HashMap$TreeNode, null}[↦217;refId=282]»]))),
	65: If(pc=252,UVar(defSites={64},value={java.util.HashMap$TreeNode, null}[↦246;refId=786]),==,NullExpr(pc=-333),target=68),
	66: Assignment(pc=257,DVar(useSites={67},value=int = 0,origin=66),IntConst(pc=257,0)),
	67: PutField(pc=258,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={64},value=java.util.HashMap$TreeNode[↦246;refId=786]),UVar(defSites={66},value=int = 0)),
	68: If(pc=262,UVar(defSites={24,52,3},value={java.util.HashMap$TreeNode, null}[refId=749; values=«java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦87;refId=439], {java.util.HashMap$TreeNode, null}[↦204;refId=281]»]),==,NullExpr(pc=-333),target=73),
	69: Assignment(pc=266,DVar(useSites={70},value=int = 0,origin=69),IntConst(pc=266,0)),
	70: PutField(pc=267,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={24,52,3},value=java.util.HashMap$TreeNode[refId=749; values=«java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦87;refId=439], {java.util.HashMap$TreeNode, null}[↦204;refId=281]»]),UVar(defSites={69},value=int = 0)),
	71: Assignment(pc=272,DVar(useSites={0,8,72,24,52,12,2,82,6,14,110,1,129,81,109,3,51,11,7,23},value={java.util.HashMap$TreeNode, null}[↦272;refId=784],origin=71),StaticFunctionCall(pc=272,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateLeft(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=748; values=«{java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280], {java.util.HashMap$TreeNode, null}[↦483;refId=297]»]),UVar(defSites={24,52,3},value=java.util.HashMap$TreeNode[refId=749; values=«java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦87;refId=439], {java.util.HashMap$TreeNode, null}[↦204;refId=281]»])))),
	72: Nop(pc=275),
	73: Goto(pc=278,target=0),
	74: If(pc=282,UVar(defSites={13},value={java.util.HashMap$TreeNode, null}[↦42;refId=509]),==,NullExpr(pc=-333),target=88),
	75: Assignment(pc=286,DVar(useSites={76},value=int ∈ [0,1],origin=75),GetField(pc=286,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={13},value=java.util.HashMap$TreeNode[↦42;refId=509]))),
	76: If(pc=289,UVar(defSites={75},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=88),
	77: Assignment(pc=293,DVar(useSites={78},value=int = 0,origin=77),IntConst(pc=293,0)),
	78: PutField(pc=294,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={13},value=java.util.HashMap$TreeNode[↦42;refId=509]),UVar(defSites={77},value=int = 0)),
	79: Assignment(pc=298,DVar(useSites={80},value=int = 1,origin=79),IntConst(pc=298,1)),
	80: PutField(pc=299,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={3},value=java.util.HashMap$TreeNode[↦12;refId=508]),UVar(defSites={79},value=int = 1)),
	81: Assignment(pc=304,DVar(useSites={0,8,24,52,12,2,82,6,14,110,1,129,109,3,51,11,7,71,23},value={java.util.HashMap$TreeNode, null}[↦304;refId=517],origin=81),StaticFunctionCall(pc=304,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateRight(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=464; values=«{java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),UVar(defSites={3},value=java.util.HashMap$TreeNode[↦12;refId=508])))),
	82: Assignment(pc=309,DVar(useSites={0,128,8,24,120,52,6,86,14,110,126,1,129,117,3,83,11,7},value={java.util.HashMap$TreeNode, null}[↦309;refId=518],origin=82),GetField(pc=309,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=486; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]))),
	83: If(pc=314,UVar(defSites={82},value={java.util.HashMap$TreeNode, null}[↦309;refId=518]),!=,NullExpr(pc=-333),target=86),
	84: Assignment(pc=317,DVar(useSites={88,116,108,90,122,121,109,99,91},value=null[↦317],origin=84),NullExpr(pc=317)),
	85: Goto(pc=318,target=87),
	86: Assignment(pc=322,DVar(useSites={88,116,108,90,122,121,109,99,91},value={java.util.HashMap$TreeNode, null}[refId=521; values=«null[↦317], {java.util.HashMap$TreeNode, null}[↦322;refId=520]»],origin=86),GetField(pc=322,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={82},value=java.util.HashMap$TreeNode[↦309;refId=518]))),
	87: Nop(pc=325),
	88: If(pc=327,UVar(defSites={84,86,13},value={java.util.HashMap$TreeNode, null}[refId=515; values=«null[↦317], {java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509]»]),!=,NullExpr(pc=-333),target=90),
	89: Goto(pc=332,target=0),
	90: Assignment(pc=336,DVar(useSites={92,102,101,93},value={java.util.HashMap$TreeNode, null}[↦336;refId=578],origin=90),GetField(pc=336,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={84,86,13},value=java.util.HashMap$TreeNode[refId=575; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509]»]))),
	91: Assignment(pc=342,DVar(useSites={96,104,106,95},value={java.util.HashMap$TreeNode, null}[↦342;refId=579],origin=91),GetField(pc=342,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={84,86,13},value=java.util.HashMap$TreeNode[refId=575; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509]»]))),
	92: If(pc=349,UVar(defSites={90},value={java.util.HashMap$TreeNode, null}[↦336;refId=578]),==,NullExpr(pc=-333),target=95),
	93: Assignment(pc=354,DVar(useSites={94},value=int ∈ [0,1],origin=93),GetField(pc=354,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={90},value=java.util.HashMap$TreeNode[↦336;refId=578]))),
	94: If(pc=357,UVar(defSites={93},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=101),
	95: If(pc=362,UVar(defSites={91},value={java.util.HashMap$TreeNode, null}[↦342;refId=579]),==,NullExpr(pc=-333),target=98),
	96: Assignment(pc=367,DVar(useSites={97},value=int ∈ [0,1],origin=96),GetField(pc=367,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={91},value=java.util.HashMap$TreeNode[↦342;refId=579]))),
	97: If(pc=370,UVar(defSites={96},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=101),
	98: Assignment(pc=374,DVar(useSites={99},value=int = 1,origin=98),IntConst(pc=374,1)),
	99: PutField(pc=375,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={84,86,13},value=java.util.HashMap$TreeNode[refId=655; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509]»]),UVar(defSites={98},value=int = 1)),
	100: Goto(pc=380,target=0),
	101: If(pc=385,UVar(defSites={90},value={java.util.HashMap$TreeNode, null}[↦336;refId=578]),==,NullExpr(pc=-333),target=104),
	102: Assignment(pc=390,DVar(useSites={103},value=int ∈ [0,1],origin=102),GetField(pc=390,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={90},value=java.util.HashMap$TreeNode[↦336;refId=578]))),
	103: If(pc=393,UVar(defSites={102},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=116),
	104: If(pc=398,UVar(defSites={91},value={java.util.HashMap$TreeNode, null}[↦342;refId=579]),==,NullExpr(pc=-333),target=107),
	105: Assignment(pc=403,DVar(useSites={106},value=int = 0,origin=105),IntConst(pc=403,0)),
	106: PutField(pc=404,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={91},value=java.util.HashMap$TreeNode[↦342;refId=579]),UVar(defSites={105},value=int = 0)),
	107: Assignment(pc=408,DVar(useSites={108},value=int = 1,origin=107),IntConst(pc=408,1)),
	108: PutField(pc=409,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={84,86,13},value=java.util.HashMap$TreeNode[refId=725; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509]»]),UVar(defSites={107},value=int = 1)),
	109: Assignment(pc=414,DVar(useSites={0,8,24,52,12,2,82,6,14,110,1,129,81,3,51,11,7,71,23},value={java.util.HashMap$TreeNode, null}[↦414;refId=762],origin=109),StaticFunctionCall(pc=414,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateLeft(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=723; values=«{java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),UVar(defSites={84,86,13},value=java.util.HashMap$TreeNode[refId=725; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509]»])))),
	110: Assignment(pc=419,DVar(useSites={128,120,114,126,129,117,111},value={java.util.HashMap$TreeNode, null}[↦419;refId=763],origin=110),GetField(pc=419,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={24,82,-2,129,81,109,-3,3,51,71,23},value=java.util.HashMap$TreeNode[refId=724; values=«{java.util.HashMap$TreeNode, null}[↦-2;refId=103], java.util.HashMap$TreeNode[↦12;refId=415], {java.util.HashMap$TreeNode, null}[↦272;refId=405], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦483;refId=398], {java.util.HashMap$TreeNode, null}[↦309;refId=184], {java.util.HashMap$TreeNode, null}[↦87;refId=198], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]))),
	111: If(pc=424,UVar(defSites={110},value={java.util.HashMap$TreeNode, null}[↦419;refId=763]),!=,NullExpr(pc=-333),target=114),
	112: Assignment(pc=427,DVar(useSites={116,122,121},value=null[↦427],origin=112),NullExpr(pc=427)),
	113: Goto(pc=428,target=115),
	114: Assignment(pc=432,DVar(useSites={116,122,121},value={java.util.HashMap$TreeNode, null}[refId=765; values=«null[↦427], {java.util.HashMap$TreeNode, null}[↦432;refId=764]»],origin=114),GetField(pc=432,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={110},value=java.util.HashMap$TreeNode[↦419;refId=763]))),
	115: Nop(pc=435),
	116: If(pc=437,UVar(defSites={112,84,114,86,13},value={java.util.HashMap$TreeNode, null}[refId=668; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509], {java.util.HashMap$TreeNode, null}[↦432;refId=226], null[↦427]»]),==,NullExpr(pc=-333),target=126),
	117: If(pc=442,UVar(defSites={82,110,3},value={java.util.HashMap$TreeNode, null}[refId=667; values=«{java.util.HashMap$TreeNode, null}[↦309;refId=425], java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦419;refId=225]»]),!=,NullExpr(pc=-333),target=120),
	118: Assignment(pc=445,DVar(useSites={121},value=int = 0,origin=118),IntConst(pc=445,0)),
	119: Goto(pc=446,target=121),
	120: Assignment(pc=450,DVar(useSites={121},value=int ∈ [0,1],origin=120),GetField(pc=450,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={82,110,3},value=java.util.HashMap$TreeNode[refId=667; values=«{java.util.HashMap$TreeNode, null}[↦309;refId=425], java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦419;refId=225]»]))),
	121: PutField(pc=453,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={112,84,114,86,13},value=java.util.HashMap$TreeNode[refId=733; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509], {java.util.HashMap$TreeNode, null}[↦432;refId=226]»]),UVar(defSites={120,118},value=int ∈ [0,1])),
	122: Assignment(pc=457,DVar(useSites={125,123},value={java.util.HashMap$TreeNode, null}[↦457;refId=771],origin=122),GetField(pc=457,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={112,84,114,86,13},value=java.util.HashMap$TreeNode[refId=733; values=«{java.util.HashMap$TreeNode, null}[↦322;refId=427], {java.util.HashMap$TreeNode, null}[↦42;refId=509], {java.util.HashMap$TreeNode, null}[↦432;refId=226]»]))),
	123: If(pc=463,UVar(defSites={122},value={java.util.HashMap$TreeNode, null}[↦457;refId=771]),==,NullExpr(pc=-333),target=126),
	124: Assignment(pc=468,DVar(useSites={125},value=int = 0,origin=124),IntConst(pc=468,0)),
	125: PutField(pc=469,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={122},value=java.util.HashMap$TreeNode[↦457;refId=771]),UVar(defSites={124},value=int = 0)),
	126: If(pc=473,UVar(defSites={82,110,3},value={java.util.HashMap$TreeNode, null}[refId=731; values=«java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦309;refId=425], {java.util.HashMap$TreeNode, null}[↦419;refId=225]»]),==,NullExpr(pc=-333),target=131),
	127: Assignment(pc=477,DVar(useSites={128},value=int = 0,origin=127),IntConst(pc=477,0)),
	128: PutField(pc=478,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={82,110,3},value=java.util.HashMap$TreeNode[refId=731; values=«java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦309;refId=425], {java.util.HashMap$TreeNode, null}[↦419;refId=225]»]),UVar(defSites={127},value=int = 0)),
	129: Assignment(pc=483,DVar(useSites={0,8,24,52,12,2,130,82,6,14,110,1,81,109,3,51,11,7,71,23},value={java.util.HashMap$TreeNode, null}[↦483;refId=769],origin=129),StaticFunctionCall(pc=483,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode rotateRight(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={-2,129,81,109,51,71,23},value={java.util.HashMap$TreeNode, null}[refId=730; values=«{java.util.HashMap$TreeNode, null}[↦414;refId=224], {java.util.HashMap$TreeNode, null}[↦304;refId=107], {java.util.HashMap$TreeNode, null}[↦272;refId=348], {java.util.HashMap$TreeNode, null}[↦82;refId=113], {java.util.HashMap$TreeNode, null}[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦483;refId=297], {java.util.HashMap$TreeNode, null}[↦199;refId=280]»]),UVar(defSites={82,110,3},value=java.util.HashMap$TreeNode[refId=731; values=«java.util.HashMap$TreeNode[↦12;refId=508], {java.util.HashMap$TreeNode, null}[↦309;refId=425], {java.util.HashMap$TreeNode, null}[↦419;refId=225]»])))),
	130: Nop(pc=486),
	131: Goto(pc=489,target=0)
),cfg=CFG(
	BB_0: BasicBlock(start=13,end=14) -> {BB_1b,BB_47}
	BB_10: BasicBlock(start=52,end=53) -> {BB_d,BB_2c}
	BB_11: BasicBlock(start=110,end=111) -> {BB_3,BB_3d}
	BB_12: BasicBlock(start=46,end=46) -> {BB_4b,BB_2d}
	BB_13: BasicBlock(start=93,end=94) -> {BB_34,BB_6}
	BB_14: BasicBlock(start=57,end=57) -> {BB_40}
	BB_15: BasicBlock(start=29,end=29) -> {BB_42}
	BB_16: BasicBlock(start=121,end=123) -> {BB_45,BB_21}
	BB_17: BasicBlock(start=84,end=85) -> {BB_39}
	BB_18: BasicBlock(start=89,end=89) -> {BB_7}
	BB_19: BasicBlock(start=116,end=116) -> {BB_45,BB_1e}
	BB_1: BasicBlock(start=98,end=100) -> {BB_7}
	BB_1a: BasicBlock(start=1,end=1) -> {BB_26,BB_30}
	BB_1b: BasicBlock(start=74,end=74) -> {BB_8,BB_3f}
	BB_1c: BasicBlock(start=102,end=103) -> {BB_19,BB_3a}
	BB_1d: BasicBlock(start=60,end=61) -> {BB_32}
	BB_1e: BasicBlock(start=117,end=117) -> {BB_b,BB_2b}
	BB_1f: BasicBlock(start=28,end=28) -> {BB_15}
	BB_20: BasicBlock(start=38,end=39) -> {BB_38,BB_3b}
	BB_21: BasicBlock(start=124,end=125) -> {BB_45}
	BB_22: BasicBlock(start=77,end=81) -> {BB_46,BB_41}
	BB_23: BasicBlock(start=96,end=97) -> {BB_1,BB_6}
	BB_24: BasicBlock(start=73,end=73) -> {BB_7}
	BB_25: BasicBlock(start=105,end=106) -> {BB_44}
	BB_26: BasicBlock(start=2,end=2) -> {BB_33}
	BB_27: BasicBlock(start=32,end=34) -> {BB_31,BB_f}
	BB_28: BasicBlock(start=17,end=18) -> {BB_42,BB_43}
	BB_29: BasicBlock(start=44,end=45) -> {BB_40,BB_12}
	BB_2: BasicBlock(start=66,end=67) -> {BB_48}
	BB_2a: BasicBlock(start=59,end=59) -> {BB_1d,BB_49}
	BB_2b: BasicBlock(start=118,end=119) -> {BB_16}
	BB_2c: BasicBlock(start=54,end=55) -> {BB_14}
	BB_2d: BasicBlock(start=49,end=51) -> {BB_46,BB_10}
	BB_2e: BasicBlock(start=86,end=86) -> {BB_39}
	BB_2f: BasicBlock(start=130,end=130) -> {BB_4a}
	BB_30: BasicBlock(start=3,end=4) -> {BB_a,BB_3e}
	BB_31: BasicBlock(start=35,end=36) -> {BB_38,BB_f}
	BB_32: BasicBlock(start=63,end=65) -> {BB_48,BB_2}
	BB_33: ExitNode(normalReturn=true)
	BB_34: BasicBlock(start=95,end=95) -> {BB_1,BB_23}
	BB_35: BasicBlock(start=127,end=129) -> {BB_46,BB_2f}
	BB_36: BasicBlock(start=31,end=31) -> {BB_7}
	BB_37: BasicBlock(start=72,end=72) -> {BB_24}
	BB_38: BasicBlock(start=43,end=43) -> {BB_12,BB_29}
	BB_39: BasicBlock(start=87,end=87) -> {BB_8}
	BB_3: BasicBlock(start=112,end=113) -> {BB_9}
	BB_3a: BasicBlock(start=104,end=104) -> {BB_25,BB_44}
	BB_3b: BasicBlock(start=40,end=42) -> {BB_7}
	BB_3c: BasicBlock(start=26,end=27) -> {BB_15}
	BB_3d: BasicBlock(start=114,end=114) -> {BB_9}
	BB_3e: BasicBlock(start=8,end=9) -> {BB_c,BB_0}
	BB_3f: BasicBlock(start=75,end=76) -> {BB_22,BB_8}
	BB_40: BasicBlock(start=58,end=58) -> {BB_48,BB_2a}
	BB_41: BasicBlock(start=82,end=83) -> {BB_2e,BB_17}
	BB_42: BasicBlock(start=30,end=30) -> {BB_36,BB_27}
	BB_43: BasicBlock(start=19,end=23) -> {BB_46,BB_e}
	BB_44: BasicBlock(start=107,end=109) -> {BB_46,BB_11}
	BB_45: BasicBlock(start=126,end=126) -> {BB_35,BB_4a}
	BB_46: ExitNode(normalReturn=false)
	BB_47: BasicBlock(start=15,end=16) -> {BB_42,BB_28}
	BB_48: BasicBlock(start=68,end=68) -> {BB_24,BB_5}
	BB_49: BasicBlock(start=62,end=62) -> {BB_32}
	BB_4: BasicBlock(start=90,end=92) -> {BB_13,BB_34}
	BB_4a: BasicBlock(start=131,end=131) -> {BB_7}
	BB_4b: BasicBlock(start=47,end=48) -> {BB_2d}
	BB_5: BasicBlock(start=69,end=71) -> {BB_46,BB_37}
	BB_6: BasicBlock(start=101,end=101) -> {BB_1c,BB_3a}
	BB_7: BasicBlock(start=0,end=0) -> {BB_1a,BB_26}
	BB_8: BasicBlock(start=88,end=88) -> {BB_18,BB_4}
	BB_9: BasicBlock(start=115,end=115) -> {BB_19}
	BB_a: BasicBlock(start=5,end=7) -> {BB_33}
	BB_b: BasicBlock(start=120,end=120) -> {BB_16}
	BB_c: BasicBlock(start=10,end=12) -> {BB_33}
	BB_d: BasicBlock(start=56,end=56) -> {BB_14}
	BB_e: BasicBlock(start=24,end=25) -> {BB_1f,BB_3c}
	BB_f: BasicBlock(start=37,end=37) -> {BB_20,BB_3b}
))

java.util.HashMap$TreeNode find(int,java.lang.Object,java.lang.Class)
AITACode(params=(Parameters(
	0: useSites={8,2,1,13,3} (origin=-1),
	1: useSites={4,6,27} (origin=-2),
	2: useSites={10,9,21,19,11,27} (origin=-3),
	3: useSites={18,21,27} (origin=-4)
)),stmts=(
	0: Nop(pc=0),
	1: Assignment(pc=5,DVar(useSites={8,2,14,13,3,31},value={java.util.HashMap$TreeNode, null}[↦5;refId=126],origin=1),GetField(pc=5,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={2,1,-1},value=java.util.HashMap$TreeNode[refId=113; values=«{java.util.HashMap$TreeNode, null}[↦12;refId=106], {java.util.HashMap$TreeNode, null}[↦5;refId=105], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	2: Assignment(pc=12,DVar(useSites={16,8,1,13,3,27,31},value={java.util.HashMap$TreeNode, null}[↦12;refId=127],origin=2),GetField(pc=12,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={2,1,-1},value=java.util.HashMap$TreeNode[refId=113; values=«{java.util.HashMap$TreeNode, null}[↦12;refId=106], {java.util.HashMap$TreeNode, null}[↦5;refId=105], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	3: Assignment(pc=19,DVar(useSites={4,6},value=an int,origin=3),GetField(pc=19,java.util.HashMap$TreeNode,hash,int,UVar(defSites={2,1,-1},value=java.util.HashMap$TreeNode[refId=113; values=«{java.util.HashMap$TreeNode, null}[↦12;refId=106], {java.util.HashMap$TreeNode, null}[↦5;refId=105], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	4: If(pc=26,UVar(defSites={3},value=an int),<=,UVar(defSites={-2},value=an int),target=6),
	5: Goto(pc=33,target=31),
	6: If(pc=39,UVar(defSites={3},value=an int),>=,UVar(defSites={-2},value=an int),target=8),
	7: Goto(pc=46,target=31),
	8: Assignment(pc=51,DVar(useSites={9,21,11},value={_ <: java.lang.Object, null}[↦51;refId=128],origin=8),GetField(pc=51,java.util.HashMap$TreeNode,key,java.lang.Object,UVar(defSites={2,1,-1},value=java.util.HashMap$TreeNode[refId=113; values=«{java.util.HashMap$TreeNode, null}[↦12;refId=106], {java.util.HashMap$TreeNode, null}[↦5;refId=105], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	9: If(pc=58,UVar(defSites={8},value={_ <: java.lang.Object, null}[↦51;refId=128]),==,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),target=13),
	10: If(pc=62,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),==,NullExpr(pc=-333),target=14),
	11: Assignment(pc=68,DVar(useSites={12},value=int ∈ [0,1],origin=11),VirtualFunctionCall(pc=68,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=103]),(UVar(defSites={8},value={_ <: java.lang.Object, null}[↦51;refId=128])))),
	12: If(pc=71,UVar(defSites={11},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=14),
	13: ReturnValue(pc=76,UVar(defSites={2,1,-1},value=java.util.HashMap$TreeNode[refId=113; values=«{java.util.HashMap$TreeNode, null}[↦12;refId=106], {java.util.HashMap$TreeNode, null}[↦5;refId=105], java.util.HashMap$TreeNode[↦-1;refId=102]»])),
	14: If(pc=79,UVar(defSites={1},value={java.util.HashMap$TreeNode, null}[↦5;refId=126]),!=,NullExpr(pc=-333),target=16),
	15: Goto(pc=86,target=31),
	16: If(pc=91,UVar(defSites={2},value={java.util.HashMap$TreeNode, null}[↦12;refId=127]),!=,NullExpr(pc=-333),target=18),
	17: Goto(pc=98,target=31),
	18: If(pc=102,UVar(defSites={-4,19},value={java.lang.Class, null}[refId=112; values=«{java.lang.Class, null}[↦106;refId=111], {java.lang.Class, null}[↦-4;refId=104]»]),!=,NullExpr(pc=-333),target=21),
	19: Assignment(pc=106,DVar(useSites={20,18,21,27},value={java.lang.Class, null}[↦106;refId=133],origin=19),StaticFunctionCall(pc=106,java.util.HashMap,isInterface=false,java.lang.Class comparableClassFor(java.lang.Object),(UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103])))),
	20: If(pc=111,UVar(defSites={19},value={java.lang.Class, null}[↦106;refId=133]),==,NullExpr(pc=-333),target=27),
	21: Assignment(pc=118,DVar(useSites={22,23},value=an int,origin=21),StaticFunctionCall(pc=118,java.util.HashMap,isInterface=false,int compareComparables(java.lang.Class,java.lang.Object,java.lang.Object),(UVar(defSites={-4,19},value=java.lang.Class[refId=134; values=«{java.lang.Class, null}[↦-4;refId=104], {java.lang.Class, null}[↦106;refId=133]»]),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={8},value={_ <: java.lang.Object, null}[↦51;refId=128])))),
	22: If(pc=124,UVar(defSites={21},value=an int),==,IntConst(pc=-333,0),target=27),
	23: If(pc=129,UVar(defSites={21},value=an int),>=,IntConst(pc=-333,0),target=25),
	24: Goto(pc=134,target=26),
	25: Nop(pc=137),
	26: Goto(pc=141,target=31),
	27: Assignment(pc=149,DVar(useSites={28,29},value={java.util.HashMap$TreeNode, null}[↦149;refId=142],origin=27),VirtualFunctionCall(pc=149,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode find(int,java.lang.Object,java.lang.Class),UVar(defSites={2},value=java.util.HashMap$TreeNode[↦12;refId=127]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4,19},value={java.lang.Class, null}[refId=136; values=«{java.lang.Class, null}[↦-4;refId=104], {java.lang.Class, null}[↦106;refId=133]»])))),
	28: If(pc=155,UVar(defSites={27},value={java.util.HashMap$TreeNode, null}[↦149;refId=142]),==,NullExpr(pc=-333),target=30),
	29: ReturnValue(pc=160,UVar(defSites={27},value=java.util.HashMap$TreeNode[↦149;refId=142])),
	30: Nop(pc=161),
	31: If(pc=167,UVar(defSites={2,1},value={java.util.HashMap$TreeNode, null}[refId=124; values=«{java.util.HashMap$TreeNode, null}[↦12;refId=106], {java.util.HashMap$TreeNode, null}[↦5;refId=105]»]),!=,NullExpr(pc=-333),target=1),
	32: Assignment(pc=170,DVar(useSites={33},value=null[↦170],origin=32),NullExpr(pc=170)),
	33: ReturnValue(pc=171,UVar(defSites={32},value=null[↦170]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4}
	BB_10: BasicBlock(start=29,end=29) -> {BB_18}
	BB_11: BasicBlock(start=28,end=28) -> {BB_10,BB_1d}
	BB_12: BasicBlock(start=21,end=21) -> {BB_b,BB_15}
	BB_13: BasicBlock(start=32,end=33) -> {BB_18}
	BB_14: BasicBlock(start=17,end=17) -> {BB_1a}
	BB_15: BasicBlock(start=22,end=22) -> {BB_16,BB_1c}
	BB_16: BasicBlock(start=27,end=27) -> {BB_b,BB_11}
	BB_17: BasicBlock(start=18,end=18) -> {BB_12,BB_1e}
	BB_18: ExitNode(normalReturn=true)
	BB_19: BasicBlock(start=16,end=16) -> {BB_14,BB_17}
	BB_1: BasicBlock(start=5,end=5) -> {BB_1a}
	BB_1a: BasicBlock(start=31,end=31) -> {BB_13,BB_4}
	BB_1b: BasicBlock(start=26,end=26) -> {BB_1a}
	BB_1c: BasicBlock(start=23,end=23) -> {BB_d,BB_e}
	BB_1d: BasicBlock(start=30,end=30) -> {BB_1a}
	BB_1e: BasicBlock(start=19,end=19) -> {BB_b,BB_f}
	BB_2: BasicBlock(start=10,end=10) -> {BB_9,BB_3}
	BB_3: BasicBlock(start=14,end=14) -> {BB_c,BB_19}
	BB_4: BasicBlock(start=1,end=4) -> {BB_5,BB_1}
	BB_5: BasicBlock(start=6,end=6) -> {BB_8,BB_a}
	BB_6: BasicBlock(start=13,end=13) -> {BB_18}
	BB_7: BasicBlock(start=12,end=12) -> {BB_6,BB_3}
	BB_8: BasicBlock(start=7,end=7) -> {BB_1a}
	BB_9: BasicBlock(start=11,end=11) -> {BB_b,BB_7}
	BB_a: BasicBlock(start=8,end=9) -> {BB_6,BB_2}
	BB_b: ExitNode(normalReturn=false)
	BB_c: BasicBlock(start=15,end=15) -> {BB_1a}
	BB_d: BasicBlock(start=24,end=24) -> {BB_1b}
	BB_e: BasicBlock(start=25,end=25) -> {BB_1b}
	BB_f: BasicBlock(start=20,end=20) -> {BB_16,BB_12}
))

java.util.HashMap$TreeNode rotateRight(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={20} (origin=-2),
	2: useSites={0,4,18,6,14,1,19,7} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-3},value={java.util.HashMap$TreeNode, null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=20),
	1: Assignment(pc=5,DVar(useSites={8,20,2,18,17,3,19,11,15},value={java.util.HashMap$TreeNode, null}[↦5;refId=104],origin=1),GetField(pc=5,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]))),
	2: If(pc=10,UVar(defSites={1},value={java.util.HashMap$TreeNode, null}[↦5;refId=104]),==,NullExpr(pc=-333),target=20),
	3: Assignment(pc=15,DVar(useSites={4,6,5},value={java.util.HashMap$TreeNode, null}[↦15;refId=105],origin=3),GetField(pc=15,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]))),
	4: PutField(pc=19,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),UVar(defSites={3},value={java.util.HashMap$TreeNode, null}[↦15;refId=105])),
	5: If(pc=25,UVar(defSites={3},value={java.util.HashMap$TreeNode, null}[↦15;refId=105]),==,NullExpr(pc=-333),target=7),
	6: PutField(pc=31,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={3},value=java.util.HashMap$TreeNode[↦15;refId=105]),UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103])),
	7: Assignment(pc=36,DVar(useSites={8,17,9,13,15},value={java.util.HashMap$TreeNode, null}[↦36;refId=106],origin=7),GetField(pc=36,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]))),
	8: PutField(pc=40,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]),UVar(defSites={7},value={java.util.HashMap$TreeNode, null}[↦36;refId=106])),
	9: If(pc=45,UVar(defSites={7},value={java.util.HashMap$TreeNode, null}[↦36;refId=106]),!=,NullExpr(pc=-333),target=13),
	10: Assignment(pc=51,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=51,0)),
	11: PutField(pc=52,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]),UVar(defSites={10},value=int = 0)),
	12: Goto(pc=55,target=18),
	13: Assignment(pc=59,DVar(useSites={14},value={java.util.HashMap$TreeNode, null}[↦59;refId=107],origin=13),GetField(pc=59,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={7},value=java.util.HashMap$TreeNode[↦36;refId=106]))),
	14: If(pc=63,UVar(defSites={13},value={java.util.HashMap$TreeNode, null}[↦59;refId=107]),!=,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),target=17),
	15: PutField(pc=68,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={7},value=java.util.HashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104])),
	16: Goto(pc=71,target=18),
	17: PutField(pc=76,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={7},value=java.util.HashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104])),
	18: PutField(pc=81,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]),UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103])),
	19: PutField(pc=86,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104])),
	20: ReturnValue(pc=90,UVar(defSites={-2,1},value={java.util.HashMap$TreeNode, null}[refId=108; values=«java.util.HashMap$TreeNode[↦5;refId=104], {java.util.HashMap$TreeNode, null}[↦-1;refId=102]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_2}
	BB_1: BasicBlock(start=10,end=12) -> {BB_b}
	BB_2: BasicBlock(start=20,end=20) -> {BB_c}
	BB_3: BasicBlock(start=1,end=2) -> {BB_2,BB_8}
	BB_4: BasicBlock(start=6,end=6) -> {BB_7}
	BB_5: BasicBlock(start=13,end=14) -> {BB_a,BB_6}
	BB_6: BasicBlock(start=17,end=17) -> {BB_b}
	BB_7: BasicBlock(start=7,end=9) -> {BB_1,BB_5}
	BB_8: BasicBlock(start=3,end=5) -> {BB_4,BB_7}
	BB_9: ExitNode(normalReturn=false)
	BB_a: BasicBlock(start=15,end=16) -> {BB_b}
	BB_b: BasicBlock(start=18,end=19) -> {BB_2}
	BB_c: ExitNode(normalReturn=true)
))

java.util.HashMap$TreeNode getTreeNode(int,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={0,2,6} (origin=-1),
	1: useSites={6} (origin=-2),
	2: useSites={6} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={java.util.HashMap$TreeNode, null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value={java.util.HashMap$TreeNode, null}[↦1;refId=104]),==,NullExpr(pc=-333),target=4),
	2: Assignment(pc=8,DVar(useSites={6},value={java.util.HashMap$TreeNode, null}[↦8;refId=106],origin=2),VirtualFunctionCall(pc=8,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode root(),UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),())),
	3: Goto(pc=11,target=5),
	4: Nop(pc=14),
	5: Assignment(pc=17,DVar(useSites={6},value=null[↦17],origin=5),NullExpr(pc=17)),
	6: Assignment(pc=18,DVar(useSites={7},value={java.util.HashMap$TreeNode, null}[↦18;refId=110],origin=6),VirtualFunctionCall(pc=18,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode find(int,java.lang.Object,java.lang.Class),UVar(defSites={2,-1},value={java.util.HashMap$TreeNode, null}[refId=107; values=«{java.util.HashMap$TreeNode, null}[↦8;refId=106], java.util.HashMap$TreeNode[↦-1;refId=102]»]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={5},value=null[↦17])))),
	7: ReturnValue(pc=21,UVar(defSites={6},value={java.util.HashMap$TreeNode, null}[↦18;refId=110]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_6,BB_2}
	BB_1: BasicBlock(start=5,end=6) -> {BB_7,BB_3}
	BB_2: BasicBlock(start=2,end=2) -> {BB_7,BB_4}
	BB_3: BasicBlock(start=7,end=7) -> {BB_5}
	BB_4: BasicBlock(start=3,end=3) -> {BB_1}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=4,end=4) -> {BB_1}
	BB_7: ExitNode(normalReturn=false)
))

java.util.HashMap$TreeNode putTreeVal(java.util.HashMap,java.util.HashMap$Node[],int,java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={32,8,40,56,4,20,52,44,28,2,50,42,49,51,15,47} (origin=-1),
	1: useSites={45} (origin=-2),
	2: useSites={57} (origin=-3),
	3: useSites={12,34,30,9,45} (origin=-4),
	4: useSites={16,24,34,18,22,30,17,37,45} (origin=-5),
	5: useSites={45} (origin=-6)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={24,34,30,21},value=null[↦0],origin=0),NullExpr(pc=0)),
	1: Assignment(pc=3,DVar(useSites={26},value=int = 0,origin=1),IntConst(pc=3,0)),
	2: Assignment(pc=7,DVar(useSites={3},value={java.util.HashMap$TreeNode, null}[↦7;refId=107],origin=2),GetField(pc=7,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	3: If(pc=10,UVar(defSites={2},value={java.util.HashMap$TreeNode, null}[↦7;refId=107]),==,NullExpr(pc=-333),target=6),
	4: Assignment(pc=14,DVar(useSites={32,8,40,56,20,52,44,28,50,42,49,51,15,47},value={java.util.HashMap$TreeNode, null}[↦14;refId=109],origin=4),VirtualFunctionCall(pc=14,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode root(),UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),())),
	5: Goto(pc=17,target=7),
	6: Nop(pc=20),
	7: Nop(pc=21),
	8: Assignment(pc=29,DVar(useSites={12,9},value=an int,origin=8),GetField(pc=29,java.util.HashMap$TreeNode,hash,int,UVar(defSites={40,4,42,-1},value={java.util.HashMap$TreeNode, null}[refId=198; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=168], {java.util.HashMap$TreeNode, null}[↦212;refId=171], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	9: If(pc=36,UVar(defSites={8},value=an int),<=,UVar(defSites={-4},value=an int),target=12),
	10: Assignment(pc=39,DVar(useSites={46,39},value=int = -1,origin=10),IntConst(pc=39,-1)),
	11: Goto(pc=42,target=39),
	12: If(pc=48,UVar(defSites={8},value=an int),>=,UVar(defSites={-4},value=an int),target=15),
	13: Assignment(pc=51,DVar(useSites={46,39},value=int = 1,origin=13),IntConst(pc=51,1)),
	14: Goto(pc=54,target=39),
	15: Assignment(pc=59,DVar(useSites={16,24,18,37},value={_ <: java.lang.Object, null}[↦59;refId=217],origin=15),GetField(pc=59,java.util.HashMap$TreeNode,key,java.lang.Object,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=198; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=168], {java.util.HashMap$TreeNode, null}[↦212;refId=171], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	16: If(pc=67,UVar(defSites={15},value={_ <: java.lang.Object, null}[↦59;refId=217]),==,UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105]),target=20),
	17: If(pc=72,UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105]),==,NullExpr(pc=-333),target=21),
	18: Assignment(pc=79,DVar(useSites={19},value=int ∈ [0,1],origin=18),VirtualFunctionCall(pc=79,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-5},value=_ <: java.lang.Object[↦-5;refId=105]),(UVar(defSites={15},value={_ <: java.lang.Object, null}[↦59;refId=217])))),
	19: If(pc=82,UVar(defSites={18},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=21),
	20: ReturnValue(pc=87,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=143; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»])),
	21: If(pc=90,UVar(defSites={0,22},value={java.lang.Class, null}[refId=123; values=«null[↦0], {java.lang.Class, null}[↦95;refId=115]»]),!=,NullExpr(pc=-333),target=24),
	22: Assignment(pc=95,DVar(useSites={24,34,30,21,23},value={java.lang.Class, null}[↦95;refId=234],origin=22),StaticFunctionCall(pc=95,java.util.HashMap,isInterface=false,java.lang.Class comparableClassFor(java.lang.Object),(UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105])))),
	23: If(pc=101,UVar(defSites={22},value={java.lang.Class, null}[↦95;refId=234]),==,NullExpr(pc=-333),target=26),
	24: Assignment(pc=110,DVar(useSites={46,25,39},value=an int,origin=24),StaticFunctionCall(pc=110,java.util.HashMap,isInterface=false,int compareComparables(java.lang.Class,java.lang.Object,java.lang.Object),(UVar(defSites={0,22},value=java.lang.Class[↦95;refId=234]),UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105]),UVar(defSites={15},value={_ <: java.lang.Object, null}[↦59;refId=217])))),
	25: If(pc=116,UVar(defSites={24},value=an int),!=,IntConst(pc=-333,0),target=39),
	26: If(pc=121,UVar(defSites={1,27},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=37),
	27: Assignment(pc=124,DVar(useSites={26},value=int = 1,origin=27),IntConst(pc=124,1)),
	28: Assignment(pc=129,DVar(useSites={30,29},value={java.util.HashMap$TreeNode, null}[↦129;refId=245],origin=28),GetField(pc=129,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=235; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=168], {java.util.HashMap$TreeNode, null}[↦212;refId=171], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	29: If(pc=135,UVar(defSites={28},value={java.util.HashMap$TreeNode, null}[↦129;refId=245]),==,NullExpr(pc=-333),target=32),
	30: Assignment(pc=145,DVar(useSites={36,31},value={java.util.HashMap$TreeNode, null}[↦145;refId=248],origin=30),VirtualFunctionCall(pc=145,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode find(int,java.lang.Object,java.lang.Class),UVar(defSites={28},value=java.util.HashMap$TreeNode[↦129;refId=245]),(UVar(defSites={-4},value=an int),UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105]),UVar(defSites={0,22},value={java.lang.Class, null}[↦95;refId=234])))),
	31: If(pc=151,UVar(defSites={30},value={java.util.HashMap$TreeNode, null}[↦145;refId=248]),!=,NullExpr(pc=-333),target=36),
	32: Assignment(pc=156,DVar(useSites={34,33},value={java.util.HashMap$TreeNode, null}[↦156;refId=210],origin=32),GetField(pc=156,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=189; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	33: If(pc=162,UVar(defSites={32},value={java.util.HashMap$TreeNode, null}[↦156;refId=210]),==,NullExpr(pc=-333),target=37),
	34: Assignment(pc=172,DVar(useSites={36,35},value={java.util.HashMap$TreeNode, null}[↦172;refId=213],origin=34),VirtualFunctionCall(pc=172,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode find(int,java.lang.Object,java.lang.Class),UVar(defSites={32},value=java.util.HashMap$TreeNode[↦156;refId=210]),(UVar(defSites={-4},value=an int),UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105]),UVar(defSites={0,22},value={java.lang.Class, null}[↦95;refId=115])))),
	35: If(pc=178,UVar(defSites={34},value={java.util.HashMap$TreeNode, null}[↦172;refId=213]),==,NullExpr(pc=-333),target=37),
	36: ReturnValue(pc=183,UVar(defSites={34,30},value=java.util.HashMap$TreeNode[refId=132; values=«java.util.HashMap$TreeNode[↦145;refId=121], java.util.HashMap$TreeNode[↦172;refId=131]»])),
	37: Assignment(pc=188,DVar(useSites={46,39},value=an int,origin=37),StaticFunctionCall(pc=188,java.util.HashMap$TreeNode,isInterface=false,int tieBreakOrder(java.lang.Object,java.lang.Object),(UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105]),UVar(defSites={15},value={_ <: java.lang.Object, null}[↦59;refId=142])))),
	38: Nop(pc=191),
	39: If(pc=199,UVar(defSites={24,10,37,13},value=an int),>,IntConst(pc=-333,0),target=42),
	40: Assignment(pc=204,DVar(useSites={32,8,20,52,44,28,50,42,49,41,51,43,15,47},value={java.util.HashMap$TreeNode, null}[↦204;refId=168],origin=40),GetField(pc=204,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=148; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	41: Goto(pc=207,target=43),
	42: Assignment(pc=212,DVar(useSites={32,8,40,20,52,44,28,50,49,51,43,15,47},value={java.util.HashMap$TreeNode, null}[refId=172; values=«{java.util.HashMap$TreeNode, null}[↦204;refId=168], {java.util.HashMap$TreeNode, null}[↦212;refId=171]»],origin=42),GetField(pc=212,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=148; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	43: If(pc=218,UVar(defSites={40,42},value={java.util.HashMap$TreeNode, null}[refId=172; values=«{java.util.HashMap$TreeNode, null}[↦204;refId=168], {java.util.HashMap$TreeNode, null}[↦212;refId=171]»]),!=,NullExpr(pc=-333),target=8),
	44: Assignment(pc=223,DVar(useSites={54,53,45,55},value={_ <: java.util.HashMap$Node, null}[↦223;refId=199],origin=44),GetField(pc=223,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=170; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»]))),
	45: Assignment(pc=236,DVar(useSites={56,52,50,49,51,55,47},value={java.util.HashMap$TreeNode, null}[↦236;refId=202],origin=45),VirtualFunctionCall(pc=236,java.util.HashMap,isInterface=false,java.util.HashMap$TreeNode newTreeNode(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103]),(UVar(defSites={-4},value=an int),UVar(defSites={-5},value={_ <: java.lang.Object, null}[↦-5;refId=105]),UVar(defSites={-6},value={_ <: java.lang.Object, null}[↦-6;refId=106]),UVar(defSites={44},value={_ <: java.util.HashMap$Node, null}[↦223;refId=199])))),
	46: If(pc=243,UVar(defSites={24,10,37,13},value=an int),>,IntConst(pc=-333,0),target=49),
	47: PutField(pc=250,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=170; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»]),UVar(defSites={45},value={java.util.HashMap$TreeNode, null}[↦236;refId=202])),
	48: Goto(pc=253,target=50),
	49: PutField(pc=260,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=170; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»]),UVar(defSites={45},value={java.util.HashMap$TreeNode, null}[↦236;refId=202])),
	50: PutField(pc=267,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=203; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»]),UVar(defSites={45},value={java.util.HashMap$TreeNode, null}[↦236;refId=202])),
	51: PutField(pc=277,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={45},value={java.util.HashMap$TreeNode, null}[↦236;refId=202]),UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=203; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»])),
	52: PutField(pc=280,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={45},value=java.util.HashMap$TreeNode[↦236;refId=202]),UVar(defSites={40,4,42,-1},value=java.util.HashMap$TreeNode[refId=203; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], {java.util.HashMap$TreeNode, null}[↦204;refId=116], {java.util.HashMap$TreeNode, null}[↦212;refId=117], java.util.HashMap$TreeNode[↦-1;refId=102]»])),
	53: If(pc=285,UVar(defSites={44},value={_ <: java.util.HashMap$Node, null}[↦223;refId=199]),==,NullExpr(pc=-333),target=56),
	54: Checkcast(pc=290,UVar(defSites={44},value=_ <: java.util.HashMap$Node[↦223;refId=199]),java.util.HashMap$TreeNode),
	55: PutField(pc=295,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={44},value=java.util.HashMap$TreeNode[↦223;refId=228]),UVar(defSites={45},value=java.util.HashMap$TreeNode[↦236;refId=202])),
	56: Assignment(pc=303,DVar(useSites={57},value={java.util.HashMap$TreeNode, null}[↦303;refId=238],origin=56),StaticFunctionCall(pc=303,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode balanceInsertion(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={4,-1},value={java.util.HashMap$TreeNode, null}[refId=110; values=«{java.util.HashMap$TreeNode, null}[↦14;refId=109], java.util.HashMap$TreeNode[↦-1;refId=102]»]),UVar(defSites={45},value=java.util.HashMap$TreeNode[↦236;refId=202])))),
	57: StaticMethodCall(pc=306,java.util.HashMap$TreeNode,isInterface=false,void moveRootToFront(java.util.HashMap$Node[],java.util.HashMap$TreeNode),(UVar(defSites={-3},value={_ <: java.util.HashMap$Node[], null}[↦-3;refId=104]),UVar(defSites={56},value={java.util.HashMap$TreeNode, null}[↦303;refId=238]))),
	58: Assignment(pc=309,DVar(useSites={59},value=null[↦309],origin=58),NullExpr(pc=309)),
	59: ReturnValue(pc=310,UVar(defSites={58},value=null[↦309]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_3,BB_2b}
	BB_10: BasicBlock(start=57,end=57) -> {BB_2c,BB_27}
	BB_11: BasicBlock(start=38,end=38) -> {BB_1d}
	BB_12: BasicBlock(start=21,end=21) -> {BB_b,BB_16}
	BB_13: BasicBlock(start=17,end=17) -> {BB_12,BB_1e}
	BB_14: BasicBlock(start=32,end=33) -> {BB_c,BB_15}
	BB_15: BasicBlock(start=34,end=34) -> {BB_2c,BB_6}
	BB_16: BasicBlock(start=22,end=22) -> {BB_2c,BB_25}
	BB_17: BasicBlock(start=44,end=45) -> {BB_2c,BB_f}
	BB_18: BasicBlock(start=27,end=29) -> {BB_29,BB_14}
	BB_19: BasicBlock(start=12,end=12) -> {BB_2e,BB_5}
	BB_1: BasicBlock(start=5,end=5) -> {BB_1c}
	BB_1a: BasicBlock(start=54,end=54) -> {BB_2c,BB_24}
	BB_1b: BasicBlock(start=49,end=49) -> {BB_20}
	BB_1c: BasicBlock(start=7,end=7) -> {BB_26}
	BB_1d: BasicBlock(start=39,end=39) -> {BB_a,BB_22}
	BB_1e: BasicBlock(start=18,end=18) -> {BB_2c,BB_2a}
	BB_1f: ExitNode(normalReturn=true)
	BB_20: BasicBlock(start=50,end=51) -> {BB_2c,BB_2}
	BB_21: BasicBlock(start=31,end=31) -> {BB_14,BB_28}
	BB_22: BasicBlock(start=40,end=41) -> {BB_7}
	BB_23: BasicBlock(start=26,end=26) -> {BB_c,BB_18}
	BB_24: BasicBlock(start=55,end=55) -> {BB_9}
	BB_25: BasicBlock(start=23,end=23) -> {BB_b,BB_23}
	BB_26: BasicBlock(start=8,end=8) -> {BB_2c,BB_4}
	BB_27: BasicBlock(start=58,end=59) -> {BB_1f}
	BB_28: BasicBlock(start=36,end=36) -> {BB_1f}
	BB_29: BasicBlock(start=30,end=30) -> {BB_2c,BB_21}
	BB_2: BasicBlock(start=52,end=53) -> {BB_1a,BB_9}
	BB_2a: BasicBlock(start=19,end=19) -> {BB_12,BB_e}
	BB_2b: BasicBlock(start=4,end=4) -> {BB_2c,BB_1}
	BB_2c: ExitNode(normalReturn=false)
	BB_2d: BasicBlock(start=47,end=48) -> {BB_20}
	BB_2e: BasicBlock(start=15,end=16) -> {BB_13,BB_e}
	BB_3: BasicBlock(start=6,end=6) -> {BB_1c}
	BB_4: BasicBlock(start=9,end=9) -> {BB_19,BB_8}
	BB_5: BasicBlock(start=13,end=14) -> {BB_1d}
	BB_6: BasicBlock(start=35,end=35) -> {BB_c,BB_28}
	BB_7: BasicBlock(start=43,end=43) -> {BB_17,BB_26}
	BB_8: BasicBlock(start=10,end=11) -> {BB_1d}
	BB_9: BasicBlock(start=56,end=56) -> {BB_2c,BB_10}
	BB_a: BasicBlock(start=42,end=42) -> {BB_7}
	BB_b: BasicBlock(start=24,end=24) -> {BB_2c,BB_d}
	BB_c: BasicBlock(start=37,end=37) -> {BB_2c,BB_11}
	BB_d: BasicBlock(start=25,end=25) -> {BB_1d,BB_23}
	BB_e: BasicBlock(start=20,end=20) -> {BB_1f}
	BB_f: BasicBlock(start=46,end=46) -> {BB_1b,BB_2d}
))

java.util.HashMap$TreeNode rotateLeft(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={20} (origin=-2),
	2: useSites={0,4,18,6,14,1,19,7} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-3},value={java.util.HashMap$TreeNode, null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=20),
	1: Assignment(pc=5,DVar(useSites={8,20,2,18,17,3,19,11,15},value={java.util.HashMap$TreeNode, null}[↦5;refId=104],origin=1),GetField(pc=5,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]))),
	2: If(pc=10,UVar(defSites={1},value={java.util.HashMap$TreeNode, null}[↦5;refId=104]),==,NullExpr(pc=-333),target=20),
	3: Assignment(pc=15,DVar(useSites={4,6,5},value={java.util.HashMap$TreeNode, null}[↦15;refId=105],origin=3),GetField(pc=15,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]))),
	4: PutField(pc=19,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),UVar(defSites={3},value={java.util.HashMap$TreeNode, null}[↦15;refId=105])),
	5: If(pc=25,UVar(defSites={3},value={java.util.HashMap$TreeNode, null}[↦15;refId=105]),==,NullExpr(pc=-333),target=7),
	6: PutField(pc=31,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={3},value=java.util.HashMap$TreeNode[↦15;refId=105]),UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103])),
	7: Assignment(pc=36,DVar(useSites={8,17,9,13,15},value={java.util.HashMap$TreeNode, null}[↦36;refId=106],origin=7),GetField(pc=36,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]))),
	8: PutField(pc=40,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]),UVar(defSites={7},value={java.util.HashMap$TreeNode, null}[↦36;refId=106])),
	9: If(pc=45,UVar(defSites={7},value={java.util.HashMap$TreeNode, null}[↦36;refId=106]),!=,NullExpr(pc=-333),target=13),
	10: Assignment(pc=51,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=51,0)),
	11: PutField(pc=52,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]),UVar(defSites={10},value=int = 0)),
	12: Goto(pc=55,target=18),
	13: Assignment(pc=59,DVar(useSites={14},value={java.util.HashMap$TreeNode, null}[↦59;refId=107],origin=13),GetField(pc=59,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={7},value=java.util.HashMap$TreeNode[↦36;refId=106]))),
	14: If(pc=63,UVar(defSites={13},value={java.util.HashMap$TreeNode, null}[↦59;refId=107]),!=,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),target=17),
	15: PutField(pc=68,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={7},value=java.util.HashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104])),
	16: Goto(pc=71,target=18),
	17: PutField(pc=76,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={7},value=java.util.HashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104])),
	18: PutField(pc=81,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104]),UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103])),
	19: PutField(pc=86,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-3},value=java.util.HashMap$TreeNode[↦-2;refId=103]),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=104])),
	20: ReturnValue(pc=90,UVar(defSites={-2,1},value={java.util.HashMap$TreeNode, null}[refId=108; values=«java.util.HashMap$TreeNode[↦5;refId=104], {java.util.HashMap$TreeNode, null}[↦-1;refId=102]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_2}
	BB_1: BasicBlock(start=10,end=12) -> {BB_b}
	BB_2: BasicBlock(start=20,end=20) -> {BB_c}
	BB_3: BasicBlock(start=1,end=2) -> {BB_2,BB_8}
	BB_4: BasicBlock(start=6,end=6) -> {BB_7}
	BB_5: BasicBlock(start=13,end=14) -> {BB_a,BB_6}
	BB_6: BasicBlock(start=17,end=17) -> {BB_b}
	BB_7: BasicBlock(start=7,end=9) -> {BB_1,BB_5}
	BB_8: BasicBlock(start=3,end=5) -> {BB_4,BB_7}
	BB_9: ExitNode(normalReturn=false)
	BB_a: BasicBlock(start=15,end=16) -> {BB_b}
	BB_b: BasicBlock(start=18,end=19) -> {BB_2}
	BB_c: ExitNode(normalReturn=true)
))

void removeTreeNode(java.util.HashMap,java.util.HashMap$Node[],boolean)
AITACode(params=(Parameters(
	0: useSites={96,88,68,36,100,52,12,108,92,66,98,10,106,122,6,102,118,110,65,49,113,89,37,101,45,61,51,75,107,59,103,87,55,47,95} (origin=-1),
	1: useSites={33} (origin=-2),
	2: useSites={0,8,34,122,14,1} (origin=-3),
	3: useSites={26,121} (origin=-4)
)),stmts=(
	0: If(pc=1,UVar(defSites={-3},value={_ <: java.util.HashMap$Node[], null}[↦-3;refId=104]),==,NullExpr(pc=-333),target=3),
	1: Assignment(pc=5,DVar(useSites={2,5},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=5,UVar(defSites={-3},value=_ <: java.util.HashMap$Node[][↦-3;refId=104]))),
	2: If(pc=9,UVar(defSites={1},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=4),
	3: Return(pc=12),
	4: Assignment(pc=15,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=15,1)),
	5: Assignment(pc=16,DVar(useSites={7},value=int ∈ [0,2147483646],origin=5),BinaryExpr(pc=16,ComputationalTypeInt,UVar(defSites={1},value=int ∈ [1,2147483647]),-,UVar(defSites={4},value=int = 1))),
	6: Assignment(pc=18,DVar(useSites={7},value=an int,origin=6),GetField(pc=18,java.util.HashMap$TreeNode,hash,int,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	7: Assignment(pc=21,DVar(useSites={8,34,14},value=int ∈ [0,2147483646],origin=7),BinaryExpr(pc=21,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,2147483646]),&,UVar(defSites={6},value=an int))),
	8: Assignment(pc=27,DVar(useSites={106,122,33,9,25,21,29,19,27,23},value={_ <: java.util.HashMap$Node, null}[↦27;refId=106],origin=8),ArrayLoad(pc=27,UVar(defSites={7},value=int ∈ [0,2147483646]),UVar(defSites={-3},value=_ <: java.util.HashMap$Node[][↦-3;refId=104]))),
	9: Checkcast(pc=28,UVar(defSites={8},value={_ <: java.util.HashMap$Node, null}[↦27;refId=106]),java.util.HashMap$TreeNode),
	10: Assignment(pc=38,DVar(useSites={16,18,14,33,17,19,11},value={_ <: java.util.HashMap$Node, null}[↦38;refId=109],origin=10),GetField(pc=38,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	11: Checkcast(pc=41,UVar(defSites={10},value={_ <: java.util.HashMap$Node, null}[↦38;refId=109]),java.util.HashMap$TreeNode),
	12: Assignment(pc=47,DVar(useSites={16,18,13},value={java.util.HashMap$TreeNode, null}[↦47;refId=112],origin=12),GetField(pc=47,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	13: If(pc=54,UVar(defSites={12},value={java.util.HashMap$TreeNode, null}[↦47;refId=112]),!=,NullExpr(pc=-333),target=16),
	14: ArrayStore(pc=65,UVar(defSites={-3},value=_ <: java.util.HashMap$Node[][↦-3;refId=104]),UVar(defSites={7},value=int ∈ [0,2147483646]),UVar(defSites={10},value={java.util.HashMap$TreeNode, null}[↦38;refId=110])),
	15: Goto(pc=66,target=17),
	16: PutField(pc=73,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={12},value=java.util.HashMap$TreeNode[↦47;refId=112]),UVar(defSites={10},value={java.util.HashMap$TreeNode, null}[↦38;refId=110])),
	17: If(pc=78,UVar(defSites={10},value={java.util.HashMap$TreeNode, null}[↦38;refId=110]),==,NullExpr(pc=-333),target=19),
	18: PutField(pc=85,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={10},value=java.util.HashMap$TreeNode[↦38;refId=110]),UVar(defSites={12},value={java.util.HashMap$TreeNode, null}[↦47;refId=112])),
	19: If(pc=90,UVar(defSites={8,10},value={java.util.HashMap$TreeNode, null}[refId=117; values=«{java.util.HashMap$TreeNode, null}[↦38;refId=110], {java.util.HashMap$TreeNode, null}[↦27;refId=107]»]),!=,NullExpr(pc=-333),target=21),
	20: Return(pc=93),
	21: Assignment(pc=96,DVar(useSites={22},value={java.util.HashMap$TreeNode, null}[↦96;refId=118],origin=21),GetField(pc=96,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={8},value={java.util.HashMap$TreeNode, null}[↦27;refId=107]))),
	22: If(pc=99,UVar(defSites={21},value={java.util.HashMap$TreeNode, null}[↦96;refId=118]),==,NullExpr(pc=-333),target=25),
	23: Assignment(pc=104,DVar(useSites={106,122,25,29,27},value={java.util.HashMap$TreeNode, null}[↦104;refId=122],origin=23),VirtualFunctionCall(pc=104,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode root(),UVar(defSites={8},value=java.util.HashMap$TreeNode[↦27;refId=107]),())),
	24: Nop(pc=107),
	25: If(pc=111,UVar(defSites={8,23},value={java.util.HashMap$TreeNode, null}[refId=123; values=«java.util.HashMap$TreeNode[↦27;refId=107], {java.util.HashMap$TreeNode, null}[↦104;refId=122]»]),==,NullExpr(pc=-333),target=33),
	26: If(pc=115,UVar(defSites={-4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=36),
	27: Assignment(pc=120,DVar(useSites={28},value={java.util.HashMap$TreeNode, null}[↦120;refId=124],origin=27),GetField(pc=120,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={8,23},value=java.util.HashMap$TreeNode[refId=123; values=«java.util.HashMap$TreeNode[↦27;refId=107], {java.util.HashMap$TreeNode, null}[↦104;refId=122]»]))),
	28: If(pc=123,UVar(defSites={27},value={java.util.HashMap$TreeNode, null}[↦120;refId=124]),==,NullExpr(pc=-333),target=33),
	29: Assignment(pc=128,DVar(useSites={30,31},value={java.util.HashMap$TreeNode, null}[↦128;refId=125],origin=29),GetField(pc=128,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={8,23},value=java.util.HashMap$TreeNode[refId=123; values=«java.util.HashMap$TreeNode[↦27;refId=107], {java.util.HashMap$TreeNode, null}[↦104;refId=122]»]))),
	30: If(pc=134,UVar(defSites={29},value={java.util.HashMap$TreeNode, null}[↦128;refId=125]),==,NullExpr(pc=-333),target=33),
	31: Assignment(pc=139,DVar(useSites={32},value={java.util.HashMap$TreeNode, null}[↦139;refId=126],origin=31),GetField(pc=139,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={29},value=java.util.HashMap$TreeNode[↦128;refId=125]))),
	32: If(pc=142,UVar(defSites={31},value={java.util.HashMap$TreeNode, null}[↦139;refId=126]),!=,NullExpr(pc=-333),target=36),
	33: Assignment(pc=151,DVar(useSites={34},value={_ <: java.util.HashMap$Node, null}[↦151;refId=128],origin=33),VirtualFunctionCall(pc=151,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$Node untreeify(java.util.HashMap),UVar(defSites={8,10},value=java.util.HashMap$TreeNode[refId=120; values=«{java.util.HashMap$TreeNode, null}[↦38;refId=110], java.util.HashMap$TreeNode[↦27;refId=107]»]),(UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103])))),
	34: ArrayStore(pc=154,UVar(defSites={-3},value=_ <: java.util.HashMap$Node[][↦-3;refId=104]),UVar(defSites={7},value=int ∈ [0,2147483646]),UVar(defSites={33},value={_ <: java.util.HashMap$Node, null}[↦151;refId=128])),
	35: Return(pc=155),
	36: Assignment(pc=160,DVar(useSites={96,92,98,82,106,122,70,38,89,69,107,87},value={java.util.HashMap$TreeNode, null}[↦160;refId=131],origin=36),GetField(pc=160,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	37: Assignment(pc=166,DVar(useSites={96,48,84,52,76,44,92,98,50,106,58,122,70,54,78,46,62,41,89,69,51,107,71,39,87,63},value={java.util.HashMap$TreeNode, null}[↦166;refId=132],origin=37),GetField(pc=166,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	38: If(pc=173,UVar(defSites={36},value={java.util.HashMap$TreeNode, null}[↦160;refId=131]),==,NullExpr(pc=-333),target=82),
	39: If(pc=178,UVar(defSites={37},value={java.util.HashMap$TreeNode, null}[↦166;refId=132]),==,NullExpr(pc=-333),target=82),
	40: Nop(pc=181),
	41: Assignment(pc=187,DVar(useSites={48,52,76,44,50,42,106,58,122,70,54,78,46,62,69,51,71,63},value={java.util.HashMap$TreeNode, null}[↦187;refId=143],origin=41),GetField(pc=187,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]))),
	42: If(pc=193,UVar(defSites={41},value={java.util.HashMap$TreeNode, null}[↦187;refId=143]),==,NullExpr(pc=-333),target=44),
	43: Goto(pc=200,target=41),
	44: Assignment(pc=205,DVar(useSites={47},value=int ∈ [0,1],origin=44),GetField(pc=205,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]))),
	45: Assignment(pc=214,DVar(useSites={46},value=int ∈ [0,1],origin=45),GetField(pc=214,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	46: PutField(pc=217,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]),UVar(defSites={45},value=int ∈ [0,1])),
	47: PutField(pc=224,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={44},value=int ∈ [0,1])),
	48: Assignment(pc=229,DVar(useSites={96,68,92,66,98,106,122,89,67,107,87,79},value={java.util.HashMap$TreeNode, null}[↦229;refId=145],origin=48),GetField(pc=229,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]))),
	49: Assignment(pc=236,DVar(useSites={72,76,74,78,71},value={java.util.HashMap$TreeNode, null}[↦236;refId=146],origin=49),GetField(pc=236,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	50: If(pc=245,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]),!=,UVar(defSites={37},value=java.util.HashMap$TreeNode[↦166;refId=132]),target=54),
	51: PutField(pc=252,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»])),
	52: PutField(pc=259,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]),UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102])),
	53: Goto(pc=262,target=64),
	54: Assignment(pc=267,DVar(useSites={56,57,61,59,55},value={java.util.HashMap$TreeNode, null}[↦267;refId=147],origin=54),GetField(pc=267,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]))),
	55: PutField(pc=277,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={54},value={java.util.HashMap$TreeNode, null}[↦267;refId=147])),
	56: If(pc=280,UVar(defSites={54},value={java.util.HashMap$TreeNode, null}[↦267;refId=147]),==,NullExpr(pc=-333),target=62),
	57: Assignment(pc=287,DVar(useSites={58},value={java.util.HashMap$TreeNode, null}[↦287;refId=148],origin=57),GetField(pc=287,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={54},value=java.util.HashMap$TreeNode[↦267;refId=147]))),
	58: If(pc=290,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]),!=,UVar(defSites={57},value={java.util.HashMap$TreeNode, null}[↦287;refId=148]),target=61),
	59: PutField(pc=297,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={54},value=java.util.HashMap$TreeNode[↦267;refId=147]),UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102])),
	60: Goto(pc=300,target=62),
	61: PutField(pc=307,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={54},value=java.util.HashMap$TreeNode[↦267;refId=147]),UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102])),
	62: PutField(pc=315,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]),UVar(defSites={37},value=java.util.HashMap$TreeNode[↦166;refId=132])),
	63: PutField(pc=325,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={37},value=java.util.HashMap$TreeNode[↦166;refId=132]),UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»])),
	64: Assignment(pc=330,DVar(useSites={65},value=null[↦330],origin=64),NullExpr(pc=330)),
	65: PutField(pc=331,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={64},value=null[↦330])),
	66: PutField(pc=339,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={48},value={java.util.HashMap$TreeNode, null}[↦229;refId=145])),
	67: If(pc=342,UVar(defSites={48},value={java.util.HashMap$TreeNode, null}[↦229;refId=145]),==,NullExpr(pc=-333),target=69),
	68: PutField(pc=349,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={48},value=java.util.HashMap$TreeNode[↦229;refId=145]),UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102])),
	69: PutField(pc=357,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]),UVar(defSites={36},value=java.util.HashMap$TreeNode[↦160;refId=131])),
	70: PutField(pc=367,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={36},value=java.util.HashMap$TreeNode[↦160;refId=131]),UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»])),
	71: PutField(pc=375,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»]),UVar(defSites={49},value={java.util.HashMap$TreeNode, null}[↦236;refId=146])),
	72: If(pc=378,UVar(defSites={49},value={java.util.HashMap$TreeNode, null}[↦236;refId=146]),!=,NullExpr(pc=-333),target=74),
	73: Goto(pc=385,target=79),
	74: Assignment(pc=392,DVar(useSites={75},value={java.util.HashMap$TreeNode, null}[↦392;refId=160],origin=74),GetField(pc=392,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={49},value=java.util.HashMap$TreeNode[↦236;refId=146]))),
	75: If(pc=395,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),!=,UVar(defSites={74},value={java.util.HashMap$TreeNode, null}[↦392;refId=160]),target=78),
	76: PutField(pc=402,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={49},value=java.util.HashMap$TreeNode[↦236;refId=146]),UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»])),
	77: Goto(pc=405,target=79),
	78: PutField(pc=412,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={49},value=java.util.HashMap$TreeNode[↦236;refId=146]),UVar(defSites={41,37},value=java.util.HashMap$TreeNode[refId=136; values=«java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦187;refId=135]»])),
	79: If(pc=417,UVar(defSites={48},value={java.util.HashMap$TreeNode, null}[↦229;refId=145]),==,NullExpr(pc=-333),target=81),
	80: Goto(pc=424,target=87),
	81: Goto(pc=431,target=87),
	82: If(pc=436,UVar(defSites={36},value={java.util.HashMap$TreeNode, null}[↦160;refId=131]),==,NullExpr(pc=-333),target=84),
	83: Goto(pc=443,target=87),
	84: If(pc=448,UVar(defSites={37},value={java.util.HashMap$TreeNode, null}[↦166;refId=132]),==,NullExpr(pc=-333),target=86),
	85: Goto(pc=455,target=87),
	86: Nop(pc=458),
	87: If(pc=466,UVar(defSites={48,36,37,-1},value=java.util.HashMap$TreeNode[refId=173; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145]»]),==,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),target=103),
	88: Assignment(pc=473,DVar(useSites={96,98,90,94,89},value={java.util.HashMap$TreeNode, null}[↦473;refId=178],origin=88),GetField(pc=473,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	89: PutField(pc=477,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={48,36,37,-1},value=java.util.HashMap$TreeNode[refId=173; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145]»]),UVar(defSites={88},value={java.util.HashMap$TreeNode, null}[↦473;refId=178])),
	90: If(pc=484,UVar(defSites={88},value={java.util.HashMap$TreeNode, null}[↦473;refId=178]),!=,NullExpr(pc=-333),target=94),
	91: Assignment(pc=492,DVar(useSites={92},value=int = 0,origin=91),IntConst(pc=492,0)),
	92: PutField(pc=493,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={48,36,37,-1},value=java.util.HashMap$TreeNode[refId=173; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145]»]),UVar(defSites={91},value=int = 0)),
	93: Goto(pc=496,target=99),
	94: Assignment(pc=503,DVar(useSites={95},value={java.util.HashMap$TreeNode, null}[↦503;refId=181],origin=94),GetField(pc=503,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={88},value=java.util.HashMap$TreeNode[↦473;refId=178]))),
	95: If(pc=506,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),!=,UVar(defSites={94},value={java.util.HashMap$TreeNode, null}[↦503;refId=181]),target=98),
	96: PutField(pc=513,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={88},value=java.util.HashMap$TreeNode[↦473;refId=178]),UVar(defSites={48,36,37,-1},value=java.util.HashMap$TreeNode[refId=173; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145]»])),
	97: Goto(pc=516,target=99),
	98: PutField(pc=523,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={88},value=java.util.HashMap$TreeNode[↦473;refId=178]),UVar(defSites={48,36,37,-1},value=java.util.HashMap$TreeNode[refId=173; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145]»])),
	99: Assignment(pc=532,DVar(useSites={100,102,101},value=null[↦532],origin=99),NullExpr(pc=532)),
	100: PutField(pc=534,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={99},value=null[↦532])),
	101: PutField(pc=538,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={99},value=null[↦532])),
	102: PutField(pc=541,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={99},value=null[↦532])),
	103: Assignment(pc=546,DVar(useSites={104},value=int ∈ [0,1],origin=103),GetField(pc=546,java.util.HashMap$TreeNode,red,boolean,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	104: If(pc=549,UVar(defSites={103},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=106),
	105: Goto(pc=554,target=107),
	106: Assignment(pc=561,DVar(useSites={122},value={java.util.HashMap$TreeNode, null}[refId=206; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], {java.util.HashMap$TreeNode, null}[↦104;refId=122], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145], {java.util.HashMap$TreeNode, null}[↦561;refId=205], java.util.HashMap$TreeNode[↦27;refId=107], java.util.HashMap$TreeNode[↦187;refId=135]»],origin=106),StaticFunctionCall(pc=561,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode balanceDeletion(java.util.HashMap$TreeNode,java.util.HashMap$TreeNode),(UVar(defSites={48,8,36,41,37,23,-1},value=java.util.HashMap$TreeNode[refId=192; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], {java.util.HashMap$TreeNode, null}[↦104;refId=122], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145], java.util.HashMap$TreeNode[↦27;refId=107], java.util.HashMap$TreeNode[↦187;refId=135]»]),UVar(defSites={48,36,37,-1},value=java.util.HashMap$TreeNode[refId=177; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145]»])))),
	107: If(pc=570,UVar(defSites={48,36,37,-1},value=java.util.HashMap$TreeNode[refId=187; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], java.util.HashMap$TreeNode[↦-1;refId=102], java.util.HashMap$TreeNode[↦229;refId=145]»]),!=,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),target=121),
	108: Assignment(pc=575,DVar(useSites={112,120,117,115,111},value={java.util.HashMap$TreeNode, null}[↦575;refId=210],origin=108),GetField(pc=575,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]))),
	109: Assignment(pc=582,DVar(useSites={110},value=null[↦582],origin=109),NullExpr(pc=582)),
	110: PutField(pc=583,java.util.HashMap$TreeNode,parent,java.util.HashMap$TreeNode,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),UVar(defSites={109},value=null[↦582])),
	111: If(pc=588,UVar(defSites={108},value={java.util.HashMap$TreeNode, null}[↦575;refId=210]),==,NullExpr(pc=-333),target=121),
	112: Assignment(pc=595,DVar(useSites={113},value={java.util.HashMap$TreeNode, null}[↦595;refId=212],origin=112),GetField(pc=595,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={108},value=java.util.HashMap$TreeNode[↦575;refId=210]))),
	113: If(pc=598,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),!=,UVar(defSites={112},value={java.util.HashMap$TreeNode, null}[↦595;refId=212]),target=117),
	114: Assignment(pc=603,DVar(useSites={115},value=null[↦603],origin=114),NullExpr(pc=603)),
	115: PutField(pc=604,java.util.HashMap$TreeNode,left,java.util.HashMap$TreeNode,UVar(defSites={108},value=java.util.HashMap$TreeNode[↦575;refId=210]),UVar(defSites={114},value=null[↦603])),
	116: Goto(pc=607,target=121),
	117: Assignment(pc=614,DVar(useSites={118},value={java.util.HashMap$TreeNode, null}[↦614;refId=213],origin=117),GetField(pc=614,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={108},value=java.util.HashMap$TreeNode[↦575;refId=210]))),
	118: If(pc=617,UVar(defSites={-1},value=java.util.HashMap$TreeNode[↦-1;refId=102]),!=,UVar(defSites={117},value={java.util.HashMap$TreeNode, null}[↦614;refId=213]),target=121),
	119: Assignment(pc=622,DVar(useSites={120},value=null[↦622],origin=119),NullExpr(pc=622)),
	120: PutField(pc=623,java.util.HashMap$TreeNode,right,java.util.HashMap$TreeNode,UVar(defSites={108},value=java.util.HashMap$TreeNode[↦575;refId=210]),UVar(defSites={119},value=null[↦622])),
	121: If(pc=627,UVar(defSites={-4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=123),
	122: StaticMethodCall(pc=633,java.util.HashMap$TreeNode,isInterface=false,void moveRootToFront(java.util.HashMap$Node[],java.util.HashMap$TreeNode),(UVar(defSites={-3},value=_ <: java.util.HashMap$Node[][↦-3;refId=104]),UVar(defSites={48,8,36,106,41,37,23,-1},value={java.util.HashMap$TreeNode, null}[refId=209; values=«java.util.HashMap$TreeNode[↦160;refId=131], java.util.HashMap$TreeNode[↦166;refId=132], {java.util.HashMap$TreeNode, null}[↦104;refId=122], java.util.HashMap$TreeNode[↦-1;refId=102], {java.util.HashMap$TreeNode, null}[↦561;refId=205], java.util.HashMap$TreeNode[↦229;refId=145], java.util.HashMap$TreeNode[↦27;refId=107], java.util.HashMap$TreeNode[↦187;refId=135]»]))),
	123: Return(pc=636)
),cfg=CFG(
	BB_0: BasicBlock(start=10,end=11) -> {BB_44,BB_22}
	BB_10: BasicBlock(start=121,end=121) -> {BB_30,BB_48}
	BB_11: BasicBlock(start=84,end=84) -> {BB_24,BB_16}
	BB_12: BasicBlock(start=61,end=61) -> {BB_47}
	BB_13: BasicBlock(start=1,end=2) -> {BB_2c,BB_41}
	BB_14: BasicBlock(start=74,end=75) -> {BB_d,BB_26}
	BB_15: BasicBlock(start=117,end=118) -> {BB_3b,BB_10}
	BB_16: BasicBlock(start=85,end=85) -> {BB_36}
	BB_17: BasicBlock(start=21,end=21) -> {BB_44,BB_1e}
	BB_18: BasicBlock(start=33,end=33) -> {BB_44,BB_1b}
	BB_19: BasicBlock(start=73,end=73) -> {BB_42}
	BB_1: BasicBlock(start=14,end=14) -> {BB_44,BB_45}
	BB_1a: BasicBlock(start=105,end=105) -> {BB_40}
	BB_1b: BasicBlock(start=34,end=34) -> {BB_44,BB_2e}
	BB_1c: BasicBlock(start=64,end=67) -> {BB_6,BB_46}
	BB_1d: BasicBlock(start=17,end=17) -> {BB_3f,BB_31}
	BB_1e: BasicBlock(start=22,end=22) -> {BB_3a,BB_a}
	BB_1f: BasicBlock(start=44,end=50) -> {BB_3e,BB_23}
	BB_20: BasicBlock(start=59,end=60) -> {BB_47}
	BB_21: BasicBlock(start=27,end=28) -> {BB_e,BB_18}
	BB_22: BasicBlock(start=12,end=13) -> {BB_1,BB_33}
	BB_23: BasicBlock(start=54,end=56) -> {BB_47,BB_c}
	BB_24: BasicBlock(start=86,end=86) -> {BB_36}
	BB_25: BasicBlock(start=81,end=81) -> {BB_36}
	BB_26: BasicBlock(start=76,end=77) -> {BB_42}
	BB_27: BasicBlock(start=39,end=39) -> {BB_3c,BB_37}
	BB_28: BasicBlock(start=98,end=98) -> {BB_35}
	BB_29: BasicBlock(start=103,end=104) -> {BB_1a,BB_f}
	BB_2: BasicBlock(start=9,end=9) -> {BB_44,BB_0}
	BB_2a: BasicBlock(start=91,end=93) -> {BB_35}
	BB_2b: BasicBlock(start=108,end=111) -> {BB_10,BB_2f}
	BB_2c: BasicBlock(start=3,end=3) -> {BB_32}
	BB_2d: BasicBlock(start=80,end=80) -> {BB_36}
	BB_2e: BasicBlock(start=35,end=35) -> {BB_32}
	BB_2f: BasicBlock(start=112,end=113) -> {BB_15,BB_39}
	BB_30: BasicBlock(start=123,end=123) -> {BB_32}
	BB_31: BasicBlock(start=18,end=18) -> {BB_3f}
	BB_32: ExitNode(normalReturn=true)
	BB_33: BasicBlock(start=16,end=16) -> {BB_1d}
	BB_34: BasicBlock(start=31,end=32) -> {BB_3d,BB_18}
	BB_35: BasicBlock(start=99,end=102) -> {BB_29}
	BB_36: BasicBlock(start=87,end=87) -> {BB_29,BB_8}
	BB_37: BasicBlock(start=40,end=40) -> {BB_4}
	BB_38: BasicBlock(start=26,end=26) -> {BB_3d,BB_21}
	BB_39: BasicBlock(start=114,end=116) -> {BB_10}
	BB_3: BasicBlock(start=96,end=97) -> {BB_35}
	BB_3a: BasicBlock(start=23,end=23) -> {BB_44,BB_9}
	BB_3b: BasicBlock(start=119,end=120) -> {BB_10}
	BB_3c: BasicBlock(start=82,end=82) -> {BB_11,BB_49}
	BB_3d: BasicBlock(start=36,end=38) -> {BB_27,BB_3c}
	BB_3e: BasicBlock(start=51,end=53) -> {BB_1c}
	BB_3f: BasicBlock(start=19,end=19) -> {BB_17,BB_b}
	BB_40: BasicBlock(start=107,end=107) -> {BB_10,BB_2b}
	BB_41: BasicBlock(start=4,end=8) -> {BB_44,BB_2}
	BB_42: BasicBlock(start=79,end=79) -> {BB_2d,BB_25}
	BB_43: BasicBlock(start=94,end=95) -> {BB_3,BB_28}
	BB_44: ExitNode(normalReturn=false)
	BB_45: BasicBlock(start=15,end=15) -> {BB_1d}
	BB_46: BasicBlock(start=68,end=68) -> {BB_6}
	BB_47: BasicBlock(start=62,end=63) -> {BB_1c}
	BB_48: BasicBlock(start=122,end=122) -> {BB_44,BB_30}
	BB_49: BasicBlock(start=83,end=83) -> {BB_36}
	BB_4: BasicBlock(start=41,end=42) -> {BB_5,BB_1f}
	BB_5: BasicBlock(start=43,end=43) -> {BB_4}
	BB_6: BasicBlock(start=69,end=72) -> {BB_14,BB_19}
	BB_7: BasicBlock(start=0,end=0) -> {BB_13,BB_2c}
	BB_8: BasicBlock(start=88,end=90) -> {BB_43,BB_2a}
	BB_9: BasicBlock(start=24,end=24) -> {BB_a}
	BB_a: BasicBlock(start=25,end=25) -> {BB_38,BB_18}
	BB_b: BasicBlock(start=20,end=20) -> {BB_32}
	BB_c: BasicBlock(start=57,end=58) -> {BB_20,BB_12}
	BB_d: BasicBlock(start=78,end=78) -> {BB_42}
	BB_e: BasicBlock(start=29,end=30) -> {BB_18,BB_34}
	BB_f: BasicBlock(start=106,end=106) -> {BB_44,BB_40}
))

