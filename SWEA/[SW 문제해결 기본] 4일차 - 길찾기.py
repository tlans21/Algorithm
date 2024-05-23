def bfs(start, visited, graph):
    visited[start] = 1
    queue = []
    queue.append(start)

    while queue:
        now = queue.pop(0)
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                queue.append(next)

T = 10

for tc in range(1, T+1):
    answer = 0
    testCase, N = map(int, input().split())
    visit = [0 for _ in range(100)]

    temp = list(map(int, input().split()))
    graph = [[] for _ in range(100)] 
    # 방향 그래프 
    for i in range(N):
        u = temp[i*2]
        v = temp[i*2 + 1]
        
        graph[u].append(v)

    bfs(0, visit, graph)
    
    if visit[99] == 1:
        answer = 1
    print("#{} {}".format(testCase, answer))
    