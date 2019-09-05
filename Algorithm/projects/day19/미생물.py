import sys

sys.stdin = open('micro.txt', 'r')

# 상하좌우 1, 2, 3, 4

dirc = [[1, 2], [2, 1], [3, 4], [4, 3]]


class microbe:
    global dirc, N

    def __init__(self, x, y, size, di):
        self.x = x
        self.y = y
        self.size = size
        self.di = di

    def move(self):
        if self.di == 1:
            self.x, self.y = self.x - 1, self.y
        elif self.di == 2:
            self.x, self.y = self.x + 1, self.y
        elif self.di == 3:
            self.x, self.y = self.x, self.y - 1
        elif self.di == 4:
            self.x, self.y = self.x, self.y + 1

        if self.x == 0 or self.y == 0 or self.x == N-1 or self.y == N-1:
            self.size = self.size // 2
            for d in dirc:
                if self.di == d[0]:
                    self.di = d[1]
                    break

def grouping(temp):
    total_size = 0
    max_size = 0
    max_di = 0
    for t in temp:
        if max_size < t.size:
            max_size = t.size
            max_di = t.di
        total_size += t.size
    return microbe(temp[0].x, temp[0].y, total_size, max_di)



def check_grouping():
    global sample, K
    result = []
    history = []
    for i in range(len(sample)):
        if i not in history:
            temp = [sample[i]]
            for j in range(i+1, len(sample)):
                if sample[i].x == sample[j].x and sample[i].y == sample[j].y:
                    history.append(j)
                    temp.append(sample[j])
            if len(temp) == 1:
                result.append(temp[0])
            else:
                result.append(grouping(temp))
    return result



T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    sample = [[0] for _ in range(K)]
    for i in range(K):
        x, y, size, di = map(int, input().split())
        sample[i] = microbe(x, y, size, di)
    time = 0
    while time < M:
        for sam in sample:
            sam.move()
        sample = check_grouping()
        time += 1
    total = 0
    for sam in sample:
        total += sam.size
    print(total)





