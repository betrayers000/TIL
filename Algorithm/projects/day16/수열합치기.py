import sys

sys.stdin = open('ssum.txt', 'r')

class SList:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_front(self, data):
        if self.head == None:
            self.head = self.Node(data, None)
        else:
            self.head = self.Node(data, self.head)

        self.size += 1

    def insert_after(self, data, p):
        p.next = SList.Node(data, p.next)
        self.size += 1

    def get_max_index(self, target):
        p = self.head
        for i in range(self.size):
            if p.data > target:
                return i
            p = p.next
        return self.size

    def get_node(self, target):
        p = self.head
        for i in range(target-1):
            p = p.next
        return p

    def get_list(self):
        result = []
        p = self.head
        while p:
            result.append(p.data)
            p = p.next
        return result

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    s = SList()
    for m in range(M):
        if m == 0:
            for n in list(map(int, input().split()))[::-1]:
                s.insert_front(n)
        else:
            temp = list(map(int, input().split()))
            idx = s.get_max_index(temp[0])
            if idx == 0:
                for t in temp[::-1]:
                    s.insert_front(t)
            else:
                for t in temp[::-1]:
                    s.insert_after(t, s.get_node(idx))
    print(s.get_list()[:-11:-1])

