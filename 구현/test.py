board = [list(map(int, input())) for _ in range(9)]


for i in range(9):
    print(*board[i])