from copy import deepcopy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result, subset = [], []

        def dfs(i, subset):
            if i == len(nums):
                subset = sorted(subset)
                if subset not in result:
                    print(subset)
                    result.append(deepcopy(subset))
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)
        
        dfs(0, subset)
        return result
