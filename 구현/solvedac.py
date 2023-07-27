# 의견이 없다면 0, 의견이 하나라도 존재한다면 모든 사람의 난이도 의견의 절사평균  30퍼로 결정

#절사평균 : 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것
# 30프로 절사평균은 15% 위, 15% 아래를 각각 제외
import sys
input = sys.stdin.readline


def round2(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
N = int(input())

if N == 0:
    print(0)
    exit(0)

grade = []

for i in range(N):
    grade.append(int(input()))


# 1 5 5 7 8
grade.sort()

percent = N * 0.15

cnt = round2(percent)

# 최솟값 제거

start = cnt
last = len(grade) - cnt
answer = round2(sum(grade[start:last]) / (len(grade) - (2*cnt)))

print(answer)






