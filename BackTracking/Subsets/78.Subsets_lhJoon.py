class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        nums : [1,2,3]
        tmp : []
        length : 0
        
              i=0    i=1      i=2     i=3 : len(nums)                                              i=3 : len(nums)
        [] -> [1] -> [1,2] -> [1,2,3] -> results.append([1,2,3]) -> return -> BT(i:2,tmp:[1,2]) -> results.append([1,2]) -> ...
        """
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
