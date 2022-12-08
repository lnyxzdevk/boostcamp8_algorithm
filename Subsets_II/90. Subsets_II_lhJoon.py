class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results=[]
        def BT(i,tmp):
            if i == len(nums):
                tmp.sort()
                if tmp not in results:
                    results.append(tmp)
                return
            BT(i+1,tmp+[nums[i]])
            BT(i+1,tmp)
        BT(0,[])
        return results