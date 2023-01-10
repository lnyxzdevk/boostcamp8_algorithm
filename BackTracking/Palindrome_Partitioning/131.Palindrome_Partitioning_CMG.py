class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, subset = [], []
        def check(string):
            return string == string[::-1]
        
        def dfs(num):
            if num == len(s):
                result.append(subset[:])
                return
            
            for i in range(num, len(s)):
                print(s[num:i+1])
                if check(s[num:i+1]):
                    subset.append(s[num:i+1])
                    dfs(i+1)
                    subset.pop()
        
        dfs(0)

        return result
