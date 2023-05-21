def solution(n,a,b):
    answer = 0
    # 35분
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    a_idx = a - 1
    b_idx = b - 1
    round = 1
    
    while True:
        if a_idx == b_idx:
            break
        a_idx = a_idx // 2
        b_idx = b_idx // 2
        round +=1
        
    answer = round-1
    return answer