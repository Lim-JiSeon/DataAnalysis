# 라이브러리(Library)

## 프로그래밍을 할 때, 코드를 작성하지 않고 필요한 기능을 수행할 수 있도록 마련된 함수와 메소드의 집합을 말한다.

### 정적 크롤링
  - requests
    <br>requests 라이브러리는 기존에 어려운 HTTP 요청을 쉽게 사용하기 위해 만들어진 라이브러리로, 파이썬과 웹을 연결하기 위해 사용
 
  ```
  pip install requests 
  ```
 
  - beautifulsoup4(BeautifulSoup)
    <br>beautifulsoup4 라이브러리는 requests로 받아온 HTML 데이터를 다루기 위해 사용되는 라이브러리로, 웹에 있는 다양한 데이터 중 필요한 데이터만 뽑아내기 위해 사용

  ```
  pip install beautifulsoup4
  ```

<hr>

### 간단한 실습 
- 네이버 웹툰의 요일 별 상위 웹툰 이름을 받아오기
  - 네이버 웹툰 html 텍스트 받아오기(1) - 연결
    ```python
    import requests
    import bs4

    req = requests.get("https://comic.naver.com/webtoon/weekday")
    print(req.text)
    ```
    <br> [결과창 보기](https://github.com/Lim-JiSeon/DataAnalysis/blob/main/Crawling%20%26%20Scraping/codemate/Crawling/Library/example_result1.html)
    
  - 네이버 웹툰 html 텍스트 받아오기(2) - html
    ```python
    import requests
    import bs4
    
    req = requests.get("https://comic.naver.com.webtoon.weekday")
    
    html = bs4.BeautifulSoup(req.text,'html.parser')
    print(html)
    ```
    <br> [결과창 보기](https://github.com/Lim-JiSeon/DataAnalysis/blob/main/Crawling%20%26%20Scraping/codemate/Crawling/Library/example_result2.html)
    
  - 네이버 웹툰 요일 별 상위 웹툰 이름 받아오기 
    ```python
    import requests
    import bs4

    req = requests.get("https://comic.naver.com/webtoon/weekday")
   
    html = bs4.BeautifulSoup(req.text, 'html.parser')
   
    columns = html.find_all('div', {'class':'col_inner'})         # 원하는 데이터를 columns에 저장

    for column in columns:                                        # 요일 받아와서 day에 저장 후 출력
        day = column.find('h4').text
        webtoons = column.find_all('a',{'class':'title'})[:5]
        print(day)

        for index in range(len(webtoons)):                        # 요일별 상위 웹툰이름을 title에 받아와서 저장 후 출력 -> index가 순위 title이 웹툰 이름
            title = webtoons[index].text
            print(f'{index+1}.{title}')
        print()
    ```
    <br> 실행 결과
    ```text
    월요 웹툰
    1.참교육
    2.쇼미더럭키짱!
    3.신의 탑
    4.뷰티풀 군바리
    5.퀘스트지상주의

    화요 웹툰
    1.쇼미더럭키짱!
    2.여신강림
    3.김부장
    4.멸망 이후의 세계
    5.1을 줄게

    수요 웹툰
    1.쇼미더럭키짱!
    2.전지적 독자 시점
    3.화산귀환
    4.헬퍼 2 : 킬베로스
    5.먹는 인생

    목요 웹툰
    1.독립일기
    2.쇼미더럭키짱!
    3.연애혁명
    4.더 복서
    5.나노마신

    금요 웹툰
    1.외모지상주의
    2.쇼미더럭키짱!
    3.갓 오브 하이스쿨
    4.나 혼자 만렙 뉴비
    5.내과 박원장

    토요 웹툰
    1.프리드로우
    2.신림/남/22
    3.취사병 전설이 되다
    4.은탄
    5.먹는 인생

    일요 웹툰
    1.독립일기
    2.싸움독학
    3.입학용병
    4.열렙전사
    5.약한영웅
    ```
    

<hr>

# 문제 해결

1. pip version update 오류
  - pip install requests 할 때 pip version upgrade 하라는 알림이 뜸
    ```
    WARNING : You are using pip version 19.2.3, however version 20.0.2 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.
    ```
    ```
    pip install --upgrade pip
    ```
    --> OSError 발생
2. OSError
  - user permission 하라는 알림이 뜸
    ```
    OSError
    ~중략~
    Consider using the `--user` option or check the permissions.
    ```
    ```
    pip install --user
    ```
    --> 한 뒤 다시 upgrade하니 성공
    
    
    
    
    
    
    
