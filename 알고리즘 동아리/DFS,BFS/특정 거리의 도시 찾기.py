from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    

dist = [-1] * (N + 1)
dist[X] = 0

def bfs(graph, X, K, dist):
    queue = deque([X])

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            #예시) graph에서 노드 1번에서 노드2번을 연결했을 때, 해당 번호는 2차원 리스트 append를 통해 값으로 표현되었음   
            if dist[next] == -1:
                queue.append(next) # 노드 번호가 들어가야함.
                dist[next] = dist[cur] + 1
                if K == dist[next]:
                    return next

    return -1            

print(bfs(graph, X, K, dist))

            



