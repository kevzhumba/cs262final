void afterNodeAccess(java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={0,2,18,10,26,22,23} (origin=-1),
	1: useSites={8,4,20,18,6,22,5,21,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),GetField(pc=1,java.util.LinkedHashMap,accessOrder,boolean,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=27),
	2: Assignment(pc=8,DVar(useSites={20,17,21,3},value={_ <: java.util.LinkedHashMap$Entry, null}[↦8;refId=104],origin=2),GetField(pc=8,java.util.LinkedHashMap,tail,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	3: If(pc=14,UVar(defSites={2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦8;refId=104]),==,UVar(defSites={-2},value={_ <: java.util.HashMap$Node, null}[↦-2;refId=103]),target=27),
	4: Checkcast(pc=18,UVar(defSites={-2},value={_ <: java.util.HashMap$Node, null}[↦-2;refId=103]),java.util.LinkedHashMap$Entry),
	5: Assignment(pc=23,DVar(useSites={20,12,14,17,9,21},value={_ <: java.util.LinkedHashMap$Entry, null}[↦23;refId=107],origin=5),GetField(pc=23,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=105]))),
	6: Assignment(pc=29,DVar(useSites={12,10,14,13},value={_ <: java.util.LinkedHashMap$Entry, null}[↦29;refId=109],origin=6),GetField(pc=29,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]))),
	7: Assignment(pc=35,DVar(useSites={8},value=null[↦35],origin=7),NullExpr(pc=35)),
	8: PutField(pc=36,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]),UVar(defSites={7},value=null[↦35])),
	9: If(pc=41,UVar(defSites={5},value={_ <: java.util.LinkedHashMap$Entry, null}[↦23;refId=107]),!=,NullExpr(pc=-333),target=12),
	10: PutField(pc=47,java.util.LinkedHashMap,head,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={6},value={_ <: java.util.LinkedHashMap$Entry, null}[↦29;refId=109])),
	11: Goto(pc=50,target=13),
	12: PutField(pc=57,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={5},value=_ <: java.util.LinkedHashMap$Entry[↦23;refId=107]),UVar(defSites={6},value={_ <: java.util.LinkedHashMap$Entry, null}[↦29;refId=109])),
	13: If(pc=62,UVar(defSites={6},value={_ <: java.util.LinkedHashMap$Entry, null}[↦29;refId=109]),==,NullExpr(pc=-333),target=16),
	14: PutField(pc=69,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={6},value=_ <: java.util.LinkedHashMap$Entry[↦29;refId=109]),UVar(defSites={5},value={_ <: java.util.LinkedHashMap$Entry, null}[↦23;refId=107])),
	15: Goto(pc=72,target=17),
	16: Nop(pc=75),
	17: If(pc=79,UVar(defSites={2,5},value={_ <: java.util.LinkedHashMap$Entry, null}[refId=110; values=«{_ <: java.util.LinkedHashMap$Entry, null}[↦8;refId=104], {_ <: java.util.LinkedHashMap$Entry, null}[↦23;refId=107]»]),!=,NullExpr(pc=-333),target=20),
	18: PutField(pc=84,java.util.LinkedHashMap,head,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105])),
	19: Goto(pc=87,target=22),
	20: PutField(pc=92,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]),UVar(defSites={2,5},value=_ <: java.util.LinkedHashMap$Entry[refId=110; values=«{_ <: java.util.LinkedHashMap$Entry, null}[↦8;refId=104], {_ <: java.util.LinkedHashMap$Entry, null}[↦23;refId=107]»])),
	21: PutField(pc=97,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={2,5},value=_ <: java.util.LinkedHashMap$Entry[refId=110; values=«{_ <: java.util.LinkedHashMap$Entry, null}[↦8;refId=104], {_ <: java.util.LinkedHashMap$Entry, null}[↦23;refId=107]»]),UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105])),
	22: PutField(pc=102,java.util.LinkedHashMap,tail,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105])),
	23: Assignment(pc=107,DVar(useSites={25},value=an int,origin=23),GetField(pc=107,java.util.LinkedHashMap,modCount,int,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	24: Assignment(pc=110,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=110,1)),
	25: Assignment(pc=111,DVar(useSites={26},value=an int,origin=25),BinaryExpr(pc=111,ComputationalTypeInt,UVar(defSites={23},value=an int),+,UVar(defSites={24},value=int = 1))),
	26: PutField(pc=112,java.util.LinkedHashMap,modCount,int,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={25},value=an int)),
	27: Return(pc=115)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_c,BB_7}
	BB_10: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_10,BB_5}
	BB_2: BasicBlock(start=10,end=11) -> {BB_6}
	BB_3: BasicBlock(start=14,end=15) -> {BB_8}
	BB_4: BasicBlock(start=20,end=21) -> {BB_b}
	BB_5: BasicBlock(start=6,end=9) -> {BB_2,BB_9}
	BB_6: BasicBlock(start=13,end=13) -> {BB_3,BB_a}
	BB_7: BasicBlock(start=2,end=3) -> {BB_f,BB_c}
	BB_8: BasicBlock(start=17,end=17) -> {BB_d,BB_4}
	BB_9: BasicBlock(start=12,end=12) -> {BB_6}
	BB_a: BasicBlock(start=16,end=16) -> {BB_8}
	BB_b: BasicBlock(start=22,end=26) -> {BB_c}
	BB_c: BasicBlock(start=27,end=27) -> {BB_e}
	BB_d: BasicBlock(start=18,end=19) -> {BB_b}
	BB_e: ExitNode(normalReturn=true)
	BB_f: BasicBlock(start=4,end=4) -> {BB_10,BB_1}
))

java.util.HashMap$TreeNode newTreeNode(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={1} (origin=-4),
	4: useSites={1} (origin=-5)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2,1,3},value=java.util.HashMap$TreeNode[↦0;refId=106],origin=0),New(pc=0,java.util.HashMap$TreeNode)),
	1: NonVirtualMethodCall(pc=9,java.util.HashMap$TreeNode,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={0},value=java.util.HashMap$TreeNode[↦0;refId=106]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={-5},value={_ <: java.util.HashMap$Node, null}[↦-5;refId=105]))),
	2: VirtualMethodCall(pc=17,java.util.LinkedHashMap,isInterface=false,void linkNodeLast(java.util.LinkedHashMap$Entry),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={0},value=java.util.HashMap$TreeNode[↦0;refId=106]))),
	3: ReturnValue(pc=22,UVar(defSites={0},value=java.util.HashMap$TreeNode[↦0;refId=106]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

void linkNodeLast(java.util.LinkedHashMap$Entry)
AITACode(params=(Parameters(
	0: useSites={0,1,3} (origin=-1),
	1: useSites={6,1,5,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,6,5},value={_ <: java.util.LinkedHashMap$Entry, null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.LinkedHashMap,tail,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	1: PutField(pc=7,java.util.LinkedHashMap,tail,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=103])),
	2: If(pc=11,UVar(defSites={0},value={_ <: java.util.LinkedHashMap$Entry, null}[↦1;refId=104]),!=,NullExpr(pc=-333),target=5),
	3: PutField(pc=16,java.util.LinkedHashMap,head,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=103])),
	4: Goto(pc=19,target=7),
	5: PutField(pc=24,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=103]),UVar(defSites={0},value=_ <: java.util.LinkedHashMap$Entry[↦1;refId=104])),
	6: PutField(pc=29,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={0},value=_ <: java.util.LinkedHashMap$Entry[↦1;refId=104]),UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=103])),
	7: Return(pc=32)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_1,BB_4}
	BB_1: BasicBlock(start=5,end=5) -> {BB_6,BB_2}
	BB_2: BasicBlock(start=6,end=6) -> {BB_3}
	BB_3: BasicBlock(start=7,end=7) -> {BB_5}
	BB_4: BasicBlock(start=3,end=4) -> {BB_3}
	BB_5: ExitNode(normalReturn=true)
	BB_6: ExitNode(normalReturn=false)
))

java.lang.Object get(java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={1,5,7} (origin=-1),
	1: useSites={0,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),StaticFunctionCall(pc=2,java.util.LinkedHashMap,isInterface=false,int hash(java.lang.Object),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	1: Assignment(pc=6,DVar(useSites={8,2,7},value={_ <: java.util.HashMap$Node, null}[↦6;refId=106],origin=1),VirtualFunctionCall(pc=6,java.util.LinkedHashMap,isInterface=false,java.util.HashMap$Node getNode(int,java.lang.Object),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={0},value=an int),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	2: If(pc=11,UVar(defSites={1},value={_ <: java.util.HashMap$Node, null}[↦6;refId=106]),!=,NullExpr(pc=-333),target=5),
	3: Assignment(pc=14,DVar(useSites={4},value=null[↦14],origin=3),NullExpr(pc=14)),
	4: ReturnValue(pc=15,UVar(defSites={3},value=null[↦14])),
	5: Assignment(pc=17,DVar(useSites={6},value=int ∈ [0,1],origin=5),GetField(pc=17,java.util.LinkedHashMap,accessOrder,boolean,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	6: If(pc=20,UVar(defSites={5},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=8),
	7: VirtualMethodCall(pc=25,java.util.LinkedHashMap,isInterface=false,void afterNodeAccess(java.util.HashMap$Node),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={1},value=_ <: java.util.HashMap$Node[↦6;refId=106]))),
	8: Assignment(pc=29,DVar(useSites={9},value={_ <: java.lang.Object, null}[↦29;refId=108],origin=8),GetField(pc=29,java.util.HashMap$Node,value,java.lang.Object,UVar(defSites={1},value=_ <: java.util.HashMap$Node[↦6;refId=106]))),
	9: ReturnValue(pc=32,UVar(defSites={8},value={_ <: java.lang.Object, null}[↦29;refId=108]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_8,BB_2}
	BB_1: BasicBlock(start=5,end=6) -> {BB_7,BB_4}
	BB_2: BasicBlock(start=1,end=1) -> {BB_8,BB_3}
	BB_3: BasicBlock(start=2,end=2) -> {BB_1,BB_5}
	BB_4: BasicBlock(start=7,end=7) -> {BB_8,BB_7}
	BB_5: BasicBlock(start=3,end=4) -> {BB_6}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=8,end=9) -> {BB_6}
	BB_8: ExitNode(normalReturn=false)
))

void afterNodeInsertion(boolean)
AITACode(params=(Parameters(
	0: useSites={10,1,3} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	1: Assignment(pc=5,DVar(useSites={2,5,3},value={_ <: java.util.LinkedHashMap$Entry, null}[↦5;refId=103],origin=1),GetField(pc=5,java.util.LinkedHashMap,head,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	2: If(pc=10,UVar(defSites={1},value={_ <: java.util.LinkedHashMap$Entry, null}[↦5;refId=103]),==,NullExpr(pc=-333),target=12),
	3: Assignment(pc=15,DVar(useSites={4},value=int ∈ [0,1],origin=3),VirtualFunctionCall(pc=15,java.util.LinkedHashMap,isInterface=false,boolean removeEldestEntry(java.util.Map$Entry),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={1},value=_ <: java.util.LinkedHashMap$Entry[↦5;refId=103])))),
	4: If(pc=18,UVar(defSites={3},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	5: Assignment(pc=22,DVar(useSites={10,6},value={_ <: java.lang.Object, null}[↦22;refId=105],origin=5),GetField(pc=22,java.util.LinkedHashMap$Entry,key,java.lang.Object,UVar(defSites={1},value=_ <: java.util.LinkedHashMap$Entry[↦5;refId=103]))),
	6: Assignment(pc=28,DVar(useSites={10},value=an int,origin=6),StaticFunctionCall(pc=28,java.util.LinkedHashMap,isInterface=false,int hash(java.lang.Object),(UVar(defSites={5},value={_ <: java.lang.Object, null}[↦22;refId=105])))),
	7: Assignment(pc=32,DVar(useSites={10},value=null[↦32],origin=7),NullExpr(pc=32)),
	8: Assignment(pc=33,DVar(useSites={10},value=int = 0,origin=8),IntConst(pc=33,0)),
	9: Assignment(pc=34,DVar(useSites={10},value=int = 1,origin=9),IntConst(pc=34,1)),
	10: ExprStmt(pc=35,VirtualFunctionCall(pc=35,java.util.LinkedHashMap,isInterface=false,java.util.HashMap$Node removeNode(int,java.lang.Object,java.lang.Object,boolean,boolean),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={6},value=an int),UVar(defSites={5},value={_ <: java.lang.Object, null}[↦22;refId=105]),UVar(defSites={7},value=null[↦32]),UVar(defSites={8},value=int = 0),UVar(defSites={9},value=int = 1)))),
	11: Nop(pc=38),
	12: Return(pc=39)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_2,BB_3}
	BB_1: BasicBlock(start=5,end=6) -> {BB_9,BB_4}
	BB_2: BasicBlock(start=1,end=2) -> {BB_5,BB_3}
	BB_3: BasicBlock(start=12,end=12) -> {BB_6}
	BB_4: BasicBlock(start=7,end=10) -> {BB_9,BB_7}
	BB_5: BasicBlock(start=3,end=3) -> {BB_9,BB_8}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=11,end=11) -> {BB_3}
	BB_8: BasicBlock(start=4,end=4) -> {BB_1,BB_3}
	BB_9: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0,2} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.HashMap,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 0,origin=1),IntConst(pc=5,0)),
	2: PutField(pc=6,java.util.LinkedHashMap,accessOrder,boolean,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={1},value=int = 0)),
	3: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.Set keySet()
AITACode(params=(Parameters(
	0: useSites={0,4,3} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1,5},value={_ <: java.util.Set, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.LinkedHashMap,keySet,java.util.Set,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	1: If(pc=6,UVar(defSites={0},value={_ <: java.util.Set, null}[↦1;refId=103]),!=,NullExpr(pc=-333),target=5),
	2: Assignment(pc=9,DVar(useSites={4,5,3},value=java.util.LinkedHashMap$LinkedKeySet[↦9;refId=104],origin=2),New(pc=9,java.util.LinkedHashMap$LinkedKeySet)),
	3: NonVirtualMethodCall(pc=14,java.util.LinkedHashMap$LinkedKeySet,isInterface=false,void <init>(java.util.LinkedHashMap),UVar(defSites={2},value=java.util.LinkedHashMap$LinkedKeySet[↦9;refId=104]),(UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]))),
	4: PutField(pc=20,java.util.LinkedHashMap,keySet,java.util.Set,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={2},value=java.util.LinkedHashMap$LinkedKeySet[↦9;refId=104])),
	5: ReturnValue(pc=24,UVar(defSites={0,2},value=_ <: java.util.Set[refId=106; values=«_ <: java.util.Set[↦1;refId=103], java.util.LinkedHashMap$LinkedKeySet[↦9;refId=104]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_2,BB_1}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_2: BasicBlock(start=2,end=3) -> {BB_5,BB_4}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_1}
	BB_5: ExitNode(normalReturn=false)
))

boolean removeEldestEntry(java.util.Map$Entry)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=0,0)),
	1: ReturnValue(pc=1,UVar(defSites={0},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

java.util.HashMap$Node replacementNode(java.util.HashMap$Node,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={6} (origin=-1),
	1: useSites={0,4,2,6,3} (origin=-2),
	2: useSites={5} (origin=-3)
)),stmts=(
	0: Checkcast(pc=1,UVar(defSites={-2},value={_ <: java.util.HashMap$Node, null}[↦-2;refId=103]),java.util.LinkedHashMap$Entry),
	1: Assignment(pc=5,DVar(useSites={6,5,7},value=java.util.LinkedHashMap$Entry[↦5;refId=107],origin=1),New(pc=5,java.util.LinkedHashMap$Entry)),
	2: Assignment(pc=10,DVar(useSites={5},value=an int,origin=2),GetField(pc=10,java.util.LinkedHashMap$Entry,hash,int,UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=105]))),
	3: Assignment(pc=14,DVar(useSites={5},value={_ <: java.lang.Object, null}[↦14;refId=109],origin=3),GetField(pc=14,java.util.LinkedHashMap$Entry,key,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]))),
	4: Assignment(pc=18,DVar(useSites={5},value={_ <: java.lang.Object, null}[↦18;refId=110],origin=4),GetField(pc=18,java.util.LinkedHashMap$Entry,value,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]))),
	5: NonVirtualMethodCall(pc=22,java.util.LinkedHashMap$Entry,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={1},value=java.util.LinkedHashMap$Entry[↦5;refId=107]),(UVar(defSites={2},value=an int),UVar(defSites={3},value={_ <: java.lang.Object, null}[↦14;refId=109]),UVar(defSites={4},value={_ <: java.lang.Object, null}[↦18;refId=110]),UVar(defSites={-3},value={_ <: java.util.HashMap$Node, null}[↦-3;refId=104]))),
	6: VirtualMethodCall(pc=31,java.util.LinkedHashMap,isInterface=false,void transferLinks(java.util.LinkedHashMap$Entry,java.util.LinkedHashMap$Entry),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]),UVar(defSites={1},value=java.util.LinkedHashMap$Entry[↦5;refId=107]))),
	7: ReturnValue(pc=36,UVar(defSites={1},value=java.util.LinkedHashMap$Entry[↦5;refId=107]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_6,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_6,BB_4}
	BB_2: BasicBlock(start=6,end=6) -> {BB_6,BB_3}
	BB_3: BasicBlock(start=7,end=7) -> {BB_5}
	BB_4: BasicBlock(start=3,end=5) -> {BB_6,BB_2}
	BB_5: ExitNode(normalReturn=true)
	BB_6: ExitNode(normalReturn=false)
))

java.util.HashMap$Node newNode(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={1} (origin=-4),
	4: useSites={1} (origin=-5)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2,1,3},value=java.util.LinkedHashMap$Entry[↦0;refId=106],origin=0),New(pc=0,java.util.LinkedHashMap$Entry)),
	1: NonVirtualMethodCall(pc=9,java.util.LinkedHashMap$Entry,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={0},value=java.util.LinkedHashMap$Entry[↦0;refId=106]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=103]),UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=104]),UVar(defSites={-5},value={_ <: java.util.HashMap$Node, null}[↦-5;refId=105]))),
	2: VirtualMethodCall(pc=17,java.util.LinkedHashMap,isInterface=false,void linkNodeLast(java.util.LinkedHashMap$Entry),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={0},value=java.util.LinkedHashMap$Entry[↦0;refId=106]))),
	3: ReturnValue(pc=22,UVar(defSites={0},value=java.util.LinkedHashMap$Entry[↦0;refId=106]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

void afterNodeRemoval(java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={11,7} (origin=-1),
	1: useSites={0,4,2,1,5} (origin=-2)
)),stmts=(
	0: Checkcast(pc=1,UVar(defSites={-2},value={_ <: java.util.HashMap$Node, null}[↦-2;refId=103]),java.util.LinkedHashMap$Entry),
	1: Assignment(pc=6,DVar(useSites={6,9,13,11},value={_ <: java.util.LinkedHashMap$Entry, null}[↦6;refId=106],origin=1),GetField(pc=6,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=104]))),
	2: Assignment(pc=11,DVar(useSites={10,9,13,7},value={_ <: java.util.LinkedHashMap$Entry, null}[↦11;refId=108],origin=2),GetField(pc=11,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=104]))),
	3: Assignment(pc=18,DVar(useSites={4,5},value=null[↦18],origin=3),NullExpr(pc=18)),
	4: PutField(pc=20,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=104]),UVar(defSites={3},value=null[↦18])),
	5: PutField(pc=23,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=104]),UVar(defSites={3},value=null[↦18])),
	6: If(pc=27,UVar(defSites={1},value={_ <: java.util.LinkedHashMap$Entry, null}[↦6;refId=106]),!=,NullExpr(pc=-333),target=9),
	7: PutField(pc=33,java.util.LinkedHashMap,head,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦11;refId=108])),
	8: Goto(pc=36,target=10),
	9: PutField(pc=42,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={1},value=_ <: java.util.LinkedHashMap$Entry[↦6;refId=106]),UVar(defSites={2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦11;refId=108])),
	10: If(pc=47,UVar(defSites={2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦11;refId=108]),!=,NullExpr(pc=-333),target=13),
	11: PutField(pc=52,java.util.LinkedHashMap,tail,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={1},value={_ <: java.util.LinkedHashMap$Entry, null}[↦6;refId=106])),
	12: Goto(pc=55,target=14),
	13: PutField(pc=61,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={2},value=_ <: java.util.LinkedHashMap$Entry[↦11;refId=108]),UVar(defSites={1},value={_ <: java.util.LinkedHashMap$Entry, null}[↦6;refId=106])),
	14: Return(pc=64)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_a,BB_3}
	BB_1: BasicBlock(start=10,end=10) -> {BB_9,BB_5}
	BB_2: BasicBlock(start=14,end=14) -> {BB_8}
	BB_3: BasicBlock(start=1,end=1) -> {BB_a,BB_6}
	BB_4: BasicBlock(start=9,end=9) -> {BB_1}
	BB_5: BasicBlock(start=13,end=13) -> {BB_2}
	BB_6: BasicBlock(start=2,end=6) -> {BB_7,BB_4}
	BB_7: BasicBlock(start=7,end=8) -> {BB_1}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=11,end=12) -> {BB_2}
	BB_a: ExitNode(normalReturn=false)
))

java.util.HashMap$TreeNode replacementTreeNode(java.util.HashMap$Node,java.util.HashMap$Node)
AITACode(params=(Parameters(
	0: useSites={6} (origin=-1),
	1: useSites={0,4,2,6,3} (origin=-2),
	2: useSites={5} (origin=-3)
)),stmts=(
	0: Checkcast(pc=1,UVar(defSites={-2},value={_ <: java.util.HashMap$Node, null}[↦-2;refId=103]),java.util.LinkedHashMap$Entry),
	1: Assignment(pc=5,DVar(useSites={6,5,7},value=java.util.HashMap$TreeNode[↦5;refId=107],origin=1),New(pc=5,java.util.HashMap$TreeNode)),
	2: Assignment(pc=10,DVar(useSites={5},value=an int,origin=2),GetField(pc=10,java.util.LinkedHashMap$Entry,hash,int,UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=105]))),
	3: Assignment(pc=14,DVar(useSites={5},value={_ <: java.lang.Object, null}[↦14;refId=109],origin=3),GetField(pc=14,java.util.LinkedHashMap$Entry,key,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]))),
	4: Assignment(pc=18,DVar(useSites={5},value={_ <: java.lang.Object, null}[↦18;refId=110],origin=4),GetField(pc=18,java.util.LinkedHashMap$Entry,value,java.lang.Object,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]))),
	5: NonVirtualMethodCall(pc=22,java.util.HashMap$TreeNode,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.HashMap$Node),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=107]),(UVar(defSites={2},value=an int),UVar(defSites={3},value={_ <: java.lang.Object, null}[↦14;refId=109]),UVar(defSites={4},value={_ <: java.lang.Object, null}[↦18;refId=110]),UVar(defSites={-3},value={_ <: java.util.HashMap$Node, null}[↦-3;refId=104]))),
	6: VirtualMethodCall(pc=31,java.util.LinkedHashMap,isInterface=false,void transferLinks(java.util.LinkedHashMap$Entry,java.util.LinkedHashMap$Entry),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=105]),UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=107]))),
	7: ReturnValue(pc=36,UVar(defSites={1},value=java.util.HashMap$TreeNode[↦5;refId=107]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_6,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_6,BB_4}
	BB_2: BasicBlock(start=6,end=6) -> {BB_6,BB_3}
	BB_3: BasicBlock(start=7,end=7) -> {BB_5}
	BB_4: BasicBlock(start=3,end=5) -> {BB_6,BB_2}
	BB_5: ExitNode(normalReturn=true)
	BB_6: ExitNode(normalReturn=false)
))

void transferLinks(java.util.LinkedHashMap$Entry,java.util.LinkedHashMap$Entry)
AITACode(params=(Parameters(
	0: useSites={9,5} (origin=-1),
	1: useSites={0,2} (origin=-2),
	2: useSites={1,9,5,3,11,7} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={4,1,7},value={_ <: java.util.LinkedHashMap$Entry, null}[↦2;refId=105],origin=0),GetField(pc=2,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-2;refId=103]))),
	1: PutField(pc=6,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={-3},value={_ <: java.util.LinkedHashMap$Entry, null}[↦-3;refId=104]),UVar(defSites={0},value={_ <: java.util.LinkedHashMap$Entry, null}[↦2;refId=105])),
	2: Assignment(pc=12,DVar(useSites={8,3,11},value={_ <: java.util.LinkedHashMap$Entry, null}[↦12;refId=108],origin=2),GetField(pc=12,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={-2},value=_ <: java.util.LinkedHashMap$Entry[↦-2;refId=103]))),
	3: PutField(pc=16,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={-3},value=_ <: java.util.LinkedHashMap$Entry[↦-3;refId=104]),UVar(defSites={2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦12;refId=108])),
	4: If(pc=22,UVar(defSites={0},value={_ <: java.util.LinkedHashMap$Entry, null}[↦2;refId=105]),!=,NullExpr(pc=-333),target=7),
	5: PutField(pc=27,java.util.LinkedHashMap,head,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={-3},value=_ <: java.util.LinkedHashMap$Entry[↦-3;refId=104])),
	6: Goto(pc=30,target=8),
	7: PutField(pc=35,java.util.LinkedHashMap$Entry,after,java.util.LinkedHashMap$Entry,UVar(defSites={0},value=_ <: java.util.LinkedHashMap$Entry[↦2;refId=105]),UVar(defSites={-3},value=_ <: java.util.LinkedHashMap$Entry[↦-3;refId=104])),
	8: If(pc=40,UVar(defSites={2},value={_ <: java.util.LinkedHashMap$Entry, null}[↦12;refId=108]),!=,NullExpr(pc=-333),target=11),
	9: PutField(pc=45,java.util.LinkedHashMap,tail,java.util.LinkedHashMap$Entry,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={-3},value=_ <: java.util.LinkedHashMap$Entry[↦-3;refId=104])),
	10: Goto(pc=48,target=12),
	11: PutField(pc=54,java.util.LinkedHashMap$Entry,before,java.util.LinkedHashMap$Entry,UVar(defSites={2},value=_ <: java.util.LinkedHashMap$Entry[↦12;refId=108]),UVar(defSites={-3},value=_ <: java.util.LinkedHashMap$Entry[↦-3;refId=104])),
	12: Return(pc=57)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_a,BB_2}
	BB_1: BasicBlock(start=5,end=6) -> {BB_9}
	BB_2: BasicBlock(start=1,end=1) -> {BB_a,BB_4}
	BB_3: BasicBlock(start=9,end=10) -> {BB_5}
	BB_4: BasicBlock(start=2,end=4) -> {BB_6,BB_1}
	BB_5: BasicBlock(start=12,end=12) -> {BB_7}
	BB_6: BasicBlock(start=7,end=7) -> {BB_9}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=11,end=11) -> {BB_5}
	BB_9: BasicBlock(start=8,end=8) -> {BB_8,BB_3}
	BB_a: ExitNode(normalReturn=false)
))

void <init>(int,float)
AITACode(params=(Parameters(
	0: useSites={0,2} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=3,java.util.HashMap,isInterface=false,void <init>(int,float),UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value=AFloatValue))),
	1: Assignment(pc=7,DVar(useSites={2},value=int = 0,origin=1),IntConst(pc=7,0)),
	2: PutField(pc=8,java.util.LinkedHashMap,accessOrder,boolean,UVar(defSites={-1},value=_ <: java.util.LinkedHashMap[↦-1;refId=102]),UVar(defSites={1},value=int = 0)),
	3: Return(pc=11)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

