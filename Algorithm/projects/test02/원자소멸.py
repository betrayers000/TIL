import sys

sys.stdin = open('input.txt', 'r')



T = int(input())
for t in range(1):
    N = int(input())
    # d_0 =[]
    # d_1 = []
    # d_2 = []
    # d_3 = []
    # for n in range(N):
    #     x, y, d, e = map(int, input().split())
    #     if d == 0:
    #         d_0.append([x, y, d, e])
    #     elif d == 1:
    #         d_1.append([x, y, d, e])
    #     elif d == 2:
    #         d_2.append([x, y, d, e])
    #     elif d == 3:
    #         d_3.append([x, y, d, e])
    # print(d_0, d_2)
    pic = [list(map(int, input().split())) for n in range(N)]
    for i in range(N):
        x, y, d, e = pic[i]
        temp = []
        for j in range(i, N):
            nx, ny, nd, ne = pic[j]
            if d == 0:
                if nd == 3 and nx == y and ny == x:
                    print('crush')
                elif nd == 2 and abs(nx-x) == abs(ny-y):
                    print('crush')
                elif nd == 1 and x == nx:
                    print('crush')
            if d == 1:
                if nd == 2 and nx == y and ny == x:
                    print('crush')
                elif nd == 3 and abs(nx-x) == abs(ny-y):
                    print('crush')
                elif nd == 0 and x == nx:
                    print('crush')
            if d == 2:
                if nd == 3 and ny == y:
                    print('crush')
                elif nd == 0 and abs(nx-x) == abs(ny-y):
                    print('crush')
                elif nd == 1 and nx == y and ny == x:
                    print('crush')
            if d == 3:
                if nd == 0 and nx == y and ny == x:
                    print('crush')
                elif nd == 1 and abs(nx-x) == abs(ny-y):
                    print('crush')
                elif nd == 2 and x == nx:
                    print('crush')




