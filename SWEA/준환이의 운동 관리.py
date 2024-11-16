T = int(input())

for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    # L분 이상 U분 이하의 운동 X는 운동 시간
    if L <= X <= U:
        print("#{} {}".format(tc, 0))
    elif X > U:
        print("#{} {}".format(tc, -1))
    elif X < L:
        print("#{} {}".format(tc, L-X))
    

