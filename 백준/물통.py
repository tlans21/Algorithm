def dfs(a, b, c):
    if a == 0:
        answer.append(c) # A물통이 비어있을 때, 값 저장

    # C -> A
    if c > 0 and a < A: # c의 물이 있으면서, a의 용량이 물통을 넘지 않아야함.
        tmp1 = a
        tmp3 = c 
        while tmp3 > 0 and tmp1 < A:
            tmp3 -= 1 # c의 용량이 줄어들고
            tmp1 += 1 # a의 용량이 증가한다.
        if [tmp1, b, tmp3] not in save: 
            save.append([tmp1, b, tmp3])
            dfs(tmp1, b, tmp3)
    
    # C -> B

    if c > 0 and b < B:
        tmp2 = b
        tmp3 = c
        while tmp3 > 0 and tmp2 < B:
            tmp3 -= 1
            tmp2 += 1
        if [a, tmp2, tmp3] not in save:
            save.append([a, tmp2, tmp3])
            dfs(a, tmp2, tmp3)

    # B -> C

    if b > 0 and c < C:
        tmp2 = b 
        tmp3 = c
        while tmp2 > 0 and tmp3 < C:
            tmp2 -= 1
            tmp3 += 1
        if [a, tmp2, tmp3] not in save:
            save.append([a, tmp2, tmp3])
            dfs(a, tmp2, tmp3)
    # B -> A
    
    if b > 0 and a < A:
        tmp1 = a
        tmp2 = b
        while tmp2 > 0 and tmp1 < A:
            tmp2 -= 1
            tmp1 += 1
        if [tmp1, tmp2, c] not in save:
            save.append([tmp1, tmp2, c])
            dfs(tmp1, tmp2, c)
    
    # A -> B
    if a > 0 and b < B:
        tmp1 = a
        tmp2 = b 
        while tmp1 > 0 and tmp2 < B:
            tmp1 -= 1
            tmp2 += 1
        if [tmp1, tmp2, c] not in save:
            save.append([tmp1, tmp2, c])
            dfs(tmp1, tmp2, c)
    
    # A -> C

    if a > 0 and c < C:
        tmp1 = a
        tmp3 = c
        while tmp1 > 0 and tmp3 < C:
            tmp1 -= 1
            tmp3 += 1
        
        if [tmp1, b, tmp3] not in save:
            save.append([tmp1, b, tmp3])
            dfs(tmp1, b, tmp3)

        
        



A, B, C = map(int, input().split())
answer = []
save = []
save.append([0, 0, C])
dfs(0, 0, C)


answer.sort()

print(*answer)