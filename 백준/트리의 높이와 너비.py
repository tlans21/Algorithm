N = int(input()) # 노드의 개수


graph = [[] for _ in range(N + 1)]

for _ in range(N):
    center, left, right = map(int, input().split()) # 중앙, 왼쪽, 오른쪽 노드 주어짐
    graph[center].append(right)
    graph[center].append(left)

# 문제 해결 : 노드 하나당 하나의 칸을 차지 하기 때문에, 가로의 길이는 N이 된다.
# DFS를 통해서 깊이를 재어 높이를 알 수 있다.
# 왼쪽 끝

# 0번째 딥스에서 DFS시행 -> 왼쪽 개수, 오른쪽 개수 파악하고 왼쪽 너비 할당, 오른쪽 너비 할당
# 1번째 딥스에서 DFS시행 ->  이하동문
# 이하동문

# 배치
# 예를들어 왼쪽으로 진행된 DFS면 

# 내일 다시 풀자.


