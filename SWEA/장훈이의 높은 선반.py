from itertools import combinations
T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    answer = 123456789
    if N != 1:
        for i in range(1, N+1):
            combi = list(combinations(heights, i))
            for combiLst in combi:
                sumValue = sum(combiLst)
                if sumValue >= B:
                    answer = min(answer, sumValue)
        answer = answer - B
    elif N == 1:
        sumValue = heights[0]
        if sumValue >= B:
            answer = sumValue - B
        
 
    print("#{} {}".format(tc, answer))