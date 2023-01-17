def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()
    while pickups and pickups[-1] == 0:
        pickups.pop()        
    
    while deliveries or pickups:     
        # 뭐가 더 먼가
        max_distance = max(len(deliveries), len(pickups))
        answer += 2 * max_distance
        current_cap = cap
        # 배달 시작
        while current_cap >= 0 and deliveries:
            if current_cap >= deliveries[-1]:
                current_cap -= deliveries.pop()
            else:
                deliveries[-1] -= current_cap
                current_cap = 0
                break
        # 배달끝
        # 수거 시작
        current_cap = cap
        while current_cap >= 0 and pickups:
            if current_cap >= pickups[-1]:
                current_cap -= pickups.pop()
            else:
                pickups[-1] -= current_cap
                current_cap = 0
                break
        # 수거 끝     
    return answer
