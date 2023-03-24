N, M = map(int, input().split())

list1 = list(map(int, input().split()))
answer = 0
for i in range(N):
    for j in range(i, N):
        if list1[i] != list1[j]:
            answer +=1

print(answer)