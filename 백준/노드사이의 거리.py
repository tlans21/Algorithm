N, M = map(int, input().split())
def dfs(start, end, tree, visited, distance):
    global answer_distance
    visited[start] = 1

    if start == end:
        answer_distance = distance
        return
    
    for nextNode in tree[start]:
        nextNodeNum, nextNodeDistance = nextNode
        if visited[nextNodeNum] == 0:
            dfs(nextNodeNum, endNode, tree, visited, distance + nextNodeDistance)
    

tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    # 두 점과 거리를 입력받는다.
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u, w])

for _ in range(M):
    startNode, endNode = map(int, input().split())
    answer_distance = 0
    visited = [0 for _ in range(N + 1)]
    dfs(startNode, endNode, tree, visited, 0)
    print(answer_distance)