# 주어진 문자열의 길이가 짝수일때는 모든 원소의 길이가 짝수여야한다.
# 주어진 문자열의 길이가 홀수일때는 하나만 홀수여야한다.
str_list = [] # 정답이 여러개일때 sort를 이용해 문자순으로 정렬
arr_str = input()
str_length = len(arr_str)

dic = dict()

for i in arr_str:
    if i not in dic:
        dic[i] = 1
    elif i in dic:
        dic[i] +=1
# 정렬된 키
keys = sorted(dic.keys())
# 홀수 키
odd_key = ""
for key in keys:
    if dic[key] % 2 == 1:
        if odd_key == '':
            odd_key = key
        else:
            print("I'm Sorry Hansoo")
            exit(0)
answer = ""
temp = ""
for key in keys:
    cnt = dic[key] // 2
    temp += key * cnt
    
answer += temp

if odd_key != "":
    answer += odd_key
answer += temp[::-1]

print(answer)