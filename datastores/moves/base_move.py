from datastores.status_effect_datastore import StatusEffectDataStore as SEStore

class BaseMove:
    def __init__(self,name,category,power=None,acc=None,effects=None,target='o',st=0,rec_hp=None,rec_st=None,enemy_only=False):
        
        if category not in ["physical","magical","special"]:
            raise Exception("想定外の攻撃タイプです")
        
        self.name = name			#技名
        self.category = category	#技タイプ(物理、魔法、特殊)
        self.power = power			#威力
        self.acc = acc				#命中
        self.effects = effects		#状態付与 ([SEFM()])
        self.target = target		#対象(自分:'s',相手:'o',両方:'b')
        self.st = st				#消費ST
        self.rec_hp = rec_hp		#HP回復値
        self.rec_st = rec_st		#ST回復値
        self.info = []				#効果説明文
        self.enemy_only = enemy_only#True:プレイヤーが覚えられない
        
    #--効果説明文--#
    def set_info(self,*texts):
        self.info = texts
        
    #--戦闘中の技使用イベント--#
    def use_event(self):
        pass

#技が持つ状態付与のデータ
class StatusEffectForMove:
    def __init__(self,name,target,acc=100,turn=None,level=None):
        self.effect = SEStore().get_effect(name)
        self.target = target
        self.acc = acc
        self.turn = turn
        self.level= level
        
    def instance_effect(self):
        return self.effect(turn=self.turn,level=self.level)
        
"""
記述例

#--攻撃--#
class Attack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "攻撃",			技名
            power = 100,			威力
            acc = 100,				命中
            effects = None			状態付与 ([{要素:値}])
            target = 'o'			対象 (自分:'s',相手:'o',両方:'b')
            st = st					消費ST
            recovery = [100,'s']	回復値([回復値,対象(自分:'s',相手:'o',両方:'b')])
            )
        self.set_info(
            '通常攻撃'
            )

"""
        