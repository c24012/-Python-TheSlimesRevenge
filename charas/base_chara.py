from datastores.move_datastore import MoveDataStore as Move

#--キャラクラス--#
class BaseChara:
    def __init__(self):
        self.name = None			#キャラ名
        self.stats = None			#能力値
        self.modifiers = None		#能力変化
        self.status_effects = None	#状態変化
        self.moves = None			#技
        self.encount_ms = ""
        
    def set_name(self,name):
        self.name = name
    
    def set_stats(self,stats):
        self.stats = stats
        
    def set_modifiers(self,modifiers):
        self.modifiers = modifiers
        
    def set_status_effects(self,status_effects):
        self.status_effects = status_effects
        
    def set_moves(self,move):
        self.moves = move.moves
        
    def set_encount_mess(self,message):
        self.encount_mess = message
        
    def damage(self,value):
        self.stats.hp -= value
        
#--ステータスクラス--#
class BaseStats:
    def __init__(self,hp,at,df,mg,md,sp):
        self.hp = hp			#体力
        self.max_hp = hp		#最大体力
        self.at = at			#攻撃
        self.df = df			#防御
        self.mg = mg			#魔法
        self.md = md			#魔防
        self.sp = sp			#俊敏
                
    #ステータス名を指定してステータス値を取得
    def get_state(self,param):
        stats = {"hp":self.hp,"max_hp":self.max_hp,"at":self.at,
                 "df":self.df,"mg":self.mg,"md":self.md,"sp":self.sp}
        return stats[param]
        
#--能力変化クラス--#
class BaseModifiers:
    def __init__(self):
        self.rate = {		
            -5:1/5 , -4:1/3 , -3:1/2 , -2:2/3 , -1:3/4 , 0:1 , 1:1.25 , 2:1.5 , 3:2 , 4:2.5 , 5:3
            }				#変化倍率定義
        self.at = 0			#攻撃
        self.df = 0			#防御
        self.mg = 0			#魔法
        self.md = 0			#魔防
        self.sp = 0			#俊敏
        
    #ステータス名を指定して倍率を取得
    def get_rate(self,param):
        return self.rate[self.get_modi()]
                
    #ステータス名を指定して変化値を取得
    def get_modi(self,param):
        stats = {"at":self.at,"df":self.df,"mg":self.mg,"md":self.md,"sp":self.sp}
        return stats[param]
        
#--状態変化クラス--#
class BaseStatusEffects:
    def __init__(self):
        self.effects = []
        
    #状態のターン経過
    def turn_check(self):
        #解除する状態リスト
        remove_effects = []
        #所持している状態のターンを1減少
        for i in range(len(self.effects)):
            self.effects[i].reduce_turn()
            turns_left = self.effects[i].get_turn()
            #残りターンが0の場合、状態を解除
            if self.turn is not None and turns_left <= 0:
                remove_effects.append(self.effects[i])
                self.effects.remove(self.effects[i])
        return remove_effects
                
        
    #指定の状態を持っているかを取得
    def is_enable(self,effect_name):
        return any(effect_name in sublist for sublist in self.effects)
    
#--技クラス--#
class BaseMoves:
    def __init__(self,moves):
        self.moves = moves

