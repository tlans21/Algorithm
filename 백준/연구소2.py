# 빈칸 0, 벽은 1, 바이러스 2
# 바이러스는 M개를 놓아야함.
from itertools import combinations
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, visited, lst):
    queue = []
    time_board = [[-1 for _ in range(N)] for _ in range(N)]
    temp_board = [[board[i][j] for j in range(N)] for i in range(N)]
    temp_visited = [[visited[i][j] for j in range(N)] for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            # 바이러스면
            if temp_board[i][j] == 2 and temp_visited[i][j] == 1:
                time_board[i][j] = 0
                queue.append((i, j, 0))
    
    while queue:
        nowX, nowY, nowTime = queue.pop(0)
        
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N:
                if temp_board[nextX][nextY] != 1 and time_board[nextX][nextY] == -1:
                    nextTime = nowTime + 1
                    time_board[nextX][nextY] = nextTime
                    temp_board[nextX][nextY] = 2
                    queue.append((nextX, nextY, nowTime + 1))

    result = 0
    for i in range(N):
        for j in range(N):
            if temp_board[i][j] == 0 and visited[i][j] == -1:
                return -1
            result = max(result, time_board[i][j])

    return result


def permutation(board, visited):
    global min_time
    global trigger
    
    
    combi = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                combi.append([i, j])   
    combi_lst = list(combinations(combi, M))

    for lst in combi_lst:
        bfs(board, visited, lst)
    
    return



N, M = map(int, input().split())
trigger  = 1
board = [list(map(int, input().split())) for _ in range(N)]
min_time = 123456789
visited = [[0 for _ in range(N)] for _ in range(N)]
permutation(board, visited)



