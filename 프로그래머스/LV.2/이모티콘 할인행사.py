from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    # 가입자수를 높이기 위해서는 할인율을 최소한으로 해야한다.
    # 할인율로 인한 손실을 최대한 막기 위해 이모티콘 가격이 낮은순으로 정렬
    emoticon = sorted(emoticons)
    # 10퍼 부터 시작
    ratio = [10, 20, 30, 40]
    prod_list = list(product(ratio, repeat=len(emoticons)))
    
    final_price = 0
    max_sum = 0
    
    for discounts in prod_list:
        plus = 0
        total_sum = 0
        for user in users:
            user_sum = 0
            user_ratio, user_price = user[0], user[1]
            for idx, value in enumerate(discounts):
                if value >= user_ratio: 
                    user_sum += emoticons[idx] * (100 - value) / 100
                
            if user_price > user_sum:
                total_sum += user_sum
            else:
                plus += 1
        
        answer = max(answer, [plus, total_sum])
            
    return answer