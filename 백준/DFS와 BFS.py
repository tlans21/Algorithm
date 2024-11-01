


N, M, V = map(int, input().split())

def dfs(start, graph, visited, answer):
    # 현재 위치 방문
    visited[start] = 1
    answer.append(start)
    for nextnode in graph[start]:
        #다음 노드로 갈 곳에 만약 방문을 안했다면
        if visited[nextnode] == 0:
            dfs(nextnode, graph, visited, answer)
            

    return;

def bfs(start, graph, visited, answer):
    queue = []
    queue.append(start)
    answer.append(start)
    visited[start] = 1
    while queue:
        curNode = queue.pop(0)
        for nextNode in graph[curNode]:
            if visited[nextNode] == 0:
                queue.append(nextNode)
                answer.append(nextNode)
                visited[nextNode] = 1

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    graph[i].sort()

answer = []

dfs(V, graph, visited, answer)
print(' '.join(map(str, answer)))

answer = []
visited = [0 for _ in range(N + 1)]
bfs(V, graph, visited, answer)
print(' '.join(map(str, answer)))
