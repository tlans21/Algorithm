N, M = map(int, input().split())
x, y, direct = map(int, input().split())
# direct = 0, 1, 2, 3 순으로  북,동,남,서를 바라본다
list1 = []
visit = [[0] * N]*M
dy = [0, 1, 0, -1] 
dx = [-1, 0, 1, 0]
for i in range(M):
    list1.append(list(map(int, input.split())))

cnt = 0
turn = 0
def turn_left():
    global direct 
    direct -=1

    if(direct == -1):
        direct = 3
      
while True :
    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]
    if(visit[ny][nx] == 0 and list1[ny][nx] == 0):
        visit[ny][nx] = 1
        x = nx
        y = ny
        cnt += 1
        turn = 0
    else:
        turn += 1
    
    if (turn == 4):
        nx = x - dx[direct]
        ny = y - dy[direct]
        if(list1[ny][nx] == 0):
            x = nx
            y = ny
        else:
            break
    
    turn = 0

print(cnt)



