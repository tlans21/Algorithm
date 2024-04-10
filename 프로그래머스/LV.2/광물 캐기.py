
def solution(picks, minerals):
    answer = []
    
    def dfs(picks, minerals, value):
        if sum(picks) == 0 or minerals == []:
            answer.append(value)

        # 가능한 곡괭이 확인하기
        can = []
        # 5개 미네랄 확인
        can_minerals = minerals[:5]
        graph = [[1, 1, 1],
                 [5, 1, 1],
                 [25, 5, 1]]

        dict_mineral = {"diamond" : 0, "iron" : 1, "stone" : 2}
        for idx, pick in enumerate(picks):
            v = 0
            if pick == 0:
                continue
            # 5번 캐기
            for can_mineral in can_minerals:
                v += graph[idx][dict_mineral[can_mineral]]
            # 횟수 감소
            picks[idx] -= 1
            dfs(picks, minerals[5:], value + v)
            
            for can_mineral in can_minerals:
                v -= graph[idx][dict_mineral[can_mineral]]
            picks[idx] += 1
    
    dfs(picks, minerals, 0)
    return min(answer)