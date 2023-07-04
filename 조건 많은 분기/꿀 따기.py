N = int(input())

lst = list(map(int, input().split()))

prefix_sum = []
prefix_sum.append(lst[0])

for i in range(1, N):
    prefix_sum.append(prefix_sum[i-1] + lst[i])

# 세가지의 경우로 나눠야한다. 꿀통이 왼쪽에 있는 경우와 오른쪽에 있는 경우, 중간에 있는 경우.

#꿀통이 왼쪽에 있는 경우, 꿀벌 1은 맨 오른 쪽에 있고 꿀벌 2는 꿀통과 꿀벌1의 인덱스를 제외한 중간에서 찾아야한다.

# 꿀 벌 벌 인경우
temp = 0
for i in range(1, N-1):
    # prefix_sum[n-2]는 오른쪽 끝에 있는 꿀벌 1 자기 자신의 꿀의 값을 제외한 누적합이다.
    temp = max(temp, prefix_sum[i] - lst[i] + prefix_sum[N-2] - lst[i])



# 벌벌꿀인 경우
# 
for i in range(1, N-1):
    
    temp = max(temp, prefix_sum[N-1] - lst[0] - lst[i] + prefix_sum[N-1] - prefix_sum[i])

# 벌 꿀 벌인 경우
for i in range(1, N-1):
    temp = max(temp, prefix_sum[i] - lst[0] + prefix_sum[N-2] - prefix_sum[i] + lst[i])
    

print(temp)