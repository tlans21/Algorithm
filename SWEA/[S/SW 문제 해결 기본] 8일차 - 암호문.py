T = 10
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    commendNumber = int(input())
    commend = list(map(str, input().split('I')))
    
    for i in commend:
        commend_list = list(map(int, i.split()))
        if len(commend_list) == 0:
            continue
        
        for j in range(commend_list[1]):
            numbers.insert(commend_list[0] + j, commend_list[j + 2])
    print("#{} {}".format(tc, ' '.join(map(str, numbers[:10]))))

