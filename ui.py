from common import text_width

class Panel:
    def __init__(self):
        self.scene_panel = ""
        self.info_panel = ""
        self.frame_text = ""
        self.frame_top = ""
        self.frame_under = ""
        self.enter_text = ("入力:","再度入力:")
    
    def set_panel(self,scene,info,frame):
        self.scene_panel = scene
        self.info_panel = info
        self.frame_text = frame
    
    def view(self,redo):
        self.build_frame_top()
        self.build_frame_under()
        
        print("\n\n\n\n\n\n\n\n")
        
        print(self.scene_panel,end="")
        print(self.frame_top,end="")
        print(self.info_panel,end="")
        print(self.frame_under,end="")
        print(self.enter_text[1 if redo else 0],end="")
        
        self.__init__()
    
    
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
        pass
    
    def text(self,text,head=0):
        return " "*head + text
    
    def horiz(self,texts,width=48,head=0):
        unit_width = width // len(texts)
        text = (" " * head)
        for i in range(len(texts)):
            text += f"{texts[i]}"+(" " * (unit_width - text_width(texts[i])))
        return text
    
    def horiz_right(self,texts,width=48,head=0):
        unit_width = width // len(texts)
        text = ""
        for i in range(len(texts)):
            text += " " * (head - text_width(texts[i]))
            text += f"{texts[i]}"+(" " * (unit_width - (head)))
        return text
    
    def horiz_alignment(self,text1,text2,text3,width=48,head=1,end=1):
        center_start = (width // 2) - (text_width(text2) // 2) - (0 if isinstance(text_width(text2) / 2,int) else 1)
        space1 = max(center_start - text_width(text1),0)
        space2 = width - center_start - text_width(text2) - text_width(text3) - head - end
        text = " "*head + text1 + " "*space1 + text2 + " "*space2 + text3
        return text
    
    def horiz_free(self,texts):
        spaces = [x[1] for x in texts]
        text = ""
        for i in range(len(texts)):
            text += " "*(spaces[i] - text_width(text)) + texts[i][0]
        return text
    
    def center(self,texts,width=48):
        head = (width // 2) - (text_width(texts) // 2)
        fin = width - head - text_width(texts)
        text = " "*head + texts + " "*fin
        return text
    
    def tab(self,text1,text2,width,head=0):
        text = (" " * head)
        if text_width(text1) >= width:
            return text+text1+text2
        else:
            space = width - text_width(text1)
            text += text1 + (" "*space) + text2
            return text
    
    def gage(self,value,max_value,size=18):
        percent = value/max_value
        if percent == 0:
            count = 0
        else:
            count = int(max(percent * size,1))
        text = "[" + ("-" * (size - count)) + ("/" * count) + "]"
        return text
    
    def place_strings_at_lines(self,texts,line_count):
        text = ""
        line_numbers = [x[0] for x in texts]
        for i in range(line_count):
            if i in line_numbers:
                text += " "+texts[line_numbers.index(i)][1]
            text += "\n"
        return text
    
    
""" #↓Panel作成例

#パネルクラスと内部テキストクラスを生成
panel = Panel()
text = Text()

#シーンパネルの内部テキスト作成

 #各行のテキスト作成
texts = []
texts.append([1,text.horiz(["スライム","ゴブリン"])])
texts.append([2,text.horiz([f"HP{text.gage(100,100)}",f"HP{text.gage(95,100)}"])])
texts.append([3,text.horiz_right(["10/100","1/100"],head=22)])
texts.append([4,text.horiz([f"TP{text.gage(15,20)}",""])])
texts.append([5,text.horiz_right(["15/20",""],head=22)])

 #改行を挿入
text_scene = text.place_strings_at_lines(texts,line_count = 7)
    
#詳細パネルの内部テキスト作成

 #各行のテキスト作成
texts = []
texts.append([1," スライムの行動"
texts.append([3,text.horiz(["1: 戦う","2: 状態変化"],head=2)])
texts.append([5,text.horiz(["3: 能力確認","4: お宝確認"],head=2)])

 #改行を挿入
text_info = text.place_strings_at_lines(texts,line_count = 8)

#パネルにシーンテキスト、詳細テキスト、フレームテキストを設定
panel.set_panel(scene=text_scene,info=text_info,frame="戦闘")
#パネルを画面に表示
panel.view()

#入力部分
input()

"""
