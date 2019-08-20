def getnext(nums, now_):
    for n in range(len(nums)):
        if nums[n] == now_:
            if n >= len(nums)-1:
                return nums[0]
            else:
                return nums[n]



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    queue = [num_list[0]]
    for i in range(M):
        now_ = queue.pop(0)
        next_ = getnext(num_list, now_)
        queue.append(next_)

    print(queue)
