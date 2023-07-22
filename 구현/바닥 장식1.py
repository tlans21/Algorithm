N, M = map(int, input().split())

board = []

for i in range(N):
    board.append(list(map(str, input())))

cnt = 0

for i in range(N):
    pre_value = ''
    for j in range(M):
        if board[i][j] == '-':
            if board[i][j] != pre_value:
                cnt+=1
        pre_value = board[i][j]

for j in range(M):
    pre_value = ''
    for i in range(N):
        if board[i][j] == '|':
            if board[i][j] != pre_value:
                cnt+=1
        pre_value = board[i][j]

print(cnt)        