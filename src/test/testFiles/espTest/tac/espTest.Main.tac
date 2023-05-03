void main(java.lang.String[])
AITACode(params=(Parameters(
	1: useSites={} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={4},value=int = 5,origin=0),IntConst(pc=0,5)),
	1: Assignment(pc=2,DVar(useSites={4},value=int = 6,origin=1),IntConst(pc=2,6)),
	2: Assignment(pc=5,DVar(useSites={4,5,3},value=espTest.Foo[↦5;refId=103],origin=2),New(pc=5,espTest.Foo)),
	3: NonVirtualMethodCall(pc=9,espTest.Foo,isInterface=false,void <init>(),UVar(defSites={2},value=espTest.Foo[↦5;refId=103]),()),
	4: Assignment(pc=16,DVar(useSites={5},value=an int,origin=4),VirtualFunctionCall(pc=16,espTest.Foo,isInterface=false,int add(int,int),UVar(defSites={2},value=espTest.Foo[↦5;refId=103]),(UVar(defSites={0},value=int = 5),UVar(defSites={1},value=int = 6)))),
	5: PutField(pc=24,espTest.Foo,a,int,UVar(defSites={2},value=espTest.Foo[↦5;refId=103]),UVar(defSites={4},value=an int)),
	6: Return(pc=27)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_4,BB_3}
	BB_1: BasicBlock(start=5,end=6) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=4,end=4) -> {BB_4,BB_1}
	BB_4: ExitNode(normalReturn=false)
))

