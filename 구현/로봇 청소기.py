N, M = map(int, input().split())

board = []

a, b, d = map(int, input().split())

# d가  0 : 북쪽, 1 : 동쪽, 2 : 남쪽 , 3 : 서쪽
# d의 후진 d[0] 1 0, d[1] 0 1, d[2] -1 0, d[3] 0 -1

for i in range(N):
    board.append(list(map(int, input().split())))


# board == 0은 청소되지않은 빈칸, 1은 벽




dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
def dfs(x, y, d):
    global cnt
    if board[x][y] == 0:
        board[x][y] = 2
        cnt += 1

    #0, 3, 2, 1순으로 만들기.
    for _ in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        

        

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                dfs(nx, ny, d)
                return
    # 네 방향 모두 청소된 경우

    #후진
    if board[x-dx[d]][y-dy[d]] == 1:
        return
    else:
        dfs(x-dx[d], y-dy[d], d)

dfs(a, b, d)
print(cnt)
        








            



