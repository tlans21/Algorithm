from collections import deque
N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 123456789
board = []

shark_size = 2



for i in range(N):
    board.append(list(map(int, input().split())))

x, y = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            x = i
            y = j

def bfs(x, y, shark_size):
    
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]

    visited[x][y] = 1
    
    queue = deque()
    queue.append((x, y))
    temp = []

    while queue:
        
        curX, curY = queue.popleft()

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and shark_size >= board[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[curX][curY] + 1
                    
                    if board[nx][ny] < shark_size and board[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    return sorted(temp, key = lambda x: (x[2], x[0], x[1]))


cnt = 0
result = 0

while True:
    shark = bfs(x, y, shark_size)

    if len(shark) == 0:
        break
    
    nx, ny, dist = shark.pop(0)

    result += dist

    # 상어 위치와 먹힌 물고기 위치 초기화
    board[nx][ny], board[x][y] = 0, 0 

    x, y = nx, ny
    # 가까운 물고기 먹은 것을 카운트
    cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0
        
print(result)






    

            

