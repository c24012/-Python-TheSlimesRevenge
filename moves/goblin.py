from .base_move import BaseMove

#--飛びかかる--#
class Pounce(BaseMove):
    def __init__(self):
        super().__init__(
            name = "飛びかかる",
            category = "物理",
            power = 130,
            acc = 90,
            tp = 5,
            target = 'u'
            )
        
#--投石--#
class HurlStone(BaseMove):
    def __init__(self):
        super().__init__(
            name = "投石",
            category = "物理",
            power = 40,
            acc = 80,
            tp = 2,
            target = 'u'
            )
        
#--挑発--#
class Taunt(BaseMove):
    def __init__(self):
        super().__init__(
            name = "挑発",
            category = "物理",
            tp = 2,
            target = 'u'
            )
        
#--様子を見る--#
class Observe(BaseMove):
    def __init__(self):
        super().__init__(
            name = "様子を見る",
            category = "特殊",
            target = 'o'
            )





    

