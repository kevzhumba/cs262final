boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={18,10,42,26,14,1,33,5,37,21,29,7} (origin=-1),
	1: useSites={0,4,36,28,34,22,17,9,43,15} (origin=-2),
	2: useSites={34,22,3,43,15} (origin=-3),
	3: useSites={34,22,43,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value={int[], null}[↦2;refId=105],origin=0),GetField(pc=2,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=6,DVar(useSites={2},value=an int,origin=1),GetField(pc=6,java.util.regex.Pattern$LazyLoop,beginIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	2: Assignment(pc=9,DVar(useSites={3},value=an int,origin=2),ArrayLoad(pc=9,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦2;refId=105]))),
	3: If(pc=10,UVar(defSites={-3},value=an int),<=,UVar(defSites={2},value=an int),target=42),
	4: Assignment(pc=14,DVar(useSites={6},value={int[], null}[↦14;refId=112],origin=4),GetField(pc=14,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	5: Assignment(pc=18,DVar(useSites={6},value=an int,origin=5),GetField(pc=18,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	6: Assignment(pc=21,DVar(useSites={8,12,38,19,27,31},value=an int,origin=6),ArrayLoad(pc=21,UVar(defSites={5},value=an int),UVar(defSites={4},value={int[], null}[↦14;refId=112]))),
	7: Assignment(pc=27,DVar(useSites={8},value=an int,origin=7),GetField(pc=27,java.util.regex.Pattern$LazyLoop,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	8: If(pc=30,UVar(defSites={6},value=an int),>=,UVar(defSites={7},value=an int),target=21),
	9: Assignment(pc=34,DVar(useSites={13},value={int[], null}[↦34;refId=127],origin=9),GetField(pc=34,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	10: Assignment(pc=38,DVar(useSites={13},value=an int,origin=10),GetField(pc=38,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	11: Assignment(pc=43,DVar(useSites={12},value=int = 1,origin=11),IntConst(pc=43,1)),
	12: Assignment(pc=44,DVar(useSites={13},value=int ∈ [-2147483647,2147483647],origin=12),BinaryExpr(pc=44,ComputationalTypeInt,UVar(defSites={6},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={11},value=int = 1))),
	13: ArrayStore(pc=45,UVar(defSites={9},value={int[], null}[↦34;refId=127]),UVar(defSites={10},value=an int),UVar(defSites={12},value=int ∈ [-2147483647,2147483647])),
	14: Assignment(pc=47,DVar(useSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦47;refId=130],origin=14),GetField(pc=47,java.util.regex.Pattern$LazyLoop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	15: Assignment(pc=53,DVar(useSites={16,20},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=53,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦47;refId=130]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	16: If(pc=60,UVar(defSites={15},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=20),
	17: Assignment(pc=64,DVar(useSites={19},value={int[], null}[↦64;refId=133],origin=17),GetField(pc=64,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	18: Assignment(pc=68,DVar(useSites={19},value=an int,origin=18),GetField(pc=68,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	19: ArrayStore(pc=73,UVar(defSites={17},value={int[], null}[↦64;refId=133]),UVar(defSites={18},value=an int),UVar(defSites={6},value=int ∈ [-2147483648,2147483646])),
	20: ReturnValue(pc=76,UVar(defSites={15},value=int ∈ [0,1])),
	21: Assignment(pc=78,DVar(useSites={22},value={_ <: java.util.regex.Pattern$Node, null}[↦78;refId=115],origin=21),GetField(pc=78,java.util.regex.Pattern$LazyLoop,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	22: Assignment(pc=84,DVar(useSites={23},value=int ∈ [0,1],origin=22),VirtualFunctionCall(pc=84,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={21},value={_ <: java.util.regex.Pattern$Node, null}[↦78;refId=115]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	23: If(pc=87,UVar(defSites={22},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=26),
	24: Assignment(pc=90,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=90,1)),
	25: ReturnValue(pc=91,UVar(defSites={24},value=int = 1)),
	26: Assignment(pc=95,DVar(useSites={27},value=an int,origin=26),GetField(pc=95,java.util.regex.Pattern$LazyLoop,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	27: If(pc=98,UVar(defSites={6},value=an int),>=,UVar(defSites={26},value=an int),target=40),
	28: Assignment(pc=102,DVar(useSites={32},value={int[], null}[↦102;refId=118],origin=28),GetField(pc=102,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	29: Assignment(pc=106,DVar(useSites={32},value=an int,origin=29),GetField(pc=106,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	30: Assignment(pc=111,DVar(useSites={31},value=int = 1,origin=30),IntConst(pc=111,1)),
	31: Assignment(pc=112,DVar(useSites={32},value=int ∈ [-2147483647,2147483647],origin=31),BinaryExpr(pc=112,ComputationalTypeInt,UVar(defSites={6},value=int ∈ [-2147483648,2147483646]),+,UVar(defSites={30},value=int = 1))),
	32: ArrayStore(pc=113,UVar(defSites={28},value={int[], null}[↦102;refId=118]),UVar(defSites={29},value=an int),UVar(defSites={31},value=int ∈ [-2147483647,2147483647])),
	33: Assignment(pc=115,DVar(useSites={34},value={_ <: java.util.regex.Pattern$Node, null}[↦115;refId=121],origin=33),GetField(pc=115,java.util.regex.Pattern$LazyLoop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	34: Assignment(pc=121,DVar(useSites={35,39},value=int ∈ [0,1],origin=34),VirtualFunctionCall(pc=121,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={33},value={_ <: java.util.regex.Pattern$Node, null}[↦115;refId=121]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=int ∈ [-2147483647,2147483647]),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	35: If(pc=128,UVar(defSites={34},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=39),
	36: Assignment(pc=132,DVar(useSites={38},value={int[], null}[↦132;refId=124],origin=36),GetField(pc=132,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	37: Assignment(pc=136,DVar(useSites={38},value=an int,origin=37),GetField(pc=136,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	38: ArrayStore(pc=141,UVar(defSites={36},value={int[], null}[↦132;refId=124]),UVar(defSites={37},value=an int),UVar(defSites={6},value=int ∈ [-2147483648,2147483646])),
	39: ReturnValue(pc=144,UVar(defSites={34},value=int ∈ [0,1])),
	40: Assignment(pc=145,DVar(useSites={41},value=int = 0,origin=40),IntConst(pc=145,0)),
	41: ReturnValue(pc=146,UVar(defSites={40},value=int = 0)),
	42: Assignment(pc=148,DVar(useSites={43},value={_ <: java.util.regex.Pattern$Node, null}[↦148;refId=109],origin=42),GetField(pc=148,java.util.regex.Pattern$LazyLoop,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	43: Assignment(pc=154,DVar(useSites={44},value=int ∈ [0,1],origin=43),VirtualFunctionCall(pc=154,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={42},value={_ <: java.util.regex.Pattern$Node, null}[↦148;refId=109]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	44: ReturnValue(pc=157,UVar(defSites={43},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_17,BB_3}
	BB_10: BasicBlock(start=39,end=39) -> {BB_7}
	BB_11: BasicBlock(start=3,end=3) -> {BB_16,BB_a}
	BB_12: BasicBlock(start=35,end=35) -> {BB_10,BB_9}
	BB_13: BasicBlock(start=40,end=41) -> {BB_7}
	BB_14: BasicBlock(start=26,end=27) -> {BB_13,BB_c}
	BB_15: BasicBlock(start=23,end=23) -> {BB_14,BB_b}
	BB_16: BasicBlock(start=4,end=6) -> {BB_17,BB_f}
	BB_17: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=14,end=15) -> {BB_17,BB_8}
	BB_2: BasicBlock(start=20,end=20) -> {BB_7}
	BB_3: BasicBlock(start=1,end=2) -> {BB_17,BB_11}
	BB_4: BasicBlock(start=9,end=13) -> {BB_17,BB_1}
	BB_5: BasicBlock(start=17,end=19) -> {BB_17,BB_2}
	BB_6: BasicBlock(start=44,end=44) -> {BB_7}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=16,end=16) -> {BB_2,BB_5}
	BB_9: BasicBlock(start=36,end=38) -> {BB_17,BB_10}
	BB_a: BasicBlock(start=42,end=43) -> {BB_17,BB_6}
	BB_b: BasicBlock(start=24,end=25) -> {BB_7}
	BB_c: BasicBlock(start=28,end=32) -> {BB_17,BB_e}
	BB_d: BasicBlock(start=21,end=22) -> {BB_17,BB_15}
	BB_e: BasicBlock(start=33,end=34) -> {BB_17,BB_12}
	BB_f: BasicBlock(start=7,end=8) -> {BB_4,BB_d}
))

boolean matchInit(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={8,20,26,14,30,1,5,11,23} (origin=-1),
	1: useSites={0,12,22,29,27,7,15} (origin=-2),
	2: useSites={12,27,15} (origin=-3),
	3: useSites={12,27,15} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={int[], null}[↦1;refId=105],origin=0),GetField(pc=1,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	1: Assignment(pc=5,DVar(useSites={2},value=an int,origin=1),GetField(pc=5,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	2: Assignment(pc=8,DVar(useSites={31},value=an int,origin=2),ArrayLoad(pc=8,UVar(defSites={1},value=an int),UVar(defSites={0},value={int[], null}[↦1;refId=105]))),
	3: Assignment(pc=11,DVar(useSites={32},value=int = 0,origin=3),IntConst(pc=11,0)),
	4: Assignment(pc=14,DVar(useSites={6},value=int = 0,origin=4),IntConst(pc=14,0)),
	5: Assignment(pc=16,DVar(useSites={6},value=an int,origin=5),GetField(pc=16,java.util.regex.Pattern$LazyLoop,cmin,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	6: If(pc=19,UVar(defSites={4},value=int = 0),>=,UVar(defSites={5},value=an int),target=14),
	7: Assignment(pc=23,DVar(useSites={10},value={int[], null}[↦23;refId=118],origin=7),GetField(pc=23,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	8: Assignment(pc=27,DVar(useSites={10},value=an int,origin=8),GetField(pc=27,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	9: Assignment(pc=30,DVar(useSites={10},value=int = 1,origin=9),IntConst(pc=30,1)),
	10: ArrayStore(pc=31,UVar(defSites={7},value={int[], null}[↦23;refId=118]),UVar(defSites={8},value=an int),UVar(defSites={9},value=int = 1)),
	11: Assignment(pc=33,DVar(useSites={12},value={_ <: java.util.regex.Pattern$Node, null}[↦33;refId=121],origin=11),GetField(pc=33,java.util.regex.Pattern$LazyLoop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	12: Assignment(pc=39,DVar(useSites={32},value=int ∈ [0,1],origin=12),VirtualFunctionCall(pc=39,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={11},value={_ <: java.util.regex.Pattern$Node, null}[↦33;refId=121]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	13: Goto(pc=44,target=29),
	14: Assignment(pc=48,DVar(useSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦48;refId=109],origin=14),GetField(pc=48,java.util.regex.Pattern$LazyLoop,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	15: Assignment(pc=54,DVar(useSites={16},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=54,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦48;refId=109]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	16: If(pc=57,UVar(defSites={15},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=19),
	17: Assignment(pc=60,DVar(useSites={32},value=int = 1,origin=17),IntConst(pc=60,1)),
	18: Goto(pc=63,target=29),
	19: Assignment(pc=66,DVar(useSites={21},value=int = 0,origin=19),IntConst(pc=66,0)),
	20: Assignment(pc=68,DVar(useSites={21},value=an int,origin=20),GetField(pc=68,java.util.regex.Pattern$LazyLoop,cmax,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	21: If(pc=71,UVar(defSites={19},value=int = 0),>=,UVar(defSites={20},value=an int),target=29),
	22: Assignment(pc=75,DVar(useSites={25},value={int[], null}[↦75;refId=112],origin=22),GetField(pc=75,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	23: Assignment(pc=79,DVar(useSites={25},value=an int,origin=23),GetField(pc=79,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	24: Assignment(pc=82,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=82,1)),
	25: ArrayStore(pc=83,UVar(defSites={22},value={int[], null}[↦75;refId=112]),UVar(defSites={23},value=an int),UVar(defSites={24},value=int = 1)),
	26: Assignment(pc=85,DVar(useSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦85;refId=115],origin=26),GetField(pc=85,java.util.regex.Pattern$LazyLoop,body,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	27: Assignment(pc=91,DVar(useSites={32},value=int ∈ [0,1],origin=27),VirtualFunctionCall(pc=91,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={26},value={_ <: java.util.regex.Pattern$Node, null}[↦85;refId=115]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	28: Nop(pc=94),
	29: Assignment(pc=97,DVar(useSites={31},value={int[], null}[↦97;refId=124],origin=29),GetField(pc=97,java.util.regex.Matcher,locals,int[],UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]))),
	30: Assignment(pc=101,DVar(useSites={31},value=an int,origin=30),GetField(pc=101,java.util.regex.Pattern$LazyLoop,countIndex,int,UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]))),
	31: ArrayStore(pc=106,UVar(defSites={29},value={int[], null}[↦97;refId=124]),UVar(defSites={30},value=an int),UVar(defSites={2},value=an int)),
	32: ReturnValue(pc=109,UVar(defSites={12,17,3,27},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_e,BB_3}
	BB_10: BasicBlock(start=17,end=18) -> {BB_2}
	BB_1: BasicBlock(start=14,end=15) -> {BB_e,BB_a}
	BB_2: BasicBlock(start=29,end=31) -> {BB_e,BB_f}
	BB_3: BasicBlock(start=1,end=2) -> {BB_e,BB_8}
	BB_4: BasicBlock(start=28,end=28) -> {BB_2}
	BB_5: BasicBlock(start=13,end=13) -> {BB_2}
	BB_6: BasicBlock(start=22,end=25) -> {BB_e,BB_c}
	BB_7: BasicBlock(start=7,end=10) -> {BB_e,BB_b}
	BB_8: BasicBlock(start=3,end=6) -> {BB_7,BB_1}
	BB_9: ExitNode(normalReturn=true)
	BB_a: BasicBlock(start=16,end=16) -> {BB_10,BB_d}
	BB_b: BasicBlock(start=11,end=12) -> {BB_e,BB_5}
	BB_c: BasicBlock(start=26,end=27) -> {BB_e,BB_4}
	BB_d: BasicBlock(start=19,end=21) -> {BB_2,BB_6}
	BB_e: ExitNode(normalReturn=false)
	BB_f: BasicBlock(start=32,end=32) -> {BB_9}
))

boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={} (origin=-1),
	1: useSites={1,3} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=1,0)),
	1: PutField(pc=2,java.util.regex.Pattern$TreeInfo,maxValid,boolean,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]),UVar(defSites={0},value=int = 0)),
	2: Assignment(pc=6,DVar(useSites={3},value=int = 0,origin=2),IntConst(pc=6,0)),
	3: PutField(pc=7,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={2},value=int = 0)),
	4: Assignment(pc=10,DVar(useSites={5},value=int = 0,origin=4),IntConst(pc=10,0)),
	5: ReturnValue(pc=11,UVar(defSites={4},value=int = 0))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=5) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void <init>(int,int)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2),
	2: useSites={0} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=3,java.util.regex.Pattern$Loop,isInterface=false,void <init>(int,int),UVar(defSites={-1},value=java.util.regex.Pattern$LazyLoop[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={-3},value=an int))),
	1: Return(pc=6)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

