

N = 100
def dfs(x, y, board, depth):
    
    if 0 < x + 1 < N:
        # 내려가기 이전에 왼쪽 오른쪽이 있는지 확인한다.
        if 0 < y + 1 < N:
            if board[x][y+1] == 1:
                dfs(x, y+1, board, depth + 1)
            elif board[x][y+1] == 0 and board[x][y-1] == 0:
                if board[x + 1][y] == 1:
                    dfs(x + 1, y, board, depth + 1)
                elif board[x + 1][y] == 2:
                    return True  
        if 0 < y - 1 < N:
            if board[x][y-1] == 1:
                dfs(x, y-1, board, depth + 1)
            elif board[x][y+1] == 0 and board[x][y-1] == 0:
                if board[x + 1][y] == 1:
                    dfs(x + 1, y, board, depth + 1)
                elif board[x + 1][y] == 2:
                    return True
    return False




    
    return False


T = int(input())

for i in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(100)]
    for j in range(0, 100):
        if board[0][j] == 1:
            result = dfs(0, j, board, 0)
            if result == True:
                print(j)