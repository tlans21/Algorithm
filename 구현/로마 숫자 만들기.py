#  시간 초과
#  from itertools import product

# N = int(input())

# dic = {'l' : 1, 'V': 5, 'X' : 10, 'L': 50}
# str_list = ['l', 'V', 'X', 'L']
# sum_dict = dict()
# product_list = product(str_list, repeat = N)

# cnt = 0

# for pro in product_list:
#     sum = 0
#     for element in pro:
#         sum += dic[element]
    
#     if sum not in sum_dict:
#         cnt += 1
#         sum_dict[sum] = 1
#     else:
#         sum_dict[sum] += 1

# print(cnt)

from itertools import combinations_with_replacement

N = int(input())

dic = {'l' : 1, 'V': 5, 'X' : 10, 'L': 50}

str_list = ['l', 'V', 'X', 'L']
cnt = 0
data_list = list(combinations_with_replacement(str_list, N))
sum_dict = dict()
for data in data_list:
    sum = 0
    for element in data:
        sum += dic[element]
    
    if sum not in sum_dict:
        cnt += 1
        sum_dict[sum] = 1
        
print(cnt)