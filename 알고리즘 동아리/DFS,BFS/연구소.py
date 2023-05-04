from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = []
temp = [[0] * M for _ in range(N)]

answer = 0


for _ in range(N):
    graph.append(list(map(int, input().split())))

safe = 0

# 문제 해결 팁, 순서를 구상
# 1. 울타리를 3개를 만든다. (8x8 64C3 시간 제한 조건에 부합), (조합으로 해결. 조합은 사실 dfs방식이다.)
# 2. 3개를 만들었으면 바이러스를 전파한다. (dfs나 bfs방식 둘다 상관없음)
# 3. 안전 영역을 세어준다.
# 4. 안전 영역의 최댓값을 알아내기 위해 max함수를 이용해 갱신하고 다시 1번으로 돌아간다.


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < M: 
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))





# 전체적 알고리즘
def dfs(count):
    global safe
    global answer
    # 울타리 설치 완료, 바이러스 전파 해야함.
    if count == 3:
        for i in range(N):
            for j in range(M):
                #2번째 이상의 시행에서 원래의 temp로 만들기 위해 해당 코드를 작성
                temp[i][j] = graph[i][j]

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    bfs(i, j)
        
        # 바이러스가 전파 되었으면 이제 안전지대를 검사해야함.
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 0:
                    safe = safe + 1
        #검사 완료 최대 갱신
        answer = max(safe, answer)
        safe = 0
        return
        
        #다음번 3개의 조합을 위해서 safe를 0개, graph를 돌려두어야 하지만 조합 알고리즘에서 graph를 원상 복귀함.
    # -- 조합 부분 --
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count = count + 1
                dfs(count)
                count = count - 1
                graph[i][j] = 0
    # -- 조합 부분 --
    
    
        

dfs(0)
print(answer)




