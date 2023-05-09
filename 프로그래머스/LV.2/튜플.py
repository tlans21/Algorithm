def solution(s):
    answer = []
    
    #첫번째 {, 마지막 }을 벗겨줘야한다.
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key = len)
    # ['2', '2,1' ... ]
    for i in s:
        str = i.split(',')
        for j in str:
            if int(j) not in answer:
                answer.append(int(j))
    return answer