T = 10
for tc in range(1, T+1):
    N = int(input())
    secret = list(map(int, input().split()))
    M = int(input())
    command = list(map(str, input().split()))


    for i in range(0, len(command)):
        
        if command[i] == 'I':
            x = int(command[i+1])
            y = int(command[i+2])
            for j in range(y):
                secretNumber = int(command[i+3+j])
                secret.insert(x+j, secretNumber)
        elif command[i] == 'D':
            x = int(command[i+1])
            y = int(command[i+2])
            del secret[x:x+y+1]
        elif command[i] == 'A':
            y = int(command[i+1])
            for j in range(1, y+1):
                s = int(command[i+1+j])                
                secret.append(s)
    print("#{} {}".format(tc, " ".join(map(str, secret))))