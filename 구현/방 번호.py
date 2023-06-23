N = input()

# 6과 9의 갯수를 세기위한 count1
count1 = 0
# 0,1,2,3,4,5,7,8을 세기위한 count2
count2 = 0

dic = dict()

for num in N:
    if num == '6' or num == '9':
        count1 += 1
    else:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] +=1
temp = 0
for i in dic.keys():
    temp = max(temp, dic[i])

set2 = temp

if count1 % 2 == 1:
    set1 = (count1 // 2) + 1
else:
    set1 = (count1 // 2)

#set1과 set2에서 가장 큰 것을 고른다.

answer = max(set1, set2)
print(answer)
