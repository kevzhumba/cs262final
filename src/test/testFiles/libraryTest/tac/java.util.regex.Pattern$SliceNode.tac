boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={10,6,1} (origin=-1),
	1: useSites={0,4,9,5,11} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={3},value=an int,origin=0),GetField(pc=2,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={2},value={int[], null}[↦6;refId=105],origin=1),GetField(pc=6,java.util.regex.Pattern$SliceNode,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceNode[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=9,UVar(defSites={1},value={int[], null}[↦6;refId=105]))),
	3: Assignment(pc=10,DVar(useSites={4},value=an int,origin=3),BinaryExpr(pc=10,ComputationalTypeInt,UVar(defSites={0},value=an int),+,UVar(defSites={2},value=int ∈ [0,2147483647]))),
	4: PutField(pc=11,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={3},value=an int)),
	5: Assignment(pc=16,DVar(useSites={8},value=an int,origin=5),GetField(pc=16,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]))),
	6: Assignment(pc=20,DVar(useSites={7},value={int[], null}[↦20;refId=107],origin=6),GetField(pc=20,java.util.regex.Pattern$SliceNode,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceNode[↦-1;refId=102]))),
	7: Assignment(pc=23,DVar(useSites={8},value=int ∈ [0,2147483647],origin=7),ArrayLength(pc=23,UVar(defSites={6},value={int[], null}[↦20;refId=107]))),
	8: Assignment(pc=24,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=24,ComputationalTypeInt,UVar(defSites={5},value=an int),+,UVar(defSites={7},value=int ∈ [0,2147483647]))),
	9: PutField(pc=25,java.util.regex.Pattern$TreeInfo,maxLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={8},value=an int)),
	10: Assignment(pc=29,DVar(useSites={11},value={_ <: java.util.regex.Pattern$Node, null}[↦29;refId=109],origin=10),GetField(pc=29,java.util.regex.Pattern$SliceNode,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceNode[↦-1;refId=102]))),
	11: Assignment(pc=33,DVar(useSites={12},value=int ∈ [0,1],origin=11),VirtualFunctionCall(pc=33,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={10},value={_ <: java.util.regex.Pattern$Node, null}[↦29;refId=109]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	12: ReturnValue(pc=36,UVar(defSites={11},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_6,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_6,BB_3}
	BB_2: BasicBlock(start=12,end=12) -> {BB_4}
	BB_3: BasicBlock(start=3,end=7) -> {BB_6,BB_5}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=8,end=11) -> {BB_6,BB_2}
	BB_6: ExitNode(normalReturn=false)
))

void <init>(int[])
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceNode[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$SliceNode,buffer,int[],UVar(defSites={-1},value=_ <: java.util.regex.Pattern$SliceNode[↦-1;refId=102]),UVar(defSites={-2},value={int[], null}[↦-2;refId=103])),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

