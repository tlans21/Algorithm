T = int(input())

input_list = []

while T:
    case = int(input())
    input_list.append(case)
    T -= 1

# 2, 3, 5, 7, 11로 분해되어야함.

cnt_2, cnt_3, cnt_5, cnt_7, cnt_11 = 0, 0, 0, 0, 0

for idx, value in enumerate(input_list):
    cnt_2, cnt_3, cnt_5, cnt_7, cnt_11 = 0, 0, 0, 0, 0
    while value != 1:
        # 2 로 나눠지면
        if value % 2 == 0:
            value = value // 2
            cnt_2 = cnt_2 + 1
        elif value % 3 == 0:
            value = value // 3
            cnt_3 = cnt_3 + 1
        elif value % 5 == 0:
            value = value // 5
            cnt_5 = cnt_5 + 1
        elif value % 7 == 0:
            value = value // 7
            cnt_7 = cnt_7 + 1
        elif value % 11 == 0:
            value = value // 11
            cnt_11 = cnt_11 + 1
    print("#" + f"{idx + 1}" + " " + f"{cnt_2}"+ " " + f"{cnt_3}"+ " " + f"{cnt_5}"+ " " + f"{cnt_7}"+ " " + f"{cnt_11}")
    

