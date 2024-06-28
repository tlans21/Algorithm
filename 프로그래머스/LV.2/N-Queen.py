answer = 0
def dfs(depth, col, n):
    global answer
    if promising(depth, col): #현재 상태를 점검해서 놓을지 안놓을지 정한다.
        if n == depth:
            answer +=1
            return
        else:
            # 순열 1 1 1 1, 1 1 1 2, 1 1 1 3, 1 1 1 4, 1 1 2 1.. 4 4 4 3 4 4 4 4
            for k in range(1, n+1):
                col[depth + 1] = k
                dfs(depth + 1, col, n)

def promising(depth, col):
    k = 1
    flag = True
    while k < depth and flag:
        if col[k] == col[depth] or abs(col[k] - col[depth]) == abs(k - depth): 
            flag = False
        k += 1
    
    return flag


def solution(n):
    col = [0] * (n+1)

    dfs(0, col, n)
    print(answer)
    return answer

solution(4)
