def solution(id_list, report_list, k):
    answer = []
    # result 결과 메일 수
    dict = {}
    dict_2 = {}
    report_set = set(report_list)
    report_list = list(report_set)
    
    
    for id in id_list:
        dict[id] = 0
        dict_2[id] = 0
    
    
    for report in report_list:
        first, second = report.split(' ')
        # 신고 당한 횟수 카운트
        dict_2[second] +=1
        
    for report in report_list:
        first, second = report.split(' ')
        if dict_2[second] >= k:
            dict[first] += 1
    
    for id in id_list:
        answer.append(dict[id])
    return answer