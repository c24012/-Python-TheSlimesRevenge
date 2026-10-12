from datastores.chara_datastore import CharaDataStore
from battle import Battle

chara = CharaDataStore()

Battle(chara.inst["スライム"](),chara.inst["ゴブリン"]())
