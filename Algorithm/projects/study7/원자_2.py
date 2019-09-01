import sys

sys.stdin = open('atom.txt', 'r')


def check(temp):
    global history
    temp = sorted(temp, key=lambda x: x[4])
    total = 0
    check = False
    if len(temp) < 2 or temp[0][:4] in history:
        return total
    else:
        start = temp[1][4]
        for i in temp:
            if i[:4] in history or i[4] == 0:
                continue
            if i[4] == start:
                total += i[3]
                history.append(i[:4])
                check = True
            else:
                break
        if check:
            total += temp[0][3]
            history.append(temp[0][:4])
    return total


T = int(input())
for t in range(1, 1+T):
    N = int(input())
    history = []
    atoms = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N - 1):
        temp = [atoms[i] + [0]]
        x, y, d, e = atoms[i]
        for j in range(i + 1, N):
            nx, ny, nd, ne = atoms[j]
            dx = atoms[i][0] - atoms[j][0]  # x 값이 같을때
            dy = atoms[i][1] - atoms[j][1]  # y 값이 동일할때
            if dx == 0:
                temp.append(atoms[j] + [abs(ny - y) / 2])
            elif dy == 0:
                temp.append(atoms[j] + [abs(nx - x) / 2])
            elif dx == dy:
                if dx < 0 :
                    if (d == 3 and nd == 1) or (d == 0 and nd == 2):
                        temp.append(atoms[j] + [abs(ny - nx)])
                else:
                    if (d == 2 and nd == 0) or (d == 1 and nd == 3):
                        temp.append(atoms[j] + [abs(ny - nx)])
            elif dx == -dy:
                if dx < 0:
                    if (d == 3 and nd == 0) or (d == 1 and nd == 2):
                        temp.append(atoms[j] + [abs(ny - nx)])
                else:
                    if (d == 2 and nd == 1) or (d == 0 and nd == 3):
                        temp.append(atoms[j] + [abs(ny - nx)])
        total += check(temp)
    print(total)
