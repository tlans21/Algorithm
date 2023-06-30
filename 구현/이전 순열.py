N = int(input())
input_list = list(map(int, input().split()))



for i in range(N-1, 0, -1):
    if input_list[i - 1] > input_list[i]:
        for j in range(N-1, 0, -1):
            if input_list[i-1] > input_list[j]:
                input_list[i-1], input_list[j] = input_list[j], input_list[i-1]
                input_list = input_list[:i] + sorted(input_list[i:], reverse=True)
                print(*input_list)
                exit()
print(-1)

