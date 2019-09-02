import sys

sys.stdin = open('add.txt', 'r')


class SList:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, data):
        if self.is_empty():
            self.head = self.Node(data, None)
        else:
            self.head = self.Node(data, self.head)
        self.size += 1

    def insert_after(self, data, p):
        p.next = SList.Node(data, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            return
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            return
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.data:
                return p
            p = p.next
        return None

    def get_index(self, target):
        p = self.head
        for k in range(target-1):
            p = p.next
        return p

    def get_list(self):
        result = []
        p = self.head
        while p:
            if p.next != None:
                result.append(p.data)
            else:
                result.append(p.data)
            p = p.next
        return result


T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    s = SList()
    for n in nums[::-1]:
        s.insert_front(n)
    for _ in range(M):
        idx, val = map(int, input().split())
        s.insert_after(val, s.get_index(idx))
    last = s.get_list()
    print(last)
    print(last[L])
