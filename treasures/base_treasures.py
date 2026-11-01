from datastores.status_effect_datastore import StatusEffectDataStore as StatusEffect

class BaseTreasure:
    def __init__(self,name,stats=None,effects=None):
        self.name = name			#お宝名
        self.info = []				#効果説明文
        self.stats = stats			#ステータス変動値
        self.effects = effects		#戦闘時付与される状態変化
        
    #--効果説明文--#
    def set_info(self,*texts):
        self.info = texts
        
    #--戦闘開始イベント--#
    def start_battle_event(self):
        pass

#お宝が持つ状態付与のデータ
class StatusEffectForTreasure:
    def __init__(self,name,target,acc=100,turn=None,level=None):
        self.effect = StatusEffect.inst[name]
        self.target = target
        self.acc = acc
        self.turn = turn
        self.level= level
        
    def instance_effect(self):
        return self.effect(turn=self.turn,level=self.level)
    
#お宝が持つ能力増減のデータ
class StatsChangeValue:
    def __init__(self,at=0,df=0,mg=0,md=0,sp=0,hp=0,tp=0):
        self.at = at
        self.df = df
        self.mg = mg
        self.md = md
        self.sp = sp
        self.hp = hp
        self.tp = tp
        
    def get_state(self,name):
        return getattr(self,name)
    
    def get_all(self):
        return [self.at,self.df,self.mg,self.md,self.sp,self.hp,self.tp]
    
        
"""
記述例

#--攻撃--#
class Attack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "攻撃",			技名
            power = 100,			威力
            acc = 100,				命中
            effects = None			状態付与 ([{要素:値}])
            target = 'o'			対象 (自分:'s',相手:'o',両方:'b')
            tp = tp					消費TP
            recovery = [100,'s']	回復値([回復値,対象(自分:'s',相手:'o',両方:'b')])
            )
        self.set_info(
            '通常攻撃'
            )

"""
        