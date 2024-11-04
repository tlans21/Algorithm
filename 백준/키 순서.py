# 제한 시간

N, M = map(int, input().split()) # N : 학생들의 수, M : 두 학생 키를 비교한 횟수

def dfs(start, currentNode):
    global cnt
    for nextNode in graph[currentNode]:
        if visited[start][nextNode] == 0:
            visited[start][nextNode] = 1
            visited[nextNode][start] = 1
            dfs(start, nextNode)

        

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 양방향인지, 단방향인지 설정을 해야할 것 같음.
    graph[a].append(b)

visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N+1):
    dfs(i, i)

answer = 0
for i in range(1, N+1):
    if sum(visited[i]) == N-1:
        answer += 1

print(answer)