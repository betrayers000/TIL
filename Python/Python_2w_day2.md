# python

### map(), zip(), filter()

#### 1. map()

- `map(function, iterable)` 의 형태로 사용

- iterable의 원소를 function을 적용한 후 그 결과를 돌려준다.

- return 하면 map_object로 반환된다.

  ```python
  def cube(n):
      return n**3
  
  numbers = [1, 2,3 ,4 ,5, 6]
  list(map(cube, numbers))
  
  # 결과
  # [1, 8, 27, 64, 125, 216]
  ```

#### 2. zip()

- `zip(*iterables)` 의 형태로 사용

- 복수 iterable한 것들을 모아준다.

- 결과는 튜플의 모듬으로 구성된 zip object를 반환한다.

  ```python
  girls = ['jane', 'iu', 'mary']
  boys = ['justin', 'david', 'kim']
  print(list(zip(girls,boys)))
  # 결과
  # [('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]
  ```

#### 3. filter()

- `filter(function, iterable)` 의 형태로 사용한다.

- `map()`과 다르게 조건에 맞는 값만 반환한다.

  ```python
  def even(n):
      return not n%2
  
  even(5)
  
  numbers = [1, 2, 3, 4, 5]
  list(filter(even, numbers))
  
  # 결과
  # [2, 4]
  ```



### OOP (Object-Oriented Programming)

> - 객체 지향 프로그래밍
>
> - 여러개의 독립된 단위 즉 'Object' 들의 모임으로 하나의 프로그램을 만드는 것
>
> - 클래스 내부 attribute나 Method에 접근하기 위해 `.` 을 사용해서 접근한다.

#### 1. 기본 구성요소

1. Class 

   - attribute와 method를 갖는다.
   - 정의하는 것

2. instance

   - Class가 실제 메모리상에 할당된 것
   - 선언하는 것
   - 실체화 한 것

3. attribute 

   - Class가 가지는 속성 = 값
   - 접근시에 괄호가 없다.

4. Method  

   - Class가 가지는 행위 = 함수

   - 접근시에 괄호가 있다.

   - 객체의 변화를 줄 수 있다.

     ```python
     my_list = [5, 6, 7, 8, 9, 1, 2, 3]
     print(type(my_list))
     
     # List.sort()를 사용해서 List 값이 직접적으로 변한다.
     # List class의 Method를 함수
     my_list.sort()
     print(my_list)
     ```

#### 2. 클래스 및 인스턴스

1. 클래스 생성

   ```python
   class TestClass:
       """
       이것은 테스트 클래스입니다.
       """
       name = 'TestClass'
   ```

2. 인스턴스 생성

   ```python
   tc = TestClass()
   ```

3. `__init__` : 생성자

   - 생성자는 인스턴스 객체가 생성될 때 호출되는 함수이다.
   - 생성자 또한 함수이기 때문에 추가인자를 받을 수있다.
   - 보통 생성자를 통해서 인스턴스 변수에 값을 넣는다.

   ```python
   class Pikachu:
   
       def __init__(self, name):
           self.name = name
           self.level = 5
           self.hp = self.level*20
           self.exp = 0
   ```

4. `__del__` : 소멸자

   - 소멸자는 객체가 소멸되는 과정에서 호출 되는 함수이다.

5. `self` 

   - 객체 자기자신을 뜻한다.
   - 클래스의 모든 메서드는 self를 첫번째 인자로 설정한다.