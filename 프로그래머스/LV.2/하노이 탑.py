def hanoi(N, start, end, via):
    global answer
    if N == 1:
        answer.append([start, end])
    else:
        hanoi(N-1, start, via, end)
        answer.append([start, end])
        hanoi(N-1, via, end, start)

    
def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 3, 2)
    
    return answer