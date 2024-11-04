# 제한 시간 2초, 즉 2억번 연산안에 해결
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global answer
    
    if dp[x][y] != -1:
        return dp[x][y] # 현재 dp가 방문 되어있다면, 진행을 멈추고 기존 dp값을 사용한다. 왜냐하면 1이랑 같거나 무조건 크기 때문에

    dp[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] > board[x][y]: # 옮긴 지역은 그 전 지역보다 많이 있어야함.
                count = 1 # 현재 방문 거리
                count += dfs(nx, ny) 
                dp[x][y] = max(dp[x][y], count)
                answer = max(answer, dp[x][y])            
    return dp[x][y]

n = int(input())
max_cnt = 0
board = []
dp = [[-1 for _ in range(n)] for _ in range(n)]
# 많이 먹는게 중요한게 아님, 어떻게 해야 최대 칸을 이동 할지가 중요한거임.
for i in range(n):
    board.append(list(map(int, input().split())))

answer = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dfs(i, j)

# 최악의 경우 4*N이다. dfs가 4*N의 깊이로 진행이 된다면
# visited로 인해서 외부 for 루프가 한번 밖에 실행이 되지 않기 때문이다

print(answer)