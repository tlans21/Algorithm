dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = []

    queue.append((x, y))

    while queue:
        nowX, nowY = queue.pop(0)
        cnt = 0
        for k in range(4):
            nextX = x + nowX
            nextY = y + nowY
            if 0 <= nextX < N and 0 <= nextY < M:
                if board[nextX][nextY] == 0:
                    cnt += 1 # 바닷물 타일 갯수
                elif board[nextX][nextY] and visited[nextX][nextY] == 0:
                    visited[nextX][nextY] = 1
                    queue.append((nextX, nextY))
        
        board[nowX][nowY] = board[nowX][nowY] - cnt # 수정
        




N, M = map(int, input().split())

board = []
visited = [[0 for _ in range(M)] for _ in range(N)] 
for _ in range(N):
    board.append(list(map(int, input().split())))



# 너비 우선 탐색을 진행한다.


bfs(i, j)

