
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset=[]
        result=[]
        candidates.sort()
        def dfs(candidates,subset,numsum,target):
            for candidate in candidates:
                if numsum+candidate>target:
                    break
                elif numsum+candidate==target:
                    subset.append(candidate)
                    sortli=sorted(subset)
                    if sortli in result:
                        subset.pop()
                        continue
                    copysub=subset[:]
                    result.append(copysub)
                    subset.pop()
                else:
                    subset.append(candidate)
                    numsum+=candidate
                    dfs(candidates,subset,numsum,target)
                    numsum-=candidate
                    subset.pop()
        dfs(candidates,subset,0,target)
        return result