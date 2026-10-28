from ui import Panel,Text

panel = Panel()
text = Text()

class FloorUI:
    def __init__(self,player,floor):
        self.player = player
        self.floor = floor
        self.floor_text = {1:"１",2:"２",3:"３",4:"４",5:"５",6:"６",7:"７",8:"８",9:"９",10:"最上"}
            
    def get_f(self):
        return self.floor_text[self.floor[0]]
    
    #--入り--#
    def enter_floor(self,redo=False):
        texts = []
        texts.append([3,text.center(f"{self.player.name}は{self.get_f()}階にたどり着いた")])
        texts.append([7,text.text("(Enter)",head=40)])
        #改行を挿入
        info = text.place_strings_at_lines(texts,line_count=8)
        self.show_panel(info,redo)
        
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
        self.show_panel(info,redo)
        
    #-- ↓ シーン共通関数 ↓ --#
        
    #--シーン--#
    def get_scene(self,player):
        #各行のテキスト作成
        texts = []
        texts.append([1,text.text(f"-魔王城:{self.get_f()}階-")])
        texts.append([3,text.text(f"{player.name}",head=1)])
        texts.append([4,text.tab(text.tab_right("HP:",f"{player.stats.hp}/{player.stats.max_hp}",width=9),
                                 text.gage(player.stats.hp,player.stats.max_hp),width=13,head=1)])
        texts.append([5,text.tab(text.tab_right("TP:",f"{player.stats.tp}/{player.stats.max_tp}",width=9),
                                 text.gage(player.stats.tp,player.stats.max_tp),width=13,head=1)])

        #改行を挿入
        result = text.place_strings_at_lines(texts,line_count=7)
        return result
    
    #--UIを表示--#
    def show_panel(self,info,redo):
        #シーンテキストを取得
        scene = self.get_scene(self.player)
        #パネルにシーンテキスト、詳細テキスト、フレームテキストを設定
        panel.set_panel(scene,info,f"{self.get_f()}階")
        #パネルを画面に表示
        panel.view(redo)
