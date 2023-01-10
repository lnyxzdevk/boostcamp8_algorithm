class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dirnum={
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
            }
        result=[]
        
        def dfs(length,digits,subset):
            if length==len(digits):
                return
            for i in dirnum[digits[length]]:
                subset.append(i)
                if length==len(digits)-1:
                    st=''.join(subset)
                    result.append(st)
                dfs(length+1,digits,subset)
                subset.pop()
            return 
        dfs(0,digits,[])
        return result