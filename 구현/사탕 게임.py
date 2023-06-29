N = int(input())


candy = [list(input()) for _ in range(N)]



def check(candy):
    answer = 1
    for i in range(N):
        # i번째 행에서 열을 검사
        cnt = 1
        for j in range(1, N):
            if candy[i][j-1] == candy[i][j]:
                cnt +=1
            else:
                cnt = 1
            
            answer = max(answer, cnt)

        cnt = 1
        for k in range(1, N):
            if candy[k][i] == candy[k-1][i]:
                cnt +=1
            else:
                cnt = 1

            answer = max(answer, cnt)
    return answer

maxNum = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

            temp = check(candy)
            maxNum = max(temp, maxNum)

            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]    
        
        if i+1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

            temp = check(candy)
            maxNum = max(temp, maxNum)

            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
print(maxNum)
            
