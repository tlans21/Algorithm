N, M = map(int, (input().split()))

if N == 1:
    print(1)
elif N == 2:
    print(min((M+1)//2, 4))
elif M < 7 :
    print(min(M, 4))
else:
    print(M-7+5)
