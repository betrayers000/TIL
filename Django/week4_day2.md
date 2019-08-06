# django

## week4_day2

### 1.  Get

- `form action` 을 이용해서 html에서 데이터를 전송
- `views.py` 내의 함수내에서 받는다.
- `request.GET.get('')` 을 이용해서 받는다.

### 2. Post

- `form action method="POST"` 를 이용해서 전송한다.
- `{% csrf_token %}` 을 써줘야 한다. 해당 form이 장고서버에서 만들어졌는지를 검정한다.
- 받는 방법은 위와 동일하다.

### 3. static

- app 내에 static 폴더를 만들고 장고문법을 이용해서 접근한다.

- html에서 `{% static '경로' %}` 로 접근한다.
- css 파일이나 이미지파일등을 저장한다.
- 서버가 실행시 미리 로드하는 곳이다.

### 4. DataBase

- `python manage.py makemigrations`
- `python manage.py migrations`

- `models.py` 안에 정의 한다.
- 아래의 경우는 title과 content를 요소로 가지는 테이블 **Post**를 정의한다.

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
```

- `save()` 를 이용해서 저장한다. 저장시 `id` 가 할당된다.

```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    post = Post()
    post.title = title
    post.content = content
    post.save()
    return render(request, 'create.html')
```

- `Post(테이블명).objects.all()` 를 통해서 접근가능하다.

```python
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
```

```django
{% extends 'base.html' %}
{% block body %}
<h1>게시글 목록입니다</h1>
  {% for post in posts %}
    <p>{{post.title}} : {{post.content}}</p>
  {% endfor %}
{% endblock %}
```

