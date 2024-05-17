from itertools import combinations
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    input_lst = list(map(int, input().split()))
    

    # 값 2개씩 계산
    combs = combinations(input_lst, 2)
    answer = [-1]
    for comb in combs:
        first = comb[0]
        seocnd = comb[1]
        operation = (first * seocnd)
        
        # 굳이 계산 x
        if max(answer) > operation:
            continue
        tmp_lst = list(map(int, str(operation)))
        now = tmp_lst[0]
        for tmp in tmp_lst:
            if now > tmp:
                break
            now = tmp
        else:
            answer.append(operation)
    print("#{} {}".format(tc, max(answer)))
        


