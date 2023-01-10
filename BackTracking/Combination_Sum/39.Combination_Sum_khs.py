from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        length = len(candidates)
        def dfs(start, subset, target):
            if sum(subset) == target:
                results.append(subset[:])
                return

            elif sum(subset) > target:
                return
            
            for i in range(start, length):
                subset.append(candidates[i])
                dfs(i, subset, target)
                subset.pop()

        dfs(0, [], target)
        return results