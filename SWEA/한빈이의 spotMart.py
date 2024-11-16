T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    snack = list(map(int, input().split()))
    snack.sort(key=lambda x: -x)
    answer = 0
    for i in range(0, N-1):
        if snack[i] >= M:
            continue
        for j in range(i + 1, N):
            if snack[i] + snack[j] <= M:
                temp = snack[i] + snack[j]
                answer = max(answer, temp)
                break
    if answer == 0:
        print("#{} {}".format(tc, -1))
    else:
        print("#{} {}".format(tc, answer))
