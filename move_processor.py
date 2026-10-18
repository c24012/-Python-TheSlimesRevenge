from common import enter,prob

class MoveProcessor:
    def __init__(self,player,enemy,ui):
        self.player = player
        self.enemy = enemy
        self.move = None
        self.user = None
        self.target = None
        self.ui = ui
        
    #技を使用
    def use_a_move(self,move,is_player):
        
        self.player.calculate_stats()
        self.enemy.calculate_stats()
        
        self.move = move
        self.user = self.player if is_player else self.enemy
        self.target = self.enemy if is_player else self.player
        self.facter_text = f"{self.user.name}の{self.move.name}！"

        is_hit = False
        if move.category == "物理":
            is_hit = self.physical_move()
        elif move.category == "魔法":
            is_hit = self.magical_move()
        else:
            is_hit = self.special_move()
            
        if is_hit:
            if move.effects is not None:
                for effect in move.effects:
                    self.give_effects(effect["effect"],effect["acc"],effect["target"])
                    
            if move.recovery is not None:
                self.recovey_hp()
        
    #物理技
    def physical_move(self):
        damage = self.calculate_damage(self.user.final_stats.at,self.target.final_stats.df)
        
        #技を外す 確率計算
        if prob(100 - self.move.acc):
            enter(self.ui.missed,args=[self.target,self.facter_text])
            return False
        
        #俊敏差による回避 確率計算
        if prob(min((self.target.stats.sp - self.user.stats.sp)/10 +self.target.stats.sp/self.user.stats.sp,90))	:
            enter(self.ui.dodged,args=[self.target,self.facter_text])
            return False
        
        #技が命中
        if damage <= 0:
            enter(self.ui.damage_zero,args=[self.target,self.facter_text])
        else:
            enter(self.ui.damage,args=[damage,self.target,self.facter_text])
            self.target.damage(damage)
            
        return True
    
    #魔法技
    def magical_move(self):
        damage = self.calculate_damage(self.user.final_stats.mg,self.target.final_stats.md)
        #技が命中
        if not any(avoids):
            if damage <= 0:
                enter(self.ui.damage_zero,args=[self.target,self.facter_text])
            else:
                enter(self.ui.damage,args=[damage,self.target,self.facter_text])
                self.target.damage(damage)
                
        return True
    
    #特殊技
    def special_move(self):
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
    def give_effects(self,effect,acc,target):
        targets = []
        if target == 's':
            targets = [self.user]
        elif target == 'o':
            targets = [self.target]
        else:
            targets = [self.user,self.target]
        
        for _target in targets:
            #失敗 確率計算
            if prob(100 - acc):
                return
            #付与成功
            enter(self.ui.add_status_effect,args=[effect,_target])
            _target.status_effects.add_effect(effect)
    
    #HP回復
    def recovey_hp(self):
        targets = []
        if self.move.target == 's':
            targets = [self.user]
        elif self.move.target == 'o':
            targets = [self.target]
        else:
            targets = [self.user,self.target]
            
        for _target in targets:
            #HP回復
            if self.move.recovery is not None:
                enter(self.ui.recovery_hp,args=[self.move.recovery,_target,self.facter_text])
                _target.recover_hp(self.move.recovery)
    
    
    
    