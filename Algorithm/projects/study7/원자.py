import sys

sys.stdin = open('atom.txt', 'r')

def move(atom):
    x, y, d, e = atom
    if d == 0:
        return [x, y + 0.5, d, e]
    elif d == 1:
        return [x, y - 0.5, d, e]
    elif d == 2:
        return [x - 0.5, y, d, e]
    elif d == 3:
        return [x + 0.5, y, d, e]


def crush_check(atoms):
    global total
    i = 0
    result = []
    n = len(atoms)
    temp = []
    while i < n:
        eng = 0
        if i in temp:
            i += 1
            continue
        x1, y1, d1, e1 = atoms[i]
        cnt = 0
        for j in range(i+1, n):
            x2, y2, d2, e2 = atoms[j]
            if x1 == x2 and y1 == y2:
                cnt += 1
                eng += e2
                temp.append(j)
            if cnt == 3:
                break
        if cnt == 0:
            result.append(atoms[i])
        else:
            eng += e1
        i += 1
        total += eng
    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for _ in range(4000):
        after = []
        for atom in atoms:
            after.append(move(atom))
        atoms = crush_check(after)
    print(total)



#1 10
#2 16
#3 5
#4 895
#5 5742
