K = int(input())
lst = []
gap_list = []

for i in range(K):
    lst = list(map(int, input().split(' ')))
    grade_list = lst[1:]
    grade_list.sort()
    gap_list = []

    for j in range(lst[0]-1):
        gap = abs(grade_list[j] - grade_list[j+1])
        
        gap_list.append(gap)
    
    print(f'Class {i+1}')
    print(f'Max {max(grade_list)}, Min {min(grade_list)}, Largest gap {max(gap_list)}')

