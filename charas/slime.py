from bases.base_chara import BaseChara
from bases.base_stats import BaseStats

#--キャラクラス--#
class Slime(BaseChara):
    def __init__(self,name="スライム"):
        super().__init__()
        self.set_name(name)	#キャラクター名
        self.set_stats(SlimeStats())
        
#--ステータス--#
class SlimeStats(BaseStats):
    def __init__(self):
        super().__init__(
            hp = 100,
            at = 10,
            df = 10,
            mg = 10,
            md = 10,
            sp = 10,
            )
        #