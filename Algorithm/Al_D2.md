# D2

### 어디에 단어가 들어갈 수 있을까

```python
def checkline(line, n):
    total = 0 
    total_cnt = 0
    par = []
    # total_cnt : 1이 n개만큼 연속된 값이 몇개인지 확인
    # total : 1이 몇개가 있는지를 확인
    # par : 1의 연속성을 확인
    # enumerate()를 이용해서 idx와 val를 같이 얻는다 par과 함께 연속성확인
    for idx, val in enumerate(line): 
        if val == 1:
            # 값이 1인경우를 정한다.
            if idx == len(line)-1:
                # idx 값이 마지막인경우 확인한다.
                if total == n-1:
                    # 마지막값이 1일경우 total 값이 n-1 이면 n개만큼 연속성이 되므로
                    # total_cnt 에 1을 더해준다.
                    # 나머지 total, par을 초기화해준다( 안해도 됨)
                    total_cnt = total_cnt +1
                else :
                    # 위의 경우가 아닌경우 n개 만큼 연속을 확보할수 없기 때문에
                    # total_cnt를 더하지않아도 된다.
                    pass
            # 마지막이 아닌경우 par에 idx값을 넣는다.
            par.append(idx)
            if len(par) == 1:
                # par의 값이 1인경우 즉 최초의 1이 들어온경우 total 에 1을 넣어준다
                total = 1
            elif len(par) > 1:
                # par 값이 1 이상인경우 맨 뒤의 값과 그 앞의 값을 비교해서 
                # idx값이 연속성적인 숫자면 total에 +1을 해준다.
                # 맨뒤와 그앞값만 비교하면 계속된 연속성을 확인할 수 있다.
                if par[-1] == par[-2]+1:
                    total = total + 1
        else:
            # val 이 0인경우 초기화를 해줘야한다.
            if total == n:
                # total 이 n인 경우 n개만큼 연속됨을 만족했기 때문에
                # total_cnt에 total_cnt +1 을 해준다.
                total = 0
                par = []
                total_cnt = total_cnt + 1
            else :
                total = 0
                par = []
    return total_cnt # 마지막에 total_cnt를 리턴한다.
             
     
T = int(input())
for t in range(1, T+1):
    n = [int(n) for n in input().split()]
    lines = []
    total = 0
    for c in range(n[0]):
        line = [int(l) for l in input().split()]
        if n[1] <= line.count(1):
            # line 리스트를 확인해서 1이 n개 이상인경우에만 체크를 한다.
            check = checkline(line, n[1])
            total = total + check
        lines.append(line) 
        # 체크 유무와 상관없이 전부 lines 리스트에 추가해준다 다음에서
        # 세로리스트를 만들기 위해서다.
    for a in range(n[0]):
        # n[0] 만큼 반복을 한다. 왜냐면 n[0]값만큼이 세로 길이이기 때문
        result = [ls[a] for ls in lines]
        # 길이만큼 반복하면서 위에서 만들어진 lines의 값을 하나씩 꺼내온다.
        if n[1] <= result.count(1):
            # 위와 동일하게 체크해준다.
            check_2 = checkline(result, n[1])
            total = total + check_2
    print(f"#{t} {total}")
```

### 파스칼의 삼각형

```python
# line을 받아서 다음 line을 만들어주는 함수
def makeline(line):
    linelen = len(line)
    # 들어온 리스트의 길이를 뽑는다.
    if linelen == 1:
        # 길이가 1인경우 즉 [1]이 들어온경우 [1, 1]를 리턴하면 된다.
        return [1, 1]
    else : 
        # 위의 경우가 아닌경우
        # 즉 [1,1] 이상이 들어온 경우이다.
        result = []
        for i in range(linelen):
           # 들어온 리스트 만큼 반복해준다. [1, 1] 이면 두번반복한다.
            if not result :
                # 첫반복에는 무조건 1을 넣어준다
                result.append(1)
            else :
                # 두번째 반복부터는 이작업을 해준다.
                result.append(line[i] + line[i-1])
        # 마지막에 무조건 1을 넣어준다.
        # 들어온 리스트 만큼만 반복되기때문에 마지막에 1을 추가해주지않으면
        # 같은 길이의 리스트가 반환된다.
        result.append(1)
    return result
        


T = int(input())
for t in range(1, T+1):
    print(f"#{t}")
    cnt = int(input())
    line = [1]
    for c in range(cnt):
        print(" ".join(map(str, line)))
        line = makeline(line)
```

###  파리잡기

```python
T = int(input())
for t in range(1, T+1):
    data = [int(i) for i in input().split()]
    n = data[0]
    m = data[1]
    areas = {}
    for cnt in range(n):
        # 한변의 크기가 n임을 이용해서 n만큼 반복을 돌린다.
        area = [int(l) for l in input().split()]
        area_dict = {(cnt, c) : area[c] for c in range(n)}
        # 일단 한줄한줄 만들어주고 
        # 해당줄에 번호를 붙여가면서 딕셔너리 형태로 뽑아준다.
        # ex > (0, 0) : 16 이런형태로 값의 좌표값을 얻어온다.
        areas.update(area_dict)
        # 위에서 얻은 딕셔너리를 하나의 딕셔너리로 합친다.

    result = []
    # 합계를 넣을 result를 초기화 한다.
    for x in range(n - m+1):
        for y in range(n - m+1):
            # 위에서 만들어진 areas의 x,y 를 m만큼의 영역으로 가져오기위함
            # n 이 한변의 길이이고 m이 파리채의 길이이기 때문에 n-m+1만큼 반복해준다.
            # ex > n = 5, m =3 x가 1,2,3 순으로 
            plus = 0
            for m1 in range(m):
                x1 = x+m1
                for m2 in range(m):
                    y1 = y+m2
                    plus = plus + areas[x1,y1]
            result.append(plus)

    print(f"#{t} {max(result)}")
```

#### 파리잡기 좋은정답

- 2차 배열을 이용한 풀이

```python
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())        # N, M 받아
    board = []
    for row in range(N):
        board.append(list(map(int, input().split())))
 
    col, row, result = 0, 0, 0
    for row in range(N-M+1):          # col = 0, 1, ... N-M 까지
        for col in range(N-M+1):      # row = 0, 1, ... N-M 까지
            temp = 0
            for r in range(M):      # 파리채 크기만큼만 움직여
                for c in range(M) :
                    temp += board[row+r][col+c]
            if result < temp :
                result = temp
    print(f"#{t} {result}")
```





### 3, 6, 9 게임

```python
N = int(input())
numbers = list(map(str, range(1, N+1)))
# string 형태로 받아서 인덱싱을 이용해서 비교해서 걸러낸다.
tsn = ["3", "6", "9"]
result = []
for num in numbers:
    total = 0
    # 겹치는 갯수
    for n in num:
        # 숫자를 한글자씩 쪼개서 비교한다
        # 비교해서 3, 6, 9가 있으면 total 을 하나씩 올린다.
        if n in tsn:
            total = total +1
    
    # 숫자 한개를 끝낸후 total 갯수를 보고 1개 이상이면 -를 써주고
    # 아니면 기존 숫자를 넣는다.
    if total >= 1:
        result.append("-"*total)
    else:
        result.append(num)
print(" ".join(result))

```



### 백만장자 프로젝트

```python
T = int(input())
for test_case in range(1, T+1):
    days = int(input())
    price = list(map(int,input().split()))
    result = []
    # dell 함수를 이용해서 리스트 삭제를 하면서 이득을 계산한다.
    # 반복의 끝은 리스트의 모든 값이 지워질때까지 돌린다.
    # 처음에 pop을 사용하려고 했지만 반복문이 하나 더들어가기 때문에 시간오버가 나온다.
    while price != []:
        midx = price.index(max(price))
        # max 값을 찾고 해당 인덱스 값을 찾는다.
        if midx == 0:
            # 만약 midx가 0이라면 해당값을 리스트에서 지우고 다시 반복한다.
            del price[midx]
            continue
        profit =price[midx]*(midx)- sum(price[0:midx])
        # midx가 0이 아니라면 midx 값에 midx 인덱스만큼 곱한 값에서 midx 전 값까지
        # 전부 더한값을 빼주면 이득이 나온다.
        result.append(profit)
        del price[0:midx+1]
        # 처음부터 midx까지 값을 리스트에서 삭제한다. 새로운 리스트가 되어 반복한다.
    print(f"#{test_case} {sum(result)}")
```

- 처음 사용한 코드는 `pop`을 이용해서 했기때문에 pop을 위해서 for를 한번더 돌려야 했다. 그래서 시간 오버가 나왔다.
- `del`을 이용하게 되면 index를 통해서 한번에 여러값을 지울수 있기때문에 추가적인 반복문 사용이 필요없기 때문에 한번의 반복으로 완료 할 수 있었다. 

#### 백만장자 정답코드중 가장 빠른 코드

```python
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    sum, max = 0, 0
    for i in range(N):
        a = data[- 1 - i]
        # 맨뒤에서 부터 비교를 했다.
        # 맨뒤에서부터 앞으로 가면서 비교를 하면 맨 뒤값이 어째든 최고값이 되어야
        # 계산이 되기 때문에 효율적
        if (a > max):
            max = a
        sum += max - a
        # 해당값이 max보다 크면 max값을 해당값으로 바꾼다.
        # 그리고 max에서 a를 빼준값을 더하면서 진행
    print("#{} {}".format(test_case + 1, sum))
```

