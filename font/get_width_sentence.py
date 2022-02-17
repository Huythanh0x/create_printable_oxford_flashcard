from fontTools.ttLib import TTFont
from pandas import describe_option

MAX_WIDTH = 280
TEXT_SIZE = 15
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
        if getTextWidth(" ".join(list_splitted_text[start_index_line:i]),TEXT_SIZE) > MAX_WIDTH:
            description +=  [" ".join(list_splitted_text[start_index_line:i-1])]
            start_index_line = i-1
        if i+1==len(list_splitted_text) and getTextWidth(" ".join(list_splitted_text[start_index_line:i+1]),TEXT_SIZE) > MAX_WIDTH:
            description +=  [" ".join(list_splitted_text[start_index_line:i-1])]
            start_index_line = i-1

    description += [" ".join(list_splitted_text[start_index_line:i+1])]

    return description

split_description = get_split_description('an object in the shape of a circle, usually made of gold and precious stones, that a king or queen wears on his or herhead on official occasions fffff')
print(split_description)
for text in split_description:
    print(getTextWidth(" " + text,TEXT_SIZE))
    print(" " + text)
getTextWidth("you",TEXT_SIZE)