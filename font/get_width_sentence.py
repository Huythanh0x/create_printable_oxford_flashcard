from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable
from pandas import describe_option

MAX_WIDTH = 310
TEXT_SIZE = 14
##init font
font = TTFont('font/Voces-Regular.ttf')
cmap = font['cmap']
t = cmap.getcmap(3,1).cmap
s = font.getGlyphSet()
units_per_em = font['head'].unitsPerEm

def getTextWidth(text,pointSize):
    total = 0
    for c in text:
        if ord(c) in t and t[ord(c)] in s:
            total += s[t[ord(c)]].width
        else:
            total += s['.notdef'].width
    total = total*float(pointSize)/units_per_em;
    return total

def get_split_description(text):
    list_splitted_text = text.split(' ')
    start_index_line = 0
    description = []
    for i,word in enumerate(list_splitted_text):
        if getTextWidth(" ".join(list_splitted_text[start_index_line:i]),TEXT_SIZE) <= MAX_WIDTH:
            pass
        else:
            description +=  [" ".join(list_splitted_text[start_index_line:i-1])]
            start_index_line = i-1
    description += [" ".join(list_splitted_text[start_index_line:i+1])]

    return description

split_description = get_split_description('a long piece of cloth with a message on it that is carried between two poles or hung in a public place to show support foor something')
print(split_description)