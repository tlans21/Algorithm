dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 123456789
def bfs(board, combi_lst):
    queue = []
    # BFS 내에서 도는 임시 보드
    temp_board = [[board[i][j] for j in range(N)] for i in range(N)]
    time_board = [[123456789 for j in range(N)] for i in range(N)]
    for k in range(M):
        (x, y) = combi_lst[k]
        time_board[x][y] = 0
        queue.append((x, y, 0))        
    while queue:
        nowX, nowY, nowTime = queue.pop(0)
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N:
                if temp_board[nextX][nextY] != 1:
                    nextTime = nowTime + 1
                    if time_board[nextX][nextY] > nextTime:
                        time_board[nextX][nextY] = nextTime
                        queue.append((nextX, nextY, nextTime))
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
            answer = min(maxLength, answer)
            return
        return 
    
    for i in range(start, len(lst)):
        combi_lst.append(lst[i])
        combination(i + 1, depth + 1, board)
        combi_lst.pop()
    return

answer = 123456789
N, M = map(int, input().split())
visit = [[0 for _ in range(N)] for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
lst = []
combi_lst = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            lst.append((i, j))


combination(0, 0, board)


if answer != 123456789:
    print(answer)
elif answer == 123456789:
    print(-1)



