dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = 10

N = 16

def bfs(x, y, visited):
    visited[x][y] = 1
    queue = []
    queue.append((x, y))

    while queue:
        nowX, nowY= queue.pop(0)
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 방문하지 않았고 길이라면 진행
                if visited[nx][ny] == 0 and board[nx][ny] == '0':
                    queue.append((nx, ny))
                    visited[nx][ny] = 1 # 방문 처리
                elif visited[nx][ny] == 0 and board[nx][ny] == '3':
                    return True
    
    return False

def dfs(x, y, visited):
    # 현재 위치 방문 처리
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0:
                if board[nx][ny] == '0':
                    if dfs(nx, ny, visited) == True:
                        return True
                    visited[nx][ny] = 0
                elif board[nx][ny] == '3':
                    visited[nx][ny] = 1
                    return True

    return False

for tc in range(1, T+1):
    answer = 0
    testCase = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    # 0은 미방문 1은 방문을 의미한다.
    visit = [[0 for _ in range(N)] for _ in range(N)]

    # 1은 벽이며, 0은 길, 2는 출발점, 3은 도착점을 의미한다.
    for i in range(len(board)):
        for j in range(0, len(board[i])):
            # 출발점에 bfs나 dfs 시행
            if board[i][j] == '2':
                result = bfs(i, j, visit)
                if result == True:
                    answer = 1
    
    print("#{} {}".format(testCase, answer))
