import sys

sys.stdin = open("input.txt", "r")

result = []


for t in range(1, 11):
    N = int(input())
    node_dir = []
    node_list = []
    for i in range(N+1):
        node_dir += [[]].copy()
        node_list += [[]].copy()
    for i in range(N):
        node = input().split()
        for j in range(len(node)):
            if j == 0:
                continue
            elif j > 1:
                node_dir[i+1].append(int(node[j]))
            else:
                node_list[i+1].append(node[j])
    start = 1
    word = []
    print(node_dir)
    print(node_list)

