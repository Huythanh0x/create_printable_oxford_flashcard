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

craw_a_list_word_and_export_html("ielts_list_word")