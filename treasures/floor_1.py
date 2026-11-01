from .base_treasures import BaseTreasure
from .base_treasures import StatusEffectForTreasure as SEFT
from .base_treasures import StatsChangeValue as SCV

#錆びたナイフ
class RustedKnife(BaseTreasure):
    def __init__(self):
        super().__init__(
            name = "錆びたナイフ",
            stats = SCV(at=10)
            )
        self.set_info("装備品:攻撃+10")
        
#折れかけの杖
class BrokenWand(BaseTreasure):
    def __init__(self):
        super().__init__(
            name = "折れかけの杖",
            stats = SCV(mg=10,md=5)
            )
        self.set_info("装備品:魔法+10,魔防+5")
        
#汚れた布
class DirtyCloth(BaseTreasure):
    def __init__(self):
        super().__init__(
            name = "汚れた布",
            stats = SCV(df=10,md=5)
            )
        self.set_info("装備品:防御+10,魔防+5")
        
#軽い石
class LightStone(BaseTreasure):
    def __init__(self):
        super().__init__(
            name = "軽い石",
            stats = SCV(at=5,df=5,sp=10)
            )
        self.set_info("装備品:攻撃+5,防御+5,俊敏+10")
        
#連鎖の輪
class BraceletOfChains(BaseTreasure):
    def __init__(self):
        super().__init__(
            name = "連鎖の輪",
            effects = [SEFT(name="盲目",target='o',acc=100,turn=3)]
            )
        self.set_info("戦闘開始時 盲目(ターン3) を相手に付与")