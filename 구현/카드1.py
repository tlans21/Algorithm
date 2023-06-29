from collections import deque
N = int(input())

card = deque()
for i in range(1, N+1):
    card.append(i)

answer = []
while len(card) != 1:
    
    remain = card.popleft()
    answer.append(remain)
    card.append(card.popleft())
lastCard = card.popleft()

answer.append(lastCard)

for i in answer:
    print(i, end =' ')