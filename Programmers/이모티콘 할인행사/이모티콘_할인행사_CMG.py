from itertools import product

def solution(users, emoticons):
    percentage = [10, 20, 30, 40]
    discountsList = product(percentage, repeat=len(emoticons))
    answer = [0, 0]
    
    for discounts in discountsList:
        tmp = [0, 0]
        for userDiscount, userMoney in users:
            profit = 0
            for emoticon, discount in zip(emoticons, discounts):
                if discount >= userDiscount:
                    profit += emoticon * (1 - discount/100)
        
            if profit >= userMoney:
                tmp[0] += 1
            else:
                tmp[1] += profit
        answer = max(answer, tmp, key=lambda x:(x[0], x[1]))
    return answer
