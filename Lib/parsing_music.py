from bs4 import BeautifulSoup
import requests
import lxml
from urllib.parse import quote

def get_artist_col(p_letter):
    # Define URL
    url = "https://my.mail.ru/music/artists-letters/"
    alphabet = p_letter
    dict_ = {}
    dict_artist = {}

    #Перебирам артистов по алфавиту
    for i in alphabet:
        url_ = url + quote(i)
        pages = requests.get(url_)
        soup = BeautifulSoup(pages.text, "lxml")
        count = len(soup.find_all('a', class_='page sp-music-booster')) + 1
        #Перебираем страницы с артистами на заданную букву
        for j in range(count):
            url_x = url_ + '/pages/' + str(j+1)
            page_ = requests.get(url_x)
            soup_ = BeautifulSoup(page_.text, "lxml")
            res = soup_.find_all('a', class_='b-music__artists-list__item__name sp-music-booster')
            
            for k in range(len(res)):
                dict_[res[k].text] = res[k].get('href')
    #Перебираем альбомы
    for l in dict_.keys():
        url_artist = 'https://my.mail.ru' + dict_.get(l) + '/albums'
        page_artist = requests.get(url_artist)
        soup_artist = BeautifulSoup(page_artist.text, "lxml")
        res_artist = soup_artist.find_all('a', class_='t-music__h2 sp-music-booster')
        #Получаем словарь Альбом - ссылка
        dict_album = {}
        for m in range(len(res_artist)):
            dict_album[res_artist[m].text.strip()] = res_artist[m].get('href')
        #Перебираем страницы альбомов
        dict_song = {}
        for n in dict_album.keys():
            url_album = 'https://my.mail.ru' + dict_album.get(n)
            page_album = requests.get(url_album)
            soup_album = BeautifulSoup(page_album.text, "lxml")
            res_song = soup_album.find_all('div', class_='songs-table__row__col__title songs-table__row__col__title--name name')
            #Получаем список треков по каждому альбому
            list_song = []
            for o in range(len(res_song)):
                list_song.append(res_song[o].text.strip())
            #Собираем словарь альбом - треки
            dict_song[n] = list_song
        #Собираем итоговый словарь Артист - альбом - треки
        dict_[l] = dict_song
    return dict_
