input_num = list(map(str, input()))
cnt = 0
temp_sum = 0
first_num = input_num
for i in range(len(first_num)):
    temp_sum += int(first_num[i])
if 0 <= temp_sum <= 9:
    print(0)
    if temp_sum % 3 == 0:
        print("YES")
    else:
        print("NO")
    exit(0)
while True:
    
    
    sum = 0
    for i in range(len(input_num)):
        sum += int(input_num[i])
    cnt += 1 
    
    if 0 <= sum <= 9:
        break
    input_num = list(map(str, str(sum)))

if sum % 3 != 0:
    print(cnt)
    print("NO")
else:
    print(cnt)
    print("YES")