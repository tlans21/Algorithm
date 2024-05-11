T = 10
for testCase in range(1, T + 1):
    # 양옆으로 -2, +2 씩만 체크
    answer = 0
    
    N = int(input())
    buildings = list(map(int, input().split()))

    
    for i in range(2, N-2):
        finalMax = max(buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2])

        if finalMax < buildings[i]:
            answer += buildings[i] - finalMax
    print(f"#{testCase}", answer)

