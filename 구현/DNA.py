N, M = map(int, input().split())

DNA = []

for i in range(N):
    DNA.append(list(map(str, input())))

distance = 0
answer = ""
for i in range(M):
    a, c, g, t = 0, 0, 0, 0
    for j in range(N):
        if DNA[j][i] == 'A':
            a +=1
        elif DNA[j][i] == 'C':
            c += 1
        elif DNA[j][i] == 'G':
            g += 1
        elif DNA[j][i] == 'T':
            t += 1
    if max(a, c, g, t) == a:
        distance += (c + g + t)
        answer += 'A'
    elif max(a, c, g, t) == c:
        distance += (a + g + t)
        answer += 'C'
    elif max(a, c, g, t) == g:
        distance += (a + c + t)
        answer += 'G'
    elif max(a, c, g, t) == t:
        answer += 'T'
        distance += (a + c + g)

print(answer)
print(distance)







            



