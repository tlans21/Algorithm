from itertools import combinations
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    answer = set([])
    combi_lst = []
    for i in range(1, N + 1):
        combi = list(combinations(number, i))
        for elements in combi:
            sum_value = 0    
            for num in elements:
                sum_value += num
            answer.add(sum_value)
    answer.add(0)
    answer = list(answer)

    print("#{} {}".format(tc, len(answer)))
