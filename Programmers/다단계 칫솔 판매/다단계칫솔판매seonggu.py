from collections import defaultdict

def solution(enroll, referral, seller, amount):
    referral_dict = dict()
    revenue = defaultdict(int)
    for i, e in enumerate(enroll):
        referral_dict[e] = referral[i]

    for i, s in enumerate(seller):
        money = amount[i] * 100
        while money >= 1 and s != '-':
            next_money = money // 10
            revenue[s] += money - next_money
            s = referral_dict[s]
            money = next_money
    
    answer = []
    for e in enroll:
        answer.append(revenue[e])
    return answer
