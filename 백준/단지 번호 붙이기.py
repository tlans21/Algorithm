# 1은 집이 있는 곳, 0은 없는 곳
# 연결된 집의 모임인 단지로 정의하고 단지에 번호 붙임.
# 연결은 상하좌우를 뜻함.


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and board[nx][ny] == '1':
                cnt += 1
                dfs(nx, ny)




N = int(input())

board = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(str, input())))

answer_list = []

for i in range(N):
    for j in range(N):
        cnt = 1
        if visited[i][j] == 0 and board[i][j] == '1':
            dfs(i, j)
            answer_list.append(cnt)


# 출력

# 총 단지수
answer_list.sort()


print(len(answer_list))
for answer in answer_list:
    print(answer)