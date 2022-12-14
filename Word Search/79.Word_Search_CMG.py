class Solution:
    flag = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, num, visited):
            if num == len(word):
                self.flag = True
                return
            
            for n in range(4):
                x, y = i + dy[n], j + dx[n]

                if x < 0 or y < 0 or x >= h or y >= w or visited[x][y]:
                    continue
                
                if board[x][y] == word[num]:
                    visited[x][y] = True
                    dfs(x, y, num + 1, visited)
                    visited[x][y] = False
        num = 0
        w, h = len(board[0]), len(board)

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0 ,0]

        visited = [[False for _ in range(w)] for _ in range(h)]

        

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    dfs(i, j, 1, visited)
                    if self.flag:
                        return True
                    visited[i][j] = False
        
        return False
