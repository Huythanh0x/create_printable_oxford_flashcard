import math
from fontTools.ttLib import TTFont


MAX_WIDTH = 285
TEXT_SIZE = 15
NUMBER_CARD_PER_PAGE = 20
NUMBER_CARD_PER_ROW = 4
MARGIN_RIGHT = 20

class HTMLFlashCardGenerator():
    def __init__(self,file_name) -> None:
        self.file_name = file_name
        self.NUMBER_CARD_PER_PAGE = NUMBER_CARD_PER_PAGE
        self.NUMBER_CARD_PER_ROW = NUMBER_CARD_PER_ROW
        self.MAX_WIDTH = MAX_WIDTH
        self.TEXT_SIZE = TEXT_SIZE
        ##init font
        font = TTFont('font/Voces-Regular.ttf')
        cmap = font['cmap']
        self.t = cmap.getcmap(3,1).cmap
        self.s = font.getGlyphSet()
        self.units_per_em = font['head'].unitsPerEm

    def getTextWidth(self,text,pointSize):
        total = 0
        for c in text:
            if ord(c) in self.t and self.t[ord(c)] in self.s:
                total += self.s[self.t[ord(c)]].width
            else:
                total += self.s['.notdef'].width
        total = total*float(pointSize)/self.units_per_em;
        return total
    
    def get_split_description(self,text):

        list_splitted_text = text.split(' ')
        start_index_line = 0
        description = []
        for i,word in enumerate(list_splitted_text):
            if self.getTextWidth(" ".join(list_splitted_text[start_index_line:i]),TEXT_SIZE) > MAX_WIDTH:
                description +=  [" ".join(list_splitted_text[start_index_line:i-1])]
                start_index_line = i-1
            if i+1==len(list_splitted_text) and self.getTextWidth(" ".join(list_splitted_text[start_index_line:i+1]),TEXT_SIZE) > MAX_WIDTH:
                description +=  [" ".join(list_splitted_text[start_index_line:i-1])]
                start_index_line = i-1

        description += [" ".join(list_splitted_text[start_index_line:i+1])]
        return description


    def create_html_flash_card(self):
        with open(f'data_csv/{self.file_name}.csv','r') as f:
            word_list = f.readlines() 

        number_of_word = len(word_list)
        number_of_page = math.ceil(len(word_list)/NUMBER_CARD_PER_PAGE)
        with open(f'output_html/{self.file_name}.html','w') as f:
            # style_css = "@media print {   .pagebreak { page-break-before: always; } /* page-break-after works, as well */}*{    margin: 0;}.container{    position: relative;    margin: 0px "+ str(MARGIN_RIGHT) +"px 0px 0px;    display: flex;}.front_card{    margin-left:0px;    width: 283.4px;    height: 154.4px;    background: #FFFFFF;    border-radius: 0px;    border: black 2px solid;    position: relative;}.front_card .type_of_word{position: absolute;width: auto;padding:3px 5px;height: 12px;font-family: sans-serif;left: 0px;top: 0px;background: #FFFFFF;border-radius: 15px;border: black 2px solid;font-style: normal;font-weight: normal;font-size: 12px;line-height: 14px;color: #000000;text-align: center;}.front_card .word{position: absolute;width: auto;height: 19px;top: 28px;margin: 0px 0px 0px;left:50%;transform: translateX(-50%);font-family: 'Montserrat', sans-serif;font-style: normal;font-weight: 700;font-size: 26px;line-height: 30px;color: #0798D6;}.front_card .describe{    position: absolute;width: 94%;height: auto;left: 50%;transform: translateX(-50%);top: 75px;font-family: sans-serif;font-style: normal;font-weight: normal;font-size: 14px;line-height: 110%;color: #000000;}.back_card{margin-left:0px;width: 283.4px;height: 154.4px;background: #FFFFFF;border-radius: 0px;border: black 2px solid;position: relative;transform: rotate(-180deg);}.back_card .ipa{    position: absolute;    width: max-content;    height: 19px;    top: 15px;    left: 50%;    font-family: 'Montserrat', sans-serif;    font-style: normal;    font-weight: 700;    font-size: 26px;    line-height: 30px;    transform: translateX(-50%);    color: #0798D6;}.back_card .example{    font-family: sans-serif;    margin-bottom: 8px;    font-style: normal;    font-weight: normal;    font-size: 14px;    line-height: 110%;    color: #000000;}.container_example{    position: absolute;    width: 94%;    height: auto;    left: 50%;    transform: translateX(-50%);    top: 60px;}.footer{    font-family: sans-serif;    margin-bottom: 8px;    margin-right: 5px;    position: absolute;    font-style: normal;    font-weight: normal;    font-size: 10px;    line-height: 0;    color: #000000;    bottom: 0;    right: 0;}.additional_describe{position: absolute;width: 80%;top:120px;height: auto;left:40px;font-family: sans-serif;font-style: normal;font-weight: normal;font-size: 14px;line-height: 110%;color: #000000;}.back_card{margin-left:0px;width: 283.4px;height: 154.4px;background: #FFFFFF;border-radius: 0px;border: black 2px solid;position: relative;transform: rotate(-180deg);}"
            
            f.writelines(f'<!DOCTYPE html><html lang="en"><head>    <link rel="stylesheet" href="./index.css"><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{self.file_name}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;500;700&display=swap" rel="stylesheet"></head><body>')

        with open(f'output_html/{self.file_name}.html','a') as f:
            for page_index in range(number_of_page):
                for row in range(NUMBER_CARD_PER_PAGE//NUMBER_CARD_PER_ROW):
                    f.writelines('<div class="container">')
                    base_index = page_index*NUMBER_CARD_PER_PAGE+row*NUMBER_CARD_PER_ROW
                    for card in range(NUMBER_CARD_PER_ROW):
                        card_index = base_index + card    
                        if card_index < number_of_word:
                            type_of_speech = word_list[card_index].split('|')[2]
                            en_word = word_list[card_index].split('|')[1]
                            description = word_list[card_index].split('|')[4]
                            if len(description) > 170:
                                description = description.split('.')[0]
                            if len(description) > 170:
                                description = description.split(';')[0]
                            split_description = self.get_split_description(description)
                            main_description = ""
                            additional_description = ""
                            for i,_ in enumerate(split_description):
                                if i < 3:
                                    main_description += " " + split_description[i]
                                else:
                                    additional_description += " " + split_description[i]

                        else:
                            type_of_speech = "noun"
                            en_word = "BatDauLapTrinh"
                            description = "FFFF"
                        if len(description) > 170:
                            front_card_html = f'<div class="front_card"><span class="type_of_word">{type_of_speech}</span><h2 class="word">{en_word}</h2><p class="describe" style="top:55px;">{main_description}</p><p class="additional_describe" style="top:100px;">{additional_description}</p></div>'
                        else:
                            front_card_html = f'<div class="front_card"><span class="type_of_word">{type_of_speech}</span><h2 class="word">{en_word}</h2><p class="describe">{main_description}</p><p class="additional_describe">{additional_description}</p></div>'
                        f.write(front_card_html)
                    f.writelines('</div>')
                
                for row in range(NUMBER_CARD_PER_PAGE//NUMBER_CARD_PER_ROW):
                    f.writelines('<div class="container">')
                    base_index = page_index*NUMBER_CARD_PER_PAGE+row*NUMBER_CARD_PER_ROW
                    for card in range(NUMBER_CARD_PER_ROW-1,-1,-1):
                        card_index = base_index + card    
                        if card_index < number_of_word:
                            api_us = word_list[card_index].split('|')[6]
                            example = word_list[card_index].split('|')[9].split(';')[0]
                            example_x = ""
                            if len(example) < 50:
                                try:
                                    if len(word_list[card_index].split('|')[9].split(';')[1]) < 80: 
                                        example_x = word_list[card_index].split('|')[9].split(';')[1]
                                    else:
                                        example_x = ""
                                except:
                                    pass
                        else:
                            api_us = "   BatDauLapTrinh"
                            example = "How to create English Flashcard for printing"
                            example_x = "Use study set to learn anything you want in ELSA SPEAK FREE"
                        f.write(f'<div class="back_card"><h2 class="ipa">{api_us}</h2><div class="container_example"><p class="example">{example}</p><p class="example">{example_x}</p></div></div>')
                    f.writelines('</div>')
                f.writelines('<div class="pagebreak"> </div>')
        with open(f'output_html/{self.file_name}.html','a') as f:
            f.writelines('</body></html>')        
