s = 'abcdcba'

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        for j in range(n-1, -1, -1):
            if s[i] == s[j]:
                pal = s[j:i - 1:-1]
                if i == 0:
                    pal = s[j::-1]
                if pal == s[i:j+1]:
                    if len(pal) > answer:
                        answer = len(pal)
    return answer

print(solution(s))