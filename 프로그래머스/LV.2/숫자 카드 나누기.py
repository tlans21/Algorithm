import math
# try 1 : 시간 초과
# def check(arrayA, arrayB):
#     cnt_store = []
#     for cnt in range(2, max(arrayA)):
#         for element in arrayA:
#             if element % cnt != 0:
#                 break
#         else:
#             cnt_store.append(cnt)
    
#     if cnt_store == []:
#         return 0
    
            
#     result = []
    
#     for cnt in cnt_store:
#         for element in arrayB:
#             if element % cnt == 0:
#                 break
#         else:
#             result.append(cnt)
    
#     if result == []:
#         return 0
#     else:
#         return max(cnt_store)

# def solution(arrayA, arrayB):
#     answer = 0
    
#     if check(arrayA, arrayB) == 0:
#         answer = check(arrayB, arrayA)
#     else:
#         answer = check(arrayA, arrayB)
#     return answer


import math

def canDivde(array, gcd):
    for num in array:
        if num % gcd == 0:
            return False
    return True


def solution(arrayA, arrayB):
    answer = 0
    gcd_A = arrayA[0]
    gcd_B = arrayB[0]
    
    for num in arrayA:
        gcd_A = math.gcd(num, gcd_A)
    
    for num in arrayB:
        gcd_B = math.gcd(num, gcd_B)
    
    if canDivde(arrayA, gcd_B):
        answer = max(answer, gcd_B)
    
    if canDivde(arrayB, gcd_A):
        answer = max(answer, gcd_A)
    
    
    return answer