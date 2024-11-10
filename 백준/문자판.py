dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(idx, x, y):
    if dp[x][y][idx] != -1:
        return dp[x][y][idx] # 값이 있다면 해당 그 값을 이용

    
    if idx >= len(str_input) - 1:
        return 1

    cnt = 0
    for k in range(1, K+1):
        for i in range(4):
            nx = x + k * dx[i]
            ny = y + k * dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == str_input[idx + 1]:
                    cnt += dfs(idx + 1, nx, ny)

    dp[x][y][idx] = cnt
    return cnt
    
count = 0
N, M, K  = map(int, input().split()) # N은 세로, M은 가로, K는 인덱스
board = []

for i in range(N):
    board.append(input())
str_input = input().rstrip()
dp = [[[-1 for idx in range(len(str_input))] for y in range(M)] for x in range(N)] 
for i in range(N):
    for j in range(M):
        if board[i][j] == str_input[0]:
            count += dfs(0, i, j)
print(count)