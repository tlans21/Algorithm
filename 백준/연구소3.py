from itertools import combinations
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(board, combi_lst, empty_cnt):
    global answer
    temp_board = [[board[i][j] for j in range(N)] for i in range(N)]
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    
    queue = []
    
    for i in range(M):
        (x, y) = combi_lst[i]
        queue.append((x, y))
        visited[x][y] = 1
    cnt_val = 0
    while queue:
        if not empty_cnt:
            break
        

        cnt_val += 1
        for _ in range(len(queue)):
            nowX, nowY = queue.pop(0)
            for i in range(4):
                nextX = nowX + dx[i]
                nextY = nowY + dy[i]
                if 0 <= nextX < N and 0 <= nextY < N:
                    if visited[nextX][nextY] == -1 and temp_board[nextX][nextY] == 0:
                        visited[nextX][nextY] = 1
                        empty_cnt -= 1
                        queue.append((nextX, nextY))
                    elif visited[nextX][nextY] == -1 and temp_board[nextX][nextY] == 2:
                        visited[nextX][nextY] = 1
                        queue.append((nextX, nextY))

    if not empty_cnt:
        return cnt_val
    else:
        return 1e9
    

answer = 1e9
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
loc_lst = []

empty_cnt = 0
combi_lst = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            loc_lst.append([i, j])
        if board[i][j] == 0:
            empty_cnt += 1

for virus in combinations(loc_lst, M):
    answer = min(answer, bfs(board, virus, empty_cnt))

if answer == 1e9:
    print(-1)
else:
    print(answer)
