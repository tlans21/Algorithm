dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque

def bfs(x, y, maps, visited, flag):
    if flag == 'lever':
        exit = False 
    elif flag == 'exit':
        exit = True
        
    time = 0
    queue = deque([(x, y, time)])
    visited[x][y] = True
    
    while queue:
        pop_x, pop_y, pop_time = queue.popleft()
        
        for i in range(4):
            now_x = pop_x + dx[i]
            now_y = pop_y + dy[i]
            
            if 0 <= now_x < len(maps) and 0 <= now_y < len(maps[now_x]):   
                if not visited[now_x][now_y]:
                    if maps[now_x][now_y] == 'O':
                        queue.append((now_x, now_y, pop_time + 1))
                        visited[now_x][now_y] = True
                    elif maps[now_x][now_y] == 'L':
                        # L을 거쳐서 E로 가는 경우
                        
                        if exit == True:
                            queue.append((now_x, now_y, pop_time + 1))
                            visited[now_x][now_y] = True
                        else:
                            return pop_time + 1
                    elif maps[now_x][now_y] == 'E':
                        # E를 거쳐서 L로 가는 경우
                        if exit == False:
                            queue.append((now_x, now_y, pop_time + 1))
                            visited[now_x][now_y] = True
                        else:
                            return pop_time + 1
                    elif maps[now_x][now_y] == 'S':
                        queue.append((now_x, now_y, pop_time + 1))
                        visited[now_x][now_y] = True
                        
    return -1

def solution(maps):
    answer = 0
    visited = [[False for j in range(len(maps[i]))] for i in range(len(maps))]
    
    # start -> lever
    start_x = -1
    start_y = -1
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start_x = i
                start_y = j
    
    # bfs 탐색 시간
    flag = 'lever'
    first_time = bfs(start_x, start_y, maps, visited, flag)
    answer += first_time 
    
    if first_time == -1:
        return -1
    
   
    # lever -> exit
    visited = [[False for j in range(len(maps[i]))] for i in range(len(maps))]
    lever_x = -1
    lever_y = -1
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'L':
                lever_x = i
                lever_y = j
    flag = 'exit'
    second_time = bfs(lever_x, lever_y, maps, visited, flag)
    
    if second_time == -1:
        return -1
    
    answer += second_time
    
    return answer