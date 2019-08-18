import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # board와 num_list를 만들어준다.
    # board는 우리가 만들어야 할 판을 0으로 채워주고
    # num_list 는 넣어야할 숫자를 리스트화시켜서 만들어준다.
    board = [[0]*N for i in range(N)]
    num_list = list(range(1, N**2+1))
    # x, y좌표를 초기화 해준다.
    # change 는 회전수이다 양방향끼리 1회전 음방향끼리 1회전한다.
    x, y = 0, 0
    change = 0
    # start 인덱스를 추가해준다. 일단 0, 0 에 1을 넣어주고 시작한다.
    # 밑에서 회전할때 맨앞경우를 무시하고 맨 뒤경우에 분기처리를 위해서
    start = num_list.pop(0)
    board[0][0] = start
    # 돌린다
    while True:
        # num_list 가 없으면 다 들어간거라서 break
        if num_list == []:
            break
        # change가 짝수일경우 양방향을 진행한다.
        if not(change%2):
            # 양방향은 2가지 오른쪽 아래쪽 방향이다
            # y+1 부터 N까지 반복하면서 숫자를 확인하고 0이면 num_list에서 하나 빼서 넣어준다.
            # 0이 아니면 break해주고 마지막 i를 x에 넣어준다.
            # 마지막 y값이 x고정시 y값 시작이되고, 마지막 x값이 y고정시 x값시작점이 된다.
            for i in range(y+1, N):
                if board[x][i] == 0:
                    board[x][i] = num_list.pop(0)
                else:
                    break
                y = i

            for j in range(x+1, N):
                if board[j][y] == 0:
                    board[j][y] = num_list.pop(0)
                else:
                    break
                x = j
            change += 1
        else:
            # 음방향의 경우 왼쪽방향 위쪽 방향이다
            # 양방향의 반대로 채워 넣어준다.
            for i in range(y-1, -1, -1):
                if board[x][i] == 0:
                    board[x][i] = num_list.pop(0)
                else:
                    break
                y = i
            for j in range(x-1, -1, -1):
                if board[j][y] == 0:
                    board[j][y] = num_list.pop(0)
                else:
                    break
                x = j
            change += 1
    print(board)
