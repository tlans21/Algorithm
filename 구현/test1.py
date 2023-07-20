lst = ['a', 'e', 'i', 'o', 'u']

input_str = input()
for i in range(len(input_str)):

    if input_str[i:i+3] in lst:
        print('yes')
