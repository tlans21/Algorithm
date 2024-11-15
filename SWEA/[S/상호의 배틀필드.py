dx = [-1, 1, 0, 0] # 상 하 좌 우 
dy = [0, 0, -1, 1]

action = ['U', 'D', 'L', 'R', 'S'] # 상 하 좌 우 슛
direction_list = ['^', 'v', '<', '>'] 


def check():
    for h in range(H):
        for w in range(W):
            for k in range(4):
                if board[h][w] == direction_list[k]:
                    return h, w, direction_list[k]


T = int(input())

for tc in range(1, T + 1):
    board = []
    H, W = map(int, input().split())
    
    for _ in range(H):
        board.append(list(map(str, input())))

    N = int(input())
    command_list = input()

    for command in command_list:
        x, y, direction = check()
        if command == 'S':
            # 슛을 쏠때 현재 방향을 알아야한다.
            # 강철 벽과 벽일때 
            for i in range(4):
                if direction_list[i] == direction:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    while(0 <= nx < H and 0 <= ny < W):
                        if board[nx][ny] == '*':
                            board[nx][ny] = '.'
                            break
                        elif board[nx][ny] == '#':
                            break

                        nx += dx[i]
                        ny += dy[i]
        else: 
            # move 현재 위치를 알아야 이동할 수 있다.
            for i in range(4):
                if command == action[i]:
                   
                    #현재 위치를 기준으로 더한다.
                    nx = x + dx[i]
                    ny = y + dy[i]
                   
                    if 0 <= nx < H and 0 <= ny < W:
                        if board[nx][ny] == '.': # 평지만 이동 가능
                           board[nx][ny] = direction_list[i]
                           board[x][y] = '.'
                        else: # 평지가 아니어도 방향은 바꿔야한다.
                            board[x][y] = direction_list[i]
                    else:
                       # 맵 바깥으로 이동하려고 해도 방향은 바꿔야한다.
                       board[x][y] = direction_list[i]
    cnt = 0
    for board_str in board:
        if cnt == 0:
            print("#{} {}".format(tc,''.join(board_str)))
        else:
            print(''.join(board_str))
        cnt += 1
                                   