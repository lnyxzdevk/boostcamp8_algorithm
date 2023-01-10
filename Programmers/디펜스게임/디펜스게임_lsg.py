import heapq as hq

def solution(n, k, enemy):
    def check(k, n, e):
        while k:
            _, max_e = hq.heappop(maxheap)
            n += max_e
            k -= 1
            if n >= e:
                n -= e
                return True, k, n
        return False, k, n

    maxheap = []
    for ans, e in enumerate(enemy):
        hq.heappush(maxheap, (-e, e))
        if n >= e:
            n -= e
        else:
            flag, k, n = check(k, n, e)
            if not flag:
                break
    else:
        return len(enemy)   
    
    return ans
