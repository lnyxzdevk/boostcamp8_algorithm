class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_to_letter = {"2":'abc', "3":'def', "4":'ghi', "5":'jkl', "6":'mno', "7":'pqrs', "8":'tuv', "9":'wxyz'}
        digits = [num_to_letter[d] for d in digits]
        results = []
        
        def dfs(depth, subword):
            if len(subword) == len(digits):
                results.append(subword[:])
                return
            
            for j in range(len(digits[depth+1])):
                subword += digits[depth+1][j]
                dfs(depth+1, subword)
                subword = subword[:-1]
        
        for i in range(len(digits[0])):
            dfs(0, digits[0][i])
            
        return results
