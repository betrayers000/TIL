nums = [1, 3, 2, 5, 4]

start = nums[0]

result = []
start = nums[0]
end = []
stack = []
temp = [start]
while True:
    if temp == []:
        break
    for n in nums:
        if n > start:
            if end == []:
                end.append(n)
                start = n
                temp.append(start)
                break
            else:
                if not n in end:
                    end.append(n)
                    start = n
                    temp.append(start)
                    break
    else:
        result.append(temp)
        stack.append(temp.pop())
        start = temp.pop()

print(result)