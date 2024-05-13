T = 10
N = 100

def dfs(x, y, board, depth, target, visited):
    visited[x][y] = True
    # 종료 조건
    if x == target - 1:
        # X -> N이 되었을 때의 depth 길이
        return depth
    
    if 0 <= y + 1 < N and board[x][y + 1] and not visited[x][y + 1]:
        return dfs(x, y + 1, board, depth + 1, target, visited)   
    elif 0 <= y - 1 < N and board[x][y - 1] and not visited[x][y - 1]:
        return dfs(x, y - 1, board, depth + 1, target, visited)
    elif 0 <= x + 1 < N and board[x + 1][y] and not visited[x + 1][y]:
        return dfs(x + 1, y, board, depth + 1, target, visited)


for tc in range(1, T+1):
    a = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_value = []
    for i in range(N):
        visit = [[False for _ in range(N)] for _ in range(N)]
        if board[0][i] == 1:
            depth_value = dfs(0, i, board, 0, N, visit)
            depth_idx = i
            min_value.append((depth_value, depth_idx))
    
    answer, answerIdx = min(min_value)
    print("#{} {}".format(a, answerIdx))    
