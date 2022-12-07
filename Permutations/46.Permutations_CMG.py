class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(perm):
            if len(perm) == len(nums):
                result.append(perm)
                return
            
            for num in nums:
                if num not in perm:
                    dfs(perm+[num])
        
        dfs([])
        return result
