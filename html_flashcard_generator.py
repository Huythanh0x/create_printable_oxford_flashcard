import math
NUMBER_CARD_PER_PAGE = 20
NUMBER_CARD_PER_ROW = 4

class HTMLFlashCardGenerator():
    def __init__(self,file_name) -> None:
        self.file_name = file_name
        self.NUMBER_CARD_PER_PAGE = NUMBER_CARD_PER_PAGE
        self.NUMBER_CARD_PER_ROW = NUMBER_CARD_PER_ROW

    def create_html_flash_card(self):
        with open(f'data_csv/{self.file_name}.csv','r') as f:
            word_list = f.readlines() 

        number_of_word = len(word_list)
        number_of_page = math.ceil(len(word_list)/NUMBER_CARD_PER_PAGE)
        number_of_card = number_of_page * NUMBER_CARD_PER_PAGE
        with open(f'output_html/{self.file_name}.html','w') as f:
            style_css = "@media print {   .pagebreak { page-break-before: always; } /* page-break-after works, as well */}*{    margin: 0;}.container{    margin: 0px 0px 0px;    display: flex;}.front_card{    margin-left:0px;    width: 283.4px;    height: 154.40624238px;    background: #FFFFFF;    border-radius: 0px;    border: black 2px solid;    position: relative;}.front_card .type_of_word{position: absolute;width: auto;padding:3px 5px;height: 12px;font-family: sans-serif;left: 0px;top: 0px;background: #FFFFFF;border-radius: 15px;border: black 2px solid;font-style: normal;font-weight: normal;font-size: 12px;line-height: 14px;color: #000000;text-align: center;}.front_card .word{position: absolute;width: auto;height: 19px;top: 28px;margin: 0px 0px 0px;left:50%;transform: translateX(-50%);font-family: 'Montserrat', sans-serif;font-style: normal;font-weight: normal;font-size: 26px;line-height: 30px;color: #0798D6;}.front_card .describe{    position: absolute;width: 94%;height: auto;left: 50%;transform: translateX(-50%);top: 75px;font-family: sans-serif;font-style: normal;font-weight: normal;font-size: 14px;line-height: 110%;color: #000000;}.back_card{margin-left:0px;width: 283.4px;height: 154.40624237px;background: #FFFFFF;border-radius: 0px;border: black 2px solid;position: relative;transform: rotate(-180deg);}.back_card .ipa{    position: absolute;    width: max-content;    height: 19px;    top: 15px;    left: 50%;    font-family: 'Montserrat', sans-serif;    font-style: normal;    font-weight: normal;    font-size: 26px;    line-height: 30px;    transform: translateX(-50%);    color: #0798D6;}.back_card .example{    font-family: sans-serif;    margin-bottom: 8px;    font-style: normal;    font-weight: normal;    font-size: 14px;    line-height: 110%;    color: #000000;}.container_example{    position: absolute;    width: 94%;    height: auto;    left: 50%;    transform: translateX(-50%);    top: 60px;}"
            f.writelines(f'<!DOCTYPE html><html lang="en"><head><style>{style_css}</style><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Flash card</title><link rel="stylesheet" href="./index.css"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;500;700&display=swap" rel="stylesheet"></head><body>')

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
                            if len(description) > 100:
                                description = description.split('.')[0]
                        else:
                            type_of_speech = "noun"
                            en_word = "BatDauLapTrinh"
                            description = "A blog where I share my career journey and some learnings I picked up along the way"
                        f.write(f'<div class="front_card"><span class="type_of_word">{type_of_speech}</span><h2 class="word">{en_word}</h2><p class="describe">{description}</p></div>')
                    f.writelines('</div>')
                
                for row in range(NUMBER_CARD_PER_PAGE//NUMBER_CARD_PER_ROW):
                    f.writelines('<div class="container">')
                    base_index = page_index*NUMBER_CARD_PER_PAGE+row*NUMBER_CARD_PER_ROW
                    for card in range(NUMBER_CARD_PER_ROW):
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
                            api_us = "Blog BatDauLapTrinh"
                            example = "How to create English Flashcard for printing"
                            example_x = "Use study set to learn anything you want in ELSA SPEAK FREE"
                        f.write(f'<div class="back_card"><h2 class="ipa">{api_us}</h2><div class="container_example"><p class="example">{example}</p><p class="example">{example_x}</p></div></div>')
                    f.writelines('</div>')
                f.writelines('<div class="pagebreak"> </div>')
        with open(f'output_html/{self.file_name}.html','a') as f:
            f.writelines('</body></html>')        