def in_order(value):
    
    if not tree[value]: # 자식이 없으면
        return int(oper[value])
    
    left = in_order(tree[value][0])
    right = in_order(tree[value][1])

    if oper[value] == '-':
        return left - right
    elif oper[value] == '+':
        return left + right
    elif oper[value] == '*':
        return left * right
    else:
        return left / right


T = 10

for tc in range(1, T + 1):
    N = int(input())
    answer = ""
    tree = {i: [] for i in range(1, N+1)}
    oper = {i: "" for i in range(1, N+1)}
    for i in range(1, N+1):
        temp = list(map(str, input().split()))
        oper[int(temp[0])] = temp[1]

        if len(temp) == 3:
            tree[int(temp[0])] += [int(temp[2])]
        elif len(temp) == 4:
            tree[int(temp[0])] += [int(temp[2])]
            tree[int(temp[0])] += [int(temp[3])]
    
    result = int(in_order(1))

    print("#{} {}".format(tc, result))
    


