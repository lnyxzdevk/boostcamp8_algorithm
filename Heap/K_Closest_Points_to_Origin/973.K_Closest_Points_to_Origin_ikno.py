import heapq
import math
class Solution:
    def __init__(self):
        self.q=[]
        self.result=[]
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for p in points:
            heapq.heappush(self.q,(self.distance(p),p[0],p[1]))
        for _ in range(k):
            _,x,y=heapq.heappop(self.q)
            self.result.append([x,y])
        return self.result
    def distance(self,p):
        return p[0]*p[0]+p[1]*p[1]