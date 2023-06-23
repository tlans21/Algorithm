N = int(input())

board = [[0 for j in range(101)] for i in range(101)]
sum = 0
for i in range(N):
    x, y= list(map(int, input().split()))

    for j in range(x, x+10):
        for k in range(y, y+10):
            if board[k][j] == 0:
                board[k][j] = 1

for s in board:
    for d in s:
        if d == 1:
            sum += 1
print(sum)


    