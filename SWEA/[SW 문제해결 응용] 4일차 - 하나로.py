def find(x):
    if root[x] == x: # 부모 노드 찾음.
        return x
    else:
        return find(root[x]) # 부모 노드를 못찾았기 때문에 다시 찾기.

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # 루트 노드가 더 작은 것을 루트로 둔다.
    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b

T = int(input())

for tc in range(1, T+1):
    temp = 1234567899999
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
    edges = []
    for i in range(N):
        x1, y1 = x_lst[i], y_lst[i]
        for j in range(i+1, N):
            x2, y2 = x_lst[j], y_lst[j]
            edges.append([((x1 - x2) ** 2 + (y1 - y2) ** 2) * E, i, j])
    edges.sort()        
    root = [i for i in range(N)]
    cnt = 0
    result = 0
    for i in range(len(edges)):
        if cnt == N-1:
            break
        
        d, n1, n2 = edges[i]
        
        # 같은 그룹에 속해 있지 않다면
        if find(n1) != find(n2):
            union(n1, n2)
            cnt += 1 # 간선 추가
            result += d
    print("#{} {}".format(tc, int(round(result, 0))))
