# 정적 크롤링(1)
- 크롤링을 할 웹 사이트 선정
- 데이터 선정

## 로또 당첨 번호
### <https://dhlottery.co.kr/gameResult.do?method=byWin>
<img width="1272" alt="image" src="https://user-images.githubusercontent.com/83554018/166116493-052786c5-19f9-4d28-9ee0-79606df26aea.png">

- HTML 코드 확인
- 로또 번호 데이터 확인

```python
"""
HTML 코드 확인
1. 라이브러리 import
2. 웹 페이지 주소 정의
3. 웹 페이지의 HTML 코드 전체 받기
4. 요청 성공 여부 확인
5. HTML 코드 출력
"""

import requests 

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'  # 코드를 간결하게 유지할 수 있도록 변수값에 저장해서 이용
raw = requests.get(URL)

#print(raw)      # <Response [200]> 출력(요청이 정상적으로 처리되었다는 의미)
print(raw.text)  
```

```python
# 로또 번호 데이터 확인
import requests

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)
target = '<div class="nums">'

if target in raw.text:
    idx = raw.text.index(target)
    print(raw.text[idx:idx+578])
```
