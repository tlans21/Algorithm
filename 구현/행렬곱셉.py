N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

M, K = map(int, input().split())

arr1 = []
for i in range(M):
    arr1.append(list(map(int, input().split())))

board = [[0 for j in range(K)] for i in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            board[i][j] += arr[i][k] * arr1[k][j]

for i in board:
    for j in i:
        print(j, end = ' ')
    print()