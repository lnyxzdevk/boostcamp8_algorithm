
class Solution:
    def get_dist(self, point):
        return point[0]**2 + point[1]**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest = sorted([(self.get_dist(p), p) for p in points])[:k]
        return list(map(lambda x: x[1], k_closest))
