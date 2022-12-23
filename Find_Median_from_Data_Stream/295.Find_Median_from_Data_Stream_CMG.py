class MedianFinder:

    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        self.lst.append(num)
        
    def findMedian(self) -> float:
        self.lst.sort()

        mid = len(self.lst) // 2

        if len(self.lst) % 2 == 0:
            return (self.lst[mid-1] + self.lst[mid]) / 2
        else:
            return self.lst[mid]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
