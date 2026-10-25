from .base_chara import BaseChara,BaseStats,BaseModifiers,BaseStatusEffects,BaseMoves
from .base_chara import MoveStore,SEStore

#--キャラクラス--#
class Slime(BaseChara):
    def __init__(self,name="スライム"):
        super().__init__()
        self.set_name(name)							#キャラクター名
        self.set_stats(Stats())						#ステータス
        self.set_modifiers(Modifiers())				#能力変化
        self.set_status_effects(StatusEffects())	#状態変化
        self.set_moves(Moves())						#技
        
    #TPを消費
    def use_tp(self,value):
        self.stats.tp -= value
        
    #TPを回復
    def recover_tp(self,value):
        self.stats.tp = min(self.stats.tp + value,self.stats.max_tp)
        
        
#--ステータス--#
class Stats(BaseStats):
    def __init__(self):
        super().__init__(
            hp = 100,		#体力
            at = 10,		#攻撃
            df = 10,		#防御
            mg = 10,		#魔法
            md = 10,		#魔防
            sp = 10,		#俊敏
            )
        #スライムのみのステータス
        self.tp = 30			#変身力
        self.max_tp = self.tp	#最大変身力

#--能力変化--#
class Modifiers(BaseModifiers):
    def __init__(self):
        super().__init__()
        self.at = 0
        self.df = 0
        self.mg = 0
        self.md = 0
        self.sp = 0

#--状態変化--#
class StatusEffects(BaseStatusEffects):
    def __init__(self):
        super().__init__([])

#--技--#
class Moves(BaseMoves):
    def __init__(self):
        super().__init__([
            MoveStore.inst["攻撃"](),
            MoveStore.inst["再生"](),
            MoveStore.inst["飛びかかる"](),
            MoveStore.inst["砂かけ"](),
            MoveStore.inst["挑発"]()
            ])




