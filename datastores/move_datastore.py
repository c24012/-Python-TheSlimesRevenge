from moves.slime import Attack,Regenerate,Rest
from moves.goblin import Pounce,HurlStone,Taunt,Observe

class MoveDataStore:
    inst = {
        "攻撃":Attack,
        "再生":Regenerate,
        "休憩":Rest,
        
        "飛びかかる":Pounce,
        "投石":HurlStone,
        "挑発":Taunt,
        "様子を見る":Observe,
        
        }
    
