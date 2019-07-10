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

