from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, subset):
            tmp = sum(subset)
            
            if tmp == target:
                result.append(deepcopy(subset))
                return
            elif tmp > target:
                return
            
            for i in range(idx, len(candidates)):
                subset.append(candidates[i])
                dfs(i, subset)
                subset.pop()
        
        dfs(0, [])

        return result
