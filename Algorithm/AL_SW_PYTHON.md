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