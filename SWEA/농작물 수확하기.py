T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    height = N // 2
    sum = 0

    for i in range(N):
        sum += int(board[N//2][i])

    for i in range(1, height + 1):
        for j in range(i, N-i):
            sum += int(board[(N // 2) - i][j])

    for i in range(1, height + 1):
        for j in range(i, N-i):
            sum += int(board[(N // 2) + i][j])

    print("#{} {}".format(tc, sum))