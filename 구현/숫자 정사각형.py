N, M = map(int, input().split())

board = [list((input())) for _ in range(N)]

def check(x, y):
    #꼭짓점 체크
    max_num = 0
    cnt = 0
    while x + cnt < N and y + cnt < M:
        if board[x][y] == board[x+cnt][y] and board[x][y] == board[x][y+cnt] and board[x][y] == board[x+cnt][y+cnt]:
            max_num = max(max_num, (cnt+1)*(cnt+1))
        cnt += 1
    return max_num
# 0, 0 부터 완전탐색
answer = 0
for i in range(N):
    for j in range(M):
        temp = check(i, j)
        answer = max(temp, answer)

print(answer)