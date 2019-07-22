# Python

## jupyter notebook

### 단축키

- `ctrl + enter` : 현재 구문 실행 후 자기 구문에 위치

- `shift + enter` : 현재 구문 실행 후 밑 구문으로 이동

- `alt + enter` : 현재 구문 실행하고 밑에 새로운 코드칸 생성

- `ctrl + d` : 삭제 (del키와 같음)

- `앞단에서 dd` : 코드줄 삭제

- `앞단에서 a` : 위로 코드줄 추가



## python 기본

### 1. 예약어

- 예약어는 변수명이나 함수명으로 사용불가 

- 예약어 종류

```
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

### 2. 주석 

- `#`: 한줄주석

- ```python
  """
  함수안에서여러줄 주석 다른경우에는 docstring으로 사용
  여러줄의 String 입력시 사용한다.
  """
  ```

### 3. 실수비교

- `==` 으로 비교할 수 없다.

```python
import math

math.isclose(a, b)
```

### 4. Bool형

- `False` :  0, 0.0, (), [], {}, '', None, 데이터가 없는경우

- `True` : 데이터가 있는 경우 

- `None` : Null 의 개념

- `is` : 를 이용한 비교는 메모리 주소까지 참조한다. python 특성상 -5 ~ 256까지는 동일한 id를 사용한다

  ```python
  5 is 5
  # 결과 True
  1000 is 1000
  # 결과 False 
  # 1000은 같은 주소(id)를 사용하지 않기 때문에 is로 비교시 다르다고 나온다.
  ```

### 5. 시퀀스형

- List, String, Tuple, Dict, Range가 존재한다.
- 인덱스를 통한 접근이 가능하다.



### 6. 오늘의 문제

```python
my_str = "Life is too short, you need python"
vowels = {"a", "e", "o", "u", "i"}

#내 답
# for i in vowels:
#     if i in my_str:
#         my_str = my_str.replace(i, "")
# print(my_str)

# 선생님 답
result = ""
for char in my_str:
    if char not in vowels:
        result += char
        
print(result)
```

> in, not in 활용! 