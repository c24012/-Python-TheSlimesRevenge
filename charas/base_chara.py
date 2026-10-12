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
        if param == "hp":
            return self.at
        elif param == "max_hp":
            return self.at
        elif param == "at":
            return self.at
        elif param == "df":
            return self.df
        elif param == "mg":
            return self.mg
        elif param == "md":
            return self.md
        elif param == "sp":
            return self.sp
        else:
            raise Exception("想定外の引数です")
        
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
        if param == "at":
            return self.rate[self.at]
        elif param == "df":
            return self.rate[self.df]
        elif param == "mg":
            return self.rate[self.mg]
        elif param == "md":
            return self.rate[self.md]
        elif param == "sp":
            return self.rate[self.sp]
        else:
            raise Exception("想定外の引数です")
                
    #ステータス名を指定して変化値を取得
    def get_modi(self,param):
        if param == "at":
            return self.at
        elif param == "df":
            return self.df
        elif param == "mg":
            return self.mg
        elif param == "md":
            return self.md
        elif param == "sp":
            return self.sp
        else:
            raise Exception("想定外の引数です")
        
#--状態変化クラス--#
class BaseStatusEffects:
    def __init__(self):
        self.effects = []
        
    #指定の状態を持っているかを取得
    def is_enable(self,effect_name):
        return any(effect_name in sublist for sublist in self.effects)
    
#--技クラス--#
class BaseMoves:
    def __init__(self,moves):
        self.moves = moves

        
    
    
        