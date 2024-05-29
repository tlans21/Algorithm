def dfs(y, depth, per, visited):
    global max_value
    if depth == N-1:
        value = 1
        for i in range(len(per)):
            value *= per[i] / 100
       
        value = value * 100
        max_value = max(max_value, value)
        return

    

    for ny in range(N):
        if visited[ny] == 0:
            visited[ny] = 1
            per.append(board[depth + 1][ny])
            dfs(ny, depth + 1, per, visited)
            per.pop()
            visited[ny] = 0
        
T = int(input())

for tc in range(1, T+1):
    max_value = -1
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # ex) board[0][2] 1번 사람이 3번 일을 성공확률
    for i in range(N):
        percentage = []
        visit = [0 for _ in range(N)]
        percentage.append(board[0][i])
        visit[i] = 1
        dfs(i, 0, percentage, visit)
        visit[i] = 0
    print("#{} {:.6f}".format(tc, round(max_value, 6)))
    

