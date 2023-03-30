N, M = map(int, input().split())
x, y, direction = map(int, input.split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

list = []
visit = [[0]*M]*N
cnt = 0
for i in range(0, N):
    list.append(input.split())

turn_cnt = 0
while True :
    direction -= 1
    if(direction == -1) :
        direction = 3
    
    nx = x + dx[direction]
    ny = y + dy[direction]


    if(list[ny][nx] == 0 and visit[ny][nx] == 0):
        visit[ny][nx] = 1
        x = nx
        y = ny
        cnt +=1
        turn_cnt = 0

        continue
    else:
        turn_cnt += 1
    
    if(turn_cnt == 4):
        nx = x - dx[direction]
        ny = y - dy[direction]
        if(list[ny][nx] == 0):
            x = nx
            y = ny
        else:
            break

    turn_cnt = 1

     

    

