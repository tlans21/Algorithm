T = int(input())


for s in range(1, T+1):
    answer = []
    N, Q = map(int, input().split())
    
    for k in range(0, N+1):
        answer.append(str(0))
        
    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        for j in range(L, R+1):
            answer[j] = str(i)
        
    print(f"#{s}", end = " ")
    print(" ".join(answer[1:]))


    
