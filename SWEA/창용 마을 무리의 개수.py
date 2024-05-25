def find(x):
    if root[x] == x:
        return x
    else:
        return find(root[x])

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    root = [i for i in range(N+1)]

    for i in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)
    # 그룹 검사
    answer = N  # 그룹이 안정해져있으면 N개의 그룹이 있다.
    for i in range(1, N+1):
        if root[i] != i:
            answer -=1
    
    print("#{} {}".format(tc, answer))

