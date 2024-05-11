T = 10

for tc in range(1, T + 1):
    _ = int(input())
    N = 100
    maps = [list(map(int, input().split())) for _ in range(N)]
    d1 = 0
    d2 = 0
    answer = 0
    # 열 값
    for i in range(N):
        sum_row = 0
        sum_column = 0
        for j in range(N):
            sum_row += maps[i][j]
            sum_column += maps[j][i]

        answer = max(sum_column, sum_row, answer)
    
        d1 += maps[i][i]
        d2 += maps[i][N-i-1]

    answer = max(d1, d2, answer)

   
    print("#{} {}".format(tc, answer))

T = 10
 
for test_case in range(1, T + 1) :
  _ = int(input())
  N = 100
  maps = [list(map(int, input().split())) for _ in range(N)]
 
  answer = 0
  d1 = 0
  d2 = 0
  
 
  for i in range(N) :
    sum_row = 0
    sum_column = 0
 
    for j in range(N) :
      sum_row += maps[i][j]
      sum_column += maps[j][i]
 
    ans = max(ans, s3, s4)
 
    s1 += lst[i][i]
    s2 += lst[i][N-i-1]
 
  ans = max(ans, s1, s2)
 
  print("#{} {}".format(test_case, ans))