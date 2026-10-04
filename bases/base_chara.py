class BaseChara:
    def __init__(self):
        self.name = None			#キャラ名
        self.stats = None			#能力値
        self.modifiers = None		#バフ,デバフ
        self.status_effects = None	#状態変化
        self.move = None			#技
        
    def set_name(self,name):
        self.name = name
    
    def set_stats(self,stats):
        self.stats = stats
        
    def set_move(self,move):
        self.move = move