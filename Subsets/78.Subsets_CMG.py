from copy import deepcopy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,3] -> [1,2] -> [1,3] -> [1] -> [2,3] -> [2] ->[3] -> []
        '''
        result, subset = [], []

        def dfs(i):
            if i == len(nums):
                result.append(deepcopy(subset))
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result
