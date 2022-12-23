class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0
    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.length += 1
        
    def findMedian(self) -> float:

        self.nums.sort()
        mid = self.length//2
        if self.length == 0 :
            return None
        if self.length == 1:
            return self.nums[0]
        if self.length%2 == 0:
            return ((self.nums[mid]+self.nums[mid-1])/2)
        return self.nums[mid]
