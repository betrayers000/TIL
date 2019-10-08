heights = [6, 9, 5, 7, 4]


def solution(heights):
    answer = [0] * len(heights)
    k = len(heights)-1
    while heights:
        n = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > n:
                answer[k] = i+1
                break
        else:
            answer[k] = 0
        k -=1
    return answer

print(solution(heights))
