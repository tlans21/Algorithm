import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(startNode):
    global result
    visited[startNode] = 1
    cycle.append(startNode)

    nextNode = numbers[startNode]
    
    if visited[nextNode] == 0:
        dfs(nextNode)
    else:
        if nextNode in cycle: # nextNode가 방문 될 수 없는 상황은 곧 싸이클이 만들어짐
            result += cycle[cycle.index(nextNode):]




T = int(input())

for tc in range(T):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(len(numbers))]
    result = []
    # 1번부터 n번까지
    for i in range(1, n + 1):
        cycle = []
        dfs(i)
    print(n - len(set(result))) 