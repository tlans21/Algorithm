T = int(input())

def dfs(x, y, depth, dir):
    if depth == 5:
        return True
    if 0 <= x < N and 0 <= y < N:
        if dir == 0:
            if board[x][y] == 'o':
                return dfs(x + 1, y, depth + 1, dir)
            else:
                return False
        elif dir == 1:
            if board[x][y] == 'o':
                return dfs(x, y + 1, depth + 1, dir)
            else:
                return False
        elif dir == 2:
            if board[x][y] == 'o':
                return dfs(x + 1, y + 1, depth + 1, dir)
            else:
                return False
        elif dir == 3:
            if board[x][y] == 'o':
                return dfs(x+1, y-1, depth + 1, dir)
            else:
                return False
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    answer = "NO"
    breakFlag = False
    for i in range(N):
        for j in range(N):
            result_1 = dfs(i, j, 0, 0)
            if result_1 == True:
                answer = "YES"
                breakFlag = True
                break                
            result_2 = dfs(i, j, 0, 1)
            if result_2 == True:
                answer = "YES"
                breakFlag = True
                break          
                
            result_3 = dfs(i, j, 0, 2)
            if result_3 == True:
                answer = "YES"
                breakFlag = True
                break          
                
            result_4 = dfs(i, j, 0, 3)
            if result_4 == True:
                answer = "YES"
                breakFlag = True
                break          

        if breakFlag == True:
            break

    print("#{} {}".format(tc, answer))