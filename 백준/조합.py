combi = [1, 2, 3]
lst = []

def dfs(start, depth):
    if depth == 2:
        print(lst)
        return
    
    for i in range(start, len(combi)):
        lst.append(combi[i])
        dfs(i + 1, depth + 1)  # start를 i + 1로 변경하여 중복 방지
        lst.pop()

dfs(0, 0)

# 