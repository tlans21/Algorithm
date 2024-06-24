# 효율성 테스트(시간초과 코드)
# def solution(board):
#     answer = 1
    
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 1:
#                 cnt = 0
#                 flag = False
#                 while True:
#                     cnt += 1
#                     for k in range(i, i + cnt):
#                         for s in range(j, j + cnt):
#                             if k < len(board) and s < len(board[i]):
#                                 if board[k][s] == 0:
#                                     flag = True
#                                     break
#                             else:
#                                 flag = True
#                                 break
#                         if flag == True:
#                             break
#                     if flag == True:
#                         break
#                     answer = max(answer, cnt * cnt)
                
#     return answer


# 다이나믹 프로그래밍(dp)
# 가로축의 길이를 계속해서 더하고, 세로 축의 길이를 더해서 그중에서 작은 것을 변으로 한다.

def solution(board):
    answer = 0
    dp = [[board[i][j] for j in range(len(board[i]))] for i in range(len(board))]
    
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                
                
    for i in range(len(board)):
        temp = max(dp[i])
        answer = max(temp, answer)
    
    answer = answer ** 2
    return answer
