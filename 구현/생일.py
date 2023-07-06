N = int(input())

lst = []

for i in range(N):
    name, days, months, years = input().split()
    lst.append((name, int(days), int(months), int(years)))

lst.sort(key = lambda x : (x[3], x[2], x[1]))


print(lst[-1][0])
print(lst[0][0])