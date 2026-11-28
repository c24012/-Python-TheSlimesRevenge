from .charas.slime import Slime
from .charas.goblin import Goblin

class CharaDataStore:
    def __init__(self):
        self.charas_data = {
            "slime":Slime,          #スライム
            "goblin":Goblin,        #ゴブリン
            }
    
    #-指定キャラを生成-#
    def inst(self,chara_name,*args):
        if chara_name in self.charas_data:
            if args:
                return self.charas_data[chara_name](*args)
            return self.charas_data[chara_name]()
        else:
            raise ValueError(f"Character '{chara_name}' not found in CharaDataStore.")
    
