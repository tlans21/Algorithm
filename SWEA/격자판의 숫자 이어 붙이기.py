dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, boardString):
    global answer
    if depth == 6:
        answer.add(boardString)
        return
    
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, depth + 1, boardString + board[nx][ny])



T = int(input())

for tc in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, board[i][j])

    
    print("#{} {}".format(tc, len(answer)))