def solution(enroll, referral, seller, amount):
    referral_dict={}
    result_dict={}
    profit=100
    
    for i in zip(enroll,referral):
        referral_dict[i[0]]=i[1]
    for en in enroll:
        result_dict[en]=0
    
    for i in range(len(seller)):
        money=amount[i]*profit
        sel=seller[i]
        while True:
            result_dict[sel]+=(money-int(0.1*money))
            money=int(0.1*money)           
            if money<1:
                break
            if referral_dict[sel]=='-':
                break
            else:
                sel=referral_dict[sel]
    result=[]
    for en in enroll:
        result.append(result_dict[en])
    

    return result