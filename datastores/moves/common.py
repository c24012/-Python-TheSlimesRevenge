from .base_move import BaseMove
from .base_move import StatusEffectForMove as SEFM

#--攻撃--#
class Attack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "攻撃",
            category = "物理",
            target = 'o',
            power = 100,
            acc = 100,
            enemy_only = True
            )
        self.set_info("通常攻撃")
        
#--休憩--#
class Rest(BaseMove):
    def __init__(self):
        super().__init__(
            name = "休憩",
            category = "特殊",
            target = 's',
            rec_st = [5,'s'],
            enemy_only = True
            )
        self.set_info(f"自分のSTを{self.rec_st[0]}回復する")
        
#--様子を見る--#
class Observe(BaseMove):
    def __init__(self):
        super().__init__(
            name = "様子を見る",
            category = "特殊",
            enemy_only = True
            )