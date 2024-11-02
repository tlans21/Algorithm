
def dfs(currentNode, targetNode, depth):
    global answer
    visited[currentNode] = 1


    if currentNode == targetNode:
        return depth
    
    for nextNode in graph[currentNode]:
        if visited[nextNode] == 0:
            result = dfs(nextNode, targetNode, depth + 1)
            if result != None:
                return result 
    return None
n = int(input()) # 전체 사람 수
personA, personB = map(int, input().split()) # 촌수 계산해야하는 사람들
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    parent, child = map(int, input().split())
    graph[child].append(parent)
    graph[parent].append(child)


answer = dfs(personA, personB, 0)

if answer == None:
    print(-1)
else:
    print(answer)