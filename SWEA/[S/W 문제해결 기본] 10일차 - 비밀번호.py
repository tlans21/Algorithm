T = 10

for tc in range(1, T+1):
    N, password = map(str, input().split())
    N = int(N)
    i = 0

    while True:
        if i == len(password) - 1:
            break

        if password[i] == password[i+1]:
            password = password[:i] + password[i+2:]
              
            i = -1 
        i += 1
    print("#{} {}".format(tc, password))