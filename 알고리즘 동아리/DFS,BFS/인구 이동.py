from collections import deque

N, L, R = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
graph = []
data = []
for i in range(N):
    graph.append(list(map(int, input().split())))




def bfs(x, y, index):
    
    global N
    global L
    global R
    
    
    cnt = 1
    queue = deque()
    queue.append((x, y))
    sum = graph[x][y]
    loc = []
    loc.append((x, y)) # 분배해주기 위함
    union[x][y] = index

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= N or union[nx][ny] != -1:
                continue
            
            diff = abs(graph[x][y] - graph[nx][ny])

            if diff >= L and diff <= R:
                queue.append((nx, ny))
                loc.append((nx, ny))
                union[nx][ny] = index
                sum += graph[nx][ny]
                cnt +=1
        
    for i, j in loc:
        graph[i][j] = sum // cnt
    return



while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    
    if index == N*N:
        break
    answer += 1

print(answer)