#최대 최소 10818
#파이썬 내부함수인 max, min 활용 한 문제 풀이 
line = int(input())
number = list(map(int, input().split()))
print(min(number),max(number))



import random
#최대 최소2트 10818 
#내부 함수를 사용하지 않은 문제 풀이
line = int(input())
number = list(map(int, input().split()))
min = number(random.randrange(0,4))
max = number(random.randrange(0,4))