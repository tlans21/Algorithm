input = input();

dx = [-2, 2, 0, 0]
dy = [0, 0, -2, 2]
cnt = 0
# i == 0, 1, 2 ,3순으로 왼쪽, 오른쪽, 위, 아래 
for i in range(0, 4):
    numberChange = ord(input[0]) - ord('a') + 1
    nx = dx[i] + numberChange
    ny = dy[i] + int(input[1])
    for j in range(0, 2):
        if i == 0:
            if j == 0:
                ny -=1
            elif j == 1:
                ny +=1 
        elif i == 1:
            if j == 0 :
                ny -=1
            elif j == 1:
                ny +=1
        elif i == 2:
            if j == 0:
                nx -=1
            elif j == 1:
                nx +=1
        elif i == 3:
            if j == 0:
                nx -=1
            elif j == 1:
                nx +=1
        if nx > 8 or nx < 1 or ny > 8 or ny < 1:
            continue
        cnt += 1

print(cnt)

