class BaseStatusEffect:
    def __init__(self,turn=None,level=None,info=""):
        self.turn = turn
        self.level = level
        self.info = info
        self.modifier = None
             
    #能力変化登録
    def set_modifier(self,at=0,df=0,mg=0,md=0,sp=0):
        self.modifier = {"at":at,"df":df,"mg":mg,"md":md,"sp":sp}
        
    #ターン経過
    def reduce_turn(self):
        if self.turn is not None:
            self.turn -= 1
            
    #残りターン取得
    def get_turn(self):
        return self.turn
    
    #ターン開始
    def on_action_start(self):
        pass
    #自分のターン開始
    def on_turn_start(self):
        pass
    #自分のターン終了
    def on_turn_end(self):
        pass
    #ターン終了
    def on_action_end(self):
        pass