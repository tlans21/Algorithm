def dfs(idx, sum):
    global answer
    
    if K == sum:
        answer += 1
        
        return
    
    if idx == N:
        return
    
    # 해당 숫자를 집합에 포함한 상태로 깊이 높아짐.
    dfs(idx + 1, sum + number[idx])
    # 해당 숫자를 집합에 포함하지 않은 상태로 깊이 높아짐.
    dfs(idx + 1, sum)
        

T = int(input())

for tc in range(1, T + 1):
    answer = 0
    N, K = map(int, input().split())
    number = list(map(int, input().split()))
    dfs(0, 0)
    print("#{} {}".format(tc, answer))    

