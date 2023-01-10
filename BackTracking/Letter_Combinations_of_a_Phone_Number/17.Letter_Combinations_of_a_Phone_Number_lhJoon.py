class Solution:
    def __init__(self):
        self.map = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        if not digits :
            return [] 
        def dfs(i,string):
            if i == len(digits):
                results.append(string)
                return
            for idx in range(len(self.map[int(digits[i])])):
                dfs(i+1,string+self.map[int(digits[i])][idx])
        dfs(0,"")
        return results