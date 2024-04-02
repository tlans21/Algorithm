import math


def solution(n, k):
    answer = []
    l = []
    k -= 1
    for i in range(1, n + 1):
        l.append(i)
    
    while l:
        a = k // math.factorial(n-1)
        answer.append(l[a])
        del l[a]
        k = k % math.factorial(n-1)
        n -= 1
    
    return answer