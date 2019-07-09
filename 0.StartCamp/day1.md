# Start Camp day 1 
## python step 1
### 저장
```python
numb = 10
string = "문자열"
t_boolean = True 
f_boolean = False
```
> True or False 맨 앞에 대문자



### 조건

```python
if (True or 조건문):
    print("if 조건이 True일 경우 수행합니다")
elif(상동):
    print("상동")
else:
    print("위의 조건이 전부 False일 경우 수행합니다")
```

> if ~ elif ~ elif ~ else
>
> 파이썬에서는 `80 < dust < 150` 의 문법이 가능하다! `dust > 80 and dust < 150` 과 같다.



### 반복

```python
n = 0
while(n < 3):
    print("위의 조건이 참일 경우 수행")
    n = n+1 #종료조건
```

> while은 종료조건을 넣어주어야 한다. 그렇지 않으면 무한반복한다.

```python
for i in range(3):
    print(i)
```

> for는 횟수가 정해진 반복문 종료조건이 필요없다.



### 리스트, 딕셔너리

```python
numbers = [1,2,3,4]
dic = {
    "첫번째":1, "두번째":2
}
print(numbers[1])
print(dic["첫번째"])
```

>리스트는 [] 를 사용한다.
>
>딕셔너리 {} 를 사용한다. key - value 의 관계를 갖는다.
>
>딕셔너리를 불러올때는 []를 사용한다.



### 함수

+ 내장함수(기본함수)
  
```python
  print("내장함수 print입니다")
```

+ 외장함수(불러와서 사용하는 함수)
  
  ```python
  import random
  
  #range()를 이용해 numbers에 1~45까지 숫자를 담는다.
  numbers = list(range(1, 46))
  #random.sample을 이용해 numbers에서 6개의 숫자를 비복원추출한다.
  pick = random.sample(numbers, 6)
  print(numbers)
  print(sorted(pick))
  ```
  
  >외장함수는 `import random` 처럼 불러오는 과정이 필요하다.



### 오늘 사용한 함수

- random
  - `.choice(리스트)` : 리스트 내용중 랜덤하게 하나 선택
  - `.sample(리스트, n)` : 리스트의 내용중 n개 만큼 비복원추출(중복없이)

 

