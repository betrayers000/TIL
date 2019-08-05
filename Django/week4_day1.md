# week4

## day1

### Django

#### 1. MTV(MODEL - TEMPLATE - VIEW)

- MVC랑 같은데 이름만 다르다.

#### 1.1 Model

- 데이터를 관리하는 영역 DB라고도 한다.

#### 1.2 Template

- 사용자가 보는 화면
- 웹에서는 HTML문서이다.
- templates 폴더안에 넣어주어야 한다.

#### 1.3 View

- 요청을 받아 Model과 Temlplate를 이용해서 응답 해준다.
- url을 받는 route와 그걸 실행하는 function이 있다.



> Django 명령어
>
> `python -m venv venv` : venv라고 하는 파이썬 가상환경을 만들어줘 
>
> `source venv/Scripts/activate` : venv 환경을 실행하겠다.
>
> `deactivate` : 위에서 실행한 환경을 종료한다.
>
> ctrl+shift+p, F1 : 검색
>
> `select interpreter` : 인터프리터 선택
>
> `python manage.py runserver` : 서버실행
>
> `django-admin startproject projectname .` : 프로젝트를 생성
>
> `django-admin startapp appname` : app을 생성



### 2. Files

#### 2.1 Project files

1. manage.py
   - 서버를 실행해주는 파일
   - 수정할 일 없습니다.

2. `__init__.py` 
   - 패키지로 인식하기 위한 파일

3. wsgi.py

   - 파이썬만의 서버와 통신 규칙 

   - 배포 전까지는 수정하지 않는다.

4. settings.py
   - setting을 저장하는 곳
   - 변수들을 저장하는 공간

5. urls.py
   - flask에서의 `@app.route` 와 비슷한 기능을 한다.

#### 2.2 App files

1. admin.py : 관리자 권한으로 실행

2. apps.py : app에 대한설정

3. models.py : 데이터 베이스와 관련

4. tests.py : 테스트 코드를 넣는곳

5. views.py : 중간관리



### 3. 구성

- 프로젝트 안에 특정 기능을 가진 app들을 만든다.



### 4. HTML에서 장고 문법

#### 4.1 반복문

```django
{% for ~ in ~ %}

{% endfor %}


{% for ~ in ~ %}

{% empty %}

{% endfor %}

for 돌릴 리스트가 비어있으면 {% empty %} 이하의 문장을 실행

{{forloop.counter}} for문이 돌아간 횟수를 나타냄
```



#### 4.2 조건문

```django
{% if~ %}

{% elif %}

{% else %}

{% endif %}
```

> 유저에 대한 정보를 가져오거나 저장하는건 파이썬내에서 처리하고 유저에게 다르게 보여주는 부분은 html에서 한다.