import sys

sys.stdin = open('input.txt', 'r')


def get_sum(x, history, total):
    global N
    global result
    global ans

    if x == N - 1:
        if ans > total:
            ans = total
        return 1
    for i in range(N):
        if i not in history:
            temp = board[x + 1][i]
            if total + temp < ans:
                history.append(i)
                total += board[x + 1][i]
                if get_sum(x + 1, history, total) == 1:
                    history.pop()
                    return
                else:
                    total -= board[x + 1][history.pop()]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]
    ans = 99
    for i in range(N):
        history = []
        history.append(i)
        total = board[0][i]
        get_sum(0, history, total)
    print(ans)