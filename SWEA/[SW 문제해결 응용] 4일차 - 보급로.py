dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

def bfs(x, y, visited):
    global answer
    queue = []
    queue.append((x, y, 0))
    visited[x][y] = 0

    while queue:
        nowX, nowY, nowCost = queue.pop(0)
        if nowX == N-1 and nowY == N-1:
            answer = min(answer, nowCost)
            continue

        for i in range(0, 4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if (0 <= nx < N and 0 <= ny < N) and visited[nx][ny]:
                nextCost = nowCost + int(board[nx][ny])
                if nextCost < visited[nx][ny]:
                    visited[nx][ny] = nextCost
                    queue.append((nx, ny, nextCost))
                    
                     



for tc in range(1, T+1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    visit = [[123456789 for _ in range(N)] for _ in range(N)]
    answer = 123456789
    bfs(0, 0, visit)
    print("#{} {}".format(tc, answer))

