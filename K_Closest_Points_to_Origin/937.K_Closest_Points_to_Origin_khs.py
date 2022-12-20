import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_points = [((point[0]**2) + (point[1]**2), i) for i,point in enumerate(points)]
        heapq.heapify(distance_points)
        answer = []
        
        for _ in range(k):
            closet_point = heapq.heappop(distance_points)
            answer.append(points[closet_point[1]])

        return answer
