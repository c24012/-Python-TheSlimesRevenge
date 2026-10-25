from status_effects.base_status_effect import BaseStatusEffect

#--ためる--#
class PowerCharge(BaseStatusEffect):
    def __init__(self,turn,level):
        super().__init__(
            name = "ためる",
            info = ["攻撃+[Lv×2]","物理技を使用すると効果を失う"],
            level = level
            )

