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

### 간단한 실습 
- 네이버 웹툰의 요일 별 상위 웹툰 이름을 받아오기
  - 네이버 웹툰 html 텍스트 받아오기
    ```python
    import requests
    import bs4

    req = requests.get("https://comic.naver.com/webtoon/weekday")
    print(req.text)
    ```
    <br> [결과창]()
