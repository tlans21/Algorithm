board = [[0 for j in range(101)] for _ in range(101)]

sum = 0
for i in range(4):
    x, y, x1, y1 = map(int, input().split())

    for i in range(x, x1):
        for j in range(y, y1):
            if board[i][j] == 0:
                board[i][j] = 1
                sum +=1
            elif board[i][j] == 1:
                continue

print(sum)