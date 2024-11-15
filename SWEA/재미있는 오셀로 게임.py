dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
def dfs(x, y, color, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == color:
            return True
        if board[nx][ny] != 0 and board[nx][ny] != color:
            willChangeList.append((nx, ny)) # 바꿔야할 좌표 값 입력
            return dfs(nx, ny, color, direction)
    return False
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N: 한 변의 길이, M : 돌을 놓는 횟수

    # 돌의 색이 1이면 흑돌, 2이면 백돌이다.
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # 기본 세팅
    board[(N//2) - 1][(N//2) - 1] = 2
    board[(N//2)][(N//2) - 1] = 1
    board[(N//2) -1][(N//2)] = 1
    board[(N//2)][(N//2)] = 2
    
    for _ in range(M):
        x, y, color = map(int, input().split())
        board[x-1][y-1] = color

        for k in range(8): # 8개의 방향에 대해서 dfs 시행
            willChangeList = []
            if dfs(x-1, y-1, color, k):
                for changeX, changeY in willChangeList:
                    board[changeX][changeY] = color
    WCnt = 0
    BCnt = 0
    for i in range(0, N):
        for j in range(0, N):
            if board[i][j] == 1:
                BCnt +=1
            elif board[i][j] == 2:
                WCnt += 1
    print("#{} {} {}".format(tc, BCnt, WCnt))