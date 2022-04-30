# 정적 크롤링(2)

### BeautifulSoup 클래스
- html 데이터를 두번째 인자로 받은 데이터 타입으로 변환해준다

  ```python
  bs4.BeautifulSoup("HTML 데이터", "데이터 타입")
  ```

### find 함수 
- 태그와 선택자가 일치하는 가장 첫 태그를 받아온다

  ```python
  # 태그만 사용하는 경우
  html.find('태그')

  # 선택자만 사용하는 경우
  html.find(id='선택자')
  html.find(attrs={'id':'선택자'})

  # 태그 이름과 선택자 정보 모두 사용하는 경우
  html.find('태그',{'id':'선택자'})
  ```

### find_all 함수
- 태그와 선택자가 일치하는 모든 데이터를 리스트 형태로 리턴한다

  ```python
  # 태그만 사용하는 경우
  html.find_all('태그')

  # 선택자만 사용하는 경우
  html.find_all(id='선택자')
  html.find_all(attrs={'id':'선택자'})

  # 태그 이름과 선택자 정보 모두 사용하는 경우
  html.find_all('태그',{'id':'선택자'})
  ```

<br><hr><br>

## 로또 번호 출력하기

<https://dhlottery.co.kr/gameResult.do?method=byWin>

```python
"""
1. 라이브러리 불러오기
2. BeautifulSoup 객체 생성
3. find 함수
4. 함수 find_all()
5. 텍스트 데이터 추출
"""

import requests
import bs4


URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find('div',{'class':'nums'})

#print(target)
balls = target.find_all("span",{"class":"ball_645"})

print("<최근 로또 당첨 번호>")
for ball in balls:
    print("당첨번호 : ",ball.text)

print("보너스 번호 : ",balls[-1].text)
```


### 반복 학습

```python
# 로또 번호가 있는 부분 출력
import requests
import bs4

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find('div', {'class' : 'nums'})

print(target)
```

```python
# 로또 번호만 리스트로 출력
import requests
import bs4

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find('div', {'class' : 'nums'})
# print(target)
balls = target.find_all("span", {'class' : 'ball_645'})

for ball in balls:
    print(ball)
```

```python
# 로또 번호를 텍스트 데이터로 추출
import requests
import bs4

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find('div', {'class' : 'nums'})
# print(target)
balls = target.find_all("span", {'class' : 'ball_645'})

for ball in balls:
    print("당첨번호 : ", ball.text)
```
