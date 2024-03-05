def solution(a, b):
    answer = ''
    sum_month = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335] 
    

    sum = sum_month[a-1] + b
    # 1, 2, 3, 4, 5, 6, 7, 8, ..
    # 금 토 일 월 화 수 목 금
    
    if sum % 7 == 1:
        answer = "FRI"
    elif sum % 7 == 2:
        answer = "SAT"
    elif sum % 7 == 3:
        answer = "SUN"
    elif sum % 7 == 4:
        answer = "MON"
    elif sum % 7 == 5:
        answer = "TUE"
    elif sum % 7 == 6:
        answer = "WED"
    elif sum % 7 == 0:
        answer = "THU"    
    
    return answer