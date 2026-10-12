from .base_move import BaseMove

#--攻撃--#
class Attack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "攻撃",
            category = "物理",
            power = 100,
            acc = 100,
            tp = 0,
            target = 'u'
            )
        
#--再生--#
class Regenerate(BaseMove):
    def __init__(self):
        super().__init__(
            name = "再生",
            category = "特殊",
            effects = [0,0],
            recovery = 30,
            tp = 0,
            target = 'o',
            )
        self.set_info(
            f"自分のHPを{self.recovery}回復する"
            )
        
#--休憩--#
class Rest(BaseMove):
    def __init__(self):
        super().__init__(
            name = "休憩",
            category = "特殊",
            tp = 0,
            target = 'o'
            )
