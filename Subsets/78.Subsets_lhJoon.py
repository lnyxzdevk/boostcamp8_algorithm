class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def BT(length,tmp):
            if length == len(nums):
                results.append(tmp)
                return 
            else:
                BT(length+1,tmp+[nums[length]])
                BT(length+1,tmp)
        BT(0,[])
        return results