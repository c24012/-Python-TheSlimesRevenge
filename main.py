import random,unicodedata,sys

#==========共有呼び出し関数==========#

#--成功確率--#
def hit_prob(x):
    return x >= random.randint(1,100)

#--コマンド選択--#
def select_command(text,max_num,exc=None,start=1,allow_empty=False):
    if exc == None:
        exc = []
    while(True):
        value = input(text)
        if not value:
            if allow_empty:
                return value
            continue
        try:
            if start <= int(value) <= max_num:
                return value
        except ValueError:
            if value in exc:
                return value

#--文字数取得(全角は2文字扱い)--#
def get_width_count(text):
    count = 0
    for c in text:
        count += 2 if unicodedata.east_asian_width(c) in 'FWA' else 1
    return count

#--横並びPrint表示--#
def con_print(*text,width,non_print=False):#24
    width_count = get_width_count(text[0])
    if non_print:
        return f"{text[0]}"+(" " * (width - width_count))+f"{text[1]}"
    else:
        print(text[0],end="")
        print(" " * (width - width_count),end="")
        print(text[1])
            
#--ゲージ表示--#
def gage_ui(value,max_value):
    percent = value/max_value
    if percent == 0:
        count = 0
    else:
        count = int(max(percent * 20,1))
    gage = "[" + ("/" * count) + ("-" * (20 - count)) + "]"
    return gage

#==========状態異常クラス==========#
class StatusEffect:
    
    def __init__(self,chara):
        self.chara = chara
        self.se = {}
        self.se_str = {}
        self.se_info = {}
        self.se_buff = {}
        #観察状態
        self.register('Observation',"観察状態","相手の動きを観察する")
        #精神崩壊状態
        self.register('MtBreak',"精神崩壊状態","防御と魔防が低下し行動不能になる",[("de",-1),("md",-1)])
        
    
    #--状態異常登録--#
    def register(self,key,name,info,buff=None):
        self.se[key] = -1
        self.se_str[key] = name
        self.se_info[key] = info
        if buff is not None:
            self.se_buff[key] = buff
    
    #--状態異常の付与確認--#
    def get_is_active(self,se_key):
        return self.se[se_key] > 0
    
    #--状態異常付与--#
    def give(self,se_key,turn):
        if self.se[se_key] != -1:
            input(f"{self.chara.name}はすでに{self.se_str[se_key]}になっている")
            return
        
        if se_key == 'Dodge':
            if self.chara.is_avoid:
                input(f"うまくいかなかった")
                return
            else:
                self.chara.is_avoid = True
        
        input(f"{self.chara.name}は{self.se_str[se_key]}になった")
        self.se[se_key] = turn
        self.set_buff_value()
    
    #--付与されてる状態異常を取得--#
    def get_name_list(self):
        active_se_list = []
        for key in self.se:
            if self.se[key] > 0:
                active_se_list.append([self.se_str[key],self.se[key],self.se_info[key]])
        return active_se_list
    
    #--ターン経過--#
    def turn_count(self):
        for key in self.se:
            if self.se[key] > 0:
                self.se[key] -= 1
                if self.se[key] == 0:
                    self.clear(key)
                
    #--状態異常解除--#
    def clear(self,se_key):
            
        self.se[se_key] = -1
        input(f"\n{self.chara.name}の{self.se_str[se_key]}がもどった")

        self.set_buff_value()
        
    #--バフ計算--#
    def set_buff_value(self):
        self.chara.buff = {"at":0,"df":0,"mg":0,"md":0,"sp":0}
        for key in self.se_buff:
            if self.get_is_active(key):
                for at_type,value in self.se_buff[key]:
                    self.chara.buff[at_type] += value
        for key in self.chara.buff:
            if self.chara.buff[key] > 3 :
                self.chara.buff[key] = 3
            elif self.chara.buff[key] < -3:
                self.chara.buff[key] = -3
                

#==========キャラ共有クラス===========#
class Chara:
    
    buff_power = {-3:1/4, -2:1/2, -1:3/4, 0:1, 1:1.25, 2:1.5, 3:2}
    
    def __init__(self,name,hp,at,df,mg,md,sp):
        #初期ステータス
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.at = at
        self.df = df
        self.mg = mg
        self.md = md
        self.sp = sp
        self.status = [hp,at,df,mg,md,sp]
        #ステータスバフ
        self.buff = {"at":0,"df":0,"mg":0,"md":0,"sp":0}
        #状態異常
        self.se = StatusEffect(self)
        #戦闘相手
        self.target = None
        #死亡しているか
        self.is_dead = False

    #--対戦相手を登録--#    
    def set_target(self,target):
        self.target = target
    
    #HPとMTを全回復
    def full_recovery(self):
        self.recovery_hp()
    
    #--体力回復--#
    def recovery_hp(self,value=-1,view=False):
        if value < 0:            #全回復
            self.hp = self.max_hp
            if view:
                input(f"{self.name}は体力が全回復した")
        else:                    #数値分回復
            if view:
                if self.hp == self.max_hp:
                    input(f"{self.name}の体力は満タンだ")
                else:
                    input(f"{self.name}は体力が{value}回復した")
            self.hp = min(self.max_hp, self.hp + value)
    
    #--攻撃--#
    def attack(self,atType,power=100):
        prob = 100
        hit = False
        #物理攻撃
        if atType == "at":
            if hit_prob(prob):   #成功確率
                    hit = self.target.damage(self.at * power / 100 + (self.at * self.buff_power[self.buff["at"]] - self.at), atType)
            else:
                    input(f"しかし、{self.target.name}に当たらなかった")
        #魔法攻撃            
        elif atType == "mg":     
            if hit_prob(prob):   #成功確率
                hit = self.target.damage(self.mg * power / 100 + (self.mg * self.buff_power[self.buff["mg"]] - self.mg), atType)
            else:
                input(f"しかし、{self.target.name}に当たらなかった")
        else :
            print("Error:atType値が想定外です atType:"+atType)
                
        return hit
        
    #--状態変化付与--#
    def give_se(self,se_key,se_turn,is_myself):
        prob = 100
        if is_myself: #自分自身
            self.se.give(se_key,se_turn)
        else:         #相手
            if hit_prob(prob): #成功確率
                self.target.se.give(se_key,se_turn)
            else:
                input(f"しかし、{self.target.name}に当たらなかった")
        
    #--ダメージ--#
    def damage(self,power,atType):
        
        if atType == "at":
            
            #回避状態は無効化
            if self.se.get_is_active('Dodge'):
                if not is_freeze_fear:
                    input(f"{self.name}は回避した")
                    counter_atk()
                    return False
                
            #フェイント状態は20%で無効化
            if self.se.get_is_active('Feint'):
                if hit_prob(20) and not is_freeze_fear:
                    input(f"{self.name}は回避した")
                    counter_atk()
                    return False
            
            scatter = random.uniform(0.9,1.1) #ダメージ乱数
            damage = int(max((power - (self.df  + (self.df * self.buff_power[self.buff["df"]] - self.df))/ 2) * scatter,1))
            self.hp -= damage
            input(f"{self.name}に{damage}のダメージ")
            self.check_dead()
            
        elif atType == "mg":
            
            scatter = random.uniform(0.9,1.1) #ダメージ乱数
            damage = int(max((power - (self.md  + (self.md * self.buff_power[self.buff["md"]] - self.md))/ 2) * scatter,1))
            self.hp -= damage
            input(f"{self.name}に{damage}のダメージ")
            self.check_dead()
            
        else:
            
            scatter = random.uniform(0.9,1.1) #ダメージ乱数
            self.mt -= int(power * scatter)
            input(f"{self.name}の精神力が{int(power * scatter)}削られた")
            self.check_break()
            
        return True
        
    #--死亡確認--#
    def check_dead(self):
        if self.hp <= 0:
            self.is_dead = True
            input(f"\n{self.name}はたおれた！")
            
    #--ターン開始--#
    def turn_start(self):
        
        #すでに死んでいたら動けない
        if self.is_dead:
            return
        
        print("\n==========================")
        print(f"{self.name}のターン")
        input("==========================")

        self.se.turn_count()

        #行動開始
        self.command()
        
    #--ターン終了時--#
    def turn_end(self):
        ##すでに死んでいたら何もせず終了
        if self.is_dead:
            return
        
    #--お互いのターン終了時--#
    def round_end(self):
        pass
        
    def command(self):
        pass
            
#==========共有行動データクラス==========#
class ActionBase:
    
    def __init__(self,chara):
        self.chara = chara
        self.at_cmd = []
        self.at_info = []
        self.datas = {"name":None, "type":None, "power":None, "prob":None, "myself":None, "se_key":None, "se_turn":None}
        
    #--技データの代入--#
    def set_datas(self,key,value):
        if key in self.datas:
            self.datas[key] = value
        else:
            sys.exit(f"Error:name:{self.chara.name} set_datas(key:{key},value:{value}) : key not found")
            
    #--datasの中身を初期化--#
    def reset_datas(self):
        for key in self.datas:
            self.datas[key] = None
        
    #--行動実行--#
    def perform(self,cmd):
        input(f"\n{self.chara.name}の{cmd.at_name}")
        hit = False
        if cmd.get_is_attack():
            hit = self.chara.attack(cmd.at_type,cmd.power)
        else:
            hit = True
            
        if cmd.get_is_se():
            self.chara.give_se(cmd.se_key,cmd.se_turn,cmd.is_myself)
    
    #--行動説明の一括追加--#
    def add_all_at_info(self):
        for cmd in self.at_cmd:
            self.at_info.append(
                [cmd.at_name,cmd.get_info(),cmd.get_se(),cmd.get_se_info()])
        
        
#==========共有コマンドデータクラス==========#
class CommandBase:
        
    type_str = {"at":"物理","mg":"魔法"}
    def __init__(self,act,datas):
        self.act = act                       #↓datas:入力例
        self.at_name = datas["name"]         #"スライム"
        self.at_type = datas["type"]         #"at"
        self.power = datas["power"]          #100
        self.is_myself = datas["myself"]     #True
        self.se_key = datas["se_key"]        #'MtBreak'
        self.se_turn = datas["se_turn"]      #2
        self.act.reset_datas()
            
    #--技の攻撃タイプ・威力・命中の詳細を取得--#
    def get_info(self):
        at_type_text = "" if self.at_type is None else f"{self.type_str[self.at_type]}"
        power_text = "" if self.power is None else f" 威力{self.power}"
        return at_type_text + power_text
        
    #--技の付与する状態変化の詳細を取得--#
    def get_se(self):
        if self.se_key is None:
            return "効果なし"
        se_name_text = f"{self.act.chara.se.se_str[self.se_key]}"
        se_turn_text = "" if self.se_turn is None else f"*{self.se_turn}ターン"
        if self.is_myself:
            return "[" + se_name_text + se_turn_text + "]を得る"
        else:
            return "相手に[" + se_name_text + se_turn_text + "]を付与"
    
    #--状態変化の効果の詳細を取得--#
    def get_se_info(self):
        if self.se_key is None:
            return ""
        return f"({self.act.chara.se.se_str[self.se_key]}:{self.act.chara.se.se_info[self.se_key]})"
            
    def get_is_attack(self):
        return self.at_type is not None
        
    def get_is_se(self):
        return self.se_key is not None
            
#==========プレイヤー(スライム)==========#
class Player(Chara):
    
    action_list = []
    status_list = {}
    
    def __init__(self):
        name = "スライム"
        hp = 50    #体力
        at = 20    #攻撃
        df = 20    #防御
        mg = 20    #魔攻
        md = 20    #魔防
        sp = 20    #俊敏
        super().__init__(name,hp,at,df,mg,md,sp)
        #行動の登録
        self.act_method = PlayerAct
        self.set_action(self)
        self.action = self.action_list[0]
        
    #--行動の登録(変身用)--#
    def set_action(self,act):
        self.action_list.append([act.act_method(self),act.name])
        self.status_list[act.name] = act.status
        
    #--ステータス代入--#
    def change_status(self,chara_name):
        hp_percent = self.hp / self.max_hp
        self.max_hp,self.at,self.df,self.mg,self.md,self.sp = self.status_list[chara_name]
        self.hp = max(int(self.max_hp * hp_percent), 1)
    
    #--行動選択--#
    def command(self):
        
        #--戦う--#
        def fight():
            #--詳細表示--#
            def hint():
                print("\n---------- 詳細 ----------")
                print(*[f"\n{cmd[0]} {cmd[1]}\n {cmd[2]} {cmd[3]}\n" for cmd in self.action[0].at_info],sep="")
                print("--------------------------")
                input("(もどる)")
                fight()
            
            print("\n---------- 戦う ----------")
            print("\n".join(f"{num}: {cmd[0]}" for num,cmd in enumerate(self.action[0].at_info,start=1)))
            print("0: もどる")
            print("--------------------------")
            select = select_command("なにをする？（詳細:*）：",len(self.action[0].at_cmd),exc=["*"],start=0)
            if select == "*":
                hint()
            elif select == "0":
                self.command()
            else:
                self.action[0].perform(self.action[0].at_cmd[int(select) - 1])
        
        #--ステータス表示--#
        def confirmation():
            #--状態変化一覧表示--#
            def se_all_view(width):
                list_p = self.se.get_name_list()
                list_t = self.target.se.get_name_list()
                for i in range(max(len(list_p),len(list_t),1)):
                    text_p = f"-{list_p[i][0]} あと{list_p[i][1]}" if i < len(list_p) else ""
                    text_t = f"-{list_t[i][0]} あと{list_t[i][1]}" if i < len(list_t) else ""
                    con_print(text_p,text_t,width=width)
                
            #--詳細表示--#
            def hint():
                list_p = self.se.get_name_list()
                list_t = self.target.se.get_name_list()
                print(f"\n{self.name}")
                for i in range(len(list_p)):
                    print(f"{list_p[i][0]}\n 効果:{list_p[i][2]}")
                print(f"\n{self.target.name}")
                for i in range(len(list_t)):
                    print(f"{list_t[i][0]}\n 効果:{list_t[i][2]}")
                input("\n(Enter:もどる)")
                   
            #--名前を表示--#
            def name_tag(name): 
                SIZE = 24
                width = get_width_count(name)
                line_count = (SIZE - width) // 2
                return f"{'-'*line_count}{name}{'-'*line_count}"
            
            def baff(buff_key,para,enemy=False):
                if enemy:
                    if self.target.buff[buff_key] == 0:
                        return ""
                    value = int(para * self.target.buff_power[self.target.buff[buff_key]]) - para
                    return ("+" if value > 0 else "") + f"{value}"
                else:
                    if self.buff[buff_key] == 0:
                        return ""
                    value = int(para * self.buff_power[self.buff[buff_key]]) - para
                    return ("+" if value > 0 else "") + f"{value}"
                
            print()
            con_print(name_tag(f"{self.name}({self.action[1]})"),name_tag(self.target.name),width=30)
            con_print(f"体力  {self.hp}/{self.max_hp}",f"体力  {self.target.hp}/{self.target.max_hp}",width=30)
            con_print(f"{gage_ui(self.hp,self.max_hp)}",f"{gage_ui(self.target.hp,self.target.max_hp)}",width=30)
            con_print(con_print(f"攻撃  {self.at}",baff('at',self.at),width=11,non_print=True),
                      con_print(f"攻撃  {self.target.at}",baff('at',self.target.at,True),width=11,non_print=True),width=30)
            con_print(con_print(f"防御  {self.df}",baff('df',self.df),width=11,non_print=True),
                      con_print(f"防御  {self.target.df}",baff('df',self.target.df,True),width=11,non_print=True),width=30)
            con_print(con_print(f"魔攻  {self.mg}",baff('mg',self.mg),width=11,non_print=True),
                      con_print(f"魔攻  {self.target.mg}",baff('mg',self.target.mg,True),width=11,non_print=True),width=30)
            con_print(con_print(f"魔防  {self.md}",baff('md',self.md),width=11,non_print=True),
                      con_print(f"魔防  {self.target.md}",baff('md',self.target.md,True),width=11,non_print=True),width=30)
            con_print(con_print(f"俊敏  {self.sp}",baff('sp',self.sp),width=11,non_print=True),
                      con_print(f"俊敏  {self.target.sp}",baff('sp',self.target.sp,True),width=11,non_print=True),width=30)
            con_print(" - - - - - - - - - - - -"," - - - - - - - - - - - -",width=30)
            con_print("状態変化","状態変化",width=30)
            se_all_view(width=30)
            con_print("------------------------","------------------------",width=30)
            
            select = input("(もどる *:詳細):")
            if select == "*":
                hint()
                
            self.command()
        
        
        #--行動選択--#
        print("")
        con_print(f"-{self.name}-",f"-{self.target.name}-",width=30)
        con_print(f"体力{gage_ui(self.hp,self.max_hp)}",f"体力{gage_ui(self.target.hp,self.target.max_hp)}",width=30)
        print("\n---------- 行動 ----------")
        print("\n".join(["1: 戦う","2: ステータス","3：持ち物"]))
        print("--------------------------")
        select = select_command("なにをする？：",4)
        if select == "1":    #戦う
            fight()
        elif select == "2":  #ステータス
            confirmation()
        elif select == "3":  #持ち物
            #持ち物表示
            pass
            
    #--お互いのターン終了時--#
    def round_end(self):
        super().round_end()
     
#==========行動:スライム==========#
class PlayerAct(ActionBase):
    
    def __init__(self,chara):
        super().__init__(chara)
        self.at_cmd.append(self.normal_atk())   #こうげき
        self.at_cmd.append(self.jumping())      #飛び跳ねる
        self.at_cmd.append(self.regenerate())   #自己再生 
        self.add_all_at_info()
        
    #--こうげき--#
    def normal_atk(self):
        self.set_datas("name","たいあたり")
        self.set_datas("type","at")
        self.set_datas("power",100)
        return CommandBase(self,self.datas)
    
    #--飛び跳ねる--#
    def jumping(self):
        self.set_datas("name","飛び跳ねる")
        self.set_datas("myself",True)
        self.set_datas("se_turn",1)
        return CommandBase(self,self.datas)
    
    #--自己再生--#
    def regenerate(self):
        self.set_datas("name","自己再生")
        self.set_datas("myself",True)
        self.set_datas("se_turn",3)
        return CommandBase(self,self.datas)
    
#==========ゴブリン==========#
class Goblin(Chara):
    def __init__(self):
        name = "ゴブリン"
        hp = 70    #体力
        mt = 35    #精神力
        at = 25    #攻撃
        df = 20    #防御
        mg = 10    #魔攻
        md = 15    #魔防
        sp = 20
        super().__init__(name,hp,at,df,mg,md,sp)
        #行動登録
        self.action = GoblinAct(self)
        self.act_method = GoblinAct
        self.turn_count = -1
        
    #--行動--#
    def command(self):
        self.turn_count = ( self.turn_count + 1 ) % 4
        #順番に行動
        if self.turn_count == 0:
            choice_act = self.action.at_cmd[0]
        elif self.turn_count == 1:
            choice_act = self.action.at_cmd[2]
        elif self.turn_count == 2:
            choice_act = self.action.at_cmd[1]
        else :
            input(f"\n{self.name}は様子を見ている")
            return
        self.action.perform(choice_act)
        
    #--観察結果取得--#
    def observation(self):
        #怒ってとびかかってきた
        if self.se.get_is_active('MastRecharge') and self.se.get_is_active('Angry'):
            return f"飛びかかってきた！怒ると飛びかかる習性があるらしい"
        #反動で動けない
        elif self.se.get_is_active('MastRecharge'):
            return f"飛びかかってきた後は疲れて動けないようだ"
        #怒った
        elif self.se.get_is_active('Angry'):
            return f"{self.name}は怒って飛びつきの構えをしている"
        #その他
        else:
            return f"{self.name}の攻撃手段は手に持っているこん棒が主のようだ"
        
#==========行動:ゴブリン==========#
class GoblinAct(ActionBase):
    
    def __init__(self,chara):
        super().__init__(chara)
        self.at_cmd.append(self.normal_atk())   #こうげき
        self.at_cmd.append(self.jumping_atk())  #飛びかかる
        self.at_cmd.append(self.charge_power()) #怒る
        self.add_all_at_info()
        
    #--こうげき--#
    def normal_atk(self):
        self.set_datas("name","なぐる")
        self.set_datas("type","at")
        self.set_datas("power",100)
        return CommandBase(self,self.datas)
    
    #--飛びかかる--#
    def jumping_atk(self):
        self.set_datas("name","とびかかる")
        self.set_datas("type","at")
        self.set_datas("power",130)
        self.set_datas("myself",True)
        self.set_datas("se_turn",2)
        return CommandBase(self,self.datas)
    
    #--怒る--#
    def charge_power(self):
        self.set_datas("name","怒る")
        self.set_datas("myself",True)
        self.set_datas("se_turn",2)
        return CommandBase(self,self.datas)

#==========戦闘==========#
def battle(player,enemy):
    #それぞれの対象を登録
    player.set_target(enemy)
    enemy.set_target(player)
    charas = [player,enemy]
    #どちらかが倒れるまでターン続行
    while(True):
        for chara in charas:
            chara.turn_start()
            chara.turn_end()
            if chara.is_dead:
                if chara == player:
                    print("\n==========================")
                    print(f"{player.name}の旅はここで幕を閉じた..")
                    print("==========================")
                    input()
                    return False
                else:
                    print("\n==========================")
                    print(f"{enemy.name}との勝負に勝った！")
                    print("==========================")
                    input()
                    return True
        #ラウンドが1巡したことを通知
        for chara in charas:
            chara.round_end()
    
    
#==========Main==========#
print("#===== プログラム開始 =====#")
player = Player()
enemys = []
enemys.append(Goblin())

for enemy in enemys:
    player.set_action(enemy)
    
print("\n--------------------------")
print("\n".join(f"{num}: {enemy.name}" for num,enemy in enumerate(enemys,start=1)))
print("--------------------------")
            
select = select_command("誰と戦う？",len(enemys))
battle(player,enemys[int(select) - 1])
print("#===== プログラム終了 =====#")


