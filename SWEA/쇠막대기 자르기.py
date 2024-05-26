T = int(input())

for tc in range(1, T+1):
    input_str = input()

    #################################
    stick = 0
    answer = 0
    for i in range(len(input_str)):
        if input_str[i] == '(':
            if i + 1 < len(input_str):
                if input_str[i + 1] != ')':
                    # 레이저로 판정하지 않고 막대기로 판정.
                    stick += 1
                else:
                    # 레이저로 판정하므로 현재의 막대기에서 반으로 가름.
                    if stick > 0:
                        answer += stick
        elif input_str[i] == ')':
            if i + 1 < len(input_str):
                if input_str[i + 1] == ')':
                    stick -= 1
                    answer += 1
            
    print("#{} {}".format(tc, answer))
   
        
            
            
