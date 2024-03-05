def solution(survey, choices):
    answer = ''
    #2시 32분
    # N : 1, C : 1 , M : 2, T : 3  A : 1 => 사전 순 TM
    
    dict = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0 , 'N' : 0}

    for i in range(0, len(choices)):
        if choices[i] < 4:   
            dict[survey[i][0]] += -choices[i] + 4
        elif choices[i] == 4:
            continue     
        elif choices[i] > 4: 
            dict[survey[i][1]] += choices[i] - 4
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dict)
    mind_board = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    
    for i in range(4):
        a_list = []
        if dict[mind_board[i][0]] > dict[mind_board[i][1]]:
            answer += mind_board[i][0]
        elif dict[mind_board[i][0]] < dict[mind_board[i][1]]:
            answer += mind_board[i][1]
        else:
            # 사전순
            a_list.append(mind_board[i][0])
            a_list.append(mind_board[i][1])
            sorted_list = sorted(a_list)
            answer += sorted_list[0]
    return answer