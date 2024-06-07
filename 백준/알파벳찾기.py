S = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = []
cnt = 0
for alphabet in alpha:
    flag = False
    for i in range(len(S)):
        if S[i] == alphabet:
            answer.append(i)
            flag = True
            break
    if flag == False:
        answer.append(-1)

print(" ".join(map(str, answer)))      


for alphabet in alpha:
    if alphabet in S:
        print(S.index(alphabet))  
    else:
        print(-1)