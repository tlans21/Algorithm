min_value = 123456789
#bfs 풀이 방식

def bfs(x, y, board, visited):
    global min_value
    queue = []
    queue.append([x, y, 0])
    visited[x][y] = 1
    while queue:
        nowX, nowY, nowCnt = queue.pop(0)
        for k in range(4):
            nextCnt = nowCnt + 1
            nextX, nextY = move(nowX, nowY, k, board)
            if board[nextX][nextY] == '.' and visited[nextX][nextY] == 0:
                visited[nextX][nextY] = 1
                queue.append([nextX, nextY, nextCnt])
            elif board[nextX][nextY] == 'G':
                min_value = min(min_value, nextCnt)

def move(x, y, dir, board):
    # 왼쪽
    if dir == 0:
        while y > 0 and board[x][y - 1] != 'D':
            y-=1
            
    # 오른쪽
    elif dir == 1:
        while 0 <= y < len(board[x]) - 1 and board[x][y + 1] != 'D':
            y += 1
    # 아래쪽
    elif dir == 2:
        while 0 <= x < len(board) - 1 and board[x + 1][y] != 'D':
            x += 1
    # 위쪽
    elif dir == 3:
        while x > 0 and board[x-1][y] != 'D':
            x -= 1
    
    return x, y
    

def solution(board):
    answer = 0
    visited = [[0 for j in range(len(board[i]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                bfs(i, j, board, visited)
    answer = min_value
    if answer == 123456789:
        return -1
    return answer