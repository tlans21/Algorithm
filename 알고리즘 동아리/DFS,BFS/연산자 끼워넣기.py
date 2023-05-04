#중복 순열 사용문제

N = int(input())

data = list(map(int, input().split()))
plus, minus, mutiple, divide = map(int, input().split())

mins = 123456789
maxs = -123456789

result = data[0]
def combination(depth, result):
    global mins
    global maxs
    global plus, minus, mutiple, divide
    if depth == N:
        mins = min(result, mins)
        maxs = max(result, maxs)
        return
    
    if plus != 0:
        plus = plus - 1
        combination(depth+1, result+data[depth])
        plus = plus + 1
    if minus != 0:
        minus = minus - 1    
        combination(depth+1, result-data[depth])
        minus = minus + 1
    if mutiple != 0:
        mutiple = mutiple - 1
        combination(depth+1, result*data[depth])
        mutiple = mutiple + 1
    if divide != 0:
        divide = divide - 1    
        combination(depth+1, int(result/data[depth]))
        divide = divide + 1

combination(1, data[0])
print(maxs)
print(mins)