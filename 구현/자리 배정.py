C, R = map(int, input().split())
answer = int(input())
#좌 #상 # 우 # 하

map = [[0 for j in range(C)] for i in range(R)]

if C*R < answer:
    print(0)
    exit(0)

rotation = min(((C-1) // 2) +   1, ((R-1) // 2) + 1)


cnt = 1
for r in range(0, rotation):
    x = R-1 - r
    y = r
    #좌
    for i in range(R-1-(r*2)):
         
        map[x][y] = cnt
        
        if map[x][y] == answer:
            print(y+1, R-x)
            exit(0) 
        x -= 1
        cnt += 1
        
    # 상
    for i in range(C-1-(r*2)):
        
        map[x][y] = cnt
        
        if map[x][y] == answer:
            print(y+1, R-x)
            exit(0)
        
        cnt +=1
        y += 1
    # 우
    for i in range(R-1-(r*2)):
        
        map[x][y] = cnt
        
        if map[x][y] == answer:
            print(y+1, R-x)
            exit(0)
        cnt +=1
        x += 1

    #하
    for i in range(C-1-(r*2)):
        map[x][y] = cnt
        

        if map[x][y] == answer:
            print(y+1, R-x)
            exit(0)
        cnt += 1
        y -= 1    

