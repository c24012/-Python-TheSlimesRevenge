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
            )
        
#--再生--#
class Regenerate(BaseMove):
    def __init__(self):
        super().__init__(
            name = "再生",
            category = "特殊",
            recovery = 40,
            tp = 0,
            target = 's',
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
            target = 's'
            )
