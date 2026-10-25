from status_effects.base_status_effect import BaseStatusEffect

#--盲目状態--#
class Blindness(BaseStatusEffect):
    def __init__(self,turn,level):
        super().__init__(
            name = "盲目",
            info = ["技の命中が30%低下"],
            turn = turn
            )
       
#--怒り状態--#
class Enraged(BaseStatusEffect):
    def __init__(self,turn,level):
        super().__init__(
            name = "怒り",
            info = ["攻撃+1,防御-1,魔防-1"],
            turn = turn
            )
        self.set_modifier(at=1,df=-1,md=-1)