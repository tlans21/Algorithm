import heapq
def prim(start, dist):
    global answer
    heap = [[dist, start]]
    
    cnt = 0
    while heap:
        if cnt == V:
            break    
        w, s = heapq.heappop(heap)

        if not visited[s]:
            visited[s] = True
            cnt += 1
            answer += w
            for adj in graph[s]:
                adjw, adjs = adj
                heapq.heappush(heap, [adjw, adjs])
    return


V, E = map(int, input().split())

answer = 0
graph = [[] for _ in range(V + 1)]
visited = [False for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A]) 
prim(1, 0)
print(answer) 
# 최소 스패닝 트리는 V개의 정점에 V-1개의 간선이 있어야 하며 사이클이 없어야한다.




