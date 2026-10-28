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
            pass
        # <5:能力確認> 能力確認へ
        elif result == 5:
            pass
        # <6:お宝確認> お宝確認へ
        elif result == 6:
            pass
        
    #モンスターとの戦闘
    def battle(self):
        is_win = Battle(self.player,CharaDS.inst["ゴブリン"]()).get_result()
        if is_win:
            self.next_floor()
        else:
            self.exit_castle(is_defeated_king=False)
        
        
        
        
        
        
        