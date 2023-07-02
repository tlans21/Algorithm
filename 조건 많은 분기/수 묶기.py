N = int(input())

plus = []
minus = []
sum = 0
zeroCnt = 0
for i in range(N):
    input_num = int(input())
    if input_num > 1:
        plus.append(input_num)
    elif input_num <= 0:
        minus.append(input_num)
    elif input_num == 1:
        sum+=1


plus.sort(reverse=True)
minus.sort()


if len(plus) % 2 == 0:
    for i in range(0, len(plus), 2):
        sum += (plus[i]* plus[i+1])
else:
    for i in range(0, len(plus)-1, 2):
        sum += (plus[i]* plus[i+1])
    sum += plus[-1]

if len(minus) % 2 == 0 :
    for i in range(0, len(minus), 2):
        sum += minus[i] * minus[i+1]
else:
    for i in range(0, len(minus)-1, 2):
        sum += minus[i] * minus[i+1]
    sum += minus[-1]

print(sum)
    





    
    



    

