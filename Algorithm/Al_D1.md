# 알고리즘

> 하루에 최소 한문제씩

## D-1

### 홀수만 더하기

``` python
count = int(input())

for i in range(count):
    nlists = str(input())
    nlists = nlists.replace("\r", "").split(" ")
    listsum = 0

    for nlist in nlists:
        nlist = int(nlist)
        if nlist%2 != 0:
            listsum = listsum +nlist
            
    print(f"#{i+1} {listsum}")
```

### 평균값 구하기

```python
counts = int(input())

for count in range(counts):
    nlist = input()
    nlist = str(nlist).split(' ')
    listsum = 0
    for i in nlist:
        listsum = listsum+int(i)
    listsum = round(listsum/10)
    print("#%d %d" % (count+1, listsum))
```

> str을 넣어주는 곳을 split 실행줄에서 넣어주면 `\r`이 붙지 않는다.

### 큰놈작은놈

```python
count = int(input())
for i in range(count):
    nums = input()
    nums = str(nums).split(" ")
    if int(nums[0]) > int(nums[1]):
        print(f"#{i+1} >")
	
    elif int(nums[0]) < int(nums[1]):
        print(f"#{i+1} <")
        
    else:
        print(f"#{i+1} =")
```

###  최대수 구하기

``` python
T = int(input())
for t in range(1, T+1):
    nums = [int(n) for n in input().strip().split(" ")]
    nums_s = sorted(nums)
    print(f"#{t} {nums_s[-1]}")
```

- 받아서 sorted로 정렬시켜서 맨마지막 값 가져오기

### 중간값 구하기

```python
n = int(input())
scorelist = [int(s) for s in input().strip().split(" ")]
s_list = sorted(scorelist)
print(s_list[n//2])
```

- 받아서 정렬시키고 전체 길이를 2로 나눈 몫으로 인덱싱해서 찾아내면됨

###  자리수 더하기

```python
n = input()
total = 0
for num in n :
    total = total + int(num)
print(total)
```

### 연월일 달력

```python
T = int(input())
day30 = ["04", "06", "09", "11"]
day28 = ["02"]
day31 = ["01", "03", "05", "07", "08", "09", "10", "12"]
for test_case in range(1, T+1):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    if month in day30:
        if int(day) > 30:
            day = "-1"
    elif month in day28:
        if int(day) > 28:
            day = "-1"
    elif month in day31:
        if int(day) > 31:
            day = "-1"
    else:
        day = "-1"
    if day == "-1":
        print(f"#{test_case} {day}")
    else:
        print(f"#{test_case} {year}/{month}/{day}")
```

- 리스트를 이용해 일이 31, 30, 28일인 달을 저장하고 Spring slicing 을 이용해서 각 단을 자르고 월을 비교해서 해당 월일이 다르면 day =-1 을 저장하는 방식으로함

### 거꾸로 출력해 보아요

```python
def back_int(n) :
    if n == 0:
        print(0)
    else:
        print(n, end = " ")
        return back_int(n-1)
n = int(input())
back_int(n)
```

- 재귀 함수를 이용해서 0 일때는 그대로 출력하고 0이 아닐때는 n을 출력한뒤에 n-1을 인자로 자기 자신을 다시 불러온다. 마지막에 공간을 없애기 위해서 이런 방식을 사용함

