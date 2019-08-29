import sys

sys.stdin = open('card.txt', 'r')

def suffle(n):
    global length, indexing
    deck = list(range(n))
    edge_start = 0
    start, end = len(deck) // 2 - 1, len(deck) // 2
    for i in range(n):
        indexing.append(deck[:])
        for j in range(start, end, 2):
            deck[j], deck[j + 1] = deck[j + 1], deck[j]
        if start == edge_start:
            start += 1
            end -= 1
            edge_start = start
        else:
            start -= 1
            end += 1

for t in range(int(input())):
    impossible = True
    length = int(input())
    indexing = []
    suffle(length)
    cards = list(map(int, input().split()))
    stacks = [cards]
    if cards == sorted(cards) or cards == sorted(cards, reverse=True):
        stacks = []
        impossible = False
    cnt = 0
    while len(stacks) != 0:
        cnt += 1
        temp_stacks = []
        while len(stacks) != 0:
            stack = stacks.pop()
            for i in range(1, length):
                temp = []
                for index in indexing[i]:
                    temp.append(stack[index])
                if temp == sorted(temp) or temp == sorted(temp, reverse=True):
                    temp_stacks = []
                    stacks = []
                    impossible = False
                    break
                else:
                    temp_stacks.append(temp)
        for temp_stack in temp_stacks:
            stacks.append(temp_stack)
        if impossible == True:
            if cnt == 5:
                break
    if impossible:
        cnt = -1
    print("#{} {}".format(t + 1, cnt))