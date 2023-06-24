N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
blank = 0
student = []
# 학생들의 정보를 입력
for i in range(N):
    student.append(list(map(int, input().split())))

#student[0][0], student[1][0]..은 학생들의 번호이다.

board = [[0 for _ in range(N+2)] for i in range(N+2)]
lst = []
temp = -1
#조건 구현
for i in range(0, len(student)):
    # 학생 번호
    stduentNum = student[i][0]
    #좋아하는 학생의 번호
    favorite1 = student[i][1]
    favorite2 = student[i][2]
    favorite3 = student[i][3]
    favorite4 = student[i][4]
    for j in range(1, N+1):
        temp = -1
        for k in range(1, N+1):
            cnt = 0
            blank = 0
            # 현재위치에 학생 번호가 존재하면 다음 순번으로 
            if board[j][k] != 0:
                continue
            for s in range(0, 4):
                nx = dx[s]+ j
                ny = dy[s]+ k

                #비어있는 칸 중에서좋아하는 학생이 많이 인접한 칸으로 자리를 정함.
                #즉 board[nx][ny] == favorite1, 2, 3, 4.. 갯수를 카운트
                if nx >= 1 and nx <=N and ny >=1 and ny <= N:
                    if (board[nx][ny] == favorite1 or board[nx][ny] == favorite2 or board[nx][ny] == favorite3 or board[nx][ny] == favorite4 ) and board[nx][ny] != 0:
                        #1번 규칙에서 비어있는 칸 중에서 좋아하는 학생이 인접한 칸을 세는 행동
                        cnt += 1
                    if board[nx][ny] == 0:
                        blank += 1 

            lst.append(cnt, blank, j, k)
    lst.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    board[lst[0][2]][lst[0][3]] = student[i][0]

    student.sort()

for s in range(0, len(student)):
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(4):
                nx = dx[k] + i
                ny = dx[k] + j
                if 1 <= nx <= N and 1<= ny <= N:
                    if board[i][j] == 

            

    


        

            
            



