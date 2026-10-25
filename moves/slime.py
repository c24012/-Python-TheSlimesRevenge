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
            tp = 0
            )
        self.set_info(
            "通常攻撃"
            )
        
#--再生--#
class Regenerate(BaseMove):
    def __init__(self):
        super().__init__(
            name = "再生",
            category = "特殊",
            target = 's',
            recovery = [40,'s'],
            tp = 0
            )
        self.set_info(
            f"自分のHPを{self.recovery}回復する"
            )

"""#--力溜め--#
class Regenerate(BaseMove):
    def __init__(self):
        super().__init__(
            name = "力溜め",
            category = "特殊",
            tp = 0,
            target = 's',
            effects = [SEFM(name="ためる",target='s',level=1)]
            )
        self.set_info(
            f"自分に ためる(Lv1) を付与する"
            )"""
