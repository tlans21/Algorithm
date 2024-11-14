T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    minValue = min(numbers)
    maxValue = max(numbers)
    sum = 0
    cnt = 0
    for i in range(len(numbers)):
        if numbers[i] == minValue:
            cnt += 1 
            continue
        elif numbers[i] == maxValue:
            cnt += 1
            continue
        else:
            sum += numbers[i]
    if 10 - cnt == 0:
        answer = 0
    else:
        answer = round(sum / (10 - cnt), 0) 

    print("#{} {}".format(tc,int(answer)))

    