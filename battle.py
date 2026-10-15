from common import enter
from battle_ui import BattleUI
from datastores.chara_datastore import CharaDataStore

chara = CharaDataStore()

class Battle:
    def __init__(self,player,enemy):
        self.ui = BattleUI(player,enemy)
        self.player = player
        self.enemy = enemy
        self.start()
    
    def start(self):
        #遭遇
        self.encount()
        #プレイヤーの行動選択へ
        self.select_action()
        #状態チェック
        #self.status_effects_check()
        #敵の行動実行
        self.enemy_action()
        #状態チェック
        #self.status_effects_check()
        
    #--遭遇--#
    def encount(self):
        #UI表示
        enter(self.ui.encount)
    
    #--敵の行動--#
    def enemy_action(self):
        pass
    
    #--状態チェック--#
    def status_effects_check(self):
        pass
        
        
    #-- ↓ プレイヤーのコマンド選択 ↓ --#
        
    #--行動選択--#
    def select_action(self):
        #UI表示
        result = enter(self.ui.select_action,max_num=4)
        
        # <1:戦う> 技選択へ
        if result == 1:
            self.move_list(page=0)
        # <2:状態変化> 状態変化確認へ
        elif result == 2:
            pass
        # <3:能力確認> ステータス確認へ
        elif result == 3:
            self.check_stats()
        # <4:お宝確認> お宝確認へ
        elif result == 4:
            pass
            
    #--攻撃技選択--# 
    def move_list(self,page):
        
        #{page}ページの技の数
        move_count = len(self.player.moves) - (page * 9)
        #次のページがあるか確認
        not_last = ((page + 1) != (len(self.player.moves) // 9 + 1))
        #前のページがあるか確認
        not_first = (page != 0)
        
        #UI表示
        result = enter(self.ui.move_list,max_num=move_count,args=[page],
                       is_info=True,is_back=True,is_next=not_last,is_before=not_first)
        
        if isinstance(result,str):
            # "":次のページへ
            if result == "":
                self.move_list(page + 1)
            # b: 前のページへ
            elif result == "b":
                self.move_list(page - 1)
            # *n: 詳細へ
            elif result[0] == '*':
                self.move_info(page,int(result[1]))
        # 数値
        else:
            # 0:行動選択へ
            if result == 0:
                self.select_action()
                
    #--攻撃技詳細--#
    def move_info(self,page,num):
        #UI表示
        enter(self.ui.move_info,args=[page,num])
        #技一覧にもどる
        self.move_list(page)
        
    #--ステータス確認--#
    def check_stats(self):
        #UI表示
        enter(self.ui.check_stats)
        #行動選択に戻る
        self.select_action()
        
        
        
        
        
