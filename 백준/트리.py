# 마지막 깊이(dfs)에서 갯수를 세면 됨. 즉 리프 노드를 알수 있다.
N = int(input())
cnt = 0
def dfs(startNode, visited, tree, nodes):
    global cnt
    visited[startNode] = 1

    isLeaf = True
    for nextNode in tree[startNode]:
        if visited[nextNode] == 0:
            dfs(nextNode, visited, tree, nodes)
            isLeaf = False
    
    if isLeaf == True:
        cnt += 1
    

nodes = list(map(int, input().split()))
tree = [[] for _ in range(N)]
rootNum = 0
for num in range(N):
    # 루트 노드일때
    if nodes[num] == -1:
        rootNum = num
        continue
    # 양방향 연결 인덱스틀 통해서 부모, 자식 노드를 알아냄
    tree[num].append(nodes[num]) 
    tree[nodes[num]].append(num)
visited = [0 for _ in range(N)]    
deleteNodeNum = int(input())
answer = []
visited[deleteNodeNum] = 1
if rootNum == deleteNodeNum:
    print(0)
else:
    dfs(rootNum, visited, tree, nodes)
    print(cnt)