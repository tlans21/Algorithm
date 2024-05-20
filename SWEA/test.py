T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    answer = max(lst)

    print("#{} {}".format(tc, answer))