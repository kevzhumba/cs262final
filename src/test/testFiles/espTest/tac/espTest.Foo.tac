void <init>()
AITACode(params=(Parameters(
	0: useSites={0,2} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.lang.Object,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: espTest.Foo[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value=int = 5,origin=1),IntConst(pc=5,5)),
	2: PutField(pc=6,espTest.Foo,a,int,UVar(defSites={-1},value=_ <: espTest.Foo[↦-1;refId=102]),UVar(defSites={1},value=int = 5)),
	3: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

