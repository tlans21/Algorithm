from collections import deque

N = int(input())

#오른쪽, 아래, 왼쪽, 위 순
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = [[0] * (N+1) for _ in range(N+1)]
K = int(input())



for i in range(K):
    a, b = map(int, input().split())
    board[a][b] = 2

L = int(input())
queue = deque()
queue.append((1, 1))
dic = dict()

for i in range(L):
   x, c = input().split()
   dic[int(x)] = c

x = 1
y = 1
board[x][y] = 1
cnt = 0
dir = 0

def turn(loc):
    global dir
    if loc == 'D':
        dir = (dir + 1) % 4 
    else:
        dir = (dir - 1) % 4

while True:
    cnt += 1
    x += dx[dir]
    y += dy[dir]

    
    if x<=0 or y<=0 or x>N or y>N or (x,y) in queue:
        break
    
    if board[x][y] == 0:
        board[x][y] = 1
        queue.append((x, y))
        pre_x, pre_y = queue.popleft()
        board[pre_x][pre_y] = 0
        if cnt in dic:
            turn(dic[cnt])
    elif board[x][y] == 2:
        board[x][y] = 1
        queue.append((x, y))
        if cnt in dic:
            turn(dic[cnt])
    else:
        break
    
print(cnt)           
    

    
    