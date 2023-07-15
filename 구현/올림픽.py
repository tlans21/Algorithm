N, K = map(int, input().split())
lst = []
for i in range(N):
     lst.append(list(map(int, input().split(' '))))

lst.sort(key=lambda x: (-x[1], -x[2], -x[3]))

idx = 0
for i in range(N):
     if lst[i][0] == K:
          idx = i
          break

for i in range(N):
    if lst[idx][1:] == lst[i][1:]:
        print(i+1)
        break
         

