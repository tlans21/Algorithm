import math
def solution(w,h):
    answer = 0
    gcd_value = math.gcd(w, h)
    answer = w*h - (gcd_value *((w // gcd_value) + (h // gcd_value) - 1))
    
    
    return answer