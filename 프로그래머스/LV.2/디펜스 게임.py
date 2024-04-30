import heapq
def solution(n, k, enemys):
    answer = 0
    # heapq 사용
    heap = []
    sum_value = 0
    for enemy in enemys:
        heapq.heappush(heap, -enemy)
        sum_value += enemy
        
        if sum_value > n:
            if k == 0:
                return answer
            # 최댓값 빼기 연산. (-로 들어있음.)
            sum_value += heapq.heappop(heap) 
            k -= 1
        answer += 1

    return answer