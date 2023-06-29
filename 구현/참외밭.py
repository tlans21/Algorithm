K = int(input())

# 1 동쪽 (오른쪽), 2 서쪽 (왼쪽), 3 남쪽 (아래쪽), 4 북쪽 (위쪽)

# ㄱ자 모양입니다. 따라서 세로변 4, 3 중에서 가장 큰 것을 고르고 
# ㄱ자 모양인 경우 첫번째, 1(오른쪽)을 가로로하고 이어지는 3을 세로로하고 사각형을 만들고 빼준다
#  90도회전, 4가 제일먼저


arr = []
x = []
y = []
lst = []
for i in range(6):
    dir, length = map(int, input().split())
    arr.append((dir, length))

    # 가로 담기
    if dir == 3 or dir == 4:
        x.append(arr[i][1])
    # 세로 담기
    elif dir == 1 or dir == 2:
        y.append(arr[i][1])

for i in range(6):
    if arr[i][0] == arr[(i+2) % 6][0]:
        lst.append(arr[(i+1)%6][1])

print(K * ((max(x) * max(y)) - (lst[0] * lst[1])))