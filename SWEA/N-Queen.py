
def dfs(depth, col):
    global answer
    # 퀸 N개를 놓아야함
    n = len(col) - 1
    
    
    if promising(depth, col):
        if n == depth:
            answer += 1
            return
        else:
            for s in range(1, n + 1):
                col[depth + 1] = s 
                dfs(depth + 1, col)
    # 같은 열, 같은 행 

def promising(depth, col):
    k = 1
    flag = True
    while(k < depth and flag):
        if col[k] == col[depth] or abs(col[k] - col[depth]) == abs(k - depth):
            flag = False
        k += 1

    return flag
    



            


            

T = int(input())

for tc in range(1, T+1):
    answer = 0
    N = int(input())
    # N * N 보드 생성
    col = [0] * (N+1)
    
    dfs(0, col)
    print("#{} {}".format(tc, answer))