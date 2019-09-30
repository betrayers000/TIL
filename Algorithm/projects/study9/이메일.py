answers = ["d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"]
answers_2 = ["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]
tops = ["com", "net", "org"]

def solution(answers):
    cnt = 0
    for ans in answers:
        if ans.count("@") > 1:
            continue
        idx = 0
        domain = False
        d = 0
        for i in range(len(ans)):
            if d > 1:
                domain = False
                break
            if ord("a") <= ord(ans[i]) <= ord("z") or ans[i] == "." or ans[i] == "@":
                if ans[i] == "." and domain:
                    idx = i
                    d += 1
                if ans[i] == "@":
                    domain = True
        if ans[idx+1:] in tops and domain:
            cnt += 1
    return cnt

print(solution(answers))
print(solution(answers_2))
