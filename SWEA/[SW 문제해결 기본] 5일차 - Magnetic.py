T = 10
for tc in (1, T+1):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    # 1은 아래로 2는 위로
    answer = 0
    # 21은 교착상태 없음, 12는 교착상태1개 , 122 교착상태 1개 1212 교착상태 2개
    for i in range(0, N):
        
        temp = ""
        for j in range(0, N):
            if board[j][i] != '0':
                temp += board[j][i]
        temp_list = list(temp)
        

        while True:
            if len(temp_list) == 0:
                break

            if temp_list[0] == '2':
                temp_list.pop(0)
            elif temp_list[-1] == '1':
                temp_list.pop()
            else:
                break
       
        temp = ""
        for temp_str in temp_list:
            temp += temp_str
        
        cnt = temp.count("12")
        
        answer += cnt
    
    print("#{} {}".format(tc, answer))
        
        