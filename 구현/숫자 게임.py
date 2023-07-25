from itertools import combinations
N = int(input())

# 3장의 카드를 뽑아야함.

card = []
answer = []

# 1~10사이의 수를 받음
for i in range(N):
    card.append(list(map(int, input().split())))

for i in range(N):
    temp = 0
    #1~N번사람
    cur_list = card[i]
    # 조합
    com_lists = list(combinations(cur_list, 3))
    # 세 수의 합이 가장 큰 것을 선별하기 위함.
    
    for com_list in com_lists:
        
        sum = 0
        
        for k in range(len(com_list)):
             sum += com_list[k]
        loc = list(map(int, str(sum)))
        last_loc = loc[-1]
        temp = max(temp, last_loc)
    # 각 번호의 사람에서 최댓값과 그 사람의 번호를 저장
    answer.append((temp, i+1))

#temp가 내림차순으로 정렬합니다. 이긴 사람이 두명이상일 경우는 temp가 같은경우를 뜻합니다.
answer.sort(key=lambda x:(-x[0], -x[1]))

# temp가 가장 큰 경우가 게임에서 이긴 경우이고, 번호를 출력해야함.
print(answer[0][1])
