java.util.HashMap$TreeNode newTreeNode(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={1} (origin=-4),
	4: useSites={1} (origin=-5)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2,1},value=java.util.HashMap$TreeNode[↦0;refId=106],origin=0),New(pc=0,java.util.HashMap$TreeNode)),
	1: NonVirtualMethodCall(pc=9,java.util.HashMap$TreeNode,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={0},value=java.util.HashMap$TreeNode[↦0;refId=106]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={-5},value={_ <: java.util.HashMap$Node, null}[↦-5;refId=105]))),
	2: ReturnValue(pc=12,UVar(defSites={0},value=java.util.HashMap$TreeNode[↦0;refId=106]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void afterNodeAccess(java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={} (origin=-2)
)),stmts=(
	0: Return(pc=0)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

int compareComparables(java.lang.Class,java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	1: useSites={2} (origin=-2),
	2: useSites={6,5} (origin=-3),
	3: useSites={0,6,1} (origin=-4)
)),stmts=(
	0: If(pc=1,UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-3;refId=104]),==,NullExpr(pc=-333),target=3),
	1: Assignment(pc=5,DVar(useSites={2},value={java.lang.Class, null}[↦5;refId=106],origin=1),VirtualFunctionCall(pc=5,java.lang.Object,isInterface=false,java.lang.Class getClass(),UVar(defSites={-4},value=_ <: java.lang.Object[↦-3;refId=104]),())),
	2: If(pc=9,UVar(defSites={1},value={java.lang.Class, null}[↦5;refId=106]),==,UVar(defSites={-2},value={java.lang.Class, null}[↦-1;refId=102]),target=5),
	3: Assignment(pc=12,DVar(useSites={7},value=int = 0,origin=3),IntConst(pc=12,0)),
	4: Goto(pc=13,target=7),
	5: Checkcast(pc=17,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-2;refId=103]),java.lang.Comparable),
	6: Assignment(pc=21,DVar(useSites={7},value=an int,origin=6),VirtualFunctionCall(pc=21,java.lang.Comparable,isInterface=true,int compareTo(java.lang.Object),UVar(defSites={-3},value={_ <: java.lang.Comparable, null}[↦-2;refId=107]),(UVar(defSites={-4},value=_ <: java.lang.Object[↦-3;refId=104])))),
	7: ReturnValue(pc=26,UVar(defSites={6,3},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_2,BB_6}
	BB_1: BasicBlock(start=5,end=5) -> {BB_8,BB_3}
	BB_2: BasicBlock(start=1,end=1) -> {BB_8,BB_4}
	BB_3: BasicBlock(start=6,end=6) -> {BB_8,BB_5}
	BB_4: BasicBlock(start=2,end=2) -> {BB_1,BB_6}
	BB_5: BasicBlock(start=7,end=7) -> {BB_7}
	BB_6: BasicBlock(start=3,end=4) -> {BB_5}
	BB_7: ExitNode(normalReturn=true)
	BB_8: ExitNode(normalReturn=false)
))

boolean isEmpty()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.HashMap,size,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=an int),!=,IntConst(pc=-333,0),target=4),
	2: Assignment(pc=7,DVar(useSites={5},value=int = 1,origin=2),IntConst(pc=7,1)),
	3: Goto(pc=8,target=5),
	4: Assignment(pc=11,DVar(useSites={5},value=int ∈ [0,1],origin=4),IntConst(pc=11,0)),
	5: ReturnValue(pc=12,UVar(defSites={4,2},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=2,end=3) -> {BB_1}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_1}
	BB_5: ExitNode(normalReturn=false)
))

java.util.HashMap$TreeNode replacementTreeNode(java.util.HashMap$Node,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={2,1,3} (origin=-2),
	2: useSites={4} (origin=-3)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={4,5},value=java.util.HashMap$TreeNode[↦0;refId=105],origin=0),New(pc=0,java.util.HashMap$TreeNode)),
	1: Assignment(pc=5,DVar(useSites={4},value=an int,origin=1),GetField(pc=5,java.util.HashMap$Node,hash,int,UVar(defSites={-2},value={_ <: java.util.HashMap$Node, null}[↦-2;refId=103]))),
	2: Assignment(pc=9,DVar(useSites={4},value={_ <: java.lang.Object, null}[↦9;refId=107],origin=2),GetField(pc=9,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[↦-2;refId=103]))),
	3: Assignment(pc=13,DVar(useSites={4},value={_ <: java.lang.Object, null}[↦13;refId=108],origin=3),GetField(pc=13,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[↦-2;refId=103]))),
	4: NonVirtualMethodCall(pc=17,java.util.HashMap$TreeNode,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={0},value=java.util.HashMap$TreeNode[↦0;refId=105]),(UVar(defSites={1},value=an int),UVar(defSites={2},value={_ <: java.lang.Object, null}[↦9;refId=107]),UVar(defSites={3},value={_ <: java.lang.Object, null}[↦13;refId=108]),UVar(defSites={-3},value={_ <: java.util.HashMap$Node, null}[↦-3;refId=104]))),
	5: ReturnValue(pc=20,UVar(defSites={0},value=java.util.HashMap$TreeNode[↦0;refId=105]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=2,end=4) -> {BB_4,BB_1}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

java.util.HashMap$Node getNode(int,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={10,6,22,25} (origin=-2),
	2: useSites={12,28,22,14,13,29,27} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,1,7},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.HashMap,table,java.util.HashMap$Node[],UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	1: If(pc=6,UVar(defSites={0},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=104]),==,NullExpr(pc=-333),target=34),
	2: Assignment(pc=10,DVar(useSites={5,3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=10,UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=104]))),
	3: If(pc=14,UVar(defSites={2},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=34),
	4: Assignment(pc=20,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=20,1)),
	5: Assignment(pc=21,DVar(useSites={6},value=int ∈ [0,2147483646],origin=5),BinaryExpr(pc=21,ComputationalTypeInt,UVar(defSites={2},value=int ∈ [1,2147483647]),-,UVar(defSites={4},value=int = 1))),
	6: Assignment(pc=23,DVar(useSites={7},value=int ∈ [0,2147483646],origin=6),BinaryExpr(pc=23,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,2147483646]),&,UVar(defSites={-2},value=an int))),
	7: Assignment(pc=24,DVar(useSites={16,8,22,17,9,21,19,11},value={_ <: java.util.HashMap$Node, null}[↦24;refId=106],origin=7),ArrayLoad(pc=24,UVar(defSites={6},value=int ∈ [0,2147483646]),UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=104]))),
	8: If(pc=28,UVar(defSites={7},value={_ <: java.util.HashMap$Node, null}[↦24;refId=106]),==,NullExpr(pc=-333),target=34),
	9: Assignment(pc=33,DVar(useSites={10},value=an int,origin=9),GetField(pc=33,java.util.HashMap$Node,hash,int,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦24;refId=106]))),
	10: If(pc=37,UVar(defSites={9},value=an int),!=,UVar(defSites={-2},value=an int),target=17),
	11: Assignment(pc=42,DVar(useSites={12,14},value={_ <: java.lang.Object, null}[↦42;refId=107],origin=11),GetField(pc=42,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦24;refId=106]))),
	12: If(pc=49,UVar(defSites={11},value={_ <: java.lang.Object, null}[↦42;refId=107]),==,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),target=16),
	13: If(pc=53,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),==,NullExpr(pc=-333),target=17),
	14: Assignment(pc=59,DVar(useSites={15},value=int ∈ [0,1],origin=14),VirtualFunctionCall(pc=59,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=103]),(UVar(defSites={11},value={_ <: java.lang.Object, null}[↦42;refId=107])))),
	15: If(pc=62,UVar(defSites={14},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=17),
	16: ReturnValue(pc=67,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦24;refId=106])),
	17: Assignment(pc=70,DVar(useSites={32,24,18,26,31},value={_ <: java.util.HashMap$Node, null}[↦70;refId=109],origin=17),GetField(pc=70,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦24;refId=106]))),
	18: If(pc=76,UVar(defSites={17},value={_ <: java.util.HashMap$Node, null}[↦70;refId=109]),==,NullExpr(pc=-333),target=34),
	19: Assignment(pc=81,DVar(useSites={20},value=int ∈ [0,1],origin=19),InstanceOf(pc=81,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦24;refId=106]),java.util.HashMap$TreeNode)),
	20: If(pc=84,UVar(defSites={19},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=24),
	21: Checkcast(pc=89,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦24;refId=106]),java.util.HashMap$TreeNode),
	22: Assignment(pc=94,DVar(useSites={23},value={java.util.HashMap$TreeNode, null}[↦94;refId=113],origin=22),VirtualFunctionCall(pc=94,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode getTreeNode(int,java.lang.Object),UVar(defSites={7},value=java.util.HashMap$TreeNode[↦24;refId=110]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103])))),
	23: ReturnValue(pc=97,UVar(defSites={22},value={java.util.HashMap$TreeNode, null}[↦94;refId=113])),
	24: Assignment(pc=100,DVar(useSites={25},value=an int,origin=24),GetField(pc=100,java.util.HashMap$Node,hash,int,UVar(defSites={32,17},value=_ <: java.util.HashMap$Node[refId=117; values=«_ <: java.util.HashMap$Node[↦70;refId=109], _ <: java.util.HashMap$Node[↦137;refId=116]»]))),
	25: If(pc=104,UVar(defSites={24},value=an int),!=,UVar(defSites={-2},value=an int),target=32),
	26: Assignment(pc=109,DVar(useSites={29,27},value={_ <: java.lang.Object, null}[↦109;refId=118],origin=26),GetField(pc=109,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={32,17},value=_ <: java.util.HashMap$Node[refId=117; values=«_ <: java.util.HashMap$Node[↦70;refId=109], _ <: java.util.HashMap$Node[↦137;refId=116]»]))),
	27: If(pc=116,UVar(defSites={26},value={_ <: java.lang.Object, null}[↦109;refId=118]),==,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),target=31),
	28: If(pc=120,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),==,NullExpr(pc=-333),target=32),
	29: Assignment(pc=126,DVar(useSites={30},value=int ∈ [0,1],origin=29),VirtualFunctionCall(pc=126,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=103]),(UVar(defSites={26},value={_ <: java.lang.Object, null}[↦109;refId=118])))),
	30: If(pc=129,UVar(defSites={29},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=32),
	31: ReturnValue(pc=134,UVar(defSites={32,17},value=_ <: java.util.HashMap$Node[refId=117; values=«_ <: java.util.HashMap$Node[↦70;refId=109], _ <: java.util.HashMap$Node[↦137;refId=116]»])),
	32: Assignment(pc=137,DVar(useSites={24,26,33,31},value={_ <: java.util.HashMap$Node, null}[↦137;refId=120],origin=32),GetField(pc=137,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={32,17},value=_ <: java.util.HashMap$Node[refId=117; values=«_ <: java.util.HashMap$Node[↦70;refId=109], _ <: java.util.HashMap$Node[↦137;refId=116]»]))),
	33: If(pc=143,UVar(defSites={32},value={_ <: java.util.HashMap$Node, null}[↦137;refId=120]),!=,NullExpr(pc=-333),target=24),
	34: Assignment(pc=146,DVar(useSites={35},value=null[↦146],origin=34),NullExpr(pc=146)),
	35: ReturnValue(pc=147,UVar(defSites={34},value=null[↦146]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_10,BB_6}
	BB_10: BasicBlock(start=34,end=35) -> {BB_8}
	BB_11: BasicBlock(start=16,end=16) -> {BB_8}
	BB_12: BasicBlock(start=31,end=31) -> {BB_8}
	BB_13: BasicBlock(start=26,end=27) -> {BB_12,BB_c}
	BB_14: BasicBlock(start=23,end=23) -> {BB_8}
	BB_15: BasicBlock(start=30,end=30) -> {BB_12,BB_f}
	BB_16: BasicBlock(start=19,end=20) -> {BB_1,BB_d}
	BB_17: BasicBlock(start=4,end=7) -> {BB_18,BB_a}
	BB_18: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=24,end=25) -> {BB_13,BB_f}
	BB_2: BasicBlock(start=14,end=14) -> {BB_18,BB_b}
	BB_3: BasicBlock(start=29,end=29) -> {BB_18,BB_15}
	BB_4: BasicBlock(start=9,end=10) -> {BB_9,BB_e}
	BB_5: BasicBlock(start=13,end=13) -> {BB_2,BB_e}
	BB_6: BasicBlock(start=2,end=3) -> {BB_10,BB_17}
	BB_7: BasicBlock(start=22,end=22) -> {BB_18,BB_14}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=11,end=12) -> {BB_5,BB_11}
	BB_a: BasicBlock(start=8,end=8) -> {BB_10,BB_4}
	BB_b: BasicBlock(start=15,end=15) -> {BB_e,BB_11}
	BB_c: BasicBlock(start=28,end=28) -> {BB_3,BB_f}
	BB_d: BasicBlock(start=21,end=21) -> {BB_18,BB_7}
	BB_e: BasicBlock(start=17,end=18) -> {BB_10,BB_16}
	BB_f: BasicBlock(start=32,end=33) -> {BB_1,BB_10}
))

boolean containsKey(java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={1} (origin=-1),
	1: useSites={0,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),StaticFunctionCall(pc=2,java.util.HashMap,isInterface=false,int hash(java.lang.Object),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	1: Assignment(pc=6,DVar(useSites={2},value={_ <: java.util.HashMap$Node, null}[↦6;refId=106],origin=1),VirtualFunctionCall(pc=6,java.util.HashMap,isInterface=false,java.util.HashMap$Node getNode(int,java.lang.Object),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={0},value=an int),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	2: If(pc=9,UVar(defSites={1},value={_ <: java.util.HashMap$Node, null}[↦6;refId=106]),==,NullExpr(pc=-333),target=5),
	3: Assignment(pc=12,DVar(useSites={6},value=int = 1,origin=3),IntConst(pc=12,1)),
	4: Goto(pc=13,target=6),
	5: Assignment(pc=16,DVar(useSites={6},value=int ∈ [0,1],origin=5),IntConst(pc=16,0)),
	6: ReturnValue(pc=17,UVar(defSites={5,3},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_7,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=1,end=1) -> {BB_7,BB_4}
	BB_3: BasicBlock(start=6,end=6) -> {BB_6}
	BB_4: BasicBlock(start=2,end=2) -> {BB_1,BB_5}
	BB_5: BasicBlock(start=3,end=4) -> {BB_3}
	BB_6: ExitNode(normalReturn=true)
	BB_7: ExitNode(normalReturn=false)
))

java.util.HashMap$Node newNode(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={1} (origin=-4),
	4: useSites={1} (origin=-5)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2,1},value=java.util.HashMap$Node[↦0;refId=106],origin=0),New(pc=0,java.util.HashMap$Node)),
	1: NonVirtualMethodCall(pc=9,java.util.HashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={0},value=java.util.HashMap$Node[↦0;refId=106]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={-5},value={_ <: java.util.HashMap$Node, null}[↦-5;refId=105]))),
	2: ReturnValue(pc=12,UVar(defSites={0},value=java.util.HashMap$Node[↦0;refId=106]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int hash(java.lang.Object)
AITACode(params=(Parameters(
	1: useSites={0,3} (origin=-2)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-1;refId=102]),!=,NullExpr(pc=-333),target=3),
	1: Assignment(pc=4,DVar(useSites={7},value=int = 0,origin=1),IntConst(pc=4,0)),
	2: Goto(pc=5,target=7),
	3: Assignment(pc=9,DVar(useSites={6,5},value=an int,origin=3),VirtualFunctionCall(pc=9,java.lang.Object,isInterface=false,int hashCode(),UVar(defSites={-2},value=_ <: java.lang.Object[↦-1;refId=102]),())),
	4: Assignment(pc=15,DVar(useSites={5},value=int = 16,origin=4),IntConst(pc=15,16)),
	5: Assignment(pc=17,DVar(useSites={6},value=an int,origin=5),BinaryExpr(pc=17,ComputationalTypeInt,UVar(defSites={3},value=an int),>>>,UVar(defSites={4},value=int = 16))),
	6: Assignment(pc=18,DVar(useSites={7},value=an int,origin=6),BinaryExpr(pc=18,ComputationalTypeInt,UVar(defSites={3},value=an int),^,UVar(defSites={5},value=an int))),
	7: ReturnValue(pc=19,UVar(defSites={6,1},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: BasicBlock(start=7,end=7) -> {BB_4}
	BB_3: BasicBlock(start=3,end=3) -> {BB_6,BB_5}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=4,end=6) -> {BB_2}
	BB_6: ExitNode(normalReturn=false)
))

java.lang.Object get(java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={1} (origin=-1),
	1: useSites={0,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),StaticFunctionCall(pc=2,java.util.HashMap,isInterface=false,int hash(java.lang.Object),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	1: Assignment(pc=6,DVar(useSites={2,5},value={_ <: java.util.HashMap$Node, null}[↦6;refId=106],origin=1),VirtualFunctionCall(pc=6,java.util.HashMap,isInterface=false,java.util.HashMap$Node getNode(int,java.lang.Object),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={0},value=an int),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	2: If(pc=11,UVar(defSites={1},value={_ <: java.util.HashMap$Node, null}[↦6;refId=106]),!=,NullExpr(pc=-333),target=5),
	3: Assignment(pc=14,DVar(useSites={6},value=null[↦14],origin=3),NullExpr(pc=14)),
	4: Goto(pc=15,target=6),
	5: Assignment(pc=19,DVar(useSites={6},value={_ <: java.lang.Object, null}[refId=108; values=«null[↦14], {_ <: java.lang.Object, null}[↦19;refId=107]»],origin=5),GetField(pc=19,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={1},value=_ <: java.util.HashMap$Node[↦6;refId=106]))),
	6: ReturnValue(pc=22,UVar(defSites={5,3},value={_ <: java.lang.Object, null}[refId=108; values=«null[↦14], {_ <: java.lang.Object, null}[↦19;refId=107]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_7,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=1,end=1) -> {BB_7,BB_4}
	BB_3: BasicBlock(start=6,end=6) -> {BB_6}
	BB_4: BasicBlock(start=2,end=2) -> {BB_1,BB_5}
	BB_5: BasicBlock(start=3,end=4) -> {BB_3}
	BB_6: ExitNode(normalReturn=true)
	BB_7: ExitNode(normalReturn=false)
))

void afterNodeInsertion(boolean)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={} (origin=-2)
)),stmts=(
	0: Return(pc=0)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

java.util.Set keySet()
AITACode(params=(Parameters(
	0: useSites={0,4,3} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1,5},value={_ <: java.util.Set, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.HashMap,keySet,java.util.Set,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	1: If(pc=6,UVar(defSites={0},value={_ <: java.util.Set, null}[↦1;refId=103]),!=,NullExpr(pc=-333),target=5),
	2: Assignment(pc=9,DVar(useSites={4,5,3},value=java.util.HashMap$KeySet[↦9;refId=104],origin=2),New(pc=9,java.util.HashMap$KeySet)),
	3: NonVirtualMethodCall(pc=14,java.util.HashMap$KeySet,isInterface=false,void <init>(java.util.HashMap),UVar(defSites={2},value=java.util.HashMap$KeySet[↦9;refId=104]),(UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	4: PutField(pc=20,java.util.HashMap,keySet,java.util.Set,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={2},value=java.util.HashMap$KeySet[↦9;refId=104])),
	5: ReturnValue(pc=24,UVar(defSites={0,2},value=_ <: java.util.Set[refId=106; values=«_ <: java.util.Set[↦1;refId=103], java.util.HashMap$KeySet[↦9;refId=104]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_2,BB_1}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=2,end=3) -> {BB_5,BB_4}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_1}
	BB_5: ExitNode(normalReturn=false)
))

java.lang.Class comparableClassFor(java.lang.Object)
AITACode(params=(Parameters(
	1: useSites={0,2} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),InstanceOf(pc=1,UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-1;refId=102]),java.lang.Comparable)),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=29),
	2: Assignment(pc=8,DVar(useSites={4,26,6,25,5},value={java.lang.Class, null}[↦8;refId=105],origin=2),VirtualFunctionCall(pc=8,java.lang.Object,isInterface=false,java.lang.Class getClass(),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-1;refId=102]),())),
	3: Assignment(pc=13,DVar(useSites={4},value=Class<java.lang.String>[↦13;refId=106],origin=3),ClassConst(pc=13,java.lang.String)),
	4: If(pc=15,UVar(defSites={2},value={java.lang.Class, null}[↦8;refId=105]),!=,UVar(defSites={3},value=Class<java.lang.String>[↦13;refId=106]),target=6),
	5: ReturnValue(pc=19,UVar(defSites={2},value={java.lang.Class, null}[↦8;refId=105])),
	6: Assignment(pc=21,DVar(useSites={8,11,7},value={_ <: java.lang.reflect.Type[], null}[↦21;refId=109],origin=6),VirtualFunctionCall(pc=21,java.lang.Class,isInterface=false,java.lang.reflect.Type[] getGenericInterfaces(),UVar(defSites={2},value={java.lang.Class, null}[↦8;refId=105]),())),
	7: If(pc=26,UVar(defSites={6},value={_ <: java.lang.reflect.Type[], null}[↦21;refId=109]),==,NullExpr(pc=-333),target=29),
	8: Assignment(pc=34,DVar(useSites={10},value=int ∈ [0,2147483647],origin=8),ArrayLength(pc=34,UVar(defSites={6},value=_ <: java.lang.reflect.Type[][↦21;refId=109]))),
	9: Assignment(pc=37,DVar(useSites={10,11,27},value=int = 0,origin=9),IntConst(pc=37,0)),
	10: If(pc=44,UVar(defSites={9,27},value=an int),>=,UVar(defSites={8},value=int ∈ [0,2147483647]),target=29),
	11: Assignment(pc=51,DVar(useSites={12,18,14,15},value={_ <: java.lang.reflect.Type, null}[↦51;refId=363],origin=11),ArrayLoad(pc=51,UVar(defSites={9,27},value=int ∈ [-2147483648,2147483646]),UVar(defSites={6},value=_ <: java.lang.reflect.Type[][↦21;refId=109]))),
	12: Assignment(pc=56,DVar(useSites={13},value=int ∈ [0,1],origin=12),InstanceOf(pc=56,UVar(defSites={11},value={_ <: java.lang.reflect.Type, null}[↦51;refId=363]),java.lang.reflect.ParameterizedType)),
	13: If(pc=59,UVar(defSites={12},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=27),
	14: Checkcast(pc=64,UVar(defSites={11},value={_ <: java.lang.reflect.Type, null}[↦51;refId=363]),java.lang.reflect.ParameterizedType),
	15: Assignment(pc=70,DVar(useSites={17},value={_ <: java.lang.reflect.Type, null}[↦70;refId=368],origin=15),VirtualFunctionCall(pc=70,java.lang.reflect.ParameterizedType,isInterface=true,java.lang.reflect.Type getRawType(),UVar(defSites={11},value={_ <: java.lang.reflect.ParameterizedType, null}[↦51;refId=364]),())),
	16: Assignment(pc=75,DVar(useSites={17},value=Class<java.lang.Comparable>[↦75;refId=369],origin=16),ClassConst(pc=75,java.lang.Comparable)),
	17: If(pc=77,UVar(defSites={15},value={_ <: java.lang.reflect.Type, null}[↦70;refId=368]),!=,UVar(defSites={16},value=Class<java.lang.Comparable>[↦75;refId=369]),target=27),
	18: Assignment(pc=82,DVar(useSites={24,20,19},value={_ <: java.lang.reflect.Type[], null}[↦82;refId=371],origin=18),VirtualFunctionCall(pc=82,java.lang.reflect.ParameterizedType,isInterface=true,java.lang.reflect.Type[] getActualTypeArguments(),UVar(defSites={11},value=_ <: java.lang.reflect.ParameterizedType[↦51;refId=364]),())),
	19: If(pc=89,UVar(defSites={18},value={_ <: java.lang.reflect.Type[], null}[↦82;refId=371]),==,NullExpr(pc=-333),target=27),
	20: Assignment(pc=93,DVar(useSites={22},value=int ∈ [0,2147483647],origin=20),ArrayLength(pc=93,UVar(defSites={18},value=_ <: java.lang.reflect.Type[][↦82;refId=371]))),
	21: Assignment(pc=94,DVar(useSites={22},value=int = 1,origin=21),IntConst(pc=94,1)),
	22: If(pc=95,UVar(defSites={20},value=int ∈ [0,2147483647]),!=,UVar(defSites={21},value=int = 1),target=27),
	23: Assignment(pc=99,DVar(useSites={24},value=int = 0,origin=23),IntConst(pc=99,0)),
	24: Assignment(pc=100,DVar(useSites={25},value={_ <: java.lang.reflect.Type, null}[↦100;refId=373],origin=24),ArrayLoad(pc=100,UVar(defSites={23},value=int = 0),UVar(defSites={18},value=_ <: java.lang.reflect.Type[][↦82;refId=371]))),
	25: If(pc=102,UVar(defSites={24},value={_ <: java.lang.reflect.Type, null}[↦100;refId=373]),!=,UVar(defSites={2},value=java.lang.Class[↦8;refId=105]),target=27),
	26: ReturnValue(pc=106,UVar(defSites={2},value=java.lang.Class[↦8;refId=105])),
	27: Assignment(pc=107,DVar(useSites={28,10,11},value=an int,origin=27),BinaryExpr(pc=107,ComputationalTypeInt,UVar(defSites={9,27},value=an int),+,IntConst(pc=107,1))),
	28: Goto(pc=110,target=10),
	29: Assignment(pc=113,DVar(useSites={30},value=null[↦113],origin=29),NullExpr(pc=113)),
	30: ReturnValue(pc=114,UVar(defSites={29},value=null[↦113]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_12,BB_6}
	BB_10: BasicBlock(start=15,end=15) -> {BB_f,BB_b}
	BB_11: BasicBlock(start=20,end=22) -> {BB_16,BB_7}
	BB_12: BasicBlock(start=29,end=30) -> {BB_14}
	BB_13: BasicBlock(start=18,end=18) -> {BB_f,BB_e}
	BB_14: ExitNode(normalReturn=true)
	BB_15: BasicBlock(start=26,end=26) -> {BB_14}
	BB_16: BasicBlock(start=23,end=24) -> {BB_f,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_14}
	BB_2: BasicBlock(start=10,end=10) -> {BB_12,BB_c}
	BB_3: BasicBlock(start=25,end=25) -> {BB_15,BB_7}
	BB_4: BasicBlock(start=14,end=14) -> {BB_f,BB_10}
	BB_5: BasicBlock(start=6,end=6) -> {BB_f,BB_9}
	BB_6: BasicBlock(start=2,end=2) -> {BB_f,BB_a}
	BB_7: BasicBlock(start=27,end=28) -> {BB_2}
	BB_8: BasicBlock(start=12,end=13) -> {BB_4,BB_7}
	BB_9: BasicBlock(start=7,end=7) -> {BB_12,BB_d}
	BB_a: BasicBlock(start=3,end=4) -> {BB_5,BB_1}
	BB_b: BasicBlock(start=16,end=17) -> {BB_13,BB_7}
	BB_c: BasicBlock(start=11,end=11) -> {BB_f,BB_8}
	BB_d: BasicBlock(start=8,end=9) -> {BB_2}
	BB_e: BasicBlock(start=19,end=19) -> {BB_11,BB_7}
	BB_f: ExitNode(normalReturn=false)
))

int size()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),GetField(pc=1,java.util.HashMap,size,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	1: ReturnValue(pc=4,UVar(defSites={0},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

void treeifyBin(java.util.HashMap$Node[],int)
AITACode(params=(Parameters(
	0: useSites={4,14} (origin=-1),
	1: useSites={0,1,9,21,23} (origin=-2),
	2: useSites={8} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={_ <: java.util.HashMap$Node[], null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=4),
	1: Assignment(pc=5,DVar(useSites={3,7},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=5,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[][↦-2;refId=103]))),
	2: Assignment(pc=8,DVar(useSites={3},value=int = 64,origin=2),IntConst(pc=8,64)),
	3: If(pc=10,UVar(defSites={1},value=int ∈ [0,2147483647]),>=,UVar(defSites={2},value=int = 64),target=6),
	4: ExprStmt(pc=14,VirtualFunctionCall(pc=14,java.util.HashMap,isInterface=false,java.util.HashMap$Node[] resize(),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),())),
	5: Goto(pc=18,target=24),
	6: Assignment(pc=23,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=23,1)),
	7: Assignment(pc=24,DVar(useSites={8},value=int ∈ [63,2147483646],origin=7),BinaryExpr(pc=24,ComputationalTypeInt,UVar(defSites={1},value=int ∈ [64,2147483647]),-,UVar(defSites={6},value=int = 1))),
	8: Assignment(pc=26,DVar(useSites={9,21},value=int ∈ [0,2147483646],origin=8),BinaryExpr(pc=26,ComputationalTypeInt,UVar(defSites={7},value=int ∈ [63,2147483646]),&,UVar(defSites={-3},value=an int))),
	9: Assignment(pc=30,DVar(useSites={10,14,19},value={_ <: java.util.HashMap$Node, null}[↦30;refId=105],origin=9),ArrayLoad(pc=30,UVar(defSites={8},value=int ∈ [0,2147483646]),UVar(defSites={-2},value=_ <: java.util.HashMap$Node[][↦-2;refId=103]))),
	10: If(pc=34,UVar(defSites={9},value={_ <: java.util.HashMap$Node, null}[↦30;refId=105]),==,NullExpr(pc=-333),target=24),
	11: Assignment(pc=37,DVar(useSites={22,21,23},value=null[↦37],origin=11),NullExpr(pc=37)),
	12: Assignment(pc=40,DVar(useSites={18,17,15},value=null[↦40],origin=12),NullExpr(pc=40)),
	13: Assignment(pc=46,DVar(useSites={14},value=null[↦46],origin=13),NullExpr(pc=46)),
	14: Assignment(pc=47,DVar(useSites={18,22,17,21,23,15},value={java.util.HashMap$TreeNode, null}[↦47;refId=117],origin=14),VirtualFunctionCall(pc=47,java.util.HashMap,isInterface=false,java.util.HashMap$TreeNode replacementTreeNode(java.util.HashMap$Node,java.util.HashMap$Node),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={9,19},value=_ <: java.util.HashMap$Node[refId=111; values=«_ <: java.util.HashMap$Node[↦30;refId=105], _ <: java.util.HashMap$Node[↦84;refId=110]»]),UVar(defSites={13},value=null[↦46])))),
	15: If(pc=54,UVar(defSites={12,14},value={java.util.HashMap$TreeNode, null}[refId=113; values=«null[↦40], {java.util.HashMap$TreeNode, null}[↦47;refId=109]»]),!=,NullExpr(pc=-333),target=17),
	16: Goto(pc=61,target=19),
	17: PutField(pc=68,java.util.HashMap$TreeNode,prev,java.util.HashMap$TreeNode,UVar(defSites={14},value={java.util.HashMap$TreeNode, null}[↦47;refId=117]),UVar(defSites={12,14},value=java.util.HashMap$TreeNode[↦47;refId=109])),
	18: PutField(pc=75,java.util.HashMap$TreeNode,next,java.util.HashMap$Node,UVar(defSites={12,14},value=java.util.HashMap$TreeNode[↦47;refId=109]),UVar(defSites={14},value=java.util.HashMap$TreeNode[↦47;refId=117])),
	19: Assignment(pc=84,DVar(useSites={20,14},value={_ <: java.util.HashMap$Node, null}[↦84;refId=120],origin=19),GetField(pc=84,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={9,19},value=_ <: java.util.HashMap$Node[refId=111; values=«_ <: java.util.HashMap$Node[↦30;refId=105], _ <: java.util.HashMap$Node[↦84;refId=110]»]))),
	20: If(pc=90,UVar(defSites={19},value={_ <: java.util.HashMap$Node, null}[↦84;refId=120]),!=,NullExpr(pc=-333),target=13),
	21: ArrayStore(pc=99,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[][↦-2;refId=103]),UVar(defSites={8},value=int ∈ [0,2147483646]),UVar(defSites={14,11},value={java.util.HashMap$TreeNode, null}[refId=118; values=«null[↦37], {java.util.HashMap$TreeNode, null}[↦47;refId=109]»])),
	22: If(pc=100,UVar(defSites={14,11},value={java.util.HashMap$TreeNode, null}[refId=118; values=«null[↦37], {java.util.HashMap$TreeNode, null}[↦47;refId=109]»]),==,NullExpr(pc=-333),target=24),
	23: VirtualMethodCall(pc=106,java.util.HashMap$TreeNode,isInterface=false,void treeify(java.util.HashMap$Node[]),UVar(defSites={14,11},value=java.util.HashMap$TreeNode[↦47;refId=109]),(UVar(defSites={-2},value=_ <: java.util.HashMap$Node[][↦-2;refId=103]))),
	24: Return(pc=109)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_11}
	BB_10: ExitNode(normalReturn=true)
	BB_11: BasicBlock(start=4,end=4) -> {BB_12,BB_1}
	BB_12: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=10,end=10) -> {BB_b,BB_3}
	BB_3: BasicBlock(start=24,end=24) -> {BB_10}
	BB_4: BasicBlock(start=1,end=3) -> {BB_5,BB_11}
	BB_5: BasicBlock(start=6,end=9) -> {BB_12,BB_2}
	BB_6: BasicBlock(start=21,end=21) -> {BB_12,BB_9}
	BB_7: BasicBlock(start=13,end=14) -> {BB_12,BB_e}
	BB_8: BasicBlock(start=17,end=17) -> {BB_12,BB_f}
	BB_9: BasicBlock(start=22,end=22) -> {BB_3,BB_c}
	BB_a: BasicBlock(start=16,end=16) -> {BB_d}
	BB_b: BasicBlock(start=11,end=12) -> {BB_7}
	BB_c: BasicBlock(start=23,end=23) -> {BB_12,BB_3}
	BB_d: BasicBlock(start=19,end=20) -> {BB_6,BB_7}
	BB_e: BasicBlock(start=15,end=15) -> {BB_8,BB_a}
	BB_f: BasicBlock(start=18,end=18) -> {BB_d}
))

java.lang.Object put(java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={3} (origin=-1),
	1: useSites={0,3} (origin=-2),
	2: useSites={3} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={3},value=an int,origin=0),StaticFunctionCall(pc=2,java.util.HashMap,isInterface=false,int hash(java.lang.Object),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	1: Assignment(pc=7,DVar(useSites={3},value=int = 0,origin=1),IntConst(pc=7,0)),
	2: Assignment(pc=8,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=8,1)),
	3: Assignment(pc=9,DVar(useSites={4},value={_ <: java.lang.Object, null}[↦9;refId=107],origin=3),VirtualFunctionCall(pc=9,java.util.HashMap,isInterface=false,java.lang.Object putVal(int,java.lang.Object,java.lang.Object,boolean,boolean),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={0},value=an int),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=104]),UVar(defSites={1},value=int = 0),UVar(defSites={2},value=int = 1)))),
	4: ReturnValue(pc=12,UVar(defSites={3},value={_ <: java.lang.Object, null}[↦9;refId=107]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_4,BB_3}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=4,end=4) -> {BB_2}
	BB_4: ExitNode(normalReturn=false)
))

int tableSizeFor(int)
AITACode(params=(Parameters(
	1: useSites={2} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={4},value=int = -1,origin=0),IntConst(pc=0,-1)),
	1: Assignment(pc=2,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=2,1)),
	2: Assignment(pc=3,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=3,ComputationalTypeInt,UVar(defSites={-2},value=an int),-,UVar(defSites={1},value=int = 1))),
	3: Assignment(pc=4,DVar(useSites={4},value=an int,origin=3),StaticFunctionCall(pc=4,java.lang.Integer,isInterface=false,int numberOfLeadingZeros(int),(UVar(defSites={2},value=an int)))),
	4: Assignment(pc=7,DVar(useSites={9,5,13},value=an int,origin=4),BinaryExpr(pc=7,ComputationalTypeInt,UVar(defSites={0},value=int = -1),>>>,UVar(defSites={3},value=an int))),
	5: If(pc=10,UVar(defSites={4},value=an int),>=,IntConst(pc=-333,0),target=8),
	6: Assignment(pc=13,DVar(useSites={14},value=int = 1,origin=6),IntConst(pc=13,1)),
	7: Goto(pc=14,target=14),
	8: Assignment(pc=18,DVar(useSites={9},value=int = 1073741824,origin=8),IntConst(pc=18,1073741824)),
	9: If(pc=20,UVar(defSites={4},value=int ∈ [0,2147483647]),<,UVar(defSites={8},value=int = 1073741824),target=12),
	10: Assignment(pc=23,DVar(useSites={14},value=int = 1073741824,origin=10),IntConst(pc=23,1073741824)),
	11: Goto(pc=25,target=14),
	12: Assignment(pc=29,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=29,1)),
	13: Assignment(pc=30,DVar(useSites={14},value=int ∈ [0,2147483647],origin=13),BinaryExpr(pc=30,ComputationalTypeInt,UVar(defSites={4},value=int ∈ [0,1073741823]),+,UVar(defSites={12},value=int = 1))),
	14: ReturnValue(pc=31,UVar(defSites={10,6,13},value=int ∈ [0,2147483647]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_8,BB_7}
	BB_1: BasicBlock(start=10,end=11) -> {BB_2}
	BB_2: BasicBlock(start=14,end=14) -> {BB_5}
	BB_3: BasicBlock(start=6,end=7) -> {BB_2}
	BB_4: BasicBlock(start=12,end=13) -> {BB_2}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=8,end=9) -> {BB_4,BB_1}
	BB_7: BasicBlock(start=4,end=5) -> {BB_6,BB_3}
	BB_8: ExitNode(normalReturn=false)
))

void <init>(int)
AITACode(params=(Parameters(
	0: useSites={1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=AFloatValue,origin=0),FloatConst(pc=2,0.75)),
	1: NonVirtualMethodCall(pc=4,java.util.HashMap,isInterface=false,void <init>(int,float),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={0},value=AFloatValue))),
	2: Return(pc=7)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.HashMap$Node replacementNode(java.util.HashMap$Node,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={2,1,3} (origin=-2),
	2: useSites={4} (origin=-3)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={4,5},value=java.util.HashMap$Node[↦0;refId=105],origin=0),New(pc=0,java.util.HashMap$Node)),
	1: Assignment(pc=5,DVar(useSites={4},value=an int,origin=1),GetField(pc=5,java.util.HashMap$Node,hash,int,UVar(defSites={-2},value={_ <: java.util.HashMap$Node, null}[↦-2;refId=103]))),
	2: Assignment(pc=9,DVar(useSites={4},value={_ <: java.lang.Object, null}[↦9;refId=107],origin=2),GetField(pc=9,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[↦-2;refId=103]))),
	3: Assignment(pc=13,DVar(useSites={4},value={_ <: java.lang.Object, null}[↦13;refId=108],origin=3),GetField(pc=13,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.HashMap$Node[↦-2;refId=103]))),
	4: NonVirtualMethodCall(pc=17,java.util.HashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={0},value=java.util.HashMap$Node[↦0;refId=105]),(UVar(defSites={1},value=an int),UVar(defSites={2},value={_ <: java.lang.Object, null}[↦9;refId=107]),UVar(defSites={3},value={_ <: java.lang.Object, null}[↦13;refId=108]),UVar(defSites={-3},value={_ <: java.util.HashMap$Node, null}[↦-3;refId=104]))),
	5: ReturnValue(pc=20,UVar(defSites={0},value=java.util.HashMap$Node[↦0;refId=105]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=2,end=4) -> {BB_4,BB_1}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0,2} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.AbstractMap,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value=AFloatValue,origin=1),FloatConst(pc=5,0.75)),
	2: PutField(pc=7,java.util.HashMap,loadFactor,float,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={1},value=AFloatValue)),
	3: Return(pc=10)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.HashMap$Node removeNode(int,java.lang.Object,java.lang.Object,boolean,boolean)
AITACode(params=(Parameters(
	0: useSites={0,56,60,57,53,45,61} (origin=-1),
	1: useSites={26,6,11,23} (origin=-2),
	2: useSites={28,14,30,13,29,23,15} (origin=-3),
	3: useSites={40,38,39} (origin=-4),
	4: useSites={36} (origin=-5),
	5: useSites={45} (origin=-6)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,1,49,45,7},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.HashMap,table,java.util.HashMap$Node[],UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	1: If(pc=7,UVar(defSites={0},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=105]),==,NullExpr(pc=-333),target=63),
	2: Assignment(pc=12,DVar(useSites={5,3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=12,UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=105]))),
	3: If(pc=16,UVar(defSites={2},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=63),
	4: Assignment(pc=23,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=23,1)),
	5: Assignment(pc=24,DVar(useSites={6},value=int ∈ [0,2147483646],origin=5),BinaryExpr(pc=24,ComputationalTypeInt,UVar(defSites={2},value=int ∈ [1,2147483647]),-,UVar(defSites={4},value=int = 1))),
	6: Assignment(pc=26,DVar(useSites={49,7},value=int ∈ [0,2147483646],origin=6),BinaryExpr(pc=26,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,2147483646]),&,UVar(defSites={-2},value=an int))),
	7: Assignment(pc=30,DVar(useSites={48,8,20,52,12,44,18,10,42,22,62,37,45,61,35,51,23,47},value={_ <: java.util.HashMap$Node, null}[↦30;refId=107],origin=7),ArrayLoad(pc=30,UVar(defSites={6},value=int ∈ [0,2147483646]),UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=105]))),
	8: If(pc=34,UVar(defSites={7},value={_ <: java.util.HashMap$Node, null}[↦30;refId=107]),==,NullExpr(pc=-333),target=63),
	9: Assignment(pc=37,DVar(useSites={48,44,42,62,37,45,61,35,51,47},value=null[↦37],origin=9),NullExpr(pc=37)),
	10: Assignment(pc=42,DVar(useSites={11},value=an int,origin=10),GetField(pc=42,java.util.HashMap$Node,hash,int,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦30;refId=107]))),
	11: If(pc=46,UVar(defSites={10},value=an int),!=,UVar(defSites={-2},value=an int),target=18),
	12: Assignment(pc=51,DVar(useSites={13,15},value={_ <: java.lang.Object, null}[↦51;refId=108],origin=12),GetField(pc=51,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦30;refId=107]))),
	13: If(pc=58,UVar(defSites={12},value={_ <: java.lang.Object, null}[↦51;refId=108]),==,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),target=17),
	14: If(pc=62,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),==,NullExpr(pc=-333),target=18),
	15: Assignment(pc=68,DVar(useSites={16},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=68,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=103]),(UVar(defSites={12},value={_ <: java.lang.Object, null}[↦51;refId=108])))),
	16: If(pc=71,UVar(defSites={15},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=18),
	17: Goto(pc=78,target=35),
	18: Assignment(pc=83,DVar(useSites={48,52,44,42,62,33,25,37,45,61,35,19,51,27,47},value={_ <: java.util.HashMap$Node, null}[↦83;refId=110],origin=18),GetField(pc=83,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦30;refId=107]))),
	19: If(pc=89,UVar(defSites={18},value={_ <: java.util.HashMap$Node, null}[↦83;refId=110]),==,NullExpr(pc=-333),target=35),
	20: Assignment(pc=94,DVar(useSites={21},value=int ∈ [0,1],origin=20),InstanceOf(pc=94,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦30;refId=107]),java.util.HashMap$TreeNode)),
	21: If(pc=97,UVar(defSites={20},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=25),
	22: Checkcast(pc=102,UVar(defSites={7},value=_ <: java.util.HashMap$Node[↦30;refId=107]),java.util.HashMap$TreeNode),
	23: Assignment(pc=107,DVar(useSites={48,44,42,62,37,45,61,35,51,47},value={java.util.HashMap$TreeNode, null}[↦107;refId=114],origin=23),VirtualFunctionCall(pc=107,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode getTreeNode(int,java.lang.Object),UVar(defSites={7},value=java.util.HashMap$TreeNode[↦30;refId=111]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103])))),
	24: Goto(pc=112,target=35),
	25: Assignment(pc=117,DVar(useSites={26},value=an int,origin=25),GetField(pc=117,java.util.HashMap$Node,hash,int,UVar(defSites={18,33},value=_ <: java.util.HashMap$Node[refId=156; values=«_ <: java.util.HashMap$Node[↦83;refId=110], _ <: java.util.HashMap$Node[↦162;refId=153]»]))),
	26: If(pc=121,UVar(defSites={25},value=an int),!=,UVar(defSites={-2},value=an int),target=33),
	27: Assignment(pc=126,DVar(useSites={28,30},value={_ <: java.lang.Object, null}[↦126;refId=171],origin=27),GetField(pc=126,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={18,33},value=_ <: java.util.HashMap$Node[refId=156; values=«_ <: java.util.HashMap$Node[↦83;refId=110], _ <: java.util.HashMap$Node[↦162;refId=153]»]))),
	28: If(pc=133,UVar(defSites={27},value={_ <: java.lang.Object, null}[↦126;refId=171]),==,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),target=32),
	29: If(pc=137,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),==,NullExpr(pc=-333),target=33),
	30: Assignment(pc=143,DVar(useSites={31},value=int ∈ [0,1],origin=30),VirtualFunctionCall(pc=143,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=103]),(UVar(defSites={27},value={_ <: java.lang.Object, null}[↦126;refId=171])))),
	31: If(pc=146,UVar(defSites={30},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=33),
	32: Goto(pc=153,target=35),
	33: Assignment(pc=162,DVar(useSites={48,52,44,34,42,62,25,37,45,61,35,51,27,47},value={_ <: java.util.HashMap$Node, null}[↦162;refId=153],origin=33),GetField(pc=162,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={18,33},value=_ <: java.util.HashMap$Node[refId=132; values=«_ <: java.util.HashMap$Node[↦83;refId=110], _ <: java.util.HashMap$Node[↦162;refId=129]»]))),
	34: If(pc=168,UVar(defSites={33},value={_ <: java.util.HashMap$Node, null}[↦162;refId=153]),!=,NullExpr(pc=-333),target=25),
	35: If(pc=173,UVar(defSites={18,33,9,7,23},value={_ <: java.util.HashMap$Node, null}[refId=158; values=«null[↦37], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], {java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦83;refId=110]»]),==,NullExpr(pc=-333),target=63),
	36: If(pc=178,UVar(defSites={-5},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=42),
	37: Assignment(pc=183,DVar(useSites={40,38},value={_ <: java.lang.Object, null}[↦183;refId=164],origin=37),GetField(pc=183,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=161; values=«_ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], {java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦83;refId=110]»]))),
	38: If(pc=190,UVar(defSites={37},value={_ <: java.lang.Object, null}[↦183;refId=164]),==,UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),target=42),
	39: If(pc=194,UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),==,NullExpr(pc=-333),target=63),
	40: Assignment(pc=200,DVar(useSites={41},value=int ∈ [0,1],origin=40),VirtualFunctionCall(pc=200,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-4},value=_ <: java.lang.Object[↦-4;refId=104]),(UVar(defSites={37},value={_ <: java.lang.Object, null}[↦183;refId=164])))),
	41: If(pc=203,UVar(defSites={40},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=63),
	42: Assignment(pc=208,DVar(useSites={43},value=int ∈ [0,1],origin=42),InstanceOf(pc=208,UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=163; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»]),java.util.HashMap$TreeNode)),
	43: If(pc=211,UVar(defSites={42},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=47),
	44: Checkcast(pc=216,UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=163; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»]),java.util.HashMap$TreeNode),
	45: VirtualMethodCall(pc=224,java.util.HashMap$TreeNode,isInterface=false,void removeTreeNode(java.util.HashMap,java.util.HashMap$Node[],boolean),UVar(defSites={18,33,9,7,23},value=java.util.HashMap$TreeNode[refId=163; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»]),(UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=105]),UVar(defSites={-6},value=int ∈ [0,1]))),
	46: Goto(pc=227,target=53),
	47: If(pc=234,UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=163; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»]),!=,UVar(defSites={18,33,7},value=_ <: java.util.HashMap$Node[refId=162; values=«_ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦83;refId=110], _ <: java.util.HashMap$Node[↦162;refId=129]»]),target=51),
	48: Assignment(pc=243,DVar(useSites={49},value={_ <: java.util.HashMap$Node, null}[↦243;refId=184],origin=48),GetField(pc=243,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=163; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»]))),
	49: ArrayStore(pc=246,UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=105]),UVar(defSites={6},value=int ∈ [0,2147483646]),UVar(defSites={48},value={_ <: java.util.HashMap$Node, null}[↦243;refId=184])),
	50: Goto(pc=247,target=53),
	51: Assignment(pc=254,DVar(useSites={52},value={_ <: java.util.HashMap$Node, null}[↦254;refId=182],origin=51),GetField(pc=254,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=163; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»]))),
	52: PutField(pc=257,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={18,33,7},value=_ <: java.util.HashMap$Node[refId=162; values=«_ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦83;refId=110], _ <: java.util.HashMap$Node[↦162;refId=129]»]),UVar(defSites={51},value={_ <: java.util.HashMap$Node, null}[↦254;refId=182])),
	53: Assignment(pc=262,DVar(useSites={55},value=an int,origin=53),GetField(pc=262,java.util.HashMap,modCount,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	54: Assignment(pc=265,DVar(useSites={55},value=int = 1,origin=54),IntConst(pc=265,1)),
	55: Assignment(pc=266,DVar(useSites={56},value=an int,origin=55),BinaryExpr(pc=266,ComputationalTypeInt,UVar(defSites={53},value=an int),+,UVar(defSites={54},value=int = 1))),
	56: PutField(pc=267,java.util.HashMap,modCount,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={55},value=an int)),
	57: Assignment(pc=272,DVar(useSites={59},value=an int,origin=57),GetField(pc=272,java.util.HashMap,size,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	58: Assignment(pc=275,DVar(useSites={59},value=int = 1,origin=58),IntConst(pc=275,1)),
	59: Assignment(pc=276,DVar(useSites={60},value=an int,origin=59),BinaryExpr(pc=276,ComputationalTypeInt,UVar(defSites={57},value=an int),-,UVar(defSites={58},value=int = 1))),
	60: PutField(pc=277,java.util.HashMap,size,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={59},value=an int)),
	61: VirtualMethodCall(pc=283,java.util.HashMap,isInterface=false,void afterNodeRemoval(java.util.HashMap$Node),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=181; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»]))),
	62: ReturnValue(pc=288,UVar(defSites={18,33,9,7,23},value=_ <: java.util.HashMap$Node[refId=181; values=«{java.util.HashMap$TreeNode, null}[↦107;refId=114], _ <: java.util.HashMap$Node[↦30;refId=107], _ <: java.util.HashMap$Node[↦162;refId=129], _ <: java.util.HashMap$Node[↦83;refId=110]»])),
	63: Assignment(pc=289,DVar(useSites={64},value=null[↦289],origin=63),NullExpr(pc=289)),
	64: ReturnValue(pc=290,UVar(defSites={63},value=null[↦289]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_19}
	BB_10: BasicBlock(start=9,end=11) -> {BB_1a,BB_5}
	BB_11: BasicBlock(start=53,end=61) -> {BB_25,BB_28}
	BB_12: BasicBlock(start=32,end=32) -> {BB_7}
	BB_13: BasicBlock(start=45,end=45) -> {BB_25,BB_e}
	BB_14: BasicBlock(start=17,end=17) -> {BB_7}
	BB_15: BasicBlock(start=22,end=22) -> {BB_25,BB_20}
	BB_16: BasicBlock(start=44,end=44) -> {BB_25,BB_13}
	BB_17: BasicBlock(start=27,end=28) -> {BB_f,BB_12}
	BB_18: BasicBlock(start=48,end=49) -> {BB_25,BB_1c}
	BB_19: BasicBlock(start=63,end=64) -> {BB_1b}
	BB_1: BasicBlock(start=14,end=14) -> {BB_27,BB_1a}
	BB_1a: BasicBlock(start=18,end=19) -> {BB_d,BB_7}
	BB_1b: ExitNode(normalReturn=true)
	BB_1c: BasicBlock(start=50,end=50) -> {BB_11}
	BB_1d: BasicBlock(start=16,end=16) -> {BB_14,BB_1a}
	BB_1e: BasicBlock(start=31,end=31) -> {BB_2,BB_12}
	BB_1f: BasicBlock(start=40,end=40) -> {BB_25,BB_3}
	BB_20: BasicBlock(start=23,end=23) -> {BB_25,BB_a}
	BB_21: BasicBlock(start=36,end=36) -> {BB_9,BB_b}
	BB_22: BasicBlock(start=30,end=30) -> {BB_25,BB_1e}
	BB_23: BasicBlock(start=51,end=52) -> {BB_11}
	BB_24: BasicBlock(start=4,end=7) -> {BB_25,BB_8}
	BB_25: ExitNode(normalReturn=false)
	BB_26: BasicBlock(start=47,end=47) -> {BB_23,BB_18}
	BB_27: BasicBlock(start=15,end=15) -> {BB_25,BB_1d}
	BB_28: BasicBlock(start=62,end=62) -> {BB_1b}
	BB_2: BasicBlock(start=33,end=34) -> {BB_c,BB_7}
	BB_3: BasicBlock(start=41,end=41) -> {BB_9,BB_19}
	BB_4: BasicBlock(start=2,end=3) -> {BB_19,BB_24}
	BB_5: BasicBlock(start=12,end=13) -> {BB_14,BB_1}
	BB_6: BasicBlock(start=39,end=39) -> {BB_19,BB_1f}
	BB_7: BasicBlock(start=35,end=35) -> {BB_21,BB_19}
	BB_8: BasicBlock(start=8,end=8) -> {BB_19,BB_10}
	BB_9: BasicBlock(start=42,end=43) -> {BB_26,BB_16}
	BB_a: BasicBlock(start=24,end=24) -> {BB_7}
	BB_b: BasicBlock(start=37,end=38) -> {BB_9,BB_6}
	BB_c: BasicBlock(start=25,end=26) -> {BB_2,BB_17}
	BB_d: BasicBlock(start=20,end=21) -> {BB_15,BB_c}
	BB_e: BasicBlock(start=46,end=46) -> {BB_11}
	BB_f: BasicBlock(start=29,end=29) -> {BB_22,BB_2}
))

void <init>(int,float)
AITACode(params=(Parameters(
	0: useSites={0,28,30} (origin=-1),
	1: useSites={12,1,29,7} (origin=-2),
	2: useSites={24,28,17,15} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.AbstractMap,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),()),
	1: If(pc=5,UVar(defSites={-2},value=an int),>=,IntConst(pc=-333,0),target=11),
	2: Assignment(pc=8,DVar(useSites={10,9},value=java.lang.IllegalArgumentException[↦8;refId=104],origin=2),New(pc=8,java.lang.IllegalArgumentException)),
	3: Assignment(pc=12,DVar(useSites={4,6},value=java.lang.StringBuilder[↦12;refId=105],origin=3),New(pc=12,java.lang.StringBuilder)),
	4: NonVirtualMethodCall(pc=16,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={3},value=java.lang.StringBuilder[↦12;refId=105]),()),
	5: Assignment(pc=19,DVar(useSites={6},value=String("Illegal initial capacity: ")[@19;refId=107],origin=5),StringConst(pc=19,Illegal initial capacity: )),
	6: Assignment(pc=21,DVar(useSites={7},value={java.lang.StringBuilder, null}[↦21;refId=109],origin=6),VirtualFunctionCall(pc=21,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={3},value=java.lang.StringBuilder[↦12;refId=105]),(UVar(defSites={5},value=String("Illegal initial capacity: ")[@19;refId=107])))),
	7: Assignment(pc=25,DVar(useSites={8},value={java.lang.StringBuilder, null}[↦25;refId=112],origin=7),VirtualFunctionCall(pc=25,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(int),UVar(defSites={6},value={java.lang.StringBuilder, null}[↦21;refId=109]),(UVar(defSites={-2},value=int ∈ [-2147483648,-1])))),
	8: Assignment(pc=28,DVar(useSites={9},value={java.lang.String, null}[↦28;refId=115],origin=8),VirtualFunctionCall(pc=28,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={7},value={java.lang.StringBuilder, null}[↦25;refId=112]),())),
	9: NonVirtualMethodCall(pc=31,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={2},value=java.lang.IllegalArgumentException[↦8;refId=104]),(UVar(defSites={8},value={java.lang.String, null}[↦28;refId=115]))),
	10: Throw(pc=34,UVar(defSites={2},value=java.lang.IllegalArgumentException[↦8;refId=104])),
	11: Assignment(pc=36,DVar(useSites={12},value=int = 1073741824,origin=11),IntConst(pc=36,1073741824)),
	12: If(pc=38,UVar(defSites={-2},value=int ∈ [0,2147483647]),<=,UVar(defSites={11},value=int = 1073741824),target=14),
	13: Assignment(pc=41,DVar(useSites={29},value=int = 1073741824,origin=13),IntConst(pc=41,1073741824)),
	14: Assignment(pc=45,DVar(useSites={15},value=AFloatValue,origin=14),FloatConst(pc=45,0.0)),
	15: Assignment(pc=46,DVar(useSites={16},value=an int,origin=15),Compare(pc=46,UVar(defSites={-3},value=AFloatValue),cmpg,UVar(defSites={14},value=AFloatValue))),
	16: If(pc=47,UVar(defSites={15},value=an int),<=,IntConst(pc=-333,0),target=19),
	17: Assignment(pc=51,DVar(useSites={18},value=int ∈ [0,1],origin=17),StaticFunctionCall(pc=51,java.lang.Float,isInterface=false,boolean isNaN(float),(UVar(defSites={-3},value=AFloatValue)))),
	18: If(pc=54,UVar(defSites={17},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=28),
	19: Assignment(pc=57,DVar(useSites={26,27},value=java.lang.IllegalArgumentException[↦57;refId=119],origin=19),New(pc=57,java.lang.IllegalArgumentException)),
	20: Assignment(pc=61,DVar(useSites={21,23},value=java.lang.StringBuilder[↦61;refId=120],origin=20),New(pc=61,java.lang.StringBuilder)),
	21: NonVirtualMethodCall(pc=65,java.lang.StringBuilder,isInterface=false,void <init>(),UVar(defSites={20},value=java.lang.StringBuilder[↦61;refId=120]),()),
	22: Assignment(pc=68,DVar(useSites={23},value=String("Illegal load factor: ")[@68;refId=122],origin=22),StringConst(pc=68,Illegal load factor: )),
	23: Assignment(pc=70,DVar(useSites={24},value={java.lang.StringBuilder, null}[↦70;refId=124],origin=23),VirtualFunctionCall(pc=70,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(java.lang.String),UVar(defSites={20},value=java.lang.StringBuilder[↦61;refId=120]),(UVar(defSites={22},value=String("Illegal load factor: ")[@68;refId=122])))),
	24: Assignment(pc=74,DVar(useSites={25},value={java.lang.StringBuilder, null}[↦74;refId=127],origin=24),VirtualFunctionCall(pc=74,java.lang.StringBuilder,isInterface=false,java.lang.StringBuilder append(float),UVar(defSites={23},value={java.lang.StringBuilder, null}[↦70;refId=124]),(UVar(defSites={-3},value=AFloatValue)))),
	25: Assignment(pc=77,DVar(useSites={26},value={java.lang.String, null}[↦77;refId=130],origin=25),VirtualFunctionCall(pc=77,java.lang.StringBuilder,isInterface=false,java.lang.String toString(),UVar(defSites={24},value={java.lang.StringBuilder, null}[↦74;refId=127]),())),
	26: NonVirtualMethodCall(pc=80,java.lang.IllegalArgumentException,isInterface=false,void <init>(java.lang.String),UVar(defSites={19},value=java.lang.IllegalArgumentException[↦57;refId=119]),(UVar(defSites={25},value={java.lang.String, null}[↦77;refId=130]))),
	27: Throw(pc=83,UVar(defSites={19},value=java.lang.IllegalArgumentException[↦57;refId=119])),
	28: PutField(pc=86,java.util.HashMap,loadFactor,float,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={-3},value=AFloatValue)),
	29: Assignment(pc=91,DVar(useSites={30},value=an int,origin=29),StaticFunctionCall(pc=91,java.util.HashMap,isInterface=false,int tableSizeFor(int),(UVar(defSites={-2,13},value=int ∈ [0,1073741824])))),
	30: PutField(pc=94,java.util.HashMap,threshold,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={29},value=an int)),
	31: Return(pc=97)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_e,BB_4}
	BB_10: BasicBlock(start=25,end=25) -> {BB_e,BB_c}
	BB_11: BasicBlock(start=22,end=23) -> {BB_e,BB_f}
	BB_12: BasicBlock(start=27,end=27) -> {BB_e}
	BB_13: BasicBlock(start=18,end=18) -> {BB_5,BB_16}
	BB_14: ExitNode(normalReturn=true)
	BB_15: BasicBlock(start=30,end=31) -> {BB_14}
	BB_16: BasicBlock(start=19,end=21) -> {BB_e,BB_11}
	BB_1: BasicBlock(start=5,end=6) -> {BB_e,BB_a}
	BB_2: BasicBlock(start=10,end=10) -> {BB_e}
	BB_3: BasicBlock(start=14,end=16) -> {BB_9,BB_16}
	BB_4: BasicBlock(start=1,end=1) -> {BB_8,BB_b}
	BB_5: BasicBlock(start=28,end=29) -> {BB_e,BB_15}
	BB_6: BasicBlock(start=9,end=9) -> {BB_e,BB_2}
	BB_7: BasicBlock(start=13,end=13) -> {BB_3}
	BB_8: BasicBlock(start=2,end=4) -> {BB_e,BB_1}
	BB_9: BasicBlock(start=17,end=17) -> {BB_e,BB_13}
	BB_a: BasicBlock(start=7,end=7) -> {BB_e,BB_d}
	BB_b: BasicBlock(start=11,end=12) -> {BB_3,BB_7}
	BB_c: BasicBlock(start=26,end=26) -> {BB_e,BB_12}
	BB_d: BasicBlock(start=8,end=8) -> {BB_e,BB_6}
	BB_e: ExitNode(normalReturn=false)
	BB_f: BasicBlock(start=24,end=24) -> {BB_e,BB_10}
))

java.lang.Object putVal(int,java.lang.Object,java.lang.Object,boolean,boolean)
AITACode(params=(Parameters(
	0: useSites={0,64,56,4,68,60,66,54,33,37,13,27,59,63} (origin=-1),
	1: useSites={40,33,17,9,37,13,27} (origin=-2),
	2: useSites={20,44,42,33,21,13,19,43,27} (origin=-3),
	3: useSites={33,53,13,27} (origin=-4),
	4: useSites={51} (origin=-5),
	5: useSites={68} (origin=-6)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,10,14,1,37,27},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.HashMap,table,java.util.HashMap$Node[],UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	1: If(pc=7,UVar(defSites={0},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=105]),==,NullExpr(pc=-333),target=4),
	2: Assignment(pc=12,DVar(useSites={8,3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=12,UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=105]))),
	3: If(pc=16,UVar(defSites={2},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=7),
	4: Assignment(pc=20,DVar(useSites={10,14,5,37,27},value={_ <: java.util.HashMap$Node[], null}[↦20;refId=107],origin=4),VirtualFunctionCall(pc=20,java.util.HashMap,isInterface=false,java.util.HashMap$Node[] resize(),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),())),
	5: Assignment(pc=26,DVar(useSites={8},value=int ∈ [0,2147483647],origin=5),ArrayLength(pc=26,UVar(defSites={4},value={_ <: java.util.HashMap$Node[], null}[↦20;refId=107]))),
	6: Nop(pc=27),
	7: Assignment(pc=33,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=33,1)),
	8: Assignment(pc=34,DVar(useSites={9},value=int ∈ [-1,2147483646],origin=8),BinaryExpr(pc=34,ComputationalTypeInt,UVar(defSites={2,5},value=int ∈ [0,2147483647]),-,UVar(defSites={7},value=int = 1))),
	9: Assignment(pc=36,DVar(useSites={10,14},value=an int,origin=9),BinaryExpr(pc=36,ComputationalTypeInt,UVar(defSites={8},value=int ∈ [-1,2147483646]),&,UVar(defSites={-2},value=an int))),
	10: Assignment(pc=40,DVar(useSites={16,24,34,18,50,26,54,30,49,53,11,27},value={_ <: java.util.HashMap$Node, null}[↦40;refId=111],origin=10),ArrayLoad(pc=40,UVar(defSites={9},value=an int),UVar(defSites={0,4},value=_ <: java.util.HashMap$Node[][refId=109; values=«_ <: java.util.HashMap$Node[][↦1;refId=105], _ <: java.util.HashMap$Node[][↦20;refId=107]»]))),
	11: If(pc=44,UVar(defSites={10},value={_ <: java.util.HashMap$Node, null}[↦40;refId=111]),!=,NullExpr(pc=-333),target=16),
	12: Assignment(pc=55,DVar(useSites={13},value=null[↦55],origin=12),NullExpr(pc=55)),
	13: Assignment(pc=56,DVar(useSites={14},value={_ <: java.util.HashMap$Node, null}[↦56;refId=115],origin=13),VirtualFunctionCall(pc=56,java.util.HashMap,isInterface=false,java.util.HashMap$Node newNode(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={12},value=null[↦55])))),
	14: ArrayStore(pc=59,UVar(defSites={0,4},value=_ <: java.util.HashMap$Node[][refId=109; values=«_ <: java.util.HashMap$Node[][↦1;refId=105], _ <: java.util.HashMap$Node[][↦20;refId=107]»]),UVar(defSites={9},value=an int),UVar(defSites={13},value={_ <: java.util.HashMap$Node, null}[↦56;refId=115])),
	15: Goto(pc=60,target=56),
	16: Assignment(pc=65,DVar(useSites={17},value=an int,origin=16),GetField(pc=65,java.util.HashMap$Node,hash,int,UVar(defSites={10},value=_ <: java.util.HashMap$Node[↦40;refId=111]))),
	17: If(pc=69,UVar(defSites={16},value=an int),!=,UVar(defSites={-2},value=an int),target=24),
	18: Assignment(pc=74,DVar(useSites={21,19},value={_ <: java.lang.Object, null}[↦74;refId=120],origin=18),GetField(pc=74,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={10},value=_ <: java.util.HashMap$Node[↦40;refId=111]))),
	19: If(pc=81,UVar(defSites={18},value={_ <: java.lang.Object, null}[↦74;refId=120]),==,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),target=23),
	20: If(pc=85,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),==,NullExpr(pc=-333),target=24),
	21: Assignment(pc=91,DVar(useSites={22},value=int ∈ [0,1],origin=21),VirtualFunctionCall(pc=91,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=103]),(UVar(defSites={18},value={_ <: java.lang.Object, null}[↦74;refId=120])))),
	22: If(pc=94,UVar(defSites={21},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=24),
	23: Goto(pc=101,target=49),
	24: Assignment(pc=106,DVar(useSites={25},value=int ∈ [0,1],origin=24),InstanceOf(pc=106,UVar(defSites={10},value=_ <: java.util.HashMap$Node[↦40;refId=111]),java.util.HashMap$TreeNode)),
	25: If(pc=109,UVar(defSites={24},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=29),
	26: Checkcast(pc=114,UVar(defSites={10},value=_ <: java.util.HashMap$Node[↦40;refId=111]),java.util.HashMap$TreeNode),
	27: Assignment(pc=123,DVar(useSites={50,54,49,53},value={java.util.HashMap$TreeNode, null}[↦123;refId=127],origin=27),VirtualFunctionCall(pc=123,java.util.HashMap$TreeNode,isInterface=false,java.util.HashMap$TreeNode putTreeVal(java.util.HashMap,java.util.HashMap$Node[],int,java.lang.Object,java.lang.Object),UVar(defSites={10},value=java.util.HashMap$TreeNode[↦40;refId=124]),(UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={0,4},value=_ <: java.util.HashMap$Node[][refId=109; values=«_ <: java.util.HashMap$Node[][↦1;refId=105], _ <: java.util.HashMap$Node[][↦20;refId=107]»]),UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104])))),
	28: Goto(pc=128,target=49),
	29: Assignment(pc=131,DVar(useSites={36,47},value=int = 0,origin=29),IntConst(pc=131,0)),
	30: Assignment(pc=136,DVar(useSites={34,50,54,49,41,53,39,31},value={_ <: java.util.HashMap$Node, null}[↦136;refId=301],origin=30),GetField(pc=136,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={10,30},value=_ <: java.util.HashMap$Node[refId=300; values=«_ <: java.util.HashMap$Node[↦40;refId=111], _ <: java.util.HashMap$Node[↦136;refId=293]»]))),
	31: If(pc=142,UVar(defSites={30},value={_ <: java.util.HashMap$Node, null}[↦136;refId=301]),!=,NullExpr(pc=-333),target=39),
	32: Assignment(pc=151,DVar(useSites={33},value=null[↦151],origin=32),NullExpr(pc=151)),
	33: Assignment(pc=152,DVar(useSites={34},value={_ <: java.util.HashMap$Node, null}[↦152;refId=303],origin=33),VirtualFunctionCall(pc=152,java.util.HashMap,isInterface=false,java.util.HashMap$Node newNode(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={32},value=null[↦151])))),
	34: PutField(pc=155,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={10,30},value=_ <: java.util.HashMap$Node[refId=300; values=«_ <: java.util.HashMap$Node[↦40;refId=111], _ <: java.util.HashMap$Node[↦136;refId=293]»]),UVar(defSites={33},value={_ <: java.util.HashMap$Node, null}[↦152;refId=303])),
	35: Assignment(pc=160,DVar(useSites={36},value=int = 7,origin=35),IntConst(pc=160,7)),
	36: If(pc=162,UVar(defSites={29,47},value=an int),<,UVar(defSites={35},value=int = 7),target=49),
	37: VirtualMethodCall(pc=169,java.util.HashMap,isInterface=false,void treeifyBin(java.util.HashMap$Node[],int),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={0,4},value=_ <: java.util.HashMap$Node[][refId=109; values=«_ <: java.util.HashMap$Node[][↦1;refId=105], _ <: java.util.HashMap$Node[][↦20;refId=107]»]),UVar(defSites={-2},value=an int))),
	38: Goto(pc=172,target=49),
	39: Assignment(pc=177,DVar(useSites={40},value=an int,origin=39),GetField(pc=177,java.util.HashMap$Node,hash,int,UVar(defSites={30},value=_ <: java.util.HashMap$Node[↦136;refId=301]))),
	40: If(pc=181,UVar(defSites={39},value=an int),!=,UVar(defSites={-2},value=an int),target=47),
	41: Assignment(pc=186,DVar(useSites={44,42},value={_ <: java.lang.Object, null}[↦186;refId=305],origin=41),GetField(pc=186,java.util.HashMap$Node,key,java.lang.Object,UVar(defSites={30},value=_ <: java.util.HashMap$Node[↦136;refId=301]))),
	42: If(pc=193,UVar(defSites={41},value={_ <: java.lang.Object, null}[↦186;refId=305]),==,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),target=49),
	43: If(pc=197,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),==,NullExpr(pc=-333),target=47),
	44: Assignment(pc=203,DVar(useSites={45},value=int ∈ [0,1],origin=44),VirtualFunctionCall(pc=203,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=103]),(UVar(defSites={41},value={_ <: java.lang.Object, null}[↦186;refId=305])))),
	45: If(pc=206,UVar(defSites={44},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=49),
	46: Nop(pc=209),
	47: Assignment(pc=216,DVar(useSites={48,36},value=an int,origin=47),BinaryExpr(pc=216,ComputationalTypeInt,UVar(defSites={29,47},value=an int),+,IntConst(pc=216,1))),
	48: Goto(pc=219,target=30),
	49: If(pc=224,UVar(defSites={10,30,27},value={_ <: java.util.HashMap$Node, null}[refId=136; values=«{java.util.HashMap$TreeNode, null}[↦123;refId=127], _ <: java.util.HashMap$Node[↦40;refId=111], {_ <: java.util.HashMap$Node, null}[↦136;refId=131]»]),==,NullExpr(pc=-333),target=56),
	50: Assignment(pc=229,DVar(useSites={52,55},value={_ <: java.lang.Object, null}[↦229;refId=140],origin=50),GetField(pc=229,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={10,30,27},value=_ <: java.util.HashMap$Node[refId=136; values=«{java.util.HashMap$TreeNode, null}[↦123;refId=127], _ <: java.util.HashMap$Node[↦40;refId=111], {_ <: java.util.HashMap$Node, null}[↦136;refId=131]»]))),
	51: If(pc=236,UVar(defSites={-5},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=53),
	52: If(pc=241,UVar(defSites={50},value={_ <: java.lang.Object, null}[↦229;refId=140]),!=,NullExpr(pc=-333),target=54),
	53: PutField(pc=247,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={10,30,27},value=_ <: java.util.HashMap$Node[refId=141; values=«{java.util.HashMap$TreeNode, null}[↦123;refId=127], _ <: java.util.HashMap$Node[↦40;refId=111], {_ <: java.util.HashMap$Node, null}[↦136;refId=131]»]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104])),
	54: VirtualMethodCall(pc=253,java.util.HashMap,isInterface=false,void afterNodeAccess(java.util.HashMap$Node),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={10,30,27},value=_ <: java.util.HashMap$Node[refId=142; values=«{java.util.HashMap$TreeNode, null}[↦123;refId=127], _ <: java.util.HashMap$Node[↦40;refId=111], {_ <: java.util.HashMap$Node, null}[↦136;refId=131]»]))),
	55: ReturnValue(pc=258,UVar(defSites={50},value={_ <: java.lang.Object, null}[↦229;refId=140])),
	56: Assignment(pc=261,DVar(useSites={58},value=an int,origin=56),GetField(pc=261,java.util.HashMap,modCount,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	57: Assignment(pc=264,DVar(useSites={58},value=int = 1,origin=57),IntConst(pc=264,1)),
	58: Assignment(pc=265,DVar(useSites={59},value=an int,origin=58),BinaryExpr(pc=265,ComputationalTypeInt,UVar(defSites={56},value=an int),+,UVar(defSites={57},value=int = 1))),
	59: PutField(pc=266,java.util.HashMap,modCount,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={58},value=an int)),
	60: Assignment(pc=271,DVar(useSites={62},value=an int,origin=60),GetField(pc=271,java.util.HashMap,size,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	61: Assignment(pc=274,DVar(useSites={62},value=int = 1,origin=61),IntConst(pc=274,1)),
	62: Assignment(pc=275,DVar(useSites={65,63},value=an int,origin=62),BinaryExpr(pc=275,ComputationalTypeInt,UVar(defSites={60},value=an int),+,UVar(defSites={61},value=int = 1))),
	63: PutField(pc=277,java.util.HashMap,size,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={62},value=an int)),
	64: Assignment(pc=281,DVar(useSites={65},value=an int,origin=64),GetField(pc=281,java.util.HashMap,threshold,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	65: If(pc=284,UVar(defSites={62},value=an int),<=,UVar(defSites={64},value=an int),target=68),
	66: ExprStmt(pc=288,VirtualFunctionCall(pc=288,java.util.HashMap,isInterface=false,java.util.HashMap$Node[] resize(),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),())),
	67: Nop(pc=291),
	68: VirtualMethodCall(pc=295,java.util.HashMap,isInterface=false,void afterNodeInsertion(boolean),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={-6},value=int ∈ [0,1]))),
	69: Assignment(pc=298,DVar(useSites={70},value=null[↦298],origin=69),NullExpr(pc=298)),
	70: ReturnValue(pc=299,UVar(defSites={69},value=null[↦298]))
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=5) -> {BB_2a,BB_2}
	BB_10: BasicBlock(start=29,end=29) -> {BB_7}
	BB_11: BasicBlock(start=21,end=21) -> {BB_2a,BB_17}
	BB_12: BasicBlock(start=28,end=28) -> {BB_1c}
	BB_13: BasicBlock(start=38,end=38) -> {BB_1c}
	BB_14: BasicBlock(start=45,end=45) -> {BB_1c,BB_f}
	BB_15: BasicBlock(start=32,end=33) -> {BB_2a,BB_16}
	BB_16: BasicBlock(start=34,end=36) -> {BB_1c,BB_b}
	BB_17: BasicBlock(start=22,end=22) -> {BB_a,BB_28}
	BB_18: BasicBlock(start=44,end=44) -> {BB_2a,BB_14}
	BB_19: BasicBlock(start=27,end=27) -> {BB_2a,BB_12}
	BB_1: BasicBlock(start=56,end=65) -> {BB_2d,BB_6}
	BB_1a: BasicBlock(start=12,end=13) -> {BB_2a,BB_d}
	BB_1b: BasicBlock(start=54,end=54) -> {BB_2a,BB_27}
	BB_1c: BasicBlock(start=49,end=49) -> {BB_1,BB_21}
	BB_1d: BasicBlock(start=7,end=10) -> {BB_2a,BB_24}
	BB_1e: BasicBlock(start=39,end=40) -> {BB_4,BB_2b}
	BB_1f: BasicBlock(start=18,end=19) -> {BB_e,BB_28}
	BB_20: ExitNode(normalReturn=true)
	BB_21: BasicBlock(start=50,end=51) -> {BB_3,BB_c}
	BB_22: BasicBlock(start=67,end=67) -> {BB_2d}
	BB_23: BasicBlock(start=16,end=17) -> {BB_1f,BB_a}
	BB_24: BasicBlock(start=11,end=11) -> {BB_1a,BB_23}
	BB_25: BasicBlock(start=43,end=43) -> {BB_18,BB_2b}
	BB_26: BasicBlock(start=26,end=26) -> {BB_2a,BB_19}
	BB_27: BasicBlock(start=55,end=55) -> {BB_20}
	BB_28: BasicBlock(start=23,end=23) -> {BB_1c}
	BB_29: BasicBlock(start=4,end=4) -> {BB_2a,BB_0}
	BB_2: BasicBlock(start=6,end=6) -> {BB_1d}
	BB_2a: ExitNode(normalReturn=false)
	BB_2b: BasicBlock(start=47,end=48) -> {BB_7}
	BB_2c: BasicBlock(start=15,end=15) -> {BB_1}
	BB_2d: BasicBlock(start=68,end=68) -> {BB_2a,BB_8}
	BB_3: BasicBlock(start=53,end=53) -> {BB_1b}
	BB_4: BasicBlock(start=41,end=42) -> {BB_25,BB_1c}
	BB_5: BasicBlock(start=2,end=3) -> {BB_1d,BB_29}
	BB_6: BasicBlock(start=66,end=66) -> {BB_2a,BB_22}
	BB_7: BasicBlock(start=30,end=31) -> {BB_15,BB_1e}
	BB_8: BasicBlock(start=69,end=70) -> {BB_20}
	BB_9: BasicBlock(start=0,end=1) -> {BB_5,BB_29}
	BB_a: BasicBlock(start=24,end=25) -> {BB_26,BB_10}
	BB_b: BasicBlock(start=37,end=37) -> {BB_2a,BB_13}
	BB_c: BasicBlock(start=52,end=52) -> {BB_3,BB_1b}
	BB_d: BasicBlock(start=14,end=14) -> {BB_2a,BB_2c}
	BB_e: BasicBlock(start=20,end=20) -> {BB_a,BB_11}
	BB_f: BasicBlock(start=46,end=46) -> {BB_2b}
))

java.util.HashMap$Node[] resize()
AITACode(params=(Parameters(
	0: useSites={0,28,60,41,5,11,39} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={48,4,12,42,1,45},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.HashMap,table,java.util.HashMap$Node[],UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	1: If(pc=6,UVar(defSites={0},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=103]),!=,NullExpr(pc=-333),target=4),
	2: Assignment(pc=9,DVar(useSites={68,44,60,18,86,14,9,7},value=int = 0,origin=2),IntConst(pc=9,0)),
	3: Goto(pc=10,target=5),
	4: Assignment(pc=14,DVar(useSites={68,44,60,18,86,14,9,7},value=int ∈ [0,2147483647],origin=4),ArrayLength(pc=14,UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=103]))),
	5: Assignment(pc=17,DVar(useSites={40,20,22,53,27,31},value=an int,origin=5),GetField(pc=17,java.util.HashMap,threshold,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	6: Assignment(pc=21,DVar(useSites={26,39},value=int = 0,origin=6),IntConst(pc=21,0)),
	7: If(pc=25,UVar(defSites={4,2},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=22),
	8: Assignment(pc=29,DVar(useSites={9},value=int = 1073741824,origin=8),IntConst(pc=29,1073741824)),
	9: If(pc=31,UVar(defSites={4,2},value=int ∈ [1,2147483647]),<,UVar(defSites={8},value=int = 1073741824),target=13),
	10: Assignment(pc=35,DVar(useSites={11},value=int = 2147483647,origin=10),IntConst(pc=35,2147483647)),
	11: PutField(pc=37,java.util.HashMap,threshold,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={10},value=int = 2147483647)),
	12: ReturnValue(pc=41,UVar(defSites={0},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=103])),
	13: Assignment(pc=43,DVar(useSites={14},value=int = 1,origin=13),IntConst(pc=43,1)),
	14: Assignment(pc=44,DVar(useSites={16,40,53,27,31},value=int ∈ [2,2147483646],origin=14),BinaryExpr(pc=44,ComputationalTypeInt,UVar(defSites={4,2},value=int ∈ [1,1073741823]),<<,UVar(defSites={13},value=int = 1))),
	15: Assignment(pc=48,DVar(useSites={16},value=int = 1073741824,origin=15),IntConst(pc=48,1073741824)),
	16: If(pc=50,UVar(defSites={14},value=int ∈ [2,2147483646]),>=,UVar(defSites={15},value=int = 1073741824),target=26),
	17: Assignment(pc=54,DVar(useSites={18},value=int = 16,origin=17),IntConst(pc=54,16)),
	18: If(pc=56,UVar(defSites={4,2},value=int ∈ [1,1073741823]),<,UVar(defSites={17},value=int = 16),target=26),
	19: Assignment(pc=60,DVar(useSites={20},value=int = 1,origin=19),IntConst(pc=60,1)),
	20: Assignment(pc=61,DVar(useSites={26,39},value=an int,origin=20),BinaryExpr(pc=61,ComputationalTypeInt,UVar(defSites={5},value=an int),<<,UVar(defSites={19},value=int = 1))),
	21: Goto(pc=64,target=26),
	22: If(pc=68,UVar(defSites={5},value=an int),<=,IntConst(pc=-333,0),target=24),
	23: Goto(pc=74,target=26),
	24: Assignment(pc=77,DVar(useSites={40,53,27,31},value=int = 16,origin=24),IntConst(pc=77,16)),
	25: Assignment(pc=81,DVar(useSites={26,39},value=int = 12,origin=25),IntConst(pc=81,12)),
	26: If(pc=87,UVar(defSites={20,6,25},value=an int),!=,IntConst(pc=-333,0),target=39),
	27: Assignment(pc=92,DVar(useSites={29},value=AFloatValue,origin=27),PrimitiveTypecastExpr(pc=92,FloatType,UVar(defSites={24,14,5},value=int ∈ [0,2147483647]))),
	28: Assignment(pc=94,DVar(useSites={29},value=AFloatValue,origin=28),GetField(pc=94,java.util.HashMap,loadFactor,float,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]))),
	29: Assignment(pc=97,DVar(useSites={33,35},value=AFloatValue,origin=29),BinaryExpr(pc=97,ComputationalTypeFloat,UVar(defSites={27},value=AFloatValue),*,UVar(defSites={28},value=AFloatValue))),
	30: Assignment(pc=102,DVar(useSites={31},value=int = 1073741824,origin=30),IntConst(pc=102,1073741824)),
	31: If(pc=104,UVar(defSites={24,14,5},value=int ∈ [0,2147483647]),>=,UVar(defSites={30},value=int = 1073741824),target=37),
	32: Assignment(pc=109,DVar(useSites={33},value=AFloatValue,origin=32),FloatConst(pc=109,1.07374182E9)),
	33: Assignment(pc=111,DVar(useSites={34},value=an int,origin=33),Compare(pc=111,UVar(defSites={29},value=AFloatValue),cmpg,UVar(defSites={32},value=AFloatValue))),
	34: If(pc=112,UVar(defSites={33},value=an int),>=,IntConst(pc=-333,0),target=37),
	35: Assignment(pc=117,DVar(useSites={39},value=an int,origin=35),PrimitiveTypecastExpr(pc=117,IntegerType,UVar(defSites={29},value=AFloatValue))),
	36: Goto(pc=118,target=38),
	37: Assignment(pc=121,DVar(useSites={39},value=an int,origin=37),IntConst(pc=121,2147483647)),
	38: Nop(pc=123),
	39: PutField(pc=128,java.util.HashMap,threshold,int,UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={20,6,25,37,35},value=an int)),
	40: Assignment(pc=133,DVar(useSites={60,82,90,41,87,55},value=java.util.HashMap$Node[][↦133;refId=104],origin=40),NewArray(pc=133,[UVar(defSites={24,14,5},value=int ∈ [0,2147483647])],java.util.HashMap$Node[])),
	41: PutField(pc=141,java.util.HashMap,table,java.util.HashMap$Node[],UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={40},value=java.util.HashMap$Node[][↦133;refId=104])),
	42: If(pc=145,UVar(defSites={0},value={_ <: java.util.HashMap$Node[], null}[↦1;refId=103]),==,NullExpr(pc=-333),target=90),
	43: Assignment(pc=148,DVar(useSites={48,88,44,60,82,86,45},value=int = 0,origin=43),IntConst(pc=148,0)),
	44: If(pc=154,UVar(defSites={88,43},value=an int),>=,UVar(defSites={4,2},value=int ∈ [0,2147483647]),target=90),
	45: Assignment(pc=160,DVar(useSites={72,76,60,66,82,74,70,46,81,49,57,85,67,83,51,59,87,55,79},value={_ <: java.util.HashMap$Node, null}[↦160;refId=1042],origin=45),ArrayLoad(pc=160,UVar(defSites={88,43},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=103]))),
	46: If(pc=164,UVar(defSites={45},value={_ <: java.util.HashMap$Node, null}[↦160;refId=1042]),==,NullExpr(pc=-333),target=88),
	47: Assignment(pc=170,DVar(useSites={48},value=null[↦170],origin=47),NullExpr(pc=170)),
	48: ArrayStore(pc=171,UVar(defSites={0},value=_ <: java.util.HashMap$Node[][↦1;refId=103]),UVar(defSites={88,43},value=int ∈ [-2147483648,2147483646]),UVar(defSites={47},value=null[↦170])),
	49: Assignment(pc=174,DVar(useSites={50},value={_ <: java.util.HashMap$Node, null}[↦174;refId=1044],origin=49),GetField(pc=174,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={45},value=_ <: java.util.HashMap$Node[↦160;refId=1042]))),
	50: If(pc=177,UVar(defSites={49},value={_ <: java.util.HashMap$Node, null}[↦174;refId=1044]),!=,NullExpr(pc=-333),target=57),
	51: Assignment(pc=184,DVar(useSites={54},value=an int,origin=51),GetField(pc=184,java.util.HashMap$Node,hash,int,UVar(defSites={45},value=_ <: java.util.HashMap$Node[↦160;refId=1042]))),
	52: Assignment(pc=189,DVar(useSites={53},value=int = 1,origin=52),IntConst(pc=189,1)),
	53: Assignment(pc=190,DVar(useSites={54},value=int ∈ [-1,2147483646],origin=53),BinaryExpr(pc=190,ComputationalTypeInt,UVar(defSites={24,14,5},value=int ∈ [0,2147483647]),-,UVar(defSites={52},value=int = 1))),
	54: Assignment(pc=191,DVar(useSites={55},value=an int,origin=54),BinaryExpr(pc=191,ComputationalTypeInt,UVar(defSites={51},value=an int),&,UVar(defSites={53},value=int ∈ [-1,2147483646]))),
	55: ArrayStore(pc=194,UVar(defSites={40},value=java.util.HashMap$Node[][↦133;refId=104]),UVar(defSites={54},value=an int),UVar(defSites={45},value=_ <: java.util.HashMap$Node[↦160;refId=1042])),
	56: Goto(pc=195,target=88),
	57: Assignment(pc=200,DVar(useSites={58},value=int ∈ [0,1],origin=57),InstanceOf(pc=200,UVar(defSites={45},value=_ <: java.util.HashMap$Node[↦160;refId=1042]),java.util.HashMap$TreeNode)),
	58: If(pc=203,UVar(defSites={57},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=62),
	59: Checkcast(pc=208,UVar(defSites={45},value=_ <: java.util.HashMap$Node[↦160;refId=1042]),java.util.HashMap$TreeNode),
	60: VirtualMethodCall(pc=217,java.util.HashMap$TreeNode,isInterface=false,void split(java.util.HashMap,java.util.HashMap$Node[],int,int),UVar(defSites={45},value=java.util.HashMap$TreeNode[↦160;refId=1046]),(UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),UVar(defSites={40},value=java.util.HashMap$Node[][↦133;refId=104]),UVar(defSites={88,43},value=int ∈ [-2147483648,2147483646]),UVar(defSites={4,2},value=int ∈ [0,2147483647]))),
	61: Goto(pc=220,target=88),
	62: Assignment(pc=223,DVar(useSites={82},value=null[↦223],origin=62),NullExpr(pc=223)),
	63: Assignment(pc=226,DVar(useSites={72,70,81,79},value=null[↦226],origin=63),NullExpr(pc=226)),
	64: Assignment(pc=229,DVar(useSites={87},value=null[↦229],origin=64),NullExpr(pc=229)),
	65: Assignment(pc=232,DVar(useSites={76,74,85,83},value=null[↦232],origin=65),NullExpr(pc=232)),
	66: Assignment(pc=237,DVar(useSites={72,76,82,74,70,78,81,85,67,83,87,79},value={_ <: java.util.HashMap$Node, null}[↦237;refId=1060],origin=66),GetField(pc=237,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={66,45},value=_ <: java.util.HashMap$Node[refId=1049; values=«_ <: java.util.HashMap$Node[↦237;refId=962], _ <: java.util.HashMap$Node[↦160;refId=1042]»]))),
	67: Assignment(pc=244,DVar(useSites={68},value=an int,origin=67),GetField(pc=244,java.util.HashMap$Node,hash,int,UVar(defSites={66,45},value=_ <: java.util.HashMap$Node[refId=1049; values=«_ <: java.util.HashMap$Node[↦237;refId=962], _ <: java.util.HashMap$Node[↦160;refId=1042]»]))),
	68: Assignment(pc=248,DVar(useSites={69},value=int ∈ [0,2147483647],origin=68),BinaryExpr(pc=248,ComputationalTypeInt,UVar(defSites={67},value=an int),&,UVar(defSites={4,2},value=int ∈ [0,2147483647]))),
	69: If(pc=249,UVar(defSites={68},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=74),
	70: If(pc=254,UVar(defSites={66,45,63},value={_ <: java.util.HashMap$Node, null}[refId=180; values=«_ <: java.util.HashMap$Node[↦160;refId=106], null[↦226], _ <: java.util.HashMap$Node[↦237;refId=113]»]),!=,NullExpr(pc=-333),target=72),
	71: Goto(pc=261,target=73),
	72: PutField(pc=268,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={66,45,63},value=_ <: java.util.HashMap$Node[refId=1061; values=«_ <: java.util.HashMap$Node[↦160;refId=106], _ <: java.util.HashMap$Node[↦237;refId=113]»]),UVar(defSites={66,45},value=_ <: java.util.HashMap$Node[refId=1049; values=«_ <: java.util.HashMap$Node[↦237;refId=962], _ <: java.util.HashMap$Node[↦160;refId=1042]»])),
	73: Goto(pc=275,target=78),
	74: If(pc=280,UVar(defSites={66,65,45},value={_ <: java.util.HashMap$Node, null}[refId=1033; values=«null[↦232], _ <: java.util.HashMap$Node[↦160;refId=944], _ <: java.util.HashMap$Node[↦237;refId=864]»]),!=,NullExpr(pc=-333),target=76),
	75: Goto(pc=287,target=77),
	76: PutField(pc=294,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={66,65,45},value=_ <: java.util.HashMap$Node[refId=1070; values=«_ <: java.util.HashMap$Node[↦160;refId=944], _ <: java.util.HashMap$Node[↦237;refId=864]»]),UVar(defSites={66,45},value=_ <: java.util.HashMap$Node[refId=1049; values=«_ <: java.util.HashMap$Node[↦237;refId=962], _ <: java.util.HashMap$Node[↦160;refId=1042]»])),
	77: Nop(pc=297),
	78: If(pc=306,UVar(defSites={66},value={_ <: java.util.HashMap$Node, null}[↦237;refId=1060]),!=,NullExpr(pc=-333),target=66),
	79: If(pc=311,UVar(defSites={66,45,63},value={_ <: java.util.HashMap$Node, null}[refId=1095; values=«null[↦226], _ <: java.util.HashMap$Node[↦160;refId=106], _ <: java.util.HashMap$Node[↦237;refId=113]»]),==,NullExpr(pc=-333),target=83),
	80: Assignment(pc=316,DVar(useSites={81},value=null[↦316],origin=80),NullExpr(pc=316)),
	81: PutField(pc=317,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={66,45,63},value=_ <: java.util.HashMap$Node[refId=1105; values=«_ <: java.util.HashMap$Node[↦160;refId=106], _ <: java.util.HashMap$Node[↦237;refId=113]»]),UVar(defSites={80},value=null[↦316])),
	82: ArrayStore(pc=326,UVar(defSites={40},value=java.util.HashMap$Node[][↦133;refId=104]),UVar(defSites={88,43},value=an int),UVar(defSites={66,62,45},value={_ <: java.util.HashMap$Node, null}[refId=160; values=«null[↦223], _ <: java.util.HashMap$Node[↦160;refId=106], _ <: java.util.HashMap$Node[↦237;refId=113]»])),
	83: If(pc=329,UVar(defSites={66,65,45},value={_ <: java.util.HashMap$Node, null}[refId=1106; values=«null[↦232], _ <: java.util.HashMap$Node[↦160;refId=1042], _ <: java.util.HashMap$Node[↦237;refId=962]»]),==,NullExpr(pc=-333),target=88),
	84: Assignment(pc=334,DVar(useSites={85},value=null[↦334],origin=84),NullExpr(pc=334)),
	85: PutField(pc=335,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={66,65,45},value=_ <: java.util.HashMap$Node[refId=1111; values=«_ <: java.util.HashMap$Node[↦160;refId=1042], _ <: java.util.HashMap$Node[↦237;refId=962]»]),UVar(defSites={84},value=null[↦334])),
	86: Assignment(pc=343,DVar(useSites={87},value=an int,origin=86),BinaryExpr(pc=343,ComputationalTypeInt,UVar(defSites={88,43},value=an int),+,UVar(defSites={4,2},value=int ∈ [0,2147483647]))),
	87: ArrayStore(pc=346,UVar(defSites={40},value=java.util.HashMap$Node[][↦133;refId=104]),UVar(defSites={86},value=an int),UVar(defSites={64,66,45},value={_ <: java.util.HashMap$Node, null}[refId=185; values=«null[↦229], _ <: java.util.HashMap$Node[↦160;refId=106], _ <: java.util.HashMap$Node[↦237;refId=113]»])),
	88: Assignment(pc=347,DVar(useSites={48,44,60,82,86,89,45},value=an int,origin=88),BinaryExpr(pc=347,ComputationalTypeInt,UVar(defSites={88,43},value=an int),+,IntConst(pc=347,1))),
	89: Goto(pc=350,target=44),
	90: ReturnValue(pc=355,UVar(defSites={40},value=java.util.HashMap$Node[][↦133;refId=104]))
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=7) -> {BB_27,BB_19}
	BB_10: BasicBlock(start=61,end=61) -> {BB_8}
	BB_11: BasicBlock(start=74,end=74) -> {BB_1f,BB_28}
	BB_12: BasicBlock(start=38,end=38) -> {BB_20}
	BB_13: BasicBlock(start=70,end=70) -> {BB_23,BB_1d}
	BB_14: BasicBlock(start=73,end=73) -> {BB_f}
	BB_15: BasicBlock(start=2,end=3) -> {BB_0}
	BB_16: BasicBlock(start=32,end=34) -> {BB_c,BB_22}
	BB_17: BasicBlock(start=45,end=45) -> {BB_2d,BB_d}
	BB_18: BasicBlock(start=17,end=18) -> {BB_25,BB_2a}
	BB_19: BasicBlock(start=22,end=22) -> {BB_b,BB_26}
	BB_1: BasicBlock(start=84,end=87) -> {BB_2d,BB_8}
	BB_1a: BasicBlock(start=44,end=44) -> {BB_30,BB_17}
	BB_1b: BasicBlock(start=59,end=59) -> {BB_2d,BB_2}
	BB_1c: BasicBlock(start=27,end=31) -> {BB_c,BB_16}
	BB_1d: BasicBlock(start=71,end=71) -> {BB_14}
	BB_1e: BasicBlock(start=49,end=50) -> {BB_29,BB_e}
	BB_1f: BasicBlock(start=76,end=76) -> {BB_3}
	BB_20: BasicBlock(start=39,end=42) -> {BB_24,BB_30}
	BB_21: BasicBlock(start=80,end=82) -> {BB_2d,BB_31}
	BB_22: BasicBlock(start=35,end=36) -> {BB_12}
	BB_23: BasicBlock(start=72,end=72) -> {BB_14}
	BB_24: BasicBlock(start=43,end=43) -> {BB_1a}
	BB_25: BasicBlock(start=26,end=26) -> {BB_1c,BB_20}
	BB_26: BasicBlock(start=23,end=23) -> {BB_25}
	BB_27: BasicBlock(start=8,end=9) -> {BB_9,BB_4}
	BB_28: BasicBlock(start=75,end=75) -> {BB_3}
	BB_29: BasicBlock(start=51,end=55) -> {BB_2d,BB_a}
	BB_2: BasicBlock(start=60,end=60) -> {BB_2d,BB_10}
	BB_2a: BasicBlock(start=19,end=21) -> {BB_25}
	BB_2b: BasicBlock(start=4,end=4) -> {BB_0}
	BB_2c: BasicBlock(start=79,end=79) -> {BB_21,BB_31}
	BB_2d: ExitNode(normalReturn=false)
	BB_2e: BasicBlock(start=47,end=48) -> {BB_2d,BB_1e}
	BB_2f: BasicBlock(start=62,end=65) -> {BB_5}
	BB_30: BasicBlock(start=90,end=90) -> {BB_6}
	BB_31: BasicBlock(start=83,end=83) -> {BB_1,BB_8}
	BB_3: BasicBlock(start=77,end=77) -> {BB_f}
	BB_4: BasicBlock(start=13,end=16) -> {BB_25,BB_18}
	BB_5: BasicBlock(start=66,end=69) -> {BB_13,BB_11}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=0,end=1) -> {BB_15,BB_2b}
	BB_8: BasicBlock(start=88,end=89) -> {BB_1a}
	BB_9: BasicBlock(start=10,end=12) -> {BB_6}
	BB_a: BasicBlock(start=56,end=56) -> {BB_8}
	BB_b: BasicBlock(start=24,end=25) -> {BB_25}
	BB_c: BasicBlock(start=37,end=37) -> {BB_12}
	BB_d: BasicBlock(start=46,end=46) -> {BB_8,BB_2e}
	BB_e: BasicBlock(start=57,end=58) -> {BB_1b,BB_2f}
	BB_f: BasicBlock(start=78,end=78) -> {BB_2c,BB_5}
))

java.lang.Object remove(java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={4} (origin=-1),
	1: useSites={0,4} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={4},value=an int,origin=0),StaticFunctionCall(pc=2,java.util.HashMap,isInterface=false,int hash(java.lang.Object),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	1: Assignment(pc=6,DVar(useSites={4},value=null[↦6],origin=1),NullExpr(pc=6)),
	2: Assignment(pc=7,DVar(useSites={4},value=int = 0,origin=2),IntConst(pc=7,0)),
	3: Assignment(pc=8,DVar(useSites={4},value=int = 1,origin=3),IntConst(pc=8,1)),
	4: Assignment(pc=9,DVar(useSites={8,5},value={_ <: java.util.HashMap$Node, null}[↦9;refId=106],origin=4),VirtualFunctionCall(pc=9,java.util.HashMap,isInterface=false,java.util.HashMap$Node removeNode(int,java.lang.Object,java.lang.Object,boolean,boolean),UVar(defSites={-1},value=_ <: java.util.HashMap[↦-1;refId=102]),(UVar(defSites={0},value=an int),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),UVar(defSites={1},value=null[↦6]),UVar(defSites={2},value=int = 0),UVar(defSites={3},value=int = 1)))),
	5: If(pc=14,UVar(defSites={4},value={_ <: java.util.HashMap$Node, null}[↦9;refId=106]),!=,NullExpr(pc=-333),target=8),
	6: Assignment(pc=17,DVar(useSites={9},value=null[↦17],origin=6),NullExpr(pc=17)),
	7: Goto(pc=18,target=9),
	8: Assignment(pc=22,DVar(useSites={9},value={_ <: java.lang.Object, null}[refId=108; values=«null[↦17], {_ <: java.lang.Object, null}[↦22;refId=107]»],origin=8),GetField(pc=22,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={4},value=_ <: java.util.HashMap$Node[↦9;refId=106]))),
	9: ReturnValue(pc=25,UVar(defSites={8,6},value={_ <: java.lang.Object, null}[refId=108; values=«null[↦17], {_ <: java.lang.Object, null}[↦22;refId=107]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_7,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3,BB_6}
	BB_2: BasicBlock(start=1,end=4) -> {BB_7,BB_1}
	BB_3: BasicBlock(start=6,end=7) -> {BB_4}
	BB_4: BasicBlock(start=9,end=9) -> {BB_5}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=8,end=8) -> {BB_4}
	BB_7: ExitNode(normalReturn=false)
))

