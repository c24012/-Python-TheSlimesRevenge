from .base_chara import BaseChara,BaseStats,BaseModifiers,BaseStatusEffects,BaseMoves
from .base_chara import MStore,SEStore
from datastores.treasures_datastore import TreasuresDataStore as TStore

#--キャラクラス--#
class Slime(BaseChara):
    def __init__(self,name="スライム"):
        super().__init__()
        self.name = name						#キャラ名
        self.stats = Stats()					#能力値
        self.modifiers = Modifiers()			#能力変化
        self.status_effects = StatusEffects()	#状態変化
        self.moves = Moves()					#技
        #スライム限定
        self.base_stats = Stats()
        self.treasures = Treasures()			#お宝
        
    #装備品の能力値変化を計算
    def calculate_treasures_stats(self):
        result_stats = self.treasures.get_all_stats()
        for key,value in result_stats.items():
            self.stats.set_state(key,self.base_stats.get_state(key) + value)
            
    #装備品の能力値変化値を取得
    def get_treasures_stats(self):
        return self.treasures.get_all_stats()
        
        
#--ステータス--#
class Stats(BaseStats):
    def __init__(self):
        super().__init__(
            hp = 100,		#HP(体力)
            st = 10,		#ST(スタミナ)
            at = 10,		#攻撃
            df = 10,		#防御
            mg = 10,		#魔法
            md = 10,		#魔防
            sp = 10,		#俊敏
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
            MStore.inst["防御"](),
            MStore.inst["休憩"]()
            ])
        
#--お宝--#
class Treasures:
    def __init__(self):
        self.treasures = [
            TStore.inst["錆びたナイフ"](),
            TStore.inst["折れかけの杖"](),
            TStore.inst["汚れた布"](),
            TStore.inst["軽い石"](),
            TStore.inst["連鎖の輪"](),
            ]
        
    def add_treasure(self,treasure):
        self.treasures.append(treasure)
        
    def remove_treasure(self,treasure):
        self.treasures.remove(treasure)
        
    def has_treasure(self,treasure=None,name=None):
        pass

    def get_len(self):
        return len(self.treasures)

    def get_all_stats(self):
        params = ["max_hp","max_st","at","df","mg","md","sp"]
        values = [0,0,0,0,0,0,0]
        for trs in self.treasures:
            if trs.stats is None:
                continue
            _stats = trs.stats.get_all()
            for i in range(len(values)):
                values[i] += _stats[i]
        result = dict(zip(params,values))
        return result

    def set_battle_class(self,battle_class):
        for i in range(self.get_len()):
            self.treasures[i].set_battle_class(battle_class)

    def on_start_battle(self):
        for i in range(self.get_len()):
            self.treasures[i].on_start_battle()


