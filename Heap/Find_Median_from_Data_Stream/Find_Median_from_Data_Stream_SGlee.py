
"""
1. minheap, max heap을 만든다.
2. minheap에 상위 50%, max heap에 하위 50% 값을 추가한다.
3. minheap과 maxheap 크기가 균형을 이루도록 조정한다.
4. median값은 minheap과 maxheap의 0번째 원소를 참조해 계산한다.
"""
import heapq as hq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        # heap에 아무것도 없는 경우
        if not self.maxheap and not self.minheap: 
            hq.heappush(self.minheap, num)
        # minheap에 넣을 경우   
        elif self.minheap[0] <= num: 
            hq.heappush(self.minheap, num)
            # dual heap 균형이 깨진 경우
            if len(self.minheap) > len(self.maxheap) + 1:
                out = hq.heappop(self.minheap)
                hq.heappush(self.maxheap, (-out, out))
        # maxheap에 넣을 경우        
        else: 
            hq.heappush(self.maxheap, (-num, num))
            # dual heap 균형이 깨진 경우
            if len(self.maxheap) > len(self.minheap) + 1:
                _, out = hq.heappop(self.maxheap)
                hq.heappush(self.minheap, out)
            

    def findMedian(self) -> float:
        # print('min', self.minheap)
        # print('max', self.maxheap)
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + self.maxheap[0][1]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return self.maxheap[0][1]    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
