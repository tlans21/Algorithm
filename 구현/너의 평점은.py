def convert(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0
sum_num = 0
sum_score = 0
for i in range(20):
    title, num, grade = input().split()
    
    if grade == 'P':
        continue

    num1 = float(num)
    sum_num += num1
    num2 = convert(grade)
    
    socore = num1 * num2
    sum_score += socore


print(sum_score / sum_num)
