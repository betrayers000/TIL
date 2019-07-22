# python

## day4

### 딕셔너리

- []를 통한 접근과 get ()을 통한 접근의 차이점은 []는 key가 없으면 에러가 발생되고, get은 None데이터를 리턴한다.

- get()을 자주 사용하는게 좀더 도움될수 있다. None으로 분기처리 할수있기 때문이다.



### 재귀함수

- 재귀함수는 끝이 있어야 한다.
- base_case 즉 점점 번위가 줄면서 반복되지 않는 최종적으로 도달하는 곳이다. 
- 아래 예시에서 base_case는 `if n <= 1: `부분이다 
- 파이썬의 경우 1000번까지만 지원한다.

```python
def factorial(n):
    if n <= 1:      #여기가 base_case
        return n
    else :
        return n * factorial(n-1)
factorial(5)
```

- `return n * factorial(n-1)`  에서 다시 자기자신을 호출한다.
- 호출 결과로 `return n * n-1 * n-2 * n-3 * ...` 이 된다.
- `n <= 1 `  를 만족하는 조건에서 n만 반환하면서 끝나게 된다.



> iterable : 순서가 있는 

### 리스트

#### 1. 리스트에 값 추가 

##### 1.1 원본을 넣는다

1. `.append` : 값 하나를 추가한다. 값으로 리스트를 추가하면 리스트 안에 리스트가 들어가있게됨

2. `.insert(index, val)` : 리스트의 index 위치에 val 값을 넣는다. 길이를 넘어선 index를 넣으면 맨 뒤로 붙는다

##### 1.2 확장개념

1. `.extend` : 리스트를 확장하는 개념이다. 하나의 리스트가 유지됨

2. `.concatenate` : extend와 동일하다.



#### 2. 리스트 값 삭제

1. `.remove(val)` : val 값을 찾아서 삭제해준다. 처음 값부터 삭제한다.

2. `.pop()` : 해당 값을 빼내서 return 해준다.



#### 3. 리스트 접근

1. `.index(val)` :  해당 val의 index 값을 리턴한다



#### 4. 정렬

1. `.sort()`  : 리턴 없이 원본데이터를 바꾼다. `reverse =  True` 를 이용하여 정렬 순서를 바꿀수 있다.

2. `.reverse()` 반대로 뒤집는다. 정렬이 아니다. 순서없이 그냥 현재 데이터에서 뒤집는다.



#### 5. 복사

##### 5.1 얕은 복사

- 리스트와 딕셔너리는 a = b 를 하면 같은 id를 가지게 된다.

```python
original_list = [1, 2, 3]
copy_list = original_list
print(id(original_list))
print(id(copy_list))
# 같은 id 값을 반환한다.
```

- mutable 한것과 immutable 한것의 차이점 복사를 하고 싶으면 다른 방법을 이용해야 한다.

```python
#첫번째 방법
a = [1, 2, 3]
b = a[:]

# 두번째 방법
a = [1, 2, 3]
b = list(a)

print(id(a))
print(id(b))
# 슬라이스를 이용해서 데이터를 긁어와서 b에 넣어주면 복사할 수 있다.
```

##### 5.2 깊은복사

- 중첩된 상황에서 사용한다

```python
a = [1, 2, [9, 10]]
b = list(a)

# 중첩상황에서는 복사할수 없다
# a의 [1, 2]는 같은 주소를 공유하지 않지만, [9,10]은 같은 주소를 공유하게 된다.
```

- `import copy` 를 해서 

- `copy.deepcopy()` 를 사용해서 copy해야 한다

```python
import copy
a = [1, 2, [9, 10]]
b = copy.deepcopy(a)
```

