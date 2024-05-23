def dfs(loc, depth, length, visited, order):
    if depth == N-1:
        for i in range(N//2):
            first = order[i*2]
            second = order[i*2 + 1]
            x1, y1 = loc[first]
            x2, y2 = loc[second]
            length = abs(x1-x2) + abs(y1-y2)
        return

    for i in range(N):
        if visited[i] == 1:
            continue

        visited[i] = 1
        order.append(i)
        dfs(loc, depth + 1, length, visited, order)
        order.pop()
        visited[i] = 0    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    visit = [0 for _ in range(N)]
    loc = []
    order = []
    for i in range(len(x_lst)):
        loc.append((x_lst[i], y_lst[i]))
    dfs(loc, 0, 0, visit, order)
    E = int(input())
