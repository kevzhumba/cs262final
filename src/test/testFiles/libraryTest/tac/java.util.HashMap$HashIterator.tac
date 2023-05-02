java.util.HashMap$Node nextNode()
AITACode(params=(Parameters(
	0: useSites={0,16,12,22,14,1,25,3,19,27} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={8,12,13,29},value={_ <: java.util.HashMap$Node, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.HashMap$HashIterator,next,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={2},value={_ <: java.util.HashMap, null}[↦6;refId=104],origin=1),GetField(pc=6,java.util.HashMap$HashIterator,this$0,java.util.HashMap,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={4},value=an int,origin=2),GetField(pc=9,java.util.HashMap,modCount,int,UVar(defSites={1},value={_ <: java.util.HashMap, null}[↦6;refId=104]))),
	3: Assignment(pc=13,DVar(useSites={4},value=an int,origin=3),GetField(pc=13,java.util.HashMap$HashIterator,expectedModCount,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	4: If(pc=16,UVar(defSites={2},value=an int),==,UVar(defSites={3},value=an int),target=8),
	5: Assignment(pc=19,DVar(useSites={6,7},value=java.util.ConcurrentModificationException[↦19;refId=112],origin=5),New(pc=19,java.util.ConcurrentModificationException)),
	6: NonVirtualMethodCall(pc=23,java.util.ConcurrentModificationException,isInterface=false,void <init>(),UVar(defSites={5},value=java.util.ConcurrentModificationException[↦19;refId=112]),()),
	7: Throw(pc=26,UVar(defSites={5},value=java.util.ConcurrentModificationException[↦19;refId=112])),
	8: If(pc=28,UVar(defSites={0},value={_ <: java.util.HashMap$Node, null}[↦1;refId=103]),!=,NullExpr(pc=-333),target=12),
	9: Assignment(pc=31,DVar(useSites={10,11},value=java.util.NoSuchElementException[↦31;refId=106],origin=9),New(pc=31,java.util.NoSuchElementException)),
	10: NonVirtualMethodCall(pc=35,java.util.NoSuchElementException,isInterface=false,void <init>(),UVar(defSites={9},value=java.util.NoSuchElementException[↦31;refId=106]),()),
	11: Throw(pc=38,UVar(defSites={9},value=java.util.NoSuchElementException[↦31;refId=106])),
	12: PutField(pc=43,java.util.HashMap$HashIterator,current,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={0},value=_ <: java.util.HashMap$Node[↦1;refId=103])),
	13: Assignment(pc=46,DVar(useSites={14,15},value={_ <: java.util.HashMap$Node, null}[↦46;refId=108],origin=13),GetField(pc=46,java.util.HashMap$Node,next,java.util.HashMap$Node,UVar(defSites={0},value=_ <: java.util.HashMap$Node[↦1;refId=103]))),
	14: PutField(pc=50,java.util.HashMap$HashIterator,next,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={13},value={_ <: java.util.HashMap$Node, null}[↦46;refId=108])),
	15: If(pc=53,UVar(defSites={13},value={_ <: java.util.HashMap$Node, null}[↦46;refId=108]),!=,NullExpr(pc=-333),target=29),
	16: Assignment(pc=57,DVar(useSites={17},value={_ <: java.util.HashMap, null}[↦57;refId=109],origin=16),GetField(pc=57,java.util.HashMap$HashIterator,this$0,java.util.HashMap,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	17: Assignment(pc=60,DVar(useSites={20,18,26},value={_ <: java.util.HashMap$Node[], null}[↦60;refId=110],origin=17),GetField(pc=60,java.util.HashMap,table,java.util.HashMap$Node[],UVar(defSites={16},value={_ <: java.util.HashMap, null}[↦57;refId=109]))),
	18: If(pc=65,UVar(defSites={17},value={_ <: java.util.HashMap$Node[], null}[↦60;refId=110]),==,NullExpr(pc=-333),target=29),
	19: Assignment(pc=69,DVar(useSites={21},value=an int,origin=19),GetField(pc=69,java.util.HashMap$HashIterator,index,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	20: Assignment(pc=73,DVar(useSites={21},value=int ∈ [0,2147483647],origin=20),ArrayLength(pc=73,UVar(defSites={17},value=_ <: java.util.HashMap$Node[][↦60;refId=110]))),
	21: If(pc=74,UVar(defSites={19},value=an int),>=,UVar(defSites={20},value=int ∈ [0,2147483647]),target=29),
	22: Assignment(pc=81,DVar(useSites={24,26},value=an int,origin=22),GetField(pc=81,java.util.HashMap$HashIterator,index,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	23: Assignment(pc=85,DVar(useSites={24},value=int = 1,origin=23),IntConst(pc=85,1)),
	24: Assignment(pc=86,DVar(useSites={25},value=an int,origin=24),BinaryExpr(pc=86,ComputationalTypeInt,UVar(defSites={22},value=an int),+,UVar(defSites={23},value=int = 1))),
	25: PutField(pc=87,java.util.HashMap$HashIterator,index,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={24},value=an int)),
	26: Assignment(pc=90,DVar(useSites={28,27},value={_ <: java.util.HashMap$Node, null}[↦90;refId=115],origin=26),ArrayLoad(pc=90,UVar(defSites={22},value=an int),UVar(defSites={17},value=_ <: java.util.HashMap$Node[][↦60;refId=110]))),
	27: PutField(pc=92,java.util.HashMap$HashIterator,next,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={26},value={_ <: java.util.HashMap$Node, null}[↦90;refId=115])),
	28: If(pc=95,UVar(defSites={26},value={_ <: java.util.HashMap$Node, null}[↦90;refId=115]),==,NullExpr(pc=-333),target=19),
	29: ReturnValue(pc=99,UVar(defSites={0},value=_ <: java.util.HashMap$Node[↦1;refId=103]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_b,BB_6}
	BB_1: BasicBlock(start=5,end=6) -> {BB_b,BB_5}
	BB_2: BasicBlock(start=29,end=29) -> {BB_f}
	BB_3: BasicBlock(start=9,end=10) -> {BB_b,BB_8}
	BB_4: BasicBlock(start=12,end=15) -> {BB_7,BB_2}
	BB_5: BasicBlock(start=7,end=7) -> {BB_b}
	BB_6: BasicBlock(start=3,end=4) -> {BB_1,BB_9}
	BB_7: BasicBlock(start=16,end=17) -> {BB_b,BB_e}
	BB_8: BasicBlock(start=11,end=11) -> {BB_b}
	BB_9: BasicBlock(start=8,end=8) -> {BB_4,BB_3}
	BB_a: BasicBlock(start=19,end=21) -> {BB_2,BB_c}
	BB_b: ExitNode(normalReturn=false)
	BB_c: BasicBlock(start=22,end=26) -> {BB_b,BB_d}
	BB_d: BasicBlock(start=27,end=28) -> {BB_a,BB_2}
	BB_e: BasicBlock(start=18,end=18) -> {BB_a,BB_2}
	BB_f: ExitNode(normalReturn=true)
))

void <init>(java.util.HashMap)
AITACode(params=(Parameters(
	0: useSites={0,16,6,1,9,21,13,3,19,7} (origin=-1),
	1: useSites={0,4,2,11} (origin=-2)
)),stmts=(
	0: PutField(pc=2,java.util.HashMap$HashIterator,this$0,java.util.HashMap,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103])),
	1: NonVirtualMethodCall(pc=6,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),()),
	2: Assignment(pc=11,DVar(useSites={3},value=an int,origin=2),GetField(pc=11,java.util.HashMap,modCount,int,UVar(defSites={-2},value={_ <: java.util.HashMap, null}[↦-2;refId=103]))),
	3: PutField(pc=14,java.util.HashMap$HashIterator,expectedModCount,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={2},value=an int)),
	4: Assignment(pc=18,DVar(useSites={20,10,14},value={_ <: java.util.HashMap$Node[], null}[↦18;refId=106],origin=4),GetField(pc=18,java.util.HashMap,table,java.util.HashMap$Node[],UVar(defSites={-2},value=_ <: java.util.HashMap[↦-2;refId=103]))),
	5: Assignment(pc=24,DVar(useSites={6,7},value=null[↦24],origin=5),NullExpr(pc=24)),
	6: PutField(pc=26,java.util.HashMap$HashIterator,next,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={5},value=null[↦24])),
	7: PutField(pc=29,java.util.HashMap$HashIterator,current,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={5},value=null[↦24])),
	8: Assignment(pc=33,DVar(useSites={9},value=int = 0,origin=8),IntConst(pc=33,0)),
	9: PutField(pc=34,java.util.HashMap$HashIterator,index,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={8},value=int = 0)),
	10: If(pc=38,UVar(defSites={4},value={_ <: java.util.HashMap$Node[], null}[↦18;refId=106]),==,NullExpr(pc=-333),target=23),
	11: Assignment(pc=42,DVar(useSites={12},value=an int,origin=11),GetField(pc=42,java.util.HashMap,size,int,UVar(defSites={-2},value=_ <: java.util.HashMap[↦-2;refId=103]))),
	12: If(pc=45,UVar(defSites={11},value=an int),<=,IntConst(pc=-333,0),target=23),
	13: Assignment(pc=49,DVar(useSites={15},value=an int,origin=13),GetField(pc=49,java.util.HashMap$HashIterator,index,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	14: Assignment(pc=53,DVar(useSites={15},value=int ∈ [0,2147483647],origin=14),ArrayLength(pc=53,UVar(defSites={4},value=_ <: java.util.HashMap$Node[][↦18;refId=106]))),
	15: If(pc=54,UVar(defSites={13},value=an int),>=,UVar(defSites={14},value=int ∈ [0,2147483647]),target=23),
	16: Assignment(pc=61,DVar(useSites={20,18},value=an int,origin=16),GetField(pc=61,java.util.HashMap$HashIterator,index,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	17: Assignment(pc=65,DVar(useSites={18},value=int = 1,origin=17),IntConst(pc=65,1)),
	18: Assignment(pc=66,DVar(useSites={19},value=an int,origin=18),BinaryExpr(pc=66,ComputationalTypeInt,UVar(defSites={16},value=an int),+,UVar(defSites={17},value=int = 1))),
	19: PutField(pc=67,java.util.HashMap$HashIterator,index,int,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={18},value=an int)),
	20: Assignment(pc=70,DVar(useSites={22,21},value={_ <: java.util.HashMap$Node, null}[↦70;refId=108],origin=20),ArrayLoad(pc=70,UVar(defSites={16},value=an int),UVar(defSites={4},value=_ <: java.util.HashMap$Node[][↦18;refId=106]))),
	21: PutField(pc=72,java.util.HashMap$HashIterator,next,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]),UVar(defSites={20},value={_ <: java.util.HashMap$Node, null}[↦70;refId=108])),
	22: If(pc=75,UVar(defSites={20},value={_ <: java.util.HashMap$Node, null}[↦70;refId=108]),==,NullExpr(pc=-333),target=13),
	23: Return(pc=78)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_9,BB_3}
	BB_1: BasicBlock(start=21,end=22) -> {BB_2,BB_8}
	BB_2: BasicBlock(start=13,end=15) -> {BB_8,BB_6}
	BB_3: BasicBlock(start=2,end=2) -> {BB_9,BB_4}
	BB_4: BasicBlock(start=3,end=10) -> {BB_8,BB_7}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=16,end=20) -> {BB_9,BB_1}
	BB_7: BasicBlock(start=11,end=12) -> {BB_2,BB_8}
	BB_8: BasicBlock(start=23,end=23) -> {BB_5}
	BB_9: ExitNode(normalReturn=false)
))

boolean hasNext()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.HashMap$Node, null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.HashMap$HashIterator,next,java.util.HashMap$Node,UVar(defSites={-1},value=_ <: java.util.HashMap$HashIterator[↦-1;refId=102]))),
	1: If(pc=4,UVar(defSites={0},value={_ <: java.util.HashMap$Node, null}[↦1;refId=103]),==,NullExpr(pc=-333),target=4),
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

