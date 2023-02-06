from itertools import product

def solution(users, emoticons):
    cases = product([10, 20, 30, 40], repeat=len(emoticons))
    best_plus_user = 0
    best_money = 0
    for case in cases:
        plus_user = 0
        money = 0
        for user in users:
            th_discount, th_buy = user
            
            buy = sum([price * (100-case[i]) // 100 
                       for i, price in enumerate(emoticons) 
                        if th_discount <= case[i]])
            if buy >= th_buy:
                plus_user += 1
            else:
                money += buy
                
        if best_plus_user < plus_user:
            best_plus_user = plus_user
            best_money = money
        elif best_plus_user == plus_user and best_money < money:
            best_money = money
    return [best_plus_user, best_money]
