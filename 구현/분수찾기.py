N = int(input())

line = 0

max_num = 0
while max_num < N:
    line += 1
    max_num += line
    

#line이 홀수인 경우 line이 분자
#line이 짝수 인경우 line이 분모

gap = max_num - N

if line % 2 == 0:
    top = line - gap
    bottom = gap + 1
elif line % 2 == 1:
    top = gap + 1
    bottom = line - gap

print(f'{top}/{bottom}')









