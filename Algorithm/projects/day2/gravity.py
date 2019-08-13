data = [4, 4, 2, 9, 6, 6, 0, 7, 0]
N = len(data)
mxd = 0
# 최대 높이를 구한다.
for i in range(N):
    if data[i] > mxd:
        mxd = data[i]
mxi_list = []
count = 0
# 최대높이의 상자가 몇개 있는지와 해당상자의 위치를 구한다.
for j in range(N):
    if data[j] == mxd:
        mxi_list.append(j)
        count += 1

# 최대높이의 상자중 첫번째 상자가 제일 낙차가 크기 때문에
# 전체 길이에서 첫번째 상자 인덱스를 빼주고 최대높이에 있는 상자 수만큼 또 빼준다.
# 자기를 포함해서 최대 상자가 있는 만큼 낙차가 줄어들기 때문
result = N - mxi_list[0] - len(mxi_list)

print(result)

