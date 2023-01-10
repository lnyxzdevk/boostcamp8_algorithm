from collections import defaultdict

class Solution:
    def dfs(self, out, x, y): 
        
        # append row
        out.append(self.batch[y])
        # find answer
        if x == self.n - 1:
            self.answer.append(out.copy())
            out.pop()
            return
        # next candidate
        c_x = x + 1
        self.y_check[y] = True
        for n_y in range(y + 1, self.n): # ↗    
            dx = abs(n_y - y)
            if x + dx >= self.n:
                break
            self.pos_check[(x + dx, n_y)] += 1
        for n_y in range(y - 1, -1, -1): # ↘
            dx = abs(n_y - y)
            if x + dx >= self.n:
                break
            self.pos_check[(x + dx, n_y)] += 1

        # dfs
        for c_y in range(self.n):
            if not self.y_check[c_y] and not self.pos_check[(c_x, c_y)]:
                self.dfs(out, c_x, c_y)
        # back
        self.y_check[y] = False
        for n_y in range(y + 1, self.n): # ↗
            dx = abs(n_y - y)
            if x + dx >= self.n:
                break
            self.pos_check[(x + dx, n_y)] -= 1
        for n_y in range(y - 1, -1, -1): # ↘
            dx = abs(n_y - y)
            if x + dx >= self.n:
                break
            self.pos_check[(x + dx, n_y)] -= 1
        out.pop()


        
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.answer = []
        self.y_check = defaultdict(int)
        self.pos_check = defaultdict(int)
        self.batch = [''.join(['Q' if i==j else '.' for i in range(n)]) for j in range(n)]
        for y in range(n):
                self.dfs([], 0, y)

        return self.answer
