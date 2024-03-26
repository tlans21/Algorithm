import heapq

def dijkstra(start, K, distance, graph):
    q = []
    heapq.heappush(q, (0, start)) # 우선 순위, 거리 값 형태로 들어간다.
    distance[start] = 0
    
    
    while q:
        dist, now = heapq.heappop(q) # 우선 순위가 가장 작은 것부터 나옴
        
        if distance[now] < dist:
            continue
        
        for node in graph[now]:
            target, node_distance = node[0], node[1]
            if distance[target] > dist + node_distance:
                distance[target] = dist + node_distance
                heapq.heappush(q, (dist + node_distance, target))
        
        
        
    


def solution(N, roads, K):
    answer = 0
    INF = 1e8
    
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    distance = [INF] * (N + 1)
    
    for road in roads:
        start, end, weight = road[0], road[1], road[2]
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    
    dijkstra(1, K, distance, graph)
    
    for d in distance[1:]:
        if d <= K:
            answer += 1
        
    
    return answer