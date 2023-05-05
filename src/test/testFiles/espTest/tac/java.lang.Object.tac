void <init>()
AITACode(params=(Parameters(
	0: useSites={} (origin=-1)
)),stmts=(
	0: Return(pc=0)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

void <clinit>()
AITACode(params=(Parameters(
	
)),stmts=(
	0: StaticMethodCall(pc=0,java.lang.Object,isInterface=false,void registerNatives(),()),
	1: Return(pc=3)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void finalize()
AITACode(params=(Parameters(
	0: useSites={} (origin=-1)
)),stmts=(
	0: Return(pc=0)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

registerNatives

