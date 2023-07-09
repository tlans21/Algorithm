N = int(input())

num_list = list(map(int, input().split()))

arr = []

arr.sort(key = lambda x: (x[0], x[1]))