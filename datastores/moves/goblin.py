from .base_move import BaseMove
from .base_move import StatusEffectForMove as SEFM

#--飛びかかる--#
class Pounce(BaseMove):
    def __init__(self):
        super().__init__(
            name = "飛びかかる",
            category = "physical",
            power = 130,
            acc = 80,
            st = 3,
            target = 'o'
            )
        self.set_info("勢いよく飛びかかって攻撃する")
        
#--砂かけ--#
class SandAttack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "砂かけ",
            category = "physical",
            power = 30,
            acc = 100,
            st = 2,
            target = 'o',
            effects = [SEFM(name="blindness",target='o',acc=70,turn=3)]
            )
        self.set_info("確率70%で相手に 盲目(3ターン) を付与する")
        
#--挑発--#
class Taunt(BaseMove):
    def __init__(self):
        super().__init__(
            name = "挑発",
            category = "special",
            st = 2,
            effects = [SEFM(name="enraged",target='o',turn=3)]
            )
        self.set_info("相手に 怒り(3ターン) を付与する")
        





    

