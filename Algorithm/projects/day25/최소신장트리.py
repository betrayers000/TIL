import sys

sys.stdin = open('tree.txt', 'r')


def f(n):
    if n == cycle[n]:
        return cycle[n]
    return f(cycle[n])


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    # 가중치(w) 테이블 만들기
    table = [[0] * (V + 1) for _ in range(V + 1)]
    path = []
    for _ in range(E):
        i, j, w = map(int, input().split())
        path.append([i, j, w])
        table[i][j] = w
        table[j][i] = w
    # 크루스칼을 위해서 가중치가 적은 순서대로 정렬
    path = sorted(path, key=lambda x: x[2])
    # 사이클 회피
    cycle = list(range(V + 1))
    rank = [0] * (V+1)
    total = 0
    for p in path:
        i, j, w = p
        r1 = f(i)
        r2 = f(j)
        if r1 != r2:
            if rank[r1] > rank[r2]:
                total += w
                cycle[r2] = r1
            else:
                cycle[r1] = r2
                total += w
                if rank[r1] == rank[r2]:
                    rank[r2] += 1
    print("#{} {}".format(t, total))