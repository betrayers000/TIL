N, K = 1, 20000


def move(N):
    result = set()
    if N-1 > 0:
        result.add(N-1)
    if N+1 > 0:
        result.add(N+1)
    if N*2 > 0:
        result.add(N*2)
    return list(result)


queue = [[N]]
s = 0
while True:
    if queue == []:
        break

    n = queue[s]
    queue += [[]].copy()
    if K in n:
        break
    while n != []:
        z = n.pop(0)
        next_ = move(z)
        queue[s+1].extend(next_)
    s += 1
print(s)
