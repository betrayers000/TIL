import sys

sys.stdin = open('input.txt', 'r')

def calcs(nums, sig):
    cnt = 0
    while True:
        if len(nums) == 1:
            break
        s2 = nums.pop()
        s1 = nums.pop()
        sign = sig.pop()
        if sign == "-":
            result = s1-s2
        elif sign == "+":
            result = s1+s2
        elif sign == "/":
            result = int(s1/s2)
        elif sign == "*":
            result = s1*s2
        nums.append(result)
        cnt += 1

    return nums



for t in range(1, 11):
    N = int(input())
    calc = [input().split() for n in range(N)]
    sig = []
    nums = []
    for c in calc:
        try:
            nums.append(int(c[1]))
        except:
            sig.append(c[1])
    result = calcs(nums, sig)
    print(result)

