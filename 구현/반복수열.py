N, M, R = map(int, input().split(' '))

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split(' '))))


for _ in range(R):
    s = min(N, M) // 2
    for i in range(s):
        x, y = i, i
        
        cur_value = graph[x][y]

        # 좌, i+1은 높이 N-i까지
        for j in range(i+1, N-i):
            x = j
            pre_value = graph[x][y]
            graph[x][y] = cur_value
            cur_value = pre_value

        # x값은 아래에 유지된 상태로 온다

        # 하, i+1 오른쪽 끝 M-i까지
        for j in range(i+1, M-i):
            y = j
            pre_value = graph[x][y]
            graph[x][y] = cur_value
            cur_value = pre_value
        
        # 우
        for j in range(i+1, N-i):
            x = N-j-1
            pre_value = graph[x][y]
            graph[x][y] = cur_value
            cur_value = pre_value
        
        # 상

        for j in range(i+1, M-i):
            y = M-j-1
            pre_value = graph[x][y]
            graph[x][y] = cur_value
            cur_value = pre_value

for i in range(N):
    for j in range(M):
        print(graph[i][j], end=" ")
    print()



