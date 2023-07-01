A, P = map(int, input().split())

i = 0
D = [A]

while i <= 10000:
    dap = 0
    num = list(map(int, str(D[i])))
    i +=1
    for j in num:
        dap += j**P    
    # print(dap)
    
    if dap in D:
        break

    D.append(dap)




print(D.index(dap))