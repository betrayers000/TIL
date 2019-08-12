# Algorithm

## day1

> 알고리즘 : 문제를 해결하는 순서
>
> 슈더코드 : 언어에 상관없이 문제를 해결할 수있는 코드



#### 1. 좋은 알고리즘이란

- 정확성 : 정확한 동작
- 작업량 : 적은 연산
- 메모리 사용량 : 적은 메모리
- 단순성 : 얼마나 단순, 누가봐도 이해가능한가
- 최적성 : 얼마나 최적화



#### 2. 시간복잡도

- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산



##### 2.1 빅-오[O] 표기법(Big-Oh)

- 최악의 경우 필요한 연산
- 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
- 최고차항만 남겨둔다.



### 3. sys.stdin

- 파이참에서 사용한다.
- 파이썬 파일과 입력 텍스트 파일의 위치가 동일해야한다.

```python
import sys
sys.stdin = open('input.txt', 'r')
```



#### 4. 정렬의 종류

- 버블 정렬
- 카운팅 정렬
- 선택 정렬
- 퀵 정렬
- 삽입 정렬
- 병합 정렬

> 버블이나 선택은 기본이다.
>
> 퀵을 많이 활용한다.



```python
N = int(input())
# 중간 index 구하기, 홀수일경우를 생각해서 0.5를 더해서 int를 줘서 뒤를 자른다
div = int(N/2 +0.5)-1
# 숫자를 받는다
nums = list(map(int, input().split()))
# 정렬된 숫자를 넣을 리스트를 만든다
sortnums = []
idx = 0
while len(sortnums) != N:
    mn = nums[0]
    # 최소값을 찾는다
    for n in nums:
        if n <= mn and not (n in sortnums):
            mn = n
    count = 0
    #해당 최소값으 개수를 찾는다
    for x in nums:
        if mn == x:
            count += 1
    # 최소값을 개수만큼 리스트에 추가한다
    for i in range(count):
        sortnums.append(mn)
print(sortnums[div])
```

- 버블 정렬

```python
N = int(input())
# 중간 index 구하기, 홀수일경우를 생각해서 0.5를 더해서 int를 줘서 뒤를 자른다
div = int(N/2 +0.5)-1
# 숫자를 받는다
nums = list(map(int, input().split()))
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if nums[j]>nums[j+1]:
            #temp = nums[j]
            #nums[j] = nums[j+1]
            #nums[j+1] = temp
            nums[j], nums[j+1] = nums[j+1], nums[j] # 파이썬만 가능
print(nums)
```

