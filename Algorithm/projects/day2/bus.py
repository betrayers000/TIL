T = int(input())
for test_case in range(1, T + 1):
    # k,n,m 받기
    k, n, m =[int(n) for n in input().split()]
    # 충전소 위치 받기
    charges = [int(t) for t in input().split()]
    # i 는 출발선 , result는 i값 모음 마지막 지점을 체크하기 위해서임
    i = 0
    result = []
    for station in range(n):
        # mv는 움직인 칸
        mv = [m for m in range(i+ 1, i+k+1) if m <= n]
        # 도착점이 mv에 있으면 반복을 멈춘다.
        if n in mv :
            break
        # mv 안에서 충전소값을 가져온다.
        cv = [c for c in charges if c in mv]
        # 충전소가 있을시에 맨마지막 충전소가 다시 시작지점이 된다.
        # 충전소가 없으면 도달하지 못했기 때문에 break를 준다.
        if len(cv) > 0:
            i = cv[-1]
            result.append(i)
        else :
            break
    # 마지막 출발선이 마지막 충전소가 있어야하는 곳보다 적으면 출발을 못했기 때문에 0
    if result[-1] < n-k:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} {len(result)}")