T = 10
N = 8
for i in range(1, T+1):
    length = int(input())
    board = [list(input()) for _ in range(N)]
    answer = 0
    for u in range(N):
        for v in range(N):
            str = ""
            # 오른쪽 늘리기
            for l in range(0, length):
                if 0 <= v + length - 1 < 8:
                    str += board[u][v + l]
                    
            # 검사 
            # case 1) str의 길이가 짝수일때
            if not str == "":
                if len(str) % 2 == 0: 
                    half_length = len(str) // 2
                    for k in range(0, half_length):
                        if list(str)[k] != list(str)[len(str) - 1 - k]:
                            break
                    else:
                        
                        answer += 1
                else:
                    half_length = len(str) // 2
                    for k in range(0, half_length):
                        if list(str)[k] != list(str)[len(str) - 1 - k]:
                            break
                    else:
                        answer += 1

            str = ""
            # 아래로 늘리기
            for l in range(0, length):
                if 0 <= u + length - 1< 8:
                    str += board[u + l][v]
            
            if not str == "":
                if len(str) % 2 == 0: 
                    half_length = len(str) // 2
                    for k in range(0, half_length):
                        if list(str)[k] != list(str)[len(str) - 1 - k]:
                            break
                    else:
                        answer += 1
                else:
                    half_length = len(str) // 2
                    for k in range(0, half_length):
                        if list(str)[k] != list(str)[len(str) - 1 - k]:
                            break
                    else:
                        answer += 1
    print("#{} {}".format(i, answer))         
            