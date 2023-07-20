mo_sound = ['a', 'e', 'i', 'o', 'u']

while True:
    flag = True
    input_str = input()
    
    if input_str == 'end':
        exit(0)
    
    mo_cnt = 0

    for i in range(len(input_str)):
        
        cur_str = input_str[i]

        # 모음있으면 카운트
        if input_str[i] in mo_sound:
            mo_cnt += 1
        
        if i+2 < len(input_str):
            if cur_str in mo_sound and input_str[i+1] in mo_sound and input_str[i+2] in mo_sound:
                flag = False

            if cur_str not in mo_sound and input_str[i+1] not in mo_sound and input_str[i+2] not in mo_sound:
                flag = False

        if i+1 < len(input_str):
            if cur_str == input_str[i+1]:
                if cur_str != 'e' and cur_str != 'o':
                    flag = False
    if mo_cnt == 0:
        flag = False
    
    if flag == True:
        print(f'<{input_str}> is acceptable.')
    else:
        print(f'<{input_str}> is not acceptable.')
        

