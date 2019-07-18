# 알고리즘

## 부분집합

### 비트 연산자를 이용해서 부분집합 전체 구하기

``` python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
            print(arr[j], end=",")
    print()
```

- 원리는 원소의 개수만큼 이진법 칸을 만들고 0이면 빠지고 1이면 해당항목의 숫자가 들어가는 형식
- `range(1<<n)` 부분 집합의 개수 2^n을 나타낸다.
- `for j in range(n)` 원소의 수만큼 비트를 비교한다
- `if i&(1<<j)` i의 j번째 비트가 1이면 j번째 원소를 출력한다.
- 

### 부분집합 합

```python
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    info = [int(a) for a in input().split()]
    n = len(A)
    result = []
    for i in range(1<<n):
        presult = []
        for j in range(n):
            if i&(1<<j):
                presult.append(A[j])
        result.append(presult)
    lis = [l for l in result if len(l) == info[0] if sum(l) == info[1]]
    print(f"#{test_case} {len(lis)}")
```

