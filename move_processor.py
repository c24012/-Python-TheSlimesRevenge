from common import enter,prob

class MoveProcessor:
    def __init__(self,player,enemy,ui):
        self.player = player
        self.enemy = enemy
        self.move = None
        self.user = None
        self.target = None
        self.ui = ui
        self.message = []
        
    #技を使用
    def use_a_move(self,move,is_player):
        
        self.message.clear()
        
        self.player.calculate_stats()
        self.enemy.calculate_stats()
        
        self.move = move
        self.user = self.player if is_player else self.enemy
        
        self.target = self.enemy if is_player else self.player
        self.message.append(f"{self.user.name}の{self.move.name}！")
        
        targets = []
        if move.target == 's':
            targets = [self.user]
        elif move.target == 'o':
            targets = [self.target]
        else:
            targets = [self.user,self.target]

        for _target in targets:
            self.target = _target
            is_hit = False
            if move.category == "物理":
                is_hit = self.physical_move()
            elif move.category == "魔法":
                is_hit = self.magical_move()
            else:
                is_hit = self.special_move()
                
            if is_hit:
                if move.effects is not None:
                    for _effect in move.effects:
                        self.give_effects(_effect)
                        
                if move.recovery is not None:
                    self.recovey_hp(move.recovery[0],move.recovery[1])
                
        #uiを表示
        enter(self.ui.free,args=[self.message])
        
    #物理技
    def physical_move(self):
        damage = self.calculate_damage(self.user.final_stats.at,self.target.final_stats.df)
        
        #技を外す 確率計算
        if prob(100 - self.move.acc):
            self.message.append(f"{self.target.name}に当たらなかった！")
            return False
        
        #俊敏差による回避 確率計算
        if prob(min((self.target.stats.sp - self.user.stats.sp)/10 +self.target.stats.sp/self.user.stats.sp,90))	:
            self.message.append(f"{self.target.name}は回避した！")
            return False
        
        #技が命中
        if damage <= 0:
            damage_text = f"{self.target.name}はダメージを受けていない！"
        else:
            damage_text = f"{self.target.name}は{damage}のダメージ！"
            self.target.damage(damage)
        self.message.append(damage_text)
            
        return True
    
    #魔法技
    def magical_move(self):
        damage = self.calculate_damage(self.user.final_stats.mg,self.target.final_stats.md)
        #技が命中
        if not any(avoids):
            if damage <= 0:
                damage_text = "{self.target.name}はダメージを受けていない！"
            else:
                damage_text = f"{self.target.name}は{damage}のダメージ！"
                self.target.damage(damage)
        self.message.append(damage_text)
                
        return True
    
    #特殊技
    def special_move(self):
        #self.message.append()
        return True
    
    #ダメージ計算
    def calculate_damage(self,at,df):
        baseDamage = at * (self.move.power / 100)				#火力指数
        diff = baseDamage * (at - df) / 3000 					#ステータス差
        low = 300 / max((at + df) - abs(at - df),1) 			#低ステータス補正
        high = pow(max((at + df) - abs(at - df),1) / 15,1.6) 	#高ステータス補正
        raito = (at + low) / (at + df + high) 					#防御に対しての攻撃の比率
        damage = baseDamage * raito + diff 						#火力指数*比率+差
        return int(damage)
        
    #状態変化を付与
    def give_effects(self,effect_data):
        targets = []
        if effect_data.target == 's':
            targets = [self.user]
        elif effect_data.target == 'o':
            targets = [self.target]
        else:
            targets = [self.user,self.target]
        
        for _target in targets:
            #失敗 確率計算
            if prob(100 - effect_data.acc):
                continue
            
            _effect = effect_data.instance_effect()
             
            #すでに付与されている場合
            if _target.status_effects.has_effect(effect_data.effect):
                #レベルの要素を持つ場合
                if _effect.level is not None:
                    #レベルが最大ではない時は強化
                    if _target.status_effects.get_effect(effect_data.effect).level < 3:
                        self.message.append(f"{_target.name}の{_effect.name}状態が強化された！")
                        _target.status_effects.level_up(effect_data.effect,_effect.level)
                    #レベル最大時は何も起こらない
                    else:
                        self.message.append(f"{_effect.name}状態はこれ以上強化できない！")
                #残りターンのみの要素を持つ場合
                elif _effect.turn is not None:
                    self.message.append(f"{_target.name}はすでに{_effect.name}状態になっている！")
                #状態定義ミス
                else:
                    raise ValueError(f"ターン,レベル共にNoneになっています\n状態名:{_effect.name}")
            #まだ付与されていない場合
            else:
                self.message.append(f"{_target.name}は{_effect.name}状態になった！")
                _target.status_effects.add_effect(_effect)
    
    #HP回復
    def recovey_hp(self,value,target):
        targets = []
        if target == 's':
            targets = [self.user]
        elif target == 'o':
            targets = [self.target]
        else:
            targets = [self.user,self.target]
            
        for _target in targets:
            #HP回復
            self.message.append(f"{_target.name}のHPは{value}回復した！")
            _target.recover_hp(value)
    
    
    
    