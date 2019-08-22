import sys

sys.stdin = open('input.txt', 'r')

def perm(per):
    global board
    length = len(per)
    if length == 1:
        return [per]
    else:
        result = []
        for i in per:
            b = per.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
        return result

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]
    board_list = list(range(1, N+1))
    ans = perm(board_list)
    total = 0
    min_total = 100
    for val in ans:
        total = 0
        for i in range(N):
            total += board[i][val[i]-1]
        if min_total > total:
            min_total = total
    print(ans)
    print(f"#{t} {min_total}")