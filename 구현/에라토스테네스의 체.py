# 58분 소요
N, K = map(int, input().split())

#1.  N = 7,  2~7에서 소수를 찾는다.
#2. 지우지 않은 수 중 가장 작은 수를 찾는데, 이 수는 소수이다.
#ex) 2, 4, 6 까지 3번째 지움
# 3지움 4번째
# 4는 지워져있음
# 5는 지움 5번째
# 7도 지움 6번째

def checkPrimeNumber(n):
    # False시 소수가 아님을, True시 소수를 의미함.
    if n == 2:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

visit = [0 for _ in range(N+2)]
cnt = 0

for i in range(2, N+1):
    cnt1 = 1
    if visit[i] == 0:
        if checkPrimeNumber(i) == False:
            print(i)
            continue
        else:
            cnt += 1
            visit[i] = cnt
    else:
        continue
    
    
    # 소수인 경우 배수처리하여 카운트
    
    cur = i
    while cur <= N:
        # 지워지 수를 카운트한다.
        if visit[cur] == 0:
            cnt +=1
            visit[cur] = cnt

        cnt1 += 1
        cur = i * cnt1
    
for i in range(2, N+1):
    if visit[i] == K:
        print(i)