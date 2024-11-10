import sys
sys.setrecursionlimit(10**6)


dx = [-1, 1, 0, 0, 1, 1, -1, -1] 
dy = [0, 0, -1, 1, 1, -1, 1, -1]
def dfs(x, y):
    visited[x][y] = 1

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < h and 0 <= ny < w:
            if visited[nx][ny] == 0 and board[nx][ny] == 1: # 방문안한 육지라면 이동
                dfs(nx, ny)



while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for _ in range(h):
        board.append(list(map(int, input().split())))
    # 0은 바다, 1은 땅
    island_cnt = 0
    # 섬의 개수는 ? 땅을 찾자.
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and board[i][j] == 1:
                dfs(i, j) # 방문안한 육지에 dfs 시행
                island_cnt += 1
    
    print(island_cnt)
