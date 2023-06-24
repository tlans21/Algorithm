# 1트 예외를 생각하지 않은 방식
N = (input())

length = len(N)

sum = 0
for i in range(1, length):
    sum += i * (9 * 10 **(i-1))

sum += ((int(N) - 10 **(length-1))+1) * length 
print(sum)