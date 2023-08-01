N, M = map(int, input().split())

board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]

temp = 0

def dfs(x, y, depth, maxValue):
    global temp
    # 이미 최종적으로 최댓값이 나왔으므로 검사 할 필요가 없다는 코드
    if temp >= maxValue + (3 - depth) * board_maxValue:
        return


    if depth == 3:
        temp = max(temp, maxValue)
        return 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0:
                
                # ㅏ ㅓ ㅗ ㅜ 모양을 만들어야함
                if depth == 1:
                    # 자리는 유지하되, 다음 가는 방향만을 방문처리와 더하기만 하고 실제로 그 자리는 가지않는다.
                    visited[nx][ny] = 1
                    dfs(x, y, depth + 1, maxValue + board[nx][ny])
                    visited[nx][ny] = 0 

                visited[nx][ny] = 1
                dfs(nx, ny, depth + 1, maxValue + board[nx][ny])
                # 백트레킹
                visited[nx][ny] = 0

board_maxValue = max(map(max, board))
    
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, board[i][j])
        visited[i][j] = 0
print(temp)


        