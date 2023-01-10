class Solution:
    def __init__(self):
        self.directs=[[0,1],[1,0],[0,-1],[-1,0]]
    def numIslands(self, grid: List[List[str]]) -> int:
        answer=0
        TF=[[False]*len(grid[0]) for _ in range(len(grid))]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if TF[x][y]==False and grid[x][y]=='1':
                    self.dfs(x,y,grid,TF)                    
                    answer+=1
        return answer
    def dfs(self,x,y,grid,TF):
        if TF[x][y]==True:
            return
        TF[x][y]=True
        for dx,dy in self.directs:
            if x+dx>=0 and x+dx<len(grid) and y+dy>=0 and y+dy<len(grid[0]):
                if grid[x+dx][y+dy]=='1':
                    self.dfs(x+dx,y+dy,grid,TF)
