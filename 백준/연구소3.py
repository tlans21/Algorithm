dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(board, combi_lst):
    temp_board = [[board[i][j] for j in range(N)] for i in range(N)]
    time_board = [[123456789 for _ in range(N)] for _ in range(N)]
    queue = []
    for i in range(M):
        (x, y) = combi_lst[i]
        queue.append((x, y, 0))
    
    while queue:
        nowX, nowY, nowTime = queue.pop(0)
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            nextTime = nowTime + 1
            if 0 <= nextX < N and 0 <= nextY < N:
                # 벽이 아닌 경우 진행
                if temp_board[nextX][nextY] == 0:
                    if time_board[nextX][nextY] > nextTime:     
                        time_board[nextX][nextY] = nextTime
                        queue.append((nextX, nextY, nextTime))

                elif temp_board[nextX][nextY] == 2:
                    if time_board[nextX][nextY] > nowTime:
                        time_board[nextX][nextY] = nowTime
                        queue.append((nextX, nextY, nowTime))
    result = -1
    for i in range(N):
        for j in range(N):
            if temp_board[i][j] != 1:
                if time_board[i][j] == 123456789:
                    return -1
                result = max(result, time_board[i][j])
    return result

def combination(start, depth, board):
    global answer
    if depth == M:
        maxLength = bfs(board, combi_lst)
        if maxLength != -1:
            answer = min(answer, maxLength)
            return
        answer = maxLength
    for i in range(start, len(loc_lst)):
        combi_lst.append(loc_lst[i])
        combination(i + 1, depth + 1, board)
        combi_lst.pop()

answer = 123456789
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
loc_lst = []

combi_lst = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            loc_lst.append((i, j))

combination(0, 0, board)
print(answer)