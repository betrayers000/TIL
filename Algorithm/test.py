def checkprice(price):
    total = 0
    while price != []:
        midx = price.index(max(price))
        md = price.pop(midx)
        for i in range(midx-1, -1, -1):
            total = total + (md - price.pop(i))
    return total


T = int(input())
for test_case in range(1, T+1):
    days = int(input())
    price = list(map(int, input().split()))
    if not(2 <= days <= 1000000):
        continue
    total = checkprice(price)
    print(f"#{test_case} {total}")
