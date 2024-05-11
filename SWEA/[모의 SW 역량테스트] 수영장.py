
def dfs(idx, plan, prices, depth, sum):
    global min_price

    if sum > min_price:
        return

    if idx >= 12:
        if min_price >= sum:
            min_price = sum
        return
    
    for i in range(0, 4):
        if plan[idx]:
            if i == 0:
                dfs(idx + 1, plan, prices, depth + 1, sum + prices[i] * plan[idx])
            elif i == 1:
                dfs(idx + 1, plan, prices, depth + 1, sum + prices[i])
            elif i == 2:
                dfs(idx + 3, plan, prices, depth + 1, sum + prices[i])
            elif i == 3:
                dfs(idx + 12, plan, prices, depth + 1, sum + prices[i])
        else:
            dfs(idx + 1, plan, prices, depth + 1, sum)
T = int(input())

for i in range(1, T+1):
    prices = list(map(int, input().split()))
    # 1일, 1달, 3달, 1년
    plan = list(map(int, input().split()))
    min_price = 9999999999
    dfs(0, plan, prices, 0, 0)
    print('#{} {}'.format(i, min_price))
    