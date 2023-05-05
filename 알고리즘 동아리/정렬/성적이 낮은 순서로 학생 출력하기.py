N = int(input())

data = []

for i in range(N):
    input_value = input().split()
    data.append((input_value[0], int(input_value[1])))

data = sorted(data, key=lambda x:x[1])

for x in data:
    print(x[0], end=' ')