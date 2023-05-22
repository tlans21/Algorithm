from itertools import combinations


def solution(orders, course):
    answer = []
    
    for i in course:
        dic = {}
        for menu in orders:
            combi = combinations(sorted(menu), i)
            for j in combi:
                if j in dic:
                    dic[j] += 1
                elif j not in dic:
                    dic[j] = 1
        if len(dic) != 0 and max(dic.values()) != 1:
            for k in dic.keys():
                if dic[k] == max(dic.values()):
                    answer += [''.join(k)]
    
                
            
            
        
    return sorted(answer)