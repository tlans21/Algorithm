N = int(input())
home = list(map(int, input().split()))
home = sorted(home)
answer = 123456789
idx = 0

def binary_search(left, right):
    global answer
    global idx

    if left > right:
        return
  
    point = 0
    mid = (left + right) // 2
    


    binary_search(mid+1, right)
    binary_search(left, mid-1)


binary_search(home[0], home[len(home) - 1])

print(idx)





