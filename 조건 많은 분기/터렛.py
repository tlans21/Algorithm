T = int(input())

board = [[0 for j in range(10000)] for i in range(10000)]

while T > 0:
    cnt = 0
    T -= 1
    x1, y1, r1, x2, y2, r2 = map(int ,input().split())
    for i in range(0, 100):
        for j in range(0, 100):
            
            dist1 = (((x1 - i) **2) + ((y1 - j) ** 2)) ** (0.5)
            dist2 = (((x2 - i) **2) + ((y1 - j) ** 2)) ** (0.5)

            if dist1 == r1 and dist2 == r2:
                print(i, j)
                cnt +=1
    
    print(cnt)
                 
    