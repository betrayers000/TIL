import sys

sys.stdin = open('edit.txt', 'r')

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
        p.next = self.Node(data, p.next)
        self.size += 1

    def delete_node(self, p):
        if self.is_empty():
            return

        t = p.next

        p.next = t.next
        self.size -= 1

    def get_list(self):
        result = []
        p = self.head
        for z in range(self.size):
            result.append(p.data)
            p = p.next
        return result

    def change_data(self, p, data):
        p.data = data

    def get_index(self, target):
        p = self.head
        for z in range(self.size):
            if p.data == target:
                return z
            p = p.next
        return -1

    def get_node(self, target):
        p = self.head
        for z in range(target):
            p = p.next
        return p

    def get_front_node(self, target):
        p = self.head
        for z in range(target-1):
            p = p.next
        return p

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    s = SList()
    for n in nums[::-1]:
        s.insert_front(n)
    for _ in range(M):
        com = input().split()
        if com[0] == "D":
            s.delete_node(s.get_front_node(int(com[1])))
        elif com[0] == "I":
            s.insert_after(int(com[2]), s.get_front_node(int(com[1])))
        elif com[0] == "C":
            s.change_data(s.get_node(int(com[1])), int(com[2]))
    try :
        print(f"#{t} {s.get_list()[L]}")
    except:
        print(f"#{t} -1")
