import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T + 1):
    a, N = input().split()
    nums = list(map(int, a))
    cnt = 0
    n = 0
    # cnt 즉 변경횟수가 N만큼 되거나 n이 해당 문자 길이만큼까지 반복한다.
    # n은 자리수 0자리부터 순서대로 최대값과 변경해내가면 가장 큰값을 가지게 된다.
    # 하지만 최대값이 여러개 있을경우에는 최대값의 개수만큼 문자를 검사해서 최소값을 해당 n으로 보내야 최대경우를 찾는다.
    while True:
        max_ = 0
        max__ = 0
        if n >= len(nums) or cnt == int(N):
            break
        # n부터 문자열 길이까지 반복시켜서 가장큰 값의 인덱스를 찾는다.
        for i in range(n, len(nums)):
            if max_ <= nums[i]:
                max_ = nums[i]
                max__ = i
        # 찾은 인덱스가 n보다 클경우 자리를 바꾼다.
        # 자리를 바꾸기전에 최대값이 여러개 있을경우 해당 최대값 카운트 만큼
        # 앞자리부터 검사를 해서 최소값을 앞으로 보낸다.
        # 이유 - 최대값이 여러개있을경우 최소값을 앞으로 보내고 변경하면 횟수는 똑같기 때문
        if max__ > n:
            if nums.count(max(nums)) > 1:
                cmin = 0
                cmin_ = nums[0]
                for z in range(nums.count(max(nums))):
                   if nums[z] < cmin_:
                       cmin_ = nums[0]
                       cmin = z
                if cmin != 0:
                    nums[n], nums[cmin] = nums[cmin], nums[n]
            nums[n], nums[max__] = nums[max__], nums[n]
            cnt += 1
        n += 1
    k = int(N)-cnt
    # 위의 과정을 끝내고 변경횟수가 N보다 작을 경우
    # 최대값이 여러개있는경우는 해당 최대값을 반복해서 변경해주면 되기때문에 pass
    # 최대값이 여러개 없는 경우에는 맨 뒷자리를 반복해서 변경해주면 최대값을 얻을 수있다.
    # 홀수일경우에는 변경해주고 짝수일경우에는 제자리이기 때문에 변경하지 않아도 된다.
    if k%2:
        if nums.count(max(nums)) > 1:
            pass
        else:
            nums[-2], nums[-1] = nums[-1], nums[-2]
    print(nums)

