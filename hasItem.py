from databases.chara_database import CharaDataBase	as Chara

class Test:
    def __init__(self):
        self.chara_list = [Chara.chara["スライム"]()]
    
    def hasChara(self,chara):
        return any(isinstance(c,chara) for c in self.chara_list)

test = Test()
print(test.hasChara(Chara.chara["ゴブリン"]))
 


