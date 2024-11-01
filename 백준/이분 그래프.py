import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(startNode, group):
    visited[startNode] = group

    for nextNode in graph[startNode]:
        if not visited[nextNode]:
            returnValue = dfs(nextNode, -group)
            
            if returnValue == False:
                return False
        elif visited[startNode] == visited[nextNode]:
            return False
    return True

K = int(input())

for tc in range(K):
    V, E = map(int, input().split()) # V 정점의 개수, E 간선의 개수
    graph = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    # E개의 간선 정보
    for nodeNum in range(E):
        u, v = map(int, input().split()) # 간선 정보
        # 양방향 그래프
        graph[u].append(v)
        graph[v].append(u)
        
    for node in range(1, V+1):
        if not visited[node]: # 방문안한 노드가 있다면 dfs 진행
            result = dfs(node, 1)
            if not result: # 한번이라도 False일시 수행 필요없음
                break
        
    print("YES" if result else "NO")

