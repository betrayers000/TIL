import sys

sys.stdin = open("input.txt", "r")

def rcp(p1, p2):
    p1_ = p1[1]
    p2_ = p2[1]
    if p1_ == 1 and p2_ == 3:
        return p1
    elif p2_ == 1 and p1_ == 3:
        return p2
    a = p2_ - p1_
    if a == 0:
        return p1
    elif a > 0:
        return p2
    elif a < 0 :
        return p1


def gaming(next_):
    t = 0
    if len(next_[0]) == 1:
        return next_[0]
    while True:
        if next_[t] == []:
            break
        if next_[t-1] == [] and len(next_[t]) == 1 and next_[t+1] == []:
            break
        if len(next_[t]) == 1 and next_[t+1] != []:
            p1 = next_[t].pop(0)
            next_[t+1].append(p1)
            continue
        p1 = next_[t].pop(0)
        if next_[t] == [] and next_[t+1] != []:
            p2 = next_[t+1].pop(0)
        else:
            p2 = next_[t].pop(0)
        np = rcp(p1, p2)
        next_ += [[]].copy()
        next_[t+1].append(np)
    for z in next_:
        if len(z) >= 1:
            return z


def grouping(players):
    global result
    n = len(players)
    if n > 2:
        if n % 2:
            group1 = [players[:n//2+1]]
            group2 = [players[n//2+1:]]
        else:
            group1 = [players[:n//2]]
            group2 = [players[n//2:]]
        grouping(gaming(group1))
        grouping(gaming(group2))
    else:
        result.extend(gaming([players]))


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 사람수
    players = list(enumerate(map(int, input().split())))
    result = []
    a = grouping(players)
    b = gaming([result])
    print(b)
    print(b[0][0]+1)





