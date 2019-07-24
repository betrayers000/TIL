# python

## week2 day3

### 1. 변수

#### 1. 1 클래스 변수

- 클래스의 속성
- 클래스 선언 블록 최상단에 위치
- `Class.class_varibale` 과 같이 접근/할당한다.

#### 1.2 인스턴스 변수

- 인스턴스의 속성
- 메서드 정의에서 `self.` 로 접근/할당한다.
- 인스턴스가 생성된 이후 `instance.val` 로 접근한다.

> 인스턴스 => 클래스 => 전역 순서로 네임스페이스를 탐색한다. 
>
> 즉 인스턴스를 통해서 클래스 변수에도 접근가능하다.
>
> 하지만 클래스 변수는 클래스를 통해서 접근하기로 하자



### 2. 메서드

#### 2.1 인스턴스 메서드

- 우리가 가장많이 사용하게 될 메서드
- 인스턴스가 사용할 메서드
- 데코레이터가 없으면 자동으로 인스턴스 메서드가 된다.
- 첫번째 인자로 무조건 `self ` 를 받도록 하자

#### 2.2 클래스 메서드

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터를 사용
- 첫번째 인자로 무조건 `cls`를 받도록 한다.
- 인스턴스의 `self` 와 마찬가지로 `cls`를 통해서 접근한다.

#### 2.3 스태틱 메서드

- 클래스가 사용할 메서드
- `@staticmethod` 데코레이터를 사용한다.
- 인자 정의는 자유롭게 하며 어떠한 인자도 자동으로 넘어가지 않는다.
- 보통 클래스에 대한 설명을 프린트할때 이용고 한다



### 3. 상속

- 클래스에서 가장 큰 특징
- 부모 클래스의 모든 속성이 자식 클래스에게 상속된다.
- 코드재사용성을 높여준다
- `super()` 를 통해서 부모클래스에 접근할 수 있다.
- 자식클래스는 부모 클래스의 속성, 메서드 모두 사용할 수 있다.

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')

p1.greeting()
s1.greeting()
```



### 4. 오버라이딩

- 자식클래스에서 부모클래스의 함수를 수정해서 사용할 수 있다.
- 부모클래스의 메서드와 같은 이름의 메서드를 작성하면 된다.

```python
class Soldier(Person):
    def __init__(self, name, age, number, email, army_id):
        super().__init__(name, age, number, email)
        self.army_id = army_id
        
    def greeting(self):
        print(f"충성! 이병 {self.name}")
        
    def walk(self):
        print("성큼성큼")
        
        
s1 = Soldier('굳건이', 20, 123123, 'email@email.com', 1234556)
s1.greeting()
s1.walk()
```

> 인스턴스 -> 자식 클래스 -> 부모클래스 -> 전역



### 5. 다중상속

- 두개이상의 클래스를 상속받는경우 다중상속이 된다.
- 상속 순서에 따라 접근 방식이 달라진다.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Mom(Person):
    gene = 'XX'

class Dad(Person):
    gene = 'XY'

class Child(Dad, Mom):
    def swim(self):
    print('첨벙첨벙')

c.gene  
# 결과 : 'XY'
```

> 상속 순서가 빠른 부모 클래스로 먼저 접근한다.