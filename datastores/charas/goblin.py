from common import choice
from .base_chara import BaseChara,BaseStats,BaseModifiers,BaseStatusEffects,BaseMoves
from .base_chara import MStore,SEStore

#--キャラクラス--#
class Goblin(BaseChara):
    def __init__(self):
        super().__init__()
        self.name = "ゴブリン"						#キャラ名
        self.stats = Stats()						#能力値
        self.modifiers = Modifiers()				#能力変化
        self.status_effects = StatusEffects()		#状態変化
        self.moves = Moves()						#技
        self.encount_ms = "こん棒を振り回している"	#エンカウントメッセージ
        
    #行動AI
    def action(self,player):
        """攻撃, 飛びかかる, 砂かけ, 挑発, 様子を見る,休憩"""
        moves = [["攻撃",2],["飛びかかる",1],["様子を見る",1]]
        
        #プレイヤーが怒り状態じゃなければ挑発
        if not player.status_effects.has_effect(effect_name="怒り"):
            moves.append(["挑発",3])
        #プレイヤーが盲目状態じゃなければ砂かけ
        if not player.status_effects.has_effect(effect_name="盲目"):
            moves.append(["砂かけ",3])
            
        #残り体力が1/3以下の場合、飛びかかるか様子を見るの2択
        if self.stats.hp <= self.stats.max_hp // 3:
            moves = [["飛びかかる",2],["様子を見る",1]]
            
        #STが半分以下の場合,休憩を追加
        if self.stats.st <= self.stats.max_st // 2:
            moves.append(["休憩",1])
        
        #ST不足の技は除外
        moves = self.exclude_move_list(moves)
        #ランダムに技を選択
        return self.moves.get_move(choice(moves))
        
        
#--ステータス--#
class Stats(BaseStats):
    def __init__(self):
        super().__init__(
            hp = 130,		#HP(体力)
            st = 10,		#ST(スタミナ)
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
            MStore.inst["攻撃"](),
            MStore.inst["飛びかかる"](),
            MStore.inst["砂かけ"](),
            MStore.inst["挑発"](),
            MStore.inst["様子を見る"](),
            MStore.inst["休憩"](),
            ])
