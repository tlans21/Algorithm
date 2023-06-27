import sys
sys.setrecursionlimit(10000)
N, L, R = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visit = [[0 for j in range(N)] for _ in range(N)]
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

def dfs(x, y, board):
    visit[x][y] = 1
    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx <N) and (0<=ny <N): 
            if visit[nx][ny] == 0 and (L <= (abs(board[x][y] - board[nx][ny])) <= R):
                loc.append((nx, ny))
                dfs(nx, ny, board)

    return loc

cnt = 0

while True:
    visit = [[0 for j in range(N)] for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            
            loc = [(i, j)]
            if visit[i][j] == 0:
                loc = dfs(i, j, board)                
            if len(loc) > 1:
                flag = True
                sum = 0
                for x, y in loc:
                    sum += board[x][y]
                avg = sum // len(loc)
                for s, k in loc:
                    board[s][k] = avg
    
    if not flag:
        print(cnt)
        break
    cnt +=1
