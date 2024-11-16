from itertools import combinations  
T = int(input())

for tc in range(1, T + 1):
    N, R = map(int, input().split())
    input_list = [i for i in range(1, N + 1)]
    answer = list(combinations(input_list, R))
    print("#{} {}".format(tc, len(answer)))