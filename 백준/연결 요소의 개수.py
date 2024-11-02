def dfs(startNode):
    visited[startNode] = 1

    for nextNode in graph[startNode]:
        if visited[nextNode] == 0:
            dfs(nextNode)
            



N, M = map(int, input().split()) # 정점 개수 : N, 간선의 개수 : M

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 출력 : 연결 요소의 개수, 즉 따로 떨어진게 그래프가 몇개인지 구해라.
answer = 0
for i in range(1, N+1):
    if visited[i] == 0:
        answer += 1
        dfs(i)
        


print(answer)