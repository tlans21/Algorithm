
def dfs(x, y, depth, state):
    if depth == N:
        return
    action = commend[depth]
    
    if action == 'U':
        nx = x - 1
        ny = y
        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] == '.': # 평지라면 이동이 가능 그외에 경우 이동 불가
                board[x][y] = '.'
                board[nx][ny] = '^'
                dfs(nx, ny, depth + 1, "up")
    elif action == "D":
        nx = x + 1
        ny = y
        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] == '.': # 평지라면 이동이 가능 그외에 경우 이동 불가
                board[x][y] = '.'
                board[nx][ny] = 'v'
                dfs(nx, ny, depth + 1, "down")
    elif action == "L":
        nx = x 
        ny = y - 1
        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] == '.': # 평지라면 이동이 가능 그외에 경우 이동 불가
                board[x][y] = '.'
                board[nx][ny] = '<'
                dfs(nx, ny, depth + 1, "left")
    elif action == "R":
        nx = x
        ny = y + 1
        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] == '.': # 평지라면 이동이 가능 그외에 경우 이동 불가
                board[x][y] = '.'
                board[nx][ny] = '>'
                dfs(nx, ny, depth + 1, "right")
    elif action == "S":
        if state == "up":  #바라보는 현재 방향 제어
            tmp1 = 1
            while 0 <= x < H:
                nx = x - tmp1
                if board[nx][y] == '*': # 벽돌 벽이라면 부서지고 평지가 됨
                    board[nx][y] = '.'
                    break
                elif board[nx][y] == '#':
                    break
                tmp1 += 1 
            # 현재 위치를 고정한채 dfs 깊이 증가
            dfs(x, y, depth + 1, "up")
        elif state == "down":
            tmp1 = 1
            while 0 <= x < H:
                nx = x + tmp1
                if board[nx][y] == "*":
                    board[nx][y] = '.'
                    break
                elif board[nx][y] == '#':
                    break
                tmp1 += 1 
            dfs(x, y, depth + 1, "down")
        elif state == "left":
            tmp2 = 1
            while 0 <= y < W:
                ny = y - tmp2
                if board[x][ny] == "*":
                    board[x][ny] = '.'
                    break
                elif board[x][ny] == '#':
                    break
                tmp2 += 1
            dfs(x, y, depth + 1, "left")
        elif state == "right":
            tmp2 = 1
            while 0 <= y < W:
                ny = y + tmp2
                if board[x][ny] == '*':
                    board[x][ny] = '.'
                    break
                elif board[x][ny] == '#':
                    break
                tmp2 += 1
            dfs(x, y, depth + 1, "right")
    return


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())

    board = []
    for _ in range(H):
        board.append(list(map(str, input())))
    x = 0
    y = 0
    state = None
    for i in range(H):
        for j in range(W):
            if board[i][j] == '<':
                x = i
                y = j
                state = "left"
            elif board[i][j] == 'v':
                x = i
                y = j
                state = "down"
            elif board[i][j] == '>':
                x = i
                y = j
                state = "right"
            elif board[i][j] == '^':
                x = i
                y = j
                state = "up"
                               
    N = int(input())
    commend = list(map(str, input()))
    dfs(i, j, 0, state)

    print(board)

