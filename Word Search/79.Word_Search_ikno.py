class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        words=''
        result=[]
        setboard=set()
        for i in board:
            for j in i:
                setboard.add(j)
        for w in word:
            if w not in setboard:
                return False 
        newboard=[[0 for _ in range(len(board[0])) ] for _ in range(len(board))]
        def dfs(x,y,length,words):
            if length>len(word):
                return
            if board[x][y]==word[length]:
                length+=1
                words+=board[x][y]
            else:
                return
            if words==word:
                result.append('true')
                return True
            for i in range(len(dx)):
                x+=dx[i]
                y+=dy[i]                
                if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                    x-=dx[i]
                    y-=dy[i]
                    continue
                if newboard[x][y]==1:
                    x-=dx[i]
                    y-=dy[i]
                    continue
                newboard[x][y]=1
                dfs(x,y,length,words)
                newboard[x][y]=0
                x-=dx[i]
                y-=dy[i]
        for x in range(len(board)):
            for y in range(0,len(board[0])):
                newboard[x][y]=1
                dfs(x,y,0,'')
                newboard[x][y]=0
        if result!=[]:
            return True
        else:
            return False