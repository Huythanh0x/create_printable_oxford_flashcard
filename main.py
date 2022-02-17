from this import d
import requests
from bs4 import BeautifulSoup
from html_flashcard_generator import HTMLFlashCardGenerator
from oxford_word_crawler import OxfordWordCrawler


def crawl_570_words_from_url():
    raw_html = requests.get("https://igeenglish.com/ielts-vocabulary/570-academic-word-list/").content
    soup = BeautifulSoup(raw_html)
    table = soup.find("tbody")
    with open('data_csv/_570_academic_words.csv','a') as f:
        word_list = [word.find('td').text for word in table.find_all("tr")]
    crawler = OxfordWordCrawler()
    crawler.crawl_list_word(word_list,'_570_academic_words')

def create_570_flashcards_html():
    generator = HTMLFlashCardGenerator('_570_academic_words')
    generator.create_html_flash_card()


def craw_a_list_word_and_export_html(output_file_name):
    with open("input_word_list/word_list.txt",'r') as f:
        word_list = f.readlines()
    crawler = OxfordWordCrawler()    
    crawler.crawl_list_word(word_list,f'{output_file_name}')

    generator = HTMLFlashCardGenerator(f'{output_file_name}')
    generator.create_html_flash_card()

def crawl_5k_words():
        crawler = OxfordWordCrawler()
        crawler.crawl_5000_words()

def create_flashcard_from_csv(file_name):

    generator = HTMLFlashCardGenerator(f'{file_name}')
    generator.create_html_flash_card()

def crawl_word_list(word_list,output_file_name):
    crawler = OxfordWordCrawler()    
    crawler.crawl_list_word(word_list,f'{output_file_name}')

def find_duplicate_in_file(file_name):
    with open(file_name) as f:
        list_word = f.readlines()
    list_w = [word.split('|')[0] for word in  list_word]
    # print(list_w)
    set_duplicate = set([x for x in list_w if list_w.count(x) > 1])
    print(set_duplicate)
    print(len(list_word))
    set_word = set(list_w)
    print(len(set_word))


# crawl_5k_words()

# create_flashcard_from_csv('_2k_advance')
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
    seq = [w for w in seq]
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


# create_flashcard_from_csv('vocab_for_IELTS')

# crawl_570_words_from_url()

# get_word_list_exclude_5k("vocab_for_IELTS")


# with open('input_word_list/word_list.txt','r') as f:
#     word_list = set(f.readlines())
#     print(word_list)

# word_list = [word.split('?q=')[0].split('/english/')[1] for word in word_list]
# print(word_list)

# crawl_word_list(word_list,"multiple_meaning")



# craw_a_list_word_and_export_html("multiple_meaning")

# create_flashcard_from_csv('_2k_advance')

# remove_duplicate_in_file('data_csv/_570_academic_words_exclude_5k.csv')
# crawl_5k_words()

# crawl_570_words_from_url()
# create_570_flashcards_html()

# craw_a_list_word_and_export_html("ielts_list_word")

# remove_duplicate_in_file('data_csv/for_print_today.csv')


# remove_A1_A2_B1("data_csv/for_print_today.csv")

create_flashcard_from_csv('_3k_basic')

# craw_a_list_word_and_export_html("demo_con_lon_small")


# create_flashcard_from_csv('demo')
# remove_duplicate_in_file('data_csv/for_print_today_excep_A1A2B1.csv')

# find_duplicate_in_file('data_csv/origin_for_print_today_excep_A1A2B1.csv')
