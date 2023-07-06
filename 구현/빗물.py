H, W = map(int, input().split())

W_list = list(map(int, input().split()))

answer = 0

for i in range(1, W-1):
    left_max = max(W_list[:i])
    right_max = max(W_list[i+1:])

    compare = min(left_max, right_max)

    if W_list[i] < compare:
        answer += compare - W_list[i]

print(answer)