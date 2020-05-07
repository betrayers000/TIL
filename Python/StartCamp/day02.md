# StartCamp_Day_2

## Python day_2

### webbrowser 

> webbrowser를 조작
>
> 자주 사용하지는 않는다.

```python
import webbrowser

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
my_keywords = ["twice", "bts", "winner", "iu"]
for my_keyword in my_keywords:
    webbrowser.open(url + my_keyword)
```

### 웹 크롤링

> requests, bs4(BeautifulSoup)를 이용한 웹크롤링

```python
import requests
from bs4 import BeautifulSoup #bs4의 BeautifulSoup를 가져온다

response = requests.get("http://naver.com").text
soup = BeautifulSoup(response, "html.parser")

for i in range(1, 11):
    naver = soup.select_one(f"#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child({i}) > a.ah_a > span.ah_k")
    print(f"{i}위 : {naver.text}")

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
tr = soup.select("tbody > tr")

for r in tr:
    print(f"{r.select_one('.tit').text.strip()} : {r.select_one('.sale').text}")
    
#.select() - 리스트 생성
#.select_one - 리스트중 가장상위 값
```

### OS

> os를 조작할 수 있는 함수

```python
import os

os.chdir(r"C:\Users\student\StartCamp\students")
    
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG_", "SSAFY_"))
    #chdir() - 디렉토리 이동
    #listdir(".") - 디렉토리 내의 파일을 리스트화
    #rename(A,B) - 이름변경
```

### Faker

```python
from faker import Faker
import os

faker = Faker('ko_KR')
for i in range(100):
    filename = f"{i}_{faker.name()}.txt"
    cmd = f"touch {filename}"
    os.system(cmd)
    #faker - 거짓정보생성
    #system() - system으로 명령어를 보냄
```

### 텍스트 관련 함수

- `str.replace(A, B)` : str의 문자열중 A문자열을 B문자열로 바꾼다.

- `.strip()` : 문자 좌우의 공백을 모두 없앤다.

  

## CLI

> 명령어를 통해서 컴퓨터를 조작하는 프로그램 (Gitbash)
>
> 항상 어디서든 내 위치가 어디인지를 확인하는게 중요하다.

### 명령어

- `pwd` : 내 경로 확인
- `cd` : 디렉토리 이동 ( ./은 현재 디렉토리, ../은 상위디렉토리)
- `ls` : 현재 디렉토리의 파일 목록
- `touch` : 파일 생성
- `rm` : 파일 삭제
- `rm -r` : 디렉토리 삭제
- `mv` : 파일이동 및 이름 변경 (파일을 이름을 변경해서 이동한다고 생각)



## Git

> 소스관리 프로그램 이를 이용한 서비스로 대표적으로 Github가 있다.
>
> Gitbash를 이용하여 타이핑 명령어 사용

### 명령어

- `git init` : git을 시작한다. 폴더가 바뀌면 다시 해줘야한다. master를 띄운다.
- `git add` : git에 임시저장한다. 아직 서버로 올라가지않는다. 수정가능!
- `git commit -m ""` : 임시저장된 파일을 로컬에 최종 저장한다. 수정불가능!
- `git push origin master` : git 서버에 commit된 파일을 올린다.
- `git pull origin master` : git 서버에서 수정된 파일을 받아온다.
- `git clone ~ `: git 서버에서 파일을 통으로 가져온다.

### 기타

- .gitignore 파일 : git에 올릴 시 무시할 파일의 리스트 gitignore.io 에서 생성가능하다