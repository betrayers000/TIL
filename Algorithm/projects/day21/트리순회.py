N = 13
edge = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]


def f(n):
    if n > 0:
        f(ch1[n])
        f(ch2[n])
        print(n, end=" ")

def preorder(n):
    if n > 0:
        print(n, end=" ")
        f(ch1[n])
        f(ch2[n])

def inorder(n):
    if n > 0:
        f(ch1[n])
        print(n, end=" ")
        f(ch2[n])


# 부모를 기준으로 저장
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)

# 자식을 기준으로 부모를 저장
par = [0] * (N+1)

for i in range(1, len(edge), 2):
    if ch1[edge[i-1]] == 0:
        ch1[edge[i-1]] = edge[i]
    else:
        ch2[edge[i - 1]] = edge[i]
    par[edge[i]] = edge[i-1]

print(ch1, ch2, par)
f(1)
print()
inorder(1)
print()
preorder(1)
