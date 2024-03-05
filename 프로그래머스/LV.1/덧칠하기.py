def solution(n, m, section):
    answer = 0
    # 연속되는 덩어리의 갯수를 체크하고, 그 길이를 측정해서 m과 비교하여 칠하는 갯수를 카운트한다.
    
    sum = 1
    start_paint = section[0] # 시작점
    
    for i in range(1, len(section)):
        if section[i] - start_paint + 1 > m:
            sum += 1
            start_paint = section[i]
        
        
    answer = sum
    return answer