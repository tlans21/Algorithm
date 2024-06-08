
N = int(input())

fruits = list(map(int, input().split()))

start = 0
end = 0

answer = [fruits[0]]
maxLength = -1
while True:
    if len(answer) <= 2:
        maxLength = max(maxLength, end - start + 1)
        end += 1
        if end >= N:
            break
        


    