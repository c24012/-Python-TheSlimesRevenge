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
        
    #TPを消費
    def use_tp(self,value):
        self.stats.tp -= value
        
    #TPを回復
    def recover_tp(self,value):
        self.stats.tp = min(self.stats.tp + value,self.stats.max_tp)
        
    #装備品の能力値変化を計算
    def calculate_treasures_stats(self):
        result_stats = self.treasures.get_all_stats()
        for key,value in result_stats.items():
            self.stats.set_state(key,self.base_stats.get_state(key) + value)
            print(self.stats.get_state(key),f"+{value}")
        
        
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

    #ステータス名を指定してステータス値を取得
    def get_state(self,param):
        if param not in {"hp","max_hp","tp","max_tp","at","df","mg","md","sp"}:
            raise ValueError(f"取得できる変数名ではありません(引数{param})")
        return getattr(self,param)

    #ステータス名を指定してステータス値を設定
    def set_state(self,param,value):
        if param not in {"hp","max_hp","tp","max_tp","at","df","mg","md","sp"}:
            raise ValueError(f"変更できる変数名ではありません(引数{param})")
        setattr(self,param,value)

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
            MStore.inst["再生"]()
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

    def get_all_stats(self):
        params = ["at","df","mg","md","sp","max_hp","max_tp"]
        values = [0,0,0,0,0,0,0]
        for trs in self.treasures:
            if trs.stats is None:
                continue
            _stats = trs.stats.get_all()
            for i in range(len(values)):
                values[i] += _stats[i]
        result = dict(zip(params,values))
        return result
        
        


