# 트리의 루트를 1로 주어짐.
# 루트와 부모 노드는 서로 다른 개념이다.
# 부모 노드를 구해보자

def dfs(currentNode, parent):
    global answer
    
    for nextNode in graph[currentNode]:
        if nextNode != parent: # 다음으로 갈 노드가 현재 부모 노드가 아니라면 진행해도 됨. 이유) 부모 노드로만 안가면 되기 때문에,
            parentNodes[nextNode] = currentNode # 다음 노드의 부모가 현재 노드로 저장
            dfs(nextNode, currentNode) # 
            


    
N = int(input())
graph = [[] for _ in range(N + 1)]

parentNodes = [0 for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
dfs(1, 0)
for i in range(2, N+1):
    print(parentNodes[i])
# idea) dfs 진행시, 현재 노드를 다음 노드의 부모로 저장하는 메커니즘으로
