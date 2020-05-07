# StartCamp

## Day5

### Python - Telegram 챗봇만들기 

#### 1. 환경변수

- python-decouple을 이용한 환경변수 설정
- .env 파일안에 환경변수를 정의한다.
- `config()` 함수를 이용하여 어디서든 꺼내 쓴다.

#### 2. Telegram api를 이용하여 메세지 보내기

```python
# 사용자의 input을 받는곳
@app.route("/write")
def write():
    return render_template("write.html")

# input받은 데이터를 telegram으로 전송
@app.route("/send")
def send():
    msg = request.args.get("msg")
    url = f"{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    return render_template("send.html")
```

#### 3. Telegram webhook을 이용하여 반응형 챗봇만들기

##### 3.1 webhook 등록하기

```python
import requests
from decouple import config

#환경변수를 불러온다
token = config("TELEGRAM_TOKEN")
user_id = config("CHAT_ID")

url = f"https://api.telegram.org/bot{token}/"
ngrok_url = "https://clustal.pythonanywhere.com"
webhook_url = f"{url}setWebhook?url={ngrok_url}/{token}"

print(webhook_url)
```

> `config()` 함수를 통해서 .env 파일에 등록된 환경변수를 가져온다



##### 3.2 반응형 챗봇을 위해 if문이용

- `methods=['POST']` : telegram 서버에 요청한다.
- 요청 받은 json정보를 dict 형태로 변환해주고 원하는 값을 찾는다.

```python
@app.route(f"/{token}", methods=['POST'])
def telegram():
    # json으로 들어오는 값을 dict 으로 변환해줌
    print(request.get_json())
    data = request.get_json()
    user_id = data.get("message").get("from").get("id")
    user_msg = data.get("message").get("text")
    
    if data.get("message").get("photo") is None:
        # user_msg에 따른 규칙
        if user_msg == "점심메뉴":
            menu_list = ["삼계탕", "철판낙지볶음밥", "물냉면"]
            result = random.choice(menu_list)
        elif user_msg == "로또":
            number_list = list(range(1, 46))
            result = sorted(random.sample(number_list, 6))
        elif user_msg == "환율":
            url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            select = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
            result = f'지금 1$는 {select.text}원 입니다.'

        elif "*" in list(user_msg):
            orlist = user_msg.split("*")
            ans = int(orlist[0]) * int(orlist[1])
            result = f"{ans} 입니다"
        elif "+" in list(user_msg):
            orlist = user_msg.split("+")
            ans = int(orlist[0]) + int(orlist[1])
            result = f"{ans} 입니다"
        elif "-" in list(user_msg):
            orlist = user_msg.split("-")
            ans = int(orlist[0]) - int(orlist[1])
            result = f"{ans} 입니다"
        elif "/" in list(user_msg):
            orlist = user_msg.split("/")
            ans = int(orlist[0]) / int(orlist[1])
            result = f"{ans} 입니다"
        
        elif user_msg[0:2] == "번역":
            raw_text = user_msg[3:]
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            data = {
                "source" : "ko",
                "target" : "en",
                "text" : raw_text
            }
            res = requests.post(papago_url, data=data, headers=header)
            translate_res = res.json()
            translate_result = translate_res.get("message").get("result").get("translatedText")
            result = translate_result

        elif user_msg[0:2] == "검색":
            raw_text = user_msg[3:]
            search_url = f"https://search.naver.com/search.naver?query={raw_text}"
            res = requests.get(search_url).text
            soup = BeautifulSoup(res, 'html.parser')
            select = soup.select("#nx_related_keywords > dl > dd.lst_relate._related_keyword_list > ul")
            result = f"{raw_text}의 연관검색어는 {select[0].text} 입니다!"
            
        else : 
            result = user_msg

    else :
        # 사용자가 보낸 사진을 찾는 과정 file_id를 통해 file_path를 얻어오고 file_path를 통해 file을 얻어온다
        result = "사진"
        file_id = data.get("message").get("photo")[-1].get("file_id")
        file_url = f"{api_url}/bot{token}/getFile?file_id={file_id}"
        file_res = requests.get(file_url)
        file_path = file_res.json().get("result").get("file_path")
        file = f"{api_url}/file/bot{token}/{file_path}"

        # 위에서 찾은 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clova_url = "https://openapi.naver.com/v1/vision/celebrity"
        clova_res = requests.post(clova_url, headers=header, files={'image':res.raw.read()})

        if clova_res.json().get("info").get("faceCount"):
            # 닮은 사람 출력
            celebrity = clova_res.json().get("faces")[0].get("celebrity")
            name = celebrity.get("value")
            confidence = celebrity.get("confidence")
            result = f"{name}와 {confidence*100}% 만큼 유사합니다"
        else :
            # 닮은 사람이 없는 경우
            result = "닮은 사람이 없습니다"

    res_url = f"{api_url}/bot{token}/sendMessage?chat_id={user_id}&text={result}"
    requests.get(res_url)
    return '', 200
```



#### 4. 기타 함수

- `str[0:3]` : 스트링의 첫번째(0)부터  세번째(2)까지 문자열 반환
- `val is val2` : val과 val2를 비교해서 같으면 True 다르면 False를 반환한다.
- `requests`의 옵션
  - `headers = header` : Api에서 요구하는 header값을 headers 명령어로 넘겨준다.
  - `files =` : Telegram에 파일을 보낼때 사용한다.
  - `data = data` : Api에 데이터를 보내기 위해서 사용한다.

