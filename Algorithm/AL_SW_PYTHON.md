# 알고리즘

## SW expert python 문제

### 숫자 카드 문제

```python
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    count = int(input())
    nums = list(str(input()).replace('\r',''))
    b = 0
    c = 0
    d = 0
    for num in nums:
        if c > nums.count(num):
            b = b
            c = c
        elif c == nums.count(num):
            if int(num) > int(b):
                b = num
        else :
            b = num
            c = nums.count(num)
    print(f"#{test_case} {b} {nums.count(b)}")
 
```

- `list.count(num) ` : 리스트 내용중 num 내용의 갯수를 반환한다.
- 다른방법 카운팅하면서 정렬해준다. 인덱스위치를 만들어서

```python
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = input()
    # 카드번호 인덱스를 만들어준다
    card = [0] * 10
    # 위의 카드번호 인덱스에 해당 카드번호의 카드개수를 합치면서 넣어준다.
    for i in range(0, N):
        v = int(num[i])
        card[v] = card[v]+1
    mxIdx = 0
    # 이미 정렬되어있기 때문에 같은값일 경우에는 카드숫자의 최대값을 가져온다.
    for i in range(0, 10):
        if card[mxIdx] <= card[i]:
            mxIdx = i
    print(f"#{t} {mxIdx} {card[mxIdx]}")
```

- 딕셔너리를 이용

```python
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))
    dic = {}
    for c in cards:
        if dic.get(c) == None:
            dic[c] = 1
        else :
            dic[c] = dic[c] +1
    mxidx = 0
    mxval = 0
    for idx, val in dic.items():
        if mxval < val:
            mxidx = idx
            mxval = val
        elif mxval == val:
            if mxidx < idx:
                mxidx = idx
                mxval = val
    print(f"#{t} {mxidx} {mxval}")
```

### 버스 정류장 문제

```python

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    k, n, m =[int(n) for n in input().strip().split(" ")]
    charges = [int(t) for t in input().strip().split(" ")]
    i = 0
    result = []
    for station in range(n):
        mv = [m for m in range(i+ 1, i+k+1) if m <= n]
        if n in mv :
            break
        cv = [c for c in charges if c in mv]
        if len(cv) > 0:
            i = cv[-1]
            result.append(i)
        else : 
            break
    if result[-1] < n-k:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} {len(result)}")
```

- 처음에 0에서 버스 이동칸을 구한다음에 정류장이 그 안에 있냐 없냐로 판단, 정류장이 있으면 가장 큰수의 정류장을 스타트 지점으로 다시 버스이동칸을 구한다. 이를 반복한다.