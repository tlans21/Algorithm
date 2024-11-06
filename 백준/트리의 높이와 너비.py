def dfs(currentNode, depth):
    global cnt
    global maxDepth
    global min_col
    global max_col
    if currentNode == -1:
        return
    
    dfs(graph[currentNode][0], depth + 1) # 왼쪽 트리 dfs 진행
    col[depth] = cnt
    # 해당 같은 열에서 너비 최대, 최소 값 구하기.
    min_col[depth] = min(min_col[depth], col[depth])
    max_col[depth] = max(max_col[depth], col[depth])

    cnt += 1

    
    dfs(graph[currentNode][1], depth + 1) # 오른쪽 트리 dfs 진행

N = int(input()) # 노드의 개수

cnt = 0
maxDepth = 0
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
nodeCntList = [[] for _ in range(N + 1)]
board = [[-1] * 2 for _ in range( N + 1)]
col = [0 for _ in range(N + 1)]
min_col = [987654321 for _ in range(N + 1)]
max_col = [0 for _ in range(N + 1)]
node = [0] * (N + 1)

for _ in range(N):
    center, left, right = map(int, input().split()) # 중앙, 왼쪽, 오른쪽 노드 주어짐
    graph[center].append(left)
    graph[center].append(right)
    if left != -1:
        node[left] = center
    if right != -1:
        node[right] = center


root = 1
for i in range(1, N + 1):
    if node[i] == 0:   
        root = i

dfs(root, 1)



answer_list = []
for i in range(1, N + 1):
    if min_col[i] != 987654321:
        answer = max_col[i] - min_col[i] + 1
        answer_list.append((answer, i))

answer_list.sort(key=lambda x: (-x[0], x[1]))
print(answer_list[0][1], answer_list[0][0])