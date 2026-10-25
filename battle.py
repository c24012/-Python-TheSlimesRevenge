from common import enter
from battle_ui import BattleUI
from move_processor import MoveProcessor

class Battle:
    def __init__(self,player,enemy):
        self.ui = BattleUI(player,enemy)
        self.mp = MoveProcessor(player,enemy,self.ui)
        self.player = player
        self.enemy = enemy
        self.start()
    
    def start(self):
        #遭遇
        self.encount()
        
        result = ""
        while result == "":
            
            #状態チェック
            self.status_effects_check(start=True)
            
            #プレイヤーの行動
            self.player_turn()
            
            #死亡確認
            result = self.is_dead_check()
            if result != "":
                return result
            
            #敵の行動
            self.enemy_turn()
            
            #死亡確認
            result = self.is_dead_check()
            if result != "":
                return result
            
            #状態チェック
            self.status_effects_check(start=False)
            
            #プレイヤーのTPを回復する
            self.player.recover_tp(1)
        
    #--遭遇--#
    def encount(self):
        #UI表示
        enter(self.ui.encount)
        
    #--プレイヤーの行動--#
    def player_turn(self):
        #プレイヤーターン開始ui
        enter(self.ui.turn_start,args=[True])
        #行動開始イベント発火
        for effect in self.player.status_effects.effects:
            effect.on_action_start()
        #状態変化による能力変化の更新
        self.player.calculate_modifier()
        #行動
        turn = 1
        while turn > 0:
            self.select_action()
            turn -= 1
        #行動終了イベント発火
        for effect in self.player.status_effects.effects:
            effect.on_action_end()
        #状態変化の残りターン消費
        remove_se = self.player.status_effects.turn_check()
        if len(remove_se) > 0:
            messages = []
            for i in range(0,len(remove_se),3):
                for effect in remove_se[i:i+3]:
                    messages.append(f"{self.player.name}の{effect.name}の効果が消えた")
                enter(self.ui.free,args=[messages])
        #状態変化による能力変化の更新
        self.player.calculate_modifier()
        
    #--敵の行動--#
    def enemy_turn(self):
        #敵ターン開始ui
        enter(self.ui.turn_start,args=[False])
        #行動開始イベント発火
        for effect in self.enemy.status_effects.effects:
            effect.on_action_start()
        #状態変化による能力変化の更新
        self.enemy.calculate_modifier()
        #行動
        turn = 1
        while turn > 0:
            move = self.enemy.action(self.player)
            self.mp.use_a_move(move,is_player=False)
            turn -= 1
        #行動終了イベント発火
        for effect in self.enemy.status_effects.effects:
            effect.on_action_end()
        #状態変化の残りターン消費
        remove_se = self.enemy.status_effects.turn_check()
        if len(remove_se) > 0:
            messages = []
            for i in range(0,len(remove_se),3):
                for effect in remove_se[i:i+3]:
                    messages.append(f"{self.enemy.name}の{effect.name}の効果が消えた")
                enter(self.ui.free,args=[messages])
        #状態変化による能力変化の更新
        self.enemy.calculate_modifier()
    
    #--状態チェック--#
    def status_effects_check(self,start):
        if start:
            #ターン開始イベント発火
            for effect in self.player.status_effects.effects:
                effect.on_turn_start()
            for effect in self.enemy.status_effects.effects:
                effect.on_turn_start()
        else:
            #ターン終了イベント発火
            for effect in self.player.status_effects.effects:
                effect.on_turn_end()
            for effect in self.enemy.status_effects.effects:
                effect.on_turn_end()
        #状態変化による能力変化の更新
        self.player.calculate_modifier()
        self.enemy.calculate_modifier()
    
    #--死亡チェック--#
    def is_dead_check(self):
        if self.player.is_dead:
            print(f"{self.player.name}は死んでしまった")
            return "lose"
        elif self.enemy.is_dead:
            print(f"{self.enemy.name}を倒した！")
            return "win"
        else:
            return ""
        
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
            self.select_check_status_effect()
        # <3:能力確認> ステータス確認へ
        elif result == 3:
            self.check_stats()
        # <4:お宝確認> お宝確認へ
        elif result == 4:
            pass
            
    #--攻撃技選択--# 
    def move_list(self,page):
        
        #このページの技の数
        move_count = len(self.player.moves.moves) - (page * 9)
        #次のページがあるか確認
        not_last = ((page + 1) != (len(self.player.moves.moves) // 9 + 1))
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
            # 1∼9:各技を繰り出す
            if 1 <= result <= 9 and isinstance(result,int):
                move = self.player.moves.moves[page*9 + result - 1]
                #TPが足りていたら発動
                if move.tp <= self.player.stats.tp:
                    self.player.use_tp(move.tp)
                    self.mp.use_a_move(move,is_player=True)
                else:
                    enter(self.ui.free,args=[["TPがなりない！"]])
                    self.move_list(page)
            # 0:行動選択へ
            elif result == 0:
                self.select_action()
                
    #--攻撃技詳細--#
    def move_info(self,page,num):
        #技データを取得
        move = self.player.moves[page*9 + num - 1]
        #付与する状態の数を取得
        effect_cocunt = 0 if move.effects is None else len(move.effects)
        
        #UI表示
        result = enter(self.ui.move_info, max_num=effect_cocunt, args=[page,num] ,is_next=True)
        # 数値
        if isinstance(result,int):
            # 1∼2:付与する状態の詳細確認へ
            if 1 <= result <= 2:
                effect = move.effects[result-1]
                self.status_effect_info_from_move(effect,page,num)
        else:
            #技一覧にもどる
            self.move_list(page)
                
    #--技の付与状態詳細--#
    def status_effect_info_from_move(self,effect,page,num):
        #UI表示
        enter(self.ui.status_effect_info_from_move,args=[effect])
        #技詳細にもどる
        self.move_info(page,num)
        
    #--誰の状態変化を確認するか選択--#
    def select_check_status_effect(self):
        #UI表示
        result = enter(self.ui.select_check_status_effect,max_num=2,is_back=True)
        
        # <1:自分の状態変化を確認> 状態変化の確認へ(プレイヤー)
        if result == 1:
            self.check_status_effect(page=0,is_player=True)
        # <1:相手の状態変化を確認> 状態変化の確認へ(敵)
        elif result == 2:
            self.check_status_effect(page=0,is_player=False)
        elif result == 0:
            #行動選択に戻る
            self.select_action()
        
    #--状態変化の確認--#
    def check_status_effect(self,page,is_player):
        if is_player:
            #{page}ページの状態変化の数
            effect_count = len(self.player.status_effects.effects) - (page * 5)
            #次のページがあるか確認
            last_page = ((page + 1) == (len(self.player.status_effects.effects) // 5 + 1))
        else:
            #{page}ページの状態変化の数
            effect_count = len(self.enemy.status_effects.effects) - (page * 5)
            #次のページがあるか確認
            last_page = ((page + 1) == (len(self.enemy.status_effects.effects) // 5 + 1))
            
        #前のページがあるか確認
        first_page = (page == 0)

        #UI表示
        result = enter(self.ui.check_status_effect,max_num=effect_count,args=[page,is_player],
                       is_back=True,is_next=not last_page,is_before=not first_page)
        
        if isinstance(result,str):
            # "":次のページへ
            if result == "":
                self.check_status_effect(page + 1)
            # b: 前のページへ
            elif result == "b":
                self.check_status_effect(page - 1)
        # 数値
        else:
            # 0 or None:行動選択へ
            if result == 0 or result is None:
                self.select_action()
            # 1-9:詳細
            elif 1 <= result and result <= 9:
                self.status_effect_info(page,is_player,result)
            
    
    #--状態詳細--#
    def status_effect_info(self,page,is_player,num):
        #UI表示
        enter(self.ui.status_effect_info,args=[page,is_player,num])
        #技一覧にもどる
        self.check_status_effect(page,is_player)
    
    #--ステータス確認--#
    def check_stats(self):
        #UI表示
        enter(self.ui.check_stats)
        #行動選択に戻る
        self.select_action()
        
        
        
        
        
