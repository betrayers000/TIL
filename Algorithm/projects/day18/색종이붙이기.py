import sys

sys.stdin = open('paper.txt', 'r')

board = [list(map(int, input().split())) for _ in range(10)]
size = [0, 0, 0, 0, 0, 0]

def check(i, j):
    idx = 0
    temp = []
    for q in range(5):
        if 0<= q+i < 10 and 0<= q+j < 10:
            temp.append(board[q+i][q+j])
    for w in range(len(temp)-1, -1, -1):
        if temp[w] == 1:
            idx = w+1
            break
    if idx == 0:
        return 0
    ni, nj = idx, idx
    total = 0
    for x in range(idx):
        for y in range(idx):
            total += board[i+x][j+y]
    if total == idx*idx:
        for x in range(idx):
            for y in range(idx):
                board[i+x][j+y] = 0
        size[idx] += 1
        return 1

    else:
        for z in range(1, idx):
            # if 0 <= i + z < 10 and 0 <= j + z < 10:
            if board[i][j+z] == 0:
                if nj == idx:
                    nj = z
            if board[i+z][j] == 0:
                if ni == idx:
                    ni = z
        if ni > nj:
            if check(i+1, j) == 1:
                return 1
        else:
            if check(i, j+1) == 1:
                return 1
    return 0


total_paper = 0
# search board
while True:
    board_total = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                total_paper += check(i, j)
                # check
            board_total += board[i][j]
    if board_total == 0:
        break
paper_check = True
print(size)
for c in size:
    if c > 5:
        paper_check = False
        break
if paper_check:
    print(total_paper)
else:
    print(-1)