def bfs(start, visited, graph):
    visited[start] = 1
    queue = []
    queue.append(start)

    while queue:
        nowLocation = queue.pop(0)
        # 그래프 표현
        for next in graph[nowLocation]:
            if not visited[next]:
                visited[next] = visited[nowLocation] + 1
                queue.append(next) 




T = 10

for tc in range(1, T+1):
    N, startPoint = map(int, input().split())
    graph = [set() for _ in range(101)]
    visit = [0 for _ in range(101)]
    temp = list(map(int, input().split()))

    
    # 분류: 2개의 인덱스씩 from to 반복
    for i in range(0, N//2):
        u = temp[i * 2]
        v = temp[i * 2 + 1]
        graph[u].add(v)
    
    bfs(startPoint, visit, graph)
    
    maxIdx = 0
    for i in range(0, 101):
        if visit[i] >= visit[maxIdx]:
            maxIdx = i

    print("#{} {}".format(tc, maxIdx))
    
