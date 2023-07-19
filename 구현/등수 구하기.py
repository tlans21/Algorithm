N, new, P = map(int, input().split())



if N == 0:
    print(1)
elif N > 0:
    score_board = list(map(int, input().split()))

    if N == P and score_board[-1] >= new:
        print(-1)
    else:
        rank = N + 1
        for i in range(N):
            if score_board[i] <= new:
                rank = i + 1
                break
        print(rank)
        
                


