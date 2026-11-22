from .base_status_effect import BaseStatusEffect

#--硬化状態--#
class Hardening(BaseStatusEffect):
    def __init__(self,turn,level):
        super().__init__(
            name = "硬化",
            turn = turn
            )
        self.set_info("受けるダメージを70%軽減")