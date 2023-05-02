void tryPresize(int)
AITACode(params=(Parameters(
	0: useSites={32,28,46,49,25,37,13,11,23} (origin=-1),
	1: useSites={6,1,5} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int = 536870912,origin=0),IntConst(pc=1,536870912)),
	1: If(pc=3,UVar(defSites={-2},value=an int),<,UVar(defSites={0},value=int = 536870912),target=4),
	2: Assignment(pc=6,DVar(useSites={34,30,17,27,31},value=int = 1073741824,origin=2),IntConst(pc=6,1073741824)),
	3: Goto(pc=8,target=10),
	4: Assignment(pc=13,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=13,1)),
	5: Assignment(pc=14,DVar(useSites={6},value=int ∈ [0,2147483647],origin=5),BinaryExpr(pc=14,ComputationalTypeInt,UVar(defSites={-2},value=int ∈ [-2147483648,536870911]),>>>,UVar(defSites={4},value=int = 1))),
	6: Assignment(pc=15,DVar(useSites={8},value=an int,origin=6),BinaryExpr(pc=15,ComputationalTypeInt,UVar(defSites={-2},value=int ∈ [-2147483648,536870911]),+,UVar(defSites={5},value=int ∈ [0,2147483647]))),
	7: Assignment(pc=16,DVar(useSites={8},value=int = 1,origin=7),IntConst(pc=16,1)),
	8: Assignment(pc=17,DVar(useSites={9},value=an int,origin=8),BinaryExpr(pc=17,ComputationalTypeInt,UVar(defSites={6},value=an int),+,UVar(defSites={7},value=int = 1))),
	9: Assignment(pc=18,DVar(useSites={34,30,17,27,31},value=an int,origin=9),StaticFunctionCall(pc=18,java.util.concurrent.ConcurrentHashMap,isInterface=false,int tableSizeFor(int),(UVar(defSites={8},value=an int)))),
	10: Nop(pc=21),
	11: Assignment(pc=23,DVar(useSites={32,12,34,46,30,17,27,23,31},value=an int,origin=11),GetField(pc=23,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	12: If(pc=28,UVar(defSites={11},value=an int),<,IntConst(pc=-333,0),target=51),
	13: Assignment(pc=32,DVar(useSites={26,38,14,49,15},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦32;refId=104],origin=13),GetField(pc=32,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	14: If(pc=39,UVar(defSites={13},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦32;refId=104]),==,NullExpr(pc=-333),target=17),
	15: Assignment(pc=44,DVar(useSites={16,36,39},value=int ∈ [0,2147483647],origin=15),ArrayLength(pc=44,UVar(defSites={13},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦32;refId=104]))),
	16: If(pc=48,UVar(defSites={15},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=34),
	17: If(pc=53,UVar(defSites={11},value=int ∈ [0,2147483647]),<=,UVar(defSites={2,9},value=an int),target=19),
	18: Goto(pc=57,target=20),
	19: Nop(pc=60),
	20: Assignment(pc=63,DVar(useSites={23},value={jdk.internal.misc.Unsafe, null}[↦63;refId=111],origin=20),GetStatic(pc=63,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	21: Assignment(pc=67,DVar(useSites={23},value=ALongValue,origin=21),GetStatic(pc=67,java.util.concurrent.ConcurrentHashMap,SIZECTL,long)),
	22: Assignment(pc=71,DVar(useSites={23},value=int = -1,origin=22),IntConst(pc=71,-1)),
	23: Assignment(pc=72,DVar(useSites={24},value=int ∈ [0,1],origin=23),VirtualFunctionCall(pc=72,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={20},value={jdk.internal.misc.Unsafe, null}[↦63;refId=111]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={21},value=ALongValue),UVar(defSites={11},value=int ∈ [0,2147483647]),UVar(defSites={22},value=int = -1)))),
	24: If(pc=75,UVar(defSites={23},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	25: Assignment(pc=79,DVar(useSites={26},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦79;refId=114],origin=25),GetField(pc=79,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	26: If(pc=84,UVar(defSites={25},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦79;refId=114]),!=,UVar(defSites={13},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦32;refId=104]),target=32),
	27: Assignment(pc=89,DVar(useSites={28},value=java.util.concurrent.ConcurrentHashMap$Node[][↦89;refId=115],origin=27),NewArray(pc=89,[UVar(defSites={2,9,11},value=int ∈ [0,2147483647])],java.util.concurrent.ConcurrentHashMap$Node[])),
	28: PutField(pc=97,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={27},value=java.util.concurrent.ConcurrentHashMap$Node[][↦89;refId=115])),
	29: Assignment(pc=104,DVar(useSites={30},value=int = 2,origin=29),IntConst(pc=104,2)),
	30: Assignment(pc=105,DVar(useSites={31},value=int ∈ [0,536870911],origin=30),BinaryExpr(pc=105,ComputationalTypeInt,UVar(defSites={2,9,11},value=int ∈ [0,2147483647]),>>>,UVar(defSites={29},value=int = 2))),
	31: Assignment(pc=106,DVar(useSites={32},value=int ∈ [-536870911,2147483647],origin=31),BinaryExpr(pc=106,ComputationalTypeInt,UVar(defSites={2,9,11},value=int ∈ [0,2147483647]),-,UVar(defSites={30},value=int ∈ [0,536870911]))),
	32: PutField(pc=110,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={11,31},value=an int)),
	33: Goto(pc=113,target=11),
	34: If(pc=131,UVar(defSites={2,9},value=an int),<=,UVar(defSites={11},value=int ∈ [0,2147483647]),target=51),
	35: Assignment(pc=136,DVar(useSites={36},value=int = 1073741824,origin=35),IntConst(pc=136,1073741824)),
	36: If(pc=138,UVar(defSites={15},value=int ∈ [1,2147483647]),>=,UVar(defSites={35},value=int = 1073741824),target=51),
	37: Assignment(pc=147,DVar(useSites={38},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦147;refId=105],origin=37),GetField(pc=147,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	38: If(pc=150,UVar(defSites={13},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦32;refId=104]),!=,UVar(defSites={37},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦147;refId=105]),target=11),
	39: Assignment(pc=155,DVar(useSites={43},value=an int,origin=39),StaticFunctionCall(pc=155,java.util.concurrent.ConcurrentHashMap,isInterface=false,int resizeStamp(int),(UVar(defSites={15},value=int ∈ [1,1073741823])))),
	40: Assignment(pc=160,DVar(useSites={46},value={jdk.internal.misc.Unsafe, null}[↦160;refId=107],origin=40),GetStatic(pc=160,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	41: Assignment(pc=164,DVar(useSites={46},value=ALongValue,origin=41),GetStatic(pc=164,java.util.concurrent.ConcurrentHashMap,SIZECTL,long)),
	42: Assignment(pc=170,DVar(useSites={43},value=int = 16,origin=42),IntConst(pc=170,16)),
	43: Assignment(pc=172,DVar(useSites={45},value=an int,origin=43),BinaryExpr(pc=172,ComputationalTypeInt,UVar(defSites={39},value=an int),<<,UVar(defSites={42},value=int = 16))),
	44: Assignment(pc=173,DVar(useSites={45},value=int = 2,origin=44),IntConst(pc=173,2)),
	45: Assignment(pc=174,DVar(useSites={46},value=an int,origin=45),BinaryExpr(pc=174,ComputationalTypeInt,UVar(defSites={43},value=an int),+,UVar(defSites={44},value=int = 2))),
	46: Assignment(pc=175,DVar(useSites={47},value=int ∈ [0,1],origin=46),VirtualFunctionCall(pc=175,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={40},value={jdk.internal.misc.Unsafe, null}[↦160;refId=107]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={41},value=ALongValue),UVar(defSites={11},value=int ∈ [0,2147483646]),UVar(defSites={45},value=an int)))),
	47: If(pc=178,UVar(defSites={46},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=11),
	48: Assignment(pc=184,DVar(useSites={49},value=null[↦184],origin=48),NullExpr(pc=184)),
	49: VirtualMethodCall(pc=185,java.util.concurrent.ConcurrentHashMap,isInterface=false,void transfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node[]),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={13},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦32;refId=104]),UVar(defSites={48},value=null[↦184]))),
	50: Goto(pc=188,target=11),
	51: Return(pc=191)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4,BB_16}
	BB_10: BasicBlock(start=34,end=34) -> {BB_7,BB_14}
	BB_11: BasicBlock(start=48,end=49) -> {BB_17,BB_8}
	BB_12: BasicBlock(start=18,end=18) -> {BB_2}
	BB_13: ExitNode(normalReturn=true)
	BB_14: BasicBlock(start=51,end=51) -> {BB_13}
	BB_15: BasicBlock(start=19,end=19) -> {BB_2}
	BB_16: BasicBlock(start=4,end=9) -> {BB_17,BB_1}
	BB_17: ExitNode(normalReturn=false)
	BB_18: BasicBlock(start=47,end=47) -> {BB_9,BB_11}
	BB_19: BasicBlock(start=15,end=16) -> {BB_10,BB_e}
	BB_1: BasicBlock(start=10,end=10) -> {BB_9}
	BB_2: BasicBlock(start=20,end=23) -> {BB_17,BB_b}
	BB_3: BasicBlock(start=13,end=14) -> {BB_19,BB_e}
	BB_4: BasicBlock(start=2,end=3) -> {BB_1}
	BB_5: BasicBlock(start=27,end=31) -> {BB_f}
	BB_6: BasicBlock(start=39,end=39) -> {BB_17,BB_a}
	BB_7: BasicBlock(start=35,end=36) -> {BB_c,BB_14}
	BB_8: BasicBlock(start=50,end=50) -> {BB_9}
	BB_9: BasicBlock(start=11,end=12) -> {BB_3,BB_14}
	BB_a: BasicBlock(start=40,end=46) -> {BB_17,BB_18}
	BB_b: BasicBlock(start=24,end=24) -> {BB_9,BB_d}
	BB_c: BasicBlock(start=37,end=38) -> {BB_9,BB_6}
	BB_d: BasicBlock(start=25,end=26) -> {BB_f,BB_5}
	BB_e: BasicBlock(start=17,end=17) -> {BB_12,BB_15}
	BB_f: BasicBlock(start=32,end=33) -> {BB_9}
),exceptionHandlers=(
	ExceptionHandler([25, 32) -> -1, <FINALLY>)
))

boolean casTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node,java.util.concurrent.ConcurrentHashMap$Node)
AITACode(params=(Parameters(
	1: useSites={7} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={7} (origin=-4),
	4: useSites={7} (origin=-5)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={7},value={jdk.internal.misc.Unsafe, null}[↦0;refId=105],origin=0),GetStatic(pc=0,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	1: Assignment(pc=5,DVar(useSites={3},value=ALongValue,origin=1),PrimitiveTypecastExpr(pc=5,LongType,UVar(defSites={-3},value=an int))),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),GetStatic(pc=6,java.util.concurrent.ConcurrentHashMap,ASHIFT,int)),
	3: Assignment(pc=9,DVar(useSites={6},value=ALongValue,origin=3),BinaryExpr(pc=9,ComputationalTypeLong,UVar(defSites={1},value=ALongValue),<<,UVar(defSites={2},value=an int))),
	4: Assignment(pc=10,DVar(useSites={5},value=an int,origin=4),GetStatic(pc=10,java.util.concurrent.ConcurrentHashMap,ABASE,int)),
	5: Assignment(pc=13,DVar(useSites={6},value=ALongValue,origin=5),PrimitiveTypecastExpr(pc=13,LongType,UVar(defSites={4},value=an int))),
	6: Assignment(pc=14,DVar(useSites={7},value=ALongValue,origin=6),BinaryExpr(pc=14,ComputationalTypeLong,UVar(defSites={3},value=ALongValue),+,UVar(defSites={5},value=ALongValue))),
	7: Assignment(pc=17,DVar(useSites={8},value=int ∈ [0,1],origin=7),VirtualFunctionCall(pc=17,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetObject(java.lang.Object,long,java.lang.Object,java.lang.Object),UVar(defSites={0},value={jdk.internal.misc.Unsafe, null}[↦0;refId=105]),(UVar(defSites={-2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-1;refId=102]),UVar(defSites={6},value=ALongValue),UVar(defSites={-4},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-3;refId=103]),UVar(defSites={-5},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-4;refId=104])))),
	8: ReturnValue(pc=20,UVar(defSites={7},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=7) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=8,end=8) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.util.concurrent.ConcurrentHashMap$Node[] initTable()
AITACode(params=(Parameters(
	0: useSites={0,4,25,21,13,11} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,1,27},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	1: If(pc=6,UVar(defSites={0},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦1;refId=103]),==,NullExpr(pc=-333),target=4),
	2: Assignment(pc=10,DVar(useSites={3},value=int ∈ [0,2147483647],origin=2),ArrayLength(pc=10,UVar(defSites={0},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦1;refId=103]))),
	3: If(pc=11,UVar(defSites={2},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=27),
	4: Assignment(pc=15,DVar(useSites={24,20,17,25,5,11,23},value=an int,origin=4),GetField(pc=15,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	5: If(pc=20,UVar(defSites={4},value=an int),>=,IntConst(pc=-333,0),target=8),
	6: StaticMethodCall(pc=23,java.lang.Thread,isInterface=false,void yield(),()),
	7: Goto(pc=26,target=0),
	8: Assignment(pc=29,DVar(useSites={11},value={jdk.internal.misc.Unsafe, null}[↦29;refId=105],origin=8),GetStatic(pc=29,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	9: Assignment(pc=33,DVar(useSites={11},value=ALongValue,origin=9),GetStatic(pc=33,java.util.concurrent.ConcurrentHashMap,SIZECTL,long)),
	10: Assignment(pc=37,DVar(useSites={11},value=int = -1,origin=10),IntConst(pc=37,-1)),
	11: Assignment(pc=38,DVar(useSites={12},value=int ∈ [0,1],origin=11),VirtualFunctionCall(pc=38,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={8},value={jdk.internal.misc.Unsafe, null}[↦29;refId=105]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={9},value=ALongValue),UVar(defSites={4},value=int ∈ [0,2147483647]),UVar(defSites={10},value=int = -1)))),
	12: If(pc=41,UVar(defSites={11},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=0),
	13: Assignment(pc=45,DVar(useSites={14,27,15},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦45;refId=108],origin=13),GetField(pc=45,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	14: If(pc=50,UVar(defSites={13},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦45;refId=108]),==,NullExpr(pc=-333),target=17),
	15: Assignment(pc=54,DVar(useSites={16},value=int ∈ [0,2147483647],origin=15),ArrayLength(pc=54,UVar(defSites={13},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦45;refId=108]))),
	16: If(pc=55,UVar(defSites={15},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=25),
	17: If(pc=59,UVar(defSites={4},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=19),
	18: Goto(pc=63,target=20),
	19: Assignment(pc=66,DVar(useSites={24,20,23},value=int ∈ [1,2147483647],origin=19),IntConst(pc=66,16)),
	20: Assignment(pc=70,DVar(useSites={21,27},value=java.util.concurrent.ConcurrentHashMap$Node[][↦70;refId=110],origin=20),NewArray(pc=70,[UVar(defSites={4,19},value=int ∈ [1,2147483647])],java.util.concurrent.ConcurrentHashMap$Node[])),
	21: PutField(pc=80,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={20},value=java.util.concurrent.ConcurrentHashMap$Node[][↦70;refId=110])),
	22: Assignment(pc=85,DVar(useSites={23},value=int = 2,origin=22),IntConst(pc=85,2)),
	23: Assignment(pc=86,DVar(useSites={24},value=int ∈ [0,536870911],origin=23),BinaryExpr(pc=86,ComputationalTypeInt,UVar(defSites={4,19},value=int ∈ [1,2147483647]),>>>,UVar(defSites={22},value=int = 2))),
	24: Assignment(pc=87,DVar(useSites={25},value=int ∈ [-536870910,2147483647],origin=24),BinaryExpr(pc=87,ComputationalTypeInt,UVar(defSites={4,19},value=int ∈ [1,2147483647]),-,UVar(defSites={23},value=int ∈ [0,536870911]))),
	25: PutField(pc=91,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={24,4},value=an int)),
	26: Goto(pc=94,target=27),
	27: ReturnValue(pc=111,UVar(defSites={0,20,13},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=112; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦1;refId=103], _ <: java.util.concurrent.ConcurrentHashMap$Node[][↦45;refId=108], java.util.concurrent.ConcurrentHashMap$Node[][↦70;refId=110]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_f,BB_5}
	BB_10: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=25,end=26) -> {BB_7}
	BB_2: BasicBlock(start=20,end=24) -> {BB_1}
	BB_3: BasicBlock(start=6,end=6) -> {BB_10,BB_9}
	BB_4: BasicBlock(start=13,end=14) -> {BB_6,BB_c}
	BB_5: BasicBlock(start=2,end=3) -> {BB_f,BB_7}
	BB_6: BasicBlock(start=17,end=17) -> {BB_b,BB_d}
	BB_7: BasicBlock(start=27,end=27) -> {BB_e}
	BB_8: BasicBlock(start=12,end=12) -> {BB_0,BB_4}
	BB_9: BasicBlock(start=7,end=7) -> {BB_0}
	BB_a: BasicBlock(start=8,end=11) -> {BB_10,BB_8}
	BB_b: BasicBlock(start=19,end=19) -> {BB_2}
	BB_c: BasicBlock(start=15,end=16) -> {BB_6,BB_1}
	BB_d: BasicBlock(start=18,end=18) -> {BB_2}
	BB_e: ExitNode(normalReturn=true)
	BB_f: BasicBlock(start=4,end=5) -> {BB_a,BB_3}
),exceptionHandlers=(
	ExceptionHandler([13, 25) -> -1, <FINALLY>)
))

long sumCount()
AITACode(params=(Parameters(
	0: useSites={0,1} (origin=-1)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2,6,3},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	1: Assignment(pc=6,DVar(useSites={12,9},value=ALongValue,origin=1),GetField(pc=6,java.util.concurrent.ConcurrentHashMap,baseCount,long,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	2: If(pc=11,UVar(defSites={0},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦1;refId=103]),==,NullExpr(pc=-333),target=12),
	3: Assignment(pc=19,DVar(useSites={5},value=int ∈ [0,2147483647],origin=3),ArrayLength(pc=19,UVar(defSites={0},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦1;refId=103]))),
	4: Assignment(pc=22,DVar(useSites={10,6,5},value=int = 0,origin=4),IntConst(pc=22,0)),
	5: If(pc=29,UVar(defSites={4,10},value=an int),>=,UVar(defSites={3},value=int ∈ [0,2147483647]),target=12),
	6: Assignment(pc=36,DVar(useSites={8,7},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦36;refId=147],origin=6),ArrayLoad(pc=36,UVar(defSites={4,10},value=int ∈ [-2147483648,2147483646]),UVar(defSites={0},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦1;refId=103]))),
	7: If(pc=41,UVar(defSites={6},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦36;refId=147]),==,NullExpr(pc=-333),target=10),
	8: Assignment(pc=47,DVar(useSites={9},value=ALongValue,origin=8),GetField(pc=47,java.util.concurrent.ConcurrentHashMap$CounterCell,value,long,UVar(defSites={6},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦36;refId=147]))),
	9: Assignment(pc=50,DVar(useSites={12,10},value=ALongValue,origin=9),BinaryExpr(pc=50,ComputationalTypeLong,UVar(defSites={1,9},value=ALongValue),+,UVar(defSites={8},value=ALongValue))),
	10: Assignment(pc=52,DVar(useSites={6,5,11},value=an int,origin=10),BinaryExpr(pc=52,ComputationalTypeInt,UVar(defSites={4,10},value=an int),+,IntConst(pc=52,1))),
	11: Goto(pc=55,target=5),
	12: ReturnValue(pc=59,UVar(defSites={1,9},value=ALongValue))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_4,BB_6}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3,BB_4}
	BB_2: BasicBlock(start=10,end=11) -> {BB_1}
	BB_3: BasicBlock(start=6,end=6) -> {BB_9,BB_5}
	BB_4: BasicBlock(start=12,end=12) -> {BB_7}
	BB_5: BasicBlock(start=7,end=7) -> {BB_2,BB_8}
	BB_6: BasicBlock(start=3,end=4) -> {BB_1}
	BB_7: ExitNode(normalReturn=true)
	BB_8: BasicBlock(start=8,end=9) -> {BB_2}
	BB_9: ExitNode(normalReturn=false)
))

java.lang.Class comparableClassFor(java.lang.Object)
AITACode(params=(Parameters(
	1: useSites={0,2} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=int ∈ [0,1],origin=0),InstanceOf(pc=1,UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-1;refId=102]),java.lang.Comparable)),
	1: If(pc=4,UVar(defSites={0},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=29),
	2: Assignment(pc=8,DVar(useSites={4,26,6,25,5},value={java.lang.Class, null}[↦8;refId=105],origin=2),VirtualFunctionCall(pc=8,java.lang.Object,isInterface=false,java.lang.Class getClass(),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-1;refId=102]),())),
	3: Assignment(pc=13,DVar(useSites={4},value=Class<java.lang.String>[↦13;refId=106],origin=3),ClassConst(pc=13,java.lang.String)),
	4: If(pc=15,UVar(defSites={2},value={java.lang.Class, null}[↦8;refId=105]),!=,UVar(defSites={3},value=Class<java.lang.String>[↦13;refId=106]),target=6),
	5: ReturnValue(pc=19,UVar(defSites={2},value={java.lang.Class, null}[↦8;refId=105])),
	6: Assignment(pc=21,DVar(useSites={8,11,7},value={_ <: java.lang.reflect.Type[], null}[↦21;refId=109],origin=6),VirtualFunctionCall(pc=21,java.lang.Class,isInterface=false,java.lang.reflect.Type[] getGenericInterfaces(),UVar(defSites={2},value={java.lang.Class, null}[↦8;refId=105]),())),
	7: If(pc=26,UVar(defSites={6},value={_ <: java.lang.reflect.Type[], null}[↦21;refId=109]),==,NullExpr(pc=-333),target=29),
	8: Assignment(pc=34,DVar(useSites={10},value=int ∈ [0,2147483647],origin=8),ArrayLength(pc=34,UVar(defSites={6},value=_ <: java.lang.reflect.Type[][↦21;refId=109]))),
	9: Assignment(pc=37,DVar(useSites={10,11,27},value=int = 0,origin=9),IntConst(pc=37,0)),
	10: If(pc=44,UVar(defSites={9,27},value=an int),>=,UVar(defSites={8},value=int ∈ [0,2147483647]),target=29),
	11: Assignment(pc=51,DVar(useSites={12,18,14,15},value={_ <: java.lang.reflect.Type, null}[↦51;refId=363],origin=11),ArrayLoad(pc=51,UVar(defSites={9,27},value=int ∈ [-2147483648,2147483646]),UVar(defSites={6},value=_ <: java.lang.reflect.Type[][↦21;refId=109]))),
	12: Assignment(pc=56,DVar(useSites={13},value=int ∈ [0,1],origin=12),InstanceOf(pc=56,UVar(defSites={11},value={_ <: java.lang.reflect.Type, null}[↦51;refId=363]),java.lang.reflect.ParameterizedType)),
	13: If(pc=59,UVar(defSites={12},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=27),
	14: Checkcast(pc=64,UVar(defSites={11},value={_ <: java.lang.reflect.Type, null}[↦51;refId=363]),java.lang.reflect.ParameterizedType),
	15: Assignment(pc=70,DVar(useSites={17},value={_ <: java.lang.reflect.Type, null}[↦70;refId=368],origin=15),VirtualFunctionCall(pc=70,java.lang.reflect.ParameterizedType,isInterface=true,java.lang.reflect.Type getRawType(),UVar(defSites={11},value={_ <: java.lang.reflect.ParameterizedType, null}[↦51;refId=364]),())),
	16: Assignment(pc=75,DVar(useSites={17},value=Class<java.lang.Comparable>[↦75;refId=369],origin=16),ClassConst(pc=75,java.lang.Comparable)),
	17: If(pc=77,UVar(defSites={15},value={_ <: java.lang.reflect.Type, null}[↦70;refId=368]),!=,UVar(defSites={16},value=Class<java.lang.Comparable>[↦75;refId=369]),target=27),
	18: Assignment(pc=82,DVar(useSites={24,20,19},value={_ <: java.lang.reflect.Type[], null}[↦82;refId=371],origin=18),VirtualFunctionCall(pc=82,java.lang.reflect.ParameterizedType,isInterface=true,java.lang.reflect.Type[] getActualTypeArguments(),UVar(defSites={11},value=_ <: java.lang.reflect.ParameterizedType[↦51;refId=364]),())),
	19: If(pc=89,UVar(defSites={18},value={_ <: java.lang.reflect.Type[], null}[↦82;refId=371]),==,NullExpr(pc=-333),target=27),
	20: Assignment(pc=93,DVar(useSites={22},value=int ∈ [0,2147483647],origin=20),ArrayLength(pc=93,UVar(defSites={18},value=_ <: java.lang.reflect.Type[][↦82;refId=371]))),
	21: Assignment(pc=94,DVar(useSites={22},value=int = 1,origin=21),IntConst(pc=94,1)),
	22: If(pc=95,UVar(defSites={20},value=int ∈ [0,2147483647]),!=,UVar(defSites={21},value=int = 1),target=27),
	23: Assignment(pc=99,DVar(useSites={24},value=int = 0,origin=23),IntConst(pc=99,0)),
	24: Assignment(pc=100,DVar(useSites={25},value={_ <: java.lang.reflect.Type, null}[↦100;refId=373],origin=24),ArrayLoad(pc=100,UVar(defSites={23},value=int = 0),UVar(defSites={18},value=_ <: java.lang.reflect.Type[][↦82;refId=371]))),
	25: If(pc=102,UVar(defSites={24},value={_ <: java.lang.reflect.Type, null}[↦100;refId=373]),!=,UVar(defSites={2},value=java.lang.Class[↦8;refId=105]),target=27),
	26: ReturnValue(pc=106,UVar(defSites={2},value=java.lang.Class[↦8;refId=105])),
	27: Assignment(pc=107,DVar(useSites={28,10,11},value=an int,origin=27),BinaryExpr(pc=107,ComputationalTypeInt,UVar(defSites={9,27},value=an int),+,IntConst(pc=107,1))),
	28: Goto(pc=110,target=10),
	29: Assignment(pc=113,DVar(useSites={30},value=null[↦113],origin=29),NullExpr(pc=113)),
	30: ReturnValue(pc=114,UVar(defSites={29},value=null[↦113]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_12,BB_6}
	BB_10: BasicBlock(start=15,end=15) -> {BB_f,BB_b}
	BB_11: BasicBlock(start=20,end=22) -> {BB_16,BB_7}
	BB_12: BasicBlock(start=29,end=30) -> {BB_14}
	BB_13: BasicBlock(start=18,end=18) -> {BB_f,BB_e}
	BB_14: ExitNode(normalReturn=true)
	BB_15: BasicBlock(start=26,end=26) -> {BB_14}
	BB_16: BasicBlock(start=23,end=24) -> {BB_f,BB_3}
	BB_1: BasicBlock(start=5,end=5) -> {BB_14}
	BB_2: BasicBlock(start=10,end=10) -> {BB_12,BB_c}
	BB_3: BasicBlock(start=25,end=25) -> {BB_15,BB_7}
	BB_4: BasicBlock(start=14,end=14) -> {BB_f,BB_10}
	BB_5: BasicBlock(start=6,end=6) -> {BB_f,BB_9}
	BB_6: BasicBlock(start=2,end=2) -> {BB_f,BB_a}
	BB_7: BasicBlock(start=27,end=28) -> {BB_2}
	BB_8: BasicBlock(start=12,end=13) -> {BB_4,BB_7}
	BB_9: BasicBlock(start=7,end=7) -> {BB_12,BB_d}
	BB_a: BasicBlock(start=3,end=4) -> {BB_5,BB_1}
	BB_b: BasicBlock(start=16,end=17) -> {BB_13,BB_7}
	BB_c: BasicBlock(start=11,end=11) -> {BB_f,BB_8}
	BB_d: BasicBlock(start=8,end=9) -> {BB_2}
	BB_e: BasicBlock(start=19,end=19) -> {BB_11,BB_7}
	BB_f: ExitNode(normalReturn=false)
))

boolean containsKey(java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1),
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value={_ <: java.lang.Object, null}[↦2;refId=105],origin=0),VirtualFunctionCall(pc=2,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.lang.Object get(java.lang.Object),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103])))),
	1: If(pc=5,UVar(defSites={0},value={_ <: java.lang.Object, null}[↦2;refId=105]),==,NullExpr(pc=-333),target=4),
	2: Assignment(pc=8,DVar(useSites={5},value=int = 1,origin=2),IntConst(pc=8,1)),
	3: Goto(pc=9,target=5),
	4: Assignment(pc=12,DVar(useSites={5},value=int ∈ [0,1],origin=4),IntConst(pc=12,0)),
	5: ReturnValue(pc=13,UVar(defSites={4,2},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_6,BB_2}
	BB_1: BasicBlock(start=5,end=5) -> {BB_4}
	BB_2: BasicBlock(start=1,end=1) -> {BB_3,BB_5}
	BB_3: BasicBlock(start=2,end=3) -> {BB_1}
	BB_4: ExitNode(normalReturn=true)
	BB_5: BasicBlock(start=4,end=4) -> {BB_1}
	BB_6: ExitNode(normalReturn=false)
))

java.lang.Object remove(java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={2} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=null[↦2],origin=0),NullExpr(pc=2)),
	1: Assignment(pc=3,DVar(useSites={2},value=null[↦3],origin=1),NullExpr(pc=3)),
	2: Assignment(pc=4,DVar(useSites={3},value={_ <: java.lang.Object, null}[↦4;refId=105],origin=2),VirtualFunctionCall(pc=4,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.lang.Object replaceNode(java.lang.Object,java.lang.Object,java.lang.Object),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),UVar(defSites={0},value=null[↦2]),UVar(defSites={1},value=null[↦3])))),
	3: ReturnValue(pc=7,UVar(defSites={2},value={_ <: java.lang.Object, null}[↦4;refId=105]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=3,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void <clinit>()
AITACode(params=(Parameters(
	
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={1},value={_ <: java.lang.Runtime, null}[↦0;refId=103],origin=0),StaticFunctionCall(pc=0,java.lang.Runtime,isInterface=false,java.lang.Runtime getRuntime(),())),
	1: Assignment(pc=3,DVar(useSites={2},value=an int,origin=1),VirtualFunctionCall(pc=3,java.lang.Runtime,isInterface=false,int availableProcessors(),UVar(defSites={0},value={_ <: java.lang.Runtime, null}[↦0;refId=103]),())),
	2: PutStatic(pc=6,java.util.concurrent.ConcurrentHashMap,NCPU,int,UVar(defSites={1},value=an int)),
	3: Assignment(pc=9,DVar(useSites={4},value=int = 3,origin=3),IntConst(pc=9,3)),
	4: Assignment(pc=10,DVar(useSites={16,10,22,23},value=java.io.ObjectStreamField[][↦10;refId=106;length=3],origin=4),NewArray(pc=10,[UVar(defSites={3},value=int = 3)],java.io.ObjectStreamField[])),
	5: Assignment(pc=14,DVar(useSites={10},value=int = 0,origin=5),IntConst(pc=14,0)),
	6: Assignment(pc=15,DVar(useSites={10,9},value=java.io.ObjectStreamField[↦15;refId=107],origin=6),New(pc=15,java.io.ObjectStreamField)),
	7: Assignment(pc=19,DVar(useSites={9},value=String("segments")[@19;refId=108],origin=7),StringConst(pc=19,segments)),
	8: Assignment(pc=21,DVar(useSites={9},value=Class<java.util.concurrent.ConcurrentHashMap$Segment[]>[↦21;refId=109],origin=8),ClassConst(pc=21,java.util.concurrent.ConcurrentHashMap$Segment[])),
	9: NonVirtualMethodCall(pc=24,java.io.ObjectStreamField,isInterface=false,void <init>(java.lang.String,java.lang.Class),UVar(defSites={6},value=java.io.ObjectStreamField[↦15;refId=107]),(UVar(defSites={7},value=String("segments")[@19;refId=108]),UVar(defSites={8},value=Class<java.util.concurrent.ConcurrentHashMap$Segment[]>[↦21;refId=109]))),
	10: ArrayStore(pc=27,UVar(defSites={4},value=java.io.ObjectStreamField[][↦10;refId=106;length=3]),UVar(defSites={5},value=int = 0),UVar(defSites={6},value=java.io.ObjectStreamField[↦15;refId=107])),
	11: Assignment(pc=29,DVar(useSites={16},value=int = 1,origin=11),IntConst(pc=29,1)),
	12: Assignment(pc=30,DVar(useSites={16,15},value=java.io.ObjectStreamField[↦30;refId=111],origin=12),New(pc=30,java.io.ObjectStreamField)),
	13: Assignment(pc=34,DVar(useSites={15},value=String("segmentMask")[@34;refId=112],origin=13),StringConst(pc=34,segmentMask)),
	14: Assignment(pc=36,DVar(useSites={15},value=Class<int>[↦36;refId=113],origin=14),GetStatic(pc=36,java.lang.Integer,TYPE,java.lang.Class)),
	15: NonVirtualMethodCall(pc=39,java.io.ObjectStreamField,isInterface=false,void <init>(java.lang.String,java.lang.Class),UVar(defSites={12},value=java.io.ObjectStreamField[↦30;refId=111]),(UVar(defSites={13},value=String("segmentMask")[@34;refId=112]),UVar(defSites={14},value=Class<int>[↦36;refId=113]))),
	16: ArrayStore(pc=42,UVar(defSites={4},value=java.io.ObjectStreamField[][↦10;refId=106;length=3]),UVar(defSites={11},value=int = 1),UVar(defSites={12},value=java.io.ObjectStreamField[↦30;refId=111])),
	17: Assignment(pc=44,DVar(useSites={22},value=int = 2,origin=17),IntConst(pc=44,2)),
	18: Assignment(pc=45,DVar(useSites={22,21},value=java.io.ObjectStreamField[↦45;refId=115],origin=18),New(pc=45,java.io.ObjectStreamField)),
	19: Assignment(pc=49,DVar(useSites={21},value=String("segmentShift")[@49;refId=116],origin=19),StringConst(pc=49,segmentShift)),
	20: Assignment(pc=51,DVar(useSites={21},value=Class<int>[↦51;refId=117],origin=20),GetStatic(pc=51,java.lang.Integer,TYPE,java.lang.Class)),
	21: NonVirtualMethodCall(pc=54,java.io.ObjectStreamField,isInterface=false,void <init>(java.lang.String,java.lang.Class),UVar(defSites={18},value=java.io.ObjectStreamField[↦45;refId=115]),(UVar(defSites={19},value=String("segmentShift")[@49;refId=116]),UVar(defSites={20},value=Class<int>[↦51;refId=117]))),
	22: ArrayStore(pc=57,UVar(defSites={4},value=java.io.ObjectStreamField[][↦10;refId=106;length=3]),UVar(defSites={17},value=int = 2),UVar(defSites={18},value=java.io.ObjectStreamField[↦45;refId=115])),
	23: PutStatic(pc=58,java.util.concurrent.ConcurrentHashMap,serialPersistentFields,java.io.ObjectStreamField[],UVar(defSites={4},value=java.io.ObjectStreamField[][↦10;refId=106;length=3])),
	24: Assignment(pc=61,DVar(useSites={25},value={jdk.internal.misc.Unsafe, null}[↦61;refId=120],origin=24),StaticFunctionCall(pc=61,jdk.internal.misc.Unsafe,isInterface=false,jdk.internal.misc.Unsafe getUnsafe(),())),
	25: PutStatic(pc=64,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe,UVar(defSites={24},value={jdk.internal.misc.Unsafe, null}[↦61;refId=120])),
	26: Assignment(pc=67,DVar(useSites={29},value={jdk.internal.misc.Unsafe, null}[↦67;refId=121],origin=26),GetStatic(pc=67,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	27: Assignment(pc=70,DVar(useSites={29},value=Class<java.util.concurrent.ConcurrentHashMap>[↦70;refId=122],origin=27),ClassConst(pc=70,java.util.concurrent.ConcurrentHashMap)),
	28: Assignment(pc=72,DVar(useSites={29},value=String("sizeCtl")[@72;refId=123],origin=28),StringConst(pc=72,sizeCtl)),
	29: Assignment(pc=75,DVar(useSites={30},value=ALongValue,origin=29),VirtualFunctionCall(pc=75,jdk.internal.misc.Unsafe,isInterface=false,long objectFieldOffset(java.lang.Class,java.lang.String),UVar(defSites={26},value={jdk.internal.misc.Unsafe, null}[↦67;refId=121]),(UVar(defSites={27},value=Class<java.util.concurrent.ConcurrentHashMap>[↦70;refId=122]),UVar(defSites={28},value=String("sizeCtl")[@72;refId=123])))),
	30: PutStatic(pc=78,java.util.concurrent.ConcurrentHashMap,SIZECTL,long,UVar(defSites={29},value=ALongValue)),
	31: Assignment(pc=81,DVar(useSites={34},value={jdk.internal.misc.Unsafe, null}[↦81;refId=126],origin=31),GetStatic(pc=81,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	32: Assignment(pc=84,DVar(useSites={34},value=Class<java.util.concurrent.ConcurrentHashMap>[↦84;refId=127],origin=32),ClassConst(pc=84,java.util.concurrent.ConcurrentHashMap)),
	33: Assignment(pc=86,DVar(useSites={34},value=String("transferIndex")[@86;refId=128],origin=33),StringConst(pc=86,transferIndex)),
	34: Assignment(pc=89,DVar(useSites={35},value=ALongValue,origin=34),VirtualFunctionCall(pc=89,jdk.internal.misc.Unsafe,isInterface=false,long objectFieldOffset(java.lang.Class,java.lang.String),UVar(defSites={31},value={jdk.internal.misc.Unsafe, null}[↦81;refId=126]),(UVar(defSites={32},value=Class<java.util.concurrent.ConcurrentHashMap>[↦84;refId=127]),UVar(defSites={33},value=String("transferIndex")[@86;refId=128])))),
	35: PutStatic(pc=92,java.util.concurrent.ConcurrentHashMap,TRANSFERINDEX,long,UVar(defSites={34},value=ALongValue)),
	36: Assignment(pc=95,DVar(useSites={39},value={jdk.internal.misc.Unsafe, null}[↦95;refId=131],origin=36),GetStatic(pc=95,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	37: Assignment(pc=98,DVar(useSites={39},value=Class<java.util.concurrent.ConcurrentHashMap>[↦98;refId=132],origin=37),ClassConst(pc=98,java.util.concurrent.ConcurrentHashMap)),
	38: Assignment(pc=100,DVar(useSites={39},value=String("baseCount")[@100;refId=133],origin=38),StringConst(pc=100,baseCount)),
	39: Assignment(pc=103,DVar(useSites={40},value=ALongValue,origin=39),VirtualFunctionCall(pc=103,jdk.internal.misc.Unsafe,isInterface=false,long objectFieldOffset(java.lang.Class,java.lang.String),UVar(defSites={36},value={jdk.internal.misc.Unsafe, null}[↦95;refId=131]),(UVar(defSites={37},value=Class<java.util.concurrent.ConcurrentHashMap>[↦98;refId=132]),UVar(defSites={38},value=String("baseCount")[@100;refId=133])))),
	40: PutStatic(pc=106,java.util.concurrent.ConcurrentHashMap,BASECOUNT,long,UVar(defSites={39},value=ALongValue)),
	41: Assignment(pc=109,DVar(useSites={44},value={jdk.internal.misc.Unsafe, null}[↦109;refId=136],origin=41),GetStatic(pc=109,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	42: Assignment(pc=112,DVar(useSites={44},value=Class<java.util.concurrent.ConcurrentHashMap>[↦112;refId=137],origin=42),ClassConst(pc=112,java.util.concurrent.ConcurrentHashMap)),
	43: Assignment(pc=114,DVar(useSites={44},value=String("cellsBusy")[@114;refId=138],origin=43),StringConst(pc=114,cellsBusy)),
	44: Assignment(pc=117,DVar(useSites={45},value=ALongValue,origin=44),VirtualFunctionCall(pc=117,jdk.internal.misc.Unsafe,isInterface=false,long objectFieldOffset(java.lang.Class,java.lang.String),UVar(defSites={41},value={jdk.internal.misc.Unsafe, null}[↦109;refId=136]),(UVar(defSites={42},value=Class<java.util.concurrent.ConcurrentHashMap>[↦112;refId=137]),UVar(defSites={43},value=String("cellsBusy")[@114;refId=138])))),
	45: PutStatic(pc=120,java.util.concurrent.ConcurrentHashMap,CELLSBUSY,long,UVar(defSites={44},value=ALongValue)),
	46: Assignment(pc=123,DVar(useSites={49},value={jdk.internal.misc.Unsafe, null}[↦123;refId=141],origin=46),GetStatic(pc=123,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	47: Assignment(pc=126,DVar(useSites={49},value=Class<java.util.concurrent.ConcurrentHashMap$CounterCell>[↦126;refId=142],origin=47),ClassConst(pc=126,java.util.concurrent.ConcurrentHashMap$CounterCell)),
	48: Assignment(pc=128,DVar(useSites={49},value=String("value")[@128;refId=143],origin=48),StringConst(pc=128,value)),
	49: Assignment(pc=131,DVar(useSites={50},value=ALongValue,origin=49),VirtualFunctionCall(pc=131,jdk.internal.misc.Unsafe,isInterface=false,long objectFieldOffset(java.lang.Class,java.lang.String),UVar(defSites={46},value={jdk.internal.misc.Unsafe, null}[↦123;refId=141]),(UVar(defSites={47},value=Class<java.util.concurrent.ConcurrentHashMap$CounterCell>[↦126;refId=142]),UVar(defSites={48},value=String("value")[@128;refId=143])))),
	50: PutStatic(pc=134,java.util.concurrent.ConcurrentHashMap,CELLVALUE,long,UVar(defSites={49},value=ALongValue)),
	51: Assignment(pc=137,DVar(useSites={53},value={jdk.internal.misc.Unsafe, null}[↦137;refId=146],origin=51),GetStatic(pc=137,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	52: Assignment(pc=140,DVar(useSites={53},value=Class<java.util.concurrent.ConcurrentHashMap$Node[]>[↦140;refId=147],origin=52),ClassConst(pc=140,java.util.concurrent.ConcurrentHashMap$Node[])),
	53: Assignment(pc=143,DVar(useSites={54},value=an int,origin=53),VirtualFunctionCall(pc=143,jdk.internal.misc.Unsafe,isInterface=false,int arrayBaseOffset(java.lang.Class),UVar(defSites={51},value={jdk.internal.misc.Unsafe, null}[↦137;refId=146]),(UVar(defSites={52},value=Class<java.util.concurrent.ConcurrentHashMap$Node[]>[↦140;refId=147])))),
	54: PutStatic(pc=146,java.util.concurrent.ConcurrentHashMap,ABASE,int,UVar(defSites={53},value=an int)),
	55: Assignment(pc=149,DVar(useSites={57},value={jdk.internal.misc.Unsafe, null}[↦149;refId=150],origin=55),GetStatic(pc=149,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	56: Assignment(pc=152,DVar(useSites={57},value=Class<java.util.concurrent.ConcurrentHashMap$Node[]>[↦152;refId=151],origin=56),ClassConst(pc=152,java.util.concurrent.ConcurrentHashMap$Node[])),
	57: Assignment(pc=155,DVar(useSites={60,67,59},value=an int,origin=57),VirtualFunctionCall(pc=155,jdk.internal.misc.Unsafe,isInterface=false,int arrayIndexScale(java.lang.Class),UVar(defSites={55},value={jdk.internal.misc.Unsafe, null}[↦149;refId=150]),(UVar(defSites={56},value=Class<java.util.concurrent.ConcurrentHashMap$Node[]>[↦152;refId=151])))),
	58: Assignment(pc=161,DVar(useSites={59},value=int = 1,origin=58),IntConst(pc=161,1)),
	59: Assignment(pc=162,DVar(useSites={60},value=an int,origin=59),BinaryExpr(pc=162,ComputationalTypeInt,UVar(defSites={57},value=an int),-,UVar(defSites={58},value=int = 1))),
	60: Assignment(pc=163,DVar(useSites={61},value=an int,origin=60),BinaryExpr(pc=163,ComputationalTypeInt,UVar(defSites={57},value=an int),&,UVar(defSites={59},value=an int))),
	61: If(pc=164,UVar(defSites={60},value=an int),==,IntConst(pc=-333,0),target=66),
	62: Assignment(pc=167,DVar(useSites={64,65},value=java.lang.ExceptionInInitializerError[↦167;refId=154],origin=62),New(pc=167,java.lang.ExceptionInInitializerError)),
	63: Assignment(pc=171,DVar(useSites={64},value=String("array index scale not a power of two")[@171;refId=155],origin=63),StringConst(pc=171,array index scale not a power of two)),
	64: NonVirtualMethodCall(pc=174,java.lang.ExceptionInInitializerError,isInterface=false,void <init>(java.lang.String),UVar(defSites={62},value=java.lang.ExceptionInInitializerError[↦167;refId=154]),(UVar(defSites={63},value=String("array index scale not a power of two")[@171;refId=155]))),
	65: Throw(pc=177,UVar(defSites={62},value=java.lang.ExceptionInInitializerError[↦167;refId=154])),
	66: Assignment(pc=178,DVar(useSites={68},value=int = 31,origin=66),IntConst(pc=178,31)),
	67: Assignment(pc=181,DVar(useSites={68},value=an int,origin=67),StaticFunctionCall(pc=181,java.lang.Integer,isInterface=false,int numberOfLeadingZeros(int),(UVar(defSites={57},value=an int)))),
	68: Assignment(pc=184,DVar(useSites={69},value=an int,origin=68),BinaryExpr(pc=184,ComputationalTypeInt,UVar(defSites={66},value=int = 31),-,UVar(defSites={67},value=an int))),
	69: PutStatic(pc=185,java.util.concurrent.ConcurrentHashMap,ASHIFT,int,UVar(defSites={68},value=an int)),
	70: Return(pc=195)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_f,BB_3}
	BB_10: BasicBlock(start=50,end=53) -> {BB_f,BB_8}
	BB_11: BasicBlock(start=16,end=21) -> {BB_f,BB_7}
	BB_12: BasicBlock(start=68,end=70) -> {BB_b}
	BB_13: BasicBlock(start=62,end=64) -> {BB_f,BB_4}
	BB_1: BasicBlock(start=10,end=15) -> {BB_f,BB_11}
	BB_2: BasicBlock(start=25,end=29) -> {BB_f,BB_e}
	BB_3: BasicBlock(start=1,end=1) -> {BB_f,BB_5}
	BB_4: BasicBlock(start=65,end=65) -> {BB_f}
	BB_5: BasicBlock(start=2,end=9) -> {BB_f,BB_1}
	BB_6: BasicBlock(start=45,end=49) -> {BB_f,BB_10}
	BB_7: BasicBlock(start=22,end=24) -> {BB_f,BB_2}
	BB_8: BasicBlock(start=54,end=57) -> {BB_f,BB_d}
	BB_9: BasicBlock(start=66,end=67) -> {BB_f,BB_12}
	BB_a: BasicBlock(start=35,end=39) -> {BB_f,BB_c}
	BB_b: ExitNode(normalReturn=true)
	BB_c: BasicBlock(start=40,end=44) -> {BB_f,BB_6}
	BB_d: BasicBlock(start=58,end=61) -> {BB_9,BB_13}
	BB_e: BasicBlock(start=30,end=34) -> {BB_f,BB_a}
	BB_f: ExitNode(normalReturn=false)
))

void addCount(long,int)
AITACode(params=(Parameters(
	0: useSites={0,32,72,24,4,68,36,52,60,50,58,6,29,71} (origin=-1),
	1: useSites={24,5,21} (origin=-2),
	2: useSites={27,31} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={16,10,1,9},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦1;refId=103],origin=0),GetField(pc=1,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	1: If(pc=7,UVar(defSites={0},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦1;refId=103]),!=,NullExpr(pc=-333),target=8),
	2: Assignment(pc=10,DVar(useSites={6},value={jdk.internal.misc.Unsafe, null}[↦10;refId=104],origin=2),GetStatic(pc=10,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	3: Assignment(pc=14,DVar(useSites={6},value=ALongValue,origin=3),GetStatic(pc=14,java.util.concurrent.ConcurrentHashMap,BASECOUNT,long)),
	4: Assignment(pc=18,DVar(useSites={6,5},value=ALongValue,origin=4),GetField(pc=18,java.util.concurrent.ConcurrentHashMap,baseCount,long,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	5: Assignment(pc=27,DVar(useSites={34,6},value=ALongValue,origin=5),BinaryExpr(pc=27,ComputationalTypeLong,UVar(defSites={4},value=ALongValue),+,UVar(defSites={-2},value=ALongValue))),
	6: Assignment(pc=31,DVar(useSites={7},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=31,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetLong(java.lang.Object,long,long,long),UVar(defSites={2},value={jdk.internal.misc.Unsafe, null}[↦10;refId=104]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={3},value=ALongValue),UVar(defSites={4},value=ALongValue),UVar(defSites={5},value=ALongValue)))),
	7: If(pc=34,UVar(defSites={6},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=31),
	8: Assignment(pc=37,DVar(useSites={24},value=int = 1,origin=8),IntConst(pc=37,1)),
	9: If(pc=42,UVar(defSites={0},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦1;refId=103]),==,NullExpr(pc=-333),target=24),
	10: Assignment(pc=47,DVar(useSites={12},value=int ∈ [0,2147483647],origin=10),ArrayLength(pc=47,UVar(defSites={0},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦1;refId=103]))),
	11: Assignment(pc=48,DVar(useSites={12},value=int = 1,origin=11),IntConst(pc=48,1)),
	12: Assignment(pc=49,DVar(useSites={13,15},value=int ∈ [-1,2147483646],origin=12),BinaryExpr(pc=49,ComputationalTypeInt,UVar(defSites={10},value=int ∈ [0,2147483647]),-,UVar(defSites={11},value=int = 1))),
	13: If(pc=53,UVar(defSites={12},value=int ∈ [-1,2147483646]),<,IntConst(pc=-333,0),target=24),
	14: Assignment(pc=58,DVar(useSites={15},value=an int,origin=14),StaticFunctionCall(pc=58,java.util.concurrent.ThreadLocalRandom,isInterface=false,int getProbe(),())),
	15: Assignment(pc=63,DVar(useSites={16},value=int ∈ [0,2147483646],origin=15),BinaryExpr(pc=63,ComputationalTypeInt,UVar(defSites={14},value=an int),&,UVar(defSites={12},value=int ∈ [0,2147483646]))),
	16: Assignment(pc=64,DVar(useSites={20,22,17},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦64;refId=109],origin=16),ArrayLoad(pc=64,UVar(defSites={15},value=int ∈ [0,2147483646]),UVar(defSites={0},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦1;refId=103]))),
	17: If(pc=68,UVar(defSites={16},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦64;refId=109]),==,NullExpr(pc=-333),target=24),
	18: Assignment(pc=71,DVar(useSites={22},value={jdk.internal.misc.Unsafe, null}[↦71;refId=110],origin=18),GetStatic(pc=71,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	19: Assignment(pc=76,DVar(useSites={22},value=ALongValue,origin=19),GetStatic(pc=76,java.util.concurrent.ConcurrentHashMap,CELLVALUE,long)),
	20: Assignment(pc=81,DVar(useSites={22,21},value=ALongValue,origin=20),GetField(pc=81,java.util.concurrent.ConcurrentHashMap$CounterCell,value,long,UVar(defSites={16},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦64;refId=109]))),
	21: Assignment(pc=90,DVar(useSites={22},value=ALongValue,origin=21),BinaryExpr(pc=90,ComputationalTypeLong,UVar(defSites={20},value=ALongValue),+,UVar(defSites={-2},value=ALongValue))),
	22: Assignment(pc=91,DVar(useSites={24,23},value=int ∈ [0,1],origin=22),VirtualFunctionCall(pc=91,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetLong(java.lang.Object,long,long,long),UVar(defSites={18},value={jdk.internal.misc.Unsafe, null}[↦71;refId=110]),(UVar(defSites={16},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦64;refId=109]),UVar(defSites={19},value=ALongValue),UVar(defSites={20},value=ALongValue),UVar(defSites={21},value=ALongValue)))),
	23: If(pc=97,UVar(defSites={22},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=26),
	24: VirtualMethodCall(pc=104,java.util.concurrent.ConcurrentHashMap,isInterface=false,void fullAddCount(long,boolean),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={-2},value=ALongValue),UVar(defSites={8,22},value=int ∈ [0,1]))),
	25: Return(pc=107),
	26: Assignment(pc=109,DVar(useSites={27},value=int = 1,origin=26),IntConst(pc=109,1)),
	27: If(pc=110,UVar(defSites={-3},value=an int),>,UVar(defSites={26},value=int = 1),target=29),
	28: Return(pc=113),
	29: Assignment(pc=115,DVar(useSites={34},value=ALongValue,origin=29),VirtualFunctionCall(pc=115,java.util.concurrent.ConcurrentHashMap,isInterface=false,long sumCount(),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),())),
	30: Nop(pc=118),
	31: If(pc=121,UVar(defSites={-3},value=an int),<,IntConst(pc=-333,0),target=74),
	32: Assignment(pc=127,DVar(useSites={68,44,42,58,33,57},value=an int,origin=32),GetField(pc=127,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	33: Assignment(pc=133,DVar(useSites={34},value=ALongValue,origin=33),PrimitiveTypecastExpr(pc=133,LongType,UVar(defSites={32},value=an int))),
	34: Assignment(pc=134,DVar(useSites={35},value=an int,origin=34),Compare(pc=134,UVar(defSites={72,5,29},value=ALongValue),cmp,UVar(defSites={33},value=ALongValue))),
	35: If(pc=135,UVar(defSites={34},value=an int),<,IntConst(pc=-333,0),target=74),
	36: Assignment(pc=139,DVar(useSites={60,38,37,71},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦139;refId=115],origin=36),GetField(pc=139,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	37: If(pc=145,UVar(defSites={36},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦139;refId=115]),==,NullExpr(pc=-333),target=74),
	38: Assignment(pc=150,DVar(useSites={40,41},value=int ∈ [0,2147483647],origin=38),ArrayLength(pc=150,UVar(defSites={36},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦139;refId=115]))),
	39: Assignment(pc=154,DVar(useSites={40},value=int = 1073741824,origin=39),IntConst(pc=154,1073741824)),
	40: If(pc=156,UVar(defSites={38},value=int ∈ [0,2147483647]),>=,UVar(defSites={39},value=int = 1073741824),target=74),
	41: Assignment(pc=161,DVar(useSites={65,45},value=an int,origin=41),StaticFunctionCall(pc=161,java.util.concurrent.ConcurrentHashMap,isInterface=false,int resizeStamp(int),(UVar(defSites={38},value=int ∈ [0,1073741823])))),
	42: If(pc=168,UVar(defSites={32},value=an int),>=,IntConst(pc=-333,0),target=62),
	43: Assignment(pc=173,DVar(useSites={44},value=int = 16,origin=43),IntConst(pc=173,16)),
	44: Assignment(pc=175,DVar(useSites={45},value=int = 65535,origin=44),BinaryExpr(pc=175,ComputationalTypeInt,UVar(defSites={32},value=int ∈ [-2147483648,-1]),>>>,UVar(defSites={43},value=int = 16))),
	45: If(pc=178,UVar(defSites={44},value=int = 65535),!=,UVar(defSites={41},value=an int),target=74),
	46: Nop(pc=185),
	47: Nop(pc=186),
	48: Nop(pc=194),
	49: Nop(pc=196),
	50: Assignment(pc=201,DVar(useSites={60,51},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦201;refId=117],origin=50),GetField(pc=201,java.util.concurrent.ConcurrentHashMap,nextTable,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	51: If(pc=207,UVar(defSites={50},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦201;refId=117]),==,NullExpr(pc=-333),target=74),
	52: Assignment(pc=211,DVar(useSites={53},value=an int,origin=52),GetField(pc=211,java.util.concurrent.ConcurrentHashMap,transferIndex,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	53: If(pc=214,UVar(defSites={52},value=an int),<=,IntConst(pc=-333,0),target=74),
	54: Assignment(pc=220,DVar(useSites={58},value={jdk.internal.misc.Unsafe, null}[↦220;refId=118],origin=54),GetStatic(pc=220,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	55: Assignment(pc=224,DVar(useSites={58},value=ALongValue,origin=55),GetStatic(pc=224,java.util.concurrent.ConcurrentHashMap,SIZECTL,long)),
	56: Assignment(pc=231,DVar(useSites={57},value=int = 1,origin=56),IntConst(pc=231,1)),
	57: Assignment(pc=232,DVar(useSites={58},value=int ∈ [-2147483647,0],origin=57),BinaryExpr(pc=232,ComputationalTypeInt,UVar(defSites={32},value=int ∈ [-2147483648,-1]),+,UVar(defSites={56},value=int = 1))),
	58: Assignment(pc=233,DVar(useSites={59},value=int ∈ [0,1],origin=58),VirtualFunctionCall(pc=233,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={54},value={jdk.internal.misc.Unsafe, null}[↦220;refId=118]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={55},value=ALongValue),UVar(defSites={32},value=int ∈ [-2147483648,-1]),UVar(defSites={57},value=int ∈ [-2147483647,0])))),
	59: If(pc=236,UVar(defSites={58},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=72),
	60: VirtualMethodCall(pc=244,java.util.concurrent.ConcurrentHashMap,isInterface=false,void transfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node[]),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={36},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦139;refId=115]),UVar(defSites={50},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦201;refId=117]))),
	61: Goto(pc=247,target=72),
	62: Assignment(pc=250,DVar(useSites={68},value={jdk.internal.misc.Unsafe, null}[↦250;refId=122],origin=62),GetStatic(pc=250,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	63: Assignment(pc=254,DVar(useSites={68},value=ALongValue,origin=63),GetStatic(pc=254,java.util.concurrent.ConcurrentHashMap,SIZECTL,long)),
	64: Assignment(pc=261,DVar(useSites={65},value=int = 16,origin=64),IntConst(pc=261,16)),
	65: Assignment(pc=263,DVar(useSites={67},value=an int,origin=65),BinaryExpr(pc=263,ComputationalTypeInt,UVar(defSites={41},value=an int),<<,UVar(defSites={64},value=int = 16))),
	66: Assignment(pc=264,DVar(useSites={67},value=int = 2,origin=66),IntConst(pc=264,2)),
	67: Assignment(pc=265,DVar(useSites={68},value=an int,origin=67),BinaryExpr(pc=265,ComputationalTypeInt,UVar(defSites={65},value=an int),+,UVar(defSites={66},value=int = 2))),
	68: Assignment(pc=266,DVar(useSites={69},value=int ∈ [0,1],origin=68),VirtualFunctionCall(pc=266,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={62},value={jdk.internal.misc.Unsafe, null}[↦250;refId=122]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={63},value=ALongValue),UVar(defSites={32},value=int ∈ [0,2147483647]),UVar(defSites={67},value=an int)))),
	69: If(pc=269,UVar(defSites={68},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=72),
	70: Assignment(pc=275,DVar(useSites={71},value=null[↦275],origin=70),NullExpr(pc=275)),
	71: VirtualMethodCall(pc=276,java.util.concurrent.ConcurrentHashMap,isInterface=false,void transfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node[]),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={36},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦139;refId=115]),UVar(defSites={70},value=null[↦275]))),
	72: Assignment(pc=280,DVar(useSites={34},value=ALongValue,origin=72),VirtualFunctionCall(pc=280,java.util.concurrent.ConcurrentHashMap,isInterface=false,long sumCount(),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),())),
	73: Goto(pc=285,target=32),
	74: Return(pc=288)
),cfg=CFG(
	BB_0: BasicBlock(start=10,end=13) -> {BB_f,BB_c}
	BB_10: BasicBlock(start=46,end=51) -> {BB_13,BB_e}
	BB_11: BasicBlock(start=29,end=29) -> {BB_8,BB_22}
	BB_12: BasicBlock(start=61,end=61) -> {BB_1d}
	BB_13: BasicBlock(start=74,end=74) -> {BB_1c}
	BB_14: BasicBlock(start=70,end=71) -> {BB_8,BB_1d}
	BB_15: BasicBlock(start=28,end=28) -> {BB_1c}
	BB_16: BasicBlock(start=38,end=40) -> {BB_13,BB_2}
	BB_17: BasicBlock(start=73,end=73) -> {BB_19}
	BB_18: BasicBlock(start=2,end=6) -> {BB_8,BB_5}
	BB_19: BasicBlock(start=32,end=35) -> {BB_13,BB_21}
	BB_1: BasicBlock(start=60,end=60) -> {BB_8,BB_12}
	BB_1a: BasicBlock(start=17,end=17) -> {BB_c,BB_1b}
	BB_1b: BasicBlock(start=18,end=22) -> {BB_8,BB_20}
	BB_1c: ExitNode(normalReturn=true)
	BB_1d: BasicBlock(start=72,end=72) -> {BB_8,BB_17}
	BB_1e: BasicBlock(start=43,end=45) -> {BB_13,BB_10}
	BB_1f: BasicBlock(start=26,end=27) -> {BB_11,BB_15}
	BB_20: BasicBlock(start=23,end=23) -> {BB_c,BB_1f}
	BB_21: BasicBlock(start=36,end=37) -> {BB_13,BB_16}
	BB_22: BasicBlock(start=30,end=30) -> {BB_6}
	BB_23: BasicBlock(start=15,end=16) -> {BB_8,BB_1a}
	BB_24: BasicBlock(start=62,end=68) -> {BB_8,BB_9}
	BB_2: BasicBlock(start=41,end=41) -> {BB_8,BB_b}
	BB_3: BasicBlock(start=59,end=59) -> {BB_1d,BB_1}
	BB_4: BasicBlock(start=54,end=58) -> {BB_8,BB_3}
	BB_5: BasicBlock(start=7,end=7) -> {BB_6,BB_7}
	BB_6: BasicBlock(start=31,end=31) -> {BB_13,BB_19}
	BB_7: BasicBlock(start=8,end=9) -> {BB_c,BB_0}
	BB_8: ExitNode(normalReturn=false)
	BB_9: BasicBlock(start=69,end=69) -> {BB_14,BB_1d}
	BB_a: BasicBlock(start=0,end=1) -> {BB_18,BB_7}
	BB_b: BasicBlock(start=42,end=42) -> {BB_24,BB_1e}
	BB_c: BasicBlock(start=24,end=24) -> {BB_8,BB_d}
	BB_d: BasicBlock(start=25,end=25) -> {BB_1c}
	BB_e: BasicBlock(start=52,end=53) -> {BB_13,BB_4}
	BB_f: BasicBlock(start=14,end=14) -> {BB_8,BB_23}
))

java.lang.Object replaceNode(java.lang.Object,java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={2,90,14} (origin=-1),
	1: useSites={0,57,29,27} (origin=-2),
	2: useSites={66,38,65,37,87} (origin=-3),
	3: useSites={32,60,33,61,35,63} (origin=-4)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),VirtualFunctionCall(pc=1,java.lang.Object,isInterface=false,int hashCode(),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),())),
	1: Assignment(pc=4,DVar(useSites={8,25,57},value=an int,origin=1),StaticFunctionCall(pc=4,java.util.concurrent.ConcurrentHashMap,isInterface=false,int spread(int),(UVar(defSites={0},value=an int)))),
	2: Assignment(pc=10,DVar(useSites={72,4,14,9,45,3,19},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109],origin=2),GetField(pc=10,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	3: If(pc=17,UVar(defSites={2,14},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[refId=131; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=130]»]),==,NullExpr(pc=-333),target=92),
	4: Assignment(pc=22,DVar(useSites={5,7},value=int ∈ [0,2147483647],origin=4),ArrayLength(pc=22,UVar(defSites={2,14},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=131; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=130]»]))),
	5: If(pc=26,UVar(defSites={4},value=int ∈ [0,2147483647]),==,IntConst(pc=-333,0),target=92),
	6: Assignment(pc=33,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=33,1)),
	7: Assignment(pc=34,DVar(useSites={8},value=int ∈ [0,2147483646],origin=7),BinaryExpr(pc=34,ComputationalTypeInt,UVar(defSites={4},value=int ∈ [1,2147483647]),-,UVar(defSites={6},value=int = 1))),
	8: Assignment(pc=37,DVar(useSites={72,9,45,19},value=int ∈ [0,2147483646],origin=8),BinaryExpr(pc=37,ComputationalTypeInt,UVar(defSites={7},value=int ∈ [0,2147483646]),&,UVar(defSites={1},value=an int))),
	9: Assignment(pc=41,DVar(useSites={80,40,24,68,20,44,18,50,10,74,42,26,70,38,54,14,41,53,83,11,47,31},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦41;refId=152],origin=9),StaticFunctionCall(pc=41,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={2,14},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=131; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=130]»]),UVar(defSites={8},value=int ∈ [0,2147483646])))),
	10: If(pc=47,UVar(defSites={9},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦41;refId=152]),==,NullExpr(pc=-333),target=92),
	11: Assignment(pc=55,DVar(useSites={21,13},value=an int,origin=11),GetField(pc=55,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152]))),
	12: Assignment(pc=61,DVar(useSites={13},value=int = -1,origin=12),IntConst(pc=61,-1)),
	13: If(pc=62,UVar(defSites={11},value=an int),!=,UVar(defSites={12},value=int = -1),target=16),
	14: Assignment(pc=70,DVar(useSites={72,4,9,45,3,19,15},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=172],origin=14),VirtualFunctionCall(pc=70,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node[] helpTransfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={2,14},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=131; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=130]»]),UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152])))),
	15: Goto(pc=75,target=3),
	16: Assignment(pc=78,DVar(useSites={86,91},value=null[↦78],origin=16),NullExpr(pc=78)),
	17: Assignment(pc=81,DVar(useSites={85},value=int = 0,origin=17),IntConst(pc=81,0)),
	18: MonitorEnter(pc=89,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152])),
	19: Assignment(pc=94,DVar(useSites={20},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦94;refId=154],origin=19),StaticFunctionCall(pc=94,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={2,14},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=131; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=130]»]),UVar(defSites={8},value=int ∈ [0,2147483646])))),
	20: If(pc=99,UVar(defSites={19},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦94;refId=154]),!=,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152]),target=80),
	21: If(pc=104,UVar(defSites={11},value=an int),<,IntConst(pc=-333,0),target=50),
	22: Assignment(pc=107,DVar(useSites={85},value=int = 1,origin=22),IntConst(pc=107,1)),
	23: Assignment(pc=114,DVar(useSites={40,42},value=null[↦114],origin=23),NullExpr(pc=114)),
	24: Assignment(pc=119,DVar(useSites={25},value=an int,origin=24),GetField(pc=119,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={9,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=212; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=210]»]))),
	25: If(pc=124,UVar(defSites={24},value=an int),!=,UVar(defSites={1},value=an int),target=47),
	26: Assignment(pc=129,DVar(useSites={28,29,27},value={_ <: java.lang.Object, null}[↦129;refId=227],origin=26),GetField(pc=129,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={9,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=212; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=210]»]))),
	27: If(pc=136,UVar(defSites={26},value={_ <: java.lang.Object, null}[↦129;refId=227]),==,UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),target=31),
	28: If(pc=141,UVar(defSites={26},value={_ <: java.lang.Object, null}[↦129;refId=227]),==,NullExpr(pc=-333),target=47),
	29: Assignment(pc=147,DVar(useSites={30},value=int ∈ [0,1],origin=29),VirtualFunctionCall(pc=147,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),(UVar(defSites={26},value=_ <: java.lang.Object[↦129;refId=227])))),
	30: If(pc=150,UVar(defSites={29},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=47),
	31: Assignment(pc=155,DVar(useSites={34,86,33,35,91},value={_ <: java.lang.Object, null}[↦155;refId=242],origin=31),GetField(pc=155,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={9,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=229; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=210]»]))),
	32: If(pc=161,UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=105]),==,NullExpr(pc=-333),target=37),
	33: If(pc=167,UVar(defSites={-4},value=_ <: java.lang.Object[↦-4;refId=105]),==,UVar(defSites={31},value={_ <: java.lang.Object, null}[↦155;refId=242]),target=37),
	34: If(pc=172,UVar(defSites={31},value={_ <: java.lang.Object, null}[↦155;refId=242]),==,NullExpr(pc=-333),target=80),
	35: Assignment(pc=178,DVar(useSites={36},value=int ∈ [0,1],origin=35),VirtualFunctionCall(pc=178,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-4},value=_ <: java.lang.Object[↦-4;refId=105]),(UVar(defSites={31},value=_ <: java.lang.Object[↦155;refId=242])))),
	36: If(pc=181,UVar(defSites={35},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=80),
	37: If(pc=189,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=104]),==,NullExpr(pc=-333),target=40),
	38: PutField(pc=195,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={9,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=244; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=210]»]),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=104])),
	39: Goto(pc=198,target=80),
	40: If(pc=203,UVar(defSites={9,23,47},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=243; values=«null[↦114], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=176]»]),==,NullExpr(pc=-333),target=44),
	41: Assignment(pc=210,DVar(useSites={42},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦210;refId=253],origin=41),GetField(pc=210,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={9,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=244; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=210]»]))),
	42: PutField(pc=213,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={9,23,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=252; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=176]»]),UVar(defSites={41},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦210;refId=253])),
	43: Goto(pc=216,target=80),
	44: Assignment(pc=225,DVar(useSites={45},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦225;refId=254],origin=44),GetField(pc=225,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={9,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=244; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=210]»]))),
	45: StaticMethodCall(pc=228,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={2,14},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=131; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=130]»]),UVar(defSites={8},value=int ∈ [0,2147483646]),UVar(defSites={44},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦225;refId=254]))),
	46: Goto(pc=231,target=80),
	47: Assignment(pc=240,DVar(useSites={48,40,24,44,42,26,38,41,31},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦240;refId=210],origin=47),GetField(pc=240,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={9,47},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=186; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦240;refId=176]»]))),
	48: If(pc=246,UVar(defSites={47},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦240;refId=210]),!=,NullExpr(pc=-333),target=24),
	49: Goto(pc=252,target=80),
	50: Assignment(pc=257,DVar(useSites={51},value=int ∈ [0,1],origin=50),InstanceOf(pc=257,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152]),java.util.concurrent.ConcurrentHashMap$TreeBin)),
	51: If(pc=260,UVar(defSites={50},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=74),
	52: Assignment(pc=263,DVar(useSites={85},value=int = 1,origin=52),IntConst(pc=263,1)),
	53: Checkcast(pc=268,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152]),java.util.concurrent.ConcurrentHashMap$TreeBin),
	54: Assignment(pc=275,DVar(useSites={57,55},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦275;refId=159],origin=54),GetField(pc=275,java.util.concurrent.ConcurrentHashMap$TreeBin,root,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={9},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦41;refId=156]))),
	55: If(pc=281,UVar(defSites={54},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦275;refId=159]),==,NullExpr(pc=-333),target=80),
	56: Assignment(pc=289,DVar(useSites={57},value=null[↦289],origin=56),NullExpr(pc=289)),
	57: Assignment(pc=290,DVar(useSites={68,66,58,59},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦290;refId=161],origin=57),VirtualFunctionCall(pc=290,java.util.concurrent.ConcurrentHashMap$TreeNode,isInterface=false,java.util.concurrent.ConcurrentHashMap$TreeNode findTreeNode(int,java.lang.Object,java.lang.Class),UVar(defSites={54},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦275;refId=159]),(UVar(defSites={1},value=an int),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),UVar(defSites={56},value=null[↦289])))),
	58: If(pc=296,UVar(defSites={57},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦290;refId=161]),==,NullExpr(pc=-333),target=80),
	59: Assignment(pc=301,DVar(useSites={86,62,61,91,63},value={_ <: java.lang.Object, null}[↦301;refId=163],origin=59),GetField(pc=301,java.util.concurrent.ConcurrentHashMap$TreeNode,val,java.lang.Object,UVar(defSites={57},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦290;refId=161]))),
	60: If(pc=307,UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-4;refId=105]),==,NullExpr(pc=-333),target=65),
	61: If(pc=313,UVar(defSites={-4},value=_ <: java.lang.Object[↦-4;refId=105]),==,UVar(defSites={59},value={_ <: java.lang.Object, null}[↦301;refId=163]),target=65),
	62: If(pc=318,UVar(defSites={59},value={_ <: java.lang.Object, null}[↦301;refId=163]),==,NullExpr(pc=-333),target=80),
	63: Assignment(pc=324,DVar(useSites={64},value=int ∈ [0,1],origin=63),VirtualFunctionCall(pc=324,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-4},value=_ <: java.lang.Object[↦-4;refId=105]),(UVar(defSites={59},value=_ <: java.lang.Object[↦301;refId=163])))),
	64: If(pc=327,UVar(defSites={63},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=80),
	65: If(pc=335,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=104]),==,NullExpr(pc=-333),target=68),
	66: PutField(pc=341,java.util.concurrent.ConcurrentHashMap$TreeNode,val,java.lang.Object,UVar(defSites={57},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦290;refId=161]),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=104])),
	67: Goto(pc=344,target=80),
	68: Assignment(pc=351,DVar(useSites={69},value=int ∈ [0,1],origin=68),VirtualFunctionCall(pc=351,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,boolean removeTreeNode(java.util.concurrent.ConcurrentHashMap$TreeNode),UVar(defSites={9},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦41;refId=156]),(UVar(defSites={57},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦290;refId=161])))),
	69: If(pc=354,UVar(defSites={68},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=80),
	70: Assignment(pc=363,DVar(useSites={71},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦363;refId=197],origin=70),GetField(pc=363,java.util.concurrent.ConcurrentHashMap$TreeBin,first,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={9},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦41;refId=156]))),
	71: Assignment(pc=366,DVar(useSites={72},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦366;refId=199],origin=71),StaticFunctionCall(pc=366,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node untreeify(java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={70},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦363;refId=197])))),
	72: StaticMethodCall(pc=369,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={2,14},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=131; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=109], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦70;refId=130]»]),UVar(defSites={8},value=int ∈ [0,2147483646]),UVar(defSites={71},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦366;refId=199]))),
	73: Goto(pc=372,target=80),
	74: Assignment(pc=377,DVar(useSites={75},value=int ∈ [0,1],origin=74),InstanceOf(pc=377,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=152]),java.util.concurrent.ConcurrentHashMap$ReservationNode)),
	75: If(pc=380,UVar(defSites={74},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=80),
	76: Assignment(pc=383,DVar(useSites={84,78,79},value=java.lang.IllegalStateException[↦383;refId=166],origin=76),New(pc=383,java.lang.IllegalStateException)),
	77: Assignment(pc=387,DVar(useSites={78},value=String("Recursive update")[@387;refId=167],origin=77),StringConst(pc=387,Recursive update)),
	78: NonVirtualMethodCall(pc=389,java.lang.IllegalStateException,isInterface=false,void <init>(java.lang.String),UVar(defSites={76},value=java.lang.IllegalStateException[↦383;refId=166]),(UVar(defSites={77},value=String("Recursive update")[@387;refId=167]))),
	79: Throw(pc=392,UVar(defSites={76},value=java.lang.IllegalStateException[↦383;refId=166])),
	80: MonitorExit(pc=395,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=111])),
	81: Goto(pc=396,target=85),
	82: CaughtException(pc=399,<ANY>,caused by={exception[VM]@80,exception@72,lv4c,exception@68,exception@78,exception@63,exception@71,exception[VM]@83,exception@19,exception@35,exception@29,exception@45,exception[VM]@53,exception@57}),
	83: MonitorExit(pc=403,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦41;refId=111])),
	84: Throw(pc=406,UVar(defSites={-100080,-1000072,76,-1000068,-1000078,-1000063,-1000071,-100083,-1000019,-1000035,-1000029,-1000045,-100053,-1000057},value=_ <: java.lang.Throwable[refId=206; values=«_ <: java.lang.Throwable[↦-1000094;refId=153], java.lang.ClassCastException[↦-100268;refId=157], _ <: java.lang.Throwable[↦-1000324;refId=164], _ <: java.lang.Throwable[↦-1000228;refId=205], _ <: java.lang.Throwable[↦-1000178;refId=180], _ <: java.lang.Throwable[↦-1000366;refId=198], _ <: java.lang.Throwable[↦-1000290;refId=160], java.lang.IllegalMonitorStateException[↦-100403;refId=174], java.lang.IllegalMonitorStateException[↦-100395;refId=182], _ <: java.lang.Throwable[↦-1000351;refId=195], _ <: java.lang.Throwable[↦-1000147;refId=190], java.lang.IllegalStateException[↦383;refId=166], _ <: java.lang.Throwable[↦-1000389;refId=168], _ <: java.lang.Throwable[↦-1000369;refId=201]»])),
	85: If(pc=409,UVar(defSites={52,22,17},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=3),
	86: If(pc=414,UVar(defSites={16,59,31},value={_ <: java.lang.Object, null}[refId=203; values=«null[↦78], {_ <: java.lang.Object, null}[↦301;refId=163], {_ <: java.lang.Object, null}[↦155;refId=179]»]),==,NullExpr(pc=-333),target=92),
	87: If(pc=418,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=104]),!=,NullExpr(pc=-333),target=91),
	88: Assignment(pc=422,DVar(useSites={90},value=long =-1,origin=88),LongConst(pc=422,-1)),
	89: Assignment(pc=425,DVar(useSites={90},value=int = -1,origin=89),IntConst(pc=425,-1)),
	90: VirtualMethodCall(pc=426,java.util.concurrent.ConcurrentHashMap,isInterface=false,void addCount(long,int),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={88},value=long =-1),UVar(defSites={89},value=int = -1))),
	91: ReturnValue(pc=431,UVar(defSites={16,59,31},value=_ <: java.lang.Object[refId=223; values=«{_ <: java.lang.Object, null}[↦301;refId=163], {_ <: java.lang.Object, null}[↦155;refId=179]»])),
	92: Assignment(pc=435,DVar(useSites={93},value=null[↦435],origin=92),NullExpr(pc=435)),
	93: ReturnValue(pc=436,UVar(defSites={92},value=null[↦435]))
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=5) -> {BB_14,BB_1b}
	BB_10: BasicBlock(start=29,end=29) -> {BB_3a,BB_f}
	BB_11: BasicBlock(start=61,end=61) -> {BB_41,BB_1c}
	BB_12: BasicBlock(start=1,end=1) -> {BB_3d,BB_1e}
	BB_13: BasicBlock(start=74,end=75) -> {BB_2c,BB_28}
	BB_14: BasicBlock(start=6,end=9) -> {BB_3d,BB_7}
	BB_15: BasicBlock(start=85,end=85) -> {BB_26,BB_2b}
	BB_16: BasicBlock(start=70,end=71) -> {BB_34,BB_f}
	BB_17: BasicBlock(start=21,end=21) -> {BB_21,BB_30}
	BB_18: BasicBlock(start=33,end=33) -> {BB_a,BB_1f}
	BB_19: BasicBlock(start=28,end=28) -> {BB_10,BB_3e}
	BB_1: BasicBlock(start=84,end=84) -> {BB_3d}
	BB_1a: BasicBlock(start=38,end=39) -> {BB_2c}
	BB_1b: BasicBlock(start=92,end=93) -> {BB_2f,BB_3d}
	BB_1c: BasicBlock(start=65,end=65) -> {BB_2a,BB_40}
	BB_1d: BasicBlock(start=73,end=73) -> {BB_2c}
	BB_1e: BasicBlock(start=2,end=2) -> {BB_2b}
	BB_1f: BasicBlock(start=34,end=34) -> {BB_2c,BB_2d}
	BB_20: BasicBlock(start=64,end=64) -> {BB_1c,BB_2c}
	BB_21: BasicBlock(start=22,end=23) -> {BB_9}
	BB_22: BasicBlock(start=44,end=45) -> {BB_e,BB_f}
	BB_23: BasicBlock(start=59,end=60) -> {BB_1c,BB_11}
	BB_24: BasicBlock(start=54,end=55) -> {BB_8,BB_2c}
	BB_25: BasicBlock(start=49,end=49) -> {BB_2c}
	BB_26: BasicBlock(start=86,end=86) -> {BB_3,BB_1b}
	BB_27: BasicBlock(start=81,end=81) -> {BB_15}
	BB_28: BasicBlock(start=76,end=78) -> {BB_3c,BB_f}
	BB_29: BasicBlock(start=91,end=91) -> {BB_2f,BB_3d}
	BB_2: BasicBlock(start=41,end=43) -> {BB_2c}
	BB_2a: BasicBlock(start=66,end=67) -> {BB_2c}
	BB_2b: BasicBlock(start=3,end=3) -> {BB_3b,BB_1b}
	BB_2c: BasicBlock(start=80,end=80) -> {BB_27,BB_f}
	BB_2d: BasicBlock(start=35,end=35) -> {BB_39,BB_f}
	BB_2e: BasicBlock(start=63,end=63) -> {BB_20,BB_f}
	BB_2f: ExitNode(normalReturn=true)
	BB_30: BasicBlock(start=50,end=51) -> {BB_b,BB_13}
	BB_31: BasicBlock(start=16,end=19) -> {BB_d,BB_f}
	BB_32: BasicBlock(start=31,end=32) -> {BB_a,BB_18}
	BB_33: BasicBlock(start=11,end=13) -> {BB_31,BB_c}
	BB_34: BasicBlock(start=72,end=72) -> {BB_1d,BB_f}
	BB_35: BasicBlock(start=40,end=40) -> {BB_2,BB_22}
	BB_36: BasicBlock(start=26,end=27) -> {BB_32,BB_19}
	BB_37: BasicBlock(start=58,end=58) -> {BB_2c,BB_23}
	BB_38: BasicBlock(start=82,end=83) -> {BB_1,BB_f}
	BB_39: BasicBlock(start=36,end=36) -> {BB_a,BB_2c}
	BB_3: BasicBlock(start=87,end=87) -> {BB_6,BB_29}
	BB_3a: BasicBlock(start=30,end=30) -> {BB_3e,BB_32}
	BB_3b: BasicBlock(start=4,end=4) -> {BB_3d,BB_0}
	BB_3c: BasicBlock(start=79,end=79) -> {BB_f}
	BB_3d: ExitNode(normalReturn=false)
	BB_3e: BasicBlock(start=47,end=48) -> {BB_25,BB_9}
	BB_3f: BasicBlock(start=15,end=15) -> {BB_2b}
	BB_40: BasicBlock(start=68,end=68) -> {BB_4,BB_f}
	BB_41: BasicBlock(start=62,end=62) -> {BB_2e,BB_2c}
	BB_4: BasicBlock(start=69,end=69) -> {BB_2c,BB_16}
	BB_5: BasicBlock(start=0,end=0) -> {BB_3d,BB_12}
	BB_6: BasicBlock(start=88,end=90) -> {BB_3d,BB_29}
	BB_7: BasicBlock(start=10,end=10) -> {BB_33,BB_1b}
	BB_8: BasicBlock(start=56,end=57) -> {BB_37,BB_f}
	BB_9: BasicBlock(start=24,end=25) -> {BB_3e,BB_36}
	BB_a: BasicBlock(start=37,end=37) -> {BB_1a,BB_35}
	BB_b: BasicBlock(start=52,end=53) -> {BB_24,BB_f}
	BB_c: BasicBlock(start=14,end=14) -> {BB_3d,BB_3f}
	BB_d: BasicBlock(start=20,end=20) -> {BB_17,BB_2c}
	BB_e: BasicBlock(start=46,end=46) -> {BB_2c}
	BB_f: CatchNode([-1,81)=>82,<none>) -> {BB_38}
),exceptionHandlers=(
	ExceptionHandler([-1, 81) -> 82, <FINALLY>),
	ExceptionHandler([82, 84) -> 82, <FINALLY>)
))

void <init>(int,float,int)
AITACode(params=(Parameters(
	0: useSites={0,25} (origin=-1),
	1: useSites={4,12,9} (origin=-2),
	2: useSites={2,14} (origin=-3),
	3: useSites={12,9,5} (origin=-4)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.AbstractMap,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),()),
	1: Assignment(pc=5,DVar(useSites={2},value=AFloatValue,origin=1),FloatConst(pc=5,0.0)),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),Compare(pc=6,UVar(defSites={-3},value=AFloatValue),cmpl,UVar(defSites={1},value=AFloatValue))),
	3: If(pc=7,UVar(defSites={2},value=an int),<=,IntConst(pc=-333,0),target=6),
	4: If(pc=11,UVar(defSites={-2},value=an int),<,IntConst(pc=-333,0),target=6),
	5: If(pc=15,UVar(defSites={-4},value=an int),>,IntConst(pc=-333,0),target=9),
	6: Assignment(pc=18,DVar(useSites={8,7},value=java.lang.IllegalArgumentException[↦18;refId=104],origin=6),New(pc=18,java.lang.IllegalArgumentException)),
	7: NonVirtualMethodCall(pc=22,java.lang.IllegalArgumentException,isInterface=false,void <init>(),UVar(defSites={6},value=java.lang.IllegalArgumentException[↦18;refId=104]),()),
	8: Throw(pc=25,UVar(defSites={6},value=java.lang.IllegalArgumentException[↦18;refId=104])),
	9: If(pc=28,UVar(defSites={-2},value=int ∈ [0,2147483647]),>=,UVar(defSites={-4},value=int ∈ [1,2147483647]),target=11),
	10: Nop(pc=31),
	11: Assignment(pc=33,DVar(useSites={16},value=ADoubleValue,origin=11),DoubleConst(pc=33,1.0)),
	12: Assignment(pc=35,DVar(useSites={13},value=ALongValue,origin=12),PrimitiveTypecastExpr(pc=35,LongType,UVar(defSites={-4,-2},value=int ∈ [1,2147483647]))),
	13: Assignment(pc=36,DVar(useSites={14},value=AFloatValue,origin=13),PrimitiveTypecastExpr(pc=36,FloatType,UVar(defSites={12},value=ALongValue))),
	14: Assignment(pc=38,DVar(useSites={15},value=AFloatValue,origin=14),BinaryExpr(pc=38,ComputationalTypeFloat,UVar(defSites={13},value=AFloatValue),/,UVar(defSites={-3},value=AFloatValue))),
	15: Assignment(pc=39,DVar(useSites={16},value=ADoubleValue,origin=15),PrimitiveTypecastExpr(pc=39,DoubleType,UVar(defSites={14},value=AFloatValue))),
	16: Assignment(pc=40,DVar(useSites={17},value=ADoubleValue,origin=16),BinaryExpr(pc=40,ComputationalTypeDouble,UVar(defSites={11},value=ADoubleValue),+,UVar(defSites={15},value=ADoubleValue))),
	17: Assignment(pc=41,DVar(useSites={19,23},value=ALongValue,origin=17),PrimitiveTypecastExpr(pc=41,LongType,UVar(defSites={16},value=ADoubleValue))),
	18: Assignment(pc=46,DVar(useSites={19},value=long =1073741824,origin=18),LongConst(pc=46,1073741824)),
	19: Assignment(pc=49,DVar(useSites={20},value=an int,origin=19),Compare(pc=49,UVar(defSites={17},value=ALongValue),cmp,UVar(defSites={18},value=long =1073741824))),
	20: If(pc=50,UVar(defSites={19},value=an int),<,IntConst(pc=-333,0),target=23),
	21: Assignment(pc=53,DVar(useSites={25},value=int = 1073741824,origin=21),IntConst(pc=53,1073741824)),
	22: Goto(pc=55,target=25),
	23: Assignment(pc=60,DVar(useSites={24},value=an int,origin=23),PrimitiveTypecastExpr(pc=60,IntegerType,UVar(defSites={17},value=ALongValue))),
	24: Assignment(pc=61,DVar(useSites={25},value=an int,origin=24),StaticFunctionCall(pc=61,java.util.concurrent.ConcurrentHashMap,isInterface=false,int tableSizeFor(int),(UVar(defSites={23},value=an int)))),
	25: PutField(pc=69,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={24,21},value=an int)),
	26: Return(pc=72)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_d,BB_4}
	BB_1: BasicBlock(start=5,end=5) -> {BB_5,BB_7}
	BB_2: BasicBlock(start=10,end=10) -> {BB_9}
	BB_3: BasicBlock(start=25,end=26) -> {BB_8}
	BB_4: BasicBlock(start=1,end=3) -> {BB_5,BB_c}
	BB_5: BasicBlock(start=6,end=7) -> {BB_d,BB_b}
	BB_6: BasicBlock(start=21,end=22) -> {BB_3}
	BB_7: BasicBlock(start=9,end=9) -> {BB_9,BB_2}
	BB_8: ExitNode(normalReturn=true)
	BB_9: BasicBlock(start=11,end=20) -> {BB_a,BB_6}
	BB_a: BasicBlock(start=23,end=24) -> {BB_d,BB_3}
	BB_b: BasicBlock(start=8,end=8) -> {BB_d}
	BB_c: BasicBlock(start=4,end=4) -> {BB_5,BB_1}
	BB_d: ExitNode(normalReturn=false)
))

java.lang.Object put(java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={1} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={1} (origin=-3)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={1},value=int = 0,origin=0),IntConst(pc=3,0)),
	1: Assignment(pc=4,DVar(useSites={2},value={_ <: java.lang.Object, null}[↦4;refId=106],origin=1),VirtualFunctionCall(pc=4,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.lang.Object putVal(java.lang.Object,java.lang.Object,boolean),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=104]),UVar(defSites={0},value=int = 0)))),
	2: ReturnValue(pc=7,UVar(defSites={1},value={_ <: java.lang.Object, null}[↦4;refId=106]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int compareComparables(java.lang.Class,java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	1: useSites={2} (origin=-2),
	2: useSites={6,5} (origin=-3),
	3: useSites={0,6,1} (origin=-4)
)),stmts=(
	0: If(pc=1,UVar(defSites={-4},value={_ <: java.lang.Object, null}[↦-3;refId=104]),==,NullExpr(pc=-333),target=3),
	1: Assignment(pc=5,DVar(useSites={2},value={java.lang.Class, null}[↦5;refId=106],origin=1),VirtualFunctionCall(pc=5,java.lang.Object,isInterface=false,java.lang.Class getClass(),UVar(defSites={-4},value=_ <: java.lang.Object[↦-3;refId=104]),())),
	2: If(pc=9,UVar(defSites={1},value={java.lang.Class, null}[↦5;refId=106]),==,UVar(defSites={-2},value={java.lang.Class, null}[↦-1;refId=102]),target=5),
	3: Assignment(pc=12,DVar(useSites={7},value=int = 0,origin=3),IntConst(pc=12,0)),
	4: Goto(pc=13,target=7),
	5: Checkcast(pc=17,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-2;refId=103]),java.lang.Comparable),
	6: Assignment(pc=21,DVar(useSites={7},value=an int,origin=6),VirtualFunctionCall(pc=21,java.lang.Comparable,isInterface=true,int compareTo(java.lang.Object),UVar(defSites={-3},value={_ <: java.lang.Comparable, null}[↦-2;refId=107]),(UVar(defSites={-4},value=_ <: java.lang.Object[↦-3;refId=104])))),
	7: ReturnValue(pc=26,UVar(defSites={6,3},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_2,BB_6}
	BB_1: BasicBlock(start=5,end=5) -> {BB_8,BB_3}
	BB_2: BasicBlock(start=1,end=1) -> {BB_8,BB_4}
	BB_3: BasicBlock(start=6,end=6) -> {BB_8,BB_5}
	BB_4: BasicBlock(start=2,end=2) -> {BB_1,BB_6}
	BB_5: BasicBlock(start=7,end=7) -> {BB_7}
	BB_6: BasicBlock(start=3,end=4) -> {BB_5}
	BB_7: ExitNode(normalReturn=true)
	BB_8: ExitNode(normalReturn=false)
))

java.lang.Object putVal(java.lang.Object,java.lang.Object,boolean)
AITACode(params=(Parameters(
	0: useSites={8,12,28,89,93} (origin=-1),
	1: useSites={0,60,33,49,5,69,21,35,51} (origin=-2),
	2: useSites={60,1,73,69,21,55} (origin=-3),
	3: useSites={72,54,30} (origin=-4)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=2),
	1: If(pc=5,UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=104]),!=,NullExpr(pc=-333),target=5),
	2: Assignment(pc=8,DVar(useSites={4,3},value=java.lang.NullPointerException[↦8;refId=108],origin=2),New(pc=8,java.lang.NullPointerException)),
	3: NonVirtualMethodCall(pc=12,java.lang.NullPointerException,isInterface=false,void <init>(),UVar(defSites={2},value=java.lang.NullPointerException[↦8;refId=108]),()),
	4: Throw(pc=15,UVar(defSites={2},value=java.lang.NullPointerException[↦8;refId=108])),
	5: Assignment(pc=17,DVar(useSites={6},value=an int,origin=5),VirtualFunctionCall(pc=17,java.lang.Object,isInterface=false,int hashCode(),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),())),
	6: Assignment(pc=20,DVar(useSites={16,60,69,21,47,31},value=an int,origin=6),StaticFunctionCall(pc=20,java.util.concurrent.ConcurrentHashMap,isInterface=false,int spread(int),(UVar(defSites={5},value=an int)))),
	7: Assignment(pc=25,DVar(useSites={88,86,93},value=int = 0,origin=7),IntConst(pc=25,0)),
	8: Assignment(pc=29,DVar(useSites={28,10,42,22,17,9,89},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107],origin=8),GetField(pc=29,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	9: If(pc=36,UVar(defSites={8,12,28},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[refId=122; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121]»]),==,NullExpr(pc=-333),target=12),
	10: Assignment(pc=41,DVar(useSites={11,15},value=int ∈ [0,2147483647],origin=10),ArrayLength(pc=41,UVar(defSites={8,12,28},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=122; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121]»]))),
	11: If(pc=45,UVar(defSites={10},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=14),
	12: Assignment(pc=49,DVar(useSites={28,10,42,22,17,9,89},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121],origin=12),VirtualFunctionCall(pc=49,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node[] initTable(),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),())),
	13: Goto(pc=54,target=9),
	14: Assignment(pc=61,DVar(useSites={15},value=int = 1,origin=14),IntConst(pc=61,1)),
	15: Assignment(pc=62,DVar(useSites={16},value=int ∈ [0,2147483646],origin=15),BinaryExpr(pc=62,ComputationalTypeInt,UVar(defSites={10},value=int ∈ [1,2147483647]),-,UVar(defSites={14},value=int = 1))),
	16: Assignment(pc=65,DVar(useSites={42,22,17,89},value=int ∈ [0,2147483646],origin=16),BinaryExpr(pc=65,ComputationalTypeInt,UVar(defSites={15},value=int ∈ [0,2147483646]),&,UVar(defSites={6},value=an int))),
	17: Assignment(pc=69,DVar(useSites={32,48,68,84,28,18,46,65,81,41,25,57,69,37,53,61,75,43,55},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦69;refId=145],origin=17),StaticFunctionCall(pc=69,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={8,12,28},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=122; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121]»]),UVar(defSites={16},value=int ∈ [0,2147483646])))),
	18: If(pc=75,UVar(defSites={17},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦69;refId=145]),!=,NullExpr(pc=-333),target=25),
	19: Assignment(pc=82,DVar(useSites={22},value=null[↦82],origin=19),NullExpr(pc=82)),
	20: Assignment(pc=83,DVar(useSites={22,21},value=java.util.concurrent.ConcurrentHashMap$Node[↦83;refId=146],origin=20),New(pc=83,java.util.concurrent.ConcurrentHashMap$Node)),
	21: NonVirtualMethodCall(pc=91,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object),UVar(defSites={20},value=java.util.concurrent.ConcurrentHashMap$Node[↦83;refId=146]),(UVar(defSites={6},value=an int),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=104]))),
	22: Assignment(pc=94,DVar(useSites={23},value=int ∈ [0,1],origin=22),StaticFunctionCall(pc=94,java.util.concurrent.ConcurrentHashMap,isInterface=false,boolean casTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={8,12,28},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=122; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121]»]),UVar(defSites={16},value=int ∈ [0,2147483646]),UVar(defSites={19},value=null[↦82]),UVar(defSites={20},value=java.util.concurrent.ConcurrentHashMap$Node[↦83;refId=146])))),
	23: If(pc=97,UVar(defSites={22},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=9),
	24: Goto(pc=100,target=92),
	25: Assignment(pc=105,DVar(useSites={44,27,31},value=an int,origin=25),GetField(pc=105,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145]))),
	26: Assignment(pc=111,DVar(useSites={27},value=int = -1,origin=26),IntConst(pc=111,-1)),
	27: If(pc=112,UVar(defSites={25},value=an int),!=,UVar(defSites={26},value=int = -1),target=30),
	28: Assignment(pc=120,DVar(useSites={10,42,22,17,9,89,29},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=152],origin=28),VirtualFunctionCall(pc=120,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node[] helpTransfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={8,12,28},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=122; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121]»]),UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145])))),
	29: Goto(pc=125,target=9),
	30: If(pc=129,UVar(defSites={-4},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=40),
	31: If(pc=136,UVar(defSites={25},value=an int),!=,UVar(defSites={6},value=an int),target=40),
	32: Assignment(pc=141,DVar(useSites={34,33,35},value={_ <: java.lang.Object, null}[↦141;refId=149],origin=32),GetField(pc=141,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145]))),
	33: If(pc=148,UVar(defSites={32},value={_ <: java.lang.Object, null}[↦141;refId=149]),==,UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),target=37),
	34: If(pc=153,UVar(defSites={32},value={_ <: java.lang.Object, null}[↦141;refId=149]),==,NullExpr(pc=-333),target=40),
	35: Assignment(pc=159,DVar(useSites={36},value=int ∈ [0,1],origin=35),VirtualFunctionCall(pc=159,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),(UVar(defSites={32},value=_ <: java.lang.Object[↦141;refId=149])))),
	36: If(pc=162,UVar(defSites={35},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=40),
	37: Assignment(pc=167,DVar(useSites={38,39},value={_ <: java.lang.Object, null}[↦167;refId=177],origin=37),GetField(pc=167,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145]))),
	38: If(pc=173,UVar(defSites={37},value={_ <: java.lang.Object, null}[↦167;refId=177]),==,NullExpr(pc=-333),target=40),
	39: ReturnValue(pc=178,UVar(defSites={37},value=_ <: java.lang.Object[↦167;refId=177])),
	40: Assignment(pc=179,DVar(useSites={90,91},value=null[↦179],origin=40),NullExpr(pc=179)),
	41: MonitorEnter(pc=187,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145])),
	42: Assignment(pc=192,DVar(useSites={43},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦192;refId=162],origin=42),StaticFunctionCall(pc=192,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={8,12,28},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=122; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121]»]),UVar(defSites={16},value=int ∈ [0,2147483646])))),
	43: If(pc=197,UVar(defSites={42},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦192;refId=162]),!=,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145]),target=81),
	44: If(pc=202,UVar(defSites={25},value=an int),<,IntConst(pc=-333,0),target=65),
	45: Assignment(pc=205,DVar(useSites={88,86,93,63},value=int = 1,origin=45),IntConst(pc=205,1)),
	46: Assignment(pc=214,DVar(useSites={47},value=an int,origin=46),GetField(pc=214,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={17,57},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=654; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦274;refId=650]»]))),
	47: If(pc=219,UVar(defSites={46},value=an int),!=,UVar(defSites={6},value=an int),target=57),
	48: Assignment(pc=224,DVar(useSites={50,49,51},value={_ <: java.lang.Object, null}[↦224;refId=666],origin=48),GetField(pc=224,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={17,57},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=654; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦274;refId=650]»]))),
	49: If(pc=231,UVar(defSites={48},value={_ <: java.lang.Object, null}[↦224;refId=666]),==,UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),target=53),
	50: If(pc=236,UVar(defSites={48},value={_ <: java.lang.Object, null}[↦224;refId=666]),==,NullExpr(pc=-333),target=57),
	51: Assignment(pc=242,DVar(useSites={52},value=int ∈ [0,1],origin=51),VirtualFunctionCall(pc=242,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),(UVar(defSites={48},value=_ <: java.lang.Object[↦224;refId=666])))),
	52: If(pc=245,UVar(defSites={51},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=57),
	53: Assignment(pc=250,DVar(useSites={90,91},value={_ <: java.lang.Object, null}[↦250;refId=680],origin=53),GetField(pc=250,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={17,57},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=667; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦274;refId=650]»]))),
	54: If(pc=256,UVar(defSites={-4},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=81),
	55: PutField(pc=262,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={17,57},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=667; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦274;refId=650]»]),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=104])),
	56: Goto(pc=265,target=81),
	57: Assignment(pc=274,DVar(useSites={48,58,46,53,61,55},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦274;refId=675],origin=57),GetField(pc=274,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={17,57},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=665; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦274;refId=650]»]))),
	58: If(pc=280,UVar(defSites={57},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦274;refId=675]),!=,NullExpr(pc=-333),target=63),
	59: Assignment(pc=285,DVar(useSites={60,61},value=java.util.concurrent.ConcurrentHashMap$Node[↦285;refId=676],origin=59),New(pc=285,java.util.concurrent.ConcurrentHashMap$Node)),
	60: NonVirtualMethodCall(pc=293,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object),UVar(defSites={59},value=java.util.concurrent.ConcurrentHashMap$Node[↦285;refId=676]),(UVar(defSites={6},value=an int),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=104]))),
	61: PutField(pc=296,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={17,57},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=665; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦274;refId=650]»]),UVar(defSites={59},value=java.util.concurrent.ConcurrentHashMap$Node[↦285;refId=676])),
	62: Goto(pc=299,target=81),
	63: Assignment(pc=302,DVar(useSites={64,88,86,93},value=an int,origin=63),BinaryExpr(pc=302,ComputationalTypeInt,UVar(defSites={45,63},value=an int),+,IntConst(pc=302,1))),
	64: Goto(pc=305,target=46),
	65: Assignment(pc=313,DVar(useSites={66},value=int ∈ [0,1],origin=65),InstanceOf(pc=313,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145]),java.util.concurrent.ConcurrentHashMap$TreeBin)),
	66: If(pc=316,UVar(defSites={65},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=75),
	67: Assignment(pc=319,DVar(useSites={88,86,93},value=int = 2,origin=67),IntConst(pc=319,2)),
	68: Checkcast(pc=324,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145]),java.util.concurrent.ConcurrentHashMap$TreeBin),
	69: Assignment(pc=331,DVar(useSites={70,73,71},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦331;refId=168],origin=69),VirtualFunctionCall(pc=331,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,java.util.concurrent.ConcurrentHashMap$TreeNode putTreeVal(int,java.lang.Object,java.lang.Object),UVar(defSites={17},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦69;refId=164]),(UVar(defSites={6},value=an int),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=104])))),
	70: If(pc=337,UVar(defSites={69},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦331;refId=168]),==,NullExpr(pc=-333),target=81),
	71: Assignment(pc=342,DVar(useSites={90,91},value={_ <: java.lang.Object, null}[↦342;refId=170],origin=71),GetField(pc=342,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={69},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦331;refId=168]))),
	72: If(pc=348,UVar(defSites={-4},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=81),
	73: PutField(pc=354,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={69},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦331;refId=168]),UVar(defSites={-3},value=_ <: java.lang.Object[↦-3;refId=104])),
	74: Goto(pc=357,target=81),
	75: Assignment(pc=362,DVar(useSites={76},value=int ∈ [0,1],origin=75),InstanceOf(pc=362,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=145]),java.util.concurrent.ConcurrentHashMap$ReservationNode)),
	76: If(pc=365,UVar(defSites={75},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=81),
	77: Assignment(pc=368,DVar(useSites={80,85,79},value=java.lang.IllegalStateException[↦368;refId=172],origin=77),New(pc=368,java.lang.IllegalStateException)),
	78: Assignment(pc=372,DVar(useSites={79},value=String("Recursive update")[@372;refId=173],origin=78),StringConst(pc=372,Recursive update)),
	79: NonVirtualMethodCall(pc=374,java.lang.IllegalStateException,isInterface=false,void <init>(java.lang.String),UVar(defSites={77},value=java.lang.IllegalStateException[↦368;refId=172]),(UVar(defSites={78},value=String("Recursive update")[@372;refId=173]))),
	80: Throw(pc=377,UVar(defSites={77},value=java.lang.IllegalStateException[↦368;refId=172])),
	81: MonitorExit(pc=380,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=111])),
	82: Goto(pc=381,target=86),
	83: CaughtException(pc=384,<ANY>,caused by={exception@60,exception[VM]@84,exception[VM]@68,exception@42,exception@79,exception@51,lv4d,exception@69,exception[VM]@81}),
	84: MonitorExit(pc=388,UVar(defSites={17},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦69;refId=111])),
	85: Throw(pc=391,UVar(defSites={-1000060,-100084,-100068,-1000042,-1000079,-1000051,77,-1000069,-100081},value=_ <: java.lang.Throwable[refId=198; values=«_ <: java.lang.Throwable[↦-1000192;refId=161], java.lang.ClassCastException[↦-100324;refId=165], java.lang.IllegalMonitorStateException[↦-100380;refId=189], java.lang.IllegalStateException[↦368;refId=172], java.lang.IllegalMonitorStateException[↦-100388;refId=179], _ <: java.lang.Throwable[↦-1000374;refId=174], _ <: java.lang.Throwable[↦-1000242;refId=197], _ <: java.lang.Throwable[↦-1000331;refId=167], _ <: java.lang.Throwable[↦-1000293;refId=184]»])),
	86: If(pc=394,UVar(defSites={45,67,7,63},value=an int),==,IntConst(pc=-333,0),target=9),
	87: Assignment(pc=399,DVar(useSites={88},value=int = 8,origin=87),IntConst(pc=399,8)),
	88: If(pc=401,UVar(defSites={45,67,7,63},value=an int),<,UVar(defSites={87},value=int = 8),target=90),
	89: VirtualMethodCall(pc=409,java.util.concurrent.ConcurrentHashMap,isInterface=false,void treeifyBin(java.util.concurrent.ConcurrentHashMap$Node[],int),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={8,12,28},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=122; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦29;refId=107], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦120;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦49;refId=121]»]),UVar(defSites={16},value=int ∈ [0,2147483646]))),
	90: If(pc=414,UVar(defSites={40,53,71},value={_ <: java.lang.Object, null}[refId=687; values=«null[↦179], {_ <: java.lang.Object, null}[↦342;refId=170], {_ <: java.lang.Object, null}[↦250;refId=680]»]),==,NullExpr(pc=-333),target=92),
	91: ReturnValue(pc=419,UVar(defSites={40,53,71},value=_ <: java.lang.Object[refId=690; values=«{_ <: java.lang.Object, null}[↦342;refId=170], {_ <: java.lang.Object, null}[↦250;refId=680]»])),
	92: Assignment(pc=424,DVar(useSites={93},value=long =1,origin=92),LongConst(pc=424,1)),
	93: VirtualMethodCall(pc=427,java.util.concurrent.ConcurrentHashMap,isInterface=false,void addCount(long,int),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={92},value=long =1),UVar(defSites={45,67,7,63},value=an int))),
	94: Assignment(pc=430,DVar(useSites={95},value=null[↦430],origin=94),NullExpr(pc=430)),
	95: ReturnValue(pc=431,UVar(defSites={94},value=null[↦430]))
),cfg=CFG(
	BB_0: BasicBlock(start=5,end=5) -> {BB_40,BB_14}
	BB_10: BasicBlock(start=29,end=29) -> {BB_1a}
	BB_11: BasicBlock(start=61,end=62) -> {BB_27}
	BB_12: BasicBlock(start=89,end=89) -> {BB_40,BB_41}
	BB_13: BasicBlock(start=1,end=1) -> {BB_0,BB_1d}
	BB_14: BasicBlock(start=6,end=6) -> {BB_40,BB_28}
	BB_15: BasicBlock(start=85,end=85) -> {BB_40}
	BB_16: BasicBlock(start=28,end=28) -> {BB_40,BB_10}
	BB_17: BasicBlock(start=70,end=70) -> {BB_24,BB_27}
	BB_18: BasicBlock(start=92,end=93) -> {BB_40,BB_3f}
	BB_19: BasicBlock(start=65,end=66) -> {BB_38,BB_31}
	BB_1: BasicBlock(start=10,end=10) -> {BB_40,BB_33}
	BB_1a: BasicBlock(start=9,end=9) -> {BB_25,BB_1}
	BB_1b: BasicBlock(start=53,end=54) -> {BB_27,BB_36}
	BB_1c: BasicBlock(start=73,end=74) -> {BB_27}
	BB_1d: BasicBlock(start=2,end=3) -> {BB_40,BB_3e}
	BB_1e: BasicBlock(start=45,end=45) -> {BB_d}
	BB_1f: BasicBlock(start=32,end=33) -> {BB_9,BB_20}
	BB_20: BasicBlock(start=34,end=34) -> {BB_2b,BB_35}
	BB_21: BasicBlock(start=22,end=22) -> {BB_40,BB_37}
	BB_22: BasicBlock(start=44,end=44) -> {BB_1e,BB_19}
	BB_23: BasicBlock(start=59,end=60) -> {BB_11,BB_e}
	BB_24: BasicBlock(start=71,end=72) -> {BB_27,BB_1c}
	BB_25: BasicBlock(start=12,end=12) -> {BB_40,BB_3}
	BB_26: BasicBlock(start=86,end=86) -> {BB_1a,BB_5}
	BB_27: BasicBlock(start=81,end=81) -> {BB_39,BB_e}
	BB_28: BasicBlock(start=7,end=8) -> {BB_1a}
	BB_29: BasicBlock(start=39,end=39) -> {BB_2f,BB_40}
	BB_2: BasicBlock(start=77,end=79) -> {BB_2a,BB_e}
	BB_2a: BasicBlock(start=80,end=80) -> {BB_e}
	BB_2b: BasicBlock(start=35,end=35) -> {BB_40,BB_3a}
	BB_2c: BasicBlock(start=48,end=49) -> {BB_1b,BB_30}
	BB_2d: BasicBlock(start=63,end=64) -> {BB_d}
	BB_2e: BasicBlock(start=18,end=18) -> {BB_3d,BB_a}
	BB_2f: ExitNode(normalReturn=true)
	BB_30: BasicBlock(start=50,end=50) -> {BB_f,BB_3c}
	BB_31: BasicBlock(start=67,end=68) -> {BB_6,BB_e}
	BB_32: BasicBlock(start=31,end=31) -> {BB_35,BB_1f}
	BB_33: BasicBlock(start=11,end=11) -> {BB_25,BB_c}
	BB_34: BasicBlock(start=43,end=43) -> {BB_22,BB_27}
	BB_35: BasicBlock(start=40,end=42) -> {BB_34,BB_e}
	BB_36: BasicBlock(start=55,end=56) -> {BB_27}
	BB_37: BasicBlock(start=23,end=23) -> {BB_8,BB_1a}
	BB_38: BasicBlock(start=75,end=76) -> {BB_2,BB_27}
	BB_39: BasicBlock(start=82,end=82) -> {BB_26}
	BB_3: BasicBlock(start=13,end=13) -> {BB_1a}
	BB_3a: BasicBlock(start=36,end=36) -> {BB_9,BB_35}
	BB_3b: BasicBlock(start=30,end=30) -> {BB_32,BB_35}
	BB_3c: BasicBlock(start=51,end=51) -> {BB_b,BB_e}
	BB_3d: BasicBlock(start=19,end=21) -> {BB_40,BB_21}
	BB_3e: BasicBlock(start=4,end=4) -> {BB_40}
	BB_3f: BasicBlock(start=94,end=95) -> {BB_2f,BB_40}
	BB_40: ExitNode(normalReturn=false)
	BB_41: BasicBlock(start=90,end=90) -> {BB_4,BB_18}
	BB_42: BasicBlock(start=83,end=84) -> {BB_15,BB_e}
	BB_4: BasicBlock(start=91,end=91) -> {BB_2f,BB_40}
	BB_5: BasicBlock(start=87,end=88) -> {BB_12,BB_41}
	BB_6: BasicBlock(start=69,end=69) -> {BB_17,BB_e}
	BB_7: BasicBlock(start=0,end=0) -> {BB_1d,BB_13}
	BB_8: BasicBlock(start=24,end=24) -> {BB_18}
	BB_9: BasicBlock(start=37,end=38) -> {BB_29,BB_35}
	BB_a: BasicBlock(start=25,end=27) -> {BB_3b,BB_16}
	BB_b: BasicBlock(start=52,end=52) -> {BB_1b,BB_f}
	BB_c: BasicBlock(start=14,end=17) -> {BB_40,BB_2e}
	BB_d: BasicBlock(start=46,end=47) -> {BB_f,BB_2c}
	BB_e: CatchNode([-1,82)=>83,<none>) -> {BB_42}
	BB_f: BasicBlock(start=57,end=58) -> {BB_2d,BB_23}
),exceptionHandlers=(
	ExceptionHandler([-1, 82) -> 83, <FINALLY>),
	ExceptionHandler([83, 85) -> 83, <FINALLY>)
))

int spread(int)
AITACode(params=(Parameters(
	1: useSites={2,1} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={1},value=int = 16,origin=0),IntConst(pc=2,16)),
	1: Assignment(pc=4,DVar(useSites={2},value=an int,origin=1),BinaryExpr(pc=4,ComputationalTypeInt,UVar(defSites={-2},value=an int),>>>,UVar(defSites={0},value=int = 16))),
	2: Assignment(pc=5,DVar(useSites={4},value=an int,origin=2),BinaryExpr(pc=5,ComputationalTypeInt,UVar(defSites={-2},value=an int),^,UVar(defSites={1},value=an int))),
	3: Assignment(pc=6,DVar(useSites={4},value=int = 2147483647,origin=3),IntConst(pc=6,2147483647)),
	4: Assignment(pc=8,DVar(useSites={5},value=int ∈ [0,2147483647],origin=4),BinaryExpr(pc=8,ComputationalTypeInt,UVar(defSites={2},value=an int),&,UVar(defSites={3},value=int = 2147483647))),
	5: ReturnValue(pc=9,UVar(defSites={4},value=int ∈ [0,2147483647]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=5) -> {BB_1}
	BB_1: ExitNode(normalReturn=true)
	BB_2: ExitNode(normalReturn=false)
))

java.lang.Object putIfAbsent(java.lang.Object,java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={1} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={1} (origin=-3)
)),stmts=(
	0: Assignment(pc=3,DVar(useSites={1},value=int = 1,origin=0),IntConst(pc=3,1)),
	1: Assignment(pc=4,DVar(useSites={2},value={_ <: java.lang.Object, null}[↦4;refId=106],origin=1),VirtualFunctionCall(pc=4,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.lang.Object putVal(java.lang.Object,java.lang.Object,boolean),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),UVar(defSites={-3},value={_ <: java.lang.Object, null}[↦-3;refId=104]),UVar(defSites={0},value=int = 1)))),
	2: ReturnValue(pc=7,UVar(defSites={1},value={_ <: java.lang.Object, null}[↦4;refId=106]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=2,end=2) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void <init>()
AITACode(params=(Parameters(
	0: useSites={0} (origin=-1)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.AbstractMap,isInterface=false,void <init>(),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),()),
	1: Return(pc=4)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=1) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

int tableSizeFor(int)
AITACode(params=(Parameters(
	1: useSites={2} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={4},value=int = -1,origin=0),IntConst(pc=0,-1)),
	1: Assignment(pc=2,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=2,1)),
	2: Assignment(pc=3,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=3,ComputationalTypeInt,UVar(defSites={-2},value=an int),-,UVar(defSites={1},value=int = 1))),
	3: Assignment(pc=4,DVar(useSites={4},value=an int,origin=3),StaticFunctionCall(pc=4,java.lang.Integer,isInterface=false,int numberOfLeadingZeros(int),(UVar(defSites={2},value=an int)))),
	4: Assignment(pc=7,DVar(useSites={9,5,13},value=an int,origin=4),BinaryExpr(pc=7,ComputationalTypeInt,UVar(defSites={0},value=int = -1),>>>,UVar(defSites={3},value=an int))),
	5: If(pc=10,UVar(defSites={4},value=an int),>=,IntConst(pc=-333,0),target=8),
	6: Assignment(pc=13,DVar(useSites={14},value=int = 1,origin=6),IntConst(pc=13,1)),
	7: Goto(pc=14,target=14),
	8: Assignment(pc=18,DVar(useSites={9},value=int = 1073741824,origin=8),IntConst(pc=18,1073741824)),
	9: If(pc=20,UVar(defSites={4},value=int ∈ [0,2147483647]),<,UVar(defSites={8},value=int = 1073741824),target=12),
	10: Assignment(pc=23,DVar(useSites={14},value=int = 1073741824,origin=10),IntConst(pc=23,1073741824)),
	11: Goto(pc=25,target=14),
	12: Assignment(pc=29,DVar(useSites={13},value=int = 1,origin=12),IntConst(pc=29,1)),
	13: Assignment(pc=30,DVar(useSites={14},value=int ∈ [0,2147483647],origin=13),BinaryExpr(pc=30,ComputationalTypeInt,UVar(defSites={4},value=int ∈ [0,1073741823]),+,UVar(defSites={12},value=int = 1))),
	14: ReturnValue(pc=31,UVar(defSites={10,6,13},value=int ∈ [0,2147483647]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=3) -> {BB_8,BB_7}
	BB_1: BasicBlock(start=10,end=11) -> {BB_2}
	BB_2: BasicBlock(start=14,end=14) -> {BB_5}
	BB_3: BasicBlock(start=6,end=7) -> {BB_2}
	BB_4: BasicBlock(start=12,end=13) -> {BB_2}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=8,end=9) -> {BB_4,BB_1}
	BB_7: BasicBlock(start=4,end=5) -> {BB_6,BB_3}
	BB_8: ExitNode(normalReturn=false)
))

java.util.concurrent.ConcurrentHashMap$Node[] helpTransfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node)
AITACode(params=(Parameters(
	0: useSites={28,22,30,33,9,13,11} (origin=-1),
	1: useSites={0,12,6,30} (origin=-2),
	2: useSites={4,1,3} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=33),
	1: Assignment(pc=5,DVar(useSites={2},value=int ∈ [0,1],origin=1),InstanceOf(pc=5,UVar(defSites={-3},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-3;refId=104]),java.util.concurrent.ConcurrentHashMap$ForwardingNode)),
	2: If(pc=8,UVar(defSites={1},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=33),
	3: Checkcast(pc=12,UVar(defSites={-3},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-3;refId=104]),java.util.concurrent.ConcurrentHashMap$ForwardingNode),
	4: Assignment(pc=15,DVar(useSites={32,10,30,5},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦15;refId=107],origin=4),GetField(pc=15,java.util.concurrent.ConcurrentHashMap$ForwardingNode,nextTable,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-3},value={java.util.concurrent.ConcurrentHashMap$ForwardingNode, null}[↦-3;refId=105]))),
	5: If(pc=20,UVar(defSites={4},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦15;refId=107]),==,NullExpr(pc=-333),target=33),
	6: Assignment(pc=24,DVar(useSites={7},value=int ∈ [0,2147483647],origin=6),ArrayLength(pc=24,UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]))),
	7: Assignment(pc=25,DVar(useSites={17},value=an int,origin=7),StaticFunctionCall(pc=25,java.util.concurrent.ConcurrentHashMap,isInterface=false,int resizeStamp(int),(UVar(defSites={6},value=int ∈ [0,2147483647])))),
	8: Nop(pc=28),
	9: Assignment(pc=32,DVar(useSites={10},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦32;refId=111],origin=9),GetField(pc=32,java.util.concurrent.ConcurrentHashMap,nextTable,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	10: If(pc=35,UVar(defSites={4},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦15;refId=107]),!=,UVar(defSites={9},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦32;refId=111]),target=32),
	11: Assignment(pc=39,DVar(useSites={12},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦39;refId=112],origin=11),GetField(pc=39,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	12: If(pc=43,UVar(defSites={11},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦39;refId=112]),!=,UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),target=32),
	13: Assignment(pc=47,DVar(useSites={16,28,14,27},value=an int,origin=13),GetField(pc=47,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	14: If(pc=53,UVar(defSites={13},value=an int),>=,IntConst(pc=-333,0),target=32),
	15: Assignment(pc=58,DVar(useSites={16},value=int = 16,origin=15),IntConst(pc=58,16)),
	16: Assignment(pc=60,DVar(useSites={17},value=int = 65535,origin=16),BinaryExpr(pc=60,ComputationalTypeInt,UVar(defSites={13},value=int ∈ [-2147483648,-1]),>>>,UVar(defSites={15},value=int = 16))),
	17: If(pc=63,UVar(defSites={16},value=int = 65535),!=,UVar(defSites={7},value=an int),target=32),
	18: Nop(pc=70),
	19: Nop(pc=71),
	20: Nop(pc=79),
	21: Nop(pc=81),
	22: Assignment(pc=86,DVar(useSites={23},value=an int,origin=22),GetField(pc=86,java.util.concurrent.ConcurrentHashMap,transferIndex,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	23: If(pc=89,UVar(defSites={22},value=an int),<=,IntConst(pc=-333,0),target=32),
	24: Assignment(pc=95,DVar(useSites={28},value={jdk.internal.misc.Unsafe, null}[↦95;refId=113],origin=24),GetStatic(pc=95,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	25: Assignment(pc=99,DVar(useSites={28},value=ALongValue,origin=25),GetStatic(pc=99,java.util.concurrent.ConcurrentHashMap,SIZECTL,long)),
	26: Assignment(pc=106,DVar(useSites={27},value=int = 1,origin=26),IntConst(pc=106,1)),
	27: Assignment(pc=107,DVar(useSites={28},value=int ∈ [-2147483647,0],origin=27),BinaryExpr(pc=107,ComputationalTypeInt,UVar(defSites={13},value=int ∈ [-2147483648,-1]),+,UVar(defSites={26},value=int = 1))),
	28: Assignment(pc=108,DVar(useSites={29},value=int ∈ [0,1],origin=28),VirtualFunctionCall(pc=108,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={24},value={jdk.internal.misc.Unsafe, null}[↦95;refId=113]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={25},value=ALongValue),UVar(defSites={13},value=int ∈ [-2147483648,-1]),UVar(defSites={27},value=int ∈ [-2147483647,0])))),
	29: If(pc=111,UVar(defSites={28},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=9),
	30: VirtualMethodCall(pc=117,java.util.concurrent.ConcurrentHashMap,isInterface=false,void transfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node[]),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={4},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦15;refId=107]))),
	31: Nop(pc=120),
	32: ReturnValue(pc=124,UVar(defSites={4},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦15;refId=107])),
	33: Assignment(pc=126,DVar(useSites={34},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦126;refId=110],origin=33),GetField(pc=126,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	34: ReturnValue(pc=129,UVar(defSites={33},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦126;refId=110]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_6}
	BB_10: BasicBlock(start=18,end=23) -> {BB_2,BB_9}
	BB_11: ExitNode(normalReturn=true)
	BB_12: BasicBlock(start=4,end=4) -> {BB_13,BB_1}
	BB_13: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=5,end=5) -> {BB_6,BB_5}
	BB_2: BasicBlock(start=24,end=28) -> {BB_13,BB_3}
	BB_3: BasicBlock(start=29,end=29) -> {BB_e,BB_7}
	BB_4: BasicBlock(start=1,end=2) -> {BB_6,BB_a}
	BB_5: BasicBlock(start=6,end=7) -> {BB_13,BB_d}
	BB_6: BasicBlock(start=33,end=34) -> {BB_11}
	BB_7: BasicBlock(start=9,end=10) -> {BB_c,BB_9}
	BB_8: BasicBlock(start=13,end=14) -> {BB_f,BB_9}
	BB_9: BasicBlock(start=32,end=32) -> {BB_11}
	BB_a: BasicBlock(start=3,end=3) -> {BB_13,BB_12}
	BB_b: BasicBlock(start=31,end=31) -> {BB_9}
	BB_c: BasicBlock(start=11,end=12) -> {BB_8,BB_9}
	BB_d: BasicBlock(start=8,end=8) -> {BB_7}
	BB_e: BasicBlock(start=30,end=30) -> {BB_13,BB_b}
	BB_f: BasicBlock(start=15,end=17) -> {BB_10,BB_9}
))

java.util.concurrent.ConcurrentHashMap$Node untreeify(java.util.concurrent.ConcurrentHashMap$Node)
AITACode(params=(Parameters(
	1: useSites={4,2,6,5,11} (origin=-2)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={13},value=null[↦0],origin=0),NullExpr(pc=0)),
	1: Assignment(pc=2,DVar(useSites={8,10},value=null[↦2],origin=1),NullExpr(pc=2)),
	2: If(pc=7,UVar(defSites={-2,11},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=110; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-1;refId=102], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦51;refId=107]»]),==,NullExpr(pc=-333),target=13),
	3: Assignment(pc=10,DVar(useSites={8,10,13,7},value=java.util.concurrent.ConcurrentHashMap$Node[↦10;refId=111],origin=3),New(pc=10,java.util.concurrent.ConcurrentHashMap$Node)),
	4: Assignment(pc=15,DVar(useSites={7},value=an int,origin=4),GetField(pc=15,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={-2,11},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=110; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-1;refId=102], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦51;refId=107]»]))),
	5: Assignment(pc=19,DVar(useSites={7},value={_ <: java.lang.Object, null}[↦19;refId=112],origin=5),GetField(pc=19,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={-2,11},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=110; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-1;refId=102], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦51;refId=107]»]))),
	6: Assignment(pc=23,DVar(useSites={7},value={_ <: java.lang.Object, null}[↦23;refId=113],origin=6),GetField(pc=23,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={-2,11},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=110; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-1;refId=102], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦51;refId=107]»]))),
	7: NonVirtualMethodCall(pc=26,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object),UVar(defSites={3},value=java.util.concurrent.ConcurrentHashMap$Node[↦10;refId=111]),(UVar(defSites={4},value=an int),UVar(defSites={5},value={_ <: java.lang.Object, null}[↦19;refId=112]),UVar(defSites={6},value={_ <: java.lang.Object, null}[↦23;refId=113]))),
	8: If(pc=32,UVar(defSites={1,3},value={java.util.concurrent.ConcurrentHashMap$Node, null}[refId=109; values=«null[↦2], java.util.concurrent.ConcurrentHashMap$Node[↦10;refId=103]»]),!=,NullExpr(pc=-333),target=10),
	9: Goto(pc=38,target=11),
	10: PutField(pc=44,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={1,3},value=java.util.concurrent.ConcurrentHashMap$Node[↦10;refId=103]),UVar(defSites={3},value=java.util.concurrent.ConcurrentHashMap$Node[↦10;refId=111])),
	11: Assignment(pc=51,DVar(useSites={4,12,2,6,5},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦51;refId=116],origin=11),GetField(pc=51,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={-2,11},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=110; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-1;refId=102], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦51;refId=107]»]))),
	12: Goto(pc=55,target=2),
	13: ReturnValue(pc=59,UVar(defSites={0,3},value={java.util.concurrent.ConcurrentHashMap$Node, null}[refId=108; values=«null[↦0], java.util.concurrent.ConcurrentHashMap$Node[↦10;refId=103]»]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=1) -> {BB_4}
	BB_1: BasicBlock(start=10,end=10) -> {BB_7}
	BB_2: BasicBlock(start=9,end=9) -> {BB_7}
	BB_3: BasicBlock(start=13,end=13) -> {BB_6}
	BB_4: BasicBlock(start=2,end=2) -> {BB_5,BB_3}
	BB_5: BasicBlock(start=3,end=7) -> {BB_9,BB_8}
	BB_6: ExitNode(normalReturn=true)
	BB_7: BasicBlock(start=11,end=12) -> {BB_4}
	BB_8: BasicBlock(start=8,end=8) -> {BB_1,BB_2}
	BB_9: ExitNode(normalReturn=false)
))

java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int)
AITACode(params=(Parameters(
	1: useSites={7} (origin=-2),
	2: useSites={1} (origin=-3)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={7},value={jdk.internal.misc.Unsafe, null}[↦0;refId=103],origin=0),GetStatic(pc=0,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	1: Assignment(pc=5,DVar(useSites={3},value=ALongValue,origin=1),PrimitiveTypecastExpr(pc=5,LongType,UVar(defSites={-3},value=an int))),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),GetStatic(pc=6,java.util.concurrent.ConcurrentHashMap,ASHIFT,int)),
	3: Assignment(pc=9,DVar(useSites={6},value=ALongValue,origin=3),BinaryExpr(pc=9,ComputationalTypeLong,UVar(defSites={1},value=ALongValue),<<,UVar(defSites={2},value=an int))),
	4: Assignment(pc=10,DVar(useSites={5},value=an int,origin=4),GetStatic(pc=10,java.util.concurrent.ConcurrentHashMap,ABASE,int)),
	5: Assignment(pc=13,DVar(useSites={6},value=ALongValue,origin=5),PrimitiveTypecastExpr(pc=13,LongType,UVar(defSites={4},value=an int))),
	6: Assignment(pc=14,DVar(useSites={7},value=ALongValue,origin=6),BinaryExpr(pc=14,ComputationalTypeLong,UVar(defSites={3},value=ALongValue),+,UVar(defSites={5},value=ALongValue))),
	7: Assignment(pc=15,DVar(useSites={8,9},value={_ <: java.lang.Object, null}[↦15;refId=106],origin=7),VirtualFunctionCall(pc=15,jdk.internal.misc.Unsafe,isInterface=false,java.lang.Object getObjectAcquire(java.lang.Object,long),UVar(defSites={0},value={jdk.internal.misc.Unsafe, null}[↦0;refId=103]),(UVar(defSites={-2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-1;refId=102]),UVar(defSites={6},value=ALongValue)))),
	8: Checkcast(pc=18,UVar(defSites={7},value={_ <: java.lang.Object, null}[↦15;refId=106]),java.util.concurrent.ConcurrentHashMap$Node),
	9: ReturnValue(pc=21,UVar(defSites={7},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦15;refId=107]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=7) -> {BB_4,BB_3}
	BB_1: BasicBlock(start=9,end=9) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: BasicBlock(start=8,end=8) -> {BB_4,BB_1}
	BB_4: ExitNode(normalReturn=false)
))

void treeifyBin(java.util.concurrent.ConcurrentHashMap$Node[],int)
AITACode(params=(Parameters(
	0: useSites={6} (origin=-1),
	1: useSites={0,8,1,33,13} (origin=-2),
	2: useSites={8,33,13} (origin=-3)
)),stmts=(
	0: If(pc=1,UVar(defSites={-2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-2;refId=103]),==,NullExpr(pc=-333),target=39),
	1: Assignment(pc=5,DVar(useSites={5,3},value=int ∈ [0,2147483647],origin=1),ArrayLength(pc=5,UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]))),
	2: Assignment(pc=9,DVar(useSites={3},value=int = 64,origin=2),IntConst(pc=9,64)),
	3: If(pc=11,UVar(defSites={1},value=int ∈ [0,2147483647]),>=,UVar(defSites={2},value=int = 64),target=8),
	4: Assignment(pc=17,DVar(useSites={5},value=int = 1,origin=4),IntConst(pc=17,1)),
	5: Assignment(pc=18,DVar(useSites={6},value=int ∈ [0,126],origin=5),BinaryExpr(pc=18,ComputationalTypeInt,UVar(defSites={1},value=int ∈ [0,63]),<<,UVar(defSites={4},value=int = 1))),
	6: VirtualMethodCall(pc=19,java.util.concurrent.ConcurrentHashMap,isInterface=false,void tryPresize(int),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={5},value=int ∈ [0,126]))),
	7: Goto(pc=22,target=39),
	8: Assignment(pc=27,DVar(useSites={20,12,34,10,14,17,9,37,21,29,19},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦27;refId=105],origin=8),StaticFunctionCall(pc=27,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={-3},value=an int)))),
	9: If(pc=32,UVar(defSites={8},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦27;refId=105]),==,NullExpr(pc=-333),target=39),
	10: Assignment(pc=36,DVar(useSites={11},value=an int,origin=10),GetField(pc=36,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={8},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105]))),
	11: If(pc=39,UVar(defSites={10},value=an int),<,IntConst(pc=-333,0),target=39),
	12: MonitorEnter(pc=46,UVar(defSites={8},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105])),
	13: Assignment(pc=49,DVar(useSites={14},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦49;refId=107],origin=13),StaticFunctionCall(pc=49,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={-3},value=an int)))),
	14: If(pc=53,UVar(defSites={13},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦49;refId=107]),!=,UVar(defSites={8},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105]),target=34),
	15: Assignment(pc=56,DVar(useSites={32},value=null[↦56],origin=15),NullExpr(pc=56)),
	16: Assignment(pc=59,DVar(useSites={28,26,25},value=null[↦59],origin=16),NullExpr(pc=59)),
	17: If(pc=67,UVar(defSites={8,29},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=124; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦127;refId=121]»]),==,NullExpr(pc=-333),target=31),
	18: Assignment(pc=70,DVar(useSites={32,24,28,26,25},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=125],origin=18),New(pc=70,java.util.concurrent.ConcurrentHashMap$TreeNode)),
	19: Assignment(pc=76,DVar(useSites={24},value=an int,origin=19),GetField(pc=76,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={8,29},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=124; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦127;refId=121]»]))),
	20: Assignment(pc=81,DVar(useSites={24},value={_ <: java.lang.Object, null}[↦81;refId=126],origin=20),GetField(pc=81,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={8,29},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=124; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦127;refId=121]»]))),
	21: Assignment(pc=86,DVar(useSites={24},value={_ <: java.lang.Object, null}[↦86;refId=127],origin=21),GetField(pc=86,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={8,29},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=124; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦127;refId=121]»]))),
	22: Assignment(pc=89,DVar(useSites={24},value=null[↦89],origin=22),NullExpr(pc=89)),
	23: Assignment(pc=90,DVar(useSites={24},value=null[↦90],origin=23),NullExpr(pc=90)),
	24: NonVirtualMethodCall(pc=91,java.util.concurrent.ConcurrentHashMap$TreeNode,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.concurrent.ConcurrentHashMap$Node,java.util.concurrent.ConcurrentHashMap$TreeNode),UVar(defSites={18},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=125]),(UVar(defSites={19},value=an int),UVar(defSites={20},value={_ <: java.lang.Object, null}[↦81;refId=126]),UVar(defSites={21},value={_ <: java.lang.Object, null}[↦86;refId=127]),UVar(defSites={22},value=null[↦89]),UVar(defSites={23},value=null[↦90]))),
	25: PutField(pc=101,java.util.concurrent.ConcurrentHashMap$TreeNode,prev,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={18},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=125]),UVar(defSites={16,18},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=123; values=«null[↦59], java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=114]»])),
	26: If(pc=104,UVar(defSites={16,18},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=123; values=«null[↦59], java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=114]»]),!=,NullExpr(pc=-333),target=28),
	27: Goto(pc=111,target=29),
	28: PutField(pc=118,java.util.concurrent.ConcurrentHashMap$TreeNode,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={16,18},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=114]),UVar(defSites={18},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=125])),
	29: Assignment(pc=127,DVar(useSites={20,30,17,21,19},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦127;refId=136],origin=29),GetField(pc=127,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={8,29},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=124; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦127;refId=121]»]))),
	30: Goto(pc=132,target=17),
	31: Assignment(pc=137,DVar(useSites={32,33},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦137;refId=131],origin=31),New(pc=137,java.util.concurrent.ConcurrentHashMap$TreeBin)),
	32: NonVirtualMethodCall(pc=143,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,void <init>(java.util.concurrent.ConcurrentHashMap$TreeNode),UVar(defSites={31},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦137;refId=131]),(UVar(defSites={18,15},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=122; values=«null[↦56], java.util.concurrent.ConcurrentHashMap$TreeNode[↦70;refId=114]»]))),
	33: StaticMethodCall(pc=146,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={31},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦137;refId=131]))),
	34: MonitorExit(pc=151,UVar(defSites={8},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105])),
	35: Goto(pc=152,target=39),
	36: CaughtException(pc=155,<ANY>,caused by={exception@32,exception@24,exception[VM]@34,exception@13,exception[VM]@37,exception@33}),
	37: MonitorExit(pc=159,UVar(defSites={8},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦27;refId=105])),
	38: Throw(pc=162,UVar(defSites={-1000032,-1000024,-100034,-1000013,-100037,-1000033},value=_ <: java.lang.Throwable[refId=135; values=«_ <: java.lang.Throwable[↦-1000049;refId=106], _ <: java.lang.Throwable[↦-1000146;refId=134], java.lang.IllegalMonitorStateException[↦-100151;refId=112], java.lang.IllegalMonitorStateException[↦-100159;refId=119], _ <: java.lang.Throwable[↦-1000143;refId=132], _ <: java.lang.Throwable[↦-1000091;refId=128]»])),
	39: Return(pc=163)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_4,BB_15}
	BB_10: BasicBlock(start=28,end=28) -> {BB_e}
	BB_11: BasicBlock(start=38,end=38) -> {BB_19}
	BB_12: BasicBlock(start=34,end=34) -> {BB_8,BB_d}
	BB_13: BasicBlock(start=17,end=17) -> {BB_16,BB_9}
	BB_14: BasicBlock(start=7,end=7) -> {BB_15}
	BB_15: BasicBlock(start=39,end=39) -> {BB_17,BB_19}
	BB_16: BasicBlock(start=18,end=24) -> {BB_2,BB_d}
	BB_17: ExitNode(normalReturn=true)
	BB_18: BasicBlock(start=4,end=6) -> {BB_19,BB_14}
	BB_19: ExitNode(normalReturn=false)
	BB_1: BasicBlock(start=10,end=11) -> {BB_7,BB_15}
	BB_2: BasicBlock(start=25,end=26) -> {BB_10,BB_6}
	BB_3: BasicBlock(start=14,end=14) -> {BB_c,BB_12}
	BB_4: BasicBlock(start=1,end=3) -> {BB_18,BB_a}
	BB_5: BasicBlock(start=9,end=9) -> {BB_1,BB_15}
	BB_6: BasicBlock(start=27,end=27) -> {BB_e}
	BB_7: BasicBlock(start=12,end=13) -> {BB_3,BB_d}
	BB_8: BasicBlock(start=35,end=35) -> {BB_15}
	BB_9: BasicBlock(start=31,end=32) -> {BB_f,BB_d}
	BB_a: BasicBlock(start=8,end=8) -> {BB_19,BB_5}
	BB_b: BasicBlock(start=36,end=37) -> {BB_11,BB_d}
	BB_c: BasicBlock(start=15,end=16) -> {BB_13}
	BB_d: CatchNode([-1,35)=>36,<none>) -> {BB_b}
	BB_e: BasicBlock(start=29,end=30) -> {BB_13}
	BB_f: BasicBlock(start=33,end=33) -> {BB_12,BB_d}
),exceptionHandlers=(
	ExceptionHandler([-1, 35) -> 36, <FINALLY>),
	ExceptionHandler([36, 38) -> 36, <FINALLY>)
))

int resizeStamp(int)
AITACode(params=(Parameters(
	1: useSites={0} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value=an int,origin=0),StaticFunctionCall(pc=1,java.lang.Integer,isInterface=false,int numberOfLeadingZeros(int),(UVar(defSites={-2},value=an int)))),
	1: Assignment(pc=4,DVar(useSites={2},value=int = 32768,origin=1),IntConst(pc=4,32768)),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),BinaryExpr(pc=6,ComputationalTypeInt,UVar(defSites={0},value=an int),|,UVar(defSites={1},value=int = 32768))),
	3: ReturnValue(pc=7,UVar(defSites={2},value=an int))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

java.lang.Object get(java.lang.Object)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={0,32,16,34,14,21} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={1},value=an int,origin=0),VirtualFunctionCall(pc=1,java.lang.Object,isInterface=false,int hashCode(),UVar(defSites={-2},value={_ <: java.lang.Object, null}[↦-2;refId=103]),())),
	1: Assignment(pc=4,DVar(useSites={8,12,30,21},value=an int,origin=1),StaticFunctionCall(pc=4,java.util.concurrent.ConcurrentHashMap,isInterface=false,int spread(int),(UVar(defSites={0},value=an int)))),
	2: Assignment(pc=10,DVar(useSites={4,9,3},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=107],origin=2),GetField(pc=10,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	3: If(pc=15,UVar(defSites={2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦10;refId=107]),==,NullExpr(pc=-333),target=38),
	4: Assignment(pc=19,DVar(useSites={5,7},value=int ∈ [0,2147483647],origin=4),ArrayLength(pc=19,UVar(defSites={2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦10;refId=107]))),
	5: If(pc=23,UVar(defSites={4},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=38),
	6: Assignment(pc=29,DVar(useSites={7},value=int = 1,origin=6),IntConst(pc=29,1)),
	7: Assignment(pc=30,DVar(useSites={8},value=int ∈ [0,2147483646],origin=7),BinaryExpr(pc=30,ComputationalTypeInt,UVar(defSites={4},value=int ∈ [1,2147483647]),-,UVar(defSites={6},value=int = 1))),
	8: Assignment(pc=33,DVar(useSites={9},value=int ∈ [0,2147483646],origin=8),BinaryExpr(pc=33,ComputationalTypeInt,UVar(defSites={7},value=int ∈ [0,2147483646]),&,UVar(defSites={1},value=an int))),
	9: Assignment(pc=34,DVar(useSites={18,10,21,13,11,27},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦34;refId=109],origin=9),StaticFunctionCall(pc=34,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦10;refId=107]),UVar(defSites={8},value=int ∈ [0,2147483646])))),
	10: If(pc=39,UVar(defSites={9},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦34;refId=109]),==,NullExpr(pc=-333),target=38),
	11: Assignment(pc=43,DVar(useSites={20,12},value=an int,origin=11),GetField(pc=43,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦34;refId=109]))),
	12: If(pc=51,UVar(defSites={11},value=an int),!=,UVar(defSites={1},value=an int),target=20),
	13: Assignment(pc=55,DVar(useSites={16,14,15},value={_ <: java.lang.Object, null}[↦55;refId=114],origin=13),GetField(pc=55,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦34;refId=109]))),
	14: If(pc=62,UVar(defSites={13},value={_ <: java.lang.Object, null}[↦55;refId=114]),==,UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),target=18),
	15: If(pc=67,UVar(defSites={13},value={_ <: java.lang.Object, null}[↦55;refId=114]),==,NullExpr(pc=-333),target=27),
	16: Assignment(pc=73,DVar(useSites={17},value=int ∈ [0,1],origin=16),VirtualFunctionCall(pc=73,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),(UVar(defSites={13},value=_ <: java.lang.Object[↦55;refId=114])))),
	17: If(pc=76,UVar(defSites={16},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=27),
	18: Assignment(pc=80,DVar(useSites={19},value={_ <: java.lang.Object, null}[↦80;refId=120],origin=18),GetField(pc=80,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦34;refId=109]))),
	19: ReturnValue(pc=83,UVar(defSites={18},value={_ <: java.lang.Object, null}[↦80;refId=120])),
	20: If(pc=86,UVar(defSites={11},value=an int),>=,IntConst(pc=-333,0),target=27),
	21: Assignment(pc=93,DVar(useSites={22,23},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦93;refId=111],origin=21),VirtualFunctionCall(pc=93,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node find(int,java.lang.Object),UVar(defSites={9},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦34;refId=109]),(UVar(defSites={1},value=an int),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103])))),
	22: If(pc=99,UVar(defSites={21},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦93;refId=111]),==,NullExpr(pc=-333),target=25),
	23: Assignment(pc=104,DVar(useSites={26},value={_ <: java.lang.Object, null}[↦104;refId=112],origin=23),GetField(pc=104,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={21},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦93;refId=111]))),
	24: Goto(pc=107,target=26),
	25: Assignment(pc=110,DVar(useSites={26},value={_ <: java.lang.Object, null}[refId=113; values=«{_ <: java.lang.Object, null}[↦104;refId=112], null[↦110]»],origin=25),NullExpr(pc=110)),
	26: ReturnValue(pc=111,UVar(defSites={25,23},value={_ <: java.lang.Object, null}[refId=113; values=«{_ <: java.lang.Object, null}[↦104;refId=112], null[↦110]»])),
	27: Assignment(pc=113,DVar(useSites={36,28,29,31},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦113;refId=121],origin=27),GetField(pc=113,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={9,27},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=117; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦34;refId=109], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦113;refId=116]»]))),
	28: If(pc=118,UVar(defSites={27},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦113;refId=121]),==,NullExpr(pc=-333),target=38),
	29: Assignment(pc=122,DVar(useSites={30},value=an int,origin=29),GetField(pc=122,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={27},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦113;refId=121]))),
	30: If(pc=127,UVar(defSites={29},value=an int),!=,UVar(defSites={1},value=an int),target=27),
	31: Assignment(pc=131,DVar(useSites={32,34,33},value={_ <: java.lang.Object, null}[↦131;refId=123],origin=31),GetField(pc=131,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={27},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦113;refId=121]))),
	32: If(pc=138,UVar(defSites={31},value={_ <: java.lang.Object, null}[↦131;refId=123]),==,UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),target=36),
	33: If(pc=143,UVar(defSites={31},value={_ <: java.lang.Object, null}[↦131;refId=123]),==,NullExpr(pc=-333),target=27),
	34: Assignment(pc=149,DVar(useSites={35},value=int ∈ [0,1],origin=34),VirtualFunctionCall(pc=149,java.lang.Object,isInterface=false,boolean equals(java.lang.Object),UVar(defSites={-2},value=_ <: java.lang.Object[↦-2;refId=103]),(UVar(defSites={31},value=_ <: java.lang.Object[↦131;refId=123])))),
	35: If(pc=152,UVar(defSites={34},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=27),
	36: Assignment(pc=156,DVar(useSites={37},value={_ <: java.lang.Object, null}[↦156;refId=125],origin=36),GetField(pc=156,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={27},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦113;refId=121]))),
	37: ReturnValue(pc=159,UVar(defSites={36},value={_ <: java.lang.Object, null}[↦156;refId=125])),
	38: Assignment(pc=160,DVar(useSites={39},value=null[↦160],origin=38),NullExpr(pc=160)),
	39: ReturnValue(pc=161,UVar(defSites={38},value=null[↦160]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_1b,BB_3}
	BB_10: BasicBlock(start=34,end=34) -> {BB_1b,BB_7}
	BB_11: BasicBlock(start=17,end=17) -> {BB_13,BB_14}
	BB_12: BasicBlock(start=22,end=22) -> {BB_19,BB_2}
	BB_13: BasicBlock(start=27,end=28) -> {BB_d,BB_c}
	BB_14: BasicBlock(start=18,end=19) -> {BB_15}
	BB_15: ExitNode(normalReturn=true)
	BB_16: BasicBlock(start=16,end=16) -> {BB_1b,BB_11}
	BB_17: BasicBlock(start=31,end=32) -> {BB_f,BB_9}
	BB_18: BasicBlock(start=26,end=26) -> {BB_15}
	BB_19: BasicBlock(start=23,end=24) -> {BB_18}
	BB_1: BasicBlock(start=10,end=10) -> {BB_d,BB_8}
	BB_1a: BasicBlock(start=4,end=5) -> {BB_d,BB_4}
	BB_1b: ExitNode(normalReturn=false)
	BB_2: BasicBlock(start=25,end=25) -> {BB_18}
	BB_3: BasicBlock(start=1,end=1) -> {BB_1b,BB_6}
	BB_4: BasicBlock(start=6,end=9) -> {BB_1b,BB_1}
	BB_5: BasicBlock(start=13,end=14) -> {BB_a,BB_14}
	BB_6: BasicBlock(start=2,end=3) -> {BB_d,BB_1a}
	BB_7: BasicBlock(start=35,end=35) -> {BB_13,BB_9}
	BB_8: BasicBlock(start=11,end=12) -> {BB_b,BB_5}
	BB_9: BasicBlock(start=36,end=37) -> {BB_15}
	BB_a: BasicBlock(start=15,end=15) -> {BB_13,BB_16}
	BB_b: BasicBlock(start=20,end=20) -> {BB_13,BB_e}
	BB_c: BasicBlock(start=29,end=30) -> {BB_13,BB_17}
	BB_d: BasicBlock(start=38,end=39) -> {BB_15}
	BB_e: BasicBlock(start=21,end=21) -> {BB_1b,BB_12}
	BB_f: BasicBlock(start=33,end=33) -> {BB_13,BB_10}
))

void <init>(int)
AITACode(params=(Parameters(
	0: useSites={2} (origin=-1),
	1: useSites={2} (origin=-2)
)),stmts=(
	0: Assignment(pc=2,DVar(useSites={2},value=AFloatValue,origin=0),FloatConst(pc=2,0.75)),
	1: Assignment(pc=4,DVar(useSites={2},value=int = 1,origin=1),IntConst(pc=4,1)),
	2: NonVirtualMethodCall(pc=5,java.util.concurrent.ConcurrentHashMap,isInterface=false,void <init>(int,float,int),UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),(UVar(defSites={-2},value=an int),UVar(defSites={0},value=AFloatValue),UVar(defSites={1},value=int = 1))),
	3: Return(pc=8)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=3,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node)
AITACode(params=(Parameters(
	1: useSites={7} (origin=-2),
	2: useSites={1} (origin=-3),
	3: useSites={7} (origin=-4)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={7},value={jdk.internal.misc.Unsafe, null}[↦0;refId=104],origin=0),GetStatic(pc=0,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	1: Assignment(pc=5,DVar(useSites={3},value=ALongValue,origin=1),PrimitiveTypecastExpr(pc=5,LongType,UVar(defSites={-3},value=an int))),
	2: Assignment(pc=6,DVar(useSites={3},value=an int,origin=2),GetStatic(pc=6,java.util.concurrent.ConcurrentHashMap,ASHIFT,int)),
	3: Assignment(pc=9,DVar(useSites={6},value=ALongValue,origin=3),BinaryExpr(pc=9,ComputationalTypeLong,UVar(defSites={1},value=ALongValue),<<,UVar(defSites={2},value=an int))),
	4: Assignment(pc=10,DVar(useSites={5},value=an int,origin=4),GetStatic(pc=10,java.util.concurrent.ConcurrentHashMap,ABASE,int)),
	5: Assignment(pc=13,DVar(useSites={6},value=ALongValue,origin=5),PrimitiveTypecastExpr(pc=13,LongType,UVar(defSites={4},value=an int))),
	6: Assignment(pc=14,DVar(useSites={7},value=ALongValue,origin=6),BinaryExpr(pc=14,ComputationalTypeLong,UVar(defSites={3},value=ALongValue),+,UVar(defSites={5},value=ALongValue))),
	7: VirtualMethodCall(pc=16,jdk.internal.misc.Unsafe,isInterface=false,void putObjectRelease(java.lang.Object,long,java.lang.Object),UVar(defSites={0},value={jdk.internal.misc.Unsafe, null}[↦0;refId=104]),(UVar(defSites={-2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-1;refId=102]),UVar(defSites={6},value=ALongValue),UVar(defSites={-4},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦-3;refId=103]))),
	8: Return(pc=19)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=7) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=8,end=8) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

void transfer(java.util.concurrent.ConcurrentHashMap$Node[],java.util.concurrent.ConcurrentHashMap$Node[])
AITACode(params=(Parameters(
	0: useSites={56,44,18,70,33,57,67,19,63} (origin=-1),
	1: useSites={0,84,92,126,81,183} (origin=-2),
	2: useSites={20,180,22,182,57,13,125,123} (origin=-3)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={40,84,52,180,28,92,124,50,74,126,81,113,41,5,181,61,99,19,147,51,11,59,123,183,15,95},value=int ∈ [0,2147483647],origin=0),ArrayLength(pc=1,UVar(defSites={-2},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-2;refId=103]))),
	1: Assignment(pc=3,DVar(useSites={3},value=an int,origin=1),GetStatic(pc=3,java.util.concurrent.ConcurrentHashMap,NCPU,int)),
	2: Assignment(pc=6,DVar(useSites={3},value=int = 1,origin=2),IntConst(pc=6,1)),
	3: If(pc=7,UVar(defSites={1},value=an int),<=,UVar(defSites={2},value=int = 1),target=9),
	4: Assignment(pc=11,DVar(useSites={5},value=int = 3,origin=4),IntConst(pc=11,3)),
	5: Assignment(pc=12,DVar(useSites={7},value=int ∈ [0,268435455],origin=5),BinaryExpr(pc=12,ComputationalTypeInt,UVar(defSites={0},value=int ∈ [0,2147483647]),>>>,UVar(defSites={4},value=int = 3))),
	6: Assignment(pc=13,DVar(useSites={7},value=an int,origin=6),GetStatic(pc=13,java.util.concurrent.ConcurrentHashMap,NCPU,int)),
	7: Assignment(pc=16,DVar(useSites={40,41,11},value=an int,origin=7),BinaryExpr(pc=16,ComputationalTypeInt,UVar(defSites={5},value=int ∈ [0,268435455]),/,UVar(defSites={6},value=an int))),
	8: Goto(pc=17,target=10),
	9: Nop(pc=20),
	10: Assignment(pc=24,DVar(useSites={11},value=int = 16,origin=10),IntConst(pc=24,16)),
	11: If(pc=26,UVar(defSites={0,7},value=an int),>=,UVar(defSites={10},value=int = 16),target=13),
	12: Assignment(pc=29,DVar(useSites={40,41},value=int = 16,origin=12),IntConst(pc=29,16)),
	13: If(pc=34,UVar(defSites={-3},value={_ <: java.util.concurrent.ConcurrentHashMap$Node[], null}[↦-3;refId=104]),!=,NullExpr(pc=-333),target=20),
	14: Assignment(pc=38,DVar(useSites={15},value=int = 1,origin=14),IntConst(pc=38,1)),
	15: Assignment(pc=39,DVar(useSites={16},value=int ∈ [-2147483646,2147483646],origin=15),BinaryExpr(pc=39,ComputationalTypeInt,UVar(defSites={0},value=int ∈ [0,2147483647]),<<,UVar(defSites={14},value=int = 1))),
	16: Assignment(pc=40,DVar(useSites={20,180,18,22,182,57,125,123},value=java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107],origin=16),NewArray(pc=40,[UVar(defSites={15},value=int ∈ [-2147483646,2147483646])],java.util.concurrent.ConcurrentHashMap$Node[])),
	17: Goto(pc=48,target=18),
	18: PutField(pc=62,java.util.concurrent.ConcurrentHashMap,nextTable,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={16},value=java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107])),
	19: PutField(pc=67,java.util.concurrent.ConcurrentHashMap,transferIndex,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={0},value=int ∈ [0,2147483647])),
	20: Assignment(pc=71,DVar(useSites={53},value=int ∈ [0,2147483647],origin=20),ArrayLength(pc=71,UVar(defSites={16,-3},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=108; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-3;refId=104], java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107]»]))),
	21: Assignment(pc=74,DVar(useSites={84,22,126,183},value=java.util.concurrent.ConcurrentHashMap$ForwardingNode[↦74;refId=109],origin=21),New(pc=74,java.util.concurrent.ConcurrentHashMap$ForwardingNode)),
	22: NonVirtualMethodCall(pc=79,java.util.concurrent.ConcurrentHashMap$ForwardingNode,isInterface=false,void <init>(java.util.concurrent.ConcurrentHashMap$Node[]),UVar(defSites={21},value=java.util.concurrent.ConcurrentHashMap$ForwardingNode[↦74;refId=109]),(UVar(defSites={16,-3},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=108; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-3;refId=104], java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107]»]))),
	23: Assignment(pc=84,DVar(useSites={27},value=int = 1,origin=23),IntConst(pc=84,1)),
	24: Assignment(pc=87,DVar(useSites={54,30},value=int = 0,origin=24),IntConst(pc=87,0)),
	25: Assignment(pc=90,DVar(useSites={84,52,180,28,92,124,50,126,81,181,51,123,183},value=int = 0,origin=25),IntConst(pc=90,0)),
	26: Assignment(pc=93,DVar(useSites={29},value=int = 0,origin=26),IntConst(pc=93,0)),
	27: If(pc=98,UVar(defSites={48,184,36,84,89,23,79,31,127},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=50),
	28: Assignment(pc=101,DVar(useSites={84,52,180,92,124,50,126,81,181,29,51,123,183},value=an int,origin=28),BinaryExpr(pc=101,ComputationalTypeInt,UVar(defSites={0,28,25,35,47},value=an int),+,IntConst(pc=101,-1))),
	29: If(pc=108,UVar(defSites={28},value=an int),>=,UVar(defSites={26,41,43},value=an int),target=31),
	30: If(pc=113,UVar(defSites={24,79},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=33),
	31: Assignment(pc=116,DVar(useSites={27},value=int = 0,origin=31),IntConst(pc=116,0)),
	32: Goto(pc=119,target=27),
	33: Assignment(pc=123,DVar(useSites={40,44,34,41,47},value=an int,origin=33),GetField(pc=123,java.util.concurrent.ConcurrentHashMap,transferIndex,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	34: If(pc=129,UVar(defSites={33},value=an int),>,IntConst(pc=-333,0),target=38),
	35: Assignment(pc=132,DVar(useSites={84,52,180,28,92,124,50,126,81,181,51,123,183},value=int = -1,origin=35),IntConst(pc=132,-1)),
	36: Assignment(pc=135,DVar(useSites={27},value=int = 0,origin=36),IntConst(pc=135,0)),
	37: Goto(pc=138,target=27),
	38: Assignment(pc=141,DVar(useSites={44},value={jdk.internal.misc.Unsafe, null}[↦141;refId=311],origin=38),GetStatic(pc=141,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	39: Assignment(pc=145,DVar(useSites={44},value=ALongValue,origin=39),GetStatic(pc=145,java.util.concurrent.ConcurrentHashMap,TRANSFERINDEX,long)),
	40: If(pc=154,UVar(defSites={33},value=int ∈ [1,2147483647]),<=,UVar(defSites={0,12,7},value=int ∈ [16,2147483647]),target=43),
	41: Assignment(pc=161,DVar(useSites={44,29},value=int ∈ [-2147483629,2147483631],origin=41),BinaryExpr(pc=161,ComputationalTypeInt,UVar(defSites={33},value=int ∈ [17,2147483647]),-,UVar(defSites={0,12,7},value=int ∈ [16,2147483646]))),
	42: Goto(pc=162,target=44),
	43: Assignment(pc=165,DVar(useSites={44,29},value=an int,origin=43),IntConst(pc=165,0)),
	44: Assignment(pc=169,DVar(useSites={45},value=int ∈ [0,1],origin=44),VirtualFunctionCall(pc=169,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={38},value={jdk.internal.misc.Unsafe, null}[↦141;refId=311]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={39},value=ALongValue),UVar(defSites={33},value=int ∈ [1,2147483647]),UVar(defSites={41,43},value=an int)))),
	45: If(pc=172,UVar(defSites={44},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=27),
	46: Assignment(pc=181,DVar(useSites={47},value=int = 1,origin=46),IntConst(pc=181,1)),
	47: Assignment(pc=182,DVar(useSites={84,52,180,28,92,124,50,126,81,181,51,123,183},value=int ∈ [0,2147483646],origin=47),BinaryExpr(pc=182,ComputationalTypeInt,UVar(defSites={33},value=int ∈ [1,2147483647]),-,UVar(defSites={46},value=int = 1))),
	48: Assignment(pc=185,DVar(useSites={27},value=int = 0,origin=48),IntConst(pc=185,0)),
	49: Goto(pc=188,target=27),
	50: If(pc=193,UVar(defSites={0,28,25,35,47},value=an int),<,IntConst(pc=-333,0),target=54),
	51: If(pc=199,UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483647]),>=,UVar(defSites={0},value=int ∈ [0,2147483647]),target=54),
	52: Assignment(pc=205,DVar(useSites={53},value=an int,origin=52),BinaryExpr(pc=205,ComputationalTypeInt,UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483646]),+,UVar(defSites={0},value=int ∈ [1,2147483647]))),
	53: If(pc=208,UVar(defSites={52},value=an int),<,UVar(defSites={20},value=int ∈ [0,2147483647]),target=81),
	54: If(pc=213,UVar(defSites={24,79},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=65),
	55: Assignment(pc=217,DVar(useSites={56},value=null[↦217],origin=55),NullExpr(pc=217)),
	56: PutField(pc=218,java.util.concurrent.ConcurrentHashMap,nextTable,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={55},value=null[↦217])),
	57: PutField(pc=223,java.util.concurrent.ConcurrentHashMap,table,java.util.concurrent.ConcurrentHashMap$Node[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={16,-3},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=108; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-3;refId=104], java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107]»])),
	58: Assignment(pc=228,DVar(useSites={59},value=int = 1,origin=58),IntConst(pc=228,1)),
	59: Assignment(pc=229,DVar(useSites={62},value=int ∈ [-2147483646,2147483646],origin=59),BinaryExpr(pc=229,ComputationalTypeInt,UVar(defSites={0},value=int ∈ [0,2147483647]),<<,UVar(defSites={58},value=int = 1))),
	60: Assignment(pc=231,DVar(useSites={61},value=int = 1,origin=60),IntConst(pc=231,1)),
	61: Assignment(pc=232,DVar(useSites={62},value=int ∈ [0,1073741823],origin=61),BinaryExpr(pc=232,ComputationalTypeInt,UVar(defSites={0},value=int ∈ [0,2147483647]),>>>,UVar(defSites={60},value=int = 1))),
	62: Assignment(pc=233,DVar(useSites={63},value=an int,origin=62),BinaryExpr(pc=233,ComputationalTypeInt,UVar(defSites={59},value=int ∈ [-2147483646,2147483646]),-,UVar(defSites={61},value=int ∈ [0,1073741823]))),
	63: PutField(pc=234,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={62},value=an int)),
	64: Return(pc=237),
	65: Assignment(pc=238,DVar(useSites={70},value={jdk.internal.misc.Unsafe, null}[↦238;refId=345],origin=65),GetStatic(pc=238,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	66: Assignment(pc=242,DVar(useSites={70},value=ALongValue,origin=66),GetStatic(pc=242,java.util.concurrent.ConcurrentHashMap,SIZECTL,long)),
	67: Assignment(pc=246,DVar(useSites={70,73,69},value=an int,origin=67),GetField(pc=246,java.util.concurrent.ConcurrentHashMap,sizeCtl,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	68: Assignment(pc=254,DVar(useSites={69},value=int = 1,origin=68),IntConst(pc=254,1)),
	69: Assignment(pc=255,DVar(useSites={70},value=an int,origin=69),BinaryExpr(pc=255,ComputationalTypeInt,UVar(defSites={67},value=an int),-,UVar(defSites={68},value=int = 1))),
	70: Assignment(pc=256,DVar(useSites={71},value=int ∈ [0,1],origin=70),VirtualFunctionCall(pc=256,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={65},value={jdk.internal.misc.Unsafe, null}[↦238;refId=345]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={66},value=ALongValue),UVar(defSites={67},value=an int),UVar(defSites={69},value=an int)))),
	71: If(pc=259,UVar(defSites={70},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=190),
	72: Assignment(pc=264,DVar(useSites={73},value=int = 2,origin=72),IntConst(pc=264,2)),
	73: Assignment(pc=265,DVar(useSites={77},value=an int,origin=73),BinaryExpr(pc=265,ComputationalTypeInt,UVar(defSites={67},value=an int),-,UVar(defSites={72},value=int = 2))),
	74: Assignment(pc=267,DVar(useSites={76},value=an int,origin=74),StaticFunctionCall(pc=267,java.util.concurrent.ConcurrentHashMap,isInterface=false,int resizeStamp(int),(UVar(defSites={0},value=int ∈ [0,2147483647])))),
	75: Assignment(pc=270,DVar(useSites={76},value=int = 16,origin=75),IntConst(pc=270,16)),
	76: Assignment(pc=272,DVar(useSites={77},value=an int,origin=76),BinaryExpr(pc=272,ComputationalTypeInt,UVar(defSites={74},value=an int),<<,UVar(defSites={75},value=int = 16))),
	77: If(pc=273,UVar(defSites={73},value=an int),==,UVar(defSites={76},value=an int),target=79),
	78: Return(pc=276),
	79: Assignment(pc=277,DVar(useSites={54,30,27},value=int = 1,origin=79),IntConst(pc=277,1)),
	80: Goto(pc=286,target=27),
	81: Assignment(pc=292,DVar(useSites={96,112,180,116,188,82,138,86,182,110,129,185,121,109,93,125,131,91,123,119,111},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦292;refId=313],origin=81),StaticFunctionCall(pc=292,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483646])))),
	82: If(pc=298,UVar(defSites={81},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦292;refId=313]),!=,NullExpr(pc=-333),target=86),
	83: Assignment(pc=304,DVar(useSites={84},value=null[↦304],origin=83),NullExpr(pc=304)),
	84: Assignment(pc=307,DVar(useSites={27},value=int ∈ [0,1],origin=84),StaticFunctionCall(pc=307,java.util.concurrent.ConcurrentHashMap,isInterface=false,boolean casTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483646]),UVar(defSites={83},value=null[↦304]),UVar(defSites={21},value=java.util.concurrent.ConcurrentHashMap$ForwardingNode[↦74;refId=109])))),
	85: Goto(pc=312,target=27),
	86: Assignment(pc=317,DVar(useSites={88,94,95},value=an int,origin=86),GetField(pc=317,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=313]))),
	87: Assignment(pc=323,DVar(useSites={88},value=int = -1,origin=87),IntConst(pc=323,-1)),
	88: If(pc=324,UVar(defSites={86},value=an int),!=,UVar(defSites={87},value=int = -1),target=91),
	89: Assignment(pc=327,DVar(useSites={27},value=int = 1,origin=89),IntConst(pc=327,1)),
	90: Goto(pc=330,target=27),
	91: MonitorEnter(pc=338,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=313])),
	92: Assignment(pc=342,DVar(useSites={93},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦342;refId=316],origin=92),StaticFunctionCall(pc=342,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node tabAt(java.util.concurrent.ConcurrentHashMap$Node[],int),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483646])))),
	93: If(pc=347,UVar(defSites={92},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦342;refId=316]),!=,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=313]),target=185),
	94: If(pc=352,UVar(defSites={86},value=an int),<,IntConst(pc=-333,0),target=129),
	95: Assignment(pc=358,DVar(useSites={104,100},value=int ∈ [0,2147483647],origin=95),BinaryExpr(pc=358,ComputationalTypeInt,UVar(defSites={86},value=int ∈ [0,2147483647]),&,UVar(defSites={0},value=int ∈ [1,2147483647]))),
	96: Assignment(pc=367,DVar(useSites={116,98,102,97,109,125,123,119},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=318],origin=96),GetField(pc=367,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=313]))),
	97: If(pc=374,UVar(defSites={96,102},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=225; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=216], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=224]»]),==,NullExpr(pc=-333),target=104),
	98: Assignment(pc=379,DVar(useSites={99},value=an int,origin=98),GetField(pc=379,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={96,102},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=225; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=216], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=224]»]))),
	99: Assignment(pc=383,DVar(useSites={104,100},value=int ∈ [0,2147483647],origin=99),BinaryExpr(pc=383,ComputationalTypeInt,UVar(defSites={98},value=an int),&,UVar(defSites={0},value=int ∈ [0,2147483647]))),
	100: If(pc=390,UVar(defSites={99},value=int ∈ [0,2147483647]),==,UVar(defSites={99,95},value=int ∈ [0,2147483647]),target=102),
	101: Nop(pc=393),
	102: Assignment(pc=403,DVar(useSites={116,98,97,109,125,123,103,119},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=224],origin=102),GetField(pc=403,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={96,102},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=179; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=152], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=159]»]))),
	103: Goto(pc=408,target=97),
	104: If(pc=413,UVar(defSites={99,95},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=107),
	105: Assignment(pc=420,DVar(useSites={125,119},value=null[↦420],origin=105),NullExpr(pc=420)),
	106: Goto(pc=423,target=108),
	107: Assignment(pc=430,DVar(useSites={116,123},value=null[↦430],origin=107),NullExpr(pc=430)),
	108: Nop(pc=433),
	109: If(pc=441,UVar(defSites={81,121},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=332; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦511;refId=331]»]),==,UVar(defSites={96,102,81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=333; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=159]»]),target=123),
	110: Assignment(pc=446,DVar(useSites={116,113,119},value=an int,origin=110),GetField(pc=446,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={81,121},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=332; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦511;refId=331]»]))),
	111: Assignment(pc=453,DVar(useSites={116,119},value={_ <: java.lang.Object, null}[↦453;refId=358],origin=111),GetField(pc=453,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={81,121},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=332; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦511;refId=331]»]))),
	112: Assignment(pc=460,DVar(useSites={116,119},value={_ <: java.lang.Object, null}[↦460;refId=359],origin=112),GetField(pc=460,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={81,121},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=332; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦511;refId=331]»]))),
	113: Assignment(pc=468,DVar(useSites={114},value=int ∈ [0,2147483647],origin=113),BinaryExpr(pc=468,ComputationalTypeInt,UVar(defSites={110},value=an int),&,UVar(defSites={0},value=int ∈ [0,2147483647]))),
	114: If(pc=469,UVar(defSites={113},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=118),
	115: Assignment(pc=472,DVar(useSites={116,123},value=java.util.concurrent.ConcurrentHashMap$Node[↦472;refId=360],origin=115),New(pc=472,java.util.concurrent.ConcurrentHashMap$Node)),
	116: NonVirtualMethodCall(pc=484,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.concurrent.ConcurrentHashMap$Node),UVar(defSites={115},value=java.util.concurrent.ConcurrentHashMap$Node[↦472;refId=360]),(UVar(defSites={110},value=an int),UVar(defSites={111},value={_ <: java.lang.Object, null}[↦453;refId=358]),UVar(defSites={112},value={_ <: java.lang.Object, null}[↦460;refId=359]),UVar(defSites={96,102,81,115,107},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=335; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], null[↦430], java.util.concurrent.ConcurrentHashMap$Node[↦472;refId=278], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=159]»]))),
	117: Goto(pc=489,target=121),
	118: Assignment(pc=492,DVar(useSites={125,119},value=java.util.concurrent.ConcurrentHashMap$Node[↦492;refId=366],origin=118),New(pc=492,java.util.concurrent.ConcurrentHashMap$Node)),
	119: NonVirtualMethodCall(pc=504,java.util.concurrent.ConcurrentHashMap$Node,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.concurrent.ConcurrentHashMap$Node),UVar(defSites={118},value=java.util.concurrent.ConcurrentHashMap$Node[↦492;refId=366]),(UVar(defSites={110},value=an int),UVar(defSites={111},value={_ <: java.lang.Object, null}[↦453;refId=358]),UVar(defSites={112},value={_ <: java.lang.Object, null}[↦460;refId=359]),UVar(defSites={96,102,118,81,105},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=334; values=«null[↦420], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], java.util.concurrent.ConcurrentHashMap$Node[↦492;refId=281], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=159]»]))),
	120: Nop(pc=507),
	121: Assignment(pc=511,DVar(useSites={112,122,110,109,111},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦511;refId=399],origin=121),GetField(pc=511,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={81,121},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=332; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦511;refId=331]»]))),
	122: Goto(pc=516,target=109),
	123: StaticMethodCall(pc=524,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={16,-3},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=108; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-3;refId=104], java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107]»]),UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483647]),UVar(defSites={96,102,81,115,107},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=335; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], null[↦430], java.util.concurrent.ConcurrentHashMap$Node[↦472;refId=278], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=159]»]))),
	124: Assignment(pc=531,DVar(useSites={125},value=an int,origin=124),BinaryExpr(pc=531,ComputationalTypeInt,UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483647]),+,UVar(defSites={0},value=int ∈ [0,2147483647]))),
	125: StaticMethodCall(pc=534,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={16,-3},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=108; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-3;refId=104], java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107]»]),UVar(defSites={124},value=an int),UVar(defSites={96,102,118,81,105},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=334; values=«null[↦420], _ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=114], java.util.concurrent.ConcurrentHashMap$Node[↦492;refId=281], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦367;refId=118], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦403;refId=159]»]))),
	126: StaticMethodCall(pc=542,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483647]),UVar(defSites={21},value=java.util.concurrent.ConcurrentHashMap$ForwardingNode[↦74;refId=109]))),
	127: Assignment(pc=545,DVar(useSites={27},value=int = 1,origin=127),IntConst(pc=545,1)),
	128: Goto(pc=548,target=185),
	129: Assignment(pc=553,DVar(useSites={130},value=int ∈ [0,1],origin=129),InstanceOf(pc=553,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=313]),java.util.concurrent.ConcurrentHashMap$TreeBin)),
	130: If(pc=556,UVar(defSites={129},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=185),
	131: Checkcast(pc=561,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=313]),java.util.concurrent.ConcurrentHashMap$TreeBin),
	132: Assignment(pc=566,DVar(useSites={168,164},value=null[↦566],origin=132),NullExpr(pc=566)),
	133: Assignment(pc=569,DVar(useSites={152,150,149},value=null[↦569],origin=133),NullExpr(pc=569)),
	134: Assignment(pc=572,DVar(useSites={177,173},value=null[↦572],origin=134),NullExpr(pc=572)),
	135: Assignment(pc=575,DVar(useSites={156,158,155},value=null[↦575],origin=135),NullExpr(pc=575)),
	136: Assignment(pc=578,DVar(useSites={153,163,175},value=int = 0,origin=136),IntConst(pc=578,0)),
	137: Assignment(pc=581,DVar(useSites={172,166,159},value=int = 0,origin=137),IntConst(pc=581,0)),
	138: Assignment(pc=586,DVar(useSites={160,140,142,139,143},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦586;refId=324],origin=138),GetField(pc=586,java.util.concurrent.ConcurrentHashMap$TreeBin,first,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={81},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦292;refId=321]))),
	139: If(pc=593,UVar(defSites={160,138},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=1432; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦586;refId=324], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦702;refId=1431]»]),==,NullExpr(pc=-333),target=162),
	140: Assignment(pc=598,DVar(useSites={146,147},value=an int,origin=140),GetField(pc=598,java.util.concurrent.ConcurrentHashMap$Node,hash,int,UVar(defSites={160,138},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=1432; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦586;refId=324], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦702;refId=1431]»]))),
	141: Assignment(pc=603,DVar(useSites={168,152,164,156,146,150,158,177,149,173,155},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1437],origin=141),New(pc=603,java.util.concurrent.ConcurrentHashMap$TreeNode)),
	142: Assignment(pc=611,DVar(useSites={146},value={_ <: java.lang.Object, null}[↦611;refId=1438],origin=142),GetField(pc=611,java.util.concurrent.ConcurrentHashMap$Node,key,java.lang.Object,UVar(defSites={160,138},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=1432; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦586;refId=324], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦702;refId=1431]»]))),
	143: Assignment(pc=616,DVar(useSites={146},value={_ <: java.lang.Object, null}[↦616;refId=1439],origin=143),GetField(pc=616,java.util.concurrent.ConcurrentHashMap$Node,val,java.lang.Object,UVar(defSites={160,138},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=1432; values=«{java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦586;refId=324], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦702;refId=1431]»]))),
	144: Assignment(pc=619,DVar(useSites={146},value=null[↦619],origin=144),NullExpr(pc=619)),
	145: Assignment(pc=620,DVar(useSites={146},value=null[↦620],origin=145),NullExpr(pc=620)),
	146: NonVirtualMethodCall(pc=621,java.util.concurrent.ConcurrentHashMap$TreeNode,isInterface=false,void <init>(int,java.lang.Object,java.lang.Object,java.util.concurrent.ConcurrentHashMap$Node,java.util.concurrent.ConcurrentHashMap$TreeNode),UVar(defSites={141},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1437]),(UVar(defSites={140},value=an int),UVar(defSites={142},value={_ <: java.lang.Object, null}[↦611;refId=1438]),UVar(defSites={143},value={_ <: java.lang.Object, null}[↦616;refId=1439]),UVar(defSites={144},value=null[↦619]),UVar(defSites={145},value=null[↦620]))),
	147: Assignment(pc=629,DVar(useSites={148},value=int ∈ [0,2147483647],origin=147),BinaryExpr(pc=629,ComputationalTypeInt,UVar(defSites={140},value=an int),&,UVar(defSites={0},value=int ∈ [0,2147483647]))),
	148: If(pc=630,UVar(defSites={147},value=int ∈ [0,2147483647]),!=,IntConst(pc=-333,0),target=155),
	149: PutField(pc=638,java.util.concurrent.ConcurrentHashMap$TreeNode,prev,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={141},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1437]),UVar(defSites={133,141},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=340; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=137], null[↦569]»])),
	150: If(pc=641,UVar(defSites={133,141},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=340; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=137], null[↦569]»]),!=,NullExpr(pc=-333),target=152),
	151: Goto(pc=648,target=153),
	152: PutField(pc=655,java.util.concurrent.ConcurrentHashMap$TreeNode,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={133,141},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=137]),UVar(defSites={141},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1437])),
	153: Assignment(pc=662,DVar(useSites={154,163,175},value=an int,origin=153),BinaryExpr(pc=662,ComputationalTypeInt,UVar(defSites={136,153},value=an int),+,IntConst(pc=662,1))),
	154: Goto(pc=665,target=160),
	155: PutField(pc=673,java.util.concurrent.ConcurrentHashMap$TreeNode,prev,java.util.concurrent.ConcurrentHashMap$TreeNode,UVar(defSites={141},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1437]),UVar(defSites={141,135},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=1433; values=«null[↦575], java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1378]»])),
	156: If(pc=676,UVar(defSites={141,135},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=1433; values=«null[↦575], java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1378]»]),!=,NullExpr(pc=-333),target=158),
	157: Goto(pc=683,target=159),
	158: PutField(pc=690,java.util.concurrent.ConcurrentHashMap$TreeNode,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={141,135},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1378]),UVar(defSites={141},value=java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=1437])),
	159: Assignment(pc=697,DVar(useSites={160,172,166},value=an int,origin=159),BinaryExpr(pc=697,ComputationalTypeInt,UVar(defSites={137,159},value=an int),+,IntConst(pc=697,1))),
	160: Assignment(pc=702,DVar(useSites={140,142,161,139,143},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦702;refId=1431],origin=160),GetField(pc=702,java.util.concurrent.ConcurrentHashMap$Node,next,java.util.concurrent.ConcurrentHashMap$Node,UVar(defSites={160,138},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[refId=1410; values=«{_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦702;refId=1372], {java.util.concurrent.ConcurrentHashMap$TreeNode, null}[↦586;refId=324]»]))),
	161: Goto(pc=707,target=139),
	162: Assignment(pc=712,DVar(useSites={163},value=int = 6,origin=162),IntConst(pc=712,6)),
	163: If(pc=714,UVar(defSites={136,153},value=an int),>,UVar(defSites={162},value=int = 6),target=166),
	164: Assignment(pc=719,DVar(useSites={180},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦719;refId=1465],origin=164),StaticFunctionCall(pc=719,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node untreeify(java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={132,141},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=341; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=137], null[↦566]»])))),
	165: Goto(pc=722,target=171),
	166: If(pc=727,UVar(defSites={137,159},value=an int),==,IntConst(pc=-333,0),target=170),
	167: Assignment(pc=730,DVar(useSites={168,180},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦730;refId=1458],origin=167),New(pc=730,java.util.concurrent.ConcurrentHashMap$TreeBin)),
	168: NonVirtualMethodCall(pc=736,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,void <init>(java.util.concurrent.ConcurrentHashMap$TreeNode),UVar(defSites={167},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦730;refId=1458]),(UVar(defSites={132,141},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=341; values=«java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=137], null[↦566]»]))),
	169: Goto(pc=739,target=171),
	170: Nop(pc=742),
	171: Assignment(pc=748,DVar(useSites={172},value=int = 6,origin=171),IntConst(pc=748,6)),
	172: If(pc=750,UVar(defSites={137,159},value=an int),>,UVar(defSites={171},value=int = 6),target=175),
	173: Assignment(pc=755,DVar(useSites={182},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦755;refId=1486],origin=173),StaticFunctionCall(pc=755,java.util.concurrent.ConcurrentHashMap,isInterface=false,java.util.concurrent.ConcurrentHashMap$Node untreeify(java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={134,141},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=163; values=«null[↦572], java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=137]»])))),
	174: Goto(pc=758,target=180),
	175: If(pc=763,UVar(defSites={136,153},value=an int),==,IntConst(pc=-333,0),target=179),
	176: Assignment(pc=766,DVar(useSites={182,177},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦766;refId=1479],origin=176),New(pc=766,java.util.concurrent.ConcurrentHashMap$TreeBin)),
	177: NonVirtualMethodCall(pc=772,java.util.concurrent.ConcurrentHashMap$TreeBin,isInterface=false,void <init>(java.util.concurrent.ConcurrentHashMap$TreeNode),UVar(defSites={176},value=java.util.concurrent.ConcurrentHashMap$TreeBin[↦766;refId=1479]),(UVar(defSites={134,141},value={java.util.concurrent.ConcurrentHashMap$TreeNode, null}[refId=163; values=«null[↦572], java.util.concurrent.ConcurrentHashMap$TreeNode[↦603;refId=137]»]))),
	178: Goto(pc=775,target=180),
	179: Nop(pc=778),
	180: StaticMethodCall(pc=787,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={16,-3},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=108; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-3;refId=104], java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107]»]),UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483647]),UVar(defSites={164,81,167},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=648; values=«java.util.concurrent.ConcurrentHashMap$TreeBin[↦730;refId=620], java.util.concurrent.ConcurrentHashMap$TreeBin[↦292;refId=219], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦719;refId=628]»]))),
	181: Assignment(pc=794,DVar(useSites={182},value=an int,origin=181),BinaryExpr(pc=794,ComputationalTypeInt,UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483647]),+,UVar(defSites={0},value=int ∈ [0,2147483647]))),
	182: StaticMethodCall(pc=797,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={16,-3},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][refId=108; values=«_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-3;refId=104], java.util.concurrent.ConcurrentHashMap$Node[][↦40;refId=107]»]),UVar(defSites={181},value=an int),UVar(defSites={176,81,173},value={_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[refId=654; values=«java.util.concurrent.ConcurrentHashMap$TreeBin[↦766;refId=644], java.util.concurrent.ConcurrentHashMap$TreeBin[↦292;refId=219], {_ <: java.util.concurrent.ConcurrentHashMap$Node, null}[↦755;refId=652]»]))),
	183: StaticMethodCall(pc=805,java.util.concurrent.ConcurrentHashMap,isInterface=false,void setTabAt(java.util.concurrent.ConcurrentHashMap$Node[],int,java.util.concurrent.ConcurrentHashMap$Node),(UVar(defSites={-2},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[][↦-2;refId=103]),UVar(defSites={0,28,25,35,47},value=int ∈ [0,2147483647]),UVar(defSites={21},value=java.util.concurrent.ConcurrentHashMap$ForwardingNode[↦74;refId=109]))),
	184: Assignment(pc=808,DVar(useSites={27},value=int = 1,origin=184),IntConst(pc=808,1)),
	185: MonitorExit(pc=813,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=211])),
	186: Goto(pc=814,target=27),
	187: CaughtException(pc=817,<ANY>,caused by={exception@168,exception[VM]@188,exception@92,exception@180,exception@116,exception@164,exception@126,exception[VM]@110,exception@182,exception@146,exception@183,exception@119,exception@123,exception[VM]@131,exception@125,exception@173,exception[VM]@185,exception@177}),
	188: MonitorExit(pc=821,UVar(defSites={81},value=_ <: java.util.concurrent.ConcurrentHashMap$Node[↦292;refId=219])),
	189: Throw(pc=824,UVar(defSites={-1000168,-100188,-1000092,-1000180,-1000116,-1000164,-1000126,-100110,-1000182,-1000146,-1000183,-1000119,-1000123,-100131,-1000125,-1000173,-100185,-1000177},value=_ <: java.lang.Throwable[refId=653; values=«_ <: java.lang.Throwable[↦-1000342;refId=315], _ <: java.lang.Throwable[↦-1000534;refId=352], _ <: java.lang.Throwable[↦-1000524;refId=350], _ <: java.lang.Throwable[↦-1000504;refId=367], _ <: java.lang.Throwable[↦-1000736;refId=621], _ <: java.lang.Throwable[↦-1000484;refId=361], _ <: java.lang.Throwable[↦-1000772;refId=645], _ <: java.lang.Throwable[↦-1000542;refId=354], java.lang.NullPointerException[↦-100446;refId=356], _ <: java.lang.Throwable[↦-1000787;refId=292], _ <: java.lang.Throwable[↦-1000719;refId=627], _ <: java.lang.Throwable[↦-1000755;refId=651], java.lang.IllegalMonitorStateException[↦-100813;refId=236], _ <: java.lang.Throwable[↦-1000797;refId=294], _ <: java.lang.Throwable[↦-1000621;refId=602], _ <: java.lang.Throwable[↦-1000805;refId=296], java.lang.IllegalMonitorStateException[↦-100821;refId=642], java.lang.ClassCastException[↦-100561;refId=322]»])),
	190: Goto(pc=825,target=27)
),cfg=CFG(
	BB_0: BasicBlock(start=105,end=106) -> {BB_44}
	BB_10: BasicBlock(start=189,end=189) -> {BB_65}
	BB_11: BasicBlock(start=20,end=22) -> {BB_65,BB_57}
	BB_12: BasicBlock(start=46,end=49) -> {BB_37}
	BB_13: BasicBlock(start=93,end=93) -> {BB_64,BB_a}
	BB_14: BasicBlock(start=152,end=152) -> {BB_8}
	BB_15: BasicBlock(start=78,end=78) -> {BB_4a,BB_65}
	BB_16: BasicBlock(start=164,end=164) -> {BB_21,BB_27}
	BB_17: BasicBlock(start=179,end=179) -> {BB_32}
	BB_18: BasicBlock(start=121,end=122) -> {BB_2a}
	BB_19: BasicBlock(start=147,end=148) -> {BB_43,BB_33}
	BB_1: BasicBlock(start=104,end=104) -> {BB_0,BB_60}
	BB_1a: BasicBlock(start=132,end=138) -> {BB_56}
	BB_1b: BasicBlock(start=89,end=90) -> {BB_37}
	BB_1c: BasicBlock(start=1,end=3) -> {BB_28,BB_61}
	BB_1d: BasicBlock(start=117,end=117) -> {BB_18}
	BB_1e: BasicBlock(start=85,end=85) -> {BB_37}
	BB_1f: BasicBlock(start=102,end=103) -> {BB_26}
	BB_20: BasicBlock(start=160,end=161) -> {BB_56}
	BB_21: BasicBlock(start=165,end=165) -> {BB_55}
	BB_22: BasicBlock(start=33,end=34) -> {BB_46,BB_24}
	BB_23: BasicBlock(start=28,end=29) -> {BB_4e,BB_5c}
	BB_24: BasicBlock(start=38,end=40) -> {BB_51,BB_2f}
	BB_25: BasicBlock(start=65,end=70) -> {BB_65,BB_38}
	BB_26: BasicBlock(start=97,end=97) -> {BB_40,BB_1}
	BB_27: CatchNode([-1,186)=>187,<none>) -> {BB_3e}
	BB_28: BasicBlock(start=9,end=9) -> {BB_7}
	BB_29: BasicBlock(start=169,end=169) -> {BB_55}
	BB_2: BasicBlock(start=101,end=101) -> {BB_1f}
	BB_2a: BasicBlock(start=109,end=109) -> {BB_e,BB_48}
	BB_2b: BasicBlock(start=124,end=125) -> {BB_62,BB_27}
	BB_2c: BasicBlock(start=173,end=173) -> {BB_9,BB_27}
	BB_2d: BasicBlock(start=13,end=13) -> {BB_11,BB_c}
	BB_2e: BasicBlock(start=129,end=130) -> {BB_a,BB_66}
	BB_2f: BasicBlock(start=41,end=42) -> {BB_35}
	BB_30: BasicBlock(start=166,end=166) -> {BB_45,BB_4}
	BB_31: BasicBlock(start=45,end=45) -> {BB_37,BB_12}
	BB_32: BasicBlock(start=180,end=180) -> {BB_3b,BB_27}
	BB_33: BasicBlock(start=149,end=150) -> {BB_5b,BB_14}
	BB_34: BasicBlock(start=176,end=177) -> {BB_67,BB_27}
	BB_35: BasicBlock(start=44,end=44) -> {BB_65,BB_31}
	BB_36: BasicBlock(start=118,end=119) -> {BB_6,BB_27}
	BB_37: BasicBlock(start=27,end=27) -> {BB_23,BB_4c}
	BB_38: BasicBlock(start=71,end=71) -> {BB_4f,BB_5e}
	BB_39: BasicBlock(start=12,end=12) -> {BB_2d}
	BB_3: BasicBlock(start=0,end=0) -> {BB_65,BB_1c}
	BB_3a: BasicBlock(start=54,end=54) -> {BB_54,BB_25}
	BB_3b: BasicBlock(start=181,end=182) -> {BB_5f,BB_27}
	BB_3c: BasicBlock(start=86,end=88) -> {BB_42,BB_1b}
	BB_3d: BasicBlock(start=159,end=159) -> {BB_20}
	BB_3e: BasicBlock(start=187,end=188) -> {BB_10,BB_27}
	BB_3f: BasicBlock(start=81,end=81) -> {BB_65,BB_5a}
	BB_40: BasicBlock(start=98,end=100) -> {BB_1f,BB_2}
	BB_41: BasicBlock(start=140,end=146) -> {BB_19,BB_27}
	BB_42: BasicBlock(start=91,end=92) -> {BB_13,BB_27}
	BB_43: BasicBlock(start=155,end=156) -> {BB_52,BB_f}
	BB_44: BasicBlock(start=108,end=108) -> {BB_2a}
	BB_45: BasicBlock(start=167,end=168) -> {BB_29,BB_27}
	BB_46: BasicBlock(start=35,end=37) -> {BB_37}
	BB_47: BasicBlock(start=162,end=163) -> {BB_30,BB_16}
	BB_48: BasicBlock(start=123,end=123) -> {BB_2b,BB_27}
	BB_49: BasicBlock(start=18,end=19) -> {BB_11}
	BB_4: BasicBlock(start=170,end=170) -> {BB_55}
	BB_4a: ExitNode(normalReturn=true)
	BB_4b: BasicBlock(start=95,end=96) -> {BB_26}
	BB_4c: BasicBlock(start=50,end=50) -> {BB_5d,BB_3a}
	BB_4d: BasicBlock(start=127,end=128) -> {BB_a}
	BB_4e: BasicBlock(start=31,end=32) -> {BB_37}
	BB_4f: BasicBlock(start=72,end=74) -> {BB_65,BB_59}
	BB_50: BasicBlock(start=175,end=175) -> {BB_17,BB_34}
	BB_51: BasicBlock(start=43,end=43) -> {BB_35}
	BB_52: BasicBlock(start=158,end=158) -> {BB_3d}
	BB_53: BasicBlock(start=186,end=186) -> {BB_37}
	BB_54: BasicBlock(start=55,end=64) -> {BB_4a,BB_65}
	BB_55: BasicBlock(start=171,end=172) -> {BB_2c,BB_50}
	BB_56: BasicBlock(start=139,end=139) -> {BB_41,BB_47}
	BB_57: BasicBlock(start=23,end=26) -> {BB_37}
	BB_58: BasicBlock(start=8,end=8) -> {BB_7}
	BB_59: BasicBlock(start=75,end=77) -> {BB_15,BB_63}
	BB_5: BasicBlock(start=115,end=116) -> {BB_1d,BB_27}
	BB_5a: BasicBlock(start=82,end=82) -> {BB_69,BB_3c}
	BB_5b: BasicBlock(start=151,end=151) -> {BB_8}
	BB_5c: BasicBlock(start=30,end=30) -> {BB_4e,BB_22}
	BB_5d: BasicBlock(start=51,end=51) -> {BB_b,BB_3a}
	BB_5e: BasicBlock(start=190,end=190) -> {BB_37}
	BB_5f: BasicBlock(start=183,end=183) -> {BB_d,BB_27}
	BB_60: BasicBlock(start=107,end=107) -> {BB_44}
	BB_61: BasicBlock(start=4,end=7) -> {BB_65,BB_58}
	BB_62: BasicBlock(start=126,end=126) -> {BB_4d,BB_27}
	BB_63: BasicBlock(start=79,end=80) -> {BB_37}
	BB_64: BasicBlock(start=94,end=94) -> {BB_4b,BB_2e}
	BB_65: ExitNode(normalReturn=false)
	BB_66: BasicBlock(start=131,end=131) -> {BB_1a,BB_27}
	BB_67: BasicBlock(start=178,end=178) -> {BB_32}
	BB_68: BasicBlock(start=111,end=114) -> {BB_5,BB_36}
	BB_69: BasicBlock(start=83,end=84) -> {BB_65,BB_1e}
	BB_6: BasicBlock(start=120,end=120) -> {BB_18}
	BB_7: BasicBlock(start=10,end=11) -> {BB_2d,BB_39}
	BB_8: BasicBlock(start=153,end=154) -> {BB_20}
	BB_9: BasicBlock(start=174,end=174) -> {BB_32}
	BB_a: BasicBlock(start=185,end=185) -> {BB_53,BB_27}
	BB_b: BasicBlock(start=52,end=53) -> {BB_3f,BB_3a}
	BB_c: BasicBlock(start=14,end=17) -> {BB_49}
	BB_d: BasicBlock(start=184,end=184) -> {BB_a}
	BB_e: BasicBlock(start=110,end=110) -> {BB_68,BB_27}
	BB_f: BasicBlock(start=157,end=157) -> {BB_3d}
),exceptionHandlers=(
	ExceptionHandler([14, 17) -> -1, java.lang.Throwable),
	ExceptionHandler([-1, 186) -> 187, <FINALLY>),
	ExceptionHandler([187, 189) -> 187, <FINALLY>)
))

void fullAddCount(long,boolean)
AITACode(params=(Parameters(
	0: useSites={96,40,88,68,84,76,44,28,82,114,74,6,102,94,129,105,25,121,117,19,59,15,127} (origin=-1),
	1: useSites={128,112,56,18} (origin=-2),
	2: useSites={50} (origin=-3)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={12,92,34,110,1},value=an int,origin=0),StaticFunctionCall(pc=0,java.util.concurrent.ThreadLocalRandom,isInterface=false,int getProbe(),())),
	1: If(pc=6,UVar(defSites={0},value=an int),!=,IntConst(pc=-333,0),target=5),
	2: StaticMethodCall(pc=9,java.util.concurrent.ThreadLocalRandom,isInterface=false,void localInit(),()),
	3: Assignment(pc=12,DVar(useSites={12,92,34,110},value=an int,origin=3),StaticFunctionCall(pc=12,java.util.concurrent.ThreadLocalRandom,isInterface=false,int getProbe(),())),
	4: Assignment(pc=17,DVar(useSites={50},value=int = 1,origin=4),IntConst(pc=17,1)),
	5: Assignment(pc=19,DVar(useSites={65},value=int = 0,origin=5),IntConst(pc=19,0)),
	6: Assignment(pc=23,DVar(useSites={80,8,60,106,97,13,77,7},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦23;refId=135],origin=6),GetField(pc=23,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	7: If(pc=29,UVar(defSites={6},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦23;refId=135]),==,NullExpr(pc=-333),target=94),
	8: Assignment(pc=34,DVar(useSites={62,9,11,79},value=int ∈ [0,2147483647],origin=8),ArrayLength(pc=34,UVar(defSites={6},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦23;refId=135]))),
	9: If(pc=38,UVar(defSites={8},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=94),
	10: Assignment(pc=45,DVar(useSites={11},value=int = 1,origin=10),IntConst(pc=45,1)),
	11: Assignment(pc=46,DVar(useSites={12},value=int ∈ [0,2147483646],origin=11),BinaryExpr(pc=46,ComputationalTypeInt,UVar(defSites={8},value=int ∈ [1,2147483647]),-,UVar(defSites={10},value=int = 1))),
	12: Assignment(pc=49,DVar(useSites={13},value=int ∈ [0,2147483646],origin=12),BinaryExpr(pc=49,ComputationalTypeInt,UVar(defSites={11},value=int ∈ [0,2147483646]),&,UVar(defSites={0,92,3},value=an int))),
	13: Assignment(pc=50,DVar(useSites={14,57,55},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦50;refId=137],origin=13),ArrayLoad(pc=50,UVar(defSites={12},value=int ∈ [0,2147483646]),UVar(defSites={6},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦23;refId=135]))),
	14: If(pc=54,UVar(defSites={13},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦50;refId=137]),!=,NullExpr(pc=-333),target=50),
	15: Assignment(pc=58,DVar(useSites={16},value=an int,origin=15),GetField(pc=58,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	16: If(pc=61,UVar(defSites={15},value=an int),!=,IntConst(pc=-333,0),target=48),
	17: Assignment(pc=64,DVar(useSites={18,37},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦64;refId=138],origin=17),New(pc=64,java.util.concurrent.ConcurrentHashMap$CounterCell)),
	18: NonVirtualMethodCall(pc=69,java.util.concurrent.ConcurrentHashMap$CounterCell,isInterface=false,void <init>(long),UVar(defSites={17},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦64;refId=138]),(UVar(defSites={-2},value=ALongValue))),
	19: Assignment(pc=75,DVar(useSites={20},value=an int,origin=19),GetField(pc=75,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	20: If(pc=78,UVar(defSites={19},value=an int),!=,IntConst(pc=-333,0),target=48),
	21: Assignment(pc=81,DVar(useSites={25},value={jdk.internal.misc.Unsafe, null}[↦81;refId=140],origin=21),GetStatic(pc=81,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	22: Assignment(pc=85,DVar(useSites={25},value=ALongValue,origin=22),GetStatic(pc=85,java.util.concurrent.ConcurrentHashMap,CELLSBUSY,long)),
	23: Assignment(pc=88,DVar(useSites={25},value=int = 0,origin=23),IntConst(pc=88,0)),
	24: Assignment(pc=89,DVar(useSites={25},value=int = 1,origin=24),IntConst(pc=89,1)),
	25: Assignment(pc=90,DVar(useSites={26},value=int ∈ [0,1],origin=25),VirtualFunctionCall(pc=90,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={21},value={jdk.internal.misc.Unsafe, null}[↦81;refId=140]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={22},value=ALongValue),UVar(defSites={23},value=int = 0),UVar(defSites={24},value=int = 1)))),
	26: If(pc=93,UVar(defSites={25},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=48),
	27: Assignment(pc=96,DVar(useSites={46},value=int = 0,origin=27),IntConst(pc=96,0)),
	28: Assignment(pc=100,DVar(useSites={30,37,29,35},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦100;refId=143],origin=28),GetField(pc=100,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	29: If(pc=106,UVar(defSites={28},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦100;refId=143]),==,NullExpr(pc=-333),target=39),
	30: Assignment(pc=111,DVar(useSites={33,31},value=int ∈ [0,2147483647],origin=30),ArrayLength(pc=111,UVar(defSites={28},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦100;refId=143]))),
	31: If(pc=115,UVar(defSites={30},value=int ∈ [0,2147483647]),<=,IntConst(pc=-333,0),target=39),
	32: Assignment(pc=122,DVar(useSites={33},value=int = 1,origin=32),IntConst(pc=122,1)),
	33: Assignment(pc=123,DVar(useSites={34},value=int ∈ [0,2147483646],origin=33),BinaryExpr(pc=123,ComputationalTypeInt,UVar(defSites={30},value=int ∈ [1,2147483647]),-,UVar(defSites={32},value=int = 1))),
	34: Assignment(pc=126,DVar(useSites={37,35},value=int ∈ [0,2147483646],origin=34),BinaryExpr(pc=126,ComputationalTypeInt,UVar(defSites={33},value=int ∈ [0,2147483646]),&,UVar(defSites={0,92,3},value=an int))),
	35: Assignment(pc=130,DVar(useSites={36},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦130;refId=145],origin=35),ArrayLoad(pc=130,UVar(defSites={34},value=int ∈ [0,2147483646]),UVar(defSites={28},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦100;refId=143]))),
	36: If(pc=131,UVar(defSites={35},value={java.util.concurrent.ConcurrentHashMap$CounterCell, null}[↦130;refId=145]),!=,NullExpr(pc=-333),target=39),
	37: ArrayStore(pc=140,UVar(defSites={28},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦100;refId=143]),UVar(defSites={34},value=int ∈ [0,2147483646]),UVar(defSites={17},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦64;refId=138])),
	38: Assignment(pc=141,DVar(useSites={46},value=int = 1,origin=38),IntConst(pc=141,1)),
	39: Assignment(pc=145,DVar(useSites={40},value=int = 0,origin=39),IntConst(pc=145,0)),
	40: PutField(pc=146,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={39},value=int = 0)),
	41: Goto(pc=149,target=46),
	42: CaughtException(pc=152,<ANY>,caused by={exception[VM]@35,exception[VM]@37}),
	43: Assignment(pc=155,DVar(useSites={44},value=int = 0,origin=43),IntConst(pc=155,0)),
	44: PutField(pc=156,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={43},value=int = 0)),
	45: Throw(pc=161,UVar(defSites={-100035,-100037},value=java.lang.ArrayIndexOutOfBoundsException[refId=118; values=«java.lang.ArrayIndexOutOfBoundsException[↦-100130;refId=115], java.lang.ArrayIndexOutOfBoundsException[↦-100140;refId=117]»])),
	46: If(pc=164,UVar(defSites={38,27},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=6),
	47: Goto(pc=167,target=132),
	48: Assignment(pc=170,DVar(useSites={65},value=int = 0,origin=48),IntConst(pc=170,0)),
	49: Goto(pc=173,target=92),
	50: If(pc=177,UVar(defSites={4,-3,51},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=53),
	51: Assignment(pc=180,DVar(useSites={50},value=int = 1,origin=51),IntConst(pc=180,1)),
	52: Goto(pc=182,target=92),
	53: Assignment(pc=185,DVar(useSites={57},value={jdk.internal.misc.Unsafe, null}[↦185;refId=149],origin=53),GetStatic(pc=185,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	54: Assignment(pc=190,DVar(useSites={57},value=ALongValue,origin=54),GetStatic(pc=190,java.util.concurrent.ConcurrentHashMap,CELLVALUE,long)),
	55: Assignment(pc=195,DVar(useSites={56,57},value=ALongValue,origin=55),GetField(pc=195,java.util.concurrent.ConcurrentHashMap$CounterCell,value,long,UVar(defSites={13},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦50;refId=137]))),
	56: Assignment(pc=204,DVar(useSites={57},value=ALongValue,origin=56),BinaryExpr(pc=204,ComputationalTypeLong,UVar(defSites={55},value=ALongValue),+,UVar(defSites={-2},value=ALongValue))),
	57: Assignment(pc=205,DVar(useSites={58},value=int ∈ [0,1],origin=57),VirtualFunctionCall(pc=205,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetLong(java.lang.Object,long,long,long),UVar(defSites={53},value={jdk.internal.misc.Unsafe, null}[↦185;refId=149]),(UVar(defSites={13},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦50;refId=137]),UVar(defSites={54},value=ALongValue),UVar(defSites={55},value=ALongValue),UVar(defSites={56},value=ALongValue)))),
	58: If(pc=208,UVar(defSites={57},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=132),
	59: Assignment(pc=215,DVar(useSites={60},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦215;refId=152],origin=59),GetField(pc=215,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	60: If(pc=220,UVar(defSites={59},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦215;refId=152]),!=,UVar(defSites={6},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦23;refId=135]),target=63),
	61: Assignment(pc=225,DVar(useSites={62},value=an int,origin=61),GetStatic(pc=225,java.util.concurrent.ConcurrentHashMap,NCPU,int)),
	62: If(pc=228,UVar(defSites={8},value=int ∈ [1,2147483647]),<,UVar(defSites={61},value=an int),target=65),
	63: Assignment(pc=231,DVar(useSites={65},value=int = 0,origin=63),IntConst(pc=231,0)),
	64: Goto(pc=234,target=92),
	65: If(pc=239,UVar(defSites={48,66,90,5,63},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=68),
	66: Assignment(pc=242,DVar(useSites={65},value=int = 1,origin=66),IntConst(pc=242,1)),
	67: Goto(pc=245,target=92),
	68: Assignment(pc=249,DVar(useSites={69},value=an int,origin=68),GetField(pc=249,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	69: If(pc=252,UVar(defSites={68},value=an int),!=,IntConst(pc=-333,0),target=92),
	70: Assignment(pc=255,DVar(useSites={74},value={jdk.internal.misc.Unsafe, null}[↦255;refId=153],origin=70),GetStatic(pc=255,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	71: Assignment(pc=259,DVar(useSites={74},value=ALongValue,origin=71),GetStatic(pc=259,java.util.concurrent.ConcurrentHashMap,CELLSBUSY,long)),
	72: Assignment(pc=262,DVar(useSites={74},value=int = 0,origin=72),IntConst(pc=262,0)),
	73: Assignment(pc=263,DVar(useSites={74},value=int = 1,origin=73),IntConst(pc=263,1)),
	74: Assignment(pc=264,DVar(useSites={75},value=int ∈ [0,1],origin=74),VirtualFunctionCall(pc=264,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={70},value={jdk.internal.misc.Unsafe, null}[↦255;refId=153]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={71},value=ALongValue),UVar(defSites={72},value=int = 0),UVar(defSites={73},value=int = 1)))),
	75: If(pc=267,UVar(defSites={74},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=92),
	76: Assignment(pc=271,DVar(useSites={77},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦271;refId=156],origin=76),GetField(pc=271,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	77: If(pc=276,UVar(defSites={76},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦271;refId=156]),!=,UVar(defSites={6},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦23;refId=135]),target=83),
	78: Assignment(pc=284,DVar(useSites={79},value=int = 1,origin=78),IntConst(pc=284,1)),
	79: Assignment(pc=285,DVar(useSites={80},value=int ∈ [-2147483646,2147483646],origin=79),BinaryExpr(pc=285,ComputationalTypeInt,UVar(defSites={8},value=int ∈ [1,2147483646]),<<,UVar(defSites={78},value=int = 1))),
	80: Assignment(pc=286,DVar(useSites={82,81},value={_ <: java.lang.Object[], null}[↦286;refId=158],origin=80),StaticFunctionCall(pc=286,java.util.Arrays,isInterface=false,java.lang.Object[] copyOf(java.lang.Object[],int),(UVar(defSites={6},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦23;refId=135]),UVar(defSites={79},value=int ∈ [-2147483646,2147483646])))),
	81: Checkcast(pc=289,UVar(defSites={80},value={_ <: java.lang.Object[], null}[↦286;refId=158]),java.util.concurrent.ConcurrentHashMap$CounterCell[]),
	82: PutField(pc=292,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={80},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦286;refId=158])),
	83: Assignment(pc=296,DVar(useSites={84},value=int = 0,origin=83),IntConst(pc=296,0)),
	84: PutField(pc=297,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={83},value=int = 0)),
	85: Goto(pc=300,target=90),
	86: CaughtException(pc=303,<ANY>,caused by={exception@80,exception[VM]@81}),
	87: Assignment(pc=306,DVar(useSites={88},value=int = 0,origin=87),IntConst(pc=306,0)),
	88: PutField(pc=307,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={87},value=int = 0)),
	89: Throw(pc=312,UVar(defSites={-1000080,-100081},value=_ <: java.lang.Throwable[refId=160; values=«_ <: java.lang.Throwable[↦-1000286;refId=157], java.lang.ClassCastException[↦-100289;refId=159]»])),
	90: Assignment(pc=313,DVar(useSites={65},value=int = 0,origin=90),IntConst(pc=313,0)),
	91: Goto(pc=316,target=6),
	92: Assignment(pc=321,DVar(useSites={12,34,110,93},value=an int,origin=92),StaticFunctionCall(pc=321,java.util.concurrent.ThreadLocalRandom,isInterface=false,int advanceProbe(int),(UVar(defSites={0,92,3},value=an int)))),
	93: Goto(pc=326,target=6),
	94: Assignment(pc=330,DVar(useSites={95},value=an int,origin=94),GetField(pc=330,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	95: If(pc=333,UVar(defSites={94},value=an int),!=,IntConst(pc=-333,0),target=125),
	96: Assignment(pc=337,DVar(useSites={97},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦337;refId=161],origin=96),GetField(pc=337,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	97: If(pc=342,UVar(defSites={96},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦337;refId=161]),!=,UVar(defSites={6},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦23;refId=135]),target=125),
	98: Assignment(pc=345,DVar(useSites={102},value={jdk.internal.misc.Unsafe, null}[↦345;refId=162],origin=98),GetStatic(pc=345,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	99: Assignment(pc=349,DVar(useSites={102},value=ALongValue,origin=99),GetStatic(pc=349,java.util.concurrent.ConcurrentHashMap,CELLSBUSY,long)),
	100: Assignment(pc=352,DVar(useSites={102},value=int = 0,origin=100),IntConst(pc=352,0)),
	101: Assignment(pc=353,DVar(useSites={102},value=int = 1,origin=101),IntConst(pc=353,1)),
	102: Assignment(pc=354,DVar(useSites={103},value=int ∈ [0,1],origin=102),VirtualFunctionCall(pc=354,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetInt(java.lang.Object,long,int,int),UVar(defSites={98},value={jdk.internal.misc.Unsafe, null}[↦345;refId=162]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={99},value=ALongValue),UVar(defSites={100},value=int = 0),UVar(defSites={101},value=int = 1)))),
	103: If(pc=357,UVar(defSites={102},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=125),
	104: Assignment(pc=360,DVar(useSites={123},value=int = 0,origin=104),IntConst(pc=360,0)),
	105: Assignment(pc=364,DVar(useSites={106},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦364;refId=165],origin=105),GetField(pc=364,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	106: If(pc=369,UVar(defSites={105},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦364;refId=165]),!=,UVar(defSites={6},value={java.util.concurrent.ConcurrentHashMap$CounterCell[], null}[↦23;refId=135]),target=116),
	107: Assignment(pc=372,DVar(useSites={108},value=int = 2,origin=107),IntConst(pc=372,2)),
	108: Assignment(pc=373,DVar(useSites={114,113},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦373;refId=166;length=2],origin=108),NewArray(pc=373,[UVar(defSites={107},value=int = 2)],java.util.concurrent.ConcurrentHashMap$CounterCell[])),
	109: Assignment(pc=382,DVar(useSites={110},value=int = 1,origin=109),IntConst(pc=382,1)),
	110: Assignment(pc=383,DVar(useSites={113},value=int ∈ [0,1],origin=110),BinaryExpr(pc=383,ComputationalTypeInt,UVar(defSites={0,92,3},value=an int),&,UVar(defSites={109},value=int = 1))),
	111: Assignment(pc=384,DVar(useSites={112,113},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦384;refId=167],origin=111),New(pc=384,java.util.concurrent.ConcurrentHashMap$CounterCell)),
	112: NonVirtualMethodCall(pc=389,java.util.concurrent.ConcurrentHashMap$CounterCell,isInterface=false,void <init>(long),UVar(defSites={111},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦384;refId=167]),(UVar(defSites={-2},value=ALongValue))),
	113: ArrayStore(pc=392,UVar(defSites={108},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦373;refId=166;length=2]),UVar(defSites={110},value=int ∈ [0,1]),UVar(defSites={111},value=java.util.concurrent.ConcurrentHashMap$CounterCell[↦384;refId=167])),
	114: PutField(pc=396,java.util.concurrent.ConcurrentHashMap,counterCells,java.util.concurrent.ConcurrentHashMap$CounterCell[],UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={108},value=java.util.concurrent.ConcurrentHashMap$CounterCell[][↦373;refId=166;length=2])),
	115: Assignment(pc=399,DVar(useSites={123},value=int = 1,origin=115),IntConst(pc=399,1)),
	116: Assignment(pc=403,DVar(useSites={117},value=int = 0,origin=116),IntConst(pc=403,0)),
	117: PutField(pc=404,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={116},value=int = 0)),
	118: Goto(pc=407,target=123),
	119: CaughtException(pc=410,<ANY>,caused by={exception@112}),
	120: Assignment(pc=413,DVar(useSites={121},value=int = 0,origin=120),IntConst(pc=413,0)),
	121: PutField(pc=414,java.util.concurrent.ConcurrentHashMap,cellsBusy,int,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={120},value=int = 0)),
	122: Throw(pc=419,UVar(defSites={-1000112},value=_ <: java.lang.Throwable[↦-1000389;refId=130])),
	123: If(pc=422,UVar(defSites={104,115},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=132),
	124: Goto(pc=428,target=132),
	125: Assignment(pc=431,DVar(useSites={129},value={jdk.internal.misc.Unsafe, null}[↦431;refId=169],origin=125),GetStatic(pc=431,java.util.concurrent.ConcurrentHashMap,U,jdk.internal.misc.Unsafe)),
	126: Assignment(pc=435,DVar(useSites={129},value=ALongValue,origin=126),GetStatic(pc=435,java.util.concurrent.ConcurrentHashMap,BASECOUNT,long)),
	127: Assignment(pc=439,DVar(useSites={128,129},value=ALongValue,origin=127),GetField(pc=439,java.util.concurrent.ConcurrentHashMap,baseCount,long,UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]))),
	128: Assignment(pc=448,DVar(useSites={129},value=ALongValue,origin=128),BinaryExpr(pc=448,ComputationalTypeLong,UVar(defSites={127},value=ALongValue),+,UVar(defSites={-2},value=ALongValue))),
	129: Assignment(pc=449,DVar(useSites={130},value=int ∈ [0,1],origin=129),VirtualFunctionCall(pc=449,jdk.internal.misc.Unsafe,isInterface=false,boolean compareAndSetLong(java.lang.Object,long,long,long),UVar(defSites={125},value={jdk.internal.misc.Unsafe, null}[↦431;refId=169]),(UVar(defSites={-1},value=_ <: java.util.concurrent.ConcurrentHashMap[↦-1;refId=102]),UVar(defSites={126},value=ALongValue),UVar(defSites={127},value=ALongValue),UVar(defSites={128},value=ALongValue)))),
	130: If(pc=452,UVar(defSites={129},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=6),
	131: Nop(pc=455),
	132: Return(pc=461)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3c,BB_17}
	BB_10: BasicBlock(start=46,end=46) -> {BB_3,BB_40}
	BB_11: BasicBlock(start=78,end=80) -> {BB_25,BB_21}
	BB_12: BasicBlock(start=93,end=93) -> {BB_3}
	BB_13: CatchNode([-1,39)=>42,<none>) -> {BB_b}
	BB_14: BasicBlock(start=61,end=62) -> {BB_1c,BB_2e}
	BB_15: BasicBlock(start=132,end=132) -> {BB_2f}
	BB_16: BasicBlock(start=116,end=118) -> {BB_7}
	BB_17: BasicBlock(start=1,end=1) -> {BB_5,BB_1}
	BB_18: BasicBlock(start=38,end=38) -> {BB_27}
	BB_19: BasicBlock(start=70,end=74) -> {BB_3c,BB_31}
	BB_1: BasicBlock(start=5,end=5) -> {BB_3}
	BB_1a: BasicBlock(start=21,end=25) -> {BB_3c,BB_a}
	BB_1b: BasicBlock(start=92,end=92) -> {BB_3c,BB_12}
	BB_1c: BasicBlock(start=65,end=65) -> {BB_3e,BB_2a}
	BB_1d: BasicBlock(start=124,end=124) -> {BB_15}
	BB_1e: BasicBlock(start=96,end=97) -> {BB_28,BB_f}
	BB_1f: BasicBlock(start=32,end=35) -> {BB_35,BB_13}
	BB_20: BasicBlock(start=17,end=18) -> {BB_3c,BB_38}
	BB_21: CatchNode([76,83)=>86,<none>) -> {BB_6}
	BB_22: BasicBlock(start=59,end=60) -> {BB_2e,BB_14}
	BB_23: BasicBlock(start=27,end=29) -> {BB_27,BB_36}
	BB_24: BasicBlock(start=113,end=115) -> {BB_16}
	BB_25: BasicBlock(start=81,end=81) -> {BB_32,BB_21}
	BB_26: BasicBlock(start=76,end=77) -> {BB_42,BB_11}
	BB_27: BasicBlock(start=39,end=41) -> {BB_10}
	BB_28: BasicBlock(start=98,end=102) -> {BB_3c,BB_29}
	BB_29: BasicBlock(start=103,end=103) -> {BB_9,BB_f}
	BB_2: BasicBlock(start=10,end=13) -> {BB_3c,BB_e}
	BB_2a: BasicBlock(start=66,end=67) -> {BB_1b}
	BB_2b: BasicBlock(start=130,end=130) -> {BB_3,BB_3f}
	BB_2c: BasicBlock(start=3,end=3) -> {BB_3c,BB_3a}
	BB_2d: BasicBlock(start=48,end=49) -> {BB_1b}
	BB_2e: BasicBlock(start=63,end=64) -> {BB_1b}
	BB_2f: ExitNode(normalReturn=true)
	BB_30: BasicBlock(start=8,end=9) -> {BB_3b,BB_2}
	BB_31: BasicBlock(start=75,end=75) -> {BB_26,BB_1b}
	BB_32: BasicBlock(start=82,end=82) -> {BB_42}
	BB_33: BasicBlock(start=119,end=122) -> {BB_3c}
	BB_34: BasicBlock(start=58,end=58) -> {BB_15,BB_22}
	BB_35: BasicBlock(start=36,end=36) -> {BB_27,BB_d}
	BB_36: BasicBlock(start=30,end=31) -> {BB_27,BB_1f}
	BB_37: BasicBlock(start=51,end=52) -> {BB_1b}
	BB_38: BasicBlock(start=19,end=20) -> {BB_2d,BB_1a}
	BB_39: BasicBlock(start=107,end=112) -> {BB_24,BB_c}
	BB_3: BasicBlock(start=6,end=7) -> {BB_30,BB_3b}
	BB_3a: BasicBlock(start=4,end=4) -> {BB_1}
	BB_3b: BasicBlock(start=94,end=95) -> {BB_1e,BB_f}
	BB_3c: ExitNode(normalReturn=false)
	BB_3d: BasicBlock(start=15,end=16) -> {BB_20,BB_2d}
	BB_3e: BasicBlock(start=68,end=69) -> {BB_1b,BB_19}
	BB_3f: BasicBlock(start=131,end=131) -> {BB_15}
	BB_40: BasicBlock(start=47,end=47) -> {BB_15}
	BB_41: BasicBlock(start=90,end=91) -> {BB_3}
	BB_42: BasicBlock(start=83,end=85) -> {BB_41}
	BB_4: BasicBlock(start=53,end=57) -> {BB_3c,BB_34}
	BB_5: BasicBlock(start=2,end=2) -> {BB_3c,BB_2c}
	BB_6: BasicBlock(start=86,end=89) -> {BB_3c}
	BB_7: BasicBlock(start=123,end=123) -> {BB_1d,BB_15}
	BB_8: BasicBlock(start=50,end=50) -> {BB_37,BB_4}
	BB_9: BasicBlock(start=104,end=106) -> {BB_39,BB_16}
	BB_a: BasicBlock(start=26,end=26) -> {BB_23,BB_2d}
	BB_b: BasicBlock(start=42,end=45) -> {BB_3c}
	BB_c: CatchNode([-1,116)=>119,<none>) -> {BB_33}
	BB_d: BasicBlock(start=37,end=37) -> {BB_18,BB_13}
	BB_e: BasicBlock(start=14,end=14) -> {BB_8,BB_3d}
	BB_f: BasicBlock(start=125,end=129) -> {BB_3c,BB_2b}
),exceptionHandlers=(
	ExceptionHandler([-1, 39) -> 42, <FINALLY>),
	ExceptionHandler([76, 83) -> 86, <FINALLY>),
	ExceptionHandler([-1, 116) -> 119, <FINALLY>)
))

