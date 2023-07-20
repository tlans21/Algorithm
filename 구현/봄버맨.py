R, C, N = map(int, input().split())

# 초기 폭탄 설치 0초
# 아무것도 안함 1초
# 전부 설치 다음 1초 (설치된 폭탄은 0초부터 시작)
# 1초가 지난후 3초가 경과되어 초기폭탄 폭팔. (설치된 폭탄은 1초)
# 전부 설치 다음 1초 (설치된 폭탄은 2초)
# 따라서 폭탄이 터지고나서 1초, (3초가 터지는것이라면) 

board = []
first_board = [['.' for j in range(C)] for i in range(R)]
for i in range(R):
    board.append(list(map(str, input())))

cnt = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
    if cnt == N:
        break

    cnt += 1

    for i in range(R):
        for j in range(C):
            # 초기 폭탄 자리 저장
            if board[i][j] == 'O':
                first_board[i][j] = 'O'
            
            # 추가 폭탄
            if board[i][j] == '.':
                board[i][j] = 'O'

    if cnt == N:
        break

    cnt += 1
    
    for i in range(R):
        for j in range(C):
            # 초기 폭탄을 기반하여 보드에서 상하좌우 제거
            if first_board[i][j] == 'O':
                board[i][j] = '.'
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < R and 0 <= ny < C:
                        board[nx][ny] = '.'
    first_board = [['.' for j in range(C)] for i in range(R)]
    
    if cnt == N:
        break

for i in range(R):
    for j in range(C):
        print(board[i][j], end = "")
    print()    



                 