N = int(input())

str_list = list()
for i in range(0, N):
    str_list.append(input())

flag = True # 단어가 연속되지 않은 상태면 False, 연속된 true

count = 0
for str1 in str_list:
    pre_str = str1[0]
    dic = dict()
    dic[pre_str] = 1
    # 1개일땐 무조건 1개
    if len(str1) == 1:
        count +=1
        continue

    for i in str1[1:]:
        cur_str = i 

        if cur_str != pre_str:
            if cur_str not in dic:
                dic[cur_str] = 1 
            else:
                 flag = False
                 break
        elif cur_str == pre_str:
            if cur_str not in dic:
                dic[cur_str] = 1
            else:
                dic[cur_str] +=1
        pre_str = cur_str
    if flag == True:
        count +=1
    elif flag == False:
        flag = True

print(count)