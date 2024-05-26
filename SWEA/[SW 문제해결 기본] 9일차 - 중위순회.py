T = 10

def in_order(n):
    global answer

    if n > N:
        return
    in_order(n * 2)
    answer += tree[n]
    in_order(n * 2 + 1)


for tc in range(1, T+1):
    N = int(input())
    answer = ""
    tree = [i for i in range(N+1)]
    for i in range(1, N+1):
        temp = list(map(str, input().split()))
        tree[i] = temp[1]
    
    in_order(1)
    print("#{} {}".format(tc, answer))


    

        

