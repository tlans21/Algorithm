N = int(input())

car_dict = dict()

for i in range(N):
    input_car = input()
    car_dict[input_car] = i


out = []
for i in range(N):
    car = input()
    out.append(car)

answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        if car_dict[out[i]] > car_dict[out[j]]:
            answer +=1
            break

print(answer)

