s = "a3dddd"

def solution(s):
    sl = s.split()
    res = []
    for sa in sl:
        temp = sa[0].upper()
        for i in range(1, len(sa)):
                temp += sa[i].lower()
        res.append(temp)
    answer = " ".join(res)
    print(res)
    return answer

print(solution(s))