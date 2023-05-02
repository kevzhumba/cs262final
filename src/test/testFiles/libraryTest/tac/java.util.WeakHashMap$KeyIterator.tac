void <init>(java.util.WeakHashMap)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={0,1} (origin=-2)
)),stmts=(
	0: PutField(pc=2,java.util.WeakHashMap$KeyIterator,this$0,java.util.WeakHashMap,UVar(defSites={-1},value=_ <: java.util.WeakHashMap$KeyIterator[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.WeakHashMap, null}[↦-2;refId=103])),
	1: NonVirtualMethodCall(pc=7,java.util.WeakHashMap$HashIterator,isInterface=false,void <init>(java.util.WeakHashMap),UVar(defSites={-1},value=_ <: java.util.WeakHashMap$KeyIterator[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.util.WeakHashMap, null}[↦-2;refId=103]))),
	2: Return(pc=10)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.lang.Object next()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value={_ <: java.util.WeakHashMap$Entry, null}[↦1;refId=104],origin=0),VirtualFunctionCall(pc=1,java.util.WeakHashMap$KeyIterator,isInterface=false,java.util.WeakHashMap$Entry nextEntry(),UVar(defSites={-1},value=_ <: java.util.WeakHashMap$KeyIterator[↦-1;refId=102]),())),
	1: Assignment(pc=4,DVar(useSites={2},value={_ <: java.lang.Object, null}[↦4;refId=107],origin=1),VirtualFunctionCall(pc=4,java.util.WeakHashMap$Entry,isInterface=false,java.lang.Object getKey(),UVar(defSites={0},value={_ <: java.util.WeakHashMap$Entry, null}[↦1;refId=104]),())),
	2: ReturnValue(pc=7,UVar(defSites={1},value={_ <: java.lang.Object, null}[↦4;refId=107]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_4,BB_2}
	BB_2: BasicBlock(start=2,end=2) -> {BB_3}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

