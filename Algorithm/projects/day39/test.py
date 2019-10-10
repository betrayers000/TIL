for i in range(1, 1000001):
    # 각 숫자의 약수세기
    check = 0
    for j in range(1, i + 1):
        if i % j == 0:
            check += 1
    if check == 2:
        print(i, end=' ')