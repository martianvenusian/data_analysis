### Beautiful Soap documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from string import punctuation
import urllib.request
import requests
from bs4 import BeautifulSoup
from requests.api import get
from mecab import Mecab


# def get_core_words_kr(text):
#     return MeCab.morphs(text)

def get_text(url):
    text = ""
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    # print(soup)    
    # print(soup.prettify())
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.title.parent.name)
    # print(soup.p)
    # print(soup.get_text())
        

    # remove whitespaces
    # for string in soup.stripped_strings:
    for string in soup.find('div', class_ = 'postContent').stripped_strings:        
        text += string + " "    
    return text
    
def clean_text(text):
    _data = text.lower()
    # remove special characters
    # for i in punctuation:
    #     _data = _data.replace(i, "")
    _data = _data.split()
    
    return _data

if __name__ == "__main__":
    # count_word_freq(data)
    url = "https://daryo.uz/2021/08/01/tokio-2020-fransiyalik-bokschi-hakamlar-qaroridan-norozi-bo%ca%bblib-1-soat-davomida-ringni-tark-etmadi-bu-jangda-bahodir-jalolovning-yarim-finaldagi-raqibi-aniqlangandi/"    
    text = get_text(url)
    print(text)

    core_words = get_core_words_kr(text)
    print(core_words)

    data = clean_text(text)
    print(data)