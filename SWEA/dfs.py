import sys

N = 100
def dfs(x, y, depth, board, visited):
    
    visited[x][y] = True
    # 좌우 확인
    if 0 < y + 1 < N and board[x][y+1] and not visited[x][y+1]:
        if dfs(x, y + 1, depth + 1, board, visited) == True:
            return True
        elif dfs(x, y + 1, depth + 1, board, visited) == False:
            visited[x][y+1] = False
    elif 0 < y - 1 < N and board[x][y-1] and not visited[x][y-1]:
        if dfs(x, y - 1, depth + 1, board, visited) == True:
            return True
        elif dfs(x, y - 1, depth + 1, board, visited) == False:
            visited[x][y-1] = False
    elif 0 < x + 1 < N and board[x+1][y] and not visited[x+1][y]:
        if board[x+1][y] == 1:
            if dfs(x + 1, y, depth + 1, board, visited) == True:
                return True
            elif dfs(x + 1, y, depth + 1, board, visited) == False:
                visited[x + 1][y] = False
        elif board[x+1][y] == 2:
            return True
    return False


T = 10

for k in range(1, T+1):
    visit = [[False for _ in range(N)] for k in range(N)]
    a = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        visit = [[False for _ in range(N)] for k in range(N)]
        if board[0][i] == 1:
            if dfs(0, i, 0, board, visit) == True:
                answer = i
                break
    print("#{} {}".format(a, answer))


