def dfs(depth, cnt, R, B, W):
    global minValue
    print(depth)
    if W == 0:
        if R >= 1:
            return
        elif B >= 1:
            return
    
    if B == 0:
        if W == 0:
    
    if depth == N:
        if R == 0 or B == 0 or W == 0:
            return

        minValue = min(minValue, cnt)
        return minValue
    


    draw = 0
    for i in range(M):
        if flag[depth][i] != 'W':
            draw += 1
    dfs(depth + 1, cnt + draw, R, B, W + 1) # 하얀색 칠하기
    
    draw = 0
    for i in range(M):
        if flag[depth][i] != 'B':
            draw += 1
    dfs(depth + 1, cnt + draw, R, B + 1, W)
    
    draw = 0
    for i in range(M):
        if flag[depth][i] != 'R':
            draw += 1
    dfs(depth + 1, cnt + draw, R + 1, B, W)


T = int(input())

for tc in range(1, T+1):
    N, M  = map(int, input().split())
    minValue = 123456789
    flag = [list(map(str, input())) for _ in range(N)]
    dfs(0, 0, 0, 0, 0)
    print("#{} {}".format(tc, minValue))