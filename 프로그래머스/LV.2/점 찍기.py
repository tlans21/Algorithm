import math
# 시간초과 코드
def solution(k, d):
    answer = 0
    a = 0
    b = 0
    x = 0
    y = 0
    cnt = 0
    while a*k <= d:
        x = a * k
        while True:
            y = b * k
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            
            if distance > d:
                break
            else:
                cnt += 1
            b += 1
        b = 0
        a += 1
    answer = cnt

    return answer


# 