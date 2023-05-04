from collections import deque

N, L, R = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for i in range(N):
    graph.append(map(int, input().split()))



def bfs():
    queue = deque()