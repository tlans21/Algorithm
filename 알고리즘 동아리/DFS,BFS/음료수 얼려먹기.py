from collections import deque

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, x, y, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx <= -1 or ny <= -1 or nx >= N or ny >= M):
                continue
            if visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))


graph = [] #1차원 배열 생성
visited = [[False] * M for _ in range(N)]
visited.append(list)
for i in range(N):
    graph.append(list(map(int, input())))

cnt = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j] == 0:
            bfs(graph, i, j, visited)
            cnt = cnt +1

print(cnt)



