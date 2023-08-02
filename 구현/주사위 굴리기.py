N, M, x, y, K = map(int, input().split())

board = []

dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    board.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    #동
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    #서    
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    #북
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    #남
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

nx = x
ny = y
for command in commands:
    nx += dx[command-1]
    ny += dy[command-1]
    if 0 <= nx < N and 0 <= ny < M:
        x = nx
        y = ny
        turn(command)
        
        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1]
        
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0
        
        print(dice[0])

    else:
        nx -= dx[command-1]
        ny -= dy[command-1]
        continue


