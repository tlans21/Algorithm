
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def dfs(x, y, board, visited):
    visited[x][y] = 1
    global trigger
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] > board[x][y]:
                trigger = False
            if visited[nx][ny] == 0 and board[x][y] == board[nx][ny]:
                dfs(nx, ny, board, visited)


N, M = map(int, input().split())

board = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] > 0 and visited[i][j] == 0:
            trigger = True
            dfs(i, j, board, visited)
            if trigger:
                answer += 1
print(answer)
