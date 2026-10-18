class BaseMove:
    def __init__(self,name,category,power=None,acc=None,effects=None,target=None,tp=None,recovery=None):
        
        if category not in ["物理","魔法","特殊"]:
            raise Exception("想定外の攻撃タイプです")
        
        self.name = name			#技名
        self.category = category	#技タイプ(物理、魔法、特殊)
        self.power = power			#威力
        self.acc = acc				#命中
        self.effects = effects		#状態付与 ([])
        self.target = target		#対象(自分:'s',相手:'o',両方:'b')
        self.tp = tp				#消費TP(-1:スライムが真似できない技)
        self.recovery = recovery	#回復値
        self.info = ""				#効果説明文
        
    #--効果説明文--#
    def set_info(self,info_text):
        self.info = info_text
        
    #--戦闘中の技使用イベント--#
    def use_event(self):
        pass

        
"""
記述例

#--攻撃--#
class Attack(BaseMove):
    def __init__(self):
        super().__init__(
            name = "攻撃",			技名
            power = 100,			威力
            acc = 100,				命中
            effects = None			状態付与 ([])
            target = 'u'			対象 (自分:'s',相手:'o',両方:'b')
            self.tp = tp			消費TP
            recovery = 100			回復値
            )

"""
        