input_str = input()

stack = []

cnt = 1
answer = 0
for i in range(0, len(input_str)):
    if input_str[i] == '(':
        cnt *=2
        stack.append(input_str[i])
    elif input_str[i] == '[':
        cnt *=3
        stack.append(input_str[i])
    elif input_str[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        elif input_str[i-1] == '(':
            answer +=cnt
        cnt //=2
        stack.pop()
    elif input_str[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        elif input_str[i-1] == '[':
            answer += cnt
        cnt //=3
        stack.pop()

if answer == 0 or stack:
    print(0)
else:
    print(answer)

