def dfs(depth, cnt, color):
    global minValue
    
    if depth == N:
        if color == 'R':
            minValue = min(minValue, cnt)
        return
    draw = 0
    
    if color == 'W':
        for i in range(M):
            if flag[depth][i] != 'W':
                draw += 1
        dfs(depth + 1, cnt + draw, 'W') # 하얀색 칠하기
        

        # 흰색에서 파란색 칠하기
        if depth > 0:
            draw = 0
            for i in range(M):
                if flag[depth][i] != 'B':
                    draw +=1
            dfs(depth + 1, cnt + draw, 'B')
            

    elif color == 'B':
        #파란색에서 파란색 칠하기
        for i in range(M):
            if flag[depth][i] != 'B':
                draw +=1
        dfs(depth + 1, cnt + draw, 'B')
        
        
        # 파란색에서 빨간색 칠하기
        if depth > 0:
            draw = 0
            for i in range(M):
                if flag[depth][i] != 'R':
                    draw +=1
            dfs(depth + 1, cnt + draw, 'R')
            

    elif color == 'R':
        # 빨간색에서 빨간색 칠하기
        for i in range(M): 
            if flag[depth][i] != 'R':
                draw += 1
        dfs(depth + 1, cnt + draw, 'R')
        draw = 0
    



T = int(input())

for tc in range(1, T+1):
    N, M  = map(int, input().split())
    minValue = 123456789
    flag = [list(map(str, input())) for _ in range(N)]
    dfs(0, 0, 'W')
    print("#{} {}".format(tc, minValue))
    
            

    
        