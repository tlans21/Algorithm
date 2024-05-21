from itertools import combinations
N = 100
lst = [0 for _ in range(N)]


for i in range(1, N):
    combi = combinations(lst, i)
    print(list(combi))