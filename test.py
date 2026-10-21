from datastores.chara_datastore import CharaDataStore
from battle import Battle

chara = CharaDataStore()

Battle(chara.inst["スライム"](name="プレイヤー"),chara.inst["ゴブリン"]())
