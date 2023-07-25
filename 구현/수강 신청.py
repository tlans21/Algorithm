# # 구현 방법 1 == '시간 초과'
# from collections import deque

# # 버튼 활성한 후, 버튼 누른 순으로 대기목록에 들어감
# # 대기목록에 있는 상태에서 다시 버튼 누를시 뒤로 다시 들어감
# # 버튼 비활성시, 대기목록 가장 앞에서부터 하나씩 수강신청이 되며, 수강인원이 꽉찰 경우 대기목록 무시후 수강신청 종료

# K, L = map(int, input().split())

# # K : 수강 가능 인원
# # L : 대기 목록 길이면서 순서대로 버튼을 클릭한 사람들
# # wait_queue는 큐다.

# wait_queue = deque()
# remove_list = []
# for i in range(L):
#     # 문자열로 입력받아야 제일 첫번째 자리가 0인 학번을 받을 수 있다.
#     wait_queue.append(input())


# for i in range(len(wait_queue)-1):
#     cur_person = wait_queue[i]
#     for j in range(i+1, len(wait_queue)):
#         if cur_person == wait_queue[j]:
#             remove_list.append(cur_person)
#             break
        
   
# for i in range(len(remove_list)):
#     wait_queue.remove(remove_list[i])

# for i in range(K):
#     print(wait_queue[i])


# 구현 방법 2

# K, L = map(int, input().split())

# wait_queue = []
# dic = dict()
# for i in range(L):
#     num = input()
#     wait_queue.append(num)
#     if num not in dic:
#         dic[num] = 1
#     else:
#         dic[num] += 1
# i = 0
# answer = []

# while i < L:
#     if len(answer) == K:
#         break
#     if dic[wait_queue[i]] == 1:
#         answer.append(wait_queue[i])
#         i += 1
#         continue
#     else:
#         for s in range(i+1, i+1+K):
#             if s < len(wait_queue):
#                 if wait_queue[i] == wait_queue[s]:
#                     dic[wait_queue[i]] -= 1
#                     i += 1
#                     continue

# print(answer)        

# 구현 방법 3

import sys
input =sys.stdin.readline
K, L = map(int, input().rstrip().split())


dic = dict()

for i in range(L):
    num = input().rstrip()
    # 들어온 순서에 대한 학번
    dic[i] = num


dic = dict(sorted(dic.items()))

two_dic = dict()
for key, value in dic.items():
    two_dic[value] = key

two_dic = sorted(two_dic.items(), key=lambda x:x[1])

cnt = 0
for key, value in two_dic:
    if cnt == K:
        break
    print(key)
    cnt +=1
