from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split()) # 해당 테스트 케이스의 재료의 수 : N, 제한 칼로리 : L
    kit = [list(map(int ,input().split())) for _ in range(N)] # 점수와 칼로리
    max_score = - 1
    for i in range(1, N+1):
        combination = list(combinations(kit, i))
        
        for combi in combination:
            score = 0
            calory = 0
            for combi_element in combi:
                score += combi_element[0]
                calory += combi_element[1]
            if calory <= L :
                max_score = max(score, max_score)
    
    print("#{} {}".format(tc, max_score))

    