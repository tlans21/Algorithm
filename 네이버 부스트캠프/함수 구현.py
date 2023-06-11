def hamsu(arr):
    answer = []
    sorted(arr)
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1
    
    for i in dic.keys():
        if dic[i] > 1:
            answer.append(dic[i])
    
    if len(answer) == 0:
        return [-1]
    else:
        return answer
arr1 = [3, 5 , 7, 9 , 1]    
solution = hamsu(arr1)
print(solution)