# StartCamp

## Day3

### Python

1. CSV 

   - csv란 ? 쉼표를 기준으로 문자열을 나눈다. 엑셀등에서 열수 있고 데이터 편집이 편하다

   > csv 형태로 저장하기

   ```python
   import csv
   
   lunch = {
       "BBQ" : "062-423-4561",
       "교촌" : "062-756-4562",
       "굽네" : "062-523-7789"
   }
   # with open() as f : > 해당 단락이 끝날때까지 open()를 f로 쓰겠다
   # f.close()를 하지않아도 됨 
   with open("lunch.csv", 'w', encoding="utf-8", newline="") as f :
       csv_writer = csv.writer(f)
       
       for item in lunch.items():
           csv_writer.writerow(item)
   ```

   

   ```python
   import csv
   import requests
   from bs4 import BeautifulSoup
   
    url = "https://www.bithumb.com/"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    tr = soup.select("#tableAsset > tbody > tr")
    with open("bit_coin.csv", 'w', encoding = 'utf-8', newline = "") as f:
        csv_writer = csv.writer(f)
        for r in tr :
            print(r.select_one('.blind').text)
            print(r.select_one('.sort_real').text)
            row = [r.select_one('.blind').text.strip(), r.select_one('.sort_real').text]
            csv_writer.writerow(row)
   ```



### HTML

- 웹페이지 작성시 사용하는 언어

- **<태그이름 속성명="속성값" 속성명2="속성값2">내용</태그이름>** 가 기본 형태
- 태그 안에 태그를 넣을 수 있다.

```python
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="./intro.css">
    </head>
    <body>        
        <h1>HTML</h1>
        <h1 class="blue">CSS</h1>
        <h2 class="blue">HyperText Markup Language</h2>
        <a href="https://naver.com">네이버</a>
        
        <h3>우리가 공부한것</h3>
        <ol>
            <li><strong><i>파이썬</i></strong></li>
            <li class="blue">HTML</li>
            <li id="git" class="blue">Git</li>
        </ol>
    </body>
</html>
```

### CSS

- HTML 문서에 색을 입혀준다.
- HTML의 `<link rel="stylesheet" href="./intro.css">`를 이용하여 연결 할 수 있다.

```css
/* 
원하는 태그에 원하는 CSS 적인 요소를 적용시킬수있다
h1 {

}
. > class
# > id
id > class > 태그 순으로 우선순위를 가진다 */
h1 {
    background-color: red;
}   
a {
    color: brown;
}
.blue {
    background-color: blue;
}
#git {
    background-color: black;
}
```



