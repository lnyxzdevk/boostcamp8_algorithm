class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def dfs(nums,subset,order):
            if subset in result: ## 빼야한다
                return
            result.append(subset[:])
            if len(subset)==len(nums):
                return
            for i in range(order,len(nums)):#여기서 num[i]==num[i-1] 조건문 사용시 
                subset.append(nums[i]) 
                dfs(nums,subset,i+1)
                subset.pop()
        dfs(nums,[],0)
        return result