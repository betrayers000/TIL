import sys

sys.stdin = open('password.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    password = list(map(int, input().split()))
    i = M
    for _ in range(K):
        if i > len(password):
            i = i - len(password)
            password.insert(i, password[i - 1] + password[i])
        elif i == len(password):
            password.append(password[i-1] + password[0])
        else:
            password.insert(i, password[i - 1] + password[i])
        i += M
    print(f"#{t} {password[:-11:-1]}")
