from .treasures.floor_1 import RustedKnife,BrokenWand,DirtyCloth,LightStone,BraceletOfChains

class TreasuresDataStore:
    def __init__(self):
        self.treasures_data = {
            #1階
            "rusted_knife":RustedKnife,                 #錆びたナイフ
            "broken_wand":BrokenWand,                   #折れかけの杖
            "dirty_cloth":DirtyCloth,                   #汚れた布
            "light_stone":LightStone,                   #軽い石
            "bracelet_of_chains":BraceletOfChains,      #連鎖の輪

            #2階

        }

    #-指定お宝を生成-#
    def inst(self,treasure_name,*args):
        if treasure_name in self.treasures_data:
            if args:
                return self.treasures_data[treasure_name](*args)
            return self.treasures_data[treasure_name]()
        else:
            raise ValueError(f"Treasure '{treasure_name}' not found in TreasuresDataStore.")
    

