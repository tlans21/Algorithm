def dfs(depth):
    global answer
    if changeCount == depth:
        answer = max(answer, int("".join(numbers)))
        return

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i] # 교환
            
            check_number = int(''.join(numbers)) # 교환된 숫자 만들기
            
            if (check_number, depth) not in visited:
                visited.append((check_number, depth)) # 현재 깊이와 교환 숫자 넣기
                dfs(depth + 1) # 교환 후 깊이 진행
            numbers[i], numbers[j] = numbers[j], numbers[i] # 다시 백트레킹으로 되돌리기
    


T = int(input())
for tc in range(1, T + 1):
    answer = 0
    visited = []
    numbers, changeCount = map(int, input().split())
    numbers = list(str(numbers))
    # dfs를 이용하여 모든 경우의 수를 생각
    # dfs 의 깊이는 changeCount로 생각
    dfs(0)
    print("#{} {}".format(tc, answer))
