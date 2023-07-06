for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())


    #겹치는 부분의 직사각형, x1 < x2 and y1 < y2 and  p1 > p2 and q1 > q2
    if p1 < x2 or p2 < x1 or q1 < y2 or y1 > q2:
        print('d')
        continue
    elif x1 == p2 or x2 == p1:
        if y1 == q2 or y2 == q1:
            print('c')
            continue
        else:
            print('b')
            continue
    elif q1==y2 or q2== y1:
        print('b')
        continue
    else:
        print('a')
        continue