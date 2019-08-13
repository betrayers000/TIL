T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = list(map(int,input().split()))
    sumlist = []
    for i in range(n - m + 1):
        maxnum = 0
        for c in range(m):
            maxnum = maxnum + numbers[i+c]
        sumlist.append(maxnum)
    print(f"#{test_case} {max(sumlist) - min(sumlist)}")