from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
   
    
    # 1:1 비율
    for key, value in counter.items():
        if value >= 2:
            # nC2 발생
            answer += (value * (value - 1)) / 2
            print((value * (value - 1)) / 2)
    
    # 그외의 비율들은 set를 통해서 중복 제거
    weights = set(weights)
    
    for weight in weights:
        if weight * 2/3 in weights:
            answer += counter[weight] * counter[weight * 2/3]
        if weight * 2/4 in weights:
            answer += counter[weight] * counter[weight * 2/4]
        if weight * 3/4 in weights:
            answer += counter[weight] * counter[weight * 3/4]
    
    
    
    
    
    return answer