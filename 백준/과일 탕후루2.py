# # N = int(input())

# # fruits = list(map(int, input().split()))
# # start = 0
# # end = 0
# # store = []
# # maxCnt = -1
# # # 시간 초과
# # while start < N and end < N: 
# #     if len(set(store)) <= 2:
# #         store.append(fruits[end])
# #         end += 1
# #     elif len(set(store)) > 2:
# #         store.pop(0)
# #         start += 1

# #     if start > end:
# #         print("break")
# #         break
    
# #     if len(set(store)) <= 2:
# #         maxCnt = max(maxCnt, len(store))

# # print(maxCnt)    


N = int(input())

fruits = list(map(int, input().split()))
start = 0
end = 0
fruits_cnt = [0 for _ in range(11)]
maxCnt = -1
store = set()
left = 0
right = 0

while right < N:
    fruits_cnt[fruits[right]] += 1
    store.add(fruits[right])
    right += 1
    while len(store) == 3:
        fruits_cnt[fruits[left]] -=1
        if fruits_cnt[fruits[left]] == 0:
            store.remove(fruits[left])
        left += 1
    maxCnt = max(maxCnt, right - left)

print(maxCnt)        

