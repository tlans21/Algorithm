# 첫번째 시도 코드(87.5 / 100.0)
def solution(plans):
    answer = []
    # 1.1새로운 과제 시작시간이 되었을 때, 진행중이던 과제 멈추고 새로운 과제 시작
    # 진행중이던 과제 끝났고, 만약에 if 멈춘 과제가 존재한다면 멈춘 과제를 이어서 진행한다.
    # 만약에, 과제를 멈춘 시각에서 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 있다면 새로 시작해야하는 과제 우선으로 한다.
    # 멈춰둔 과제가 여러개 존재시, 최근을 우선으로 처리한다.
    
    # 시간순 정렬
    plans = sorted(plans, key = lambda x: x[1])
    stopPlans = []
    for idx in range(len(plans)):
        
        # 현재 idx
        name = plans[idx][0]
        start = plans[idx][1] # ex 11:40 -> 11 * 60 + 40
        playtime = int(plans[idx][2]) 
        
        start = int(start[0:2]) * 60 + int(start[3:5])
        
        # 마지막 순번 제외
        if idx < len(plans) - 1:
            nextTime = plans[idx + 1][1]
            nextTime = int(nextTime[0:2]) * 60 + int(nextTime[3:5])
        elif idx == len(plans) - 1:
            nextTime = 123456789

        # 진행중이던 과제를 끝냈을때,
        if (start + playtime) <= nextTime:
            answer.append(name)
            # 진행중인 과제가 끝난 시각과 새로운 과제가 시작하는 시간이 같다면 남아있는 과제가 있어도 새로운 과제를 진행
            if start + playtime == nextTime:
                continue

            curTime = start + playtime # 해당 조건에서의 현재 시간
            while stopPlans:
                # 가장 최근에 멈춘 과제 순서부터 시작.
                stopName, stopPlaytime = stopPlans.pop()

                # 남아있는 과제를 진행하다가 새로운 과제를 해야할 시간이 올때 종료해야함.
                if curTime + stopPlaytime >= nextTime:
                    stopPlan = [stopName, stopPlaytime - (nextTime - curTime)]
                    stopPlans.append(stopPlan)
                    break
                else:
                    answer.append(stopName)
                    curTime += stopPlaytime

        # # 진행중이던 과제를 끝내지 못했을때
        else:
            #기존 과제를 stopPlan에 넣는다.
            remainTime = playtime - (nextTime - start)
            stopPlan = [name, remainTime] #이름, 잔여 시간
            stopPlans.append(stopPlan)
    
    
    print(answer)                
    return answer


# 두번째 시도 코드(100.0 / 100.0)
def solution(plans):
    answer = []
    # 1.1새로운 과제 시작시간이 되었을 때, 진행중이던 과제 멈추고 새로운 과제 시작
    # 진행중이던 과제 끝났고, 만약에 if 멈춘 과제가 존재한다면 멈춘 과제를 이어서 진행한다.
    # 만약에, 과제를 멈춘 시각에서 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 있다면 새로 시작해야하는 과제 우선으로 한다.
    # 멈춰둔 과제가 여러개 존재시, 최근을 우선으로 처리한다.
    
    # 시간순 정렬
    plans = sorted(plans, key = lambda x: x[1])
    stopPlans = []
    for idx in range(len(plans)):
        
        # 현재 idx
        name = plans[idx][0]
        start = plans[idx][1] # ex 11:40 -> 11 * 60 + 40
        playtime = int(plans[idx][2]) 
        
        start = int(start[0:2]) * 60 + int(start[3:5])
        
        # 마지막 순번 제외
        if idx < len(plans) - 1:
            nextTime = plans[idx + 1][1]
            nextTime = int(nextTime[0:2]) * 60 + int(nextTime[3:5])
        elif idx == len(plans) - 1:
            nextTime = 123456789

        # 진행중이던 과제를 끝냈을때,
        if (start + playtime) <= nextTime:
            answer.append(name)
            # 진행중인 과제가 끝난 시각과 새로운 과제가 시작하는 시간이 같다면 남아있는 과제가 있어도 새로운 과제를 진행
            if start + playtime == nextTime:
                continue

            curTime = start + playtime # 해당 조건에서의 현재 시간
            while stopPlans:
                # 가장 최근에 멈춘 과제 순서부터 시작.
                stopName, stopPlaytime = stopPlans.pop()

                # 남아있는 과제를 진행하다가 새로운 과제를 해야할 시간이 올때 종료해야함.
                if curTime + stopPlaytime > nextTime: # 틀린부분 >= 가 아닌 >이다. 남은 과제를 완료한 시간과 새로운 과제의 시간이 같으면 이는 완료를 한 것이므로 다시 넣을 필요가 없기 때문이다.
                    stopPlan = [stopName, stopPlaytime - (nextTime - curTime)]
                    stopPlans.append(stopPlan)
                    break
                else:
                    answer.append(stopName)
                    curTime += stopPlaytime

        # # 진행중이던 과제를 끝내지 못했을때
        else:
            #기존 과제를 stopPlan에 넣는다.
            remainTime = playtime - (nextTime - start)
            stopPlan = [name, remainTime] #이름, 잔여 시간
            stopPlans.append(stopPlan)
    
    
    print(answer)                
    return answer



