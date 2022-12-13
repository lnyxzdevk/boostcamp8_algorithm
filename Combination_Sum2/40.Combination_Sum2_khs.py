class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        def dfs(start, subset):
            if sum(subset) == target :
                answer.append(subset[:])
                return

            if sum(subset) > target:
                return
            
            for i in range(start, len(candidates)):
                if candidates[i-1] == candidates[i] and i > start:
                    continue

                subset.append(candidates[i])
                dfs(i+1, subset)
                subset.pop()

        dfs(0, [])
        return answer
