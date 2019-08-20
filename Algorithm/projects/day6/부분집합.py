# 합이 10인 부분집합의 개수
def f(i, N, K, s):
    global cnt
    global bit
    # if i == N:
    #     s = 0
    #     for j in range(N): # 0~N-1은 원래 집합의 원소 1~N을 가리킴
    #         if bit[j] == 1: #j+1이 부분집합에 포함된 경우
    #             s += j+1
    #     if s == K:
    #         cnt += 1
    if s == K: # s가 K면 원소를 더 추가하게 되면 K보다 커지므로 바로 끝낸다.
        cnt += 1
        return
    elif i == N: # 합이 K가 아닌경우 모두 다돌았는데
        return
    else:
        bit[i] = 0
        f(i+1, N, K, s) # i번이 가리키는 값은 부분집합에 포함하지 않음
        bit[i] = 1
        f(i+1, N, K, s + i+1) # i번이 가리키는 값을 부분집합이 포함
N = 10
K = 10
cnt = 0
bit = [0]*N
f(0, N, K, 0)
print(cnt)