from itertools import permutations

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = int(input())

quest = []
for i in range(N):
    quest.append(list(map(int, input().split())))

permutations_list = list(permutations(data, 3))

answer = 0

for permutation in permutations_list:
    cnt = 0 
    for i in range(len(quest)):
        strike = 0
        ball = 0
        num_str = list(map(int, str(quest[i][0])))
        for j in range(0, 3):
            if permutation[j] == num_str[j]:
                strike += 1
            elif permutation[j] != num_str[j]:
                if num_str[j] in permutation:
                    ball +=1
        
        if quest[i][1] == strike and quest[i][2] == ball:
            cnt += 1
        else:
            break
    if cnt == len(quest):
        answer +=1
print(answer)                    
            

                
