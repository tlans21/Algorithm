import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, element):
    visited[x][y] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and board[nx][ny] > element:
                dfs(nx, ny, element)


N = int(input())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

setStore = set()
for i in range(N):
    for j in range(N):
        setStore.add(board[i][j])

answer = 0

for setElement in setStore:
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)] 
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j] > setElement:
                dfs(i, j, setElement) # 안전 지대 만들기
                cnt += 1
    answer = max(answer, cnt)

# 예외 케이스 : 아무 지역도 물에 잠기지 않을 수 있다. 이 말은 맵 전체가 안전지대이다.
if answer == 0:
    print(1)
else:
    print(answer)
