class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        종료조건 : depth? x -> 이번엔 depth 는 중복으로 뽑을 수 있기에 무의미하다 그러면, sum 이 target 보다 크면? return 을 하는건 어떨까.
        중복은 어떻게 나타내줄까 : for 문을 돌리면서 인자를 i 로 설정하고 계속 같은 i 를 넣어준다 -> 가장 작은 수로 그것보다 커지거나 같아 질때까지! 그때 이후로 다음 인덱스의 수를 더해주는거지.
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
