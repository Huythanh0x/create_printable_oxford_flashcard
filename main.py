import requests
from bs4 import BeautifulSoup
from html_flashcard_generator import HTMLFlashCardGenerator
from oxford_word_crawler import OxfordWordCrawler
import glob
import os

def crawl_570_words():
    raw_html = requests.get("https://igeenglish.com/ielts-vocabulary/570-academic-word-list/").content
    soup = BeautifulSoup(raw_html)
    table = soup.find("tbody")
    word_list = [word.find('td').text for word in table.find_all("tr")]
    crawler = OxfordWordCrawler()
    crawler.crawl_list_word(word_list,'_570_academic_words')



def craw_a_list_word(output_file_name):
    with open("input_word_list/word_list.txt",'r') as f:
        word_list = f.readlines()
    crawler = OxfordWordCrawler()    
    crawler.crawl_list_word(word_list,f'{output_file_name}')

def crawl_5000_words():
        crawler = OxfordWordCrawler()
        crawler.crawl_5000_words()

def create_flashcard_from_csv(file_name):

    generator = HTMLFlashCardGenerator(f'{file_name}')
    generator.create_html_flash_card()

def crawl_word_list(word_list,output_file_name):
    crawler = OxfordWordCrawler()    
    crawler.crawl_list_word(word_list,f'{output_file_name}')

def get_word_list_exclude_5k(file_name):
    with open (f"data_csv/{file_name}.csv",'r') as f:
        word_list = f.readlines()

    word_list_exclude_5k = [word for word in word_list if word.split("|")[3] == "D"]
    with open (f"data_csv/{file_name}_exclude_5k.csv",'w') as f:
        for word in word_list_exclude_5k:
            f.writelines(f"{word}")

def remove_duplicate_in_file(file_name):
    with open(file_name,'r') as f:
        list_here = f.readlines()
    new_list =  f7(list_here)

    with open(file_name,'w') as f:
        for line in new_list:
            f.writelines(f'{line}')

def remove_A1_A2_B1(file_name):
    with open(file_name,'r') as f:
        list_here = f.readlines()
    new_list =  [word for word in list_here if 'A1' not in word and 'A2' not in word and 'B1' not in word]

    with open(f"{file_name}_excep_A1A2B1.csv",'w') as f:
        for line in new_list:
            f.writelines(f'{line}')

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def get_D_cefr(file_name):
    with open(f"data_csv/{file_name}.csv",'r') as f:
        list_here = f.readlines()
    new_list =  [word for word in list_here if '|D|' in word]

    with open(f"data_csv/{file_name}_file_D.csv",'w') as f:
        for line in new_list:
            f.writelines(f'{line}')
def create_list_word_for_ELSA(file_name):
    with open(f'data_csv/{file_name}.csv','r') as f:
        list_word = f.readlines()
    pure_list_word = []
    for word in list_word:
        pure_list_word.append(word.split("|")[1].strip())
        pure_list_word.append(str(BeautifulSoup(word.split("|")[9]).text.split(';')[-1]).strip())

    with open(f'output_word_list_for_elsa/{file_name}','w') as f:
        f.writelines("\n".join(pure_list_word))

def rename_file_multiple_part():
    full_files_name = glob.glob("data_csv/*")
    pure_files_name = [name[:-11] for name in full_files_name]
    # print(pure_files_name)
    multiple_parts_files_name = []
    for i,name in enumerate(pure_files_name):
        if pure_files_name.index(name) != i:
            multiple_parts_files_name.append(name)
    single_part_files_name = [file_name for file_name in pure_files_name if file_name not in multiple_parts_files_name]

    for single_part_file_name in single_part_files_name:
        try:
            os.rename(f'{single_part_file_name}_part_1.csv',f'{single_part_file_name}_full_part.csv')
        except:
            print(f'don\'t need to rename {single_part_file_name}')

def create_all_flash_card():
    full_files_name = glob.glob("data_csv/*")
    for name in full_files_name:
        create_flashcard_from_csv(name[9:-4])

# craw_a_list_word("my_custom_wordlist")
# crawl_5000_words()
# remove_A1_A2_B1("data_csv/for_print_today.csv")
# get_D_cefr('ielts_list_word')
# crawl_570_words()
# create_list_word_for_ELSA('_570_academic_words')


rename_file_multiple_part()

create_all_flash_card()