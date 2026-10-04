import unicodedata

#--文字数取得(全角は2文字扱い)--#
def text_width(text):
    count = 0
    for c in text:
        count += 2 if unicodedata.east_asian_width(c) in 'FWA' else 1
    return count
