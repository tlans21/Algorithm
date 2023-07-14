from collections import deque
# n개의 트럭이 건너가려고함

n, w, L = map(int, input().split())

trucks = list(map(int, input().split()))

bridge = [0] * w

# 다리에는 w대의 트럭만 동시에 올라갈 수 있음.

#다리의 길이는 w 단위 길이
#하나의 단위시간에 하나의 단위 길이만큼 이동한다고 가정
# 동시에 다리위에 올라가 있는 트럭들의 합은 다리의 최대하중인 L보다 작아야함

bridge_weight = 0

cnt = 0
while True:
    out = bridge.pop(0)
    bridge_weight -= out
    if trucks:
        if bridge_weight + trucks[0] <= L:
            bridge_weight += trucks[0]
            truck = trucks.pop(0)
            bridge.append(truck)
            
        else:
            bridge.append(0)
    cnt +=1

    if len(bridge) == 0:
        break

print(cnt)
        


