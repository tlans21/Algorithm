T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split()) # N :사람 수 # M 초 시간을 들이면 K개의 붕어빵 만들수있음.

    # 각 사람이 언제 도착하는지 시간 초
    # 도착하는 순서가 오름차순으로 정렬이 필요해보임.
    # 정렬 된 순으로 차례로 제공
    clients = list(map(int, input().split()))
    clients.sort()
    cnt = 1
    flag = True
    for client in clients:
        # client는 오는 손님 순으로
        breadCnt = (client // M) * K  # 만들어진 붕어빵 수

        if breadCnt - cnt < 0:
            flag = False
            break
        cnt += 1

    if flag == True:
        print("#{} {}".format(tc, "Possible")) 
    else:
        print("#{} {}".format(tc, "Impossible"))   
