T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = [0]
    # 얻을 수 있는 최대 점수를 길이로 한다.
    # 0점은 가능하므로 1로 표시, 가능하지 않다면 0
    temp = [0]
    # 숫자는 하나씩 밖에 못쓰기 때문에, for문 제일 앞에 위치
    for number in numbers:
        for i in range(len(result)):
            temp.append(result[i] + number)
        result = list(set(temp))
    print(f'#{tc} {len(result)}') 

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    result = [0]
    temp = [0]
    for i in range(N):
        for j, val in enumerate(result):
            temp.append(result[j]+score[i])
        result = list(set(temp))
    print(f'#{test_case} {len(result)}')
    
    