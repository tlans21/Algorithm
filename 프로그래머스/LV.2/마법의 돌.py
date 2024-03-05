def solution(storey):
    
    count_list = []
    # 엘리베이터가 위치한 층과 버튼의 값을 더한 결과가 0보다 작으면 움직이지 않는다.
    # 가장 아래층이 0층이다
    
    # 움직이는데는 마법의 돌 1개 소모
    # 마법의 돌을 최소한으로 해야함.
    
    def dfs(st, count):
        if st == 0:
            count_list.append(count)
            return
        
        loc_first = st % 10  # 첫번째 자리
        up, down = 10 - loc_first, loc_first
        
        if up < down:
            dfs((st//10) + 1, count + up)
        elif up > down:
            dfs(st//10, count + down)
        else:
            for i in range(2):
                dfs((st//10) + i, count + up)
                
    dfs(storey, 0)
    answer = min(count_list)
    
    return answer