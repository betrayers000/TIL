import sys

sys.stdin = open('calc.txt', 'r')


def bfs(M, n):
    q = [0] * 1000000
    h = set()
    # front, rear = -1, -1
    # rear += 1
    front, rear = 0, 0
    rear = (rear + 1) % 1000000
    q[rear] = [n, 0]
    calc = [3, 2, 1, 4]
    while front != rear:
        # front += 1
        front = (front + 1) % 1000000
        n, c = q[front]
        if {n} & h == set():
            h.add(n)
            for i in range(4):
                nx = 0
                if calc[i] == 1:
                    nx = n + 1
                elif calc[i] == 2:
                    nx = n - 1
                elif calc[i] == 3:
                    if n % 2 != 1:
                        nx = n // 2
                elif calc[i] == 4:
                    nx = n + 10
                if nx == M:
                    return c + 1
                else:
                    if 0 < nx <= 1000000 and {nx} & h == set():
                        # rear += 1
                        rear = (rear + 1) % 1000000
                        q[rear] = [nx, c + 1]
    return 0


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    print("#{} {}".format(t, bfs(N, M)))
