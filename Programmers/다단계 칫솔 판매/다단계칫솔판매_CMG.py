from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    dic = defaultdict()
    
    for idx, e in enumerate(enroll):
        dic[e] = idx

    for s, a in zip(seller, amount):
        earn = 100 * a
        
        while s != '-' and earn > 0:
            idx = dic[s]
            answer[idx] += earn - earn // 10
            earn //= 10
            s = referral[idx]
    
    return answer
        
