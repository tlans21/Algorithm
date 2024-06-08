# 1 3
# 1 4
# 2 3
# 3 4
# 4 5 친구 인 경우 ex
# 1은 2까지 1 -> 3 -> 2 2단계 
# 1은 3까지 1 -> 3 1단계
# 1은 4까지 1 -> 1단계
# 1은 5까지 1 - > 1 -> 4 -> 5 2단계
# 따라서 단계의 총합은 2 + 1 + 1 + 2 = 6이다.

def bfs(start):
    queue = []
    queue.append(start)
    visited[start] = 0
    while queue:
        now = queue.pop(0)
        for adj in graph[now]:
            if visited[adj] > visited[now] + 1:
                visited[adj] = visited[now] + 1 
                queue.append(adj)


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    # 양방향이다.
    graph[u].append(v)
    graph[v].append(u)
answer = []
for i in range(1, N + 1):
    sum = 0
    for j in range(1, N+1):
        if i == j:
            continue
        visited = [123456789 for _ in range(N+1)]
        bfs(i)
        sum += visited[j]
    answer.append(sum)

min_value = 123456789
min_idx = -1
for i in range(len(answer)):
    if min_value > answer[i]:
        min_value = answer[i]
        min_idx = i

print(min_idx + 1)


        