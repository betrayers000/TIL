def solution(heights):
    answer = [0] * len(heights)
    for i in range(len(heights)-1, 0, -1):
        temp = i
        now = heights[i]
        while temp > 0:
            temp -= 1
            left = heights[temp]
            if now < left:
                answer[i] = temp+1
                break
    return answer

heights = [6,9,5,7,4]
solution(heights)