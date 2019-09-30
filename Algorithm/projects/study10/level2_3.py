def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = []
        for s in tree:
            if s in skill:
                n = skill.index(s)
                if temp != [] and temp[-1]+1 == n:
                    temp.append(n)
                elif temp == [] and n == 0:
                    temp.append(n)
                else:
                    break
        else:
            answer += 1
    return answer

s1 = "AZED"
s2 = ["EBACD", "CBADF", "AECB", "BDA"]

print(solution(s1, s2))