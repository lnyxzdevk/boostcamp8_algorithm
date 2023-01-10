class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        result = []
        
        def dfs(i, candi):
            if len(candi) == len(digits):
                if len(digits) != 0:
                    result.append(candi)
                return
            
            for letter in phone[digits[i]]:
                dfs(i + 1, candi + letter)

        dfs(0 , '')
        
        return result
