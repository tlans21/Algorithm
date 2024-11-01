dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, board):
    visited[x][y] = 1 # 방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            # 다음으로 갈 곳이 방문하지도 않고 유기농 배추가 있다면 깊이 진행
            if visited[nx][ny] == 0 and board[nx][ny] == 1:
                dfs(nx, ny, visited, board)

    return 
    



T = int(input())

for _ in range(0, T):
    M, N , K = map(int, input().split()) # M 가로, N 세로
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    # K번 반복해서 좌표값 입력
    for cnt in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1 # 배추의 위치  같은 경우는 없음


    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, visited, board)
                answer += 1   
    
    print(answer)