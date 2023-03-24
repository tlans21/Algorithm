#달팽이는 올라가고 싶다 2869번 1추라이
 
a,b,v = map(int,input().split()) # A,B,V출력

#초깃값 
day = 0
high = 0

while True:
    day += 1
    high += a
    if high == v: # >=로 변환 햇움 왜냐면 같을떄만 멈추게 해서 오류임 ㅋ

        print(day)
        break

        
    high -= b



import math         

#2 츄라이 
a,b,v = map(int,input().split())

day = 0
high = 0

 #남은 길이 v-a
 # #하루동안 올라가는 길이 a-b

day = (v-a) / (a-b)
print(math.floor(day))

#3츄라이 

a,b,v = map(int,input().split())

day = 0
high = 0

 #남은 길이 v-a
 # #하루동안 올라가는 길이 a-b

day = (v-b)/(a-b) # v일떄 낮에 올라갓다가 밤에 내려오는 경우 --- v-b로 바꿔주기(하루 밤이 지난 경우) 
print(math.ceil(day))
