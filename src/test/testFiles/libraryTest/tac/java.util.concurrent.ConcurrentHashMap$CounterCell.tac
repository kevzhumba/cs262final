void <init>(long)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.concurrent.ConcurrentHashMap$CounterCell,value,long,UVar(defSites={-1},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦-1;refId=102]),UVar(defSites={-2},value=ALongValue)),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

