import sys

sys.stdin = open('calc.txt', 'r')

def f(n):
    global N
    if n > 0:
        a = f(ch1[n])
        b = f(ch2[n])
        if a != None and b != None:
            if tree[n] == "+":
                tree[n] = a+b
            elif tree[n] == "-":
                tree[n] = a-b
            elif tree[n] == "/":
                tree[n] = int(a/b)
            elif tree[n] == "*":
                tree[n] = a*b
        return tree[n]


for t in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for _ in range(N):
        n = input().split()
        nn = int(n[0])
        try:
            int(n[1])
            tree[nn] = int(n[1])
        except:
            tree[nn] = n[1]
        if len(n) == 4:
            ch1[nn] = int(n[2])
            ch2[nn] = int(n[3])
        elif len(n) == 3:
            ch1[nn] = int(n[2])

    f(1)
    print(tree[1])