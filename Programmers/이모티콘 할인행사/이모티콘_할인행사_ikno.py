from itertools import product
def solution(users, emoticons):
    
    maxpeople=0
    maxmoney=0
    saleslist=[10,20,30,40]
    len_emoticons=len(emoticons)
    purchase_user=[0]*len(users)
    t=product(saleslist, repeat=len_emoticons)
    for emo in t:
        for j in range(len(emo)):
            for k in range(len(users)):
                if users[k][0]<=emo[j]:
                    purchase_user[k]+=((100-emo[j])*emoticons[j])/100
        
        pluspeople=0
        money=0
        for t in range(len(purchase_user)):
            if users[t][1]<=purchase_user[t]:
                pluspeople+=1
            else:
                money+=purchase_user[t]
        if maxpeople<pluspeople:
            maxmoney=money
            maxpeople=pluspeople
        elif maxpeople==pluspeople:
            if maxmoney<money:
                maxmoney=money
        else:
            pass
        purchase_user=[0]*len(users)
    answer = [maxpeople,maxmoney]
    return answer