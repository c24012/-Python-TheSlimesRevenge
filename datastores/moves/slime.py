from .base_move import BaseMove
from .base_move import StatusEffectForMove as SEFM

#--防御--#
class Guard(BaseMove):
    def __init__(self):
        super().__init__(
            name = "硬化",
            category = "特殊",
            effects = [SEFM(name="硬化",target='s',acc=100,turn=1)]
            )
        self.set_info("自分に 硬化(1ターン) を付与する")
