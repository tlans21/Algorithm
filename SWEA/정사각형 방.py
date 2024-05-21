dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, depth):
    global answer
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if board[x][y] + 1 == board[nx][ny]:
                return dfs(nx, ny, depth + 1)
    return depth + 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = 0
    answer_lst = []
    board = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            tempDepth = dfs(i, j, 0)
            answer_lst.append((tempDepth, board[i][j]))

    sort_answerLst = sorted(answer_lst, key=lambda x: (x[0], -x[1]))
    answer_num = sort_answerLst[-1][1]
    answer_depth = sort_answerLst[-1][0]
    
    print("#{} {} {}".format(tc, answer_num, answer_depth))
