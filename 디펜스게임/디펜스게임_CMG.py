import heapq

def solution(n, k, enemy):
    heap = []
    total, answer = 0, 0
    
    for e in enemy:
        total += e
        
        if total <= n:
            heapq.heappush(heap, -e)
            answer += 1
        elif k > 0:
            k -= 1
            total += heapq.heappushpop(heap, -e)
            answer += 1
        else:
            break
    
    return answer
            
