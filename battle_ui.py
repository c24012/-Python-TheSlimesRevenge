from ui import Panel,Text

panel = Panel()
text = Text()

class BattleUI:
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy
                
    #--遭遇--#
    def encount(self,redo=False):
        texts = []
        texts.append([2,text.center(f"{self.enemy.name}が現れた！")])
        texts.append([5,text.center(self.enemy.encount_mess)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--被ダメージ--#
    def damage(self,value,target,factor_text,redo=False):
        texts = []
        texts.append([2,text.text(factor_text,3)])
        texts.append([4,text.text(f"{target.name}は{value}のダメージ！",3)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--被ダメージ(0ダメージ)--#
    def damage_zero(self,target,factor_text,redo=False):
        texts = []
        texts.append([2,text.text(factor_text,3)])
        texts.append([4,text.text(f"{target.name}はダメージを受けていない！",3)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--体力回復--#
    def recovery_hp(self,value,target,factor_text,redo=False):
        texts = []
        texts.append([2,text.text(factor_text,3)])
        texts.append([4,text.text(f"{target.name}は{value}回復した！",3)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--技を外す--#
    def missed(self,target,factor_text,redo=False):
        texts = []
        texts.append([2,text.text(factor_text,3)])
        texts.append([4,text.text(f"{target.name}に当たらなかった！",3)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--技を回避--#
    def dodged(self,target,factor_text,redo=False):
        texts = []
        texts.append([2,text.text(factor_text,3)])
        texts.append([4,text.text(f"{target.name}は回避した！",3)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--状態付与--#
    def add_status_effect(self,effect,target,redo=False):
        texts = []
        texts.append([3,text.text(f"{target.name}は{effect.name}状態になった！",3)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--状態解除--#
    def removed_status_effect(self,effect,is_player,redo=False):
        target = self.player if is_player else self.enemy
        texts = []
        texts.append([3,text.text(f"{target.name}の{effect.name}の効果が消えた",3)])
        texts.append([7,text.horiz_right(["(Enter)",""],head=47)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #-- ↓ プレイヤーのコマンド選択 ↓ --#
        
    #--行動選択--#
    def select_action(self,redo=False):
        texts = []
        texts.append([1,f" {self.player.name}の行動"])
        texts.append([3,text.horiz(["1: 戦う","2: 状態変化"],head=2)])
        texts.append([5,text.horiz(["3: 能力確認","4: お宝確認"],head=2)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--戦う--#
    def move_list(self,page,redo=False):
        
        moves = self.player.moves[0+(page*9):9+(page*9)]
        move_texts = [""]*9
        for i in range(9):
            if len(moves) > i:
                move_texts[i] = (f"{i+1}:{text.tab(moves[i].name,f'TP{moves[i].tp}',width=15)}")
        max_page = len(self.player.moves) // 9 + 1
                
        texts = []
        texts.append([1,text.horiz([move_texts[0],move_texts[5]],head=1)])
        texts.append([2,text.horiz([move_texts[1],move_texts[6]],head=1)])
        texts.append([3,text.horiz([move_texts[2],move_texts[7]],head=1)])
        texts.append([4,text.horiz([move_texts[3],move_texts[8]],head=1)])
        texts.append([5,text.horiz([move_texts[4],""],head=1)])
        texts.append([6,text.horiz_right(["(詳細:*[番号])",""],head=47)])
        texts.append([7,text.horiz_alignment("(b:前,0:もどる)",f"{page+1} / {max_page}","(Enter:次)")])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"技選択",redo)
        
    #--技詳細--#
    def move_info(self,page,num,redo=False):
        
        move = self.player.moves[page*9 + num - 1]
        power = f"{move.power}" if move.category != "特殊" else " -"
        acc = f"{move.acc}" if move.category == "物理" else " -"
        
        texts = []
        texts.append([1,
            text.horiz_free([[f"[ {move.name} ]",1],[f"{move.category}",22],
                                            [f"威力:{power}",28],[f"命中:{acc}",38]])])
        texts.append([3,text.text(move.info,2)])
            
        if move.effects is not None:
            texts.append([5,text.text(f"(回復するよ)",head=2)])
            if len(move.effects) == 2:
                texts.append([6,text.text(f"(回復しないかも)",head=2)])
                
        texts.append([7,text.text("(Enter)",head=40)])
        
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"技詳細",redo)
        
    #--状態変化確認 対象選択--#
    def select_check_status_effect(self,redo=False):
        texts = []
        texts.append([1,f" {self.player.name}の行動"])
        texts.append([3,text.text("1: 自分の状態変化を確認",head=2)])
        texts.append([5,text.text("2: 相手の状態変化を確認",head=2)])
        texts.append([7,text.text("(0:もどる)",head=3)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"戦闘",redo)
        
    #--状態変化確認--#
    def check_status_effect(self,page,is_player,redo=False):
        if is_player:
            effects = self.player.status_effects.effects[0+(page*5):5+(page*5)]
            max_page = len(self.player.status_effects.effects) // 5 + 1
        else:
            effects = self.enemy.status_effects.effects[0+(page*5):5+(page*5)]
            max_page = len(self.enemy.status_effects.effects) // 5 + 1
        
        level_texts = [""]*5
        left_turn_texts = [""]*5
        for i in range(len(effects)):
            if effects[i].level is None:
                pass
            else:
                level_texts[i] = f"Lv{effects[i].level}"
            if effects[i].turn is None:
                left_turn_texts[i] = f"残り∞ターン"
            else:
                left_turn_texts[i] = f"残り{effects[i].turn}ターン"
        
        effects_texts = [""]*5
        for i in range(5):
            if len(effects) > i:
                effects_texts[i] = (f"{i+1}" + ":" +
                     text.horiz_free([[effects[i].name,0],[level_texts[i],20],[left_turn_texts[i],25]]))
                
        texts = []
        texts.append([1,text.text(effects_texts[0],head=1)])
        texts.append([2,text.text(effects_texts[1],head=1)])
        texts.append([3,text.text(effects_texts[2],head=1)])
        texts.append([4,text.text(effects_texts[3],head=1)])
        texts.append([5,text.text(effects_texts[4],head=1)])
        texts.append([6,text.horiz_right(["(詳細:*[番号])",""],head=47)])
        texts.append([7,text.horiz_alignment("(b:前,0:もどる)",f"{page+1} / {max_page}","(Enter:次)")])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"状態変化 "+(self.player.name if is_player else self.enemy.name),redo)
        
    #--能力確認--#
    def check_stats(self,redo=False):
        #-[+,-]の表示-#
        def modi_text(level):
            if level > 0:
                return "+" * level
            elif level < 0:
                return "-" * abs(level)
            else:
                return ""
            
        #表示するデータを取得
        stats_text = ("攻撃","防御","魔力","魔防","俊敏")
        stats_type = ("at","df","mg","md","sp")
        player_stats = [self.player.stats.get_state(_type) for _type in stats_type]
        player_modi = [self.player.modifiers.get_modi(_type) for _type in stats_type]
        enemy_stats = [self.enemy.stats.get_state(_type) for _type in stats_type]
        enemy_modi = [self.enemy.modifiers.get_modi(_type) for _type in stats_type]
        
        texts = []
        texts.append([1,text.horiz([f"[{self.player.name}]",f"[{self.enemy.name}]"],head=2)])
        for i in range(5):
            texts.append([i+2,text.horiz([text.tab(f"{stats_text[i]} {player_stats[i]}",f"{modi_text(player_modi[i])}",width=10),
                                    text.tab(f"{stats_text[i]} {enemy_stats[i]}",f"{modi_text(enemy_modi[i])}",width=10)],head=2)])
        texts.append([7,text.text("(Enter)",head=40)])
        
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"能力確認",redo)
    
    #-- ↑ プレイヤーのコマンド選択 ↑ --#
        
        
    #--シーン(共通)--#
    def get_scene(self,player,enemy):
        #各行のテキスト作成
        texts = []
        texts.append([1,text.horiz([player.name,enemy.name])])
        texts.append([2,text.horiz([f"HP{text.gage(player.stats.hp,player.stats.max_hp)}",
                                   f"HP{text.gage(enemy.stats.hp,enemy.stats.max_hp)}"])])
        texts.append([3,text.horiz_right([f"{player.stats.hp}/{player.stats.max_hp}",
                                    f"{enemy.stats.hp}/{enemy.stats.max_hp}"],head=22)])
        texts.append([4,text.horiz([f"TP{text.gage(player.stats.tp,player.stats.max_tp)}",""])])
        texts.append([5,text.horiz_right([f"{player.stats.tp}/{player.stats.max_tp}",""],head=22)])

        #改行を挿入
        result = text.place_strings_at_lines(texts,line_count=7)
        return result
    
    #--UIを表示--#
    def show_panel(self,info,frame,redo):
        #シーンテキストを取得
        scene = self.get_scene(self.player,self.enemy)
        #パネルにシーンテキスト、詳細テキスト、フレームテキストを設定
        panel.set_panel(scene,info,frame)
        #パネルを画面に表示
        panel.view(redo)
