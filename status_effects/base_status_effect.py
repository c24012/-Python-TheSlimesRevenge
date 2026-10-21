class BaseStatusEffect:
    def __init__(self,name,turn=None,level=None,info=""):
        self.name = name
        self.turn = turn
        self.level = level
        self.info = info
        self.set_modifier()
             
    #能力変化登録
    def set_modifier(self,at=0,df=0,mg=0,md=0,sp=0):
        self.modifier = {"at":at,"df":df,"mg":mg,"md":md,"sp":sp}
        
    #効果詳細を取得
    def get_status_effect_info(self):
        if self.info != "":
            return self.info
        elif any(value != 0 for value in self.modifier.values()):
            lv_text = ""
            param_text = {"at":"攻撃lv","df":"防御lv","mg":"魔法lv","md":"魔防lv","sp":"俊敏lv"}
            for param in self.modifier:
                if self.modifier[param] != 0:
                    lv_text += "" if lv_text == "" else ","
                    lv_text += param_text[param]+ ("+" if self.modifier[param] > 0 else "") + f"{self.modifier[param]}"
            return lv_text
        else:
            return ""
        
    #ターン経過
    def reduce_turn(self):
        if self.turn is not None:
            self.turn -= 1
            
    #残りターン取得
    def get_turn(self):
        return self.turn
    
    #能力変化取得
    def get_modifier(self):
        print([self.modifier[x] for x in self.modifier])
        return [self.modifier[x] for x in self.modifier]
    
    #ターン開始
    def on_turn_start(self):
        pass
    #ターン終了
    def on_turn_end(self):
        pass
    #自分のターン開始
    def on_action_start(self):
        pass
    #自分のターン終了
    def on_action_end(self):
        pass