def solution(rows, columns, queries):
    answer = []
       
    square = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            square[row][col] = t
            t += 1
        
    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        tmp = square[x1][y1]
        min_value = tmp
        # 왼쪽 세로
        for k in range(x1, x2):
            square[k][y1] = square[k + 1][y1]
            min_value = min(min_value, square[k + 1][y1])
        # 아래 가로
        for k in range(y1, y2):
            square[x2][k] = square[x2][k + 1]
            min_value = min(min_value, square[x2][k + 1])
        #오른쪽 세로
        for k in range(x2, x1, -1):
            square[k][y2] = square[k-1][y2]
            min_value = min(min_value, square[k][y2])
        # 위 가로
        for k in range(y2, y1, -1):
            square[x1][k] = square[x1][k-1]
            min_value = min(min_value, square[x1][k])
        square[x1][y1 + 1] = tmp
        answer.append(min_value)
     
    return answer