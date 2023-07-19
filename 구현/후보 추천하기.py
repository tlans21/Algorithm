N = int(input())
K = int(input())

window = []
human = list(map(int, input().split()))
cnt_list = []

for i in range(K):

    if human[i] in window:
        #window의 길이만큼 검사
        for j in range(len(window)):
            #찾은 경우 추천수 증가
            if window[j] == human[i]:
                cnt_list[j] += 1
                break
    else:
        if len(window) < N:
            window.append(human[i])
            cnt_list.append(1)
        else:
            #추천 수 최소를 찾아야함.
            for j in range(N):
                if min(cnt_list) == cnt_list[j]:
                    del cnt_list[j]
                    del window[j]
                    break
            window.append(human[i])
            cnt_list.append(1)
window.sort()

for i in range(len(window)):
    print(window[i], end=' ')







    