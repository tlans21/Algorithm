T = 10
N = 100

for tc in range(1, T + 1):
    num = int(input())
    board = [list(input()) for _ in range(N)]
    length_list = []
    answer = -1

    for i in range(N):
        for j in range(N):
            # 기준점 
            # 오른쪽으로 진행    
            
            
            
            # 검사 횟수
            str = ""
            cnt = N-j
            for k in range(cnt):
                str += board[i][j+k]
                # 더 할때마다 검사를 진행
                for s in range(len(str)// 2):
                    if str[s] != str[len(str) - s - 1]:
                        break
                else:
                    length_list.append(len(str))
            # 왼쪽으로 진행
            str = ""
            for k in range(cnt):
                str += board[j+k][i]
                # 더 할때마다 검사를 진행
                for s in range(len(str)//2):
                    if str[s] != str[len(str) - s - 1]:
                        break
                else:
                    length_list.append(len(str))
    answer = max(length_list)
    print("#{} {}".format(num, answer))


        

            