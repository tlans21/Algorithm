def solution(players, callings):
    answer = []
    dict = {}
    dict2 = {}
    
    for i in range(0, len(players)):
        dict[players[i]] = i + 1
        dict2[i+1] = players[i]
    
    for name in callings:
        back_player = name
        # 현재 등수
        current_rank = dict[back_player] 
        # 더한 등수 
        plus_rank = current_rank - 1
        
        front_player = dict2[plus_rank]
        
        dict[back_player] = plus_rank
        dict[front_player] = current_rank
        dict2[plus_rank] = back_player
        dict2[current_rank] = front_player
    
    answer = list(dict2.values())
    
    
    return answer