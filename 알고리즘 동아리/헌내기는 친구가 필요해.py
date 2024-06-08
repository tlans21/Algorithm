dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I는 한번만 주어짐
# 도연이가 만날 수 있는 사람의 수를 출력.

def bfs(x, y):
    global people
    queue = []
    queue.append([x, y])
    visited[x][y] = 1
    
    while queue:
        nowX, nowY = queue.pop(0)
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < M:
                if visited[nextX][nextY] == -1 and board[nextX][nextY] != 'X':
                    visited[nextX][nextY] = 1
                    queue.append([nextX, nextY])
                    if board[nextX][nextY] == 'P':
                        people += 1
    return

N, M = map(int, input().split())

board = [list(map(str, input())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
people = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            bfs(i, j) # 도연이가 있는 공간에 bfs 실행하여 사람찾기.
if people != 0:
    print(people)
else:
    print("TT")