def dfs(depth):
    global answer
    if depth == changeNumber:
        answer = max(answer, int(''.join(numbers)))
        return
     
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i] # 값 바꾸기

            numbers_check = int(''.join(numbers))
            if (numbers_check, depth) not in visited:
                visited.append((numbers_check, depth))
                dfs(depth + 1)
                
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for tc in range(1, T + 1):
    answer = 0
    numbers, changeNumber = map(int, input().split())
    numbers = list(str(numbers))
    visited = []

    dfs(0)
    print("#{} {}".format(tc, answer))