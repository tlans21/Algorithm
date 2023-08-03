
def move_right(gear_num, pre_dir, temp):
    
    if gear_num == 4:
        return


    if gear[gear_num][2] == gear[gear_num + 1][6]:
        return
    temp[gear_num + 1] = (-1) * pre_dir
    move_right(gear_num + 1, temp[gear_num + 1], temp)

def move_left(gear_num, pre_dir, temp):

    if gear_num == 1:
        return
    

    if gear[gear_num][6] == gear[gear_num - 1][2]:
        return
    
    temp[gear_num - 1] = (-1) * pre_dir
    move_left(gear_num - 1, temp[gear_num - 1], temp)



gear = [[]]

a = list(map(int, list(str(input().rstrip()))))
b = list(map(int, list(str(input().rstrip()))))
c = list(map(int, list(str(input().rstrip()))))
d = list(map(int, list(str(input().rstrip()))))

gear.append(a)
gear.append(b)
gear.append(c)
gear.append(d)


rotation = int(input())

answer = 0
for i in range(rotation):
    gear_num, dir = map(int, input().split())
    # False의 의미는 극이 서로 다르다는 뜻
    temp = [0] * 5
    temp[gear_num] = dir

    if gear_num > 1:
        move_left(gear_num, dir, temp)
    if gear_num < 4:
        move_right(gear_num, dir, temp)
    for j in range(1, 5):
        if temp[j] == -1:
            gear_pop = gear[j].pop(0)
            gear[j].append(gear_pop)
        elif temp[j] == 1:
            gear_pop = gear[j].pop()
            gear[j].insert(0, gear_pop)
answer = 0
for i in range(1, 5):
    if gear[i][0] == 1:
        answer += pow(2, i-1)
        

print(answer)
    

    # 극이 같다면 gear_num 인덱스의 기어는 회전을 하지않는다.
    
   

    

        
        
            
