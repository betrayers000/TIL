begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

def solution(begin, target, words):
    answer = 0
    q = []
    n = len(begin)
    visited = [0] * len(words)
    for i in range(len(words)):
        if visited[i] == 0:
            a = words[i]
            for j in range(n):
                for k in range(n):
                    if k != j:
                        if a[k] != begin[k]:
                            break
                else:
                    q.append(i)
                    visited[i] = 1
    while q:
        b = q.pop(0)
        nw = words[b]
        if nw == target:
            return visited[b]
        for i in range(len(words)):
            if visited[i] == 0:
                a = words[i]
                for j in range(n):
                    for k in range(n):
                        if k != j:
                            if a[k] != nw[k]:
                                break
                    else:
                        q.append(i)
                        visited[i] = visited[b] +1
    return answer

print(solution(begin,target,words))