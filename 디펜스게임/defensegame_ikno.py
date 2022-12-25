import heapq
def solution(n, k, enemy):
    result=0
    heap=[]
    for ene in enemy:
        if n>= ene:
            heapq.heappush(heap,-ene)
            n=n-ene
        else:
            if k>0:
                k-=1
                if heap==[]:
                    result+=1
                    continue
                maxene=heapq.heappop(heap)
                if (-maxene)>ene:
                    n=n-maxene
                    n=n-ene
                    heapq.heappush(heap,-ene)
                else:
                    heapq.heappush(heap,maxene)
                    pass
            else:
                break
        result+=1

    return result