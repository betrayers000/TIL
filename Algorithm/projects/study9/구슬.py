drum = ["######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]
command = ["#", "<", ">", "*"]

def solution(drum):
    board = [list(i) for i in drum]
    N = len(drum)
    ans = 0
    for k in range(N):
        start = [0, k]
        stack = []
        stack.append(start)
        while stack:
            i, j = stack.pop()
            cnt = 0
            moving = [[i + 1, j], [i, j + 1], [i, j - 1], [i + 1, j]]
            c_idx = command.index(board[i][j])
            if c_idx == 3:
                cnt += 1
            ni, nj = moving[c_idx]
            if ni == N:
                ans += 1
                break
            if 0 <= ni < N and 0 <= nj < N:
                stack.append([ni, nj])
            if cnt > 1:
                break
    return ans

print(solution(drum))
