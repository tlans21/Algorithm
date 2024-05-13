T = 10

for tc in range(1, T+1):
    num = int(input())
    answer = 0
    targetString = input()
    str_input = input()

    convert_str = str_input.replace(targetString, '^')
   
    for str_element in convert_str:
        if str_element == '^':
            answer += 1
    
    print("#{} {}".format(num, answer))

# 다른 풀이

for _ in range(10) :
    T = int(input())
    string = input()
    sentence = input()

    count = sentence.count(string)
    print("#{} {}".format(T, count))