# python

## 2주차

### day1

#### 1. 딕셔너리(dict) 추가 및 삭제

1. `pop(key, default)`: key가 딕셔너리에 있으면 제거하고 그 값을 반환하고 없으면 default반환

   - 일반적인 사용

   ```python
   my_dict = {'apple': '사과', 'banana': '바나나'}
   my_dict.pop('apple')
   print(my_dict)
   # pop을 사용하면 해당 값은 딕셔너리에서 삭제된다.
   # {'banana': '바나나'}
   ```

   - default 값 이용

   ```python
   my_dict.pop('멜론', '없음')
   # key 값이 없는 경우 '없음'을 반환한다.
   ```

2. `update()` : key, value를 추가한다. 기존에 key가 있을경우 덮어쓰기 한다.

   ```python
   my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
   my_dict.update(apple = '사과아아')
   my_dict['banana'] = "바나나나아"
   # update와 키값을 명시하고 값을 넣어주는 것과 같다.
   ```

3. 딕셔너리에서 내포(comprehension)

   - 리스트와 마찬가지로 딕셔너리에서도 내포가 사용가능하다.
   - 일반적인 사용

   ```python
   dusts_80 = {location: dust for location, dust in dusts.items() if dust > 80}
   ```

   - 내포에서 `if ~ else ~ ` 또한 사용가능하다.
   - `if`문을 이용해서 value 값을 지정해줄수 있다.

   ```python
   result = {key: ('매우나쁨' if value > 150 else '나쁨' if value > 80 else '보통')for key, value in dusts.items()}
   ```



#### 2. 세트(set) 추가 및 삭제

1. `add()` : 세트에 값을 추가한다. 중복값은 추가 할 수 없다.
2. `update()` : 여러가지 값을 추가한다. 반드시 iterable한 값을 넣어야 한다.
3. `remove()` : 값을 제거한다. 단 값을 제거시 값이 없을 경우 에러가 발생한다.
4. `discard()` : 값을 제거한다. 하지만 값이 없을 경우 에러가 발생하지 않는다.
5. `pop()` : 인자를 넣어줄 수 없다. 랜덤한 값을 제거한다.



#### 3. Module 과 Package

1. `import` :모듈을 활용하기 위해 해당 공간으로 모듈을 가져오기 위함

2. ` as ` 를 이용해서 해당 모듈의 이름을 내가 원하는 것으로 바꿔서 사용할 수 있다.

   ```python
   import random
   from bs4 import BeautifulSoup # 등의 사용도 가능하다.
   from myPacakge.math.formula import * 
   # formula 모듈에서 모든 변수와 함수를 가져온다는 뜻.
   # "*"을 사용시 해당 모듈내의 모든 변수와 함수를 가져온다.
   ```

2. 패키지
   - 점으로 구분된 모듈 이름을 써서 파이썬 모듈 이름 공간을 구조화하는 방법
   - 예를 들어 mPackage.math 는 mPackage 안에 math 모듈을 가르킨다.
   - 패키지로 취급 하기 위해서는 해당 폴더에 `__init__.py` 를 필요로 한다.

#### 4. 예외 처리

>  `try : ~ except : ~ ` 를 이용해서 오류가 발생했을 시에 분기 처리를 해줄 수 있다.

1. 기본 사용방법

   ```python
   try : 
       num = int(input())
       print(num)
   except ValueError:
       print("숫자를 입력하세요")
       
   # try 문 안에 실행할 코드를 넣어주고, 
   # except 문 안에는 에러가 발생시 나타날 코드를 입력해준다.
   ```

2. 중복 오류처리

   ```python
   try:
       num = input("100으로 나눌 값을 입력하세요 : ")
       print(100/int(num))
   except (ValueError, ZeroDivisionError):
       print("바보?")
       
   # 에러를 튜플형태로 넣어서 중복처리 할 수 있다.
   
   try:
       num = input("100으로 나눌 값을 입력하세요 : ")
       print(100/int(num))
   except Exception:
       print("뭔지 모르겠지만 잘못됨")
   except ValueError:
       print("숫자 넣어주세요")
   except ZeroDivisionError as e:
       print(f"{e}입니다. 0 넣지마세요")
       
   # except문을 중복 사용하여 에러 종류에 맞춤 코드를 작성할수있다.
   # 단 작성시에는 가장 작은 단위의 에러부터 위에서 작성해야 한다.
   # 위 코드의 Exception은 큰 단위로 모든 에러에 코드가 실행된다.
   # 에러명을 명시해주지 않아도 except 문이 실행된다.
   # `as e` 등을 사용해서 에러 값을 활용할수있다.
   ```

3. `else ` 의 사용

   - 에러가 발생되지 않았을 경우에 실행되는 코드!

   ```python
   try:
       numbers = [1, 2, 3]
       number = numbers[5]
   except IndexError:
       print("에러발생")
   else:
       print(number**2)
   
   # 여기에도 else를 사용할 수 있다. (for 에서도 사용하고 try에서도 사용가능하다..)
   # 에러가 발생되지 않았을 경우에만 실행된다. (for와 비슷 for는 break를 만나지 않을 시 실행)
   ```

4. `finally` 의 사용

   - 에러 유무와 상관없이 무조건 실행되는 코드 ! 

   ```python
   try:
       fruits = {
           "apple": "사과",
           "peach": "복숭아"
       }
       fruits["pineapple"]
   except KeyError as err:
       print(f"{err} 에러가 발생!!!")
   finally : 
       print("finally!!!!")
       
   # finally 코드는 에러 유무와 상관없이 무조건 실행된다.
   ```

5. `raise` 의 사용

   - 무조건 에러 발생시키기! 

   ```python
   raise
   # 코드가 실행중 위 코드와 만나면 무조건 에러를 발생시키고 정지한다
   ```

   