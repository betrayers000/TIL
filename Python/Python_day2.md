# Python

## Day2

### 1. 조건문

- 조건식과 함께 사용되어야 한다.
- 조건식이 참(True)인경우 `:` 이후 문장을 수행
- 조건식이 거짓(False)인경우 `else:` 이후 문장을 수행

### 2. 조건표현식

- `true_value if <조건식> else false_value` 의 형태
- 다른 언어의 삼항연산자와 동일하다.

### 3. 반복문 while

- while 조건식 의 구조로 만들어진다.
- 조건식이 False가 되는 식을 넣어주지 않으면 무한 반복된다.

### 4. 반복문 for

- dict

  - 파이썬에서만 존재하는 형태
  - 여러가지 함수가 존재한다.

  - `.keys()` : key값에 접근한다.

    ```python
    for key in dict.keys():
        print(key)
    # for key in dict:
    # 	print(key)
    # 위 형태는 같다.
    ```

  - `.values()`: value값에 접근한다.

    ```python
    for val in dict.values():
        print(val)
    ```

  - `.items()` : key값과 value 값에 둘다 접근한다 

    ```python
    for key, val in dict.items():
        print(key, val)
    ```

- enumerate

  - 인덱스 값과 value 값을 같이 튜플로 반환해준다.

  ```python
  names = ["kim", "oh", "park","jumg"]
  list(enumerate(names))
  
  # 결과 
  # [(0, 'kim'), (1, 'oh'), (2, 'park'), (3, 'jumg')]
  ```

- break

  - break와 만나면 반복을 끝낸다.

    ```python
    for i in range(1, 10):
        if i == 5:
            break
        print(i)
    print("끝")
    # 1
    # 2
    # 3
  # 4
    # 까지 프린트 되고, break를 만나 반복문을 종료시키고
    # 끝 
    # 을 프린트한다.
    ```
  
- continue

  - continue를 만나면 continue  하단의 코드를 실행하지 않고 바로 다음 반복으로 넘어간다

    ```python
    for i in range(1, 6):
        if i%2 == 0:
            print("짝수")
            continue
        print(i)
    # 1
    # 짝수
    # 3
  # 짝수
    # 5
    # if 조건을 만족시키고 continue와 만나면 print(i)를 실행하지 않고
    # 다음 반복으로 넘어간다
    ```
  
- for ~ else ~ 

  - for문이 성공적으로 실행되면(break를 만나지 않을 시) else 문이 실행된다.

    ```python
    nums = [1, 2, 3]
    for i in nums:
        if i == 4:
            print("True")
            break
    else :
        print("False")
    ```

    
