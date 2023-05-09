N = int(input())
data = []

for i in range(N):
    data.append(int(input()))

# 최소한의 합을 가져야합니다. 카드를 뭉쳤을때,
# 따라서 오름차순 정렬이 필요합니다.

data = sorted(data)
sum = data[0]
list = []
answer = 0

if N == 1:
    print(0)
else:
    for i in range(1, len(data)):
        sum += data[i]
        list.append(sum)

    for i in list:
        answer +=i

    print(answer)

