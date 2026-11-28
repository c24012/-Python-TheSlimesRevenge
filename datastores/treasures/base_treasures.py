from datastores.status_effect_datastore import StatusEffectDataStore as StatusEffect

class BaseTreasure:
    def __init__(self,name,stats=None,effects=None):
        self.name = name			#お宝名
        self.info = []				#効果説明文
        self.stats = stats			#ステータス変動値
        self.effects = effects		#戦闘時付与される状態変化
        self.battle_class = None    #戦闘クラス(戦闘時のみ使用)
        
    #--効果説明文--#
    def set_info(self,*texts):
        self.info = texts

    #--状態を付与(戦闘中のみ)--#
    def add_status_effect(self,effects):
        for _effect in effects:
            self.battle_class.mp.give_effects(_effect,is_player=True)

    #-- ↓ 外部から呼び出す関数 ↓--#

    #--戦闘クラス登録--#
    def set_battle_class(self,battle_clase):
        self.battle_class = battle_clase
        
    #--戦闘開始イベント--#
    def on_start_battle(self):
        pass



#お宝が持つ状態付与のデータ
class StatusEffectForTreasure:
    def __init__(self,name,target,acc=100,turn=None,level=None):
        self.effect = StatusEffect().get_effect(name)
        self.target = target
        self.acc = acc
        self.turn = turn
        self.level= level
        
    def instance_effect(self):
        return self.effect(turn=self.turn,level=self.level)
    
#お宝が持つ能力増減のデータ
class StatsChangeValue:
    def __init__(self,hp=0,st=0,at=0,df=0,mg=0,md=0,sp=0):
        self.hp = hp
        self.st = st
        self.at = at
        self.df = df
        self.mg = mg
        self.md = md
        self.sp = sp
        
    def get_state(self,name):
        return getattr(self,name)
    
    def get_all(self):
        return [self.hp,self.st,self.at,self.df,self.mg,self.md,self.sp]
    
        
"""
記述例

#--剣--#
class Sword(BaseTreasure):
    def __init__(self):
        super().__init__(
            name = ""			    #お宝名
            stats = SCV(at=10)      #ステータス変動値
            effects = [SEFT(name="盲目",target='o',acc=100,turn=3)]		#戦闘時付与される状態変化
            )
        self.set_info(
            '装備品:攻撃+10'
            )

"""
        