T = int(input())

dict = {}
r_dict = {}

i = 1
j = 1

for k in range(1, 50000):
    dict[k] = (i, j)
    r_dict[(i, j)] = k
    i = i - 1
    j = j + 1

    if i == 0:
        i = j
        j = 1



for tc in range(1, T + 1):
    u, v = map(int, input().split())
   
    
    # 초기 값
    
        
    result_x1, result_y1 = dict[u]
    result_x2, result_y2 = dict[v]
    answer = r_dict[(result_x1 + result_x2, result_y1 + result_y2)] 
    
    print("#{} {}".format(tc, answer))





    
    
            

        

            