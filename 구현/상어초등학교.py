N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
blank = 0
student = []
# 학생들의 정보를 입력
for i in range(N*N):
    student.append(list(map(int, input().split())))

#student[0][0], student[1][0]..은 학생들의 번호이다.

board = [[0 for _ in range(N+1)] for i in range(N+1)]

#조건 구현
for i in range(0, len(student)):
    lst = []
    for j in range(1, N+1):
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
                if 1 <= nx <= N and 1 <= ny <= N:
                    if board[nx][ny] in student[i][1:]:
                        #1번 규칙에서 비어있는 칸 중에서 좋아하는 학생이 인접한 칸을 세는 행동
                        cnt += 1
                    if board[nx][ny] == 0:
                        blank += 1
            

            lst.append([cnt, blank, j, k])
    lst.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    # cnt가 높은 순으로 정렬, 즉 주위에 좋아하는 사람이 많은 곳에 첫번째로 배치되어 정렬된다는 뜻. lst[0][2] lst[0][3]은 좌표
    board[lst[0][2]][lst[0][3]] = student[i][0]

#학생 번호순으로 정렬
student.sort()

# 자리 배치가 완료 되고 점수 부여
sum = 0

for i in range(0, len(student)):
    for j in range(1, N+1):
        for k in range(1, N+1):
            cnt1 = 0
            # 학생번호가 보드판에서 못 찾은 경우 다음 턴으로 넘어감.
            if student[i][0] != board[j][k]:
                continue

            # 학생번호가 보드판에서 찾은 경우
            for s in range(0, 4):
                nx = dx[s] + j
                ny = dy[s] + k

                if 1 <= nx <= N and 1 <= ny <= N:
                    if board[nx][ny] in student[i][1:]:
                        cnt1 +=1

            if cnt1 == 1:
                sum +=1
            elif cnt1 == 2:
                sum +=10
            elif cnt1 == 3:
                sum +=100
            elif cnt1 == 4:
                sum +=1000
print(sum)       


            

    


        

            
            



