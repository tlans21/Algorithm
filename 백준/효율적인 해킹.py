
def dfs(startNode, graph, visited):
    global cnt
    visited.add(startNode)

    for nextNode in graph[startNode]:
        if nextNode not in visited:
            dfs(nextNode, graph, visited) 
            cnt += 1

N, M = map(int, input().split())

# 컴퓨터는 1번부터 N번까지

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

answer = [0]
cnt = 1
for node in range(1, N + 1):
    cnt = 1
    visited = set()
    dfs(node, graph, visited)
    answer.append(cnt)
max_value = max(answer)

final_answer = []
for idx, value in enumerate(answer):
    if value == max_value:
        final_answer.append(idx)

print(" ".join(list(map(str, final_answer))))
            