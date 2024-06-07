dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = []
    queue.append([x, y])
    visited[x][y] = 0
    while queue:
        nowX, nowY = queue.pop(0)
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if 0 <= nextX < n and 0 <= nextY < m:
                if board[nextX][nextY] != 0 and visited[nextX][nextY] == -1:
                    visited[nextX][nextY] = visited[nowX][nowY] + 1
                    queue.append([nextX, nextY])
    
n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            x = i
            y = j
bfs(x, y)

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            visited[i][j] = 0
for lst in visited:
    print(" ".join(map(str, lst)))
