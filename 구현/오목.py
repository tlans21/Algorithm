board = []

#하, 우, 우상, 우하, 
dx = [1, 0, -1, 1]
dy = [0, 1, 1, 1]
for i in range(19):
    board.append(list(map(int, input().split())))

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            
            first = board[i][j]

            for k in range(4):
                x, y = i, j
                
                cnt = 1

                nx = x + dx[k]
                ny = y + dy[k]

                while 0 <= nx <= 18 and 0 <= ny <= 18 and first == board[nx][ny]:
                    cnt +=1
                    

                    if cnt == 5:     
                        # 6목인 경우
                        if 0 <= x-dx[k] <= 18 and 0 <= y-dy[k] <= 18 and board[x-dx[k]][y-dy[k]] == first:
                            break
                        if 0 <= nx+dx[k] <= 18 and 0 <= ny+dy[k] <= 18 and board[nx+dx[k]][ny+dy[k]] == first:
                            break

                        print(first)
                        print(x + 1, y + 1)                        
                        exit(0)
                    nx += dx[k]
                    ny += dy[k]
print(0)
                
            
                         
                
                      