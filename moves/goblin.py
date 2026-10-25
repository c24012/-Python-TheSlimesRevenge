from .base_move import BaseMove
from .base_move import StatusEffectForMove as SEFM

#--飛びかかる--#
class Pounce(BaseMove):
    def __init__(self):
        super().__init__(
            name = "飛びかかる",
            category = "物理",
            power = 130,
            acc = 80,
            tp = 5,
            target = 'o'
            )
        self.set_info(
            "勢いよく飛びかかって攻撃する"
            )
        
#--砂かけ--#
class SandAttack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "砂かけ",
            category = "物理",
            power = 30,
            acc = 100,
            tp = 2,
            target = 'o',
            effects = [SEFM(name="盲目",target='o',acc=70,turn=3)]
            )
        self.set_info(
            "確率70%で相手に 盲目(3ターン) を付与する"
            )
        
#--挑発--#
class Taunt(BaseMove):
    def __init__(self):
        super().__init__(
            name = "挑発",
            category = "特殊",
            tp = 2,
            effects = [SEFM(name="怒り",target='o',turn=3)]
            )
        self.set_info(
            "相手に 怒り(3ターン) を付与する"
            )
        
#--様子を見る--#
class Observe(BaseMove):
    def __init__(self):
        super().__init__(
            name = "様子を見る",
            category = "特殊",
            )





    

