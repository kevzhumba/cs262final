int foo(int)
AITACode(params=(Parameters(
	1: useSites={} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={2},value=int = 4,origin=0),IntConst(pc=0,4)),
	1: Assignment(pc=1,DVar(useSites={2},value=int = 5,origin=1),IntConst(pc=1,5)),
	2: Assignment(pc=2,DVar(useSites={9},value=an int,origin=2),StaticFunctionCall(pc=2,popTest.Main,isInterface=false,int foo1(int,int),(UVar(defSites={0},value=int = 4),UVar(defSites={1},value=int = 5)))),
	3: Assignment(pc=6,DVar(useSites={5},value=int = 4,origin=3),IntConst(pc=6,4)),
	4: Assignment(pc=7,DVar(useSites={5},value=int = 5,origin=4),IntConst(pc=7,5)),
	5: Assignment(pc=8,DVar(useSites={9},value=an int,origin=5),StaticFunctionCall(pc=8,popTest.Main,isInterface=false,int foo1(int,int),(UVar(defSites={3},value=int = 4),UVar(defSites={4},value=int = 5)))),
	6: Assignment(pc=12,DVar(useSites={8},value=int = 5,origin=6),IntConst(pc=12,5)),
	7: Assignment(pc=13,DVar(useSites={8},value=int = 6,origin=7),IntConst(pc=13,6)),
	8: Assignment(pc=15,DVar(useSites={10},value=an int,origin=8),StaticFunctionCall(pc=15,popTest.Main,isInterface=false,int foo1(int,int),(UVar(defSites={6},value=int = 5),UVar(defSites={7},value=int = 6)))),
	9: Assignment(pc=21,DVar(useSites={10},value=an int,origin=9),BinaryExpr(pc=21,ComputationalTypeInt,UVar(defSites={2},value=an int),+,UVar(defSites={5},value=an int))),
	10: Assignment(pc=23,DVar(useSites={11},value=an int,origin=10),BinaryExpr(pc=23,ComputationalTypeInt,UVar(defSites={9},value=an int),+,UVar(defSites={8},value=an int))),
	11: ReturnValue(pc=24,UVar(defSites={10},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_5,BB_3}
	BB_1: BasicBlock(start=6,end=8) -> {BB_5,BB_2}
	BB_2: BasicBlock(start=9,end=11) -> {BB_4}
	BB_3: BasicBlock(start=3,end=5) -> {BB_5,BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: ExitNode(normalReturn=false)
))

void main(java.lang.String[])
AITACode(params=(Parameters(
	1: useSites={} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value=int = 5,origin=0),IntConst(pc=0,5)),
	1: Assignment(pc=1,DVar(useSites={6},value=an int,origin=1),StaticFunctionCall(pc=1,popTest.Main,isInterface=false,int foo(int),(UVar(defSites={0},value=int = 5)))),
	2: Assignment(pc=5,DVar(useSites={3},value=int = 5,origin=2),IntConst(pc=5,5)),
	3: Assignment(pc=6,DVar(useSites={6},value=an int,origin=3),StaticFunctionCall(pc=6,popTest.Main,isInterface=false,int foo(int),(UVar(defSites={2},value=int = 5)))),
	4: Assignment(pc=10,DVar(useSites={5,7},value=popTest.Foo[↦10;refId=105],origin=4),New(pc=10,popTest.Foo)),
	5: NonVirtualMethodCall(pc=14,popTest.Foo,isInterface=false,void <init>(),UVar(defSites={4},value=popTest.Foo[↦10;refId=105]),()),
	6: Assignment(pc=21,DVar(useSites={7},value=an int,origin=6),BinaryExpr(pc=21,ComputationalTypeInt,UVar(defSites={1},value=an int),+,UVar(defSites={3},value=an int))),
	7: PutField(pc=22,popTest.Foo,a,int,UVar(defSites={4},value=popTest.Foo[↦10;refId=105]),UVar(defSites={6},value=an int)),
	8: Return(pc=25)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_5,BB_2}
	BB_1: BasicBlock(start=6,end=8) -> {BB_3}
	BB_2: BasicBlock(start=2,end=3) -> {BB_5,BB_4}
	BB_3: ExitNode(normalReturn=true)
	BB_4: BasicBlock(start=4,end=5) -> {BB_5,BB_1}
	BB_5: ExitNode(normalReturn=false)
))

int foo1(int,int)
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

