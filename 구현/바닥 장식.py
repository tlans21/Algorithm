N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(str, input())))




visited = [[0 for j in range(M)] for i in range(N)]


def dfs(x, y, first):

    visited[x][y] = 1

    # 가로가 들어온 경우

    if first == '-':
        ny = y + 1
        if 0 <= ny < M:
            if visited[x][ny] == 0 and board[x][ny] == first:
                visited[x][ny] = 1
                dfs(x, ny, first)
    elif first == '|':
        nx = x + 1
        if 0 <= nx < N:
            if visited[nx][y] == 0 and board[nx][y] == first:
                visited[nx][y] = 1
                dfs(nx, y, first)
    
    return


    # 세로가 들어온 경우

cnt = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j, board[i][j])
            cnt += 1

print(cnt)