class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        종료조건 : depth? x -> 이번엔 depth 는 중복으로 뽑을 수 있기에 무의미하다 그러면, sum 이 target 보다 크면? return 을 하는건 어떨까.
        """
        result = []
        candidates.sort()
        def BT(i,tmp):
            if sum(tmp) == target :
                result.append(tmp)
                return
            elif sum(tmp) > target :
                return
            else:
                for k in range(i,len(candidates)):
                    BT(k,tmp+[candidates[k]])
        BT(0,[])
        return result