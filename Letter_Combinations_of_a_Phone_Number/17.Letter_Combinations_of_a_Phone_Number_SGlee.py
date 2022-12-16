from collections import deque
class Solution:
    def dfs(self, substring, res_digits):
        if not res_digits:
            self.answer.append(substring)
            return 
        num = int(res_digits[0])
        for alphabet in self.digit_map[num]:
            self.dfs(substring + alphabet, res_digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.answer = []
        self.digit_map = dict()
        for i in range(2, 7):
            self.digit_map[i] = [chr(ord('a') + 3*i+ j - 6) for j in range(3)]
        self.digit_map[7] = ['p', 'q', 'r', 's']
        self.digit_map[8] = ['t', 'u', 'v']
        self.digit_map[9] = ['w', 'x', 'y', 'z']
        
        self.dfs("", digits)
        return self.answer
