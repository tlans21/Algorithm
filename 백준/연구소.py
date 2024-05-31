dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board):
    global maxValue
    queue = []
    temp_board = [[board[i][j] for j in range(M)] for i in range(N)]
    
    for i in range(N):
        for j in range(M):
            if temp_board[i][j] == 2:
                queue.append((i, j))

    cnt = 0
    while queue:
        nowX, nowY = queue.pop(0)
        if temp_board[nowX][nowY] != 2:
            continue

        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < M:
                # board :0은 빈칸, 1은 벽, 2는 전염병
                if temp_board[nextX][nextY] == 0:
                    temp_board[nextX][nextY] = 2
                    queue.append((nextX, nextY))

    for k in range(N):
        for s in range(M):
            if temp_board[k][s] == 0:
                cnt += 1
    maxValue = max(maxValue, cnt)
    return

def permutation(cnt, board):
    # 벽 3개
    if cnt == 3:
        bfs(board)
        return
    # 벽 세우기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                permutation(cnt + 1, board)
                board[i][j] = 0

    return

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
# 3칸 넣기
boardCopy = [[0 for _ in range(M)] for _ in range(N)]

maxValue = -1

for i in range(N):
    for j in range(M):
        boardCopy[i][j] = board[i][j]

permutation(0, boardCopy)

print(maxValue)
