class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def BT(tmp):
            if len(tmp) == len(nums):
                results.append(tmp)
            else:
                for i in nums:
                    if i not in tmp:
                        BT(tmp+[i])
        BT([])
        return results