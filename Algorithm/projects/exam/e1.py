s = "baaabbabbb"
s_2 = "babba"
s_3 = "abaaaa"

def solution(s):
    temp = s[0]
    cnt = 1
    result = ""
    for i in range(len(s)):
        result += s[i]
        if temp == s[i]:
            cnt += 1
        else:
            temp = s[i]
            cnt = 1
        if cnt >= 3:
            if i < len(s)//2:
                result = result[-2:]
            else:
                result = result[:-1]
    print(result)
    return len(result)

print(solution(s))
print(solution(s_2))
print(solution(s_3))
