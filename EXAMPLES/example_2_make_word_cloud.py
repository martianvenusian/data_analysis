from wordcloud import WordCloud
from example_1_count_words import get_text
from example_1_count_words import count_word_freq
from example_1_count_words import clean_text

def crate_world_cloud(counter):
    cloud = WordCloud(background_color='white')
    cloud.fit_words(counter)
    cloud.to_file('test.png')
    
    

if __name__ == "__main__":
    url = "https://daryo.uz/2021/08/01/tokio-2020-fransiyalik-bokschi-hakamlar-qaroridan-norozi-bo%ca%bblib-1-soat-davomida-ringni-tark-etmadi-bu-jangda-bahodir-jalolovning-yarim-finaldagi-raqibi-aniqlangandi/"
    text = get_text(url)
    data = clean_text(text)
    cnt = count_word_freq(data)
    crate_world_cloud(cnt)


# source: https://m.blog.naver.com/PostView.naver?blogId=alwaysblue15&logNo=222016956240&navType=tl