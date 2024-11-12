def dfs(startNode, parent):
    count[startNode] = 1
    for nextNode in graph[startNode]:
        if nextNode != parent:
            dfs(nextNode, startNode)
            count[startNode] += count[nextNode] 


N, R, Q = map(int, input().split()) # N : 정점의 수, R 루트의 번호, Q 쿼리의수


graph = [[] for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

dfs(R, -1)
for _ in range(Q):
    query = int(input())
    print(count[query])
    
