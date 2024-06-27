# 시간 초과 코드
min_value = 123456789
def dfs(x, y, depth, board, visited):
    global min_value
    # 현재 dfs 시행했을때 위치가 목표지점이라면 종료
    if min_value < depth:
        return
    
    if board[x][y] == 'G':
        min_value = min(min_value, depth)
        return

    
    for k in range(4):
        nx, ny = move(x, y, k, board)
        if  0 <= nx < len(board) and 0 <= ny <len(board[nx]) and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, board, visited)           
            visited[nx][ny] = 0
        

def move(x, y, dir, board):
    # 왼쪽
    if dir == 0:
        # 왼쪽 바깥으로 가거나 벽에 막혔을 때 조건 처리
        while 0 <= y < len(board[x]):
            if board[x][y] == 'D':
                break
            y -= 1
            
        y += 1
    # 오른쪽
    elif dir == 1:
        while 0 <= y < len(board[x]):
            if board[x][y] == 'D':
                break
            y += 1
            
        y -= 1
    # 아래쪽
    elif dir == 2:
        while 0 <= x < len(board):
            if board[x][y] == 'D':
                break
            x += 1

        x -= 1 
    # 위쪽
    elif dir == 3:
        while 0 <= x < len(board):
            if board[x][y] == 'D':
                break
            x -= 1
        x += 1
    
    return [x, y]


def solution(board):
    global min_value
    answer = 0
    visited = [[0 for j in range(len(board[i]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                return_value = dfs(i, j, 0, board, visited)
    answer = min_value
    if min_value == 123456789:
        return -1
    return answer



# board = [list(map(str, input())) for _ in range(5)]
# min_value = 123456789
# def dfs(x, y, depth, board, visited):
#     global min_value
#     # 현재 dfs 시행했을때 위치가 목표지점이라면 종료
#     if min_value < depth:
#         return
    
#     if board[x][y] == 'G':
#         print("depth", depth)
#         min_value = min(min_value, depth)
#         return

    
#     for k in range(4):
#         nx, ny = move(x, y, k, board)
#         if  0 <= nx < len(board) and 0 <= ny <len(board[nx]) and visited[nx][ny] == 0:
#             visited[nx][ny] = 1
#             dfs(nx, ny, depth + 1, board, visited)           
#             visited[nx][ny] = 0
        

# def move(x, y, dir, board):
#     # 왼쪽
#     if dir == 0:
#         # 왼쪽 바깥으로 가거나 벽에 막혔을 때 조건 처리
#         while y > 0 and board[x][y-1] != 'D':
#             y -=1
        
#     # 오른쪽
#     elif dir == 1:
#         while 0 <= y < len(board[x]) -1 and board[x][y+1]:
#             y += 1
            
#     # 아래쪽
#     elif dir == 2:
#         while 0 <= x < len(board) - 1 and board[x+1][y]:
#             x += 1

#     # 위쪽
#     elif dir == 3:
#         while 0 <= y < len(board):
#             if board[x][y] == 'D':
#                 break
#             x -= 1
#         x += 1
    
#     return [x, y]


# def solution(board):
#     global min_value
#     answer = 0
#     visited = [[0 for j in range(len(board[i]))] for i in range(len(board))]
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 'R':
#                 dfs(i, j, 0, board, visited)
#     answer = min_value
#     return answer
# solution(board)
# print("답 :", min_value)