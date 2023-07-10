from collections import deque
input_str = input()
queue = deque()
stack = []
flag = False
temp = ""
for i in range(0, len(input_str)):
    if input_str[i] == '<':
        while len(stack) != 0:
            temp += stack.pop()

        flag = True
        temp += '<'
    elif input_str[i] == '>':
        flag = False
        temp += '>'
    elif input_str[i] == ' ':
        while len(stack) != 0:
            temp += stack.pop()
        temp += ' '
        continue
    elif flag == True:
        temp += input_str[i]
    elif flag == False:
        stack.append(input_str[i])

while len(stack) != 0:
    temp += stack.pop()

print(temp)