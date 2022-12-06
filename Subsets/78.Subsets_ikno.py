from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #nP3
        output=[[]]
        lennum=len(nums)
        for i in range(1,lennum+1):
            cnums=combinations(nums,i)
            cnums=list(cnums)
            for c in cnums:
                output.append(list(c))
        return output