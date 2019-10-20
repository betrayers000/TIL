T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = []
    while len(nums) != N:
        nums.extend(input().split())
    if len(nums) > 1:
        # 만들 수 있는 숫자모으기
        make = []
        for i in range(len(nums)):
            temp = ''
            for k in range(i, len(nums)):
                temp += nums[k]
                make.append(temp)
        # 문자열에서 숫자로 만들때 생기는 중복을 처리하기
        make = sorted(list(set(map(int, make))))
        ans = 0
        x = 0
        temp = 0
        while len(make) != 1:
            if make[1] - make[0] == 1:
                make.pop(0)
            else:
                pre = make.pop(0)
                ans = pre + 1
                break
        if ans == 0:
            ans = make[-1] + 1
    else:
        if nums[0] == "0":
            ans = 1
        else:
            ans = 0
    print('#{} {}'.format(tc, ans))