dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

temp_board = [[0 for j in range(C)] for i in range(R)]

airCondition = []
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            airCondition.append([i, j])
            temp_board[i][j] = -1

up = airCondition[0]
upX = up[0]
upY = up[1]
down = airCondition[1]
downX = down[0]
downY = down[1] 
time = 0
while True:
    temp_board = [[0 for j in range(C)] for i in range(R)]
    temp_board[upX][upY] = -1
    temp_board[downX][downY] = -1
    for i in range(R):
        for j in range(C):
            # 상하좌우 가능한 것을 체크
            cnt = 0
            if board[i][j] != -1:
                transport = board[i][j] // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if board[nx][ny] != -1:
                            cnt += 1 # 이동이 가능하면 체크
                            temp_board[nx][ny] += transport 
                temp_board[i][j] += board[i][j] - (cnt * transport)
    

    # 공기 청정기 위는 시계방향, 아래는 반시계방향으로 먼지를 한칸씩 이동시킨다.
    # 위 시계방향
    
    # 왼쪽
    
    for i in range(upX, 0, -1):
        if temp_board[i][0] != -1:
            temp_board[i][0] = temp_board[i-1][0]
        elif temp_board[i][0] == -1:
            temp_board[i-1][0] = 0
    # 위쪽
    for i in range(0, C-1):
        temp_board[0][i] = temp_board[0][i+1]
    
    # 오른쪽
    for i in range(0, upX):
        temp_board[i][C-1] = temp_board[i + 1][C-1]
    
    # 아래쪽
    for i in range(C-1, 1, -1):
        temp_board[upX][i] = temp_board[upX][i-1]
    temp_board[upX][1] = 0
    
    # 공기 청정기 아래쪽

    # 왼쪽
    for i in range(downX, R-1):
        if temp_board[i][0] != -1:
            temp_board[i][0] = temp_board[i+1][0]
        elif temp_board[i][0] == -1:
            temp_board[i + 1][0] = 0
    # 아래쪽
    for i in range(0, C-1):
        temp_board[R-1][i] = temp_board[R-1][i + 1]
    
    # 오른쪽    
    for i in range(R-1, downX, -1):
        temp_board[i][C-1] = temp_board[i-1][C-1]

    # 위쪽
    
    for i in range(C-1, 1, -1):
        temp_board[downX][i] = temp_board[downX][i-1]
    temp_board[downX][1] = 0

    time += 1

    board = [[temp_board[i][j] for j in range(C)] for i in range(R)]

    if time == T:
        break
answer = 0
for i in range(R):
    for j in range(C):
        if board[i][j] != -1:
            answer += board[i][j]

print(answer)

