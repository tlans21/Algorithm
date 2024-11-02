# 나의 병사는 하얀색 옷, 적의 병사는 파란 색 옷을 입는다.
# 같은 팀의 병사가 모일수록 강해진다.
# N명이 뭉쳐있을땐 N^2의 힘을 낸다.
# 대각선은 인접하다고 보지않는다.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, board, visited):
    visited[x][y] = 1
    global cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < M and 0 <= ny < N):
            if(visited[nx][ny] == 0 and board[x][y] == board[nx][ny]):
                cnt += 1
                dfs(nx, ny, board, visited)
                
    


N, M = map(int, input().split())

board = []
visited = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(M):
    board.append(list(map(str, input())))

cnt = 1
w_cnt = 0
b_cnt = 0

for i in range(M):
    for j in range(N):
        cnt = 1
        if visited[i][j] == 0:
            # 하얀색팀 즉 나의팀이면
            if board[i][j] == 'W':
                dfs(i, j, board, visited)
                w_cnt += (cnt**2)
            elif board[i][j] == 'B':
                dfs(i, j, board, visited)
                b_cnt += (cnt**2)

print(w_cnt, b_cnt)

    