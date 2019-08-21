import sys

sys.stdin = open('input.txt', 'r')

def bfs(x, end):
    global node
    global E
    global V
    # 큐 생성하고 초기값 설정
    q = []
    q.append([x])
    # visited 로 이미지나온곳을 체크하기위해 노드 수 +1만큼 만들어준다
    # 인덱스 조절하기 귀찮아서 한개 더만듬
    visited = [0] * (V+1)
    # 거리를 0으로 초기화 해준다.
    d = 0
    while 1:
        # 현재 거리의 큐안에 값이 없으면 찾지 못했음으로
        # 거리를 0으로 주고 break
        if q[d] == []:
            d = 0
            break
        # 현재 거리 큐에서 지금 값을 뽑는다.
        now = q[d].pop(0)
        # now에 맞는 visited를 1로 바꿔준다
        visited[now] = 1
        # now와 end가 동일하면 break한다
        if now == end:
            break
        # now에 노드가 존재하면 q에 리스트를 하나더 생성해준다. (거리 표기를 위해)
        # 노드를 확인하고 visited를 체크하고 없으면 현재거리의 +1 한 큐에 넣어준다.
        if node[now] != []:
            q += [[]].copy()
            for n in node[now]:
                if visited[n] != 1:
                    q[d+1].append(n)
        # 현재 큐가 비어있으면 d+1 을 해준다. 다음 거리로 넘어가기 위해
        if q[d] == []:
            d += 1
    return d





T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    node = [[]]
    for _ in range(V):
        node += [[]].copy()
    for __ in range(E):
        x, y = map(int, input().split())
        node[x].append(y)
        node[y].append(x)
    end = list(map(int, input().split()))
    print(bfs(end[0], end[1]))


