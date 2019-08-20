def Pascal(N):
    if N == 1:
        return [1]
    elif N == 2:
        return [1, 1]
    else:
        prev = Pascal(N - 1)
        next_center = []
        for i in range(0, len(prev) - 1):
            next_center.append(prev[i] + prev[i + 1])
        return [1, *next_center, 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for i in range(1, N + 1):
        print(" ".join(map(str, Pascal(i))))
