nums = [3, 30, 34, 5, 9]

def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:int(x[0]), reverse=True)
    n = len(numbers)
    visited = [0] * n
    idx = []
    for i in range(n):
        if len(numbers[i]) == 1:
            idx.append(i)
    idx.append(n)
    for i in range(len(idx)-1):
        left = []
        right = []
        now = numbers[idx[i]]
        for j in range(idx[i]+1, idx[i+1]):
            temp = numbers[j]
            if int(temp[1]) > int(now):
                left.append(int(temp))
            else:
                right.append(int(temp))
        left.sort(reverse=True)
        right.sort(reverse=True)
        res = left + [int(now)] +right
        answer += ''.join(map(str, res))
    return answer
#
# def f(n, k, s, numbers):
#     global answer, used
#     if n == k:
#         if int(answer) < int(s):
#             answer = s
#         return
#     elif n > 0 and answer[0] > s[0]:
#         return
#     else:
#         for i in range(k):
#             if used[i] == 0:
#                 used[i] =1
#                 f(n+1, k, s + numbers[i], numbers)
#                 used[i] = 0
#
# def solution(numbers):
#     global used, answer
#     answer = str(max(numbers))
#     n = len(numbers)
#     temp = list(map(str, numbers))
#     used = [0] * n
#     f(0, n, "", temp)
#     return answer

print(solution(nums))
