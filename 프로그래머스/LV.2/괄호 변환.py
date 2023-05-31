def isbalanced(str):
    cnt = 0
    for i in range(len(str)):
        if str[i] == '(':
            cnt+=1
        elif str[i] == ')':
            cnt -=1
        
        if cnt == 0:
            return True
    return False

def isCorrect(str):
    cnt1 = 0
    for i in range(len(str)):
        if str[i] == '(':
            cnt1 +=1
        elif str[i] == ')':
            cnt1 -=1
        
        if cnt1 < 0:
            return False
    return True
def splitUV(str):
    for i in range(len(str)):
        if isbalanced(str[:i+1]):
            u = str[:i+1]
            v = str[i+1:]
            break
    return u, v
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
def reverseStr(str):
    emptystr=""
    for i in str:
        if i == '(':
            emptystr +=')'
        elif i == ')':
            emptystr +='('
    return emptystr
def process(p):
    answer = '' 
    if p == "":
        return ""
    u, v = splitUV(p)
    if isCorrect(u):
        u += solution(v)
        return u
    else:
        answer +='('
        answer += solution(v)
        answer += ')'
        answer += reverseStr(u[1:-1]) 
        
    
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.
    return answer

def solution(p):
    return process(p)