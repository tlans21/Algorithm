s = int(input())
num_list = list(map(int, str(s)))

sum = 0
for i in range(0, len(num_list)):
    if num_list[i] == 1:
        if i+1 < len(num_list) and num_list[i+1] == 0:
            sum += 10
            i = i+1
            continue
        else:
            sum += num_list[i] 
            continue
    else:
        sum += num_list[i]
print(sum)