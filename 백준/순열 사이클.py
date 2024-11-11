import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def dfs(startNode):
    global result 
    visited[startNode] = 1
    cycle.append(startNode)
    nextNode = numbers[startNode]

    if visited[nextNode] == 0:
        dfs(nextNode)
    else:
        if startNode in cycle:
            result += 1
            return


for tc in range(T):
    N = int(input())

    numbers = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(len(numbers))]
    result = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)
    print(result)
