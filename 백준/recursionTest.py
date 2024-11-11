def dfs(depth):
    if depth == 10:
        return 1
    
    cnt = 0

    cnt += (dfs(depth + 1) + 1)
    print(cnt)
    return cnt 



answer = dfs(0)

print(answer)
