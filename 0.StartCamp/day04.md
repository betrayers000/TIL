# StartCamp

# Day4

### 1. python - flask

> 나만의 웹페이지를 만들어보자! 

- flask를 이용해서 서버 생성 및 실행

  ```python
  from flask import Flask, render_template, request
  app = Flask(__name__)
  
  if __name__ == '__main__':
      app.run(debug=True)
  ```

- `app.route("/")` 안의 경로로 웹페이지 생성 및 html 태그 적용

  ```python
  @app.route("/html_tags")
  def html_tags():
      return """
      <h1>안녕하세요</h1>
      <h2>반갑습니다</h2>
      """
  ```

- 하지만 비효율적이기 때문에 `render_template`를 이용해서 html문서로 직접 연결함 

- 이때 폴더이름을 templates로 만들어야 한다!

  ```python
  @app.route("/html_file")
  def html_file():
      return render_template('index.html')
  ```

- 웹페이지 마다 routing 해주기 힘들기 때문에 variable routing을 이용해서 동적 페이지를 만든다.

- `<int:num>` 을 이용해서 웹페이지를 통해서 파라미터를 받아온다. 

- url 뒤에 ? 뒤쪽에 파라미터 값이 들어간다.

  > https://search.naver.com/search.naver?query=twice
  >
  > 위의 경우에 query 가 파라미터 이다.

  ```python
  @app.route("/cube/<int:num>")
  def cube(num):
      result = num**3
      return f"{num}의 세제곱은 {result}입니다."
  ```

- Ginja 언어를 이용해서 HTML문서에서 if문과 for문 사용하기

  ```python
  #html에서 if문사용
  @app.route("/greeting_html/<string:name>")
  def greeting_html(name):
      return render_template("greeting.html", name=name)
  
  #html에서 for문사용
  @app.route("/movies")
  def movies():
      movie_list = ['스파이더맨', '존윅', '토이스토리', '라이온킹']
      return render_template("movies.html", movie_list=movie_list)
  ```

  ```html
  <body>
      {% if name == "정우" %}
      <p style="color:rgb(35, 87, 184)">{{name}}</p>야 안녕!!
      {% else %}
      <p style="color:rgb(100, 226, 68)">{{name}}</p>님 안녕하세요!!
      {% endif %}
      
      <ol>
          {% for movie in movie_list %}
              <li>{{movie}}</li>
          {% endfor %}
      </ol>
  </body>
  ```

- HTML과 python 사이에서 데이터를 주고 받기위해 form 을 사용한다

- `request.args.get()`을 이용해서 데이터를 요청한다

  ```python
  #form 사용한 데이터 주고받기 --------------------------
  @app.route("/ping")
  def ping():
      return render_template("ping.html")
  
  @app.route("/pong")
  def pong():
      user_input = request.args.get("test")
      #args = arguments = 매개변수들
      return render_template("pong.html", user_input=user_input)
  #---------------------------------------------------
  ```

- HTML에서 input을 이용해서 사용자가 입력한 값을 보내줄 수있다.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Ping</title>
    </head>
    <body>
        <h1>여기는 핑입니다.</h1>
        <form action="/pong">
            <input type="text" name="test">
            <input type="submit">
        </form>
    </body>
    </html>
    ```


- `render_template` 를 이용해서 HTML로 값을 보내준다.

- 받은 값은 {{}}를 사용하여 사용할 수 있다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Pong</title>
  </head>
  <body>
      <h1>여기는 퐁입니다.</h1>
      사용자가 방금 입력한 데이터는 
      <p>{{user_input}}입니다</p>
  </body>
  </html>
  ```



### 2. Python Dict 활용

#### 활용 함수

1. `.json()` : json 형태를 dict 형태로 변환

2. `set()` : set 형태로 변환

   > set 형식이란 집합형식이다. 교집합 합집합이 가능하다.

3. `set1 & set2` : set1 과 set2의 교집합을 구한다.
4. `var in vars` : vars 안에 var이 있는지 없는지에 대한 여부를 반환

```python
@app.route('/lotto')
def lotto():
    return render_template("lotto.html")

@app.route("/lotto_result")
def lotto_result():
    # 사용자가 입력한 정보를 가져오기
    numbers = request.args.get("numbers").split()
    user_numbers = []
    for n in numbers:
        user_numbers.append(int(n))
    
    #로또 홈페이지에서 정보를 가져오기
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    #json 데이터를 dict 형태로 변환해주낟
    lotto_numbers = res.json()
    
    
    winning_numbers = []
    for i in range(1, 7):
        winning_numbers.append(lotto_numbers[f'drwtNo{i}'])

    bonus_number = [lotto_numbers["bnusNo"]]

    result = "꽝"
    
    matched = len(set(user_numbers) & set(winning_numbers))
    secondmatched = len(set(user_numbers) & set(bonus_number))

    if matched == 6:
        result = "1등"
    elif matched == 5 :
        result = "3등"
        if secondmatched == 1: # bonus_number in user_numbers:
            result = "2등"
    elif matched == 4:
        result = "4등"
    elif matched == 3:
        result == "5등"
    else:
        result = "꽝"

    return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, r=result, b=bonus_number)
```

