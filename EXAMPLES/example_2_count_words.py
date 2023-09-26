from EXAMPLES.example_1_clean_text import get_text
from collections import Counter
from example_1_clean_text import get_text
from example_1_clean_text import clean_text

def count_word_freq(data):
    _data = data
    cnt = Counter(_data)
    return cnt

if __name__ == "__main__":
    # count_word_freq(data)
    url = "https://daryo.uz/2021/08/01/tokio-2020-fransiyalik-bokschi-hakamlar-qaroridan-norozi-bo%ca%bblib-1-soat-davomida-ringni-tark-etmadi-bu-jangda-bahodir-jalolovning-yarim-finaldagi-raqibi-aniqlangandi/"

    text = get_text(url)
    print(text)
    data = clean_text(text)
    print(data)

    cnt = count_word_freq(data=data)
    print(cnt)