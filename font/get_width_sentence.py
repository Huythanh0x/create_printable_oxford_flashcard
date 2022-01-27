from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable

MAX_WIDTH = 265
TEXT_SIZE = 14

font = TTFont('font/Roboto-400.ttf')
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

text = 'a person who works to achieve political or social change, especially as a member of an organization with particular aims'
list_splitted_text = text.split(' ')
start_index_line = 0
for i,word in enumerate(list_splitted_text):
    if getTextWidth(" ".join(list_splitted_text[start_index_line:i]),TEXT_SIZE) < MAX_WIDTH:
        pass
    else:
        print(" ".join(list_splitted_text[start_index_line:i-1]))
        print(getTextWidth(" ".join(list_splitted_text[start_index_line:i-1]),TEXT_SIZE))
        start_index_line = i-1

# text = "language that shows which country, area"
# width = getTextWidth(text,14)
# print ('Text: "%s"' % text)
# print ('Width in points: %f' % width)
# print(len(text))
print("-------------------------------------------------------")
print(getTextWidth("a way of pronouncing the words of a",14))
print(getTextWidth(" language that shows which country, area",14))
print(getTextWidth("or social class a person comes from; how",14))
print(getTextWidth("welll somebody pronounces a particular",14))
print(getTextWidth("the fact of somebody being away from a",14))
print(getTextWidth("place where they are usually expected to",14))
print(getTextWidth("the fact of being responsible for your",14))
print(getTextWidth("decisions or actions and expected to",14))
print(getTextWidth("responsible for your decisions or actions",14))
print(getTextWidth("the condition of being unable to stop using",14))
print(getTextWidth("or doing something as a habit, especially",14))
print(getTextWidth("something, or of being changed, to suit a",14))
print(getTextWidth("and expected to explain them when you",14))
print("-------------------------------------------")
print(getTextWidth("a way of pronouncing the words of a language",14))
print(getTextWidth(" language that shows which country, area or",14))
print(getTextWidth("or social class a person comes from; how well",14))
print(getTextWidth("welll somebody pronounces a particular language",14))
print(getTextWidth("the fact of somebody being away from a place",14))
print(getTextWidth("place where they are usually expected to be;",14))
print(getTextWidth("the fact of being responsible for your decisions",14))
print(getTextWidth("decisions or actions and expected to explain",14))
print(getTextWidth("responsible for your decisions or actions and",14))
print(getTextWidth("the condition of being unable to stop using or",14))
print(getTextWidth("or doing something as a habit, especially something",14))
print(getTextWidth("something, or of being changed, to suit a new",14))
print(getTextWidth("and expected to explain them when you are",14))



# print ('Width in inches: %f' % (width/72))
# print ('Width in cm: %f' % (width*2.54/72))
# print ('Width in WP Units: %f' % (width*1200/72))