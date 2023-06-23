visit = [0 for i in range(1, 10002)]

sum = 0
for i in range(1, 10001):
    cur = i
    while cur <= 10000:
        sum = 0
        str_num = str(cur)
        sum += cur
        for j in str_num:
            sum += int(j)
        if sum > 10000:
            break
        visit[sum] +=1 
        cur = sum 

for i in range(1, 10001):
    if visit[i] == 0:
        print(i)         
    