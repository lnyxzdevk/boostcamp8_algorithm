class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def dfs(i, j):
            if i < 0  or i >=  len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            grid[i][j] = '0'

            for x in range(4):
                dfs(i + dx[x], j + dy[x])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    island += 1
        
        return island
