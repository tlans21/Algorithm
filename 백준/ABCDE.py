def dfs(startNode, depth):
    global answer
    if depth == 4: 
        answer = 1
        return 
    visited[startNode] = 1
    
    for nextNode in graph[startNode]:
        if visited[nextNode] == 0: 
            dfs(nextNode, depth + 1)
    visited[startNode] = 0 # 백트레킹
    

N, M = map(int, input().split()) # N : 사람 수, M : 친구 관계 수

answer = 0
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

for i in range(0, N):
    if answer == 0: 
        visited = [0 for _ in range(N)]
        dfs(i, 0)

print(answer)


