N = int(input())

human = []

for i in range(N):
    human.append(int(input()))
answer = 0
if len(human) == 1:
    print(answer)
    exit(0)
    
while True:
    temp = -1
    for i in range(1, N):
        if temp < human[i]:
            temp = human[i]
            idx = i
    if human[0] <= human[idx]:
        answer += 1
        human[0] += 1
        human[idx] -= 1
    else:
        break
print(answer)        
