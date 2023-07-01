N = int(input())

S = list(map(int ,input().split()))

lst = [0] * N

for i in range(1, N+1):
    num = S[i-1]
    cnt = 0
    for j in range(N):
        if num == cnt and lst[j] == 0:
            lst[j] = i
            break
        elif lst[j] == 0:
            cnt += 1
    
print(*lst)
