from .base_move import BaseMove
from .base_move import StatusEffectForMove as SEFM

#--攻撃--#
class EnemyAttack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "攻撃",
            category = "物理",
            target = 'o',
            power = 100,
            acc = 100,
            )
        self.set_info(
            "通常攻撃"
            )