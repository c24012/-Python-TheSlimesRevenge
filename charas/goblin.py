from .base_chara import BaseChara,BaseStats,BaseModifiers,BaseStatusEffects,BaseMoves
from .base_chara import MoveStore,SEStore

#--キャラクラス--#
class Goblin(BaseChara):
    def __init__(self):
        super().__init__()
        self.set_name("ゴブリン")					#キャラクター名
        self.set_stats(Stats())						#ステータス
        self.set_modifiers(Modifiers())				#能力変化
        self.set_status_effects(StatusEffects())	#状態変化
        self.set_moves(Moves())						#技
        self.set_encount_mess(						
            "こん棒を振り回している")				#遭遇コメント
        
        
#--ステータス--#
class Stats(BaseStats):
    def __init__(self):
        super().__init__(
            hp = 100,		#体力
            at = 15,		#攻撃
            df = 5,			#防御
            mg = 5,			#魔法
            md = 5,			#魔防
            sp = 15,		#俊敏
            )

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
            MoveStore.inst["飛びかかる"](),
            MoveStore.inst["砂かけ"](),
            MoveStore.inst["挑発"](),
            MoveStore.inst["様子を見る"](),
            ])




