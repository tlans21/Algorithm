N = int(input())

data = []

for i in range(N):
    input_value = input().split()
    data.append((input_value[0], int(input_value[1])))

result = sorted(data, key=lambda x:x[2])

for x in result:
    print(x[0], end=' ')