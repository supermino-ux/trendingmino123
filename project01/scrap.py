import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://search.naver.com/search.naver?&where=news&query=%EC%9B%B9%ED%88%B0', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

client = MongoClient('localhost',27017)
db = client.webtoon


# trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# divs = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
def my_scrap():
    cnt = 0
    result = []
    for i in range(0, 100):
        # sp_nws1
        content = soup.select(f'#sp_nws{i}')

        if len(content) != 0:
            url = content[0].select_one('div.news_wrap.api_ani_send > div > a')['href']
            title = content[0].select_one('div.news_wrap.api_ani_send > div > a')['title']
            update = content[0].select_one('div.news_wrap.api_ani_send > div > div.news_info > div > span').text
            img = content[0].select_one('div.news_wrap.api_ani_send > a > img')['src']
            cnt = cnt + 1
            if cnt == 6:
                break
            else:
                news = {
                    'title': title,
                    'update': update,
                    'img': img,
                    'url':url,
                }
                result.append(news)
                # mongodb insert
                # db.news.insert_one(news)
            print(url, title, update, img)
    return result

my_scrap()


    # sp_nws1

    # for div in divs:
    #     print(div)
    # # 아래 빈 칸('')을 채워보세요
    # for tr in trs:
    #     rank = tr.select_one('td.number').text[0:2].strip()
    #     title = tr.select_one('a.title.ellipsis').text.strip()
    #     artist = tr.select_one('a.artist.ellipsis').text
    #     print(rank, title, artist)
