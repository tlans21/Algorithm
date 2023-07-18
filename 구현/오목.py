board = []

# 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
for i in range(19):
    board.append(list(map(int, input().split())))

for i in range(19):
    for j in range(19):
        for k in range(8):
            x, y = i, j
            cnt = 0    
            for s in range(5):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx <= 18 and 0 <= ny <= 18:
                    if board[x][y] == board[nx][ny]:
                        cnt +=1
                    else:
                        break
                    x = nx 
                    y = ny
                else:
                    continue
            if cnt == 5:
                if board[i][j] == 1:
                    print(1)
                    print(i, j)
                    exit(0)
                elif board[i][j] == 2:
                    print(2)
                    print(i, j)
                    exit(0)

                         
                
                      