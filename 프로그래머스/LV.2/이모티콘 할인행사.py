from itertools import product
def solution(users, emoticons):
    answer = []
    # 가입자수를 높이기 위해서는 할인율을 최소한으로 해야한다.
    # 할인율로 인한 손실을 최대한 막기 위해 이모티콘 가격이 낮은순으로 정렬
    emoticon = sorted(emoticons)
    # 10퍼 부터 시작
    ratio = [10, 20, 30, 40]
    prod_list = list(product(ratio, repeat=len(emoticons)))
    
    plus = 0
    final_price = 0
    
    for user in users:
        user_ratio, user_price = user[0], user[1]
        for prod in prod_list:
            sum = 0
            breakPoint = False
            for idx, value in enumerate(prod):
                # 할인율에 부합하지 않으므로 continue
                if value < user_ratio:
                    continue
                # 계속 더하기    
                if sum < user_price:
                    sum += emoticons[idx] * ((100 - value) / 100)
                else:
                    # 가격을 넘었으니 플러스 구매
                    breakPoint = True
                    plus += 1
                    break
            else:
                print(sum)
                final_price += sum
                
                
            if breakPoint == True:
                break
            
    answer.append(plus)
    answer.append(final_price)
                
    return answer