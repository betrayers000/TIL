import sys

sys.stdin = open("input.txt", "r")


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
    x = N
    word = []
    while True:
        if len(word) >= N:
            break
        for i in range(len(node_dir)):
            if node_dir[i] == []:
                continue
            else:
                if x in node_dir[i]:
                    word.append(node_list[x])
                    node_dir[i].pop(0)
                    if node_dir[x] != []:
                        x = node_dir[x][0]
                    else:
                        x = i
                    break
        else:
            word.append(node_list[1])
            s = 1
            while True:
                try:
                    s = node_dir[s][0]
                except:
                    break
            x = s
    print(word)
