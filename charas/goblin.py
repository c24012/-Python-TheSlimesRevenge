from .base_chara import BaseChara,BaseStats,BaseModifiers,BaseStatusEffects,BaseMoves
from datastores.move_datastore import MoveDataStore as Move

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
            hp = 140,		#体力
            at = 30,		#攻撃
            df = 10,		#防御
            mg = 5,			#魔法
            md = 5,			#魔防
            sp = 15,		#俊敏
            )

#--能力変化--#
class Modifiers(BaseModifiers):
    pass

#--状態変化--#
class StatusEffects(BaseStatusEffects):
    pass

#--技--#
class Moves(BaseMoves):
    def __init__(self):
        super().__init__([
            Move.inst["飛びかかる"](),
            Move.inst["投石"](),
            Move.inst["挑発"](),
            Move.inst["様子を見る"](),
            ])




