from common import text_width

class Panel:
    def __init__(self):
        self.scene_panel = ""
        self.info_panel = ""
        self.frame_text = ""
        self.frame_top = ""
        self.frame_under = ""
        self.enter_text = "入力:"
    
    def set_panel_text(self,scene,info,frame):
        self.scene_panel = scene
        self.info_panel = info
        self.frame_text = frame
    
    def view(self):
        self.build_frame_top()
        self.build_frame_under()
        
        print(self.scene_panel,end="")
        print(self.frame_top,end="")
        print(self.info_panel,end="")
        print(self.frame_under,end="")
        print(self.enter_text,end="")
    
    
    def build_frame_top(self,width=48,space=1):
        if width % 2 == 1:
            width += 1
        if self.frame_text == "":
            self.frame_top = " " + "-"*width + " \n"
            return
        line_count = (width - text_width(self.frame_text) - space) // 2
        self.frame_top = " " + "-"*line_count + " " + self.frame_text + " " + "-"*line_count + " \n"
    
    def build_frame_under(self,width=48):
        if width % 2 == 1:
            width += 1
        self.frame_under += " " + "-"*width + " \n"

class Text:
    def __init__(self):
        self.text = ""
        pass
    
    def horiz(self,texts,width=48,head=0):
        unit_width = width // len(texts)
        self.text = (" " * head)
        for i in range(len(texts)):
            self.text += f"{texts[i]}"+(" " * (unit_width - text_width(texts[i])))
        return self.text
    
    def horiz_right(self,texts,width=48,head=0):#head22
        unit_width = width // len(texts)
        self.text = ""
        for i in range(len(texts)):
            self.text += " " * (head - text_width(texts[i]))
            self.text += f"{texts[i]}"+(" " * (unit_width - (head)))
        return self.text
    
    def gage(self,value,max_value,size=18):
        percent = value/max_value
        if percent == 0:
            count = 0
        else:
            count = int(max(percent * size,1))
        gage = "[" + ("-" * (size - count)) + ("/" * count) + "]"
        return gage
    
    def place_strings_at_lines(self,texts,line_numbers,line_count):
        self.text = ""
        for i in range(line_count):
            if i in line_numbers:
                self.text += " "+texts[line_numbers.index(i)]
            self.text += "\n"
        return self.text
    
    
""" #↓Panel作成例

#パネルクラスと内部テキストクラスを生成
panel = Panel()
text = Text()

#シーンパネルの内部テキスト作成

 #各行のテキスト作成
text_name = text.horiz(["スライム","ゴブリン"])
text_hp_gage = text.horiz([f"HP{text.gage(100,100)}",f"HP{text.gage(95,100)}"])
text_hp = text.horiz_right(["10/100","1/100"],head=22)
text_tp_gage = text.horiz([f"TP{text.gage(15,20)}",""])
text_tp = text.horiz_right(["15/20",""],head=22)

 #各行を1つのStringにまとめる
text_scene = text.place_strings_at_lines([
    text_name,
    text_hp_gage,
    text_hp,
    text_tp_gage,
    text_tp
    ],
    [1,2,3,4,5],
    line_count = 7
    )
    
#詳細パネルの内部テキスト作成

 #各行のテキスト作成
text_instr = " スライムの行動"
text_actions = [
    text.horiz(["1: 戦う","2: 状態変化"],head=2),
    text.horiz(["3: 能力確認","4: お宝確認"],head=2)]

 #各行を1つのStringにまとめる
text_info = text.place_strings_at_lines([
    text_instr,
    text_actions[0],
    text_actions[1],
    ],
    [1,3,5],
    line_count = 8
    )

#パネルにシーンテキスト、詳細テキスト、フレームテキストを設定
panel.set_panel_text(scene=text_scene,info=text_info,frame="戦闘")
#パネルを画面に表示
panel.view()

#入力部分
input()

"""
