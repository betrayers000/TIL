data = [[1, 0, 5], [2, 2, 2], [3, 3, 1], [4, 4, 1], [5, 10, 2]]
data_2 = [[1, 0, 3], [2, 1, 3], [3, 3, 2], [4, 9, 1], [5, 10, 2]]
data_3 = [[1, 2, 10], [2, 5, 8], [3, 6, 9], [4, 20, 6], [5, 25, 5]]


def get_list(nl):
    minV = -1
    min_idx = 0
    for idx, n in enumerate(nl):
        if n[2] < minV or minV == -1:
            minV = n[2]
            min_idx = idx
    return min_idx

def solution(data):
    ans = []
    time = 0
    next_list = []
    last_n = 0
    now = 0
    while 1:
        # print(ans, next_list, time, now)
        if next_list != []:
            if time >= now:
                idx = get_list(next_list)
                a, b, c = next_list.pop(idx)
                ans.append(a)
                now = time + c
        if len(ans) == len(data):
            break
        for i in range(last_n, len(data)):
            n, t, p = data[i]
            if t == time:
                next_list.append(data[i])
                last_n = n - 1
        time += 1
    return ans

print(solution(data))
print(solution(data_2))
print(solution(data_3))
