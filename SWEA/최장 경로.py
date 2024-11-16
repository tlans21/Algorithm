def dfs(startNode, depth):
    global ans
    visited[startNode] = 1

    for nextNode in graph[startNode]:
        if visited[nextNode] == 0:
            dfs(nextNode, depth + 1)
            visited[nextNode] = 0 # 백 트레킹

    ans = max(ans, depth)
    return 

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N 정점 개수, M 간선 갯수
    ans = 1
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        visited = [0 for _ in range(N + 1)]
        dfs(i, 1)
    print("#{} {}".format(tc, ans))