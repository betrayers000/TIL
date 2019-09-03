T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    max_price = prices[-1]
    profit = 0
    max_profit = 0

    for i in range(N, -1, -1):
        if prices[i]> max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]

    if profit > max_profit:
        max_profit = profit

    print('#{} {}'.format(tc, max_profit))
