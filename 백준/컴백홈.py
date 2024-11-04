# 시간 제한 2초 2억번 연산
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, depth):
    global answer
    visited[x][y] = 1
    
    if x == 0 and y == C-1:
        if K == depth + 1:
            answer += 1
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if visited[nx][ny] == 0 and board[nx][ny] == '.':
                dfs(nx, ny, depth + 1)
                visited[nx][ny] = 0


R, C, K = map(int, input().split())

answer = 0
board = []
visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    board.append(list(map(str, input())))

dfs(R-1, 0, 0) # R-1, 0에서 시작
print(answer)

