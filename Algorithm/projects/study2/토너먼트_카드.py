import sys

sys.stdin = open("input.txt", "r")

def rcp(p1, p2):
    global winningList
    p1_ = str(p1[1])
    p2_ = str(p2[1])
    if [p1_, p2_] in winningList:
        return [p1]
    else :
        return [p2]



# def gaming(players):
#     next_players = []
#     while players != []:
#         if len(players) == 1:
#             next_players.append(players.pop())
#             break
#         p1 = players.pop(0)
#         p2 = players.pop(0)
#         winner = rcp(p1, p2)
#         next_players.append(winner)
#     return next_players



def grouping(players):
    n = len(players)
    if n == 1:
        return players
    if n == 2:
        return grouping(rcp(players[0], players[1]))
    else:
        if n % 2:
            group1 = players[:n//2+1]
            group2 = players[n//2+1:]
        else:
            group1 = players[:n//2]
            group2 = players[n//2:]
        group1 = grouping(group1)
        group2 = grouping(group2)
        return grouping(group1 + group2)



T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 사람수
    players = list(enumerate(map(int, input().split())))
    winningList = [['1', '3'], ['2', '1'], ['3', '2'], ['1', '1'], ['2', '2'], ['3', '3']]
    a = grouping(players)
    print(a)
    print(a[0][0]+1)






