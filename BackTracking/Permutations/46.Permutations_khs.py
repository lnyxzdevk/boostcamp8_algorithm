from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        length = len(nums)
        def dfs(subset):
            if len(subset) == length:
                results.append(subset[:])

            for n in nums:
                if n not in subset:
                    subset.append(n)
                    dfs(subset)
                    subset.pop()

        dfs([])

        return results


sol = Solution()
print(sol.permute([1,2,3]))

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]