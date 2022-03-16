# 선택자
## 동일한 태그를 분간해 주기 위해, HTML에서는 선택자라는걸 사용하는데, 선택자는 각 태그를 구별할 수 있는 일종의 주소를 부여하는 것을 의미한다. 

### 선택자의 필요성
- 선택자를 사용하지 않았을 경우
  ```HTML
  <div>
    <div>
      <span>파이썬</span>
      <span>크롤링</span>
    </div>

    <div>
      <span>C언어</span>
      <span>게임</span>
    </div>
  </div>
  ```
  <br>-> 언어 데이터같이 특정한 데이터만 필요해 태그를 사용하여 데이터를 선택하려고 할 때, 프로젝트 정보도 포함된다. 즉 같은 태그를 구별하기가 어렵다.

- 선택자를 사용했을 경우
  ```HTML
  <div id = "contents">
    <div class = "metadata1">
      <span class = "language">파이썬</span>
      <span class = "project">크롤링</span>
    </div>

    <div class = "metadata2">
      <span class = "language">C언어</span>
      <span class = "project">게임</span>
    </div>
  </div>
  ```
  <br>-> 언어 관련 데이터만 받아오고 싶을 경우 span 태그와 language 라는 선택자를 사용해 받아올 수 있게 된다.
  
<hr>

### id 와 class
- id
  - id는 특정 요소만 가질 수 있는 고유한 값으로, 우리나라 국민들의 주민등록번호, 한 학교 학생들의 학번 등과 같다.
  - HTML에서도 하나의 id는 고유한 선택자로, 하나의 HTML 코드에 id는 중복되지 않고 하나만 존재한다.

- class
  - class도 태그의 선택자로 사용되지만 id처럼 고유한 값은 아니며, class는 같은 속성을 지닌 데이터들을 묶어주는 값으로 사용된다.
  - class는 여러번 사용될 수 있다.

<br>

| 이름 | 닉네임 | 직업 | 언어 |  
|:------:|:-------:|:------:|:------:|
| 홍길동 | code123 | 학생 | 파이썬 |                      
| 김변수 | python99 | 직장인 | 파이썬 |
| 이바둑 | javva1 | 학생 | 자바 |
 
 -> 사람 한명을 HTML 태그로 본다면 
  
<table>
  <th>HTML태그</th>
  <th>id</th>
  <th>class</th>
  <tr>
    <td rowspan="3">사람</td>
    <td>code123</td>
    <td>학생, 파이썬</td>
  </tr>
  <tr>
    <td>python99</td>
    <td>직장인, 파이썬</td>
  </tr>
  <tr>
    <td>javva1</td>
    <td>학생, 자바</td>
  </tr>
</table>  
  
-> 닉네임은 고유한 값이므로 태그의 id가 되고, 직업과 언어는 그 사람이 가진 특성으로 비슷한 속성끼리 묶어주기 때문에 태그의 class가 된다.  
  
<hr>

### 선택자 사용법  
- 데이터 검색 방법
  - id : 태그 뒤에 # 붙이기
  - class : 태그 뒤에 . 붙이기

```html
<div id="123" class="456">
```

- 태그만 사용하여 데이터를 찾을 경우 : 태그
  ```html
  div
  ```
- 태그와 id를 사용하여 데이터를 찾을 경우 : 태그#id
  ```html
  div#123
  ```
- 태그와 class를 사용하여 데이터를 찾을 경우 : 태그.class
  ```html
  div.456
  ```
- 태그, id, class를 모두 사용하여 데이터를 찾을 경우 : 태그#id.class
  ```html
  div#123.456
  ```
- class 이름에 공백이 포함될 경우 : 공백을 .으로 대체
  ```html
  <div class="hello python">          <!--div.hello.python-->
  ```

<hr>

### 선택자 실습  
- [복권 사이트](https://dhlottery.co.kr/gameResult.do?method=byWin) 로또 번호 검색하기

  <img width="1242" alt="image" src="https://user-images.githubusercontent.com/83554018/158497513-35f2a946-605f-44eb-bfc5-be4331635137.png">


  - F12 -> 개발자 도구 창 열기
  
    <img width="1107" alt="image" src="https://user-images.githubusercontent.com/83554018/158497556-368f68bc-6237-4c7b-bd45-7aa226e53c33.png">


  - select 버튼 클릭
  
    <img width="1083" alt="image" src="https://user-images.githubusercontent.com/83554018/158497605-1833a6a5-f3e7-4a60-b573-c906f2e08a78.png">


  - 해당 태그와 선택자 찾기(Ctrl + F 누르면 검색 가능)
  
    <img width="1091" alt="image" src="https://user-images.githubusercontent.com/83554018/158497749-25a100a9-1b83-48d7-9c43-07658339b3e6.png">

- 더 정확한 검색(id + class 이용)
  - 포함관계 이용하기
  
    <img width="1087" alt="image" src="https://user-images.githubusercontent.com/83554018/158498003-b2b887e3-d1ab-4ada-98cb-5d31884b1eb4.png">
    
    ```html
    <div id="article" class="contentsArticle">
    ...
      ...
      ...
        ...
        <div class="nums">
    ```
    
    <br>-> HTML은 태그의 내용으로, 태그가 사용되는 포함 관계를 갖는다. 이러한 포함관계는 <b>들여쓰기</b>를 통해 파악한다.
    <br>-> id인 article이 class nums를 포함하고 있는 관계이므로 article을 이용해서 더 정확하게 nums를 찾을 수 있다.
    
    
    <img width="1091" alt="image" src="https://user-images.githubusercontent.com/83554018/158499260-a6b06a6f-73e3-4314-b662-91e813234871.png">
    
    ```html
    div#article div.class
    ```

    

  
  
  
  
  
  
  
  
  
  
  
  
