T = 10

for tc in range(1, T+1):
    tc_input = int(input())
    minusNumber = 0
    data = list(map(int, input().split()))

    while True:
        first = data.pop(0)
        minusNumber += 1
        endValue = first - minusNumber
        
        if endValue < 0:
            endValue = 0


        data.append(endValue)
        if endValue == 0:
            break

        if minusNumber == 5:
            minusNumber = 0
        
        
    print("#{} {}".format(tc_input, " ".join(map(str, data))))
