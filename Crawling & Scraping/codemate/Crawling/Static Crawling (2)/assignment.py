# 과제 - 유의미한 데이터 추출하기
# 네이버 웹툰 요일별 인기 웹툰 이름 출력

import requests
import bs4


URL = 'https://comic.naver.com/webtoon/weekday?order=User'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

columns = html.find_all('div',{'class':'col_inner'})

for column in columns:
    day = column.find('h4').text
    webtoons = column.find_all('a',{'class':'title'})
    print(day)
    for idx in range(len(webtoons)):
        print(f'{idx+1}. {webtoons[idx].text}')
    print()
                    
