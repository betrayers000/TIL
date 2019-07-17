# python

## day3

### 함수

#### 1. 가변인자 리스트 

- `def my_func(*args):`를 사용해서 정의하게 되면 가변인자 리스트 튜플 형태로 받을 수있다.
- `my_func(1, 2, 3, 4, 5)` 했을 시에 결과 `(1, 2, 3, 4, 5)` 가 나온다.

#### 2. 키워드 인자 

- `def greeting(age = 0, name ="익명")`처럼 기본 값을 줄 수 있다.

- kwargs는  딕셔너리 형태로 반환한다

  ```python
  def my_func(**kwargs):
  
  return kwargs
  ```

- 딕셔너리 형태로 인수를 넣을 수도 있다.

```python
def user(username, password, password_con):
    if password == password_con:
        print(f"{username}님 가입되었습니다.")
    else :
        print("비밀번호가 일치하지 않습니다.")

my_account = {
    'username': '홍길동',
    'password': '1q2w3e4r',
    'password_con': '1q2w3e4r'
}

user(my_account) # 에러가 나온다 
user(**my_account) # **을 붙여야지 에러가 나오지 않는다
```
