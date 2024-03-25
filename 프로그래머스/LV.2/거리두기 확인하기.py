dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, place, visited, depth):
    if depth == 2:
        return True
    
    # 방문 처리
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] != 'X' and visited[nx][ny] == 0:
                if place[nx][ny] == 'P':
                    return False
                else:
                    if visited[nx][ny] == 1:
                        continue
                    if dfs(nx,ny,place,visited,depth+1) == False:
                        return False
                    
def search(place, visited):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and visited[i][j] == 0:
                if dfs(i, j, place, visited, 0) == False:
                    return False
    
    return True
            
def solution(places):
    answer = []
    for place in places:
        visited = [[0 for s in range(0, 5)] for k in range(0, 5)]
        if search(place, visited):
            answer.append(1)
        else:
            answer.append(0)
                        
    return answer