

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # ex) board[0][2] 1번 사람이 3번 일을 성공확률
    for i in range(N):
        for j in range(N):
            percentage = board[i][j]

    

