boolean study(java.util.regex.Pattern$TreeInfo)
AITACode(params=(Parameters(
	0: useSites={0,4,12,14,9} (origin=-1),
	1: useSites={8,10,6,5,13,3,15} (origin=-2)
)),stmts=(
	0: Assignment(pc=1,DVar(useSites={2},value={java.util.regex.Pattern$Qtype, null}[↦1;refId=104],origin=0),GetField(pc=1,java.util.regex.Pattern$Ques,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	1: Assignment(pc=4,DVar(useSites={2},value={java.util.regex.Pattern$Qtype, null}[↦4;refId=105],origin=1),GetStatic(pc=4,java.util.regex.Pattern$Qtype,INDEPENDENT,java.util.regex.Pattern$Qtype)),
	2: If(pc=7,UVar(defSites={0},value={java.util.regex.Pattern$Qtype, null}[↦1;refId=104]),==,UVar(defSites={1},value={java.util.regex.Pattern$Qtype, null}[↦4;refId=105]),target=12),
	3: Assignment(pc=11,DVar(useSites={6},value=an int,origin=3),GetField(pc=11,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103]))),
	4: Assignment(pc=16,DVar(useSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=113],origin=4),GetField(pc=16,java.util.regex.Pattern$Ques,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	5: ExprStmt(pc=20,VirtualFunctionCall(pc=20,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={4},value={_ <: java.util.regex.Pattern$Node, null}[↦16;refId=113]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	6: PutField(pc=26,java.util.regex.Pattern$TreeInfo,minLength,int,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={3},value=an int)),
	7: Assignment(pc=30,DVar(useSites={8},value=int = 0,origin=7),IntConst(pc=30,0)),
	8: PutField(pc=31,java.util.regex.Pattern$TreeInfo,deterministic,boolean,UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103]),UVar(defSites={7},value=int = 0)),
	9: Assignment(pc=35,DVar(useSites={10},value={_ <: java.util.regex.Pattern$Node, null}[↦35;refId=116],origin=9),GetField(pc=35,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	10: Assignment(pc=39,DVar(useSites={11},value=int ∈ [0,1],origin=10),VirtualFunctionCall(pc=39,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={9},value={_ <: java.util.regex.Pattern$Node, null}[↦35;refId=116]),(UVar(defSites={-2},value=java.util.regex.Pattern$TreeInfo[↦-2;refId=103])))),
	11: ReturnValue(pc=42,UVar(defSites={10},value=int ∈ [0,1])),
	12: Assignment(pc=44,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦44;refId=106],origin=12),GetField(pc=44,java.util.regex.Pattern$Ques,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	13: ExprStmt(pc=48,VirtualFunctionCall(pc=48,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node, null}[↦44;refId=106]),(UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103])))),
	14: Assignment(pc=53,DVar(useSites={15},value={_ <: java.util.regex.Pattern$Node, null}[↦53;refId=109],origin=14),GetField(pc=53,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	15: Assignment(pc=57,DVar(useSites={16},value=int ∈ [0,1],origin=15),VirtualFunctionCall(pc=57,java.util.regex.Pattern$Node,isInterface=false,boolean study(java.util.regex.Pattern$TreeInfo),UVar(defSites={14},value={_ <: java.util.regex.Pattern$Node, null}[↦53;refId=109]),(UVar(defSites={-2},value={java.util.regex.Pattern$TreeInfo, null}[↦-2;refId=103])))),
	16: ReturnValue(pc=60,UVar(defSites={15},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_4,BB_3}
	BB_1: BasicBlock(start=14,end=15) -> {BB_9,BB_6}
	BB_2: BasicBlock(start=6,end=10) -> {BB_9,BB_7}
	BB_3: BasicBlock(start=12,end=13) -> {BB_9,BB_1}
	BB_4: BasicBlock(start=3,end=3) -> {BB_9,BB_8}
	BB_5: ExitNode(normalReturn=true)
	BB_6: BasicBlock(start=16,end=16) -> {BB_5}
	BB_7: BasicBlock(start=11,end=11) -> {BB_5}
	BB_8: BasicBlock(start=4,end=5) -> {BB_9,BB_2}
	BB_9: ExitNode(normalReturn=false)
))

boolean match(java.util.regex.Matcher,int,java.lang.CharSequence)
AITACode(params=(Parameters(
	0: useSites={8,12,44,38,22,1,33,41,25,5,19} (origin=-1),
	1: useSites={36,20,34,10,42,26,6,46,9,13,45,27,39,23} (origin=-2),
	2: useSites={20,34,42,6,13,39,23} (origin=-3),
	3: useSites={20,34,10,42,6,46,13,27,39,23} (origin=-4)
)),stmts=(
	0: Assignment(pc=0,DVar(useSites={3},value={int[], null}[↦0;refId=105],origin=0),GetStatic(pc=0,java.util.regex.Pattern$2,$SwitchMap$java$util$regex$Pattern$Qtype,int[])),
	1: Assignment(pc=4,DVar(useSites={2},value={java.util.regex.Pattern$Qtype, null}[↦4;refId=106],origin=1),GetField(pc=4,java.util.regex.Pattern$Ques,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	2: Assignment(pc=7,DVar(useSites={3},value=an int,origin=2),VirtualFunctionCall(pc=7,java.util.regex.Pattern$Qtype,isInterface=false,int ordinal(),UVar(defSites={1},value={java.util.regex.Pattern$Qtype, null}[↦4;refId=106]),())),
	3: Assignment(pc=10,DVar(useSites={4},value=an int,origin=3),ArrayLoad(pc=10,UVar(defSites={2},value=an int),UVar(defSites={0},value={int[], null}[↦0;refId=105]))),
	4: Switch(pc=11,defaultTarget=41,index=UVar(defSites={3},value=an int),npairs=(IntIntPair(1,5),IntIntPair(2,19),IntIntPair(3,33)),
	5: Assignment(pc=37,DVar(useSites={6},value={_ <: java.util.regex.Pattern$Node, null}[↦37;refId=132],origin=5),GetField(pc=37,java.util.regex.Pattern$Ques,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	6: Assignment(pc=43,DVar(useSites={7},value=int ∈ [0,1],origin=6),VirtualFunctionCall(pc=43,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={5},value={_ <: java.util.regex.Pattern$Node, null}[↦37;refId=132]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	7: If(pc=46,UVar(defSites={6},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=12),
	8: Assignment(pc=50,DVar(useSites={10},value={_ <: java.util.regex.Pattern$Node, null}[↦50;refId=135],origin=8),GetField(pc=50,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	9: Assignment(pc=55,DVar(useSites={10},value=an int,origin=9),GetField(pc=55,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	10: Assignment(pc=59,DVar(useSites={11},value=int ∈ [0,1],origin=10),VirtualFunctionCall(pc=59,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={8},value={_ <: java.util.regex.Pattern$Node, null}[↦50;refId=135]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={9},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	11: If(pc=62,UVar(defSites={10},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=15),
	12: Assignment(pc=66,DVar(useSites={13},value={_ <: java.util.regex.Pattern$Node, null}[↦66;refId=142],origin=12),GetField(pc=66,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	13: Assignment(pc=72,DVar(useSites={14},value=int ∈ [0,1],origin=13),VirtualFunctionCall(pc=72,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={12},value={_ <: java.util.regex.Pattern$Node, null}[↦66;refId=142]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	14: If(pc=75,UVar(defSites={13},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=17),
	15: Assignment(pc=78,DVar(useSites={18},value=int = 1,origin=15),IntConst(pc=78,1)),
	16: Goto(pc=79,target=18),
	17: Assignment(pc=82,DVar(useSites={18},value=int ∈ [0,1],origin=17),IntConst(pc=82,0)),
	18: ReturnValue(pc=83,UVar(defSites={17,15},value=int ∈ [0,1])),
	19: Assignment(pc=85,DVar(useSites={20},value={_ <: java.util.regex.Pattern$Node, null}[↦85;refId=122],origin=19),GetField(pc=85,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	20: Assignment(pc=91,DVar(useSites={21},value=int ∈ [0,1],origin=20),VirtualFunctionCall(pc=91,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={19},value={_ <: java.util.regex.Pattern$Node, null}[↦85;refId=122]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	21: If(pc=94,UVar(defSites={20},value=int ∈ [0,1]),!=,IntConst(pc=-333,0),target=29),
	22: Assignment(pc=98,DVar(useSites={23},value={_ <: java.util.regex.Pattern$Node, null}[↦98;refId=125],origin=22),GetField(pc=98,java.util.regex.Pattern$Ques,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	23: Assignment(pc=104,DVar(useSites={24},value=int ∈ [0,1],origin=23),VirtualFunctionCall(pc=104,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={22},value={_ <: java.util.regex.Pattern$Node, null}[↦98;refId=125]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	24: If(pc=107,UVar(defSites={23},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=31),
	25: Assignment(pc=111,DVar(useSites={27},value={_ <: java.util.regex.Pattern$Node, null}[↦111;refId=128],origin=25),GetField(pc=111,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	26: Assignment(pc=116,DVar(useSites={27},value=an int,origin=26),GetField(pc=116,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	27: Assignment(pc=120,DVar(useSites={28},value=int ∈ [0,1],origin=27),VirtualFunctionCall(pc=120,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={25},value={_ <: java.util.regex.Pattern$Node, null}[↦111;refId=128]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={26},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	28: If(pc=123,UVar(defSites={27},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=31),
	29: Assignment(pc=126,DVar(useSites={32},value=int = 1,origin=29),IntConst(pc=126,1)),
	30: Goto(pc=127,target=32),
	31: Assignment(pc=130,DVar(useSites={32},value=int ∈ [0,1],origin=31),IntConst(pc=130,0)),
	32: ReturnValue(pc=131,UVar(defSites={29,31},value=int ∈ [0,1])),
	33: Assignment(pc=133,DVar(useSites={34},value={_ <: java.util.regex.Pattern$Node, null}[↦133;refId=118],origin=33),GetField(pc=133,java.util.regex.Pattern$Ques,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	34: Assignment(pc=139,DVar(useSites={35},value=int ∈ [0,1],origin=34),VirtualFunctionCall(pc=139,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={33},value={_ <: java.util.regex.Pattern$Node, null}[↦133;refId=118]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	35: If(pc=142,UVar(defSites={34},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=38),
	36: Assignment(pc=146,DVar(useSites={39},value=an int,origin=36),GetField(pc=146,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	37: Nop(pc=149),
	38: Assignment(pc=151,DVar(useSites={39},value={_ <: java.util.regex.Pattern$Node, null}[↦151;refId=139],origin=38),GetField(pc=151,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	39: Assignment(pc=157,DVar(useSites={40},value=int ∈ [0,1],origin=39),VirtualFunctionCall(pc=157,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={38},value={_ <: java.util.regex.Pattern$Node, null}[↦151;refId=139]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={36,-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	40: ReturnValue(pc=160,UVar(defSites={39},value=int ∈ [0,1])),
	41: Assignment(pc=162,DVar(useSites={42},value={_ <: java.util.regex.Pattern$Node, null}[↦162;refId=111],origin=41),GetField(pc=162,java.util.regex.Pattern$Ques,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	42: Assignment(pc=168,DVar(useSites={43},value=int ∈ [0,1],origin=42),VirtualFunctionCall(pc=168,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={41},value={_ <: java.util.regex.Pattern$Node, null}[↦162;refId=111]),(UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]),UVar(defSites={-3},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	43: If(pc=171,UVar(defSites={42},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=50),
	44: Assignment(pc=175,DVar(useSites={46},value={_ <: java.util.regex.Pattern$Node, null}[↦175;refId=114],origin=44),GetField(pc=175,java.util.regex.Pattern$Ques,next,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]))),
	45: Assignment(pc=180,DVar(useSites={46},value=an int,origin=45),GetField(pc=180,java.util.regex.Matcher,last,int,UVar(defSites={-2},value={java.util.regex.Matcher, null}[↦-2;refId=103]))),
	46: Assignment(pc=184,DVar(useSites={47},value=int ∈ [0,1],origin=46),VirtualFunctionCall(pc=184,java.util.regex.Pattern$Node,isInterface=false,boolean match(java.util.regex.Matcher,int,java.lang.CharSequence),UVar(defSites={44},value={_ <: java.util.regex.Pattern$Node, null}[↦175;refId=114]),(UVar(defSites={-2},value=java.util.regex.Matcher[↦-2;refId=103]),UVar(defSites={45},value=an int),UVar(defSites={-4},value={_ <: java.lang.CharSequence, null}[↦-4;refId=104])))),
	47: If(pc=187,UVar(defSites={46},value=int ∈ [0,1]),==,IntConst(pc=-333,0),target=50),
	48: Assignment(pc=190,DVar(useSites={51},value=int = 1,origin=48),IntConst(pc=190,1)),
	49: Goto(pc=191,target=51),
	50: Assignment(pc=194,DVar(useSites={51},value=int ∈ [0,1],origin=50),IntConst(pc=194,0)),
	51: ReturnValue(pc=195,UVar(defSites={48,50},value=int ∈ [0,1]))
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=2) -> {BB_24,BB_17}
	BB_10: BasicBlock(start=28,end=28) -> {BB_1d,BB_d}
	BB_11: BasicBlock(start=38,end=39) -> {BB_24,BB_7}
	BB_12: BasicBlock(start=32,end=32) -> {BB_1b}
	BB_13: BasicBlock(start=17,end=17) -> {BB_1a}
	BB_14: BasicBlock(start=22,end=23) -> {BB_24,BB_9}
	BB_15: BasicBlock(start=44,end=45) -> {BB_24,BB_c}
	BB_16: BasicBlock(start=27,end=27) -> {BB_24,BB_10}
	BB_17: BasicBlock(start=3,end=3) -> {BB_24,BB_23}
	BB_18: BasicBlock(start=35,end=35) -> {BB_11,BB_20}
	BB_19: BasicBlock(start=48,end=49) -> {BB_21}
	BB_1: BasicBlock(start=5,end=6) -> {BB_24,BB_6}
	BB_1a: BasicBlock(start=18,end=18) -> {BB_1b}
	BB_1b: ExitNode(normalReturn=true)
	BB_1c: BasicBlock(start=50,end=50) -> {BB_21}
	BB_1d: BasicBlock(start=31,end=31) -> {BB_12}
	BB_1e: BasicBlock(start=11,end=11) -> {BB_26,BB_5}
	BB_1f: BasicBlock(start=43,end=43) -> {BB_1c,BB_15}
	BB_20: BasicBlock(start=36,end=36) -> {BB_24,BB_a}
	BB_21: BasicBlock(start=51,end=51) -> {BB_1b}
	BB_22: BasicBlock(start=19,end=20) -> {BB_24,BB_e}
	BB_23: BasicBlock(start=4,end=4) -> {BB_f,BB_1,BB_22,BB_4}
	BB_24: ExitNode(normalReturn=false)
	BB_25: BasicBlock(start=47,end=47) -> {BB_1c,BB_19}
	BB_26: BasicBlock(start=15,end=16) -> {BB_1a}
	BB_2: BasicBlock(start=10,end=10) -> {BB_24,BB_1e}
	BB_3: BasicBlock(start=14,end=14) -> {BB_13,BB_26}
	BB_4: BasicBlock(start=41,end=42) -> {BB_24,BB_1f}
	BB_5: BasicBlock(start=12,end=13) -> {BB_24,BB_3}
	BB_6: BasicBlock(start=7,end=7) -> {BB_5,BB_8}
	BB_7: BasicBlock(start=40,end=40) -> {BB_1b}
	BB_8: BasicBlock(start=8,end=9) -> {BB_24,BB_2}
	BB_9: BasicBlock(start=24,end=24) -> {BB_1d,BB_b}
	BB_a: BasicBlock(start=37,end=37) -> {BB_11}
	BB_b: BasicBlock(start=25,end=26) -> {BB_24,BB_16}
	BB_c: BasicBlock(start=46,end=46) -> {BB_24,BB_25}
	BB_d: BasicBlock(start=29,end=30) -> {BB_12}
	BB_e: BasicBlock(start=21,end=21) -> {BB_d,BB_14}
	BB_f: BasicBlock(start=33,end=34) -> {BB_24,BB_18}
))

void <init>(java.util.regex.Pattern$Node,java.util.regex.Pattern$Qtype)
AITACode(params=(Parameters(
	0: useSites={0,2,1} (origin=-1),
	1: useSites={1} (origin=-2),
	2: useSites={2} (origin=-3)
)),stmts=(
	0: NonVirtualMethodCall(pc=1,java.util.regex.Pattern$Node,isInterface=false,void <init>(),UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]),()),
	1: PutField(pc=6,java.util.regex.Pattern$Ques,atom,java.util.regex.Pattern$Node,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]),UVar(defSites={-2},value={_ <: java.util.regex.Pattern$Node, null}[↦-2;refId=103])),
	2: PutField(pc=11,java.util.regex.Pattern$Ques,type,java.util.regex.Pattern$Qtype,UVar(defSites={-1},value=java.util.regex.Pattern$Ques[↦-1;refId=102]),UVar(defSites={-3},value={java.util.regex.Pattern$Qtype, null}[↦-3;refId=104])),
	3: Return(pc=14)
),cfg=CFG(
	BB_0: BasicBlock(start=0,end=0) -> {BB_3,BB_1}
	BB_1: BasicBlock(start=1,end=3) -> {BB_2}
	BB_2: ExitNode(normalReturn=true)
	BB_3: ExitNode(normalReturn=false)
))

