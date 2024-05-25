T = 10

for tc in range(1, T+1):
    N = int(input())
    input_str = input()

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    # idea : 여는 괄호일때 +1, 닫는 괄호 일때 -1, cnt값이 마이너스 값이 되는순간을 리턴한다. 짝을 찾을 수 없기 때문.
    # 마지막은 cnt 값들이 모두 0이 되어야함.

    for string_value in input_str:
        if cnt1 < 0 or cnt2 < 0 or cnt3 < 0 or cnt4 < 0: 
            break

        if string_value == '{':
            cnt1 += 1
        elif string_value == '(':
            cnt2 += 1
        elif string_value == '[':
            cnt3 += 1
        elif string_value == '<':
            cnt4 += 1
        elif string_value == '}':
            cnt1 -=1
        elif string_value == ')':
            cnt2 -=1
        elif string_value == ']':
            cnt3 -=1
        elif string_value == '>':
            cnt4 -=1

    if cnt1 == 0 and cnt2 == 0 and cnt3 == 0 and cnt4 == 0:
        print("#{} {}".format(tc, 1))    
    else:
        print("#{} {}".format(tc, 0))
    