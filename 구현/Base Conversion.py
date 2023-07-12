A, B = map(int, input().split(' '))
N = int(input())

data = list(map(int, input().split(' ')))

sum = 0
answer = []
# n진법을 10진법으로 변환
for i in range(N):
    sum += data.pop() * (A ** i)

while sum > 0:
    q, r = divmod(sum, B)
    sum = q
    answer.append(r)


while len(answer) != 0:
    print(answer.pop(), end=' ')
