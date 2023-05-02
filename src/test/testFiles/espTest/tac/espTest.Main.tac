void main(java.lang.String[])
AITACode(params=(Parameters(
	1: useSites={} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2},value=int = 5,origin=0),IntConst(pc=0,5)),
	1: Assignment(pc=2,DVar(useSites={2},value=int = 6,origin=1),IntConst(pc=2,6)),
	2: Assignment(pc=7,DVar(useSites={5},value=an int,origin=2),StaticFunctionCall(pc=7,espTest.Main,isInterface=false,int add(int,int),(UVar(defSites={0},value=int = 5),UVar(defSites={1},value=int = 6)))),
	3: Assignment(pc=11,DVar(useSites={4,5},value=espTest.Foo[↦11;refId=104],origin=3),New(pc=11,espTest.Foo)),
	4: NonVirtualMethodCall(pc=15,espTest.Foo,isInterface=false,void <init>(),UVar(defSites={3},value=espTest.Foo[↦11;refId=104]),()),
	5: PutField(pc=23,espTest.Foo,a,int,UVar(defSites={3},value=espTest.Foo[↦11;refId=104]),UVar(defSites={2},value=an int)),
	6: Return(pc=26)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_4,BB_2}
	BB_1: BasicBlock(start=5,end=6) -> {BB_3}
	BB_2: BasicBlock(start=3,end=4) -> {BB_4,BB_1}
	BB_3: ExitNode(normalReturn=true)
	BB_4: ExitNode(normalReturn=false)
))

int add(int,int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=an int,origin=0),BinaryExpr(pc=2,ComputationalTypeInt,UVar(defSites={-2},value=an int),+,UVar(defSites={-3},value=an int))),
	1: ReturnValue(pc=3,UVar(defSites={0},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

