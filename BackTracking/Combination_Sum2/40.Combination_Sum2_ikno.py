class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        summ=0
        result=[]
        def dfs(length,subset,summ,a):

            if target==summ:
                result.append(subset[:])
            if length>len(candidates):
                return
            for i in range(a,len(candidates)):
                summ+=candidates[i]
                if i>a and candidates[i]==candidates[i-1]:
                    summ-=candidates[i]
                    continue
                if summ>target:
                    break
                elif summ<=target:
                    length+=1
                    subset.append(candidates[i])
                    dfs(length,subset,summ,i+1)
                    subset.pop()
                    length-=1
                summ-=candidates[i]
            return 
        dfs(0,[],0,0)
        return result