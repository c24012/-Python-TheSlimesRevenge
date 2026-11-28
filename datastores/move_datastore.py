from .moves.common import Attack,Rest,Observe
from .moves.slime import Guard
from .moves.goblin import Pounce,SandAttack,Taunt

class MoveDataStore:
    def __init__(self):
        self.moves_data = {
            #共通技
            "attack":Attack,            #攻撃
            "rest":Rest,                #休憩
            "observe":Observe,          #様子を見る
            
            #スライム
            "guard":Guard,              #防御
        
            #ゴブリン
            "pounce":Pounce,            #飛びかかる
            "sand_attack":SandAttack,   #砂かけ
            "taunt":Taunt,              #挑発
        
        }
    
    #-指定技を生成-#
    def inst(self,move_name,*args):
        if move_name in self.moves_data:
            if args:
                return self.moves_data[move_name](*args)
            return self.moves_data[move_name]()
        else:
            raise ValueError(f"Move '{move_name}' not found in MoveDataStore.")
    
