def solution(users, emoticons):
    discount = [10 ,20, 30, 40]
    dis_list = []
    def dfs(tmp, depth):
        if depth == len(emoticons):
            dis_list.append(tmp[:])
            return
        for d in discount:
            tmp.append(d)
            dfs(tmp, depth + 1)
            tmp.pop()
    
    dfs([], 0)
    """
    dfs(0,0) -> tmp =[10,0...] -> tmp[10,10...10] -> tmp[10,10...0] ->tmp[10,...20] -> 10,,,30 -> 10,,,40 -> 10,,,,20,20 -> 30
    """
    best_plus_user = 0
    best_money = 0
    for case in dis_list:
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
