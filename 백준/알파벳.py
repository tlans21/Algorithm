dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, recordLst):
    global answer
    if len(recordLst) == 26:
        answer = 26
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < R and 0 <= ny < C):
            if not (ord(board[nx][ny]) - ord('A') in recordLst):
                recordLst.append(ord(board[nx][ny]) - ord('A'))
                dfs(nx, ny, depth + 1, recordLst)
                recordLst.pop()
    answer = max(len(recordLst), answer)
    return


answer = 0
R, C = map(int, input().split())

board = [list(map(str, input())) for _ in range(R)]

dfs(0, 0, 0, [ord(board[0][0]) - ord('A')])
print(answer)