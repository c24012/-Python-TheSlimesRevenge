from datastores.status_effect_datastore import StatusEffectDataStore as StatusEffect
from .base_move import BaseMove

se = StatusEffect()

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
        
#--砂かけ--#
class SandAttack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "砂かけ",
            category = "物理",
            power = 30,
            acc = 70,
            tp = 2,
            target = 'o',
            effects = [{"effect":se.inst["盲目"],"turn":3,"acc":100,"target":'o'}]
            )
        
#--挑発--#
class Taunt(BaseMove):
    def __init__(self):
        super().__init__(
            name = "挑発",
            category = "特殊",
            tp = 2,
            effects = [{"effect":se.inst["怒り"],"turn":3,"acc":100,"target":'o'}]
            )
        
#--様子を見る--#
class Observe(BaseMove):
    def __init__(self):
        super().__init__(
            name = "様子を見る",
            category = "特殊",
            tp = -1,
            )





    

