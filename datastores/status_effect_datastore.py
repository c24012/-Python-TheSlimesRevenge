from .status_effects.test import PowerCharge
from .status_effects.slime import Hardening
from .status_effects.goblin import Blindness,Enraged

class StatusEffectDataStore:
    def __init__(self):
        self.status_effects_data = {
            #テスト
            "power_charge":PowerCharge,         #チャージ
            
            #スライム
            "hardening":Hardening,              #硬化
        
            #ゴブリン
            "blindness":Blindness,              #盲目
            "enraged":Enraged,                  #怒り
        
        }

    #-指定状態を生成-#
    def inst(self,effect_name,*args):
        if effect_name in self.status_effects_data:
            if args:
                return self.status_effects_data[effect_name](*args)
            return self.status_effects_data[effect_name]()
        else:
            raise ValueError(f"Status Effect '{effect_name}' not found in StatusEffectDataStore.")

    #-指定状態を取得-#
    def get_effect(self,effect_name):
        result = self.status_effects_data.get(effect_name)
        if result is None:
            raise ValueError(f"Status Effect '{effect_name}' not found in StatusEffectDataStore.")
        return result
