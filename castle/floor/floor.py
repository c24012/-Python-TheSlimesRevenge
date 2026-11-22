from common import enter
from datastores.chara_datastore import CharaDataStore as CharaDS
from castle.battle.battle import Battle
from .floor_ui import FloorUI

class Floor:
    def __init__(self,player):
        self.player = player
        self.floor = [1]
        self.ui = FloorUI(player,self.floor)
        self.is_defeated_king = None
        self.start()
        
    def start(self):
       enter(self.ui.enter_floor)
       self.select_action()
       
    #次のフロアへ
    def next_floor(self):
        self.floor[0] += 1
        self.start()
        
    #魔王城から脱出
    def exit_castle(self,is_defeated_king):
        self.is_defeated_king = is_defeated_king
       
    #-- ↓ プレイヤーのコマンド選択 ↓ --#
        
    #--行動選択--#
    def select_action(self):
        #UI表示
        result = enter(self.ui.select_action,max_num=6,is_back=True)
        
        # <0:リタイア> リタイア確認へ
        if result == 0 or result is None:
            pass
        # <1:戦闘> モンスターと戦闘開始
        elif result == 1:
            self.battle()
        # <2:お宝採集> お宝採集へ
        elif result == 2:
            pass
        # <3:探索> 探索へ
        elif result == 3:
            pass
        # <4:技確認> 技確認へ
        elif result == 4:
            self.move_list(0)
        # <5:能力確認> 能力確認へ
        elif result == 5:
            self.check_stats()
        # <6:お宝確認> お宝確認へ
        elif result == 6:
            self.treasure_list(0)
        
    #--モンスターとの戦闘--#
    def battle(self):
        is_win = Battle(self.player,CharaDS.inst["ゴブリン"]()).get_result()
        if is_win:
            self.bleak_room()
        else:
            self.exit_castle(is_defeated_king=False)
            
    #休憩部屋
    def bleak_room(self):
        #休憩してHP(1/3)とTP(全回復)を回復
        hp_amount = self.player.stats.max_hp // 3
        st_amount = self.player.stats.max_st
        self.player.recover_hp(hp_amount)
        self.player.recover_st(st_amount)
        #UI表示
        enter(self.ui.bleak_room,args=[hp_amount,st_amount])
        #次のフロアへ
        self.next_floor()
    
    #-- ↓ 情報確認用コマンド ↓ --#
    
    #--技の確認--# 
    def move_list(self,page):
        
        #このページの技の数
        move_count = len(self.player.moves.moves) - (page * 9)
        #次のページがあるか確認
        not_last = ((page + 1) != (len(self.player.moves.moves) // 9 + 1))
        #前のページがあるか確認
        not_first = (page != 0)
        
        #UI表示
        result = enter(self.ui.move_list,max_num=move_count,args=[page],
                       is_back=True,is_next=not_last,is_before=not_first)
        
        if isinstance(result,str):
            # "":次のページへ
            if result == "":
                self.move_list(page + 1)
            # b: 前のページへ
            elif result == "b":
                self.move_list(page - 1)
        # 数値
        else:
            # 1∼9:技の詳細へ
            if 1 <= result <= 9 and isinstance(result,int):
                self.move_info(page=page,num=result)
            # 0:行動選択へ
            elif result == 0:
                self.select_action()
                
    #--攻撃技詳細--#
    def move_info(self,page=0,num=0,move=None,is_learn_move=False):
        #技データを取得
        if is_learn_move:
            _move = move
        else:
            _move = self.player.moves.moves[page*9 + num - 1]
        #付与する状態の数を取得
        effect_cocunt = 0 if _move.effects is None else len(_move.effects)
        
        #UI表示
        result = enter(self.ui.move_info, max_num=effect_cocunt, args=[_move] ,is_next=True)
        # 数値
        if isinstance(result,int):
            # 1∼2:付与する状態の詳細確認へ
            if 1 <= result <= 2:
                effect = _move.effects[result-1]
                self.status_effect_info_from_move(effect,page,num,move,is_learn_move)
        else:
            #技習得時なら習得画面にもどる
            if is_learn_move:
                self.learn_move()
            else:
                #技一覧にもどる
                self.move_list(page)
                
    #--技の付与状態詳細--#
    def status_effect_info_from_move(self,effect,page,num,move=None,is_learn_move=False):
        #UI表示
        enter(self.ui.status_effect_info_from_move,args=[effect])
        #技詳細にもどる
        self.move_info(page=page,num=num,move=move,is_learn_move=is_learn_move)
    
    #--ステータス確認--#
    def check_stats(self):
        #UI表示
        enter(self.ui.check_stats)
        #行動選択に戻る
        self.select_action()
        
    #--お宝確認--# 
    def treasure_list(self,page):
        
        #このページの技の数
        move_count = len(self.player.treasures.treasures) - (page * 9)
        #次のページがあるか確認
        not_last = ((page + 1) != (len(self.player.treasures.treasures) // 9 + 1))
        #前のページがあるか確認
        not_first = (page != 0)
        
        #UI表示
        result = enter(self.ui.treasures_list,max_num=move_count,args=[page],
                       is_info=True,is_back=True,is_next=not_last,is_before=not_first)
        
        if isinstance(result,str):
            # "":次のページへ
            if result == "":
                self.treasure_list(page + 1)
            # b: 前のページへ
            elif result == "b":
                self.treasure_list(page - 1)
        # 数値
        else:
            # 1∼9:各技を繰り出す
            if 1 <= result <= 9 and isinstance(result,int):
                self.treasure_info(page,result)
            # 0:行動選択へ
            elif result == 0:
                self.select_action()
                
    #--お宝詳細--#
    def treasure_info(self,page,num):
        #技データを取得
        treasure = self.player.treasures.treasures[page*9 + num - 1]
        #付与する状態の数を取得
        effect_cocunt = 0 if treasure.effects is None else len(treasure.effects)
        
        #UI表示
        result = enter(self.ui.treasure_info, max_num=effect_cocunt, args=[treasure] ,is_next=True)
        # 数値
        if isinstance(result,int):
            # 1∼2:付与する状態の詳細確認へ
            if 1 <= result <= 2:
                effect = treasure.effects[result-1]
                self.status_effect_info_from_treasure(effect,page,num)
        else:
            #お宝確認にもどる
            self.treasure_list(page)
                    
    #--お宝の付与状態詳細--#
    def status_effect_info_from_treasure(self,effect,page,num):
        #UI表示
        enter(self.ui.status_effect_info_from_treasure,args=[effect])
        #お宝詳細にもどる
        self.treasure_info(page,num)
    

        
        
        
        
        
        
        