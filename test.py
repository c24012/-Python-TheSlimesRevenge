from datastores.chara_datastore import CharaDataStore
from castle.battle.battle import Battle
from castle.floor.floor import Floor

chara = CharaDataStore()

#Battle(chara.inst["スライム"](),chara.inst["ゴブリン"]())
Floor(chara.inst["スライム"]())