import unicodedata
import random

#--文字数取得(全角は2文字扱い)--#
def text_width(text):
    count = 0
    for c in text:
        count += 2 if unicodedata.east_asian_width(c) in 'FWA' else 1
    return count

#--入力処理--#
def enter(ui_method,max_num=0,args=None,is_info=False,is_back=False,is_next=False,is_before=False,is_closed=False):
    is_redo = False
    while(True):
        if args is None:
            ui_method(is_redo)
        else:
            ui_method(*args,is_redo)
        if max_num == 0:
            input()
            return
        else:
            try:
                value = input()
                #*n:詳細
                if is_info and value != "" and value[0] == "*" and len(value) > 1:
                    if 1 <= int(value[1]) <= max_num:
                        return value
                #0:もどる
                elif is_back and value == "0":
                    return 0
                #b:前のページ
                elif is_before and value == "b":
                    return value
                #"":次のページ
                elif is_next and value == "":
                    return value
                #y/n:2択質問
                elif is_closed and (value == "y" or value == "n"):
                    return value
                #指定内の数値
                elif 1 <= int(value) <= max_num:
                    return int(value)
                else:
                    is_redo = True
            except ValueError:
                is_redo = True
                
#--確率--#
def prob(persent):
    num = random.randint(1, 100)
    return num <= int(persent)
    