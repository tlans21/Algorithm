T = int(input())

# 101000 -> 000000 -> 111111 -> 100000-> 101111-> 101000
# 000000
for tc in range(1, T+1):
    answer = 0
    memory = input()
    n = ['0']*len(memory)
    for i in range(len(memory)):
        if n[i] != memory[i]:
            n[i:] = memory[i] * len(n[i:])
            answer +=1
    print("#{} {}".format(tc, answer))


