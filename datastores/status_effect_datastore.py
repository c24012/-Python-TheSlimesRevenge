from .status_effects.test import PowerCharge
from .status_effects.slime import Hardening
from .status_effects.goblin import Blindness,Enraged

class StatusEffectDataStore:
    inst = {
        #テスト
        "ためる":PowerCharge,
        
        #スライム
        "硬化":Hardening,
        
        #ゴブリン
        "盲目":Blindness,
        "怒り":Enraged,
        
        
        }
    

