import sys
def checkRow(x, a):
    for i in range(9):
        if a == board[x][i]:
            return False    
    return True

def checkColumn(y, a):
    for i in range(9):
        if a == board[i][y]:
            return False
    return True

def checkSquare(x, y, a):
    nx = (x//3) * 3
    ny = (y//3) * 3
    
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j] == a:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()
        exit()

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        
        if checkColumn(x, i) and checkRow(y, i) and checkSquare(x, y, i):
            board[x][y] = i
            dfs(idx+1)
            board[x][y] = 0

board = [list(map(int, input())) for _ in range(9)]

blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))
        
dfs(0)

