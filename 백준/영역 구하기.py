import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt 
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N:
            if board[nx][ny] == 0 and visited[nx][ny] == 0: # 색칠 안된 공간으로 깊이 진행하도록 함.
                cnt += 1
                dfs(nx, ny)


cnt = 0
M, N, K = map(int, input().split()) # M은 세로, N은 가로 
visited = [[0 for _ in range(N)] for _ in range(M)]
board = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split()) # y는 세로, x는 가로
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1
# 1은 색칠된 공간

answer = 0
answer_store = []
for i in range(M): 
    for j in range(N):
        cnt = 1 # 제일 초기 재귀의 경우 cnt를 세어주지 않기 때문에 함수 외부에서 미리 카운트시킴.
        if board[i][j] == 0 and visited[i][j] == 0: # 색칠 안된 공간 dfs 시행과 깊이 진행이 안되어있는 곳으로
            dfs(i, j)
            answer_store.append(cnt)
            answer += 1
answer_store.sort() # 오름 차순 정렬
print(answer)
print(*answer_store)
