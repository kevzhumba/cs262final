java.lang.Object next()
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={_ <: java.lang.Object[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.IdentityHashMap$KeyIterator,traversalTable,java.lang.Object[],UVar(defSites={-1},value=_ <: java.util.IdentityHashMap$KeyIterator[↦-1;refId=102]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),VirtualFunctionCall(pc=5,java.util.IdentityHashMap$KeyIterator,isInterface=false,int nextIndex(),UVar(defSites={-1},value=_ <: java.util.IdentityHashMap$KeyIterator[↦-1;refId=102]),())),
	2: Assignment(pc=8,DVar(useSites={3},value={_ <: java.lang.Object, null}[↦8;refId=107],origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={_ <: java.lang.Object[], null}[↦1;refId=103]))),
	3: Assignment(pc=9,DVar(useSites={4},value={_ <: java.lang.Object, null}[↦9;refId=109],origin=3),StaticFunctionCall(pc=9,java.util.IdentityHashMap,isInterface=false,java.lang.Object unmaskNull(java.lang.Object),(UVar(defSites={2},value={_ <: java.lang.Object, null}[↦8;refId=107])))),
	4: ReturnValue(pc=12,UVar(defSites={3},value={_ <: java.lang.Object, null}[↦9;refId=109]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_5,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_5,BB_2}
	BB_2: BasicBlock(start=3,end=3) -> {BB_5,BB_4}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=4) -> {BB_3}
	BB_5: ExitNode(normalReturn=false)
))

void <init>(java.util.IdentityHashMap)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={0,1} (origin=-2)
)),stmts=(
	0: PutField(pc=2,java.util.IdentityHashMap$KeyIterator,this$0,java.util.IdentityHashMap,UVar(defSites={-1},value=_ <: java.util.IdentityHashMap$KeyIterator[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.IdentityHashMap, null}[↦-2;refId=103])),
	1: NonVirtualMethodCall(pc=7,java.util.IdentityHashMap$IdentityHashMapIterator,isInterface=false,void <init>(java.util.IdentityHashMap),UVar(defSites={-1},value=_ <: java.util.IdentityHashMap$KeyIterator[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.IdentityHashMap, null}[↦-2;refId=103]))),
	2: Return(pc=10)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

