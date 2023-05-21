def solution(sequence, k):
    answer = []
    l, r  = 0, -1
    answer_l = 0
    answer_r = 0
    temp = 123456789
    sum = 0
    while True:
        if sum < k:
            r +=1
            if r >= len(sequence):
                break
            sum += sequence[r]
        elif sum >=k:
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l +=1
        
        if sum == k:
            if temp > r-l:
                temp = r-l
                answer_r = r
                answer_l = l
        
    answer.append(answer_l)
    answer.append(answer_r)
    return answer