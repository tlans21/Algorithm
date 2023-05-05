N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

result = sorted(array, reverse=True)

print(result)