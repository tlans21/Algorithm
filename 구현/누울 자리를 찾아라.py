N = int(input())

board = [list(input()) for _ in range(N)]

row = 0
for i in range(0, N):
    cnt = 0
    for j in range(0, N):
        if board[i][j] == '.' :
           cnt += 1
        elif board[i][j] == 'X':
            if cnt >=2 :
                row +=1
            cnt = 0
    if cnt >= 2:
        row +=1


column = 0
for i in range(0, N):
    cnt1 = 0
    for j in range(0, N):
        if board[j][i] == '.':
            cnt1 +=1
        elif board[j][i] == 'X':
            if cnt1 >= 2:
                column +=1
            cnt1 = 0

    if cnt1 >= 2:
        column +=1

print(row, column)
