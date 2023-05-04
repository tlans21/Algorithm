from collections import deque

N, K = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
data = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        #바이러스 데이터 저장, 바이러스 종류, 시간, 위치 X, 위치 Y값 저장
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort() # 문제에서 번호가 낮은 순으로 먼저 전염된다고하므로 낮은순이 가장 앞에오도록 하기위함

queue = deque(data)

target_S, target_X, target_Y = map(int, input().split())


while queue:
    virus, S, X, Y = queue.popleft()
    if S == target_S:
        break
    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((virus, S+1, nx, ny))

print(graph[target_X-1][target_Y-1])



#