from .moves.common import Attack,Rest,Observe
from .moves.slime import Guard
from .moves.goblin import Pounce,SandAttack,Taunt

class MoveDataStore:
    inst = {
        #共通技
        "攻撃":Attack,
        "休憩":Rest,
        "様子を見る":Observe,
        
        #スライム
        "防御":Guard,
        
        #ゴブリン
        "飛びかかる":Pounce,
        "砂かけ":SandAttack,
        "挑発":Taunt,
        
        }
    
