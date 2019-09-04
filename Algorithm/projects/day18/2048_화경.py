import sys

sys.stdin = open('2048.txt', 'r')

def game(lists):
    result = []
    global N
    temp = []
    for i in range(len(lists)):
        a = list(lists[i])
        compare = -1
        res = []
        for j in range(len(lists)):
            if a[j] == 0:
                pass
            elif compare == -1:
                compare = a[j]
            elif compare == a[j]:
                res.append(int(compare)*2)
                compare = -1
            elif compare != a[j]:
                res.append(compare)
                compare = a[j]
        if compare != -1:
            res.append(compare)
        temp.append(res)
    return temp
for tc in range(int(input())):
    N,C = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    if C == 'up':
        row = list(zip(*board))
        result = game(row)
        for k in range(N):
            if len(result[k]) != N:
                result[k].extend(['0'] * (N - len(result[k])))
            for j in range(N):
                result[k][j] = str(result[k][j])
        final = list(zip(*result))
    elif C == 'down':
        row = list(zip(*board))
        result = []
        temp = []
        for i in range(len(row)):
            a = list(row[i])[::-1]
            compare = -1
            res = []
            for j in range(len(row)):
                if a[j] == 0:
                    pass
                elif compare == -1:
                    compare = a[j]
                elif compare == a[j]:
                    res.append(int(compare) * 2)
                    compare = -1
                elif compare != a[j]:
                    res.append(compare)
                    compare = a[j]
            if compare != -1:
                res.append(compare)
            temp.append(res)
        for k in range(N):
            if len(temp[k]) != N:
                temp[k] = temp[k][::-1]
                temp[k] = ['0'] * (N - len(temp[k])) + temp[k]
            for j in range(N):
                temp[k][j] = str(temp[k][j])
        final = list(zip(*temp))
    elif C == 'right':
        temp = []
        for i in range(len(board)):
            a = list(board[i])
            compare = -1
            res = []
            for j in range(len(board)):
                if a[j] == 0:
                    pass
                elif compare == -1:
                    compare = a[j]
                elif compare == a[j]:
                    res.append(int(compare) * 2)
                    compare = -1
                elif compare != a[j]:
                    res.append(compare)
                    compare = a[j]
            if compare != -1:
                res.append(compare)
            temp.append(res)
        print(temp)
        # for k in range(N):
        #     if len(temp[k]) != N:
        #         temp[k] = ['0'] * (N - len(temp[k])) + temp[k]
        #     for j in range(N):
        #         temp[k][j] = str(temp[k][j])
        final = temp
    else:
        result = game(board)
        for k in range(N):
            if len(result[k]) != N:
                result[k].extend(['0'] * (N - len(result[k])))
            for j in range(N):
                result[k][j] = str(result[k][j])
        final = result
    print('#{}'.format(tc+1))
    for fin in final:
        print(' '.join(fin))