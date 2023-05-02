void <init>(int)
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1),
	1: useSites={1} (origin=-2)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$GroupHead[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$GroupHead,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupHead[↦-1;refId=102]),UVar(defSites={-2},value=an int)),
	2: Return(pc=9)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={4,6,1,9} (origin=-1),
	1: useSites={0,8,3,7} (origin=-2),
	2: useSites={5,7} (origin=-3),
	3: useSites={7} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern$GroupHead,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupHead[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={10},value=an int,origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: Assignment(pc=12,DVar(useSites={5},value={int[], null}[↦12;refId=109],origin=3),GetField(pc=12,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	4: Assignment(pc=16,DVar(useSites={5},value=an int,origin=4),GetField(pc=16,java.util.regex.Pattern$GroupHead,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupHead[↦-1;refId=102]))),
	5: ArrayStore(pc=20,UVar(defSites={3},value={int[], null}[↦12;refId=109]),UVar(defSites={4},value=an int),UVar(defSites={-3},value=an int)),
	6: Assignment(pc=22,DVar(useSites={7},value={_ <: java.util.regex.Pattern$Node, null}[↦22;refId=112],origin=6),GetField(pc=22,java.util.regex.Pattern$GroupHead,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$GroupHead[↦-1;refId=102]))),
	7: Assignment(pc=28,DVar(useSites={11},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=28,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦22;refId=112]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	8: Assignment(pc=34,DVar(useSites={10},value={int[], null}[↦34;refId=115],origin=8),GetField(pc=34,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	9: Assignment(pc=38,DVar(useSites={10},value=an int,origin=9),GetField(pc=38,java.util.regex.Pattern$GroupHead,localIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$GroupHead[↦-1;refId=102]))),
	10: ArrayStore(pc=43,UVar(defSites={8},value={int[], null}[↦34;refId=115]),UVar(defSites={9},value=an int),UVar(defSites={2},value=an int)),
	11: ReturnValue(pc=46,UVar(defSites={7},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_7,BB_1}
	BB_1: BasicBlock(start=1,end=2) -> {BB_7,BB_3}
	BB_2: BasicBlock(start=6,end=7) -> {BB_7,BB_6}
	BB_3: BasicBlock(start=3,end=5) -> {BB_7,BB_2}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=11,end=11) -> {BB_4}
	BB_6: BasicBlock(start=8,end=10) -> {BB_7,BB_5}
	BB_7: ExitNode(normalReturn=false)
))

