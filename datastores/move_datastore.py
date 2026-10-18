from moves.slime import Attack,Regenerate,Rest
from moves.goblin import Pounce,SandAttack,Taunt,Observe

class MoveDataStore:
    inst = {
        "攻撃":Attack,
        "再生":Regenerate,
        "休憩":Rest,
        
        "飛びかかる":Pounce,
        "砂かけ":SandAttack,
        "挑発":Taunt,
        "様子を見る":Observe,
        
        }
    
