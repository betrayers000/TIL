prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp = len(prices)
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                temp = j
                answer.append(temp-i)
                break
        else:
            answer.append(temp-1-i)
    return answer


print(solution(prices))