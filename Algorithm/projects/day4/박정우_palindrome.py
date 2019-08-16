def check_pal(line, N, M):
    for i in range(N - M + 1):
        word = line[i:i + M]
        if word == word[::-1]:
            return True, word
    return False, word


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for n in range(N)]
    board_ = []
    for i in range(N):
        temp = ""
        for b in board:
            temp += b[i]
        board_.append(temp)
    for line in board:
        check, word = check_pal(line, N, M)
        if check:
            result = word
            break
    for line_ in board_:
        check, word = check_pal(line_, N, M)
        if check:
            result = word
            break
    print(f"#{t} {result}")