import heapq
def solution(n, k, enemy):
    answer = 0
    total=0
    #제일 큰거 담는 heap
    heap = []
    for i in enemy:
        total += i
        if total <=n :
            heapq.heappush(heap,-i)
            answer += 1
        elif k >0 :
            heapq.heappush(heap,-i)
            total += heapq.heappop(heap)
            answer += 1
            k -= 1
        else:
            break
    return answer