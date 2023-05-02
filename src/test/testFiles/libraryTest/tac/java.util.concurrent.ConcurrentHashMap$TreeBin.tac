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

java.util.concurrent.ConcurrentHashMap$TreeNode rotateLeft(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={20} (origin=-2),
	2: useSites={0,4,18,6,14,1,19,7} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=20),
	1: Assignment(pc=5,DVar(useSites={8,20,2,18,17,3,19,11,15},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦5;refId=104],origin=1),GetField(pc=5,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]))),
	2: If(pc=10,UVar(defSites={1},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦5;refId=104]),==,NullExpr(pc=-333),target=20),
	3: Assignment(pc=15,DVar(useSites={4,6,5},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦15;refId=105],origin=3),GetField(pc=15,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]))),
	4: PutField(pc=19,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]),UVar(defSites={3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦15;refId=105])),
	5: If(pc=25,UVar(defSites={3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦15;refId=105]),==,NullExpr(pc=-333),target=7),
	6: PutField(pc=31,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦15;refId=105]),UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103])),
	7: Assignment(pc=36,DVar(useSites={8,17,9,13,15},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦36;refId=106],origin=7),GetField(pc=36,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]))),
	8: PutField(pc=40,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]),UVar(defSites={7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦36;refId=106])),
	9: If(pc=45,UVar(defSites={7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦36;refId=106]),!=,NullExpr(pc=-333),target=13),
	10: Assignment(pc=51,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=51,0)),
	11: PutField(pc=52,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]),UVar(defSites={10},value=int = 0)),
	12: Goto(pc=55,target=18),
	13: Assignment(pc=59,DVar(useSites={14},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦59;refId=107],origin=13),GetField(pc=59,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦36;refId=106]))),
	14: If(pc=63,UVar(defSites={13},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦59;refId=107]),!=,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]),target=17),
	15: PutField(pc=68,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104])),
	16: Goto(pc=71,target=18),
	17: PutField(pc=76,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104])),
	18: PutField(pc=81,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]),UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103])),
	19: PutField(pc=86,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]),UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104])),
	20: ReturnValue(pc=90,UVar(defSites={-2,1},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=108; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102]»]))
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

boolean checkInvariants(java.util.concurrent.ConcurrentHashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={0,8,4,20,2,18,1,33,25,13,3,35,27,39} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={16,17,19},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={24,50,42,26,49,41,23},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦6;refId=105],origin=1),GetField(pc=6,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]))),
	2: Assignment(pc=11,DVar(useSites={32,44,34,54,45,55,31},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦11;refId=106],origin=2),GetField(pc=11,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]))),
	3: Assignment(pc=16,DVar(useSites={6,7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦16;refId=107],origin=3),GetField(pc=16,java.util.concurrent.ConcurrentHashMap$TreeNode,prev,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]))),
	4: Assignment(pc=22,DVar(useSites={12,5,11},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦22;refId=108],origin=4),GetField(pc=22,java.util.concurrent.ConcurrentHashMap$TreeNode,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]))),
	5: Checkcast(pc=25,UVar(defSites={4},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦22;refId=108]),java.util.concurrent.ConcurrentHashMap$TreeNode),
	6: If(pc=32,UVar(defSites={3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦16;refId=107]),==,NullExpr(pc=-333),target=11),
	7: Assignment(pc=37,DVar(useSites={8},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦37;refId=111],origin=7),GetField(pc=37,java.util.concurrent.ConcurrentHashMap$TreeNode,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦16;refId=107]))),
	8: If(pc=41,UVar(defSites={7},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦37;refId=111]),==,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),target=11),
	9: Assignment(pc=44,DVar(useSites={10},value=int = 0,origin=9),IntConst(pc=44,0)),
	10: ReturnValue(pc=45,UVar(defSites={9},value=int = 0)),
	11: If(pc=48,UVar(defSites={4},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=109]),==,NullExpr(pc=-333),target=16),
	12: Assignment(pc=53,DVar(useSites={13},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦53;refId=112],origin=12),GetField(pc=53,java.util.concurrent.ConcurrentHashMap$TreeNode,prev,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={4},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦22;refId=109]))),
	13: If(pc=57,UVar(defSites={12},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦53;refId=112]),==,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),target=16),
	14: Assignment(pc=60,DVar(useSites={15},value=int = 0,origin=14),IntConst(pc=60,0)),
	15: ReturnValue(pc=61,UVar(defSites={14},value=int = 0)),
	16: If(pc=63,UVar(defSites={0},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦1;refId=103]),==,NullExpr(pc=-333),target=23),
	17: Assignment(pc=68,DVar(useSites={18},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦68;refId=113],origin=17),GetField(pc=68,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={0},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦1;refId=103]))),
	18: If(pc=71,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),==,UVar(defSites={17},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦68;refId=113]),target=23),
	19: Assignment(pc=76,DVar(useSites={20},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦76;refId=114],origin=19),GetField(pc=76,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={0},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦1;refId=103]))),
	20: If(pc=79,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),==,UVar(defSites={19},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦76;refId=114]),target=23),
	21: Assignment(pc=82,DVar(useSites={22},value=int = 0,origin=21),IntConst(pc=82,0)),
	22: ReturnValue(pc=83,UVar(defSites={21},value=int = 0)),
	23: If(pc=85,UVar(defSites={1},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦6;refId=105]),==,NullExpr(pc=-333),target=31),
	24: Assignment(pc=89,DVar(useSites={25},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦89;refId=115],origin=24),GetField(pc=89,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=105]))),
	25: If(pc=93,UVar(defSites={24},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦89;refId=115]),!=,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),target=29),
	26: Assignment(pc=97,DVar(useSites={28},value=an int,origin=26),GetField(pc=97,java.util.concurrent.ConcurrentHashMap$TreeNode,hash,int,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=105]))),
	27: Assignment(pc=101,DVar(useSites={28},value=an int,origin=27),GetField(pc=101,java.util.concurrent.ConcurrentHashMap$TreeNode,hash,int,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]))),
	28: If(pc=104,UVar(defSites={26},value=an int),<=,UVar(defSites={27},value=an int),target=31),
	29: Assignment(pc=107,DVar(useSites={30},value=int = 0,origin=29),IntConst(pc=107,0)),
	30: ReturnValue(pc=108,UVar(defSites={29},value=int = 0)),
	31: If(pc=110,UVar(defSites={2},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦11;refId=106]),==,NullExpr(pc=-333),target=39),
	32: Assignment(pc=114,DVar(useSites={33},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦114;refId=116],origin=32),GetField(pc=114,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦11;refId=106]))),
	33: If(pc=118,UVar(defSites={32},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦114;refId=116]),!=,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]),target=37),
	34: Assignment(pc=122,DVar(useSites={36},value=an int,origin=34),GetField(pc=122,java.util.concurrent.ConcurrentHashMap$TreeNode,hash,int,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦11;refId=106]))),
	35: Assignment(pc=126,DVar(useSites={36},value=an int,origin=35),GetField(pc=126,java.util.concurrent.ConcurrentHashMap$TreeNode,hash,int,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]))),
	36: If(pc=129,UVar(defSites={34},value=an int),>=,UVar(defSites={35},value=an int),target=39),
	37: Assignment(pc=132,DVar(useSites={38},value=int = 0,origin=37),IntConst(pc=132,0)),
	38: ReturnValue(pc=133,UVar(defSites={37},value=int = 0)),
	39: Assignment(pc=135,DVar(useSites={40},value=int ∈ [0,1],origin=39),GetField(pc=135,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={-2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-1;refId=102]))),
	40: If(pc=138,UVar(defSites={39},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=49),
	41: If(pc=142,UVar(defSites={1},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦6;refId=105]),==,NullExpr(pc=-333),target=49),
	42: Assignment(pc=146,DVar(useSites={43},value=int ∈ [0,1],origin=42),GetField(pc=146,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=105]))),
	43: If(pc=149,UVar(defSites={42},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=49),
	44: If(pc=153,UVar(defSites={2},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦11;refId=106]),==,NullExpr(pc=-333),target=49),
	45: Assignment(pc=157,DVar(useSites={46},value=int ∈ [0,1],origin=45),GetField(pc=157,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦11;refId=106]))),
	46: If(pc=160,UVar(defSites={45},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=49),
	47: Assignment(pc=163,DVar(useSites={48},value=int = 0,origin=47),IntConst(pc=163,0)),
	48: ReturnValue(pc=164,UVar(defSites={47},value=int = 0)),
	49: If(pc=166,UVar(defSites={1},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦6;refId=105]),==,NullExpr(pc=-333),target=54),
	50: Assignment(pc=170,DVar(useSites={51},value=int ∈ [0,1],origin=50),StaticFunctionCall(pc=170,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,boolean checkInvariants(java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=105])))),
	51: If(pc=173,UVar(defSites={50},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=54),
	52: Assignment(pc=176,DVar(useSites={53},value=int = 0,origin=52),IntConst(pc=176,0)),
	53: ReturnValue(pc=177,UVar(defSites={52},value=int = 0)),
	54: If(pc=179,UVar(defSites={2},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦11;refId=106]),==,NullExpr(pc=-333),target=59),
	55: Assignment(pc=183,DVar(useSites={56},value=int ∈ [0,1],origin=55),StaticFunctionCall(pc=183,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,boolean checkInvariants(java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦11;refId=106])))),
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

void <init>(java.util.concurrent.ConcurrentHashMap$TreeNode)
AITACode(params=(Parameters(
	0: useSites={4,52,49,3} (origin=-1),
	1: useSites={16,4,12,18,10,6,22,14,46,49,41,37,21,45,19,11,43,7,39} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={3},value=int = -2,origin=0),IntConst(pc=1,-2)),
	1: Assignment(pc=3,DVar(useSites={3},value=null[↦3],origin=1),NullExpr(pc=3)),
	2: Assignment(pc=4,DVar(useSites={3},value=null[↦4],origin=2),NullExpr(pc=4)),
	3: NonVirtualMethodCall(pc=5,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object),UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦-1;refId=102]),(UVar(defSites={0},value=int = -2),UVar(defSites={1},value=null[↦3]),UVar(defSites={2},value=null[↦4]))),
	4: PutField(pc=10,java.util.concurrent.ConcurrentHashMap$TreeBin,first,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦-1;refId=102]),UVar(defSites={-2},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103])),
	5: Assignment(pc=13,DVar(useSites={12,22,46,49,41,37,21,45,43,39},value=null[↦13],origin=5),NullExpr(pc=13)),
	6: If(pc=18,UVar(defSites={-2,7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]),==,NullExpr(pc=-333),target=49),
	7: Assignment(pc=22,DVar(useSites={16,8,12,18,10,6,22,14,46,49,41,37,21,45,19,11,43,39},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦22;refId=219],origin=7),GetField(pc=22,java.util.concurrent.ConcurrentHashMap$TreeNode,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]))),
	8: Checkcast(pc=25,UVar(defSites={7},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦22;refId=219]),java.util.concurrent.ConcurrentHashMap$TreeNode),
	9: Assignment(pc=32,DVar(useSites={10,11},value=null[↦32],origin=9),NullExpr(pc=32)),
	10: PutField(pc=34,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]),UVar(defSites={9},value=null[↦32])),
	11: PutField(pc=37,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]),UVar(defSites={9},value=null[↦32])),
	12: If(pc=41,UVar(defSites={46,-2,5,7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=210; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], null[↦13]»]),!=,NullExpr(pc=-333),target=18),
	13: Assignment(pc=45,DVar(useSites={14},value=null[↦45],origin=13),NullExpr(pc=45)),
	14: PutField(pc=46,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]),UVar(defSites={13},value=null[↦45])),
	15: Assignment(pc=50,DVar(useSites={16},value=int = 0,origin=15),IntConst(pc=50,0)),
	16: PutField(pc=51,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]),UVar(defSites={15},value=int = 0)),
	17: Goto(pc=56,target=48),
	18: Assignment(pc=60,DVar(useSites={32,34,30},value={_ <: java.lang.Object, null}[↦60;refId=224],origin=18),GetField(pc=60,java.util.concurrent.ConcurrentHashMap$TreeNode,key,java.lang.Object,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]))),
	19: Assignment(pc=66,DVar(useSites={26,23},value=an int,origin=19),GetField(pc=66,java.util.concurrent.ConcurrentHashMap$TreeNode,hash,int,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=123; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]))),
	20: Assignment(pc=71,DVar(useSites={32,29},value=null[↦71],origin=20),NullExpr(pc=71)),
	21: Assignment(pc=79,DVar(useSites={32,34},value={_ <: java.lang.Object, null}[↦79;refId=232],origin=21),GetField(pc=79,java.util.concurrent.ConcurrentHashMap$TreeNode,key,java.lang.Object,UVar(defSites={46,-2,5,37,7,39},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=227; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=200], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=205]»]))),
	22: Assignment(pc=86,DVar(useSites={26,23},value=an int,origin=22),GetField(pc=86,java.util.concurrent.ConcurrentHashMap$TreeNode,hash,int,UVar(defSites={46,-2,5,37,7,39},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=227; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=200], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=205]»]))),
	23: If(pc=94,UVar(defSites={22},value=an int),<=,UVar(defSites={19},value=an int),target=26),
	24: Assignment(pc=97,DVar(useSites={36,42},value=int = -1,origin=24),IntConst(pc=97,-1)),
	25: Goto(pc=100,target=36),
	26: If(pc=107,UVar(defSites={22},value=an int),>=,UVar(defSites={19},value=an int),target=29),
	27: Assignment(pc=110,DVar(useSites={36,42},value=int = 1,origin=27),IntConst(pc=110,1)),
	28: Goto(pc=113,target=36),
	29: If(pc=118,UVar(defSites={20,30},value={java.lang.Class, null}[refId=215; values=«null[↦71], {java.lang.Class, null}[↦123;refId=172]»]),!=,NullExpr(pc=-333),target=32),
	30: Assignment(pc=123,DVar(useSites={32,29,31},value={java.lang.Class, null}[↦123;refId=237],origin=30),StaticFunctionCall(pc=123,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.lang.Class comparableClassFor(java.lang.Object),(UVar(defSites={18},value={_ <: java.lang.Object, null}[↦60;refId=224])))),
	31: If(pc=129,UVar(defSites={30},value={java.lang.Class, null}[↦123;refId=237]),==,NullExpr(pc=-333),target=34),
	32: Assignment(pc=138,DVar(useSites={36,42,33},value=an int,origin=32),StaticFunctionCall(pc=138,java.util.concurrent.ConcurrentHashMap,isInterface=false,int compareComparables(java.lang.Class,java.lang.Object,java.lang.Object),(UVar(defSites={20,30},value=java.lang.Class[↦123;refId=237]),UVar(defSites={18},value={_ <: java.lang.Object, null}[↦60;refId=224]),UVar(defSites={21},value={_ <: java.lang.Object, null}[↦79;refId=232])))),
	33: If(pc=144,UVar(defSites={32},value=an int),!=,IntConst(pc=-333,0),target=36),
	34: Assignment(pc=151,DVar(useSites={36,42},value=an int,origin=34),StaticFunctionCall(pc=151,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,int tieBreakOrder(java.lang.Object,java.lang.Object),(UVar(defSites={18},value={_ <: java.lang.Object, null}[↦60;refId=224]),UVar(defSites={21},value={_ <: java.lang.Object, null}[↦79;refId=232])))),
	35: Nop(pc=154),
	36: If(pc=162,UVar(defSites={32,24,34,27},value=an int),>,IntConst(pc=-333,0),target=39),
	37: Assignment(pc=167,DVar(useSites={40,38,22,41,21,45,43,39},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=264],origin=37),GetField(pc=167,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={46,-2,5,37,7,39},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=247; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=200], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=205]»]))),
	38: Goto(pc=170,target=40),
	39: Assignment(pc=175,DVar(useSites={40,22,41,37,21,45,43},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=271; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=264], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=270]»],origin=39),GetField(pc=175,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={46,-2,5,37,7,39},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=247; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=200], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=205]»]))),
	40: If(pc=181,UVar(defSites={37,39},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=271; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=264], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=270]»]),!=,NullExpr(pc=-333),target=21),
	41: PutField(pc=187,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=267; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»]),UVar(defSites={46,-2,5,37,7,39},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=269; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=200], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=205]»])),
	42: If(pc=192,UVar(defSites={32,24,34,27},value=an int),>,IntConst(pc=-333,0),target=45),
	43: PutField(pc=198,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={46,-2,5,37,7,39},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=269; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=200], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=205]»]),UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=267; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»])),
	44: Goto(pc=201,target=46),
	45: PutField(pc=207,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={46,-2,5,37,7,39},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=269; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦167;refId=200], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦175;refId=205]»]),UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=267; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»])),
	46: Assignment(pc=212,DVar(useSites={12,22,49,41,37,21,45,43,39,47},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=285],origin=46),StaticFunctionCall(pc=212,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,java.util.concurrent.ConcurrentHashMap$TreeNode balanceInsertion(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={46,-2,5,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=280; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184]»]),UVar(defSites={-2,7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=281; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115]»])))),
	47: Goto(pc=216,target=48),
	48: Goto(pc=225,target=6),
	49: PutField(pc=230,java.util.concurrent.ConcurrentHashMap$TreeBin,root,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦-1;refId=102]),UVar(defSites={46,-2,5,7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=210; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦22;refId=115], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦212;refId=184], null[↦13]»])),
	50: Assignment(pc=233,DVar(useSites={51},value=int ∈ [0,1],origin=50),GetStatic(pc=233,java.util.concurrent.ConcurrentHashMap$TreeBin,$assertionsDisabled,boolean)),
	51: If(pc=236,UVar(defSites={50},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=58),
	52: Assignment(pc=240,DVar(useSites={53},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦240;refId=228],origin=52),GetField(pc=240,java.util.concurrent.ConcurrentHashMap$TreeBin,root,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦-1;refId=102]))),
	53: Assignment(pc=243,DVar(useSites={54},value=int ∈ [0,1],origin=53),StaticFunctionCall(pc=243,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,boolean checkInvariants(java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={52},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦240;refId=228])))),
	54: If(pc=246,UVar(defSites={53},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=58),
	55: Assignment(pc=249,DVar(useSites={56,57},value=java.lang.AssertionError[↦249;refId=230],origin=55),New(pc=249,java.lang.AssertionError)),
	56: NonVirtualMethodCall(pc=253,java.lang.AssertionError,isInterface=false,void <init>(),UVar(defSites={55},value=java.lang.AssertionError[↦249;refId=230]),()),
	57: Throw(pc=256,UVar(defSites={55},value=java.lang.AssertionError[↦249;refId=230])),
	58: Return(pc=257)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_23,BB_22}
	BB_10: BasicBlock(start=33,end=33) -> {BB_20,BB_15}
	BB_11: BasicBlock(start=13,end=17) -> {BB_1a}
	BB_12: BasicBlock(start=41,end=42) -> {BB_13,BB_7}
	BB_13: BasicBlock(start=45,end=45) -> {BB_c}
	BB_14: BasicBlock(start=32,end=32) -> {BB_23,BB_10}
	BB_15: BasicBlock(start=34,end=34) -> {BB_23,BB_5}
	BB_16: BasicBlock(start=54,end=54) -> {BB_8,BB_1f}
	BB_17: BasicBlock(start=49,end=51) -> {BB_8,BB_1}
	BB_18: BasicBlock(start=7,end=8) -> {BB_23,BB_3}
	BB_19: BasicBlock(start=39,end=39) -> {BB_1d}
	BB_1: BasicBlock(start=52,end=53) -> {BB_23,BB_16}
	BB_1a: BasicBlock(start=48,end=48) -> {BB_2}
	BB_1b: BasicBlock(start=18,end=20) -> {BB_f}
	BB_1c: ExitNode(normalReturn=true)
	BB_1d: BasicBlock(start=40,end=40) -> {BB_12,BB_f}
	BB_1e: BasicBlock(start=26,end=26) -> {BB_e,BB_4}
	BB_1f: BasicBlock(start=55,end=56) -> {BB_23,BB_d}
	BB_20: BasicBlock(start=36,end=36) -> {BB_b,BB_19}
	BB_21: BasicBlock(start=30,end=30) -> {BB_23,BB_6}
	BB_22: BasicBlock(start=4,end=5) -> {BB_2}
	BB_23: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=6,end=6) -> {BB_17,BB_18}
	BB_3: BasicBlock(start=9,end=12) -> {BB_11,BB_1b}
	BB_4: BasicBlock(start=27,end=28) -> {BB_20}
	BB_5: BasicBlock(start=35,end=35) -> {BB_20}
	BB_6: BasicBlock(start=31,end=31) -> {BB_14,BB_15}
	BB_7: BasicBlock(start=43,end=44) -> {BB_c}
	BB_8: BasicBlock(start=58,end=58) -> {BB_1c}
	BB_9: BasicBlock(start=47,end=47) -> {BB_1a}
	BB_a: BasicBlock(start=24,end=25) -> {BB_20}
	BB_b: BasicBlock(start=37,end=38) -> {BB_1d}
	BB_c: BasicBlock(start=46,end=46) -> {BB_23,BB_9}
	BB_d: BasicBlock(start=57,end=57) -> {BB_23}
	BB_e: BasicBlock(start=29,end=29) -> {BB_14,BB_21}
	BB_f: BasicBlock(start=21,end=23) -> {BB_a,BB_1e}
))

java.util.concurrent.ConcurrentHashMap$TreeNode balanceInsertion(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={40,54,67,11,27} (origin=-2),
	2: useSites={2,26,6,1,5,53} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 1,origin=0),IntConst(pc=1,1)),
	1: PutField(pc=2,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={-3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103]),UVar(defSites={0},value=int = 1)),
	2: Assignment(pc=6,DVar(useSites={48,36,52,28,34,26,6,54,9,25,5,21,53,13,61,3,27,7,55,63},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦6;refId=200],origin=2),GetField(pc=6,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={2,9,-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=171; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=106], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=116]»]))),
	3: If(pc=11,UVar(defSites={2},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦6;refId=200]),!=,NullExpr(pc=-333),target=7),
	4: Assignment(pc=15,DVar(useSites={5},value=int = 0,origin=4),IntConst(pc=15,0)),
	5: PutField(pc=16,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={2,9,-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=171; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=106], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=116]»]),UVar(defSites={4},value=int = 0)),
	6: ReturnValue(pc=20,UVar(defSites={2,9,-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=171; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=106], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=116]»])),
	7: Assignment(pc=22,DVar(useSites={8},value=int ∈ [0,1],origin=7),GetField(pc=22,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]))),
	8: If(pc=25,UVar(defSites={7},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	9: Assignment(pc=29,DVar(useSites={64,40,12,2,66,50,10,26,6,14,5,37,53,67,39,23},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦29;refId=202],origin=9),GetField(pc=29,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]))),
	10: If(pc=34,UVar(defSites={9},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦29;refId=202]),!=,NullExpr(pc=-333),target=12),
	11: ReturnValue(pc=38,UVar(defSites={40,54,-2,67,27},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=201; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦238;refId=167], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦196;refId=112], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦143;refId=177], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦101;refId=123]»])),
	12: Assignment(pc=41,DVar(useSites={42,46,13,43},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦41;refId=204],origin=12),GetField(pc=41,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={9},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]))),
	13: If(pc=47,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]),!=,UVar(defSites={12},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦41;refId=204]),target=42),
	14: Assignment(pc=51,DVar(useSites={16,19,15},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦51;refId=210],origin=14),GetField(pc=51,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={9},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]))),
	15: If(pc=57,UVar(defSites={14},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦51;refId=210]),==,NullExpr(pc=-333),target=25),
	16: Assignment(pc=62,DVar(useSites={17},value=int ∈ [0,1],origin=16),GetField(pc=62,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={14},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦51;refId=210]))),
	17: If(pc=65,UVar(defSites={16},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=25),
	18: Assignment(pc=70,DVar(useSites={19},value=int = 0,origin=18),IntConst(pc=70,0)),
	19: PutField(pc=71,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={14},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦51;refId=210]),UVar(defSites={18},value=int = 0)),
	20: Assignment(pc=75,DVar(useSites={21},value=int = 0,origin=20),IntConst(pc=75,0)),
	21: PutField(pc=76,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]),UVar(defSites={20},value=int = 0)),
	22: Assignment(pc=80,DVar(useSites={23},value=int = 1,origin=22),IntConst(pc=80,1)),
	23: PutField(pc=81,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={9},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]),UVar(defSites={22},value=int = 1)),
	24: Goto(pc=86,target=2),
	25: Assignment(pc=91,DVar(useSites={26},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦91;refId=245],origin=25),GetField(pc=91,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]))),
	26: If(pc=94,UVar(defSites={2,9,-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=212; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=106], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=116]»]),!=,UVar(defSites={25},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦91;refId=245]),target=34),
	27: Assignment(pc=101,DVar(useSites={40,28,54,67,11},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦101;refId=251],origin=27),StaticFunctionCall(pc=101,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,java.util.concurrent.ConcurrentHashMap$TreeNode rotateLeft(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=211; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦238;refId=167], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦196;refId=112], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦143;refId=177], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦101;refId=123]»]),UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200])))),
	28: Assignment(pc=106,DVar(useSites={32,36,34,29},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦106;refId=252],origin=28),GetField(pc=106,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]))),
	29: If(pc=111,UVar(defSites={28},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦106;refId=252]),!=,NullExpr(pc=-333),target=32),
	30: Assignment(pc=114,DVar(useSites={40,37,39},value=null[↦114],origin=30),NullExpr(pc=114)),
	31: Goto(pc=115,target=33),
	32: Assignment(pc=119,DVar(useSites={40,37,39},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=254; values=«null[↦114], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦119;refId=253]»],origin=32),GetField(pc=119,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={28},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦106;refId=252]))),
	33: Nop(pc=122),
	34: If(pc=124,UVar(defSites={28,2},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=248; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦106;refId=124], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]»]),==,NullExpr(pc=-333),target=2),
	35: Assignment(pc=128,DVar(useSites={36},value=int = 0,origin=35),IntConst(pc=128,0)),
	36: PutField(pc=129,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={28,2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=248; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦106;refId=124], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]»]),UVar(defSites={35},value=int = 0)),
	37: If(pc=133,UVar(defSites={32,30,9},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=249; values=«null[↦114], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦119;refId=125], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]»]),==,NullExpr(pc=-333),target=2),
	38: Assignment(pc=137,DVar(useSites={39},value=int = 1,origin=38),IntConst(pc=137,1)),
	39: PutField(pc=138,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={32,30,9},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=268; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦119;refId=125], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]»]),UVar(defSites={38},value=int = 1)),
	40: Assignment(pc=143,DVar(useSites={54,41,67,11,27},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦143;refId=272],origin=40),StaticFunctionCall(pc=143,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,java.util.concurrent.ConcurrentHashMap$TreeNode rotateRight(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=246; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦238;refId=167], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦196;refId=112], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦101;refId=123], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦143;refId=177]»]),UVar(defSites={32,30,9},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=268; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦119;refId=125], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]»])))),
	41: Goto(pc=147,target=2),
	42: If(pc=152,UVar(defSites={12},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦41;refId=204]),==,NullExpr(pc=-333),target=52),
	43: Assignment(pc=157,DVar(useSites={44},value=int ∈ [0,1],origin=43),GetField(pc=157,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={12},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦41;refId=204]))),
	44: If(pc=160,UVar(defSites={43},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=52),
	45: Assignment(pc=165,DVar(useSites={46},value=int = 0,origin=45),IntConst(pc=165,0)),
	46: PutField(pc=166,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={12},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦41;refId=204]),UVar(defSites={45},value=int = 0)),
	47: Assignment(pc=170,DVar(useSites={48},value=int = 0,origin=47),IntConst(pc=170,0)),
	48: PutField(pc=171,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]),UVar(defSites={47},value=int = 0)),
	49: Assignment(pc=175,DVar(useSites={50},value=int = 1,origin=49),IntConst(pc=175,1)),
	50: PutField(pc=176,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={9},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]),UVar(defSites={49},value=int = 1)),
	51: Goto(pc=181,target=2),
	52: Assignment(pc=186,DVar(useSites={53},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦186;refId=235],origin=52),GetField(pc=186,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]))),
	53: If(pc=189,UVar(defSites={2,9,-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=206; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=106], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=116]»]),!=,UVar(defSites={52},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦186;refId=235]),target=61),
	54: Assignment(pc=196,DVar(useSites={40,67,11,27,55},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦196;refId=241],origin=54),StaticFunctionCall(pc=196,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,java.util.concurrent.ConcurrentHashMap$TreeNode rotateRight(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=205; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦238;refId=167], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦196;refId=112], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦143;refId=177], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦101;refId=123]»]),UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200])))),
	55: Assignment(pc=201,DVar(useSites={56,61,59,63},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦201;refId=242],origin=55),GetField(pc=201,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={2},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]))),
	56: If(pc=206,UVar(defSites={55},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦201;refId=242]),!=,NullExpr(pc=-333),target=59),
	57: Assignment(pc=209,DVar(useSites={64,66,67},value=null[↦209],origin=57),NullExpr(pc=209)),
	58: Goto(pc=210,target=60),
	59: Assignment(pc=214,DVar(useSites={64,66,67},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=244; values=«null[↦209], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦214;refId=243]»],origin=59),GetField(pc=214,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={55},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦201;refId=242]))),
	60: Nop(pc=217),
	61: If(pc=219,UVar(defSites={2,55},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=238; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦201;refId=113], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]»]),==,NullExpr(pc=-333),target=2),
	62: Assignment(pc=223,DVar(useSites={63},value=int = 0,origin=62),IntConst(pc=223,0)),
	63: PutField(pc=224,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={2,55},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=238; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦201;refId=113], java.util.concurrent.ConcurrentHashMap$TreeNode[↦6;refId=200]»]),UVar(defSites={62},value=int = 0)),
	64: If(pc=228,UVar(defSites={9,57,59},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=239; values=«null[↦209], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦214;refId=114], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]»]),==,NullExpr(pc=-333),target=2),
	65: Assignment(pc=232,DVar(useSites={66},value=int = 1,origin=65),IntConst(pc=232,1)),
	66: PutField(pc=233,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={9,57,59},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=258; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦214;refId=114], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]»]),UVar(defSites={65},value=int = 1)),
	67: Assignment(pc=238,DVar(useSites={40,68,54,11,27},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦238;refId=262],origin=67),StaticFunctionCall(pc=238,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,java.util.concurrent.ConcurrentHashMap$TreeNode rotateLeft(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode),(UVar(defSites={40,54,-2,67,27},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=236; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦238;refId=167], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦196;refId=112], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦101;refId=123], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦143;refId=177]»]),UVar(defSites={9,57,59},value=java.util.concurrent.ConcurrentHashMap$TreeNode[refId=258; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦214;refId=114], java.util.concurrent.ConcurrentHashMap$TreeNode[↦29;refId=202]»])))),
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

void <clinit>()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value=Class<java.util.concurrent.ConcurrentHashMap>[↦0;refId=102],origin=0),ClassConst(pc=0,java.util.concurrent.ConcurrentHashMap)),
	1: Assignment(pc=2,DVar(useSites={2},value=int ∈ [0,1],origin=1),VirtualFunctionCall(pc=2,java.lang.Class,isInterface=false,boolean desiredAssertionStatus(),UVar(defSites={0},value=Class<java.util.concurrent.ConcurrentHashMap>[↦0;refId=102]),())),
	2: If(pc=5,UVar(defSites={1},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=5),
	3: Assignment(pc=8,DVar(useSites={6},value=int = 1,origin=3),IntConst(pc=8,1)),
	4: Goto(pc=9,target=6),
	5: Assignment(pc=12,DVar(useSites={6},value=int ∈ [0,1],origin=5),IntConst(pc=12,0)),
	6: PutStatic(pc=13,java.util.concurrent.ConcurrentHashMap$TreeBin,$assertionsDisabled,boolean,UVar(defSites={5,3},value=int ∈ [0,1])),
	7: Assignment(pc=16,DVar(useSites={8},value={jdk.internal.misc.Unsafe, null}[↦16;refId=105],origin=7),StaticFunctionCall(pc=16,jdk.internal.misc.Unsafe,isInterface=false,jdk.internal.misc.Unsafe getUnsafe(),())),
	8: PutStatic(pc=19,java.util.concurrent.ConcurrentHashMap$TreeBin,U,jdk.internal.misc.Unsafe,UVar(defSites={7},value={jdk.internal.misc.Unsafe, null}[↦16;refId=105])),
	9: Assignment(pc=22,DVar(useSites={12},value={jdk.internal.misc.Unsafe, null}[↦22;refId=106],origin=9),GetStatic(pc=22,java.util.concurrent.ConcurrentHashMap$TreeBin,U,jdk.internal.misc.Unsafe)),
	10: Assignment(pc=25,DVar(useSites={12},value=Class<java.util.concurrent.ConcurrentHashMap$TreeBin>[↦25;refId=107],origin=10),ClassConst(pc=25,java.util.concurrent.ConcurrentHashMap$TreeBin)),
	11: Assignment(pc=27,DVar(useSites={12},value=String("lockState")[@27;refId=108],origin=11),StringConst(pc=27,lockState)),
	12: Assignment(pc=29,DVar(useSites={13},value=ALongValue,origin=12),VirtualFunctionCall(pc=29,jdk.internal.misc.Unsafe,isInterface=false,long objectFieldOffset(java.lang.Class,java.lang.String),UVar(defSites={9},value={jdk.internal.misc.Unsafe, null}[↦22;refId=106]),(UVar(defSites={10},value=Class<java.util.concurrent.ConcurrentHashMap$TreeBin>[↦25;refId=107]),UVar(defSites={11},value=String("lockState")[@27;refId=108])))),
	13: PutStatic(pc=32,java.util.concurrent.ConcurrentHashMap$TreeBin,LOCKSTATE,long,UVar(defSites={12},value=ALongValue)),
	14: Return(pc=35)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_8,BB_4}
	BB_1: BasicBlock(start=5,end=5) -> {BB_2}
	BB_2: BasicBlock(start=6,end=7) -> {BB_8,BB_7}
	BB_3: BasicBlock(start=13,end=14) -> {BB_6}
	BB_4: BasicBlock(start=2,end=2) -> {BB_5,BB_1}
	BB_5: BasicBlock(start=3,end=4) -> {BB_2}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=8,end=12) -> {BB_8,BB_3}
	BB_8: ExitNode(normalReturn=false)
))

java.util.concurrent.ConcurrentHashMap$TreeNode rotateRight(java.util.concurrent.ConcurrentHashMap$TreeNode,java.util.concurrent.ConcurrentHashMap$TreeNode)
AITACode(params=(Parameters(
	1: useSites={20} (origin=-2),
	2: useSites={0,4,18,6,14,1,19,7} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=20),
	1: Assignment(pc=5,DVar(useSites={8,20,2,18,17,3,19,11,15},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦5;refId=104],origin=1),GetField(pc=5,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]))),
	2: If(pc=10,UVar(defSites={1},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦5;refId=104]),==,NullExpr(pc=-333),target=20),
	3: Assignment(pc=15,DVar(useSites={4,6,5},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦15;refId=105],origin=3),GetField(pc=15,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]))),
	4: PutField(pc=19,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]),UVar(defSites={3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦15;refId=105])),
	5: If(pc=25,UVar(defSites={3},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦15;refId=105]),==,NullExpr(pc=-333),target=7),
	6: PutField(pc=31,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦15;refId=105]),UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103])),
	7: Assignment(pc=36,DVar(useSites={8,17,9,13,15},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦36;refId=106],origin=7),GetField(pc=36,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]))),
	8: PutField(pc=40,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]),UVar(defSites={7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦36;refId=106])),
	9: If(pc=45,UVar(defSites={7},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦36;refId=106]),!=,NullExpr(pc=-333),target=13),
	10: Assignment(pc=51,DVar(useSites={11},value=int = 0,origin=10),IntConst(pc=51,0)),
	11: PutField(pc=52,java.util.concurrent.ConcurrentHashMap$TreeNode,red,boolean,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]),UVar(defSites={10},value=int = 0)),
	12: Goto(pc=55,target=18),
	13: Assignment(pc=59,DVar(useSites={14},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦59;refId=107],origin=13),GetField(pc=59,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦36;refId=106]))),
	14: If(pc=63,UVar(defSites={13},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦59;refId=107]),!=,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]),target=17),
	15: PutField(pc=68,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104])),
	16: Goto(pc=71,target=18),
	17: PutField(pc=76,java.util.concurrent.ConcurrentHashMap$TreeNode,left,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={7},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦36;refId=106]),UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104])),
	18: PutField(pc=81,java.util.concurrent.ConcurrentHashMap$TreeNode,right,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104]),UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103])),
	19: PutField(pc=86,java.util.concurrent.ConcurrentHashMap$TreeNode,parent,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={-3},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦-2;refId=103]),UVar(defSites={1},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104])),
	20: ReturnValue(pc=90,UVar(defSites={-2,1},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=108; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦5;refId=104], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦-1;refId=102]»]))
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

