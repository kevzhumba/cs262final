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

void main(java.lang.String[])
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=int ∈ [0,2147483647],origin=0),ArrayLength(pc=1,UVar(defSites={-2},value={java.lang.String[], null}[↦-1;refId=102]))),
	1: Assignment(pc=2,DVar(useSites={2},value=int = 4,origin=1),IntConst(pc=2,4)),
	2: If(pc=3,UVar(defSites={0},value=int ∈ [0,2147483647]),>=,UVar(defSites={1},value=int = 4),target=7),
	3: Assignment(pc=6,DVar(useSites={5},value=int = 5,origin=3),IntConst(pc=6,5)),
	4: Assignment(pc=7,DVar(useSites={5},value=int = 6,origin=4),IntConst(pc=7,6)),
	5: Assignment(pc=9,DVar(useSites={13},value=an int,origin=5),StaticFunctionCall(pc=9,callIfStatement.Main,isInterface=false,int foo1(int,int),(UVar(defSites={3},value=int = 5),UVar(defSites={4},value=int = 6)))),
	6: Goto(pc=13,target=11),
	7: Assignment(pc=16,DVar(useSites={9},value=int = 5,origin=7),IntConst(pc=16,5)),
	8: Assignment(pc=17,DVar(useSites={9},value=int = 7,origin=8),IntConst(pc=17,7)),
	9: Assignment(pc=19,DVar(useSites={13},value=an int,origin=9),StaticFunctionCall(pc=19,callIfStatement.Main,isInterface=false,int foo1(int,int),(UVar(defSites={7},value=int = 5),UVar(defSites={8},value=int = 7)))),
	10: Nop(pc=22),
	11: Assignment(pc=23,DVar(useSites={12,13},value=callIfStatement.Foo[↦23;refId=106],origin=11),New(pc=23,callIfStatement.Foo)),
	12: NonVirtualMethodCall(pc=27,callIfStatement.Foo,isInterface=false,void <init>(),UVar(defSites={11},value=callIfStatement.Foo[↦23;refId=106]),()),
	13: PutField(pc=33,callIfStatement.Foo,a,int,UVar(defSites={11},value=callIfStatement.Foo[↦23;refId=106]),UVar(defSites={9,5},value=an int)),
	14: Return(pc=36)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_9,BB_2}
	BB_1: BasicBlock(start=10,end=10) -> {BB_8}
	BB_2: BasicBlock(start=1,end=2) -> {BB_5,BB_6}
	BB_3: BasicBlock(start=6,end=6) -> {BB_8}
	BB_4: BasicBlock(start=13,end=14) -> {BB_7}
	BB_5: BasicBlock(start=7,end=9) -> {BB_9,BB_1}
	BB_6: BasicBlock(start=3,end=5) -> {BB_9,BB_3}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=11,end=12) -> {BB_9,BB_4}
	BB_9: ExitNode(normalReturn=false)
))

