T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    answer = 0
    maxIdx = N-1
    for i in range(N-2, -1, -1):
        if price[maxIdx] >= price[i]:
            answer += price[maxIdx] - price[i]
        else:
            maxIdx = i


    print("#{} {}".format(tc, answer))