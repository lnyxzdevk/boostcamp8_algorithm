import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[] 
        result =[]

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, [dist, x, y])

        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
        
        return result