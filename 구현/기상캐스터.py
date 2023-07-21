H, W = map(int, input().split())

# H 세로, W 가로

board = []

for i in range(H):
    board.append(list(map(str, input())))

answer = [[-1 for j in range(W)] for i in range(H)]

flag = False

for i in range(H):
    flag = False
    for j in range(W):
        if board[i][j] == 'c':
            answer[i][j] = 0
            flag = True
            cnt = 0
        else:
            if flag == True:
                cnt +=1
                answer[i][j] = cnt

for i in range(H):
    for j in range(W):
        print(answer[i][j], end=' ')
    print()

