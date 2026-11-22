from ui import Panel,Text

panel = Panel()
text = Text()
floor_text = {1:" 1",2:" 2",3:" 3",4:" 4",5:" 5",6:" 6",7:" 7",8:" 8",9:" 9",10:"最上"}

class FloorUI:
    def __init__(self,player,floor):
        self.player = player
        self.floor = floor
            
    def get_f(self):
        return floor_text[self.floor[0]]
    
    #--入り--#
    def enter_floor(self,redo=False):
        texts = []
        texts.append([3,text.center(f"{self.player.name}は{self.get_f()}階にたどり着いた")])
        texts.append([7,text.text("(Enter)",head=40)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,f"{self.get_f()}階",redo)
        
    #--休憩部屋--#
    def bleak_room(self,hp,st,redo=False):
        texts = []
        texts.append([1,text.text(f"上に進む階段を見つけた！",head=1)])
        texts.append([3,text.text(f"{self.player.name}は少し休憩して次の階へ進んだ",head=1)])
        i = 4
        if hp > 0:
            texts.append([i,text.text(f"HPが{hp}回復した",head=2)])
            i += 1
        if st > 0:
            texts.append([i,text.text(f"STが{st}回復した",head=2)])
        texts.append([7,text.text("(Enter)",head=40)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,f"{self.get_f()}階",redo)
        
    #-- ↓ プレイヤーのコマンド選択 ↓ --#
        
    #--行動選択--#
    def select_action(self,redo=False):
        texts = []
        texts.append([1,text.text("なにをする？",head=1)])
        texts.append([3,text.horiz(["1: 戦闘","2: お宝採集","3: 探索"],head=3)])
        texts.append([5,text.horiz(["4: 技確認","5: 能力確認","6: お宝確認"],head=3)])
        texts.append([7,text.text("(0:リタイア)",head=1)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,f"{self.get_f()}階",redo)
        
    #--技確認--#
    def move_list(self,page,redo=False):
        
        moves = self.player.moves.moves[0+(page*9):9+(page*9)]
        move_texts = [""]*9
        for i in range(9):
            if len(moves) > i:
                move_texts[i] = (f"{i+1}:{text.tab(moves[i].name,f'ST{moves[i].st}',width=15)}")
        max_page = len(self.player.moves.moves) // 9 + 1
                
        texts = []
        texts.append([1,text.horiz([move_texts[0],move_texts[5]],head=1)])
        texts.append([2,text.horiz([move_texts[1],move_texts[6]],head=1)])
        texts.append([3,text.horiz([move_texts[2],move_texts[7]],head=1)])
        texts.append([4,text.horiz([move_texts[3],move_texts[8]],head=1)])
        texts.append([5,text.horiz([move_texts[4],""],head=1)])
        texts.append([6,text.text("(番号:詳細)",head=36)])
        texts.append([7,text.horiz_alignment("(b:前,0:もどる)",f"{page+1} / {max_page}","(Enter:次)")])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"技確認",redo)
        
    #--技詳細--#
    def move_info(self,move,redo=False):
        power = f"{move.power}" if move.category != "特殊" else " -"
        acc = f"{move.acc}" if move.category == "物理" else " -"
        
        texts = []
        texts.append([1,
            text.horiz_free([[f"[ {move.name} ]",1],[f"{move.category}",22],
                                            [f"威力:{power}",28],[f"命中:{acc}",38]])])
        
        for i in range(len(move.info)):
            texts.append([3+i,text.text(move.info[i],head=2)])
            
        if move.effects is not None:
            effect_texts = ""
            effect_texts += f"(1:{move.effects[0].instance_effect().name}"
            if len(move.effects) == 2:
                effect_texts += f",2:{move.effects[0].instance_effect().name}"
            effect_texts += ")"
            texts.append([6,text.horiz_free([[effect_texts,2],["(番号:詳細)",36]])])
        
        texts.append([7,text.text("(Enter)",head=40)])
        
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"技詳細",redo)
        
    #--技の付与状態詳細--#
    def status_effect_info_from_move(self,effect_class,redo=False):

        effect = effect_class.instance_effect()

        type_text =""
        if effect.turn is not None and effect.level is not None:
            type_text = "ターンX , Lv:X"
        elif effect.turn is not None:
            type_text = "ターンX"
        else:
            type_text = "Lv:X"
        
        texts = []
        texts.append([1,text.horiz_free([[f"[ {effect.name} ]",1],[type_text,20]])])
        
        for i in range(len(effect.info)):
            texts.append([3+i,text.text(effect.info[i],head=3)])
        
        texts.append([7,text.text("(Enter)",head=40)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"状態詳細",redo)
        
    #--能力確認--#
    def check_stats(self,redo=False):
        #表示するデータを取得
        base = self.player.base_stats.get_all_state()
        modi = self.player.get_treasures_stats()
        
        modi = {k:(f"+{v}" if v >= 0 else f"{v}") for k,v in modi.items()}
        
        texts = []
        texts.append([1,text.horiz([text.tab(f"(基礎)","(お宝)",width=11),text.tab(f"(基礎)","(お宝)",width=11)],head=2)])
        texts.append([2,text.horiz([text.tab_right(text.tab_right("HP",f"{base['max_hp']}",width=6),f"{modi['max_hp']}",width=8),
                                    text.tab_right(text.tab_right("ST",f"{base['max_st']}",width=6),f"{modi['max_st']}",width=8)],head=2)])
        
        texts.append([4,text.horiz([text.tab_right(text.tab_right("攻撃",f"{base['at']}",width=4),f"{modi['at']}",width=8),
                                    text.tab_right(text.tab_right("防御",f"{base['df']}",width=4),f"{modi['df']}",width=8)],head=2)])
        texts.append([5,text.horiz([text.tab_right(text.tab_right("魔力",f"{base['mg']}",width=4),f"{modi['mg']}",width=8),
                                    text.tab_right(text.tab_right("魔防",f"{base['md']}",width=4),f"{modi['md']}",width=8)],head=2)])
        texts.append([6,text.tab_right(text.tab_right("俊敏",f"{base['sp']}",width=4),f"{modi['sp']}",width=8,head=2)])
        
        texts.append([7,text.text("(Enter)",head=40)])
        
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"能力確認",redo)
        
    #--お宝確認--#
    def treasures_list(self,page,redo=False):
        
        treasures = self.player.treasures.treasures[0+(page*9):9+(page*9)]
        treasure_texts = [""]*9
        for i in range(9):
            if len(treasures) > i:
                treasure_texts[i] = (f"{i+1}:{treasures[i].name}")
        max_page = len(self.player.treasures.treasures) // 9 + 1
                
        texts = []
        texts.append([1,text.horiz([treasure_texts[0],treasure_texts[5]],head=1)])
        texts.append([2,text.horiz([treasure_texts[1],treasure_texts[6]],head=1)])
        texts.append([3,text.horiz([treasure_texts[2],treasure_texts[7]],head=1)])
        texts.append([4,text.horiz([treasure_texts[3],treasure_texts[8]],head=1)])
        texts.append([5,text.horiz([treasure_texts[4],""],head=1)])
        texts.append([6,text.text("(番号:詳細)",head=36)])
        texts.append([7,text.horiz_alignment("(b:前,0:もどる)",f"{page+1} / {max_page}","(Enter:次)")])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"お宝確認",redo)
        
    #--お宝詳細--#
    def treasure_info(self,treasure,redo=False):
        texts = []
        texts.append([1,text.text(f" [ {treasure.name} ]")])
        
        for i in range(len(treasure.info)):
            texts.append([3+i,text.text(treasure.info[i],head=2)])
            
        if treasure.effects is not None:
            effect_texts = ""
            effect_texts += f"(1:{treasure.effects[0].instance_effect().name}"
            if len(treasure.effects) == 2:
                effect_texts += f",2:{treasure.effects[0].instance_effect().name}"
            effect_texts += ")"
            texts.append([6,text.horiz_free([[effect_texts,2],["(番号:詳細)",36]])])
        
        texts.append([7,text.text("(Enter)",head=40)])
        
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"お宝詳細",redo)
    
    #--お宝の付与状態詳細--#
    def status_effect_info_from_treasure(self,effect_class,redo=False):

        effect = effect_class.instance_effect()

        type_text =""
        if effect.turn is not None and effect.level is not None:
            type_text = "ターンX , Lv:X"
        elif effect.turn is not None:
            type_text = "ターンX"
        else:
            type_text = "Lv:X"
        
        texts = []
        texts.append([1,text.horiz_free([[f"[ {effect.name} ]",1],[type_text,20]])])
        
        for i in range(len(effect.info)):
            texts.append([3+i,text.text(effect.info[i],head=3)])
        
        texts.append([7,text.text("(Enter)",head=40)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,"状態詳細",redo)
    
    #-- ↓ シーン共通関数 ↓ --#
        
    #--シーン--#
    def get_scene(self,player):
        #各行のテキスト作成
        texts = []
        texts.append([1,text.text(f"-魔王城:{self.get_f()}階-")])
        texts.append([3,text.text(f"{player.name}",head=1)])
        texts.append([4,text.tab(text.tab_right("HP:",f"{player.stats.hp}/{player.stats.max_hp}",width=9),
                                 text.gage(player.stats.hp,player.stats.max_hp),width=13,head=1)])
        texts.append([5,text.tab(text.tab_right("ST:",f"{player.stats.st}/{player.stats.max_st}",width=9),
                                 text.gage(player.stats.st,player.stats.max_st),width=13,head=1)])

        #改行を挿入
        result = text.place_strings_at_lines(texts,line_count=7)
        return result
    
    #--UIを表示--#
    def show_panel(self,info,frame,redo):
        #シーンテキストを取得
        scene = self.get_scene(self.player)
        #パネルにシーンテキスト、詳細テキスト、フレームテキストを設定
        panel.set_panel(scene,info,frame)
        #パネルを画面に表示
        panel.view(redo)
