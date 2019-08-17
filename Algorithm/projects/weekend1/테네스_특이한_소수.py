T = int(input())
n_list = [2]
for num in range(1, 1000000):
    check = True
    for n in n_list:
        if n ** 2 > num:
            break
        if not (num % n):
            check = False
            break
    # 2이상으로 해야한다 이미 2가 들어가있기 때문
    # 2를 빼고 num != 1 로 해도 된다.
    if check and num > 2:
        n_list.append(num)
for t in range(1, T + 1):
    D, A, B = map(int, input().split())
    cnt = 1
    for i in n_list:
        if i < A:
            continue
        elif i > B:
            break
        if str(D) in str(i):
            cnt += 1
    print(cnt)
