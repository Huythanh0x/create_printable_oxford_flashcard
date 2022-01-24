from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import bs4

class OxfordWordCrawler():
    def __init__(self):
        op = webdriver.ChromeOptions()
        # op.add_argument('headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
        self.BASE_URL = f"https://www.oxfordlearnersdictionaries.com"
    
    def get_html_from_local_html(self):
        with open('Oxford 3000 and 5000 _ OxfordLearnersDictionaries.com.html','r') as f:
            self.html_content = '\n'.join(f.readlines())

    def get_html_from_remote(self):
        URL_3000 = "https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000"
        self.driver.get(URL_3000)
        self.html_content = self.driver.page_source
    
    def get_data_from_url(self,clean_word_url):
        self.driver.get(clean_word_url)
        detail_word_html = self.driver.page_source
        soup = bs4.BeautifulSoup(detail_word_html)
        _id = clean_word_url.split('/')[-1]
        en_word = soup.find('h1', attrs={ "class" : "headword"})
        en_word = en_word.text        
        definition = soup.find('span',{'class':'def'})
        definition = definition.text
        try:
            examples = [example.text for example in soup.find('ul',{'class':'examples'})]
            pass
            if examples is not None and len(examples) > 0:
                examples = ";".join(examples)
            else:
                examples = 'There is no example for this word'
        except:
            pass
            examples = 'There is no example for this word'
        api_uk = soup.find('div',{'class':'phons_br'}).span
        api_uk = api_uk.text
        mp3_uk = soup.find('div',{'class':'phons_br'}).div
        mp3_uk = mp3_uk['data-src-mp3']
        api_us = soup.find('div',{'class':'phons_n_am'}).span
        api_us = api_us.text
        mp3_us = soup.find('div',{'class':'phons_n_am'}).div
        mp3_us = mp3_us['data-src-mp3']
        try:
            cefr = soup.find('div',attrs={"hclass":"symbols"}).a
            symbol = cefr.span['class'][0]
            cefr = cefr["href"].split("level=")[1].upper()
            if cefr == 'B2' and '5' in symbol:
                cefr = 'B2+'
        except:
            cefr = "D"
        type = soup.find('span',attrs={"class":"pos"})
        type = type.text
        return _id,en_word,type,cefr,definition,api_uk,api_us,mp3_uk,mp3_us,examples,clean_word_url

    def get_clean_word_list_url(self):
        soup = bs4.BeautifulSoup(self.html_content, "html.parser")
        word_list = soup.find('ul', attrs={ "class" : "top-g"})

        clean_wor_list_url = [self.BASE_URL + word.a["href"] for word in word_list if isinstance(word,bs4.element.Tag)]
        self.clearn_word_list_url = clean_wor_list_url

    def crawl_5000_words(self):
        self.get_html_from_remote()
        self.get_clean_word_list_url()
        for word_url in self.clearn_word_list_url:
            try:
                _id,en_word,type,cefr,definition,api_uk,api_us,mp3_uk,mp3_us,examples,clean_word_url = self.get_data_from_url(word_url)
                if cefr == "B2+" or cefr == "C1":
                    with open(f"data_csv/_2k_advance.csv","a") as f:
                        f.write(f"{_id}|{en_word}|{type}|{cefr}|{definition}|{api_uk}|{api_us}|{mp3_uk}|{mp3_us}|{examples}|{clean_word_url}\n")
                else:
                    with open(f"data_csv/_3k_basic.csv","a") as f:
                        f.write(f"{_id}|{en_word}|{type}|{cefr}|{definition}|{api_uk}|{api_us}|{mp3_uk}|{mp3_us}|{examples}|{clean_word_url}\n")    
            except:
                with open('error.log','a') as f:
                    f.writelines(f'{word_url}')

    def crawl_list_word(self,list_word,output_name):
        for word in list_word:
            word_url = self.BASE_URL +"/definition/english/"+ word
            try:
                _id,en_word,type,cefr,definition,api_uk,api_us,mp3_uk,mp3_us,examples,clean_word_url = self.get_data_from_url(word_url)
                with open(f"data_csv/{output_name}.csv","a") as f:
                    f.write(f"{_id}|{en_word}|{type}|{cefr}|{definition}|{api_uk}|{api_us}|{mp3_uk}|{mp3_us}|{examples}|{clean_word_url}\n")    
            except:
                with open('error.log','a') as f:
                    f.writelines(f'{word_url}')
