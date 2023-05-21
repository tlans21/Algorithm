

def solution(n, k):
    answer = -1
    
    def convertString(n, k):
        converts ="0123456789ABCDEF"
        q, r = divmod(n, k)
        if n < k :
            return converts[n]
        else:
            return convertString(q, k) + converts[r]
     
    str1 = convertString(n, k)
    def prime_number(s):
        cnt = 0
        if s < 2:
            return False
        end = int(s **(1/2))
        for i in range(2, end+1):
            if s % i == 0:
                return False
        return True
    
    cnt = 0
    str1 = str1.split('0')
    
    for i in range(len(str1)):
        if str1[i] == '':
            continue
        flag = prime_number(int(str1[i]))
        if flag == True:
            cnt +=1
     
    answer = cnt       
    return answer