import heapq

def solution(n, k, enemy):
    heap = []
    answer = 0
    
    for e in enemy:
        if n >= e:
            heapq.heappush(heap, -e)
            n -= e
        
        elif k:
            k -= 1
            max_e = heapq.heappushpop(heap, -e)
            n -= (max_e + e)
        else:
            break
        
        answer += 1
    return answer
