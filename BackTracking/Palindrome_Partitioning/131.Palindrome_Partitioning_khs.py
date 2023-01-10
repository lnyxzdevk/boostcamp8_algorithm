class Solution:
    def partition(self, s):
        results = []
        
        def dfs(start, subword):
                
            if start >= len(s):
                results.append(subword[:])
                return
                
            for i in range(start, len(s)):
                tmp = s[start: i+1]
                subword.append(tmp)
                if tmp == tmp[::-1]:
                    dfs(i+1, subword)
                subword.pop()
                        
        dfs(0, [])
        
        return results
