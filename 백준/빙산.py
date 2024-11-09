import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_icebergs():
    ice_visited = [[0 for _ in range(M)] for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(M):
            if ice_visited[i][j] == 0 and board[i][j]:
                count += 1
                q = []
                ice_visited[i][j] = 1
                q.append((i, j))
                while q:
                    nowX, nowY = q.pop(0)

                    for k in range(4):
                        nextX = nowX + dx[k]
                        nextY = nowY + dy[k]
                        if 0 <= nextX < N and 0 <= nextY < M :
                            if ice_visited[nextX][nextY] == 0 and board[nextX][nextY]:
                                ice_visited[nextX][nextY] = 1
                                q.append((nextX, nextY))

    return count    

                    


def melt_bfs(x, y):
    global year
    queue = []
        
    temp_board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue.append((x, y))
    visited[x][y] = 1

    # 현재 빙산의 상태를 temp_board에 복사
    for i in range(N):
        for j in range(M):
            temp_board[i][j] = board[i][j]
    
    
    while queue:
        nowX, nowY = queue.pop(0)

        cnt = 0
        for k in range(4):
            nextX = nowX + dx[k]
            nextY = nowY + dy[k]
            if 0 <= nextX < N and 0 <= nextY < M:
                if board[nextX][nextY] == 0:
                    cnt += 1 # 바닷물 타일 갯수
                elif board[nextX][nextY] and visited[nextX][nextY] == 0:
                    visited[nextX][nextY] = 1
                    queue.append((nextX, nextY))
        

        fix_value = board[nowX][nowY] - cnt # 변경된 값
        
        if fix_value <= 0:
            temp_board[nowX][nowY] = 0 # 0보다 작을 수 없으므로 0
        else:
            temp_board[nowX][nowY] = fix_value  # 임시 저장 보드에 변화된 값들을 넣는다.
    
    return temp_board



N, M = map(int, input().split())

year = 0
board = []
temp_board = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)] 
for _ in range(N):
    board.append(list(map(int, input().split())))


while True:
    ice_count = count_icebergs()

    if ice_count >= 2:
        print(year)
        break
    elif ice_count == 0:
        print(0)
        break

    start_found = False
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                board = melt_bfs(i, j)
                start_found = True
                break
        if start_found == True:
            break
        
    year+= 1
