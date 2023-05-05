N = int(input())

data = []
for i in range(N):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

    # 1.국어 내림차순
    # 2. 국어 점수가 같을시 영어점수 오름차순
    # 3.  국어 점수와 영어점수가 같으면 수학점수 내림차순
    # 4. 모든 점수 같을시 이름이 오름차순

data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for students in data:
    print(students[0])
