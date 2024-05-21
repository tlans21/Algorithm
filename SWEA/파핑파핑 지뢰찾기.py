T = int(input())

dx =[-1, -1, 1, 1, 0, 0, -1, 1]
dy =[-1, 1, -1, 1, -1, 1, 0, 0]

def bfs(x, y, visited):
    queue = []
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        nowX, nowY = queue.pop(0)
        cnt = 0
        for i in range(8):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N and board[nextX][nextY] == '*':
                cnt += 1
        
        if cnt == 0:
            board[nowX][nowY] = '0'
            for i in range(8):
                nextX = nowX + dx[i]
                nextY = nowY + dy[i]

                if (0 <= nextX < N and 0 <= nextY < N) and board[nextX][nextY] == '.' and visited[nextX][nextY] == 0:
                    visited[nextX][nextY] = 1
                    queue.append((nextX, nextY))
        else:
            board[nowX][nowY] = str(cnt)    
                

        board[nowX][nowY] = cnt
            

def check(x, y):
    
    for i in range(8):
        nx = x + dx[i] 
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == '*':
                return False
            
    return True

for tc in range(1, T+1):
    N = int(input())
    answer = 0
    board = [list(map(str, input())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                if check(i, j) == True:
                # 해당 자리를 우선하여 진행
                    bfs(i, j, visit)
                    answer += 1

    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                if check(i, j) == False:
                # 해당 자리를 우선하여 진행
                    bfs(i, j, visit)
                    answer += 1

    print("#{} {}".format(tc, answer))      

